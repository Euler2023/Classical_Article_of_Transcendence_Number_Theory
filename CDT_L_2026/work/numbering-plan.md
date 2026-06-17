# Numbering Plan

This report documents the numbering system of the original paper `CDT_L_2026` for Section 1, and details the necessary LaTeX counter configurations.

## Numbering System Classification

- **Theorem-like objects (Main results)**: Alphabet-based global numbering (`Theorem A`, `Corollary B`, `Theorem C`).
- **Theorem-like objects (Ordinary results)**: Subsection-based numbering reset at the subsection level (`Lemma 1.2.1`, `Lemma 1.2.3`, `Theorem 1.2.4`).
- **Equations**: Subsection-based or section-based numbering. Let's check:
  - Equation (1.1.1): Subsection 1.1, equation 1.
  - Equation (1.1.2): Subsection 1.1, equation 2.
  - Equation (1.2.2): Subsection 1.2, equation 2.
  - Equation (1.2.8): Subsection 1.2, equation 8.
  So equations are subsection-based!

## LaTeX Counter Configuration

To match this numbering system perfectly, we will introduce:

1. **Main results (Alphabet-based)**:
   ```latex
   \newtheorem{maintheorem}{Theorem}
   \renewcommand{\themaintheorem}{\Alph{maintheorem}}
   \newtheorem{maincorollary}[maintheorem]{Corollary}
   \providecommand*{\maintheoremautorefname}{定理}
   \providecommand*{\maincorollaryautorefname}{推论}
   ```
   This ensures:
   - `\begin{maintheorem}` -> Theorem A (first)
   - `\begin{maincorollary}` -> Corollary B (second, shared counter)
   - `\begin{maintheorem}` -> Theorem C (third, shared counter)

2. **Ordinary theorem-like environments**:
   Configure theorem-like environments to reset at the `subsection` level:
   ```latex
   \newtheorem{theorem}{Theorem}[subsection]
   \newtheorem{proposition}[theorem]{Proposition}
   \newtheorem{lemma}[theorem]{Lemma}
   \newtheorem{corollary}[theorem]{Corollary}
   \newtheorem{conjecture}[theorem]{Conjecture}
   \newtheorem{definition}[theorem]{Definition}
   \newtheorem{example}[theorem]{Example}
   \newtheorem{notation}[theorem]{Notation}
   \newtheorem{question}[theorem]{Question}
   \newtheorem{remark}[theorem]{Remark}
   ```
   Since `lemma`, `theorem`, `corollary`, etc. share the `theorem` counter which is bound to `[subsection]`, they will naturally be numbered as `1.2.1`, `1.2.2`, `1.2.3`, `1.2.4`, etc.

3. **Equations**:
   We will bind equations to subsections:
   ```latex
   \numberwithin{equation}{subsection}
   ```

## Rendered Numbering Verification Plan

During the compile check phase, we will systematically verify the PDF page output against this ledger:
- Page 3: `Theorem A` must render as **定理 A**
- Page 4: `Equation (1.1.2)` must render as **(1.1.2)**
- Page 4: `Corollary B` must render as **推论 B**
- Page 4: `Theorem C` must render as **定理 C**
- Page 5: `Lemma 1.2.1` must render as **引理 1.2.1**
- Page 5: `Equation (1.2.2)` must render as **(1.2.2)**
- Page 7: `Lemma 1.2.3` must render as **引理 1.2.3**
- Page 7: `Theorem 1.2.4` must render as **定理 1.2.4**
- Page 9: `Equation (1.2.8)` must render as **(1.2.8)**
