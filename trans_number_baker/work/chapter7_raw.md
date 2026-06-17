$$f(z_1, z_2) = \alpha_1 \omega_1 z_1 + \alpha_2 \omega_2 z_2 + \beta_1 \zeta_1(\omega_1 z_1) + \beta_2 \zeta_2(\omega_2 z_2).$$

The function is constructed to satisfy

$$\Phi_{m_1, m_2}(s+\frac{1}{2}, s+\frac{1}{2}) = 0$$

for all integers s with  $1 \le s \le h$  and all non-negative integers  $m_1$ ,  $m_2$  with  $m_1 + m_2 \le k$ , where the suffixes denote partial derivatives as in Chapter 2.

The essence of the proof is an extrapolation algorithm analogous to that described in connexion with linear forms in logarithms, but the order of  $\Phi$  here is greater than in the earlier work and, to compensate, rational extrapolation points with large denominators are utilized; an important rôle in the discussion is therefore played by the division value properties of the elliptic functions. The counterpart of Lemma 4 of Chapter 2 asserts that, for any integer J between 0 and 50 inclusive, we have

$$\Phi_{m_1, m_2}(s + r/q, s + r/q) = 0$$

for all integers q, r, s with q even, (r,q) = 1,

$$1\leqslant q\leqslant 2h^{\frac{1}{4}J},\quad 1\leqslant s\leqslant h^{\frac{1}{4}J+1},\quad 1\leqslant r< q,$$

and all non-negative integers  $m_1$ ,  $m_2$  with  $m_1 + m_2 \leq k/2^J$ . The demonstration proceeds by induction and involves an application of the maximum-modulus principle as in the original lemma. It also utilizes the observation that, apart from a factor  $\omega_1^{m_1}\omega_2^{m_2}$ , the number on the left of the required equation is algebraic with degree at most  $c'q^4$ , where c' is defined like c above; and precise estimates for the number and its conjugates are furnished by division value theory. One concludes from the lemma that

$$\Phi_{m_1, m_2}(s+\frac{1}{4}, s+\frac{1}{4}) = 0 \quad (1 \le s \le L+1, \ 0 \le m_1, m_2 \le L),$$

which is clearly a system of  $(L+1)^3$  linear equations in the same number of variables  $p(\lambda_0, \lambda_1, \lambda_2)$ ; on noting that, for any regular function f, the determinant or order n with the ith derivative of  $(f(z))^j$  in the ith row and jth column has value

$$2! \dots n! (f'(z))^{\frac{1}{2}n(n+1)},$$

one easily verifies that the system of equations is untenable, and this proves Theorem 6.6.

The special case of the theorem when  $\wp_1$ ,  $\wp_2$  are the same  $\wp$ -function, say  $\wp$ , is of particular interest. For then  $\omega_1$ ,  $\omega_2$  can be taken as a pair of fundamental periods of  $\wp$  and we have the Legendre relation

$$\eta_1\omega_2-\eta_2\omega_1=2\pi i.$$

In this case Coates t and more recently Masser t have much extended the arguments and have proved:

**Theorem 6.7.** The space spanned by 1,  $\omega_1$ ,  $\omega_2$ ,  $\eta_1$ ,  $\eta_2$  and  $2\pi i$  over the algebraic numbers has dimension either 4 or 6 according as  $\wp$  does or does not admit complex multiplication.

The theorem clearly exhibits a non-trivial example of five numbers that are algebraically dependent but linearly independent over the algebraic numbers. Moreover it implies that, when  $\wp$  admits complex multiplication, the numbers in question satisfy an algebraic linear relation other than that between the periods; this was discovered by Masser. It takes the form

$$a\eta_{2}-c\tau\eta_{1}=\gamma\omega_{0}$$

where  $\gamma$  is algebraic and a, c are the integers occurring in the equation

$$a + b\tau + c\tau^2 = 0$$

satisfied by  $\tau = \omega_1/\omega_2$ . A necessary and sufficient condition for  $\gamma$  to be 0 is that either  $g_2$  or  $g_3$  be 0, and thus one deduces that  $\eta_1/\eta_2$  is transcendental if and only if neither invariant vanishes. The theorem also shows, for instance, that  $\pi + \omega$  and  $\pi + \eta$  are transcendental for any period  $\omega$  of  $\omega(z)$  and quasi-period  $\eta$  of  $\omega(z)$ . The transcendence of  $\omega(z)$  incidentally, follows from Theorem 6.1 by way of the functions  $\omega(\omega z/\pi)$  and  $\omega(z)$ .

The demonstration of Theorem 6.6 extends easily to establish, under the conditions appertaining to Theorem 6.7, the transcendence of any

<sup>†</sup> Amer. J. Math. 93 (1971), 385-97; Inventiones Math. 11 (1970), 167-82.

<sup>†</sup> Ph.D. Thesis, Cambridge, 1974.

non-vanishing linear combination of  $\omega_1$ ,  $\omega_2$ ,  $\eta_1$ ,  $\eta_2$  and  $2\pi i$ ; the auxiliary function now takes the form

$$\begin{split} \Phi(z_1,z_2,z_3) &= \sum_{\lambda_{\mathfrak{s}}=0}^L \ldots \sum_{\lambda_{\mathfrak{s}}=0}^L p(\lambda_0,\ldots,\lambda_3) \\ &\quad \times (f(z_1,z_2,z_3))^{\lambda_0} (\wp_1(\omega_1z_1))^{\lambda_1} (\wp_2(\omega_2z_2))^{\lambda_3} e^{2\pi i \lambda_3 z_3}, \end{split}$$

where  $L = [k^{\frac{1}{2}}]$  and  $f(z_1, z_2, z_3)$  is the sum of  $f(z_1, z_2)$ , as defined above, and an algebraic multiple of  $\pi z_3$ . Here, however, it is necessary to appeal to another remarkable property of the division values, namely that, for any positive integer n, the field obtained by adjoining  $\wp(\omega_1/n)$ ,  $\wp(\omega_2/n)$ ,  $\wp'(\omega_1/n)$  and  $\wp'(\omega_2/n)$  to  $K = Q(g_2, g_3, e^{2\pi i/n})$  has degree at most  $2n^3$  over K; this ensures that the estimate  $c'q^4$  referred to above remains unaltered in the present context. To complete the proof of Theorem 6.7 one has to establish the linear independence over the algebraic numbers of  $\omega_1$ ,  $\eta_1$  and  $2\pi i$  in the case when  $\omega$  admits complex multiplication, and of these, together with  $\omega_2$ ,  $\eta_3$ , in the case when to does not. The work runs on similar lines, using slightly modified auxiliary functions, but the determinant arguments at the end are no longer applicable; ad hoc techniques have been introduced to overcome this difficulty involving, in particular, new considerations on the density of zeros of meromorphic functions. The linear independence of  $\omega_1, \omega_2$  and  $2\pi i$  was in fact proved first by Coates utilizing a deep result of Serre, but Masser later verified this more elementarily.

In another direction, the work has been refined to yield estimates from below for linear forms in periods and quasi-periods. They show, for instance, that for any  $\wp$ -function with algebraic invariants, for any  $\varepsilon > 0$ , and for any positive integer n,

$$|\wp(n)| < C n^{(\log \log n)^{7+\epsilon}},$$

where C depends only on  $g_2$ ,  $g_3$  and  $\epsilon$ .<sup>†</sup> In fact a similar result has been established for  $\wp(\pi+n)$  and for  $\wp(\alpha)$ , where  $\alpha$  is any non-zero algebraic number. The estimate compares well with the lower bound  $|\wp(n)| > Cn$  valid for some C > 0 and infinitely many n.

Finally, as a further example of the type of theorem that has been obtained by the above methods, we mention a recent result of Masser<sup>‡</sup> concerning algebraic points on elliptic curves; he has proved, namely, that if  $\wp(z)$  has algebraic invariants and admits complex multiplication, then any numbers  $u_1, \ldots, u_n$  for which  $\wp(u_i)$  is algebraic are

<sup>†</sup> Amer. J. Math. 92 (1970), 619-22 (A. Baker); P.C.P.S. 73 (1973), 339-50 (D. W. Masser).

‡ Ph.D. Thesis, Cambridge, 1974.

either linearly dependent over *Qicojcj^)* or linearly independent over the field of all algebraic numbers. It would be of much interest to establish a theorem of the latter kind more generally for all p-functions with algebraic invariants, and it would likewise be of interest to extend Theorem 6.6 to apply to any number of ^-functions; both problems, however, seem out of reach at present.

# RATIONAL APPROXIMATIONS TO ALGEBRAIC NUMBERS

#### 1. Introduction

In 1909, a remarkable improvement on Liouville's theorem was obtained by the Norwegian mathematician Axel Thue. † He proved that for any algebraic number  $\alpha$  with degree n > 1 and for any  $\kappa > \frac{1}{2}n + 1$  there exists  $c = c(\alpha, \kappa) > 0$  such that  $|\alpha - p/q| > c/q^{\kappa}$  for all rationals p/q (q>0). His work rested on the construction of an auxiliary polynomial in two variables possessing zeros to a high order. and it can be regarded as the source of many of our modern transcendence techniques. The condition on  $\kappa$  was relaxed by Siegel<sup>‡</sup> in 1921 to  $\kappa > s + n/(s+1)$  for any positive integer s, thus, in particular, to  $\kappa > 2\sqrt{n}$ , and it was further relaxed by Dyson! and Gelfond! independently in 1947 to  $\kappa > \sqrt{(2n)}$ . The latter expositions continued to involve polynomials in two variables and further progress seemed to require some extension of the arguments relating to polynomials in many variables; in fact special results in this connexion had already been obtained by Schneider in 1936. A generalization of the desired kind was discovered by Roth<sup>††</sup> in 1955; he showed indeed that the above proposition holds for any  $\kappa > 2$ , a condition which, in view of the introductory remarks of Chapter 1, is essentially best possible.

Roth's work, however, gave rise to a number of further problems. Siegel had initiated studies on the approximation of algebraic numbers by algebraic numbers in a fixed field, and also by algebraic numbers with bounded degree, and although Roth's arguments could be readily generalized to furnish a best possible result in connexion with the first topic,<sup>‡‡</sup> they did not seem to admit a similar extension in connexion with the second. Even less, therefore, did they appear capable of dealing with the wider question concerning the simultaneous approximation of algebraic numbers by rationals. The whole subject was resolved by Schmidt<sup>#</sup> in 1970; building upon Roth's foundations but

```
† J.M. 135 (1909), 284–305.
§ Acta Math. 79 (1947), 225–40.
¶ J. M. 175 (1936), 182–92.
‡ See LeVeque (Bibliography).

‡ M.Z. 10 (1921), 173–213.

| Bibliography.

† Mathematika, 2 (1955), 1–20.

§ Bibliography.
```

introducing several new ideas, in particular from the Geometry of Numbers, he proved:

**Theorem 7.1.** For any algebraic numbers  $\alpha_1, ..., \alpha_n$  with  $1, \alpha_1, ..., \alpha_n$  linearly independent over the rationals, and for any  $\epsilon > 0$ , there are only finitely many positive integers q such that

$$q^{1+\epsilon}\|q\alpha_1\|\dots\|q\alpha_n\|<1.$$

Here ||x|| denotes the distance of x from the nearest integer taken positively. The theorem implies, by a classical transference principle, that there are only finitely many non-zero integers  $q_1, ..., q_n$  with

$$|q_1 \dots q_n|^{1+\epsilon} ||q_1 \alpha_1 + \dots + q_n \alpha_n|| < 1.$$

Further, as immediate corollaries, we see that there are only finitely many integers  $p_1, \ldots, p_n, q \ (q > 0)$  satisfying

$$|\alpha_j - p_j/q| < q^{-1-(1/n)-\epsilon} \quad (1 \leqslant j \leqslant n),$$

and also only finitely many integers  $p, q_1, ..., q_n$  satisfying

$$|q_1\alpha_1+\ldots+q_n\alpha_n-p|< q^{-n-\epsilon},$$

where  $q = \max |q_j|$ . Furthermore we have:

**Theorem 7.2.** For any algebraic number  $\alpha$  with degree exceeding n and any  $\epsilon > 0$ , there are only finitely many algebraic numbers  $\beta$  with degree at most n such that  $|\alpha - \beta| < B^{-n-1-\epsilon}$ , where B denotes the height of  $\beta$ .

The theorem follows from the inequality just above with  $\alpha_j = \alpha^j$ , on noting that, if P(x) is the minimal polynomial for  $\beta$ , then

$$|P(\alpha)| < BC|\alpha - \beta|$$

for some C depending only on  $\alpha$ . The exponent of B is essentially best possible, as has been demonstrated by Wirsing. In fact, Wirsing obtained Theorem 7.2 in 1965 before the work of Schmidt, but with the less precise exponent  $-2n - \epsilon$ .

One of the main applications of the methods of this chapter has concerned Diophantine equations of norm form in several variables, which generalize the Thue equation discussed in Chapter 4; indeed the

<sup>†</sup> See Cassels' Diophantine approximation (Bibliography).

<sup>‡</sup> J. M. 206 (1961), 67-77.

<sup>§</sup> Proc. Symposia Pure Math. (Amer. Math. Soc.), 20 (1971), 213-47.

work has led to a complete description of all such equations that possess only finitely many solutions.

**Theorem 7.3.** Let K be an algebraic number field and let M be a module in K. A necessary and sufficient condition for there to exist an integer m such that the equation  $N\mu = m$  has infinitely many solutions  $\mu$  in M is that M be a full module in some subfield of K which is neither the rational nor an imaginary quadratic field.

The necessity follows at once from the fact that the subfield, if it exists, contains at least one fundamental unit, and the sufficiency is a consequence of a generalized version of Theorem 7.1 relating to products of linear forms; $^{\ddagger}$  it is in fact a direct corollary in the case when the dimension of M is small compared with the degree of K. As examples, one sees that the equation

$$N(x_1 + x_2\sqrt{2} + x_3\sqrt{3}) = 1$$

has infinitely many solutions in integers  $x_1$ ,  $x_2$ ,  $x_3$  given by

$$x_1 + x_2\sqrt{2} = \pm (1 + \sqrt{2})^n$$
, and by  $x_1 + x_3\sqrt{3} = \pm (2 + \sqrt{3})^n$ ,

where n = 0, 1, 2, ...; and the equation

$$N(x_1+q^{1/p}x_2+\ldots+q^{(p-2)/p}x_{p-1})=m,$$

where p, q are primes and m is any integer, has only a finite number of solutions in integers  $x_1, ..., x_{p-1}$ ; for clearly the field generated by  $q^{1/p}$  over the rationals has only trivial subfields. It should be noted, however, that, in contrast to the work of Chapter 4, the arguments here are not effective and cannot lead to a determination of the totality of solutions. In fact, apart from a few special results of Skolem, the only effective theorems established to date on equations of norm form in three or more variables derive from the work on the hypergeometric function referred to in §5 of Chapter 4.

A generalization of Roth's theorem in the p-adic domain was obtained by Ridout¶ in 1957; in particular he proved that for any algebraic number  $\alpha$  and any  $\epsilon > 0$ , there exist only finitely many integers p, q, comprised solely of powers of fixed sets of primes, such that  $|\alpha - p/q| < q^{-\epsilon}$ . In this case, however, Theorem 3.1 gives rather more; in fact, on taking  $\alpha_1 = \alpha$  and the remaining  $\alpha$ 's as the given

<sup>†</sup> M.A. 191 (1971), 1-20.

<sup>‡</sup> For an account of this and associated topics one may refer to the excellent survey of Schmidt; Enseignement Math. 17 (1971), 187-253.

<sup>§</sup> Bibliography. || P.C.P.S. 63 (1967), 693-702.

Mathematika, 4 (1957), 125-31; 5 (1958), 40-8; see also Mahler (Bibliography).

primes, one sees at once that  $q^{-\epsilon}$  can be replaced by  $(\log q)^{-\epsilon}$  for some c depending only on  $\alpha$  and the primes, a result moreover that is fully effective. Further theorems in the context of p-adic approximations follow from the other inequalities for  $|\Lambda|$  recorded in Chapter 3.

#### 2. Wronskians

The Wronskian of polynomials  $\phi_1(x), \ldots, \phi_k(x)$  of one variable is defined as the determinant of order k with  $(j!)^{-1}\phi_i^{(j)}(x)$  in the ith row and (j+1)th column, where  $1 \leq i \leq k, \ 0 \leq j < k$ , and  $\phi^{(j)}$  denotes the jth derivative of  $\phi$ . Such Wronskians occurred in the original work of Thue, and they sufficed for the expositions of Siegel, Dyson and Gelfond; the arguments of Roth and Schmidt, however, involved the concept of a generalized Wronskian. Suppose that  $\phi_1, \ldots, \phi_k$  are polynomials in n variables  $x_1, \ldots, x_n$  and let  $\Delta^{(j)}$  denote a differential operator of the form

$$(j_1!\ldots j_n!)^{-1}(\partial/\partial x_1)^{j_1}\ldots(\partial/\partial x_n)^{j_n},$$

where  $j_1 + \ldots + j_n = j$ . Then any determinant of order k with some  $\Delta^{(j)}\phi_i$  in the ith row and (j+1)th column is called a generalized Wronskian of  $\phi_1, \ldots, \phi_k$ . There are clearly only finitely many generalized Wronskians of  $\phi_1, \ldots, \phi_k$ , and when n=1 the set reduces to the original Wronskian. We shall require later the result that if  $\phi_1, \ldots, \phi_k$  are linearly independent over their field of coefficients then some generalized Wronskian does not vanish identically; proofs are given, for instance, in the tracts of Cassels and Mahler.

## 3. The index

The proof of Theorem 7.1 involves polynomials P in kn variables  $x_{lm}$  ( $1 \le l \le k$ ,  $1 \le m \le n$ ), homogeneous in  $x_{1m}, \ldots, x_{km}$  for each m. Suppose that P has real coefficients and let  $L_m$  ( $1 \le m \le n$ ) be real linear forms in  $x_{1m}, \ldots, x_{km}$ . Then the index of P with respect to  $L_1, \ldots, L_n$  and positive integers  $r_1, \ldots, r_n$  is defined as the largest value of  $\theta$  such that P can be expressed as a linear combination of the polynomials  $L_1^{j_1} \ldots L_n^{j_n}$  with

$$(j_1/r_1) + \ldots + (j_n/r_n) \geq \theta,$$

and with real polynomials in the  $x_{lm}$  as coefficients. It is easily verified that, for any polynomials

P, Q as above, the index, for brevity, ind, with respect to the  $L_m$  and  $r_m$  satisfies ind  $(P+Q) \ge \min (\operatorname{ind} P, \operatorname{ind} Q)$ ,

$$\operatorname{ind} PQ = \operatorname{ind} P + \operatorname{ind} Q.$$

We shall require also the related concept of the index of a real polynomial  $P(x_1, ..., x_n)$  with respect to rationals  $p_m/q_m$   $(q_m > 0)$  and integers  $r_m > 0$   $(1 \le m \le n)$ ; this is defined as the index of the polynomial  $x_{01}^{d_1} ... x_{0n}^{d_n} P(x_{11}/x_{21}, ..., x_{1n}/x_{2n})$ 

in the 2n variables  $x_{lm}$  (l = 1, 2) with respect to the linear forms

$$L_m = q_m x_{1m} - p_m x_{2m}$$

and the  $r_m$ , where  $d_m$  denotes the degree of P in  $x_m$ . The index in the latter sense occurred first in the work of Roth, and the generalized concept was introduced by Schmidt.

In analogy with the notation of earlier chapters, we define the height ||P|| of a polynomial P as the maximum of the absolute values of its coefficients; we shall speak of the height only for polynomials with rational integer coefficients, not identically 0. The same definition will of course apply in the special case of linear forms.

Suppose now that P is a polynomial in kn variables as indicated at the beginning of the section. Let  $L_1, ..., L_n$  be linear forms as there, with relatively prime integer coefficients, and let  $q_m = ||L_m||$ . Further let  $r_1, ..., r_n$  be positive integers such that  $\delta r_m > r_{m+1}$   $(1 \le m < n)$ , where  $\delta = (\epsilon/32)^{2^n}$  and  $0 < \epsilon < 1$ . We have

**Lemma 1.** If  $q_m^{r_m} > q_1^{r_{r_1}} (1 \le m \le n)$  and  $q_1^{\delta n} > 8^{nk^2}$ , where  $0 < \eta \le k$ , and if also P has height at most  $q_1^{\delta n r_1/k^2}$  and degree at most  $r_m$  in  $x_{1m}, \ldots, x_{km}$ , then the index of P with respect to the  $L_m$  and  $r_m$  is at most  $\epsilon$ .

This is an extension, due to Schmidt, of the most fundamental part of Roth's work, sometimes called Roth's lemma. The result follows easily in fact from the case considered by Roth, as we now show.

We assume, as we may without loss of generality, that  $q_m = |a_{1m}|$ , where

$$L_m = \sum_{l=1}^k a_{lm} x_{lm} \quad (1 \leqslant m \leqslant n).$$

