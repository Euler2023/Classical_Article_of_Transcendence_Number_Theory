import os
import re

def parse_log_for_overfulls(log_path):
    # Extracts all overfull display hboxes with their line number and pt width
    overfulls = []
    detected_line_re = re.compile(r'Overfull \\hbox \(([\d\.]+)pt too wide\) detected at line (\d+)')
    
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = detected_line_re.search(line)
            if m:
                pt = float(m.group(1))
                line_num = int(m.group(2))
                overfulls.append((pt, line_num))
    return sorted(list(set(overfulls)))

def find_math_at_line(filepath, line_num):
    # Returns the line content if it contains display math or a math environment
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    if len(lines) < line_num:
        return None
        
    # Check lines around line_num (from line_num-2 to line_num+2) for math content
    start = max(0, line_num - 3)
    end = min(len(lines), line_num + 2)
    chunk = lines[start:end]
    chunk_str = "".join(chunk)
    
    # Check if this chunk contains mathematical environments or display delimiters
    math_indicators = ["\\[", "\\]", "$$", "\\begin{equation}", "\\begin{align}", "\\begin{multline}", "\\begin{gather}", "\\begin{aligned}"]
    is_math = any(ind in chunk_str for ind in math_indicators) or ("=" in chunk_str and ("$" in chunk_str or "\\" in chunk_str))
    
    if is_math:
        # Return the exact line and its context
        return lines[line_num - 1].strip(), start, end, chunk
    return None

def main():
    log_path = "CDT_L_2026_Chn.log"
    print(f"Reading overfull display warnings from {log_path}...")
    overfull_items = parse_log_for_overfulls(log_path)
    print(f"Found {len(overfull_items)} overfull line warnings in log.\n")
    
    # Get all .tex files in tex/ and root
    tex_files = []
    for root, dirs, files in os.walk("."):
        # skip git, work, etc.
        if "work" in root or ".git" in root or ".claude" in root:
            continue
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(os.path.join(root, file))
                
    resolved = []
    unresolved = []
    
    for pt, line_num in overfull_items:
        matches = []
        for filepath in tex_files:
            res = find_math_at_line(filepath, line_num)
            if res:
                line_content, start_idx, end_idx, chunk = res
                matches.append((filepath, line_content, start_idx, end_idx, chunk))
                
        if len(matches) == 1:
            resolved.append((matches[0][0], line_num, pt, matches[0][1], matches[0][2], matches[0][3], matches[0][4]))
        elif len(matches) > 1:
            # Ambiguous match, we'll list them all
            print(f"Ambiguous match for line {line_num} ({pt}pt wide) in files: {[m[0] for m in matches]}")
            unresolved.append((line_num, pt, [m[0] for m in matches]))
        else:
            # Check if it was in the main file
            res_main = find_math_at_line("CDT_L_2026_Chn.tex", line_num)
            if res_main:
                resolved.append(("CDT_L_2026_Chn.tex", line_num, pt, res_main[0], res_main[1], res_main[2], res_main[3]))
            else:
                unresolved.append((line_num, pt, []))
                
    print(f"\nSuccessfully resolved {len(resolved)} overfull display equations:")
    print("=" * 100)
    
    for idx, (filepath, line, pt, content, start, end, chunk) in enumerate(sorted(resolved, key=lambda x: (x[0], x[1]))):
        print(f"({idx+1}) File: {filepath} | Line {line} | {pt}pt too wide")
        print("-" * 100)
        for i, l in enumerate(chunk):
            curr_line = start + i + 1
            marker = "->" if curr_line == line else "  "
            print(f"{curr_line:4d} {marker} {l.rstrip()}")
        print("=" * 100)
        
    if unresolved:
        print(f"\nCould not uniquely resolve {len(unresolved)} line numbers:")
        for line_num, pt, files in unresolved:
            print(f"  Line {line_num} ({pt}pt wide) - Candidate files: {files}")

if __name__ == "__main__":
    main()
