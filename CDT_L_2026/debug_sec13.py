import re

filepath = "tex/sec13.tex"

pattern = re.compile(
    r'(\\section\{.*?\}|\\subsection\{.*?\}|\\subsubsection\{.*?\}|\\begin\{(?:equation|align|theorem|lemma|proposition|corollary|remark|definition|example|notation|question|conjecture|mylemma|mythm|mydef|figure|table)\}(?:\s*\\label\{(.*?)\})?)'
)

with open(filepath, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        for match in pattern.finditer(line):
            print(f"Line {i+1:4d}: {match.group(1)}")
