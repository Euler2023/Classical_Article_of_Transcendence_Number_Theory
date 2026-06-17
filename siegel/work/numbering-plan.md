# Numbering Plan - Siegel's Transcendental Numbers

This plan defines the numbering scheme for chapters, sections, equations, and theorem-like environments in the Chinese translation of Carl Ludwig Siegel's *Transcendental Numbers*.

## 1. Chapter and Section Numbering
* **Chapter I**: 第一章 指数函数 (THE EXPONENTIAL FUNCTION)
* **Chapter II**: 第二章 线性微分方程的解 (SOLUTIONS OF LINEAR DIFFERENTIAL EQUATIONS)
* **Sections**: Numbered with section numbers like §1, §2, etc., following the book's classical format.

## 2. Equation Numbering Style
* **Source Style**: Global sequential numbering within each chapter (e.g., (1) to (46) in Ch. I, and (49) to (53) in Ch. II).
* **Implementation**: We will utilize LaTeX's `\tag{...}` macro for equations with specific numbers corresponding exactly to the source text. This matches the existing styling in the English template files and guarantees flawless numbering.
* **Equation References**: Managed via `\eqref{eq:label}`.

## 3. Lemmas & Theorems
* **Lemmas**:
  - Lemma 1 (Chapter II, §2) $\rightarrow$ **引理 1** (implemented using the template's standard `\begin{mylem} ... \end{mylem}` or similar theorem environments).
  - Lemma 2 (Chapter II, §2) $\rightarrow$ **引理 2**
* **Theorems/Propositions**: The main body proofs (such as Lindemann-Weierstrass Theorem in Ch. I, §12) are formulated inline or within unnumbered/numbered theorem blocks as in the original.

## 4. Other Environments
* **Remarks & Examples**: Will map to the template's `remark` and `example` environments.
