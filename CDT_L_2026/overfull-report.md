# Overfull Display Equations Report

This report lists all uniquely resolved display equations that exceed the text margin (total: 35).


## File: `./tex/sec10.tex`

### Equation 1 (Line 158) - **9.82484pt too wide**

```latex
 156    \frac{\iint_{\mathbf{T}^2} \log |\varphi(z) - \varphi(w)| \, \mu_{\text{Haar}}(z) \mu_{\text{Haar}}(w)}{\log 16 + \log |G'(0)| - \frac{552431}{242760}}.
 157    \end{equation}
 158 -> 使用 \S~A.2 中定义的 gobble 围道中（稍微）优化的选择 $\operatorname{Gob}(0.92, 110, 23)$，我们发现 $|G'(0)| = 0.9163768\dots$，并且商 \eqref{eq:10.3.4} 的计算结果大约为 $22.7527$，距离所需的阈值 $17$ 还有相当长的一段距离。$\vartriangle$
 159    \end{remark}
 160    
```


## File: `./tex/sec11.tex`

### Equation 2 (Line 126) - **29.77345pt too wide**

```latex
 124    我们还可以求几何级数的和，将积分公式 \eqref{eq:11.1.13} 表达为：
 125    \begin{equation}\label{eq:11.1.16}\tag{11.1.16}
 126 -> L(2,\chi_{-3})H_A(x) - 2H_B(x) = \iint_{[0,1]^2} \frac{1 + st + s^2t^2}{(1 + st + s^2t^2)^2 - 9st(1 - t^3)(1 - s^3)x} dsdt.
 127    \end{equation}
 128    由 \eqref{eq:11.1.15}，该公式将函数 $L(2,\chi_{-3})H_A(x) - 2H_B(x)$ 表示为一族在 $\mathbf{C} \setminus [1,\infty)$ 上全纯的（在此处恰好为有理）函数 $f_{s,t}(x) \in \mathcal{O}(\mathbf{C} \setminus [1,\infty))$ 的连续积分。在复区域上的全纯性质在对参数 $(s,t) \in [0,1]^2$ 的任意连续积分下均能得以保持，因此该积分表示同样清晰地展现了 \eqref{eq:11.1.16} 在 $\mathbf{C} \setminus [1,\infty)$ 上的解析性。这就是 Zudilin 在 \cite{Zud17} 中的观点。
```

### Equation 3 (Line 139) - **17.66562pt too wide**

```latex
 137    在 \cite{Zag09} 的情况 $\mathbf{E}$ 中给出了另一种对 $G$ 的 holonomic 有理逼近序列，其 ODE 奇点为 $\{0, 1/8; 1/4, \infty\}$（前两个是超收敛的），且分母类型为 $[1, \dots, n]^2$。
 138    
 139 -> 由于 $e^2 > 16 \cdot (1/4)$ 且 $e^4 > \left(\frac{1+\sqrt{5}}{2}\right)^5$（且优势巨大！），除非发现完全全新的想法，否则这无疑排除了利用我们的方法、通过这两类特殊的有理逼近来解决 Catalan 常数无理性的可能性。
 140    \end{remark}
 141    
```


## File: `./tex/sec12.tex`

### Equation 4 (Line 187) - **35.93895pt too wide**

```latex
 185    \[ a_0 + \frac{a_{-1}}{y} + \frac{a_{-2}}{y^2} + \frac{a_{-3}}{y^3} = \frac{676}{9y^2} + \frac{2}{y^3}. \]
 186    这当然现在有解。这反映了在这些函数之间存在一个线性相关性。事实上，在以下函数之间已经存在一个 $\mathbf{C}(y)$-线性相关性：
 187 -> \[ \int \frac{G_A(y)}{y^2} \, dy, \quad \int \frac{G_A(y)}{y^3} \, dy, \quad G_A(y), \quad G_A'(y), \quad G_A''(y), \quad G_A'''(y) \quad \text{和} \quad 1. \]
 188    作为与解 $a_{-2} = 676/9$ 和 $a_{-3} = 2$ 的另一个相容性检查，我们有（与方程 \eqref{eq:12.1.6} 类比）：
 189    \[ a_0 G_A(y) + a_{-1} \frac{G_A(y)}{y} + a_{-2} \frac{G_A(y)}{y^2} + a_{-3} \frac{G_A(y)}{y^3} = \frac{676}{9} \frac{G_A(y)}{y^2} + 2 \frac{G_A(y)}{y^3} \]
```


## File: `./tex/sec14.tex`

### Equation 5 (Line 541) - **26.61748pt too wide**

```latex
 539    \[ B_{6}(y), B_{7}(y), \int yG(y) dy, \int G(y) dy, \int \frac{G(y) - G(0)}{y} dy, \]
 540    \[ \int \frac{G(y) - G(0) - G'(0)y}{y^{2}} dy, \int \frac{G(y) - G(0) - G'(0)y - G''(0)\frac{y^{2}}{2}}{y^{3}} dy, \]
 541 -> \[ \int \frac{G(y) - G(0) - G'(0)y - G''(0)\frac{y^{2}}{2} - G'''(0)\frac{y^{3}}{6}}{y^{4}} dy. \]
 542    对函数 \(B_1, \ldots, B_7\) 参见 (10.1.2), (10.1.4) 以及 (10.2.1), 
 543    以及对函数 G（其最终将不存）参见定义 14.1.9. 
```

### Equation 6 (Line 562) - **17.3819pt too wide**

```latex
 560    在配合命题 14.1.11, 取 \(\Sigma^0_{Y_0(2)} := \{y_{a^-,b^-}\}\) 为以下多重指标的 \(y := x + w(x) = x^2/(x-1)\) 像的前提下, 
 561    推论 9.0.19 此时适用:
 562 -> \[ \Sigma_{Y(2)}^0 := \left\{ (a - \sqrt{a^2 - 1})(b - \sqrt{b^2 - 1}) \right\} = \left\{ \frac{1}{(2n + 1 + 2\sqrt{n^2 + n})(2m + 1 + 2\sqrt{m^2 + m})} \right\}; \]
 563    以及 \(\Sigma^1_{Y_0(2)} := \emptyset\), \(U_{Y_0(2)} := D(0, 1/100)\), 以及当然有 \(\varphi_{Y_0(2)} := \varphi = h \circ \psi\). 
 564    因此我们的 holonomy 边界的解析性条件是满足的.
```

### Equation 7 (Line 575) - **35.19937pt too wide**

```latex
 573      \centering
 574      \includegraphics[width=0.65\textwidth]{assets/fig/_page_187_Figure_2.jpeg}
 575 ->   \caption{\(\xi \in [1.5, 2]\) 范围内 \((2/17^2)(9\xi + I_{\xi}^{17}(\xi))\) 的函数图像片段，显示区间 \(\xi \in [1.7, 1.78]\) 被包含在极小值化范围内.}\label{fig:14.5.1}
 576    \end{figure}
 577    
```


## File: `./tex/sec15.tex`

### Equation 8 (Line 299) - **25.29433pt too wide**

```latex
 297    \[ y = \frac{x}{1 + 13x + 49x^2}. \]
 298    如果我们现在取权重 2 的 Eisenstein 级数:
 299 -> \[ E = \frac{7E_2(\tau) - E_2(7\tau)}{1 - 7} = 1 + 4q + 12q^2 + 16q^3 + 28q^4 + \dots \]
 300    并且随后将其写为 y 的函数, 
 301    我们获得了一个在 \(\mathbf{P}^1 \setminus \{0, 1/27, -1, \infty\}\) 
```


## File: `./tex/sec2.tex`

### Equation 9 (Line 382) - **11.56613pt too wide**

```latex
 380    特别地, 如果我们在\autoref{thm:2.5.1} 中将 \(\varphi\) 限制为单值映射, 那么我们无法指望证明\autoref{thm:2.8.4}, 因为此时
 381    \[ \lvert\varphi'(0)\rvert \le 4 < 4.481689... = e^{3/2}. \]
 382 -> Koebe 映射在开单位圆盘上是 1:1 的, 但它延伸到 \(\mathbb{C} \setminus \{\pm 1\} \to \mathbb{C} \setminus \{1\}\) 上是一个 2:1 的有理映射. 将此二次有理映射与 \(\mathbb{D} \to \mathbb{C} \setminus ((-\infty, -1] \cup [1, \infty))\) 的黎曼共形映射 (即 \(\sqrt{G(z^2)} = 2z/(1+z^2)\)) 进行复合, 我们最终得到双值映射:
 383    \begin{equation}\label{eq:2.11.2}
 384    \varphi : \mathbf{D} \to \mathbf{C} \setminus \{1\}, \qquad \varphi(z) := G\left(\sqrt{G(z^2)}\right) = \frac{8(z+z^3)}{(1+z)^4} = 1 - \left(\frac{1-z}{1+z}\right)^4.
```


## File: `./tex/sec3.tex`

### Equation 10 (Line 33) - **35.10733pt too wide**

```latex
  31    我们用 \(\mathbf{n} \mapsto \mathbf{n}^+\) 表示这一全序的后继函数. 在
  32    \[ \mathbf{Q}[\![\mathbf{x}]\!] =: F = \bigcup_{\mathbf{n} \in \mathbf{N}^d, \, \prec} F^{(\mathbf{n})} \]
  33 -> 上产生的过滤是分裂且极大的: 后继商 \(\mathbf{Q}\)-向量空间 \(F^{(\mathbf{n})}/F^{(\mathbf{n}^+)} \cong \mathbf{Q}\) 是一维的, 且以 \(F^{(\mathbf{n})} \setminus F^{(\mathbf{n}^+)}\) 中唯一的单项式 \(\mathbf{x}^{\mathbf{n}}\) 的等价类为基底. 
  34    利用单同态 \(\psi_D: E^I_{D,\Omega} \hookrightarrow F\), \(F\) 上的 \((\mathbf{N}^d, \prec)\)-过滤在 \(\mathbf{Q}\)-向量空间 \(E_{D,\Omega}^I \otimes_{\mathbf{Z}} \mathbf{Q}\) 上诱导了一个 \((\mathbf{N}^d, \prec)\)-过滤:
  35    \[ E_{D,\Omega}^{I,(\mathbf{n})} := \psi_D^{-1} \left( F^{(\mathbf{n})} \right) \subset E_{D,\Omega}^I \otimes_{\mathbf{Z}} \mathbf{Q}. \]
```

### Equation 11 (Line 113) - **73.44116pt too wide**

```latex
 111    因为这一特化后的单项式恰好是使得 \(\gamma \cdot (\mathbf{x}^{(1)})^{\mathbf{k}}(\mathbf{x}^{(2)})^{\mathbf{n}_2}\) 是来自 \(F(\mathbf{x}^{(1)},\mathbf{x}^{(2)})\) 的单项式的那些 \(\gamma \cdot (\mathbf{x}^{(1)})^{\mathbf{k}}\). 
 112    以此方式, \(\mathbf{n}_1 \in \mathcal{V}_{D,\Omega_1}^{I_1}\). 
 113 -> 同理可得 \(\mathbf{n}_2 \in \mathcal{V}_{D,\Omega_2}^{I_2}\), 从而证明了所要求的包含关系 \(\mathcal{V}_{D,\Omega_1 \times \Omega_2}^{I_1 \times I_2} \subseteq \mathcal{V}_{D,\Omega_1}^{I_1} \times \mathcal{V}_{D,\Omega_2}^{I_2}\).
 114    \end{proof}
 115    
```


## File: `./tex/sec6.tex`

### Equation 12 (Line 92) - **42.06079pt too wide**

```latex
  90    
  91    \begin{corollary}\label{cor:6.0.14}
  92 -> 假设与定理~\ref{thm:6.0.2} 相同的条件和记号, 但更简单地考虑单个全纯映射 $\varphi: (\overline{\mathbf{D}}, 0) \to (\mathbf{C}, 0)$, 其满足 $|\varphi'(0)| > e^{\tau(\mathbf{b}; \mathbf{e})}$, 且使得拉回 $\varphi^* f_i$ 在开单位圆盘上是亚纯函数, 即 $\varphi^* f_i \in \mathcal{M}(\mathbf{D})$.
  93    如果要么 $|\varphi'(0)| > e^{\sigma_m}$, 要么所有函数 $f_i$ 都是 holonomic, 那么:
  94    \begin{equation}\label{eq:6.0.15}
```

### Equation 13 (Line 121) - **29.71733pt too wide**

```latex
 119    这在终点 $\xi = 1$ 处达到.
 120    因此我们发现了与采用较粗糙方案时相同的数值 $\tau(\mathbf{b}, \mathbf{e}) = \tau^{\flat}(\mathbf{b}) + \tau^{\sharp}(\mathbf{e}) = 3/4$:
 121 -> \[ \mathbf{b} = (0, 1)^t, \qquad \mathbf{e} = (0, 0), \qquad \tau^{\flat}(\mathbf{b}) = 3/4, \quad \tau^{\sharp}(\mathbf{e}) = 0, \]
 122    在此例中与 \S~2.5 相比并没有取得改进.
 123    
```

### Equation 14 (Line 208) - **74.31647pt too wide**

```latex
 206    \subsubsection{阿基米德精细化}\label{sec:6.1.3}
 207    
 208 -> 首先, 这一渐近方案允许通过初等方法将积分 $\int_{\mathbf{T}} \log^+ |\varphi| \, \mu_{\text{Haar}}$ 改进为严格较小的量 $\int_0^1 t \cdot (\log |\varphi(e^{2\pi it})|)^* \, dt$.
 209    我们已经在 \cite[§ 2.3.3]{CDT21} 中指出, 通过再次利用定理~\ref{thm:4.2.1}, 可以将~\eqref{eq:6.1.1} 中的单项式指数 $\mathbf{k}$ 限制在超立方体 $[0,D]^d$ 的低偏差部分, 从而实现对 holonomy 边界的一些改进.
 210    用具体的启发式语言来说, 这意味着当 $d \to \infty$ 时, 指数向量 $(k_1,\ldots,k_d)$ 在~\eqref{eq:6.1.1} 中可以被认为接近于集合 $\{jD/d:0\le j< d\}$ 的某种排序.
```

### Equation 15 (Line 344) - **50.85359pt too wide**

```latex
 342    \subsection{抽屉原理步骤: 引理 6.2.6 的证明}\label{sec:6.3}
 343    
 344 -> 我们的证明结合了经典的 Thue--Siegel 引理 \cite[Lemma 2.9.1]{BG06} 以及关于函数非佳逼近性质与消亡过滤跳跃 Cartesian 乘积结构的结合引理~\ref{lem:3.2.14}, 遵循我们在 \S~6.1.2 中概述的步骤.
 345    
 346    \begin{proof}[引理~\ref{lem:6.2.6} 的证明]
```

### Equation 16 (Line 357) - **62.84981pt too wide**

```latex
 355    F(\mathbf{x}) = \sum_{\substack{\mathbf{i} \in V_m^d \\ \mathbf{k}/D \in P_{\epsilon}^d \cap \mathbf{Z}^d}} c_{\mathbf{i}, \mathbf{k}} \, \mathbf{x}^{\mathbf{k}} \prod_{s=1}^d f_{i_s}(x_s) = \sum_{\mathbf{n} \in \mathbf{N}^d} \beta_{\mathbf{n}} \, \mathbf{x}^{\mathbf{n}},
 356    \end{equation}
 357 -> 只要满足 $\max_{j=1}^{d} n_{j} \leq (m-\delta)D$ 或 $\mathbf{n} \notin (m+\delta)D \cdot P_{\epsilon}^{d}$, 所有的系数 $\beta_{\mathbf{n}}$ 均消亡, 我们便在模板形式~\eqref{eq:6.2.8} 的未知系数 $c_{i,k}$ 中建立了一个包含 $M \leq 2((m-\delta)D)^d$ 个线性方程的线性方程组.
 358    一旦维度 $d \gg_{\epsilon,\delta} 1$ 足够大, 定理~\ref{thm:4.2.1} 和引理~\ref{lem:6.2.4} 表明, 我们线性方程组中自由参数 $c_{\mathbf{i},\mathbf{k}}$ 的个数 $N$ 将超过数量:
 359    \begin{equation}\label{eq:6.3.3}
```

### Equation 17 (Line 512) - **240.91583pt too wide**

```latex
 510    为了稍后记号的便利, 我们定义 $T_{\gamma,\epsilon}^d := \{\mathbf{z} \in \mathbf{T}^d : \forall k, D(\mathbf{z}^{(k)}) < \epsilon\}$.
 511    我们用 $d^{(k)} := \lceil \gamma_{k+1} d/m \rceil - \lceil \gamma_k d/m \rceil$ 表示变量块 $\mathbf{z}^{(k)}$ 的长度, 并在块形式中将 $\mathbf{z} := e^{2\pi i \mathbf{s}}$ 写为 $\mathbf{z} = (\mathbf{z}^{(0)}, \dots, \mathbf{z}^{(l)})$, 使得 $\mathbf{z} \in T_{\gamma,\epsilon}^d$ 等同于对每个 $k = 0, \dots, l$ 都有 $D(\mathbf{s}^{(k)}) < \epsilon$.
 512 -> 给定一个向量 $\mathbf{w} = (w_1, \dots, w_d) \in \mathbf{R}^d$, 让我们稍微滥用一下记号, 用 $\mathbf{w}^* := (w_1^*, \dots, w_d^*)$ 表示 $\mathbf{w}$ 的分量集合的递增\ \footnotetext[23]{或者更确切地说, 是非降的.}重排向量.
 513    根据推论~\ref{cor:6.2.11}, 运行条件 $\mathbf{k}/D \in P_{\epsilon}^d$ 蕴含着:
 514    \begin{equation}\label{eq:6.5.16}
```

### Equation 18 (Line 625) - **34.10042pt too wide**

```latex
 623    \end{equation}
 624    中可能作为 $\mathbf{x}^{\mathbf{n}}$ 系数出现的非零有理数 $\beta \in \mathbf{Q}^{\times}$ 的最小公分母, 在所有可能的 $\mathbf{k} \in D \cdot P^d_{\epsilon}$、所有可能的 $\{1, \dots, d\}$ 的置换 $\pi$ 以及对每个 $i \in \{1, \dots, m\}$ 的所有可能的形式函数:
 625 -> \begin{equation}\label{eq:6.6.5}
 626    g_{1+(i-1)d/m}(x), \dots, g_{id/m}(x) \in \bigoplus_{n=0}^{\infty} \frac{x^n}{[1, \dots, b_{i,1} \cdot n] \cdots [1, \dots, b_{i,r} \cdot n]} \mathbf{Z}
 627    \end{equation}
```

### Equation 19 (Line 674) - **128.08102pt too wide**

```latex
 672    \begin{align}
 673    &\exp\left(\sum_{i=1}^{m}\sum_{s=1}^{d/m}\sum_{h=1}^{r}\left(b_{i,h}\cdot\left((i-1)D+smD/d\right)+O(\epsilon D)\right)\right) \nonumber\\
 674 -> &\quad =\exp\left(mD\sum_{i=1}^{m}\sum_{s=1}^{d/m}\sigma_{i}\cdot\left((i-1)/m+s/d\right)+O(\epsilon dD)\right) \nonumber\\
 675    &\quad =\exp\left(\alpha\sum_{i=1}^{m}\sigma_{i}\int_{(i-1)/m}^{i/m}2t\,dt+O(\epsilon\alpha)+o_{d\to\infty}(\alpha)\right) \nonumber\\
 676    &\quad =\exp\left(\alpha\tau^{\flat}(\mathbf{b})+O(\epsilon\alpha)+o_{d\to\infty,\epsilon\to0}(\alpha)\right),\label{eq:6.6.13}
```

### Equation 20 (Line 724) - **75.23433pt too wide**

```latex
 722      \item[(i)] 所有素数 $p \le \xi D$ 仅给~\eqref{eq:6.6.18} 的分母增加一个可以忽略的 $\exp(o(\xi D)) = \exp(o(\alpha))$ 因子;
 723      \item[(ii)] 清理因子满足:
 724 ->   \[ [1, \dots, \xi D]^{\lfloor d\left(\sum_{i=1}^m e_i\right)/m\rfloor} = \exp\left(\xi dD\left(\sum_{i=1}^m e_i\right)/m + o(\alpha)\right) = \exp\left(\xi\left(\sum_{i=1}^m e_i\right) \cdot 2\alpha/m^2 + o(\alpha)\right). \]
 725    \end{enumerate}
 726    
```

### Equation 21 (Line 728) - **112.36401pt too wide**

```latex
 726    
 727    那么显而易见, 在相差一个 $\exp(o_{d\to\infty,\epsilon\to0}(\alpha))$ 因子的意义下, 当 $h_j(x)$ 遍历~\eqref{eq:6.6.17}, $n$ 遍历 $(m + \delta)D \cdot P^d_{\epsilon}$, $\mathbf{k}$ 遍历 $D \cdot P^d_{\epsilon}$ 时, 所有的形式表达式~\eqref{eq:6.6.18} 的 $\mathbf{x}^{\mathbf{n}}$ 系数的最小公分母是下式的除数:
 728 -> \[ \frac{[1,\ldots,\xi D]^{\infty}}{(n_1-k_1)^{\max_i(e_i)}\dots(n_d-k_d)^{\max_i(e_i)}}, \quad \mathbf{n}\in(m+\delta)D\cdot P^d_{\epsilon}, \quad \mathbf{k}\in D\cdot P^d_{\epsilon}; \]
 729    并且, 在相差一个 $\exp(o_{d\to\infty,\epsilon\to0}(\alpha))$ 因子的意义下, 这又是下式的除数\ \footnotetext[24]{即使包括所有的 $\mathbf{k} \in [0, D]^d$, 即再次忽略 $\mathbf{k} \in P_{\epsilon}^d$ 的限制.}:
 730    \begin{equation}\label{eq:6.6.19}
```

### Equation 22 (Line 755) - **81.11499pt too wide**

```latex
 753    \end{equation}
 754    
 755 -> 我们对速率 $\exp \alpha \cdot \tau^{\sharp}(\mathbf{e}) + o(\alpha)$ 的定义为总的额外分母估计~\eqref{eq:6.6.21} 在参数 $\xi \in [0, m]$ 上的极小值.
 756    
 757    \subsection{定理 6.0.2 的证明}\label{sec:6.7}
```

### Equation 23 (Line 839) - **24.99171pt too wide**

```latex
 837    \begin{aligned}
 838    \varphi_{Y_0(2)}(z) &:= h\left(\operatorname{Gob}(r,e,f)(\delta z)\right), \\
 839 -> \varphi_k(z) &:= \varphi_{Y_0(2)}\left(\gamma_k z\right), \quad k = 0, 1, 2,
 840    \end{aligned}
 841    \]
```


## File: `./tex/sec7.tex`

### Equation 24 (Line 601) - **118.98181pt too wide**

```latex
 599    
 600    固定一个满足 \(\log |\varphi'(0)| > \sigma_m + \epsilon\) 的 \(\epsilon > 0\). 
 601 -> 那么存在一个 \(N_0 \in \mathbb{N}\), 使得对于所有 \(n \geq N_0\), 我们有:
 602    \[ h_{\infty}(\psi_D^{(n)}) \le -n \log |\varphi'(0)| + D \int_{\mathbf{T}} \log^+ |\varphi(z)| \, \mu_{\text{Haar}}(z) + (\epsilon/2)n + o(D); \]
 603    \[ h_{\text{fin}}(\psi_D^{(n)}) \le (\sigma_m + \epsilon/2)n. \]
```

### Equation 25 (Line 605) - **54.9757pt too wide**

```latex
 603    \[ h_{\text{fin}}(\psi_D^{(n)}) \le (\sigma_m + \epsilon/2)n. \]
 604    因此对于所有 \(n \in \mathbb{N}\),
 605 -> \[ h_{\infty}(\psi_D^{(n)}) \le -n \log |\varphi'(0)| + D \int_{\mathbf{T}} \log^+ |\varphi(z)| \, \mu_{\text{Haar}}(z) + (\epsilon/2)n + o(D); \]
 606    \[ h_{\text{fin}}(\psi_D^{(n)}) \le (\sigma_m + \epsilon/2)n + o(D). \]
 607    通过斜率不等式 \eqref{eq:7.2.14} 和 \(\log |\varphi'(0)| > \sigma_m + \epsilon\), 紧接着有:
```

### Equation 26 (Line 680) - **215.33934pt too wide**

```latex
 678    我们修改了 \cite[第 10.5.5 节]{Bos20} 中的计算. 
 679    不使用文献中所使用的 \(\varphi\), 
 680 -> 我们对这个次调和函数 \(\log |z^{-n}h_r\varphi_r^*(s(x)\cdot x^D)|\) 应用 Poisson--Jensen 公式——或次调和性质. 
 681    这为我们提供了上界:
 682    \begin{equation}\label{eq:7.4.2}
```

### Equation 27 (Line 692) - **20.38914pt too wide**

```latex
 690    \end{equation}
 691    为了证明它, 我们从 Poincaré--Lelong 公式开始, 该公式给出:
 692 -> \[ \frac{i}{\pi} \partial \overline{\partial} \log \|\varphi_r^*(x^{-D})\|_{\varphi_r^* \overline{\mathcal{L}}^{\otimes D}} = -c_1 \left( \varphi_r^* \overline{\mathcal{L}}^{\otimes D} \right), \]
 693    \[ \frac{i}{\pi} \partial \overline{\partial} \log^+ |z|^{-1} = -\delta_0 + \mu_{\text{Haar}}. \]
 694    因此, 根据 Green--Stokes 公式, 我们发现
```

### Equation 28 (Line 766) - **62.45915pt too wide**

```latex
 764    因此只需证明定理 7.1.6. 
 765    根据引理 7.4.1 和 7.4.5, 利用斜率记号 \eqref{eq:7.1.7}, 
 766 -> 我们有对于 \(n/D \in [\alpha_k, \alpha_{k+1}]\), 
 767    对于 \(h_{\infty}(\psi_D^{(n)})\) 的最优边界是通过在 \(0 \le k \le l\) 中使用 \(r_k\) 获得的; 
 768    在此我们设定 \(\alpha_0 = 0, \alpha_{l+1} = m\). 
```

### Equation 29 (Line 1134) - **18.59645pt too wide**

```latex
1132    &&> 5.08 > 4 + 1 = \sigma_m + \max_{i=1}^{m}(e_i).
1133    \end{aligned}
1134 -> \]
1135    
1136    令 \(\overline{h}_{\infty}(\psi_D^{(n)})\), \(\overline{h}_{\text{fin}}(\psi_D^{(n)})\) 
```


## File: `./tex/sec8.tex`

### Equation 30 (Line 163) - **85.40726pt too wide**

```latex
 161    \end{equation}
 162    这对于在 \(\mathbf{R}^n\) 上所有可表示为 \(\nu = \nu^+ - \nu^-\) （伴随着具有收敛能量积分 \(I(\nu^\pm) < \infty\) 的有限正测度 \(\nu^\pm\), 
 163 -> 且具有支撑集 \(\operatorname{supp}(\nu) \subseteq \{\|\mathbf{x}\| \leq R\}\)）的带符号测度 \(\nu\) 都是有效的, 
 164    其中最优常数 \(a_n\) 恰好为:
 165    \[ a_n := \begin{cases} \exp\left(\frac{1}{2} + \dots + \frac{1}{n-4} + \frac{1}{n-2}\right), & \text{对于 } n \text{ 偶数;} \\ \exp\left(\frac{1}{1} + \dots + \frac{1}{n-4} + \frac{1}{n-2} - \log 2\right), & \text{对于 } n \text{ 奇数.} \end{cases} \]
```

### Equation 31 (Line 209) - **0.35551pt too wide**

```latex
 207    \begin{proposition}[Nazarov]\label{prop:8.1.13}
 208    对于任意连续函数 \(\varphi : \mathbf{T} \to \mathbf{C}\),
 209 -> \[ \iint_{\mathbf{T}^2} \log |\varphi(z) - \varphi(w)| \, \mu_{\text{Haar}}(z) \mu_{\text{Haar}}(w) \leq \iint_{\mathbf{T}^2} \log \max \left( |\varphi(z)|, |\varphi(w)| \right) \, \mu_{\text{Haar}}(z) \mu_{\text{Haar}}(w) \]
 210    \[ = \int_0^1 2t \cdot (\log |\varphi(e^{2\pi i t})|)^* \, dt, \]
 211    其中 \(g^*\) 表示一个连续函数 \((0,1) \to \mathbf{R}\) 的递增重排 \eqref{eq:2.4.1}. 
```

### Equation 32 (Line 399) - **120.13292pt too wide**

```latex
 397    我们观察到：一个形式截面 \(g(\mathbf{x}) \in F_{\mathbf{Q}} = \Gamma(\widehat{X}_0, \mathcal{L}^{\otimes D})\) 
 398    在 \(\mathbf{x} = \mathbf{0}\) 处的消逝阶数 \(\operatorname{ord}_0(g(\mathbf{x}))\) （作为 \(\mathcal{L}^{\otimes D}|_{\widehat{X}_0}\) 的正则截面, 
 399 -> 而不是作为 \(\mathbf{x}^{-D}\mathbf{Q}[\![\mathbf{x}]\!]\) 中的 Laurent 级数） 
 400    至少为 n, 当且仅当 \(g(\mathbf{x}) \in F_{\mathbf{Q}}^{(0,\ldots,0,n)}\). 
 401    我们还观察到 \(g(\mathbf{x}) \in F_{\mathbf{Q}}^{(\mathbf{n})}\) 当且仅当要么 \(\operatorname{ord}_0(g(\mathbf{x})) > |\mathbf{n}|\), 
```

### Equation 33 (Line 502) - **12.72002pt too wide**

```latex
 500    那么 \(h(z_1) \cdots h(z_d) \cdot \left(\varphi_{r(\mathbf{n})}^*\right) G(\mathbf{z}) \in \mathcal{O}\left(\overline{\mathbf{D}}^d\right)\) 
 501    在整个 \(\overline{\mathbf{D}}^d\) 上是全纯的, 
 502 -> 并且具有与 \(\varphi_{r(\mathbf{n})}^*G\) 相同的领先阶数射流 \(J_n\left(\varphi_{r(\mathbf{n})}^*G\right)\).
 503    
 504    这使我们可以利用 \cite[引理 2.4.1]{CDT21} 来根据齐次多项式 \(J_n\left(\varphi_{r(\mathbf{n})}^*G\right) = J_n\left(h(z_1)\cdots h(z_d)\cdot \varphi_{r(\mathbf{n})}^*G\right)\) 
```

### Equation 34 (Line 846) - **61.43823pt too wide**

```latex
 844    召回对于 \(D\gg 1\), 我们有 \(\mathcal{V}_D^d\subset [0,(m+\epsilon')D]^d\). 
 845    对于所有 \(\mathbf{n}\in\mathcal{V}_D^d\), 由此产生的评估高度估计为:
 846 -> \[ h_{\infty}(\psi_D^{(\mathbf{n})}) \le D \int_{\mathbf{T}^d} \max_{\mathbf{t} \in P_{\epsilon}^d} \left\{ \sum_{j=1}^d t_j \log |\varphi_{k(j)}(z_j)| \right\} \mu_{\text{Haar}} - |\mathbf{n}| \log |\varphi'_l(0)| - \sum_{j=1}^d n_j \log |\varphi'_{k(j)}(0)/\varphi'_l(0)| + o(D). \]
 847    
 848    由于在任何情况下我们都拥有平凡边界:
```


## File: `./tex/sec9.tex`

### Equation 35 (Line 307) - **19.47746pt too wide**

```latex
 305    在另一方面, 由于有理代数曲线的分支双重覆盖 \(X(2) \to X_0(2)\) 
 306    在我们形式级数展开的中心 h=0 （尖点 \(\tau=i\infty\)）处是完全分歧的, 
 307 -> 由引理 7.4.5 的投影公式紧接着有：在 \eqref{eq:9.0.22} 的 \(Y_0(2)\) 版本的 holonomy 商中的对应积分以及共形半径项都精确地被该覆盖的次数（在我们的情况下等于 2）所缩放. 
 308    在我们最基本的情况下, 我们可以通过如下一种非常直接以及显式的方式看到这一点. 
 309    让我们在上半平面 \(\tau \in \mathbf{H}\) 上将 hauptmodul h 评估于 \(e^{2\pi i\tau}\) 处的值写为 \(H(\tau)\), 
```

