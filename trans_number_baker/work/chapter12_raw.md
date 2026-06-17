
 $y'_{i} = \sum_{j=1}^{n} f_{ij}(x) y_{j} \quad (1 \leq i \leq n),$  (1)

where the  $f_{ij}$  are rational functions of x, and the coefficients of all the E's and f's are supposed to be elements of an algebraic number field K. We have then

**Theorem 11.1.** If  $E_1(x), ..., E_n(x)$  are algebraically independent over K(x) then, for any non-zero algebraic number  $\alpha$  distinct from the poles of the  $f_{ij}, E_1(\alpha), ..., E_n(\alpha)$  are algebraically independent.

The theorem can easily be extended to yield an assertion to the effect that the maximum number of algebraically independent elements among  $E_1(x), \ldots, E_n(x)$  is the same as that among

$$E_1(\alpha), \ldots, E_n(\alpha),$$

and moreover there is no difficulty in generalizing the latter result to inhomogeneous equations where an additional rational function is present on the right of (1). As an immediate application of Theorem 11.1, we see that if  $\lambda$  is rational, but not a negative integer or half an odd integer, then  $K_{\lambda}(\alpha)$  and  $K'_{\lambda}(\alpha)$  are algebraically independent for every non-zero algebraic number  $\alpha$ ; for it is well known! that  $K_{\lambda}(x)$  and  $K'_{\lambda}(x)$  are algebraically independent over Q(x). This further implies, for example, that the continued fraction with partial quotients 1, 2, 3, ... is transcendental; for  $J_0(\sqrt{(-4x)})$  [=  $K_0(\sqrt{(-4x)})$ ] satisfies the differential equation xy'' + y' = y, and the continued fraction in question is given by y/y' evaluated at x = 1. Oleinikov" has obtained some similar theorems for third order linear differential equations; for instance he has shown that if

$$F(x) = \sum_{n=0}^{\infty} \frac{(x/3)^{8n}}{n! [\lambda, n] [\mu, n]},$$

<sup>†</sup> I.A.N. 23 (1959), 35-66.

<sup>‡</sup> Cf. the survey of Feldman and Shidlovsky (Bibliography).

f Cf. Siegel (Bibliography).

<sup>||</sup> D.A.N. 166 (1966), 540-3.

where  $\lambda$ ,  $\mu$  are rationals such that none of  $\lambda + \mu$ ,  $\lambda - 2\mu$ ,  $\mu - 2\lambda$  are integers, then F(x), F'(x), F''(x) satisfy the hypothesis of Theorem 11.1, whence  $F(\alpha)$ ,  $F'(\alpha)$ ,  $F''(\alpha)$  are algebraically independent for every non-zero algebraic number  $\alpha$ . And Shidlovsky<sup>†</sup> has proved a striking theorem to the effect that if

$$\Phi_k(x) = \sum_{n=0}^{\infty} x^{kn}/(n!)^k,$$

then, for any non-zero algebraic  $\alpha$  and any r, the numbers  $\Phi_k^{(l)}(\alpha/k)$ , with  $1 \leq l < k$ ,  $1 \leq k \leq r$ , are algebraically independent. Plainly also Theorem 11.1 includes Lindemann's theorem.

## 2. Basic construction

The proof of Theorem 11.1 follows closely the arguments of the preceding chapter, but it is no longer a simple matter to confirm that  $\Delta(x)$  does not vanish identically. The verification, which is Shidlovsky's major discovery in the subject, will be given in Lemma 2 below.

We shall signify by  $E_1(x), ..., E_n(x)$  E-functions as above, linearly independent over K(x) and we shall suppose that  $0 < \epsilon < 1$ . Constants implied by  $\leqslant$  or  $\gg$  will depend on the coefficients in the E's, f's and on  $\epsilon$  only. By f(x) we signify a polynomial, not identically 0, with coefficients in K, such that  $f_{ij}$  is a polynomial for all  $f_{ij}$  in (1).

**Lemma 1.** For any integer  $r \gg 1$ , there are polynomials

$$P_i(x) \quad (1 \leqslant i \leqslant n),$$

not all identically 0, with degrees at most r and algebraic integer coefficients in K with sizes at most  $(r!)^{1+\epsilon}$ , such that

$$\sum_{i=1}^{n} P_i(x) E_i(x) = \sum_{m=M}^{\infty} \rho_m x^m, \qquad (2)$$

where  $|\rho_m| < r! (m!)^{-1+\epsilon}$  and

$$M = n(r+1) - 1 - [\epsilon r].$$

**Proof.** Let  $a_{ij}$  be the coefficient of  $x^j/j!$  in  $E_i(x)$  and let  $b_{i0}, b_{i1}, \ldots$  be the sequence of integers associated with  $E_i$  as in § 1. By Lemma 1 of Chapter 6, there exist algebraic integers  $p_{ij}$   $(1 \le i \le n, 0 \le j \le r)$  in K,

<sup>†</sup> Trudy Moskov. 18 (1968), 55-64.

not all 0, such that

$$\sum_{i=1}^{n} \sum_{j=0}^{\min(r, m)} {m \choose j} a_{i, m-j} p_{ij} = 0 \quad (0 \le m < M),$$
 (3)

and indeed they can be selected to have sizes at most  $N^{\delta NM/(N-M)}$ , where N=n(r+1) and  $\delta=(\epsilon/4n)^2$ ; for, on multiplying (3) by  $b_{1m}\dots b_{nm}$ , the coefficients become algebraic integers in K with sizes  $\leq 2^M M^{\frac{1}{2}\delta M}$ , as is clear on taking  $\delta/(2n)$  in place of  $\epsilon$  in the defining property of the b's. We conclude, as in the proof of Lemma 1 of Chapter 10, that the polynomials

$$P_i(x) = r! \sum_{j=0}^{r} p_{ij}(j!)^{-1} x^j \quad (1 \le i \le n)$$

have the asserted properties. In fact (2) plainly holds with

$$\rho_m = (r!/m!)\,\sigma_m,$$

where  $\sigma_m$  denotes the left-hand side of (3), and since M < N < 2nr and  $N - M > \epsilon r$ , we see that the  $p_{ij}$  have sizes at most  $r^{\frac{1}{2}\epsilon r}$ , whence  $|\sigma_m| < (m!)^{\epsilon}$  for  $m \ge M$ , as required.

**Lemma 2.** Let  $P_{ij}(x)$   $(1 \le i \le n, j \ge 1)$  be defined recursively by

$$P_{i1} = P_i$$
,  $P_{i,j+1} = f P'_{ij} + f \sum_{h=1}^{n} f_{hi} P_{hj}$ .

Then the determinant  $\Delta(x)$  of order n with  $P_{ij}(x)$  in the ith row and jth column is not identically 0.

**Proof.** Suppose, on the contrary, that  $\Delta(x)$  vanishes identically. Let k be the integer such that the first k columns of  $\Delta(x)$  are linearly independent over K(x) but the (k+1)th column is linearly dependent on these. We signify by  $\mathbf{Q}$  the matrix formed by the first k columns of  $\Delta(x)$ , and by  $\mathbf{R}$  and  $\mathbf{S}$  the matrices formed from the first k rows of  $\mathbf{Q}$  and last n-k rows respectively. We assume, as clearly we may, that the notation is such that  $\mathbf{R}$  is non-singular, and we proceed to prove that the degrees of the numerators and denominators of the rational function elements of  $\mathbf{S}\mathbf{R}^{-1}$  are  $\ll 1$ , where in fact the implied constant depends only on the f's. This will suffice to establish the lemma; for denoting by  $\mathbf{L}$  the row vector with jth element

$$L_{j} = \sum_{i=1}^{n} P_{ij} E_{i} \quad (1 \leq j \leq k),$$

and putting  $\mathbf{A} = (E_1, ..., E_k)$ ,  $\mathbf{B} = (E_{k+1}, ..., E_n)$ ,

we have L = AR + BS whence

$$LR^{-1} = A + BSR^{-1}. (4)$$

But  $L_j$  satisfies the differential equation  $L_{j+1} = fL'_j$  and so each element of L has a zero at x=0 with order at least M-n. Further, each element of  $\mathbf{R}^{-1}$  can be expressed as a rational function in K(x) with denominator det  $\mathbf{R}$ , and since the latter is a polynomial with degree at most kr+c, where  $c \leqslant 1$ , it follows that each element of  $\mathbf{L}\mathbf{R}^{-1}$  has a zero at x=0 with order at least M-kr-n-c. On the other hand, the vector on the right of (4) cannot vanish identically in view of the assumed linear independence of  $E_1, \ldots, E_n$ , and the order of the zeros of its elements at x=0, if any, are bounded independently of the coefficients of the elements of  $\mathbf{S}\mathbf{R}^{-1}$ , and so, in particular, of r. Now k < n, and so M-kr tends to infinity with r; hence we have a contradiction if r is sufficiently large.

To prove the assertion concerning SR<sup>-1</sup>, we observe first that there is a square matrix F of order k, with elements in K(x), such that, for any solution y of (1), the vector Y = yQ satisfies the differential equation Y' = YF. Indeed if  $Y_j$  denotes the jth element of Y, then  $Y_{j+1} = fY'_j$  for all j < k and, by the definition of  $k, fY'_k$  is expressible as a linear combination of  $Y_1, \ldots, Y_k$  with coefficients in K(x). Let now  $\mathbf{w}_1, \dots, \mathbf{w}_n$  be power series solutions of (1) linearly independent over Kand let W be the square matrix of order n with jth row  $w_i$ . Then each row of WQ is a solution of Y' = YF; but this has at most k solutions linearly independent over K and thus there exists an n-k by n matrix **M** with coefficients in K and rank n-k satisfying MWQ = 0. Denoting by U and V the matrices formed from the first k columns of MW and the last n-k columns respectively, we have UR + VS = 0. Since R is non-singular and MW has rank n-k it follows that V is non-singular and so  $SR^{-1} = -V^{-1}U$ . Clearly the elements of  $V^{-1}U$  are rational functions in the elements of W with coefficients in K and with the degrees of the numerators and denominators bounded independently of r. Hence they can be expressed as quotients of linear forms in certain monomials in the elements of W, linearly independent over K(x), the coefficients in the linear forms being rational functions in K(x) for which again the degrees of the numerators and denominators are bounded independently of r. Since the elements of  $SR^{-1}$  and so also of  $V^{-1}U$  are in fact in K(x), they must be given by quotients of such coefficients, and the assertion follows.

#### 3. Further lemmas

We now obtain analogues of Lemmas 3 and 4 of Chapter 10. The arguments here will follow closely their earlier counterparts and so we shall be relatively brief.

By  $\alpha$  we shall signify an element of K with  $\alpha f(\alpha) \neq 0$ . By  $c_1, c_2, \ldots$  we denote positive numbers which may depend on  $\alpha, \epsilon$  and the coefficients in the E's and f's only.

**Lemma 3.** There are distinct suffixes J(j)  $(1 \le j \le n)$  not exceeding  $\epsilon r + c_1$  such that the determinant with  $P_{\epsilon, J(j)}(x)$  in the ith row and jth column does not vanish at  $x = \alpha$ .

**Proof.** We begin by noting that  $\Delta(x)$  remains unaltered if the first row is replaced by  $E_1^{-1}L_j$  with j=1,2,...,n, where  $L_j$  is defined as in the proof of Lemma 2. Hence  $\Delta(x)$  has a zero at x=0 with order at least  $M-c_2$ , and since it is a polynomial with degree at most  $nr+c_3$ , it follows that a non-negative integer t exists, not exceeding

$$nr + c_3 - (M - c_2) \leqslant \epsilon r + c_4$$

such that  $\Delta^{(t)}(\alpha) \neq 0$ ; we suppose that t is chosen minimally.

We now introduce linear forms in  $w_1, ..., w_n$  by (3) of Chapter 10. On applying the operator fd/dx to (4) of that chapter t times, replacing  $w'_i$  occurring at each stage by the right-hand side of (1) with  $y_j = w_j$ , we obtain

$$w_i(f(\alpha))^t \Delta^{(t)}(\alpha) = \sum_{j=1}^{n+t} W_j F_{ij}(\alpha) \quad (1 \leq i \leq n),$$

where the  $F_{ij}$  denote polynomials in x given by linear combinations of the f's,  $\Delta$ 's and their derivatives. Hence the linear forms

$$W_i \quad (1 \leqslant j \leqslant n+t)$$

with  $x = \alpha$  include a set of n linearly independent forms and the lemma follows with J(j) given by the associated suffixes.

**Lemma 4.** There are algebraic integers  $q_{ij}$   $(1 \le i, j \le n)$  in K with sizes at most  $(r!)^{1+18\epsilon}$  forming a non-zero determinant and satisfying

$$\left|\sum_{i=1}^{n} q_{ij} E_i(\alpha)\right| < (r!)^{-n+1+16\epsilon n} \quad (1 \leq j \leq n). \tag{5}$$

**Proof.** Let l be a positive integer such that  $l\alpha$  and the coefficients in

If and all  $lff_{ij}$  are algebraic integers. We proceed to prove that the numbers  $q_{ij} = l^{r+(m+1)J(j)}P_{i,J(j)}(\alpha) \quad (1 \leq i, j \leq n),$ 

where m denotes the maximum of the degrees of the  $ff_{ij}$  and f, have the required properties. First it is clear that  $l^jP_{ij}$  has algebraic integer coefficients and degree at most r+mj. Thus the q's are algebraic integers and, by Lemma 3, they form a non-zero determinant. Further, it is easily verified by induction that the sizes of the coefficients of  $l^jP_{ij}$  are at most  $(r+mj)^{2j}c_b^i(r!)^{1+\epsilon}$ , and since the J(j) do not exceed  $\epsilon r+c_1$ , this gives the required estimate for the sizes of the q's.

It remains to prove (5). Denoting by  $\Phi(x)$  the left-hand side of (2), it is clear that the sum on the left of (5) is given, apart from a factor  $l^{r+(m+1)J}$ , by  $(fd/dx)^{J-1}\Phi$  evaluated at  $x=\alpha$ , where J=J(j). But, again by induction, we see that this is a linear form in the  $\Phi^{(h)}(\alpha)$ , where h=0,1,...,J-1, having coefficients with absolute values at most  $(c_6J)^{2J}$ . Hence it suffices to prove that

$$|\Phi^{(h)}(\alpha)| < (r!)^{-n+1+8\epsilon n} \quad (0 \le h < J).$$

Now from Lemma 1 we obtain

$$|\Phi^{(h)}(\alpha)| < r! \sum_{m=-M}^{\infty} (m!)^{\epsilon} ((m-h)!)^{-1} |\alpha|^{m-h},$$

and the sum on the right is at most

$$h! \sum_{m=-M}^{\infty} (m!)^{-1+\epsilon} 2^m |\alpha|^{m-h} \leqslant h! c_7^M (M!)^{-1+\epsilon}.$$

Since  $h < \epsilon r + c_1$  and  $M \leq 2nr$  we have  $h! \leq (r!)^{3\epsilon}$  and

$$M! \geqslant (2nr)^{-\epsilon r} (r!)^n \geqslant (r!)^{n-3\epsilon}$$
.

The required estimate follows at once.

## 4. Proof of main theorem

Suppose that  $E_1(\alpha), \ldots, E_n(\alpha)$  are algebraically dependent. Then they satisfy an equation  $P(E_1, \ldots, E_n) = 0$ , where P is a polynomial with algebraic coefficients, not all 0. We shall denote by c the degree of P, and we shall assume, as we may without loss of generality, that the coefficients in P are algebraic integers in K. The degree of K will be denoted by d, and we shall suppose that  $0 < \varepsilon < 1$ . Further we shall signify by m an integer such that the binomial coefficients

$$k = \binom{m+n+c}{n}, \quad l = \binom{m+n}{n}$$

satisfy *k — l< l/(2d);* the latter inequality certainly holds for all sufficiently large TO since *k* and *I* are asymptotic to *m n jn\* as *m -\*•* oo, as is easily seen by expressing them as polynomials in *m* with degree *n.* In the sequel, constants implied by < or > will depend on *a, e, m* and the coefficients in the *E'a,* /'s and *P* only.

Let now *Sx,*..., *Sk* be the ^-functions *E{\*... Eft,* where*<sup>j</sup> <sup>x</sup> j <sup>n</sup>* run through all non-negative integers with *j <sup>x</sup> +... +jn* < TO + c. Then clearly *Sx, ...,&k* satisfy a further system of linear differential equations of the form (1), where the new coefficients are given by linear combinations of the/'s; furthermore, *&x,...,Sk* are linearly independent over *K(x)* by virtue of the hypothesis regarding the algebraic independence of *Ex(x), ..., En{x).* We conclude from § 2 and § 3 that, for any integer r > 1, there exist algebraic integers *qtj* (1 < *i,j* < *k)* in *K* possessing the properties cited in Lemma 4 with *&x Sk* in place of *Ex,...,En.* For each set of non-negative integers *ji,...,jn* with *jx+... +jn* < *m* we write

$$E_1^{j_1} \dots E_n^{j_n} P(E_1, \dots, E_n) = \sum_{i=1}^k p_{ij} \mathscr{E}_i$$

where the *p^* are either coefficients in *P* or 0, *a,ndj* = *j(jv ... ,jn)* takes the values 1,2, *...,l.* Then on the right we have *I* linear forms in (?! *&k* linearly independent over *K,* all of which vanish at *x* = a. Since the determinant of the gy is not 0, it follows that there exist *k* - *1* of the forms *k*

which together with the latter make up a linearly independent set; without loss of generality we can suppose that they are given by <1>,+1,..., *<J>k.* We shall suppose also, as clearly we may, that *Sx(a)* + 0.

We now compare estimates for the determinant *D* of order *k* with *<sup>p</sup>{i* in the tth row and *jth* column for j ^ *I* and *qi}* in that position for *j > I.* Plainly *D* is a non-zero algebraic integer in *K,* and, since *pif* < 1, it has size «^ (r!)a+i««)«-«); hence

$$|D| \gg (r!)^{-(1+16\epsilon)(k-l)d} \geqslant (r!)^{-(1+16\epsilon)l/2}$$

On the other hand, *D* is unaltered if the first row is replaced by 0 for j" < Z and by *S^<sup>x</sup> (a.)* Oy for j > *I.* Further, by Lemma 4, the latter elements are -^ (r!)-\*+i+"\*\*; thus

$$|D| \ll (r!)^{(1+16\epsilon)(k-l-1)-k+1+16\epsilon k} \leqslant (r!)^{-l+32\epsilon k}$$

But *k <* f *I* and so, if e < *jfa* and *r* is sufficiently large, we have a contradiction. This proves the theorem.

Subsequent to the fundamental discovery of Shidlovsky, researches in this field have largely centred on establishing the function—theoretic hypotheses of Theorem 11.1 and its extensions for particular classes of E-functions, and, as indicated in § 1, this has in fact been accomplished in many striking cases. Studies have also been carried out in connexion with obtaining positive lower bounds for expressions of the type  $P(E_1, ..., E_n)$  as above, and in fact an estimate of the form  $Ch^{-c}$  has been established, where h denotes the maximum of the sizes of the coefficients of P and C, c are positive numbers which do not depend on h; but c here increases rapidly with n. The main outstanding problem in the subject is to generalize the theory to wider classes of analytic functions than E-functions, and any progress here would be of much interest.

† Cf. Lang (Bibliography, first work).

## ALGEBRAIC INDEPENDENCE

## 1. Introduction

Few theorems have been established to date on algebraic, as opposed to linear, independence of transcendental numbers. Indeed, apart from the results on *E*-functions discussed in the last chapter, which in fact follow at once from their linear analogues, and the examples mentioned in Chapter 8 that arise from the properties of Mahler's classification, the only work in this context of a general nature is based on studies of Gelfond† carried out in 1949. Recently a number of authors have obtained important improvements in this connexion, and these latest developments will be the theme of the present chapter.

The essential character of the results is well-illustrated by:

**Theorem 12.1.** If both  $\xi_1$ ,  $\xi_2$ ,  $\xi_3$  and  $\eta_1$ ,  $\eta_2$ ,  $\eta_3$  are linearly independent over the rationals, then two at least of the numbers

$$\xi_i$$
,  $e^{\xi_i \eta_j}$   $(1 \leq i, j \leq 3)$ 

are algebraically independent.

Gelfond proved the theorem originally subject to certain supplementary conditions, and the formulation here is due to Tijdeman.<sup>‡</sup> As an immediate consequence one sees that if  $\alpha$  is an algebraic number other than 0 or 1 and  $\beta$  is a cubic irrational then  $\alpha^{\beta}$ ,  $\alpha^{\beta^2}$  are algebraically independent; this follows in fact on taking  $\xi_j = \beta^{j-1}$  and  $\eta_j = \xi_j \log \alpha$ . Tijdeman also derived two variants of Theorem 12.1; he proved that if  $\xi_1$ ,  $\xi_2$ ,  $\xi_3$ ,  $\xi_4$  and  $\eta_1$ ,  $\eta_2$  are linearly independent over the rationals, then two at least of  $\xi_i$ ,  $e^{\xi_i \eta_j}$  are algebraically independent over the rationals, then two at least of  $\xi_i$ ,  $\eta_j$ ,  $e^{\xi_i \eta_j}$  are algebraically independent. These results include some earlier theorems of Šmelev.§

Very recently, Brownawell and Waldschmidt succeeded independently in obtaining a new version of the latter result which sufficed to solve a well-known problem of Schneider. They proved:

<sup>†</sup> Bibliography

**Theorem 12.2.** If both  $\xi_1$ ,  $\xi_2$  and  $\eta_1$ ,  $\eta_2$  are linearly independent over the rationals and if  $e^{\xi_1\eta_2}$  and  $e^{\xi_2\eta_2}$  are algebraic, then two at least of  $\xi_4$ ,  $\eta_4$ ,  $e^{\xi_1\eta_2}$  are algebraically independent.

This implies, more especially, that if  $\xi_1$ ,  $\xi_2$  and  $\eta_1$ ,  $\eta_2$  are linearly independent over the rationals then at least two different numbers amongst  $\xi_i$ ,  $\eta_j$ ,  $e^{\xi_i\eta_j}$  are transcendental. It follows at once, on taking  $\xi_1 = \eta_1 = 1$ ,  $\xi_2 = \eta_2 = e$ , that one at least of  $e^e$  and  $e^{e^z}$  is transcendental. Furthermore, from Theorem 12.2, one sees, for instance, that at least one of  $\alpha^{\log \alpha}$  and  $\alpha^{(\log \alpha)^z}$  is transcendental for any algebraic number  $\alpha$  other than 0 or 1. These results represent the nearest approach we have to date towards a confirmation of the transcendence of numbers of the type  $\log \pi$  and  $e^{\pi^z}$ .

In another direction, Lang<sup>†</sup> has proved:

**Theorem 12.3.** If  $\xi_1$ ,  $\xi_2$ ,  $\xi_3$  and  $\eta_1$ ,  $\eta_2$  are linearly independent over the rationals then one at least of the numbers  $e^{\xi_1\eta_2}$  is transcendental.

Surprisingly, the demonstration of Theorem 12.3 is much simpler than that of Theorems 12.1 and 12.2, and yet the result admits several notable corollaries. In particular, it follows that, for any algebraic number  $\alpha$ , not 0 or 1, and any transcendental  $\beta$ , one at least of  $\alpha^{\beta}$ ,  $\alpha^{\beta^{3}}$  is transcendental; and in fact this result holds for any irrational  $\beta$  in view of the Gelfond-Schneider theorem. As a further example, the theorem plainly shows that for any real irrational  $\beta$ , the function  $x^{\beta}$  cannot assume algebraic values at more than two consecutive integral values of x > 2. More general results of this nature, involving, for instance, the Weierstrass  $\varphi$ -function, were obtained by Ramachandra, who apparently discovered Theorem 12.3 independently. The theorem also throws some light on the problem raised by Schneider as to the untenability of the equation

$$\log \alpha \log \beta = \log \gamma \log \delta$$

in algebraic numbers  $\alpha$ ,  $\beta$ ,  $\gamma$ ,  $\delta$ , having logarithms linearly independent over the rationals; it shows in fact that, given  $\alpha$ ,  $\gamma$ , there cannot be two solutions  $\beta$ ,  $\delta$  such that all six logarithms are linearly independent. The problem is, of course, only a special case of the wider open question as to a verification of the algebraic independence of the logarithms of algebraic numbers.

We remark finally that most of our expectations in connexion with

the transcendence properties of the exponential and logarithmic functions are covered by a general conjecture, attributed to Schanuel, to the effect that if *E,x,...*, £n are linearly independent over the rationals, then the transcendence degree of the field generated by £x £n, e\*i,...,e&> over the rationals is at least *n.* The conjecture includes Theorems 1.4 and 2.1, and moreover it implies the algebraic independence of e and *it.* The power series analogue has been proved by Ax. \*

## **2. Exponential polynomials**

Our object here is to establish a theorem of Tijdeman' on the zeros of functions of the form

$$F(z) = \sum_{k=0}^{K-1} \sum_{l=1}^{L} f(k,l) z^{k} e^{\sigma_{l} z}.$$

We shall assume that *o~x, ...,CL* are complex numbers with absolute values at most *S,* and that the/'s are arbitrary complex numbers for which *F* does not vanish identically. Constants implied by <^ will be absolute. We prove:

**Lemma 1.** *The number of zeros of F in any closed disc, with radius R, counted urith multiplicities, is* <^ *KL + RS.*

Tijdeman actually obtained the estimate *3KL + 4RS,* but the constants are not important for our purpose here. The main interest of the result lies in the fact that, in contrast to all previous theorems of its kind, there is no dependence on the differences between the <r's, and it is this strengthening that leads to the improvements in Gelfond's results mentioned earlier.

To commence the proof, let *C* be the circle centre the origin\* with radius *R,* and let *M(R)* be the maximum of |.F| on *C.* Further, let

$$W(z) = (z - \omega_1) \dots (z - \omega_h),$$

where w1,..., *OJH* run through the zeros of *F,* taken with multiplicities, within and on *C.* Then *FjW* is regular within and on any concentric circle with larger radius, and so, by the maximum-modulus principle,

$$|W(v)|M(R) \leq |W(u)|M(4R),$$

where *u, v* are some numbers with |«| = *R* and *\v\* = *4R.* Now clearly

$$|W(u)| \leq (2R)^h, \quad |W(v)| \geq (3R)^h,$$

<sup>t</sup> *Ann. Math.* 93 (1971), 252-68. *t I.M.* 33 (1971), 1-7. § Plainly, this choice involves no loss of generality.

and thus

$$h \leqslant \log (M(4R)/M(R)).$$

It remains therefore to show that the number on the right is

$$\ll KL + RS$$
.

Let the sequence  $\sigma_1, ..., \sigma_1, ..., \sigma_L$ , of N = KL numbers, where each  $\sigma$  is repeated K times, be written as  $\eta_1, ..., \eta_N$ . By Newton's interpolation formula we have, for any w, z,

$$e^{zw} = \sum_{n=0}^{N} a_n P_n(w),$$

where

$$P_n(w) = (w - \eta_1) \dots (w - \eta_n) \quad (1 \le n \le N),$$

and

$$a_n = \frac{1}{2\pi i} \! \int_{\Gamma} \frac{e^{z\zeta}}{P_{n+1}(\zeta)} \left(\! \frac{\zeta - \eta_{n+1}}{\zeta - w} \! \right)^{\delta_n} \! d\zeta, \label{eq:anomaly}$$

 $\Gamma$  denoting a circle with centre the origin, described in the positive sense, including the  $\eta$ 's and w, and  $\delta_n = 0$  if n < N,  $\delta_N = 1$ . Clearly  $a_n$  is independent of w for n < N and  $a_N$  is an integral function of w. We put

$$P(w) = \sum_{n=0}^{N-1} a_n P_n(w) = \sum_{n=0}^{N-1} p_n w^n,$$

and then it is readily verified that

$$F(z) = \sum_{k=0}^{K-1} \sum_{l=1}^{L} f(k,l) P^{(k)}(\sigma_l) = \sum_{n=0}^{N-1} p_n F^{(n)}(0).$$

We proceed now to employ the latter formula to obtain an upper bound for |F|.

By Cauchy's theorem we have

$$F^{(n)}(0) = \frac{n!}{2\pi i} \int_C \frac{F(\zeta) d\zeta}{\zeta^{n+1}},$$

and thus

$$\left|F^{(n)}(0)\right| \leqslant n! \, M(R)/R^n.$$

This gives

$$|F(z)| \leqslant M(R) \sum_{n=0}^{N-1} n! |p_n|/R^n.$$

To estimate the latter sum, let

$$b_n = \frac{1}{2\pi i} \int_{\Gamma} \frac{e^{|z|\zeta}}{Q_{n+1}(\zeta)} d\zeta,$$

where  $Q_n(w) = (w-S)^n$  and  $\Gamma$  denotes a circle as above including S. On comparing the coefficients in  $(P_n(\zeta))^{-1}$  and  $(Q_n(\zeta))^{-1}$  when these are

expressed as series in decreasing powers of  $\zeta$ , we obtain  $|a_n| \leq b_n$  for all n < N. But plainly  $b_n = e^{|z|S} |z|^n/n!$ 

and so, in view of the formula

$$n! p_n = \sum_{r=n}^{N-1} a_r P_r^{(n)}(0),$$

we have

$$n! \, \big| \, p_n \big| \, \leqslant \, n! \, \sum_{r \, = \, n}^{N \, - \, 1} \binom{r}{n} \, S^{r - n} \, b_r \, = \, e^{|\mathbf{z}| S} \sum_{r \, = \, n}^{N \, - \, 1} \big| z \big|^r \, S^{r - n} / (r - n)! \, \leqslant \, \big| z \big|^n \, \, e^{2|z|S},$$

whence

$$|F(z)| \leq M(R) e^{2|z|S} \sum_{n=0}^{N-1} (|z|/R)^n.$$

On taking |z| = 4R, we conclude that

$$M(4R) \leqslant M(R) e^{8RS} 4^N,$$

and the lemma follows at once.

## 3. Heights

We shall require a more explicit version of Lemma 2 of Chapter 8. The result is due to Gelfond, who in fact obtained the proposition in a generalized form relating to polynomials in several variables.

**Lemma 2.** If P(x) is a polynomial with degree n and height h, and if  $P = P_1 P_2 \dots P_k$ , where  $P_i(x)$  is a polynomial with height  $h_i$ , then

$$h \geqslant e^{-n}h_1h_2\dots h_k.$$

We assume without loss of generality that  $P(0) \neq 0$ . For any zero  $\rho$  of P and any complex number z with |z| = 1, let w be the projection of  $\rho$  on the line through z and  $-\rho/|\rho|$ , taking w = z if  $z = \pm \rho/|\rho|$ . Then, by simple geometry,

$$|z-\rho| \ge |w-\rho| = \frac{1}{2}(1+|\rho|)|z-\rho/|\rho||.$$

Thus, if  $\rho_1, ..., \rho_n$  are all the zeros of P, then

$$|P(z)| \geqslant 2^{-n}M_1 \dots M_k R(z),$$

where  $M_i$  denotes the maximum of  $P_i$  on the unit circle and

$$R(z) = \prod_{j=1}^{n} |z - \rho_j/|\rho_j|.$$

Now for any polynomial

$$Q(x) = q_0 + q_1 x + \ldots + q_m x^m$$

we have

$$\int_0^1 |Q(e^{2\pi i\phi})|^2 d\phi = \sum_{j=0}^m |q_j|^2.$$

Hence taking Q = R and noting that R has leading coefficient 1 and constant coefficient with absolute value 1, we obtain

$$\int_0^1 |P(e^{2\pi i\phi})|^2 d\phi \geqslant 2^{1-2n} (M_1 \dots M_k)^2.$$

But, on taking Q = P, we see that the number on the left is at most  $2nh^2$ , and clearly also

$$M_j^2\geqslant \int_0^1 |P_j(e^{2\pi i\phi})|^2 d\phi\geqslant h_j^2.$$

Since  $e^n \ge n^{\frac{1}{2}}2^n$ , this proves the lemma.

We shall require also a lemma closely related to the inequality  $|\alpha - \beta| \gg a^{-l}b^{-m}$  mentioned in § 6 of Chapter 8. Again we shall adopt the convention that when one refers to the height of a polynomial it is implied that the coefficients are rational integers, not all 0.

**Lemma 3.** If  $P_1(x)$ ,  $P_2(x)$  are polynomials with degrees  $n_1$ ,  $n_2$  and heights  $h_1$ ,  $h_2$  respectively and if  $P_1$ ,  $P_2$  have no common factor then, for any complex number z,

$$\max(|P_1(z)|, |P_2(z)|) \ge (n_1 + n_2)^{-\frac{1}{2}(n_1 + n_2 + 1)} h_1^{-n_2} h_2^{-n_1}.$$

The proof depends on the observation that since  $P_1$ ,  $P_2$  have no common factor, their resultant R is not 0. Now R can be expressed as the familiar Sylvester determinant of order  $n_1 + n_2$  formed by eliminating x from the equations

$$x^i P_1(x) = 0 \quad (0 \leqslant i < n_2), \qquad x^j P_2(x) = 0 \quad (0 \leqslant j < n_1).$$

Thus R is a rational integer and so  $|R| \ge 1$ . On the other hand, R is unaltered if one replaces the element in the first column and ith row by  $z^{i-1}P_1(z)$  for  $i \le n_2$  and by  $z^{i-n_2-1}P_2(z)$  for  $i > n_2$ . Hence, if  $|z| \le 1$ , the lemma follows from the upper estimates for the cofactors of these elements furnished by Hadamard's inequality. If |z| > 1 one argues similarly, replacing now the elements in the last column by numbers as above multiplied by  $z^{-n_1-n_2+1}$ .

## 4. Algebraic criterion

We now establish a lemma giving a sufficient condition for a number to be algebraic; it was derived in its original form by Gelfond and later sharpened by Brownawell and Waldschmidt. It shows that, in a sense, a number cannot be too well approximated by algebraic numbers unless it is itself algebraic and all the terms in the sequence beyond a certain point are equal. We shall actually prove the proposition in a form relating to polynomial sequences since this is more useful for applications.

First we need a preliminary lemma. Let P(x) be a polynomial with degree n and height h, and let z be any complex number.

**Lemma 4.** If  $|P(z)| \le 1$  then P has a factor Q, a power of an irreducible polynomial with integer coefficients, such that

$$|Q(z)| \leq |P(z)| \exp(8n(n + \log h)).$$

We write P as a product  $P_1 
ldots P_k$  of powers of distinct irreducible polynomials and, for brevity, we put  $p_j = |P_j(z)|$ . Then, by hypothesis,  $p_1 
ldots p_k 
ldots 1$  and so there exists a suffix l, possibly 1 or k, such that

$$p_1 \ldots p_{l-1} \geqslant p_l \ldots p_k, \quad p_1 \ldots p_l \leqslant p_{l+1} \ldots p_k.$$

Now  $P_1 \dots P_{l-1}$  and  $P_l \dots P_k$  have degrees at most n, no common factor and, in view of Lemma 2, heights at most  $e^nh$ . Hence from Lemma 3 and the first inequality above we see that

$$p_1 \dots p_{l-1} \geqslant \exp(-4n(n + \log h)).$$

Similarly, by virtue of the second inequality above, this estimate obtains also for  $p_{l+1} \dots p_k$ . Thus we have

$$p_l \leq p_1 \dots p_k \exp{(8n(n + \log h))},$$

and the assertion follows with  $Q = P_l$ .

**Lemma 5.** If  $\omega$  is a transcendental number and if  $P_j(x)$  (j = 1, 2, ...) is a sequence of polynomials with degrees and heights at most  $n_j$  and  $h_j$  respectively such that

$$n_i < n_{i+1} \ll n_i$$
,  $\log h_i \leqslant \log h_{i+1} \ll \log h_i$ ,

then, for some infinite sequence of values of j,

$$\log |P_i(\omega)| \gg -n_i(n_i + \log h_i).$$

Here the implied constants are again absolute. For the proof we assume that the latter inequality does not hold for j sufficiently large, and we derive a contradiction if the implied constant is large enough. By Lemma 4, *P<sup>i</sup>* has a factor *Qjt* a power of an irreducible polynomial, such that

and, by Lemma 2, *Q}* has height at most e"\* fy. It follows from Lemma 3 that, for all sufficiently large*<sup>j</sup> , Q<sup>i</sup>* is a power of some irreducible polynomial *Q,* say, independent of*<sup>j</sup> ;* for if *Q<sup>t</sup>* and *Qi+l* have no common factor then

$$\max(|Q_j(\omega)|, |Q_{j+1}(\omega)|) > e^{-4n_j^2+1}h_j^{-n_{j+1}}h_{j+1}^{-n_{j}}$$

and, in view of the hypotheses concerning *ni+1* and *hj+1,* this plainly contradicts either the previous inequality or its analogue with *j* replaced by *j* + 1. Since obviously *Qj* is at most the n^th power of *Q,* we Obtai n

and since also *n^* -> oo as *j -\*•* oo, it follows that *Q{o>)* = 0. But this contradicts the hypothesis that *w* is transcendental.

