import os
import re

def parse_log_for_overfulls(log_path):
    overfulls = []
    # Match Overfull \hbox (Xpt too wide) detected at line Y
    detected_line_re = re.compile(r'Overfull \\hbox \(([\d\.]+)pt too wide\) detected at line (\d+)')
    
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = detected_line_re.search(line)
            if m:
                pt = float(m.group(1))
                line_num = int(m.group(2))
                overfulls.append((pt, line_num))
    # Return unique items sorted by line number
    return sorted(list(set(overfulls)), key=lambda x: x[1])

def get_tex_files():
    tex_files = []
    for root, dirs, files in os.walk("."):
        if any(ignored in root for ignored in ["work", ".git", ".claude"]):
            continue
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(os.path.join(root, file))
    return tex_files

def resolve_overfull(pt, line_num, tex_files):
    candidates = []
    for filepath in tex_files:
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        if len(lines) < line_num:
            continue
            
        line_content = lines[line_num - 1]
        
        # We check if the line or its immediate neighbors contain math
        start_idx = max(0, line_num - 3)
        end_idx = min(len(lines), line_num + 2)
        context_str = "".join(lines[start_idx:end_idx])
        
        math_indicators = ["\\[", "\\]", "$$", "\\begin{", "\\end{", "\\tag", "\\label", "=", "+", "-", "\\sum", "\\int"]
        is_math = any(ind in context_str for ind in math_indicators)
        
        if is_math:
            candidates.append({
                "file": filepath,
                "line_len": len(line_content),
                "content": line_content.strip(),
                "context": lines[start_idx:end_idx],
                "start_line": start_idx + 1
            })
            
    if not candidates:
        return None
        
    # Sort candidates by line length of the target line, longest first
    candidates.sort(key=lambda x: x["line_len"], reverse=True)
    return candidates[0]

def main():
    log_path = "CDT_L_2026_Chn.log"
    print(f"Analyzing LaTeX log: {log_path}")
    overfull_items = parse_log_for_overfulls(log_path)
    print(f"Found {len(overfull_items)} overfull line warnings.\n")
    
    tex_files = get_tex_files()
    resolved_reports = []
    
    for pt, line_num in overfull_items:
        match = resolve_overfull(pt, line_num, tex_files)
        if match:
            resolved_reports.append({
                "file": match["file"],
                "line": line_num,
                "pt": pt,
                "content": match["content"],
                "context": match["context"],
                "start_line": match["start_line"]
            })
            
    # Write report to markdown file
    report_path = "overfull-report.md"
    print(f"Writing resolved report to {report_path}...")
    
    # Sort resolved reports by file, then by line number
    resolved_reports.sort(key=lambda x: (x["file"], x["line"]))
    
    # Filter duplicate reports (same file, same line)
    unique_reports = []
    seen = set()
    for r in resolved_reports:
        key = (r["file"], r["line"])
        if key not in seen:
            seen.add(key)
            unique_reports.append(r)
            
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Overfull Display Equations Report\n\n")
        f.write(f"This report lists all uniquely resolved display equations that exceed the text margin (total: {len(unique_reports)}).\n\n")
        
        current_file = None
        for idx, r in enumerate(unique_reports):
            if r["file"] != current_file:
                current_file = r["file"]
                f.write(f"\n## File: `{current_file}`\n\n")
                
            f.write(f"### Equation {idx+1} (Line {r['line']}) - **{r['pt']}pt too wide**\n\n")
            f.write("```latex\n")
            for i, line_text in enumerate(r["context"]):
                curr_num = r["start_line"] + i
                marker = "->" if curr_num == r["line"] else "  "
                f.write(f"{curr_num:4d} {marker} {line_text}")
            f.write("```\n\n")
            
    print(f"Report generated successfully. Found {len(unique_reports)} unique overfull equations.")

if __name__ == "__main__":
    main()
