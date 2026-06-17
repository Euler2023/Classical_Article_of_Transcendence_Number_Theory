import re
import os

def trace_flow(filepath):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return
        
    print(f"Tracing numbering flow in {filepath}...")
    
    # We want to match:
    # \section{...}
    # \subsection{...}
    # \subsubsection{...}
    # \begin{equation}\label{...}
    # \begin{theorem}\label{...}
    # \begin{lemma}\label{...}
    # \begin{remark}\label{...}
    # \begin{definition}\label{...}
    # \begin{example}\label{...}
    # etc.
    
    pattern = re.compile(
        r'(\\section\{.*?\}|\\subsection\{.*?\}|\\subsubsection\{.*?\}|\\begin\{(?:equation|align|theorem|lemma|proposition|corollary|remark|definition|example|notation|question|conjecture)\}(?:\s*\\label\{(.*?)\})?)'
    )
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        for match in pattern.finditer(line):
            text = match.group(1)
            label = match.group(2) if len(match.groups()) > 1 else ""
            clean_text = text.replace('\n', ' ').strip()
            print(f"Line {i+1:4d}: {clean_text}")

if __name__ == "__main__":
    trace_flow("tex/sec7.tex")
