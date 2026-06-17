import os
import re
from find_overfulls import parse_latex_log, get_context_from_file

def main():
    log_path = "CDT_L_2026_Chn.log"
    overfulls = parse_latex_log(log_path)
    
    unique_overfulls = []
    seen = set()
    for o in overfulls:
        f = o["file"]
        if f.startswith("./"):
            f = f[2:]
        key = (f, o["line_start"], o["line_end"], o["type"])
        if key not in seen:
            seen.add(key)
            o["file"] = f
            unique_overfulls.append(o)
            
    # Filter only display equation overfulls in tex/ files or CDT_L_2026_Chn.tex
    display_overfulls = [o for o in unique_overfulls if o["type"] == "display" and (o["file"].startswith("tex/") or o["file"] == "CDT_L_2026_Chn.tex")]
    
    print(f"Found {len(display_overfulls)} display equation overfulls in LaTeX source files:\n")
    
    for idx, w in enumerate(sorted(display_overfulls, key=lambda x: (x["file"], x["line_start"]))):
        print("=" * 80)
        print(f"({idx+1}) FILE: {w['file']} | Line {w['line_start']} | {w['pt']}pt too wide")
        print("=" * 80)
        context = get_context_from_file(w["file"], w["line_start"], w["line_end"], context=2)
        print(context)
        print("-" * 80)
        print()

if __name__ == "__main__":
    main()
