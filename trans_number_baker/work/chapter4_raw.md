
fundamental studies on rational approximations to algebraic numbers; on writing the equation in the form

$$a(x-\alpha_1y)\ldots(x-\alpha_ny)=m,$$

one sees that one of the zeros  $\alpha$  of F(x, 1) has a rational approximation x/y (y > 0) with  $|\alpha - x/y| < c/y^n$  for some c depending only on F and m, and Thue showed that this is impossible if y is sufficiently large. Thue's work was much extended by Siegel<sup>‡</sup> in 1929; Siegel proved that the equation f(x, y) = 0, where f denotes a polynomial with integer coefficients, has only a finite number of solutions in integers x, y if the curve it represents has genus 1 or genus 0 and at least three infinite valuations; otherwise the curve can be parameterized and there are then infinitely many so-called 'ganzartige' solutions, that is, algebraic solutions with constant denominators. Siegel's work depended upon, amongst other things, an improved version of Thue's approximation result which he obtained in 1921, and the famous Mordell-Weil theorem, proved in 1928, on the finiteness of the basis of the group of rational points on the curve. The work of Thue and Siegel satisfactorily settles the question as to which curves possess only finitely many integer points and, moreover, it yields an estimate for the number of points when finite. But it throws no light on the basic Hilbert problem as to whether or not such points exist and, even less therefore, does it provide an algorithm for determining their totality; for the arguments depend on an assumption, made at the outset, that the equation has at least one large solution and this is purely hypothetical. Another proof of Thue's theorem, under a mild restriction, was given by Skolem in 1935 by means of a p-adic argument very different from the original, but here the work depends on the compactness property of the p-adic integers and so is again non-effective.

Our purpose here is to apply the work of Chapter 3 to effectively resolve a wide class of Diophantine equations. In particular we shall treat the Thue equation F(x,y)=m defined over any algebraic number field, the famous Mordell equation  $y^2=x^3+k$ , to which, incidentally, there attaches a history dating back to Bachet in 1621, and we shall obtain an effective algorithm for determining all the integer points on an arbitrary curve of genus 1. Our theorems will be proved in an essentially qualitative form, but it will be apparent that

```
† See Chapter 7.

§ M.Z. 10 (1921), 173-213.

¶ M.A. 111 (1935), 399-424.
```

<sup>‡</sup> Abh. Preuss. Akad. Wiss. (1929), no. 1. || Acta Math. 53 (1928), 281-315.

they can be adapted to yield explicit bounds for the sizes of all the solutions of the equations. A summary of quantitative aspects of the work is given in the last section.

# **2. The Thue equation**

Let *K* be an algebraic number field with degree *d,* let *ocv* ..., an be *n* > 3 distinct algebraic integers in *K,* and let *fi* be any non-zero algebraic integer in *K.* We prove:

## **Theorem 4.1.** *The equation*

$$(X - \alpha_1 Y) \dots (X - \alpha_n Y) = \mu$$

*has only a finite number of solutions in algebraic integers X, Y in K and these can be effectively determined.*

We define the *size* of any algebraic integer *6* in *K* as the maximum of the absolute values of its conjugates, and we signify the size of *8* by ||0||. With this notation, we shall in fact show how one can obtain an explicit bound for ||X|| and || *Y\\* for all *X, Y* as above. The bound can be expressed in terms of *d* and the maximum of the heights of alf ..., an, */i* and some algebraic integer generating *K;* we shall denote by clf c2,... positive numbers that can be specified in terms of these quantities only. We shall assume that *K* has *s* conjugate real fields and *It* conjugate complex fields so that *d* = *s + 2t;* further we shall signify by *(P\** 0<d) the conjugates of any element *6* of *K,* with *&•\*>, ...,&»* real and0<»+« #«+«> the complex conjugates of 0<»+«+» *ffM* respectively. The subsequent arguments rest on the well-known result, dating back to Dirichlet, that there exist r = *s +1 —* 1 units 7n ..., *yr* in *K* such that

$$\left|\log\left|\eta_i^{(j)}\right|\right| < c_1 \quad (1 \leqslant i, j \leqslant r)$$

and |A| > c2, where A denotes the determinant of order r with log| *v\<sup>n</sup> \* in the tth row and *jth* column.\*

We suppose now that *X, Y* are any algebraic integers in *K* satisfying the given equation and we write, for brevity,

$$\beta_i = X - \alpha_i Y \quad (1 \leqslant i \leqslant n).$$

We denote by *Nfi{* the field norm of *ftt* and we put *mi — \Nfit\,* so that *ml...mn* = *\N/i\.* We proceed first to show that an associate *yi* of /?t

**t Cf. Hooke (Bibliography).**

can be determined such that

$$|\log|\gamma_i^{(j)}|| < c_3 \quad (1 \le j \le d). \tag{1}$$

This follows in fact from the observation that every point P in r-dimensional Euclidean space occurs within a distance  $c_4$  of some point of the lattice with basis

$$(\log |\eta_i^{(1)}|, ..., \log |\eta_i^{(r)}|) \quad (1 \le i \le r).$$

On taking P as the point

$$(\log |\beta_i^{(1)}|, ..., \log |\beta_i^{(r)}|),$$

we deduce that there exist rational integers  $b_{i1}, ..., b_{ir}$  such that

$$\gamma_i = \beta_i \eta_1^{b_{i_1}} \dots \eta_r^{b_{i_r}} \tag{2}$$

satisfies (1) for  $1 \le j \le r$ , with  $c_4$  in place of  $c_3$ , and since

$$|\gamma_i^{(j+t)}| = |\gamma_i^{(j)}| \quad (s < j \le s+t),$$

the same holds for  $1 \le j \le d$  except possibly for j = s + t and j = s + 2t (only one of which exists if t = 0). But we have

$$\left|\gamma_i^{(1)}\dots\gamma_i^{(d)}\right| = m_i, \quad 1\leqslant m_i\leqslant \left|N\mu\right|\leqslant c_5,$$

whence (1) holds for all j, as required.

Now let  $H_i = \max |b_{ij}|$  and let l be a suffix for which  $H_l = \max H_i$ . The equations

$$\log |\gamma_i^{(j)}/\beta_i^{(j)}| = b_{i1} \log |\eta_1^{(j)}| + \dots + b_{i_r} \log |\eta_r^{(j)}| \quad (1 \le j \le r)$$

serve to express each number  $\Delta b_{ij}$  as a linear combination of the numbers on the left with coefficients given by cofactors of  $\Delta$ , and thus the maximum of the absolute values of these numbers exceeds  $c_8H_i$ . Let the maximum be given by j=J. Then from (1) we have

$$\left|\log\left|\beta_i^{(J)}\right|\right| = \left|\log\left|\beta_i^{(J)}/\gamma_i^{(J)}\right| + \log\left|\gamma_i^{(J)}\right|\right| > c_6H_i - c_3,$$

and, since  $|\beta_i^{(1)} \dots \beta_i^{(d)}| = m_i$ , it follows that

$$\log |\beta_i^{(h_i)}| < -(c_6 H_i - c_3 - \log m_i)/(d-1)$$

for some  $h_i$ . Thus, if  $H_l > c_7$ , we have  $|\beta_l^{(h)}| < e^{-c_4 H_l}$  for some h. Further, since  $\beta_1^{(h)} \dots \beta_n^{(h)} = \mu^{(h)}$ ,

we obtain  $|\beta_k^{(h)}| > c_0$  for some  $k \neq l$ . We take j to be any suffix other than k or l; this exists since, by hypothesis,  $n \geq 3$ .

We may now, for simplicity, omit the superscript h and assume that  $\alpha_i^{(h)} = \alpha_i$ ,  $\beta_i^{(h)} = \beta_i$ . From the identity

$$(\alpha_k - \alpha_l) \beta_j + (\alpha_l - \alpha_j) \beta_k + (\alpha_j - \alpha_k) \beta_l = 0,$$

we obtain

$$\eta_1^{b_1} \dots \eta_r^{b_r} - \alpha = \omega,$$

where

$$b_s = b_{ks} - b_{js} \quad (1 \leqslant s \leqslant r),$$

$$\alpha = \frac{(\alpha_j - \alpha_l) \, \gamma_k}{(\alpha_k - \alpha_l) \, \gamma_j}, \quad \omega = \frac{(\alpha_k - \alpha_j) \, \beta_l \, \gamma_k}{(\alpha_k - \alpha_l) \, \beta_k \, \gamma_j}.$$

On noting that, for any complex number z, the inequality  $|e^z - 1| < \frac{1}{4}$  implies that  $|z - ib\pi| \le 4 |e^z - 1|$ .

for some rational integer b, we deduce easily, on taking

$$z = b_1 \log \eta_1 + \ldots + b_r \log \eta_r - \log \alpha,$$

where the logarithms have their principal values, that, if  $|\omega/\alpha| < \frac{1}{4}$ , then  $|\Lambda| \le 4 |\omega/\alpha|$ , where  $\Lambda = z - b \log (-1)$ . Clearly  $\omega \neq 0$  and so also  $\Lambda \neq 0$ . Further we see that  $|b_j| \le 2H_l$  for all j, and so the imaginary part of z has absolute value at most  $\pi B$ , where  $B = 4rH_l$ . Thus we have  $|b| \le B$ , and certainly  $|b_j| \le B$ . Furthermore, from the estimates for  $\beta_k = \beta_k^{(h)}$  and  $\beta_l = \beta_l^{(h)}$  given above, we see that, if  $H_l > c_{10}$ , then

$$4|\omega/\alpha| < c_{11}|\beta_l/\beta_k| < e^{-c_{12}B}$$
.

But  $\eta_1, ..., \eta_r$  and  $\alpha$  have degrees at most d, and their heights are bounded above by a number  $c_{13}$ . Hence Theorem 3.1 gives  $|\Lambda| > B^{-C}$  for some C as above, and from this and our estimate  $|\Lambda| < e^{-c_{13}B}$  we conclude that  $B < c_{14}$ , whence  $H_l < c_{15}$ . It follows from (1) and (2) that

$$\|\beta_i\| < e^{c_{14}H_i} < c_{17},$$

and now the equations

$$X = \frac{\alpha_2 \beta_1 - \alpha_1 \beta_2}{\alpha_2 - \alpha_1}, \quad Y = \frac{\beta_1 - \beta_2}{\alpha_2 - \alpha_1}$$

and their conjugates clearly imply the validity of Theorem 4.1.

# 3. The hyperelliptic equation

As in § 2, we signify by K an algebraic number field with degree d. We suppose that  $\alpha_1, \ldots, \alpha_n$  are  $n \ge 3$  algebraic integers in K with, say,  $\alpha_1, \alpha_2, \alpha_3$  distinct and different from  $\alpha_4, \ldots, \alpha_n$ , and we prove:

Theorem 4.2. The equation

$$Y^2 = (X - \alpha_1) \dots (X - \alpha_n) \tag{3}$$

has only a finite number of solutions in algebraic integers X, Y in K and these can be effectively determined.

We shall establish Theorem 4.2 from Theorem 4.1 by a method of Siegel,<sup>†</sup> and again it will be clear that the arguments enable one to furnish explicit bounds for ||X|| and ||Y||. The conclusion of Theorem 4.2 plainly remains valid if a non-zero factor in K is introduced on the right of (3), and thus the theorem covers, in particular, the elliptic equation  $u^2 = ax^3 + bx^2 + cx + d.$ 

where all quantities signify rational integers. In this case, however, the result can be derived from Theorem 4.1 by a readier method, due to Mordell, involving the theory of the reduction of binary quartic forms.<sup>‡</sup>

Suppose now that X, Y are non-zero algebraic integers in K satisfying (3). We show first that there exist algebraic integers  $\xi_j$ ,  $\eta_j$ ,  $\zeta_j$  (j=1,2,3) in K with

$$X - \alpha_j = (\xi_j/\eta_j) \, \xi_j^2,$$

$$\max (\|\xi_j\|, \|\eta_j\|) < c_1,$$
(4)

where  $c_1$ , like  $c_2, c_3, \ldots$ , denotes a positive number specified as in § 2, that is, depending only on d and the maximum of the heights of  $\alpha_1, \ldots, \alpha_n$  and some algebraic integer generating K. For simplicity we write  $\alpha = \alpha_i$ , and we observe that, by virtue of the ideal equation

$$[Y^2] = [X - \alpha_1] \dots [X - \alpha_n],$$
$$[X - \alpha] = \mathfrak{ab}^2$$

we have

for some ideals a, b in K, where a divides

$$\prod_{i+j} [\alpha - \alpha_i].$$

Further, there exist ideals a', b' in the ideal classes inverse to those of a, b respectively with norms at most  $c_2$ , and clearly aa' and  $a'b'^2$  are principal ideals; the latter are therefore generated by algebraic integers  $\xi'$ ,  $\eta'$  in K with

$$|N\xi'| \leqslant c_2 Na$$
,  $|N\eta'| \leqslant c_2^3$ .

† J. London Math. Soc. 1 (1926), 66-8.

<sup>‡</sup> J. London Math. Soc. 43 (1968), 1-9.

Furthermore, since  $Na \leq \prod_{i+j} N[\alpha - \alpha_j] < c_3$ ,

it follows easily, as in the derivation of (1), that there exist associates  $\xi''$ ,  $\eta''$  of  $\xi'$ ,  $\eta'$  respectively satisfying

$$\max(\|\xi''\|, \|\eta''\|) < c_4.$$

Now bb' is principal and is therefore generated by some algebraic integer  $\zeta'$  in K. Hence from the equation

$$(a'b'^2)[X-\alpha] = (aa')(bb')^2$$

we obtain

$$X-\alpha=\epsilon(\xi''/\eta'')\,\zeta'^2$$
,

where  $\epsilon$  denotes a unit in K. By Dirichlet's theorem there exists a fundamental system  $\epsilon_1, \ldots, \epsilon_r$  of units in K satisfying

$$\max \left(\left\| \epsilon_1 \right\|, ..., \left\| \epsilon_r \right\| \right) < c_5,$$

and we have

$$\epsilon = \rho \epsilon_1^{j_1} \dots \epsilon_r^{j_r}$$

for some rational integers  $j_1, ..., j_r$  and some root of unity  $\rho$ ; it is now clear that the numbers  $\xi, \eta, \zeta$  given by

$$\xi'' \rho \epsilon_1^{i_1} \dots \epsilon_r^{i_r}, \quad \eta'', \quad \zeta' \epsilon_1^{\frac{1}{2}(j_1-j_1')} \dots \epsilon_r^{\frac{1}{2}(j_r-j_r')}$$

respectively, where  $j_i' = 0$  or 1 according as  $j_i$  is even or odd, have the required properties.

On eliminating X from (4) we obtain three equations of the form

$$\sigma_2 \zeta_2^2 - \sigma_3 \zeta_3^2 = \alpha_3 - \alpha_2,$$

where  $\sigma_j = \xi_j/\eta_j$  (j = 1, 2, 3). Further, on writing

$$\beta_1 = \sigma_2^{\frac{1}{2}} \zeta_2 - \sigma_3^{\frac{1}{2}} \zeta_3$$

for any choice of the square roots, and defining  $\beta_2$ ,  $\beta_3$  similarly by cyclic permutation of the suffixes, we have

$$\beta_1 + \beta_2 + \beta_3 = 0. \tag{5}$$

Now  $\beta_1$  is a non-zero element of the field generated by  $\sigma_2^{\frac{1}{2}}$  and  $\sigma_3^{\frac{1}{2}}$  over K; further, on multiplying by  $\delta = \eta_1 \eta_2 \eta_3$ , one obtains an algebraic integer with field norm having absolute value at most  $c_6$ . It follows easily, as above, that  $\delta \beta_1 = \beta_1' c_1^3$  for some unit  $c_1$  in the field and some associate  $\beta_1'$  with  $\|\beta_1'\| < c_7$ ; and, after permutation of suffixes, the same holds for  $\beta_2$ ,  $\beta_3$ . Thus (5) gives

$$\beta_1' \epsilon_1^3 + \beta_2' \epsilon_2^3 + \beta_3' \epsilon_3^3 = 0,$$

and, on multiplying by /?i2 /ei, this becomes a Thue equation

$$x^3 - \lambda y^3 = \mu,$$

where 
$$x = \beta_2' \epsilon_2 / \epsilon_3, \quad y = \epsilon_1 / \epsilon_3.$$

Hence, by Theorem 4.1, ||a;|| and ||y|| are at most c8, and it remains only to show that |Z|| and || *Y\\* are likewise bounded.

Fixing the choice of the sign of erf, one can plainly select the sign of erf in *fi3* so that |e3| < c,. Then the bound *\y\ <* c8 established above gives *\ex\ <* c10, whence, since *\S\ >* c <sup>u</sup> , we obtain *\fix\* < c12. But this holds for either choice of the sign of crj and thus we conclude that both |£2| and |£3| are at most c13. It is now apparent from (4) that *\X\ <* cM; on commencing with the equations conjugate to (3) we derive the same bound for each conjugate of *X,* and the theorem follows.

# **4. Curves of genus 1**

Let *f{x,y)* be an absolutely irreducible polynomial with integer coefficients such that the curve/(ar, *y)* = 0 has genus 1. We prove:

**Theorem 4.3.** *The equation f(x,y) =* 0 *has only a finite number of solutions in integers x, y and these can be effectively determined.*

As mentioned in §1, the first part of the theorem was initially established by Siegel in 1929, but his method of proof was ineffective. The argument we shall give here, which is based on a birational transformation that reduces the equation to the canonical form considered in Theorem 4.2, provides an effective and simpler proof of Siegel's theorem in the case of curves of genus 1; but it does not seem to extend easily to curves of higher genus.

We shall denote by Q, *Q.(x)* and *K* respectively the field of all algebraic numbers, the field of rational functions in *x* with coefficients in Q, and the finite algebraic extension of Q(a;) formed by adjoining a root of /(x, *y)* = 0. By the Riemann-Roch theorem, there exist rational functions *Xx, Xt* on the curve with orders —2,-3 respectively at some fixed infinite valuation, say *Q,* of *K,* and with non-negative orders at all other valuations of *K;* moreover, one can effectively determine the algebraic coefficients in their Puiseux expansions. We now observe, following Chevalley, that the seven functions 1, *Xx, Xs, X\, X\, X\, XtXt* have poles of order at most 6 at *Q* and so, by the Riemann-Roch theorem again, they are linearly dependent over Q.

**Let** *pv ...,p7* be the respective coefficients in the linear equation relating them; clearly we havep6 4= 0, for the six functions excluding *X\* have distinct orders at *Q.* On writing

$$X = X_{1}, \quad Y = 2p_{5}X_{2} + p_{7}X_{1} + p_{3},$$
 we obtain 
$$Y^{2} = aX^{3} + bX^{2} + cX + d,$$

where *a, b,* c, *d* are polynomials in *plt ...,p7* with integer coefficients. The cubic on the right has distinct zeros, for if the equation reduced to

$$\{Y/(X-\alpha)\}^2=\alpha(X-\beta),$$

then *Y/(X —* a) could possess a pole only at *Q;* but, since *Xv X%* have orders —2,-3 respectively at *Q* and *p6* # 0, the function has in fact a pole of order 1 at *Q,* contrary to the Riemann-Roch theorem.

We observe now that, since *Xlt X2* are rational functions of *x, y* with coefficients in a fixed field, the functions *X, Y* become algebraic numbers in a fixed field when x, *y* are rational integers. Moreover, there exists a non-zero rational integer *q,* independent of a; and *y,* such that *qX* and *qY* are algebraic integers; for the function *X* = *X<sup>t</sup>* has a pole only at the infinite valuation *Q* and thus the equation satisfied by *X* over Q(x) has the form

$$X^{m} + P_{1}(x) X^{m-1} + \ldots + P_{m}(x) = 0,$$

where TO is the degree of/ in *y* and Px *Pm* are polynomials in *x* with algebraic coefficients and degree at most 2. We conclude from Theorem 4.2 that *X, Y* can take only finitely many values when *x, y* are rational integers. On noting again that *X* has a pole at *Q,* it follows at once that there are only finitely many x, and, in view of the initial equation /(x, *y)* = 0, so also finitely many *y.* Further, it is readily confirmed that all the arguments employed above are, in principle, effective, and this proves Theorem 4.3.

The method of proof can easily be extended to treat curves of genus 0 when there exist at least three infinite valuations, and this together with the above result enables one to resolve effectively the general cubic equation /(x, *y) =* 0; the latter can, however, be reduced more directly to the form considered in Theorem 4.2.

# **5. Quantitative bounds**

**As remarked earlier,** the arguments employed here enable one to **furnish explicit upper** bounds for the size of all the solutions of the **above equations.** To calculate these bounds one needs first **a** quantitative version of Theorem 3.1, and, in this connexion, the most useful result so far established reads:

If  $\alpha_1, ..., \alpha_n$  are  $n \ge 2$  non-zero algebraic numbers with degrees and heights at most  $d \ (\ge 4)$  and  $A \ (\ge 4)$  respectively, and if rational integers  $b_1, ..., b_n$  exist with absolute values at most B such that

$$0 < |b_1 \log \alpha_1 + \ldots + b_n \log \alpha_n| < e^{-bB},$$

where  $0 < \delta \leqslant 1$ , and the logarithms have their principal values, then

$$B < (4^{n^2} \delta^{-1} d^{2n} \log A)^{(2n+1)^2}.$$

By applying this together with certain estimates for units in algebraic number fields, it has been shown that all solutions X, Y of the Thue equation referred to in Theorem 4.1 satisfy

$$\max(||X||, ||Y||) < \exp\{(dH)^{(10d)^5}\},\$$

where H denotes the maximum of the heights of  $\alpha_1, \ldots, \alpha_n, \mu$  and some algebraic integer generating K.<sup>‡</sup> This leads to the bound

$$\exp \exp \left(d^{10d^2}H^{d^2}\right)$$

for the sizes of all solutions X, Y of the hyperelliptic equation discussed in Theorem 4.2. Further, employing the latter estimate and an effective construction for rational functions, it has been proved that all integer points x, y on the curve f(x,y) = 0 of Theorem 4.3 satisfy  $\max(|x|,|y|) < \exp\exp\{(2H)^{10^{n/2}}\}$ ,

where H denotes the maximum of the absolute values of the coefficients of f and n denotes its degree.

In special cases one has stronger bounds. For instance, for the elliptic equation mentioned after the enunciation of Theorem 4.2, the estimate  $\max (|x|, |y|) < \exp \{(10^6 H)^{10^6}\}$ 

has been established, where a, b, c, d are assumed to have absolute values at most H; and for the Mordell equation  $y^2 = x^3 + k$ , it has been shown, by way of an expression for C in terms of  $\Omega$  similar to that recorded after Theorem 3.1, that the bound  $\exp(c|k|^{1+\epsilon})$  is valid for any  $\epsilon > 0$ , where c depends only on  $\epsilon$ . Furthermore, techniques have been devised which, for a wide range of numerical examples, render the problem of determining the complete list of solutions in question accessible to machine computation; thus, for example, it has been proved that the only integer solutions of the pair of equations

<sup>†</sup> Mathematika, 15 (1968), 204-16.

<sup>†</sup> Phil. Trans. Roy. Soc. London, A 263 (1968), 173-91; P.C.P.S. 65 (1969), 439-44. † P.C.P.S. 68 (1970), 105-23 (J. Coates). || P.C.P.S. 67 (1970), 595-602.

<sup>¶</sup> Acta Arith. 24 (1973), 251-9 (H. Stark).

 $3x^2-2=y^2$  and  $8x^2-7=z^2$  are given by x=1 and x=11, and that the equation  $y^2=x^3-28$  has only the solutions given by x=4, 8, 37 (the corresponding values of y being  $\pm 6$ ,  $\pm 22$ ,  $\pm 225$  respectively).

Much interest attaches to the size of the solutions of the original Thue equation F(x,y)=m (see §1) relative to m. As a consequence of the third inequality for  $|\Lambda|$  recorded after the enunciation of Theorem 3.1, the arguments leading to Theorem 4.1 show that, if  $m \ge 2$ , then |x| and |y| cannot exceed  $m^C$  for some computable C depending only on F. This yields at once an improvement on Liouville's theorem; indeed, with the notation of Theorem 1.1, we have

$$|\alpha - p/q| > c/q^{\kappa}$$

for all rationals p/q (q>0), where c,  $\kappa$  are positive numbers, effectively computable in terms of  $\alpha$ , with  $\kappa < n$ . The result, in slightly weaker form, was first established in 1967, particular cases, however, having been obtained a few years earlier by means of special properties of Gauss' hypergeometric function. For instance it had been proved that when  $\alpha$  is the cube-root of 2 and 17 then the above inequality holds with  $c=10^{-6}$ ,  $\kappa=2.955$  and  $c=10^{-9}$ ,  $\kappa=2.4$  respectively, values in fact that are almost certainly sharper than those given by the more general techniques. But, leaving aside the effective nature of c, much more about rational approximations to algebraic numbers is known from the field of research begun by Thue, and this will be the theme of Chapter 7.

Various other equations can be treated by the methods described here. They can be used, for instance, to give bounds for all solutions in integers x, y of the equation  $y^m = f(x)$ , where m > 2 and f denotes any polynomial with integer coefficients possessing at least two distinct zeros; in particular, they enable one to solve effectively the Catalan equation  $x^m - y^n = 1$  for any given m, n. Moreover, they can be generalized by means of analysis in the p-adic domain to furnish all rational solutions of the equations F(x,y) = m and  $y^2 = x^3 + k$  whose denominators are comprised solely of powers of fixed sets of primes; thus, more especially, they yield an effective determination of all elliptic curves with a given conductor.

```
† Quart. J. Math. Oxford Ser. (2) 20 (1969), 129-37; J. Number Th. 4 (1972), 107-17. ‡ I.A.N. 35 (1971), 973-90.
```

<sup>§</sup> Phil. Trans. Roy. Soc. London, A 263 (1968), 173-91.

<sup>||</sup> Proc. London Math. Soc. 4 (1964), 385-98.

<sup>¶</sup> Quart. J. Math. Oxford Ser. (2) 15 (1964), 375-83.

<sup>††</sup> P.C.P.S. 65 (1969), 439-44. In fact R. Tijdeman has recently shown that they enable one to give an effective bound for all solutions x, y, m, n of the Catalan equation.

†† Acta Arith. 15 (1969), 279-305; 16 (1970), 399-412, 425-35 (J. Coates).
