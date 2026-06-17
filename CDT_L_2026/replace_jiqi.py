import os
import re

def replace_jiqi():
    dirs_to_search = ['tex', '.']
    base_path = '.'
    
    # We are running this inside output/CDT_L_2026/ or root, let's auto-detect
    if os.path.exists('output/CDT_L_2026'):
        base_path = 'output/CDT_L_2026'
    
    print(f"Base path for replacement: {os.path.abspath(base_path)}")
    
    # We will search in base_path/tex/*.tex and base_path/*.tex
    files_to_process = []
    tex_dir = os.path.join(base_path, 'tex')
    if os.path.exists(tex_dir):
        for f in os.listdir(tex_dir):
            if f.endswith('.tex'):
                files_to_process.append(os.path.join(tex_dir, f))
                
    for f in os.listdir(base_path):
        if f.endswith('.tex'):
            files_to_process.append(os.path.join(base_path, f))
            
    print(f"Found {len(files_to_process)} TeX files to process.")
    
    for file_path in files_to_process:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Perform replacements
        # 1. "极其" -> "以及"
        if "极其" in content:
            # Let's count occurrences
            count = content.count("极其")
            patched = content.replace("极其", "以及")
            
            # Let's also clean up some specific common double-typos if any
            # "以及极其" -> "以及以及" -> "以及"
            patched = patched.replace("以及以及", "以及")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(patched)
            print(f"Patched {file_path}: replaced {count} occurrences of '极其' with '以及'.")

if __name__ == '__main__':
    replace_jiqi()
