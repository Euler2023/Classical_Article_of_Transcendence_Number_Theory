import os
import re

def parse_latex_log(log_path):
    if not os.path.exists(log_path):
        print(f"Error: Log file not found at {log_path}")
        return []

    overfulls = []
    # Stack to track open files
    file_stack = ["CDT_L_2026_Chn.tex"]
    
    # We match things like (./tex/sec14.tex or (./CDT_L_2026_Chn.bbl
    # Also handle closing parenthesis )
    # Note: LaTeX log line wrapping can make this slightly challenging, but we can do a decent job.
    
    # Regexes for file tracking
    # Matches (./path/to/file.ext or (CDT_L_2026_Chn.aux
    file_open_re = re.compile(r'\(([^() \t\n\r]+\.(?:tex|aux|bbl|cls|sty|def|cfg|ldf|clo|toc))')
    
    # Regexes for overfull warnings
    # 1. Detected at line Y
    detected_line_re = re.compile(r'Overfull \\hbox \(([\d\.]+)pt too wide\) detected at line (\d+)')
    # 2. In paragraph at lines X--Y
    detected_para_re = re.compile(r'Overfull \\hbox \(([\d\.]+)pt too wide\) in paragraph at lines (\d+)--(\d+)')

    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Track active files using a simplified tokenizer for parenthesis
        # We also do a regex check on the raw line for file opens
        raw_line = lines[i]
        
        # Look for open files
        for match in file_open_re.finditer(raw_line):
            filepath = match.group(1)
            file_stack.append(filepath)
            
        # Look for closing parenthesis that signifies file close
        # Usually file closes look like ')' or ') (./nextfile.tex'
        # A simple check: if the raw line ends with ')\n' or has ')' followed by space or '('
        # Let's count how many closing parentheses are there compared to opening ones that are NOT file paths.
        # But to be robust, we can also use standard log tracking or look at the structure.
        # Let's count ')' on the line.
        close_count = raw_line.count(')')
        open_count = raw_line.count('(')
        # Only pop if there are more close parens than open parens
        if close_count > open_count:
            for _ in range(close_count - open_count):
                if len(file_stack) > 1:
                    file_stack.pop()

        # Check for overfull box warnings
        m1 = detected_line_re.search(raw_line)
        if m1:
            pt_wide = float(m1.group(1))
            line_num = int(m1.group(2))
            current_file = file_stack[-1] if file_stack else "unknown"
            overfulls.append({
                "type": "display",
                "file": current_file,
                "line_start": line_num,
                "line_end": line_num,
                "pt": pt_wide
            })
        else:
            m2 = detected_para_re.search(raw_line)
            if m2:
                pt_wide = float(m2.group(1))
                line_start = int(m2.group(2))
                line_end = int(m2.group(3))
                current_file = file_stack[-1] if file_stack else "unknown"
                overfulls.append({
                    "type": "paragraph",
                    "file": current_file,
                    "line_start": line_start,
                    "line_end": line_end,
                    "pt": pt_wide
                })
        i += 1

    return overfulls

def get_context_from_file(filepath, line_start, line_end, context=3):
    # Resolve relative path
    # If the log specifies ./tex/sec14.tex, we look for it
    real_path = filepath
    if filepath.startswith("./"):
        real_path = filepath[2:]
    
    if not os.path.exists(real_path):
        # Try prepending tex/ if file is secX.tex
        if os.path.exists(os.path.join("tex", real_path)):
            real_path = os.path.join("tex", real_path)
        else:
            return f"File {filepath} not found (tried {real_path})"

    with open(real_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    start_idx = max(0, line_start - 1 - context)
    end_idx = min(len(lines), line_end + context)
    
    context_lines = []
    for idx in range(start_idx, end_idx):
        line_num = idx + 1
        prefix = "-> " if line_start <= line_num <= line_end else "   "
        context_lines.append(f"{line_num:4d}{prefix}{lines[idx].rstrip()}")
        
    return "\n".join(context_lines)

def main():
    log_path = "CDT_L_2026_Chn.log"
    print(f"Parsing LaTeX log: {log_path}...")
    overfulls = parse_latex_log(log_path)
    
    # Filter out duplicate entries if any, and sort them
    unique_overfulls = []
    seen = set()
    for o in overfulls:
        # Normalize file path
        f = o["file"]
        if f.startswith("./"):
            f = f[2:]
        key = (f, o["line_start"], o["line_end"], o["type"])
        if key not in seen:
            seen.add(key)
            o["file"] = f
            unique_overfulls.append(o)
            
    print(f"Found {len(unique_overfulls)} unique Overfull \\hbox warnings.\n")
    
    # Group by file
    by_file = {}
    for o in unique_overfulls:
        by_file.setdefault(o["file"], []).append(o)
        
    for filename, warnings in sorted(by_file.items()):
        # Skip auxiliary or non-project files if any
        if not filename.endswith(".tex") and not filename.endswith(".bbl"):
            continue
        print("=" * 80)
        print(f" FILE: {filename} ({len(warnings)} warnings)")
        print("=" * 80)
        
        for idx, w in enumerate(warnings):
            print(f"\nWarning #{idx+1}: Type: {w['type']}, Width: {w['pt']}pt too wide")
            print(f"Lines: {w['line_start']} to {w['line_end']}")
            print("-" * 40)
            context = get_context_from_file(filename, w["line_start"], w["line_end"])
            print(context)
            print("-" * 40)

if __name__ == "__main__":
    main()
