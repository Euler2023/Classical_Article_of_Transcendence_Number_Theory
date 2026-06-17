# Source Ledger - Siegel's Transcendental Numbers

This ledger maps the structure and elements of Carl Ludwig Siegel's *Transcendental Numbers*, based on the proofread English Markdown sources in `input/siegel/by_chapter/`.

## 1. Document Structure & Baselines
* **Source Basename**: `siegel`
* **Template**: Qbook (Siegel) template (`template/Siegel/`)
* **Output Path**: `output/siegel/`
* **Translation Scope**: Preface + Chapter I + Chapter II + Bibliography

## 2. Chapters & Sections Map

| Section | Heading | Source File | Kept? | Type |
| :--- | :--- | :--- | :--- | :--- |
| **Front** | Preface (Carl Ludwig Siegel, April 1949) | `template/Siegel/tex/preface.tex` | Yes | Preface |
| **Ch. I** | **CHAPTER I: THE EXPONENTIAL FUNCTION** | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Chapter |
| I.§1 | The irrationality of $e$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§2 | The operator $f(D)$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§3 | Approximation to $e^x$ by rational functions | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§4 | The irrationality of $e^a$ for rational $a \neq 0$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§5 | The irrationality of $\pi$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§6 | The irrationality of $\tan a$ for rational $a \ne 0$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§7 | The function $P_1 e^{\rho_1 X} + \dots + P_m e^{\rho_m X}$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§8 | Estimation of $R(1)$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§9 | Estimation of $P_k(1)$ and its denominator | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§10 | The transcendency of $e^a$ for real algebraic $a \neq 0$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§11 | The determinant of m approximation forms | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§12 | Algebraic independence | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§13 | Another expression for the remainder term $R(x)$ | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§14 | The interpolation formula | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| I.§15 | Concluding remarks | `CHAPTER I THE EXPONENTIAL FUNCTION.md` | Yes | Section |
| **Ch. II** | **CHAPTER II: SOLUTIONS OF LINEAR DIFFERENTIAL EQUATIONS** | `CHAPTER II SOLUTIONS OF LINEAR DIFFERENTIAL EQUATIONS.md` | Yes | Chapter |
| II.§1 | Functions of type E | `CHAPTER II SOLUTIONS OF LINEAR DIFFERENTIAL EQUATIONS.md` | Yes | Section |
| II.§2 | Arithmetical lemmas | `CHAPTER II SOLUTIONS OF LINEAR DIFFERENTIAL EQUATIONS.md` | Yes | Section |
| **Ch. III** | **CHAPTER III: THE TRANSCENDENCY OF $a^b$** | `CHAPTER III THE TRANSCENDENCY OF $a^b$.md` | Yes | Chapter |
| III.§1 | Schneider's proof | `CHAPTER III THE TRANSCENDENCY OF $a^b$.md` | Yes | Section |
| III.§2 | Gelfond's proof | `CHAPTER III THE TRANSCENDENCY OF $a^b$.md` | Yes | Section |
| **Ch. IV** | **CHAPTER IV: ELLIPTIC FUNCTIONS** | `CHAPTER IV ELLIPTIC FUNCTIONS.md` | Yes | Chapter |
| IV.§1 | Abelian differentials | `CHAPTER IV ELLIPTIC FUNCTIONS.md` | Yes | Section |
| IV.§2 | Elliptic integrals | `CHAPTER IV ELLIPTIC FUNCTIONS.md` | Yes | Section |
| IV.§3 | The approximation form | `CHAPTER IV ELLIPTIC FUNCTIONS.md` | Yes | Section |
| IV.§4 | Conclusion of the proof | `CHAPTER IV ELLIPTIC FUNCTIONS.md` | Yes | Section |
| IV.§5 | Some other results | `CHAPTER IV ELLIPTIC FUNCTIONS.md` | Yes | Section |
| **Back** | Bibliography | `template/Siegel/tex/ref.tex` | Yes | References |

## 3. Numbered Objects Count (Target Estimates)
* **Equations (Numbered)**:
  - Chapter I: Equations (1) to (46)
  - Chapter II: Equations (49) to (53)
  - Chapter III: Equations (110) to (111)
  - Chapter IV: Equations (120) to (127), and (129) to (136)
* **Theorems/Lemmas**:
  - Lemma 1 (Chapter II, §2)
  - Lemma 2 (Chapter II, §2)
  - Schneider's Theorem (Chapter IV, §2)
  - Schneider's Theorem on Elliptic Functions (Chapter IV, §5)
  - Schneider's Theorem on Abelian Integrals (Chapter IV, §5)
* **Other Environments**:
  - Custom remarks and concluding notes in all chapters.

## 4. Front/Back Matter Decision
* **Preface**: Kept (from `template/Siegel/tex/preface.tex`).
* **Table of Contents**: Kept.
* **Bibliography**: Kept (from `template/Siegel/tex/ref.tex`, cross-referenced in the text).
