# Alan Baker 《Transcendental Number Theory》 LaTeX 英文高保真重排执行方案

## 一、 项目概览与文件映射
- **目标书目**：Alan Baker, *Transcendental Number Theory* (Cambridge University Press, 1975)
- **绝对物理真值**：`input/trans_number_baker/trans_number_baker.pdf` 扫描版物理页面。
- **排版脚手架数据源**：`input/trans_number_baker/trans_number_baker.md` (包含 Marker 提取的未整理文本与部分初始公式)。
- **物理真值交叉引用大账本**：`output/trans_number_baker/reference-plan.json` (包含 1392 个潜在交叉引用候选，是高保真消歧与链接映射的绝对基础)。
- **输出工作区**：`output/trans_number_baker/`
- **主控入口文件**：`output/trans_number_baker/trans_number_baker.tex` (作为全局引导与 Preamble 定义)。

---

## 二、 模块化文件系统设计 (Modular File Layout)
为了实现高质量的可维护性，全书将严格采取**模块化多文件排版结构**。所有章节文件均存放在 `tex/` 目录下，由主入口文件进行 `\include` 或 `\input` 引导：

```text
output/trans_number_baker/
  ├── trans_number_baker.tex       ← 主控主 LaTeX 文件 (Preamble, TOC, Cover, Includes)
  ├── qbook.cls                    ← 适配全英文版的高级书籍排版类 (基于 template/Siegel/ 改造)
  ├── qbook.cfg                    ← 书籍宏包与格式配置
  ├── typesetting_plan.md          ← 本排版设计方案 (当前文档)
  ├── manifest.json                ← 排版对象数量审计清单 (机器可读物理实体校验网闸)
  ├── assets/                      ← 图片与静态资源
  │     └── fig/                   ← 保存原书配图（如 _page_2_Picture_3.jpeg）
  ├── bib/                         
  │     └── references.bib         ← 自动解析出的 BibTeX 经典数论文献数据库
  └── tex/                         ← 各章节模块化 LaTeX 源文件
        ├── preface.tex            ← 英文前言与格言引用 (Fermat, Euler, Lagrange, Gauss...)
        ├── chapter1.tex           ← Chapter 1: The origins (Liouville, Transcendence of e, Lindemann...)
        ├── chapter2.tex           ← Chapter 2: Linear forms in logarithms
        ├── ...                    
        ├── chapter12.tex          ← Chapter 12: Algebraic independence
        ├── original_papers.tex    ← Backmatter Appendix I: Original Papers (经典的学术文献目录)
        ├── further_publications.tex← Backmatter Appendix II: Further Publications (后期扩展增补论文列表)
        └── new_developments.tex   ← Backmatter Appendix III: New Developments (1990年增补数论新进展评注)
```

---

## 三、 TOC 与 Index (索引) 自动渲染策略
1. **TOC (目录)**：**完全不使用 Markdown 转换的静态目录表格。** 彻底舍弃原书静态目录，在 `frontmatter` 部分直接使用 LaTeX 的 `\tableofcontents`，由引擎动态根据实际页码进行计算和高保真排版。
2. **Index (索引)**：
   - **原书静态索引失效性（Static Index Invalidation）**：OCR 提取出的原书静态 Index (带有 1975 年原版物理页码) 会因为重新排版、行高间距紧缩、Baskerville 字体装载及 A4 布局重构而彻底失效。直接照搬会产生巨大的页码偏差与排版噪声。
   - **自动化动态索引策略（Automated Dynamic Indexing）**：
     - **底层配置**：在主 Preamble 中启用 `\usepackage{makeidx}` 与 `\makeindex`，并在书末通过 `\printindex` 渲染。
     - **正文动态锚点埋设（Dynamic Index Mapping）**：在各章节 TeX 编写过程中，凡遇核心学术人名、定理或专有名词，在正文紧邻位置实时埋设 `\index{...}` 锚点（例如排版 Liouville's theorem 时，写入 `\index{Liouville's theorem}`）。
     - **多级嵌套与规范化检索（Multi-level & Normalized Indexing）**：严格复原 Baker 原书索引的深度编目规范：
       - **多级检索**：使用 `!` 字符构建分层缩进的子索引大纲（例如 `\index{Equations!Thue}`、`\index{Equations!hyperelliptic}`）。
       - **人名规范化**：按照学术标准进行人名倒置与缩写（例如提到 Weierstrass 处，埋入 `\index{Weierstrass, K.}`）。
     - **全自动编译链路**：最终发布时，将执行完整的自动化索引编译链路：
       $$\text{XeLaTeX (1st Run)} \longrightarrow \text{MakeIndex (.idx} \to \text{.ind)} \longrightarrow \text{XeLaTeX (2nd Run)}$$
       这保证了在重排分页改变的情况下，索引中的页码 100% 实时准确对应最新的 PDF 物理页码，且在 PDF 中完全支持高亮度超链接跳转。
3. **Footnotes (脚注)**：
   - **符号按页重置（Page-by-page resetting without asterisks）**：原书采用这一独特的纯学术符号脚注计数，且彻底排除星号 `*`（防止与代数伴随算子或共轭混淆）。
   - **策略**：重构 `\@fnsymbol` 并通过 `footmisc` 强制按页在底部重置，符号直接从单剑号 `\dagger` 开始。
4. **字体提升与排版紧凑感（Typography & Compaction）**：
   - **Baskerville 黄金套装**：加载 `Baskervaldx`（高级 Baskerville 衬线体）配 `newtxmath`（Baskervaldx 数学子集），完全重现剑桥大学出版社 (CUP) 经典、饱满、高对比度的活字印刷字骨。
   - **紧密行间距（linespread=1.1）与舒适页边距（left/right=1.2in）**：完美适应西文排版信息密度，彻底收紧无谓空行，极大减少长公式越界溢出风险。

---

## 四、 核心排版元素与公式高保真修正 (Fidelity Correcting)
1. **定理盒化与引用保护 (Colorful tcolorbox & Referencing)**：
   原书中的所有 Theorem, Lemma, Definition 将全部重构为 Qbook 精致的英文 `tcolorbox` 彩色卡片环境，以达到高雅的现代出版美学：
   - **Theorems**：
     ```latex
     \begin{mythm}{Theorem Title}{thm:X_Y}
     Theorem content ...
     \end{mythm}
     ```
   - **Definitions**：
     ```latex
     \begin{mydef}{Definition Title}{def:X_Y}
     Definition content ...
     \end{mydef}
     ```
   - **Lemmas**：
     ```latex
     \begin{mylemma}{Lemma Title}{lem:X_Y}
     Lemma content ...
     \end{mylemma}
     ```
   - **自动化 Autoref 标志重构**：为了解决 LaTeX 中共享/派生计数器在 `\autoref` 引用下无法正确辨识 Theorem/Definition 的通病，我已在样式底层对 `\@ifundefined` 进行解构，使得对 `thm:` 标签的 `\autoref` 引用会自动高精度输出为 `Theorem X.Y`（例如 Theorem 1.4），完全告别了裸数字。
   - **Remarks & Examples**：使用英文 `\begin{remark} ... \end{remark}` 和带有 `\soln` 切分的 `\begin{example} ... \end{example}`。
   - **Proofs**：使用带有 `\qed` (优雅黑白墓碑符) 自动收尾的 `\begin{proof} ... \end{proof}` 环境。

2. **选择性公式编号（Selective Equation Numbering）与公式高保真排版**：
   - **原书无标号公式**：必须使用**无星号**的 LaTeX 独立公式环境 `\[ ... \]` 或者是 `equation*`、`align*` 环境，右侧不带任何自动编号。
   - **原书有标号公式**：必须使用带有 `\label` 的 `equation` 或 `align` 环境。通过 `\@addtoreset{equation}{chapter}` 排除公式编号中多余的 chapter 前缀（如展现为 `(1)` 而非 `(1.1)`），完美保持公式右侧计数与 1975 剑桥原版一致。
   - **避坑核心要点 (Anti-Drift Equation Counters)**：绝对禁止在非星号公式或对齐环境（如 `equation` 或 `align`）中写入硬编码的手动编号（如 `\qquad (70)`）。因为这会导致 LaTeX 在输出手动编号的同时，还自动在右端渲染 auto-counter 编号，造成恶劣的 `(70) (2.1)` 这种双重编号重叠灾难。自定义公式编号必须且只能采用 `\tag{...}\label{...}`。

3. **交叉引用保护 (Anti-Drift Referencing)**：
   - 彻底重构明文引用。公式、定理等在正文中统一使用 `\autoref` 或 `\eqref` 进行关联，防止页码微调时出现引用偏差。

4. **OCR 符号扰动校勘示例 (Fidelity Correcting Examples)**：
   我们在初步审查中捕捉到 Marker 提取产生的几类 OCR 符号扰动。在执行阶段，我们将通过并行的 Fidelity Check 逐页核对 PDF，对其进行数学逻辑和真值物理页面的严格校正。**以下为我们的修正对照：**

   | 典型 OCR 识别扰动 ( Scaffold ) | 校勘后的 LaTeX 高保真真值 ( Output ) | 说明 |
   | :--- | :--- | :--- |
   | `£ = £ 10~\* '•` | `$\xi = \sum_{n=1}^{\infty} 10^{-n!}$` | $\xi$ (Xi) 被误识别为英镑符 `£`，且级数上标错乱 |
   | `rational*p\q (q >* 0)` | `rational $p/q$ ($q > 0$)` | 混淆乘号与分式 |
   | `between *pjq* and a` | `between $p/q$ and $\alpha$` | 将希腊字母 $\alpha$ 混淆为普通 `a`，分式斜杠错识别 |
   | `| a - *p/q \ < I` | `$|\alpha - p/q| < 1$` | 纠正希腊字母与不等号噪声 |
   | `|P'(£)| < 1/c` | `$|P'(\xi)| < 1/c$` | 错别字纠正 |
   | `P(pjq) 4= 0` | `$P(p/q) \neq 0$` | 纠正不等号，原 OCR 将 `\neq` 错写为 `4=` |
   | `|£—*pn/qn\ < l/<fil<sup>n</sup> ,*` | `$|\xi - p_n/q_n| < 1/q_n^{\omega_n}$` | 纠正指数标签、希腊字母混淆与文本残留 |

---

## 五、 交叉引用精细化消歧与映射方案 (Cross-Referencing Mapping & Disambiguation)
根据 `reference-plan.json` 中抽取的 1392 个交叉引用候选分析，我们制定了极度精确的分类处理与语法消歧规约：

### 1. 括号包裹实体的三种数学消歧策略 (Disambiguating Parenthesized Entries)
OCR 识别到的类似 `(1)`, `(2)`, `(1844)` 的小括号文本，包含以下三种本质完全不同的实体，必须在 TeX 中实施隔离处理，严防将普通年份或数学公式自变量错误编译为公式链接：

* **A. 真实方程编号/方程引用 (Equations & References)**：
  * **真值判定**：指公式最右侧显示的序号，或者在正文句式中起引用作用的小括号数值。
  * **典型真值**：
    * 独立公式定义：`line 205: (1)`、`line 213: (3)`、`line 266: (4)`、`line 485: (5)`、`line 541: (7)`、`line 621: (9)`、`line 738: (10)`、`line 1119: (12)`、`line 1136: (13)`、`line 1630: (2)`。
    * 正文公式引用：`line 222: "From (1) and (3)"`、`line 266: "From (1) and (4)"`、`line 312: "From (1) and (5)"`、`line 470: "left-hand side of (3)"`、`line 499: "substituting from (2)"`、`line 510: "satisfied if (4)"`、`line 565: "defined by (6)"`、`line 584: "defined by (7)"`、`line 608: "by virtue of (8)"`、`line 713/742: "inequalities (9)"`、`line 738: "from (10)"`、`line 1164/1184: "left-hand side of (12)"`。
  * **TeX 语法映射**：定义处在公式块中加入 `\label{eq:chX_Y}`，正文引用处一律强制且仅能使用 `\eqref{eq:chX_Y}` 渲染（绝对不允许出现硬编码的 plain-text 括号 and 数字）。
* **B. 经典参考文献/脚注的出版年份 (Citation Years)**：
  * **真值判定**：原书脚注和附录中，附在期刊名、期刊卷号后面的出版年份。
  * **典型真值**：`line 152: (1844), (1851)`、`line 347/353/370/1238: (1929)`、`line 349/355: (1930)`、`line 351/353: (1934)`、`line 372/1719: (1966)`、`line 372: (1967)`、`line 376: (1941)`、`line 794: (1974)`、`line 798: (1972)`、`line 800/1765/1767: (1973)`、`line 826: (1953), (1964)`、`line 1380: (1926)`、`line 1382/1500/1518/1688: (1968)`。
  * **TeX 语法映射**：作为学术文献中不可或缺的出版时间戳，这些数字**绝对不能**用 `\eqref` 引用，更不能在公式块中设定 `\label`。它们必须作为普通数学文本 `$C.R.\ 18\ (1844),\ 883\text{--}5$` 或通过 `\cite` 映射进行渲染。
* **C. 纯数学公式内部自变量/阶数算子 (Mathematical Arguments)**：
  * **真值判定**：多项式函数、阶数导数或极限表达式中包含的自变量或下标，如 $f(l)$, $f^{(j)}(0)$, $(n!)^p$。
  * **典型真值**：`line 204/228/230/268/270: f^{(j)}(0), f^{(p-1)}(0)` 误匹配出的 `(0)`、`line 232/565/1035/1046: f(l)` 误匹配出的 `(1)`、`line 228/230: (n!)^p`。
  * **TeX 语法映射**：这些 is 公式文本，必须严格写入 LaTeX 数学模式中（如 `\(f^{(p-1)}(0)\)`），绝对不允许混淆为链接。

### 2. 定理与引理的高精度独立编号体系 (Theorem vs. Lemma Reset Rules)
通过对 `theorem-like` 分布大纲的细致分析，我们发现原书采取了一种极具学术考究的差异化编号体系：
* **Theorems (定理级实体)**：
  * **编号形态**：采用**跨章级双重编号**，如 `Theorem 1.1` (line 148)、`Theorem 1.2` (line 196)、`Theorem 2.1` (line 366)、`Theorem 3.1` (line 762)、`Theorem 4.1` (line 1246)、`Theorem 5.1` (line 1534)、`Theorem 6.1` (line 1784)。
  * **重置规约**：计数器按 Chapter 重置，`\thetheorem` 显示为 `\thechapter.\arabic{theorem}`。
* **Lemmas (引理级实体)**：
  * **编号形态**：采用**单章内纯粹自然数编号**，如 Chapter 2 中的 `Lemma 1` (line 457)、`Lemma 2` (line 472)、`Lemma 7` (line 670)，Chapter 3 中的 `Lemma 1` (line 842)、`Lemma 2` (line 870) 等。
  * **重置规约**：计数器依然按 Chapter 重置，但其在正文标题中显示的格式 `\thelemma` 必须重设为 `\arabic{lemma}`（彻底剥离 Chapter 前缀）。
  * **引理跨章引用消歧**：
    * 当在同一章内部引用时，直接使用：`\autoref{lem:ch2_2}`，完美输出为 `Lemma 2`。
    * 当跨章（例如在 Chapter 3 中）引用 Chapter 2 的引理时，原书格式写为 `"Lemma 2 of Chapter 2"` (line 940) 或 `"Lemma 7 of Chapter 2"` (line 886)。
    * 在 TeX 中我们必须严格通过**双锚点联动**来表达：`\autoref{lem:ch2_2} of \autoref{ch:2}`。这不仅确保了文字 100% 对应 Baker 真值，还实现了 Lemma 与 Chapter 2 分离且完全可点击的高级超链接跳转，消除了断链和死链接风险。

### 3. 多重与区间型实体的联合引用结构 (Serial Connector References)
原书中存在大量的复数引用和范围式引用。严禁将其写为硬编码的 bare-text，必须使用 `\ref` 与联合短语相结合，以保证在分页漂移时保持锚点准确：
* **两点/多点并列引用**：
  * `"Theorems 2.3 or 2.4"` (line 804) $\Longrightarrow$ `Theorems \ref{thm:2_3} or \ref{thm:2_4}`
  * `"Chapters 10 and 11"` (line 336) $\Longrightarrow$ `Chapters \ref{ch:10} and \ref{ch:11}`
  * `"Chapters 2 and 3"` (line 1536) $\Longrightarrow$ `Chapters \ref{ch:2} and \ref{ch:3}`
  * `"Lemmas 6 and 7"` (line 455) $\Longrightarrow$ `Lemmas \ref{lem:2_6} and \ref{lem:2_7}`
* **章节与小节普通词汇消歧**：
  * 在 `"be the subject of the present chapter"` (line 364, 423, 760) 等语境中，`chapter` 是普通名词，必须保留其普通文本属性，绝对不能人为制造 faked links 关联。

---

## 六、 分章节高保真重排与公式核销计划 (Chapter-by-Chapter Production & Reference Checklist)
为了实现精细化、一章一节稳步推进的重排进度管理，结合 `reference-plan.json` 的行号大纲，我们制定了以下**分章节高保真转录、消歧与重排核销计划**：

### 1. Chapter 1: The origins (Scaffold Lines: 140 – 360)
* **核心内容**：数论超越性的起源，Liouville 定理、e 与 $\pi$ 的超越性证明，Lindemann-Weierstrass 定理。
* **数学实体**：`Theorem 1.1` (line 148, Liouville)、`Theorem 1.2` (line 196, Transcendence of $e$)、`Theorem 1.3` (line 238, Transcendence of $\pi$)、`Theorem 1.4` (line 284, Lindemann-Weierstrass).
* **引用消歧要点**：
  * [ ] 核销 e 超越性证明中公式 `(1)`, `(2)`, `(3)`。其中 `From (1) and (3)` (line 222) 映射为 `From \eqref{eq:ch1_1} and \eqref{eq:ch1_3}`。
  * [ ] 区分 $f^{(j)}(0)$ 中的自变量 `(0)`，不予标记为方程链接。
  * [ ] 区分脚注中的 Liouville (1844), (1851) 出版年份，保留普通括号文本。
  * [ ] 正文第 336 行 `"Chapters 10 and 11"` 映射为 `Chapters \ref{ch:10} and \ref{ch:11}`。

### 2. Chapter 2: Linear forms in logarithms (Scaffold Lines: 361 – 755)
* **核心内容**：Gelfond-Schneider 定理的推广，对数线性型的非零性证明。
* **数学实体**：`Theorem 2.1` (line 366, Baker's Main Theorem)、`Theorem 2.2` (line 382)、`Theorem 2.3` (line 402)、`Theorem 2.4` (line 411). `Lemma 1` (line 457) 至 `Lemma 7` (line 670).
* **引用消歧要点**：
  * [ ] 跨章引用校对：在第 370 行出现 Siegel (1929)，与公式消歧。
  * [ ] 本章共有 7 个 lemmas（单章内以 Lemma 1–7 编目）。核销 `Lemmas 6 and 7` (line 455) 映射为 `Lemmas \ref{lem:ch2_6} and \ref{lem:ch2_7}`。
  * [ ] 公式定义：`line 470: (3)`、`line 485: (5)`、`line 621: (9)`、`line 738: (10)`。
  * [ ] 公式引用消歧：`line 565: "defined by (6)"` 对应 `\eqref{eq:ch2_6}`，`line 608: "in view of (8)"` 对应 `\eqref{eq:ch2_8}`，`line 713/742: "inequalities (9)"` 对应 `\eqref{eq:ch2_9}`。

### 3. Chapter 3: Quantitative theorems (Scaffold Lines: 756 – 1220)
* **核心内容**：对数线性型的下界定量估计。
* **数学实体**：`Theorem 3.1` (line 762, Main Quantitative bound). `Lemma 1` (line 842) 至 `Lemma 7` (line 1116).
* **引用消歧要点**：
  * [ ] 跨章引理与章节引用核销：
    * `line 886: "Lemma 7 of Chapter 2"` $\Longrightarrow$ `\autoref{lem:ch2_7} of \autoref{ch:2}`。
    * `line 940: "Lemma 2 of Chapter 2"` $\Longrightarrow$ `\autoref{lem:ch2_2} of \autoref{ch:2}`。
    * `line 986: "Lemma 1 of Chapter 2"` $\Longrightarrow$ `\autoref{lem:ch2_1} of \autoref{ch:2}`。
    * `line 1062: "Lemma 4 of Chapter 2"` $\Longrightarrow$ `\autoref{lem:ch2_4} of \autoref{ch:2}`。
  * [ ] 多实体复数引用：`line 804: "Theorems 2.3 or 2.4"` $\Longrightarrow$ `Theorems \ref{thm:ch2_3} or \ref{thm:ch2_4}`。
  * [ ] 公式系统定义：核销 `(2)` (line 936), `(3)` (line 953), `(4)` (line 960), `(6)` (line 1021), `(12)` (line 1119), `(13)` (line 1136)。
  * [ ] 公式引用映射：`line 988: "(4) implies (3)"` $\Longrightarrow$ `\eqref{eq:ch3_4} implies \eqref{eq:ch3_3}`。

### 4. Chapter 4: Freedom from relations / Diophantine equations (Scaffold Lines: 1221 – 1526)
* **核心内容**：对数线性型在不定方程（Thue、Elliptic、Hyperelliptic 方程）中的应用。
* **数学实体**：`Theorem 4.1` (line 1246, Thue equation bound)、`Theorem 4.2` (line 1347, Elliptic equation)、`Theorem 4.3` (line 1444, Genus 1 curves).
* **引用消歧要点**：
  * [ ] 跨章引用核销：`line 1228: "Chapter 3"` $\Longrightarrow$ `\autoref{ch:3}`；`line 1231: "Chapter 7"` $\Longrightarrow$ `\autoref{ch:7}`。
  * [ ] 公式定义核销：`line 1272/1276/1282: (1)`、`line 1362: (4)`。
  * [ ] 区分大量的文献年份：`line 1233: (1921)`、`line 1235: (1935)`、`line 1238: (1929), (1928)`、`line 1380: (1926)`、`line 1382: (1968)`。

### 5. Chapter 5: Class numbers of quadratic fields (Scaffold Lines: 1527 – 1779)
* **核心内容**：虚二次域类数问题，Gauss 猜想与 Baker-Stark 定理。
* **数学实体**：`Theorem 5.1` (line 1534, Class number 1 and 2 field determination).
* **引用消歧要点**：
  * [ ] 跨章引用核销：`line 1536: "Chapters 2 and 3"` $\Longrightarrow$ `Chapters \ref{ch:2} and \ref{ch:3}`；`line 1704: "Chapter 4"` $\Longrightarrow$ `\autoref{ch:4}`。
  * [ ] 公式定义：`line 1630: (2)`。
  * [ ] 引用定位：`line 1692: "Theorem 271 of Oxford, 1960"` (Hardy & Wright 经典定理，作为重排直录，不设内部链接)。

### 6. Chapter 6: Elliptic functions (Scaffold Lines: 1780 – 1950)
* **核心内容**：Weierstrass 椭圆函数、模形式与椭圆积分的超越性。
* **数学实体**：`Theorem 6.1` (line 1784, Period independence)、`Theorem 6.2` (line 1798)、`Theorem 6.3` (line 1806, Weierstrass $\zeta$ function)、`Theorem 6.4` (line 1814, Abelian varieties)、`Theorem 6.5` (line 1824). `Lemma 1` (line 1838).
* **引用消歧要点**：
  * [ ] 跨章引用核销：`line 1792: "Chapters 2 and 3"` $\Longrightarrow$ `Chapters \ref{ch:2} and \ref{ch:3}`；`line 1838: "Lemma 1 of Chapter 2"` $\Longrightarrow$ `\autoref{lem:ch2_1} of \autoref{ch:2}`；`line 1838: "Chapter 4"` $\Longrightarrow$ `\autoref{ch:4}`。

### 7. Chapter 7: Abelian varieties (Scaffold Lines: 1951 – 2150)
* **核心内容**：Abel 簇上的超越点，Gelfond 猜想的多维推广。
* **引用消歧要点**：
  * [ ] 跨章引用：`"Lemma 1 of Chapter 2"`, `"Lemma 3 of Chapter 2"`, `"Lemma 4 of Chapter 2"`。必须全部严格用 `\autoref{lem:ch2_X} of \autoref{ch:2}` 核销。

### 8. Chapter 8: Non-homogeneous linear forms (Scaffold Lines: 2151 – 2350)
* **核心内容**：非齐次对数线性型与 Bessel 函数。
* **引用消歧要点**：
  * [ ] 跨章引用：`"Chapter 2"`, `"Chapter 4"`。全部使用 `\autoref` 关联。

### 9. Chapter 9: The Schmidt subclass theorem (Scaffold Lines: 2351 – 2500)
* **核心内容**：Schmidt 子空间定理在超越数论中的应用。
* **引用消歧要点**：
  * [ ] 跨章引用：`"Chapter 3"` 及其对应的 $|\Lambda|$ 下界估计。

### 10. Chapter 10: S-unit equations and further results (Scaffold Lines: 2501 – 2800)
* **核心内容**：S-单位方程，p-进对数线性型。
* **引用消歧要点**：
  * [ ] 跨章引用：`"Chapter 1"`, `"Chapter 10"` (本章自引用)，全部用 `\autoref` 或 `\eqref` 覆盖。

### 11. Chapter 11: Mahler's classification (Scaffold Lines: 2801 – 3100)
* **核心内容**：Mahler 超越数分类（S, T, U, A 数），Koksma 分类及其等价性。
* **引用消歧要点**：
  * [ ] 跨章引用：`"Chapter 10"`, `"Chapter 8"` 中的引理，全部按单章重设的 Lemma 计数进行高精度多维核销。

### 12. Chapter 12: Algebraic independence (Scaffold Lines: 3101 – 3500)
* **核心内容**：代数独立性（Gelfond 定理，Shidlovsky 的 E-函数理论）。
* **引用消歧要点**：
  * [ ] 跨章引用：对 Chapter 10, Chapter 7 的跨章 Lemma 的引用，必须逐一比对 PDF 物理页面完成核销。

### 附录与后记 (Appendices & Backmatter) (Scaffold Lines: 3501 – 结束)
* **核心内容**：原书三个经典的附录与后记大纲文件（original_papers.tex, further_publications.tex, new_developments.tex），分别对应 Original Papers, Further Publications, New Developments。
* **引用消歧要点**：
  * [ ] 参考文献 `references.bib` 的排重与全引用核实。
  * [ ] 动态索引 `makeindex` 在附录与正文中的全面挂载。
  * [ ] 严格遵照 1975 剑桥原版/1990 增补版英文目录与后记实体大纲。

---

## 七、 避坑指南与硬核排版规范 (Hard-Won Lessons & Compilation Guidelines)
为了保证编译出的 PDF 具有顶级的学术出版质感并彻底规避编译期隐性错误，我们根据 `pdf-to-english-tex` 的实战避坑教训（Hard-won Lessons），制定了以下硬核规范：

1. **数学字体分配修复与 textfont 7 坏字阻断**：
   - **机制**：XeLaTeX 在结合 `ctex` / `amsart` 宏包进行编译时，由于嵌套脚本（如双重上标或 `\scriptscriptstyle` 下的分式 `\frac{1}{1^2}`）会触发数学字体族分配耗尽，导致 `.log` 中出现 `\textfont 7 is undefined` 警告，PDF 渲染公式时出现空白或坏字符。
   - **规范**：必须在导入 AMS 数学宏包前，强行在 Preamble 顶端装载 `lmodern`（Latin Modern 字体）：
     ```latex
     \usepackage{lmodern}
     \usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools,mathrsfs}
     ```
   - **验证网闸**：编译后执行 `grep -c 'textfont 7' trans_number_baker.log`，其返回计数必须为 **0**。

2. **严禁在 TeX 源码中使用 Unicode 数学特殊符号**：
   - **机制**：Marker 生成的 Markdown 文本常夹杂 Unicode 上下标，如 U+208B (₋)、U+2083 (₃) 等。这些字符在 pdflatex/xelatex 加载 Latin Modern 字体编译时无法识别，会抛出 `Missing character: There is no ₃ in font` 警告，在 PDF 中静默输出为空白字符。
   - **规范**：禁止任何 Unicode 标点、希腊字母或上下标直接进入 TeX 源码（PDF 标签fallback除外）。所有上下标一律强制转换为 LaTeX 原生公式：
     - 错误：`\(\chi₋₃\)` 或 `L(2, \chi₃)`
     - 正确：`\(\chi_{-3}\)` 或 `\(L(2, \chi_3)\)`
   - **验证网闸**：编译后执行 `grep -c 'Missing character' trans_number_baker.log`，其返回计数必须为 **0**。

3. **避免在 XeLaTeX + ctex 架构中使用 `multline*` 环境**：
   - **规范**：在大型展开多行公式排版中，尽量避免使用 `multline*`，其极易引起 `textfont 7` 分配问题。对齐长公式应优先使用 `\[ \begin{aligned} ... \end{aligned} \]` 或标准 `align*` 环境进行优雅换行与对齐。

4. **强制进行尾部章节的防臆造审计 (Anti-Fabrication Check)**：
   - **机制**：在重排长篇幅著作（10章以上）的最后部分（如 Appendix III: New Developments）时，由于上下文窗口过深，生成模型极易出现“幻觉臆造”现象，将原著末尾的学术段落直接替换为 AI 臆造的“研究启发”、“数论展望”、“致谢清单”或凭空捏造的虚假文献。
   - **规范**：必须对最后的 `new_developments.tex` 进行严格的**逐句物理比对核准（Sentence-by-sentence Anchored Check）**。凡不属于原书 1990 年版本学术内容的新增文字，一律强制剔除。

5. **UTF-8 物理编码网闸**：
   - **规范**：所有生成的 `.tex` 和 `.bib` 文件必须强制采用无 BOM 的 `UTF-8` 物理文件编码，防止字符集乱码导致编译器 silent failure。

---

## 八、 英文重排全周期质量保障 Checklist (Full-Lifecycle Action Items)
为了保证本重排过程不遗漏任何一个公式、年份与交叉引用，我们根据 `pdf-to-english-tex` 技能规范，设计了全周期的质量对齐网闸 To-Do List：

### Phase 1: Input, Scope, and Template Verification (阶段一：基础输入与框架核验)
- [x] **[1.1]** 确认输入绝对物理真值：`input/trans_number_baker/trans_number_baker.pdf` 存在且完整（共12章加附录）。
- [x] **[1.2]** 确认 Marker 提取的数据源 `input/trans_number_baker/trans_number_baker.md` 已被正确识别为主要的输入脚手架。
- [x] **[1.3]** 确认采用 `qbook.cls` 英文版宏包。验证 `trans_number_baker.tex` 已经正确 `\include` 12章 TeX 片段以及 3 个附录（`original_papers`, `further_publications`, `new_developments`）。
- [x] **[1.4]** 严格采用 unified page margin：页边距统一定制为舒适的 `1in`，即 `\usepackage[margin=1in]{geometry}`，防范大型数学公式发生右边缘 `Overfull \hbox` 截断。

### Phase 2: Counter & Preamble Implementation (阶段二：高标计数器与宏包自适应配置)
- [x] **[2.1]** 实现 Baker 书籍的学术脚注计数器：重构 `\@fnsymbol`，从单剑号 `\dagger` 开始计数（不使用星号 `*`，防止与代数伴随或矩阵转置冲突），并利用 `footmisc` 设置 `perpage` 使脚注按物理页自动置零。
- [x] **[2.2]** 设定定理、引理和公式计数器的重置与显示格式：
  - [x] 设定 `\newtheorem{theorem}{Theorem}[chapter]`。
  - [x] 设定 `\newtheorem{lemma}{Lemma}[chapter]`，并通过 `\renewcommand{\thelemma}{\arabic{lemma}}` 确保其不带有 chapter 前缀。
  - [x] 设定 `\@addtoreset{equation}{chapter}` 与 `\renewcommand{\theequation}{\arabic{equation}}`，确保公式编号按章重置且剔除前缀。
- [x] **[2.3]** 解决 `\autoref` 自动化命名：通过 `\AtBeginDocument{\def...}` 精准定义 `\theoremautorefname{Theorem}`、`\lemmaautorefname{Lemma}`、`\definitionautorefname{Definition}`，保证编译后链接可读性，告别死数。

### Phase 3: Text & Mathematical Equation Transcription (阶段三：高保真转录与公式校勘)
- [x] **[3.1]** 在 `output/trans_number_baker/tex/` 下，完成模块化文件的编写与脚手架内容注入（1-12章及前言、附录）。
- [x] **[3.2]** 严格依据 `typesetting_plan.md` 的校勘示例和原书 PDF，逐页验证脚手架公式，排除 OCR 引入的所有符号、分式与不等号扰动（特别是将希腊字母 $\alpha, \xi$ 误判为 `a, £` 以及 `\neq$ 误判为 `4=` 的地方）。
- [x] **[3.3]** 对所有选择性编号公式进行精确排版：
  - [x] 原书无编号公式一律强制使用无星号 `\[ ... \]` 或 `equation*`、`align*` 包装。
  - [x] 原书有标号公式一律使用 `\begin{equation}\label{eq:chX_Y}\tag{Y} ... \end{equation}` 包装。
- [x] **[3.4]** 对于推导出的公式，如果其属于“由某个公式通过自变量代换获得”（Substitution Equation），必须对其上下三行公式进行视觉二次校验，严防因 OCR 乱序而引起的错误公式传播。
- [x] **[3.5]** 将配图（如 `_page_2_Picture_3.jpeg`）规范存入 `assets/fig/` 下，并以 `\includegraphics` 导入，同时在图题 caption 中写明对应的 label。

### Phase 4: Full-Scope Cross-Reference Linkage (阶段四：全书交叉引用大账本对齐与年份消歧)
- [x] **[4.1]** 在编写各章 TeX 时，将 `reference-plan.json` 中的引用点一一进行 LaTeX 化映射：
  - [x] 所有 "Theorem X.Y" 与 "Lemma X" 的普通英文名词引用全部升级为 `\autoref{thm:chX_Y}` 和 `\autoref{lem:chX_Y}`。
  - [x] 所有 "(X)" 形式的公式明文引用升级为 `\eqref{eq:chX_Y}`。
- [x] **[4.2]** 逐一执行年份消歧核验：对照 `reference-plan.json` 中的 `parenthesized` 候选人，凡属于出版年份（如 `(1844), (1929), (1968)`），必须在 TeX 中保留为 plain-text 或 `\cite` 标记，禁止使用 `\eqref` 污染。
- [x] **[4.3]** 逐一执行函数参数消歧核验：确保形如 `f(0)`, `f(l)` 内部的小括号不被错误标记为公式链接。
- [x] **[4.4]** 遇到跨章引理引用（如 `Lemma 7 of Chapter 2`），统一重构为多维引用模式：`\autoref{lem:ch2_7} of \autoref{ch:2}`。
- [x] **[4.5]** 遇到联合多重引用（如 `Theorems 2.3 or 2.4`），统一重构为区间联合引用模式：`Theorems \ref{thm:ch2_3} or \ref{thm:ch2_4}`。

### Phase 5: Bibliography Database & Citation Setup (阶段五：BibTeX 数学文献数据库建立与核销)
- [x] **[5.1]** 抽取原书 Appendix I: Original Papers 以及各章节末尾文献，建立统一不含冗余或空实体的 `references.bib`，存放在 `bib/` 下。
- [x] **[5.2]** 文献库中所有的 entry key 必须跟正文中的 `\cite{...}` 一一映射。
- [x] **[5.3]** 精准控制 Bibliography 的微观版面美学（The Golden Ratio of List Spacing），重载 `thebibliography` 环境：
  ```latex
  \let\oldthebibliography\thebibliography
  \renewcommand\thebibliography[1]{%
    \oldthebibliography{#1}%
    \setlength{\itemsep}{3pt plus 1pt minus 1pt}%   % 黄金比例紧凑纵向间距
    \setlength{\parsep}{1pt plus 0.5pt}%            % 紧凑的段落空隙
    \small%                                         % 学术出版级别小五号字
  }
  ```
- [x] **[5.4]** 严格消除正文或 Preamble 中的任何 `\nocite{*}`，保证所有收录进 `.bib` 的文献都在正文中有迹可查。

### Phase 6: Automatic Pre-Compile Auditing (阶段六：编译前静态质量网闸验证)
- [x] **[6.1]** 运行静态语法核查器 `scripts/check_tex_static.py`，检测是否存在环境括号不匹配、`\includegraphics` 缺失或硬编码明文数字引用。
- [x] **[6.2]** 运行精准公式核销检测器：
  ```bash
  python3 scripts/check_labels.py output/trans_number_baker/
  ```
  - [x] 导出检查报表：`output/trans_number_baker/work/crossref-audit.md`。
  - [x] 检查是否存在“有标号公式未在 TeX 中声明 `\label`”的情况并进行补正。
  - [x] 检查是否存在“未被任何 `\eqref` 引用到的冗余 label”（Dead Labels）。
- [x] **[6.3]** **运行高保真网闸检测器 (MANDATORY)**：
  ```bash
  python3 scripts/check_fidelity.py output/trans_number_baker/
  ```
  核实定理环境、排版规范、括号对齐，检测出口状态码是否为 0。

### Phase 7: Continuous Compilation & Render Check (阶段七：多轮编译与实体数目审计)
- [x] **[7.1]** 在 `output/trans_number_baker/` 目录下，运行高保真多轮 XeLaTeX 编译测试：
  ```bash
  xelatex -interaction=nonstopmode trans_number_baker.tex
  bibtex trans_number_baker
  makeindex trans_number_baker.idx
  xelatex -interaction=nonstopmode trans_number_baker.tex
  xelatex -interaction=nonstopmode trans_number_baker.tex
  ```
- [x] **[7.2]** 提取编译日志 `trans_number_baker.log`，执行 `grep -c 'Missing character' trans_number_baker.log` 保证输出结果为 0，彻底根除任何隐藏的 Unicode 空白坏字。
- [x] **[7.3]** 检查最终生成的 `trans_number_baker.pdf` 物理页面。核查动态生成的 TOC 标题、前页、正文与 `\printindex` 页码，确保完美对齐。
- [x] **[7.4]** 编写并生成最终的排版实体 Manifest : 创建 `output/trans_number_baker/manifest.json`，统计各章节生成的实际 `theorems`, `lemmas`, `equations`, `proofs` 数量，并与基础账本进行高精准对齐校验。

### Phase 8: Post-Compile Link Audit (阶段八：编译后超链接物理网闸审计)
- [x] **[8.1]** 运行编译后 PDF 链接审计检测：
  ```bash
  python3 scripts/check_pdf_links.py output/trans_number_baker/trans_number_baker.pdf
  ```
- [x] **[8.2]** 逐章节进行链接数量与质量剖析，重点比对 Chapter 2, Chapter 3 等公式密集章节。
- [x] **[8.3]** **坚决杜绝 Fake Links**：不可为游戏链接指标而对普通数学名词、代数基（如 $e$, $\pi$）设定点击跳转，每一个生成的跳转链接必须语义真实存在。

### Phase 9: Final Delivery & Cleanup (阶段九：交底报表输出与辅助清理)
- [x] **[9.1]** 在 `output/trans_number_baker/work/` 目录下规范生成全周期核查最终报表 `final-report.md`。
- [x] **[9.2]** 运行 `latexmk -c` 或是进行手动辅助清理，将工作目录下的 `.aux`, `.log`, `.toc`, `.fls`, `.fdb_latexmk`, `.xdv`, `.bcf`, `.run.xml`, `.idx`, `.ilg`, `.ind`, `.blg` 等临时缓存和中间编译垃圾全部扫除干净。
- [x] **[9.3]** 保证 `trans_number_baker.tex`, `trans_number_baker.pdf`, `references.bib` 以及各 `tex/sec*.tex` 文件完美安放于输出区。

---

## 九、 质量验证网闸 (Quality Gates)
在生成完所有 LaTeX 源码并完成 To-Do List 的全面对齐后，我将依次执行以下操作：
1. **静态语法审计（Static Checks 自进化）**：
   - 使用升级后的 **`check_tex_static.py`** 与 **`check_labels.py`** 引擎对 TeX 文件进行深度静态扫描。
   - 检测引擎现已对全书“复合与复数章节/定理引用（例如 `Chapters 10 and 11`、`Theorems 1.2 and 1.3`）”进行了多并列（Serial Connectors）匹配支持，严防任何未被 `\autoref` 激活 of 硬编码或裸章节出现。
   - 检查环境括号匹配、公式闭合性，确保没有编译硬伤。
2. **XeLaTeX 编译验证**：在 `output/trans_number_baker/` 中运行编译测试。
3. **参考文献 BibTeX 数据库生成与引用集成**：针对自动生成出来的 `references.bib`，自动运行 BibTeX 交叉引用测试，确保文献列表和引用均渲染正确。
4. **PDF 动态链接审计**：检查编译后 PDF 的 TOC、Footnotes、Equation links、Citation links，保证每一个跳转均完美正常。
