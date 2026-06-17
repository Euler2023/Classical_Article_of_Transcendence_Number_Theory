import os
import re

def replace_daggers(text):
    def repl(match):
        run = match.group(0)
        mapped = []
        for char in run:
            if char == '†':
                mapped.append('\\textdagger')
            elif char == '‡':
                mapped.append('\\textdoubledagger')
        return f"\\textsuperscript{{{''.join(mapped)}}}"
    
    return re.sub(r'[†‡]+', repl, text)

def process_tex_files():
    tex_dir = "/home/wlt2025/project/math/tools/dev_pdf_to_latex/output/trans_number_baker/tex"
    files = [f for f in os.listdir(tex_dir) if f.endswith('.tex')]
    
    for filename in sorted(files):
        filepath = os.path.join(tex_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified_content = replace_daggers(content)
        
        if modified_content != content:
            print(f"Modifying {filename}...")
            # Also print some preview of matches
            for line_no, (orig_line, new_line) in enumerate(zip(content.splitlines(), modified_content.splitlines()), 1):
                if orig_line != new_line:
                    print(f"  Line {line_no}:")
                    print(f"    - {orig_line.strip()}")
                    print(f"    + {new_line.strip()}")
                    
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        else:
            print(f"No daggers found in {filename}.")

if __name__ == "__main__":
    process_tex_files()
