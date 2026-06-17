# Math Display Overflow Audit — `CDT_L_2026`

Generated: 2026-06-15 11:24
LaTeX Log: `CDT_L_2026_Chn.log`
Total Unique Overfull Display Equations: 20

## ⚠️ Detected Math Display Overflows (> 5pt too wide)
The following display equations exceed the text margins, resulting in unreadable PDFs. You must split them using standard `aligned` environments or multi-line structures.


### File: `tex/sec1.tex`

#### Line 163 — 🔴 **85.40726pt too wide**
```latex
 161    
 162    \begin{lemma}[Simple Lemma]\label{lem:1.2.3}
 163 -> 一个在 $\mathbf{Z}[\![x]\!]$ 中的整系数幂级数, 如果定义了在半径为 $R > 1$ 的圆盘 $|x| < R$ 上的全纯函数, 那么它必定是一个多项式.
 164    \end{lemma}
 165    
```


### File: `tex/sec10.tex`

#### Line 158 — 🔴 **9.82484pt too wide**
```latex
 156    \frac{\iint_{\mathbf{T}^2} \log |\varphi(z) - \varphi(w)| \, \mu_{\text{Haar}}(z) \mu_{\text{Haar}}(w)}{\log 16 + \log |G'(0)| - \frac{552431}{242760}}.
 157    \end{equation}
 158 -> 使用 \S~A.2 中定义的 gobble 围道中（稍微）优化的选择 $\operatorname{Gob}(0.92, 110, 23)$，我们发现 $|G'(0)| = 0.9163768\dots$，并且商 \eqref{eq:10.3.4} 的计算结果大约为 $22.7527$，距离所需的阈值 $17$ 还有相当长的一段距离。$\vartriangle$
 159    \end{remark}
 160    
```


### File: `tex/sec13.tex`

#### Line 121 — 🔴 **29.71733pt too wide**
```latex
 119    
 120    在另一方面, 根据 \eqref{eq:8.0.2} 的定义,
 121 -> 通过仅考虑满足 \(n_{j_1} > n_{j_2} \implies i_{j_1} \ge i_{j_2}\) 的 \(\mathbf{n}\), 我们有一个容易的下界,
 122    并且有 \(\tau^{\flat\flat}(\mathbf{b}')\) 至少为:
 123    \[
```


### File: `tex/sec14.tex`

#### Line 584 — 🔴 **35.19937pt too wide**
```latex
 582    
 583    \begin{equation}\label{eq:14.5.4}
 584 -> \begin{aligned}
 585    \tau^{\sharp}(\mathbf{e}) &= \frac{2}{m^{2}} \min_{\xi \in [0, m]} \left\{ \xi \sum_{i=1}^{m} e_{i} \right. \\
 586    &\quad + \left. \left( \max_{1 \leq i \leq m} e_{i} \right) I_{\xi}^{m}(\xi) \right\} \\
```


### File: `tex/sec15.tex`

#### Line 148 — 🔴 **17.66562pt too wide**
```latex
 146    
 147    一种更一般的方案, 正如我们在第 3.3.3 以及 3.3.7 节中在最基本的例子上指出的那样,
 148 -> 可以通过形成由对一基本函数评估一正规形式的 Hermite--Pad{\'e} 逼近序列而获得的特殊线性形式的生成函数来予以寻求.
 149    Beukers \cite{Beu81}\cite{Beu84} （利用多重对数）以及 Pr{\'e}vost \cite{Pre96} （具有 \(\zeta(3, 1+1/y)\) 作为要在形如 y=1/n 处评估的基本函数）,
 150    各自都能够在这样的方案内解释 Ap{\'e}ry 序列.
```

#### Line 344 — 🔴 **50.85359pt too wide**
```latex
 342    具有满足 \(\varphi(z) = 4z/(1+z)^2\) 的 Riemann 映射共形半径 \(\rho(\Omega, 0) = 4\),
 343    并且它承认超越解析函数 \(\log(1-x) = -\sum_{n=1}^{\infty} x^n/n\),
 344 -> 其分母类型可以用具有 r=1 以及 \(b_1 = 1\) 的形式 \eqref{eq:2.7.8} 来表达.
 345    我们在该例中对于 \eqref{eq:2.7.9} 的右手边有 \((2/3) \log 4 = 0.924196 \dots\).
 346    
```

#### Line 357 — 🔴 **62.84981pt too wide**
```latex
 355    以便设计出一个关于集成素数计数函数估计的有理 Gelfond--Schnirelman 风格的初等证明：
 356    对所有足够大的 X, 均有 \(\int_1^X \psi(t) dt > (4/3) \log 2 \cdot X^2/2\).
 357 -> 这里的系数比 Chebyshev 的 \(\log \left(2^{1/2}3^{1/3}5^{1/5}30^{-1/30}\right) = 0.921292\ldots\)
 358    稍微好一些, 并且现在的关键在于该证明其实并不是新的：
 359    它是与 Bombieri、Nair 以及 Chudnovsky
```


### File: `tex/sec2.tex`

#### Line 187 — 🔴 **35.93895pt too wide**
```latex
 185    并带有它们自身且各不相同的对 Nevanlinna 生长特征的精细化表述,
 186    这在第 7.1.1 节中我们将其称为 Bost--Charles 特征.)
 187 -> 现在的关键点在于, 这一极限过程 $d \to \infty$ 的论证进一步允许了对 \eqref{eq:2.2.3} 到 \(\mathbf{Q}[\! [x]\!]\) 函数的推广中 \(\tau = b\sigma\) 项进行类似的``分母递增重排''改进.
 188    某种这样的改进对于我们定理 A 和 C 的所有证明都是必不可少的.
 189    我们确实也在第 7 节中对第 6 节的主要结果给用了单变量处理.
```

#### Line 307 — 🔴 **19.47746pt too wide**
```latex
 305    \subsection{超越对数的算术特征}\label{sec:2.8}
 306    
 307 -> 鉴于\autoref{thm:2.7.2}, 探求其他基本超越函数在其解析区域 and 幂级数算术行为方面的算术特征是非常自然的. 考虑到 Bely\u{\i} 定理 \cite{BG06}, 一个自然的起点是 (正是在\autoref{thm:2.7.2} 中) 解析开拓到沿所有在 $\mathbf{P}^1 \setminus \{0,1,\infty\}$ 中的路径的多值全纯函数幂级数. 相比于\autoref{thm:2.7.2} 的分母类型 \([1,\dots,n]\), 走得更远需要使用一个多值的映射 \(\varphi\), 但仍然需要一个局部单值性输入 (这将在第 2.9 节进行讨论, 并在定义 9.0.12 和推论 9.0.19 中形式化), 这对于我们的无理数证明方法至关重要.
 308    
 309    \begin{theorem}\label{thm:2.8.4}
```


### File: `tex/sec3.tex`

#### Line 113 — 🔴 **73.44116pt too wide**
```latex
 111    因为这一特化后的单项式恰好是使得 \(\gamma \cdot (\mathbf{x}^{(1)})^{\mathbf{k}}(\mathbf{x}^{(2)})^{\mathbf{n}_2}\) 是来自 \(F(\mathbf{x}^{(1)},\mathbf{x}^{(2)})\) 的单项式的那些 \(\gamma \cdot (\mathbf{x}^{(1)})^{\mathbf{k}}\).
 112    以此方式, \(\mathbf{n}_1 \in \mathcal{V}_{D,\Omega_1}^{I_1}\).
 113 -> 同理可得 \(\mathbf{n}_2 \in \mathcal{V}_{D,\Omega_2}^{I_2}\), 从而证明了所要求的包含关系 \(\mathcal{V}_{D,\Omega_1 \times \Omega_2}^{I_1 \times I_2} \subseteq \mathcal{V}_{D,\Omega_1}^{I_1} \times \mathcal{V}_{D,\Omega_2}^{I_2}\).
 114    \end{proof}
 115    
```

#### Line 208 — 🔴 **74.31647pt too wide**
```latex
 206    他的 (隐式) Roth 型猜想是它们实际上对于每个 \(\varepsilon > 0\) 都应当包含在 \(\{0, 1, \ldots, (2 + \varepsilon)D + O_{\varepsilon, \mathcal{L}}(1)\}\) 中.
 207    
 208 -> 在同年, Shidlovsky \cite{Shi59} (参见 \cite[§ 3.5, Lemma 8]{Shi89}, 或 \cite[§ VII.3]{Lan66})
 209    独立发现了在 \(\mathbf{C}(x)\) 上线性 ODE 情况下更精确的函数形式,
 210    并用它完成了 Siegel 关于 E-函数特殊值的代数无关性理论 \cite{Sie49} 的主要结果.
```


### File: `tex/sec6.tex`

#### Line 92 — 🔴 **42.06079pt too wide**
```latex
  90    
  91    \begin{corollary}\label{cor:6.0.14}
  92 -> 假设与定理~\ref{thm:6.0.2} 相同的条件和记号, 但更简单地考虑单个全纯映射 $\varphi: (\overline{\mathbf{D}}, 0) \to (\mathbf{C}, 0)$, 其满足 $|\varphi'(0)| > e^{\tau(\mathbf{b}; \mathbf{e})}$, 且使得拉回 $\varphi^* f_i$ 在开单位圆盘上是亚纯函数, 即 $\varphi^* f_i \in \mathcal{M}(\mathbf{D})$.
  93    如果要么 $|\varphi'(0)| > e^{\sigma_m}$, 要么所有函数 $f_i$ 都是 holonomic, 那么:
  94    \begin{equation}\label{eq:6.0.15}
```


### File: `tex/sec7.tex`

#### Line 126 — 🔴 **29.77345pt too wide**
```latex
 124    \[ \mathring{A}(r,\varphi) := \frac{1}{\pi} \iint_{D(0,r)} \frac{|\varphi'|^2}{(1+|\varphi|)^2} \, dx dy = \iint_{D(0,r)} \varphi^* \omega_{\mathrm{FS}} =: r \frac{d}{dr} \mathring{T}(r,\varphi). \]
 125    
 126 -> 现在, 通过将公式 \eqref{eq:7.1.8} 的分子解释为一个 Riemann 和, 在极限下（在假设对于 \(r \leq 1\) 均有 \(\widehat{A}(r,\varphi) \leq \widehat{A}(1,\varphi) \leq m\) 的前提下）, 我们得到以下结果:
 127    
 128    \begin{theorem}\label{thm:7.1.10}
```

#### Line 299 — 🔴 **25.29433pt too wide**
```latex
 297    \[ (E_{\mathbf{Q}_v}, \|\cdot\|_{E,v}) \hookrightarrow (F_{\mathbf{Q}_v}, \|\cdot\|_{F,v}) \]
 298    的算子范数的对数:
 299 -> \[ h_v(\psi) := \sup_{e \in E_{\mathbf{Q}_v} \setminus \{0\}} \log \frac{\|\psi(e)\|_{F,v}}{\|e\|_{E,v}} = \sup_{e \in E \setminus \{0\}} \log \frac{\|\psi(e)\|_{F,v}}{\|e\|_{E,v}}. \]
 300    \(\psi\) 的全局高度是所有地方 \(v \in M_{\mathbf{Q}}\) 上的局部 v-进高度的总和:
 301    \[ h(\psi) := \sum_{v \in M_{\mathbf{Q}}} h_v(\psi). \]
```

#### Line 697 — 🔴 **34.10042pt too wide**
```latex
 695    D(\overline{\mathcal{L}} \cdot \overline{\mathcal{L}}_r) = -\int_{\mathbf{T}} \log \|\varphi_r^* x^{-D}\|_{\varphi_r^* \overline{\mathcal{L}}^{\otimes D}} \mu_{\text{Haar}}.
 696    \end{equation}
 697 -> 为了证明它, 我们从 Poincaré--Lelong 公式开始, 该公式给出:
 698    \[ \frac{i}{\pi} \partial \overline{\partial} \log \|\varphi_r^*(x^{-D})\|_{\varphi_r^* \overline{\mathcal{L}}^{\otimes D}} = -c_1 \left( \varphi_r^* \overline{\mathcal{L}}^{\otimes D} \right), \]
 699    \[ \frac{i}{\pi} \partial \overline{\partial} \log^+ |z|^{-1} = -\delta_0 + \mu_{\text{Haar}}. \]
```


### File: `tex/sec8.tex`

#### Line 382 — 🔴 **11.56613pt too wide**
```latex
 380    以及在 \(\mathbf{P}^1(\mathbf{C})\) 上的 Fubini--Study 形式 \(\omega_{\text{FS}}\) 的 \(L^2\)-范数.
 381    因此, 根据引理 7.2.7, 我们有
 382 -> \[ \widehat{\operatorname{deg}}\,\Gamma\left(\mathcal{X},\overline{\mathcal{L}}^{\otimes D}\right) = d(D+1)^{d-1}\widehat{\operatorname{deg}}\,\Gamma\left(\mathbf{P}_{\mathbf{Z}}^{1},\overline{\mathcal{O}(1)}^{\otimes D}\right). \]
 383    现在, 第一个断言源于算术 Hilbert--Samuel 公式 \eqref{eq:7.3.4}.
 384    第二个断言根据 \eqref{eq:7.2.4} 源于第一个断言.
```

#### Line 399 — 🔴 **120.13292pt too wide**
```latex
 397    以及对剩下的这一个 \(\operatorname{pr}_{i}^{*}\mathcal{O}(1)\) 因子穿过两次.
 398    根据投影公式, 这为我们提供了
 399 -> \[ \overline{\mathcal{L}}^{d+1} = d \binom{d+1}{2} (d-1)! \left( \overline{\mathcal{O}(1)} \cdot \overline{\mathcal{O}(1)} \right), \]
 400    并且我们以此透视同样恢复了引理 8.2.5. \(\vartriangle\)
 401    \end{remark}
```

#### Line 508 — 🔴 **12.72002pt too wide**
```latex
 506    \[ \varphi_{\mathbf{r}}: \overline{\mathbf{D}}^d \to \mathbf{C}^d \hookrightarrow \mathcal{X}(\mathbf{C}), \qquad \mathbf{z} \mapsto (\varphi(r_1 z_1), \dots, \varphi(r_d z_d)). \]
 507    我们将使用 Poisson--Jensen 公式通过射流函数来约束 \(\log |c_{\mathbf{n}}|\),
 508 -> 随后借助 Poincaré--Lelong 公式将产生的边界与 \(\overline{\mathcal{L}}\) 的 Chern 形式联系起来.
 509    我们遵循第 7.4 节中的记号, 并且我们从 \eqref{eq:7.1.7} 借用斜率 \(\alpha_k\) 的记号.
 510    此外, 对于每个 \(\mathbf{n} \in \mathbf{N}^d\), 我们定义 \(r(\mathbf{n}) := (r(n_1), \ldots, r(n_d))\),
```

#### Line 518 — 🔴 **240.91583pt too wide**
```latex
 516    通篇本节, \(\mathbf{z} = (z_1, \dots, z_d)\) 表示 \(\overline{\mathbf{D}}^d\) 上的坐标.
 517    我们使用通过 \(\mathbf{x}^{-D} \mapsto \mathbf{1}\) 给出的、\(\mathcal{L}^{\otimes D}\) 在 \(\mathbf{A}^d_{\mathbf{C}}\)
 518 -> 上的平凡化 \(\mathcal{L}^{\otimes D}|_{\mathbf{C}^d} \stackrel{\simeq}{\to} \mathcal{O}_{\mathbf{C}^d}\).
 519    在此识别下, \(s/\mathbf{x}^{-D} = s \cdot \mathbf{x}^D =: G(\mathbf{x})\)
 520    自然在 \(\Gamma(\widehat{X}_0, \mathcal{O}_{\widehat{X}_0})\) 中且消逝阶数为 n.
```

#### Line 550 — 🔴 **26.61748pt too wide**
```latex
 548    \begin{aligned}
 549    &\int_{\mathbf{T}^d} \log \left| J_n \left( h(z_1) \cdots h(z_d) \cdot \varphi_{r(\mathbf{n})}^* G \right) \right| \mu_{\text{Haar}} \\
 550 -> &\quad \leq \int_{\mathbf{T}^d} \log \left| h(z_1) \cdots h(z_d) \cdot \varphi_{r(\mathbf{n})}^* G \right| \mu_{\text{Haar}} \\
 551    &\quad = \int_{\mathbf{T}^d} \log \left| \varphi_{r(\mathbf{n})}^* G \right| \mu_{\text{Haar}} + O_h(1).
 552    \end{aligned}
```

