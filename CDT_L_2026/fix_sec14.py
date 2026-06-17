import os

filepath = "tex/sec14.tex"

replacements = [
    (
        r"\subsubsection{微分方程 \(\mathcal{L}(G_A) = 0\)}\label{sec:14.2}",
        r"\subsection{微分方程 \(\mathcal{L}(G_A) = 0\)}\label{sec:14.2}"
    ),
    (
        r"\subsubsection{纯函数以及源自 G 的函数的线性无关性}\label{sec:14.3}",
        r"\subsection{纯函数以及源自 G 的函数的线性无关性}\label{sec:14.3}"
    ),
    (
        r"\subsubsection{奇异点的位置}\label{sec:14.4}",
        r"\subsection{奇异点的位置}\label{sec:14.4}"
    ),
    (
        r"\subsubsection{定理 C 的证明}\label{sec:14.5}",
        r"\subsection{定理 C 的证明}\label{sec:14.5}"
    )
]

def apply_fixes():
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found!")
        return

    print(f"Modifying {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for idx, (old, new) in enumerate(replacements):
        if old in content:
            content = content.replace(old, new)
            print(f"  Successfully applied fix #{idx+2}")
            modified = True
        else:
            print(f"  Warning: Fix #{idx+2} not applied (text not found)!")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Done.")
    else:
        print("No changes were made.")

if __name__ == "__main__":
    apply_fixes()
