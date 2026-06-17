import os

candidates = {
    65: ["tex/sec5.tex", "tex/sec14.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec4.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/appB.tex", "tex/sec13.tex", "tex/appA.tex", "tex/sec10.tex", "tex/sec11.tex"],
    92: ["tex/sec5.tex", "tex/sec14.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec6.tex", "tex/appB.tex", "tex/sec13.tex", "tex/appA.tex", "tex/sec10.tex", "tex/sec11.tex"],
    113: ["tex/sec5.tex", "tex/sec14.tex", "tex/sec7.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/appB.tex", "tex/sec13.tex", "tex/appA.tex", "tex/sec10.tex", "tex/sec11.tex"],
    120: ["tex/sec5.tex", "tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/sec13.tex", "tex/appA.tex", "tex/sec10.tex", "tex/sec11.tex"],
    121: ["tex/sec5.tex", "tex/sec14.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/sec13.tex", "tex/appA.tex", "tex/sec10.tex", "tex/sec11.tex"],
    139: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/appB.tex", "tex/appA.tex", "tex/sec10.tex"],
    158: ["tex/sec7.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec12.tex", "tex/sec6.tex", "tex/appB.tex", "tex/sec10.tex", "tex/sec11.tex"],
    163: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec6.tex", "tex/appA.tex"],
    171: ["tex/sec14.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/appB.tex"],
    172: ["tex/sec14.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/appB.tex"],
    182: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/appB.tex", "tex/appA.tex"],
    187: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec12.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex", "tex/appA.tex"],
    198: ["tex/sec14.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec2.tex"],
    209: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec8.tex", "tex/sec2.tex", "tex/sec1.tex"],
    289: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec9.tex", "tex/sec2.tex", "tex/sec6.tex"],
    296: ["tex/sec14.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec2.tex", "tex/sec6.tex"],
    297: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec9.tex", "tex/sec2.tex", "tex/sec6.tex"],
    318: ["tex/sec3.tex", "tex/sec15.tex", "tex/sec9.tex", "tex/sec2.tex", "tex/sec1.tex", "tex/sec6.tex"],
    344: ["tex/sec14.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec2.tex"],
    357: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec3.tex", "tex/sec2.tex", "tex/sec6.tex"],
    372: ["tex/sec14.tex", "tex/sec3.tex", "tex/sec15.tex", "tex/sec8.tex", "tex/sec6.tex"],
    399: ["tex/sec7.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec2.tex", "tex/sec6.tex"],
    405: ["tex/sec14.tex", "tex/sec3.tex", "tex/sec8.tex", "tex/sec2.tex"],
    507: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec8.tex"],
    542: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    543: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    560: ["tex/sec14.tex", "tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    575: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    592: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    596: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    616: ["tex/sec8.tex", "tex/sec6.tex"],
    665: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    671: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    719: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    720: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    731: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    746: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    757: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    823: ["tex/sec7.tex", "tex/sec8.tex", "tex/sec6.tex"],
    837: ["tex/sec7.tex", "tex/sec8.tex"],
    843: ["tex/sec7.tex", "tex/sec8.tex"]
}

def print_line(filepath, line_num):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    if len(lines) >= line_num:
        # get 3 lines of context
        start = max(0, line_num - 2)
        end = min(len(lines), line_num + 1)
        res = []
        for i in range(start, end):
            prefix = "->" if i == line_num - 1 else "  "
            res.append(f"     {i+1:4d} {prefix} {lines[i].rstrip()}")
        return "\n".join(res)
    return None

for line, files in sorted(candidates.items()):
    print(f"================================================================================")
    print(f" LINE {line}")
    print(f"================================================================================")
    for f in files:
        res = print_line(f, line)
        if res:
            # Check if there is actual math in this range
            content = res.lower()
            if "\\" in content or "equation" in content or "align" in content or "\[" in content or "]" in content or "=" in content:
                print(f"  File: {f}")
                print(res)
                print("-" * 80)
