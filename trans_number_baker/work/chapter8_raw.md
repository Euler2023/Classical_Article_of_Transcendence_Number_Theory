We shall further assume that  $(a_{1m}, a_{2m})^{\dagger}$  is at most  $q_m^{(k-2)/(k-1)}$ ; this also involves no loss of generality, since a prime p can divide at most

 $\dagger$  (a, b) denotes the greatest common divisor of a, b.

k-2 of the integers  $(a_{1m}, a_{lm})$  with  $1 < l \le k$ , whence their product divides  $q_m^{k-2}$ . Let now P' be the polynomial obtained from P by successively removing, in some order, the highest power of

$$x_{lm} \quad (3 \leqslant l \leqslant k, 1 \leqslant m \leqslant n)$$

that divides P and then setting the variable to 0; further let P'' be the polynomial obtained by setting  $x_{2m} = 1$  in P' for each m. Then clearly the index of P with respect to the  $L_m$  and  $r_m$  is at most the index of P'' with respect to  $-a_{2m}/a_{1m}$  and  $r_m$ . Also, by assumption, the denominator of  $a_{2m}/a_{1m}$ , when expressed in lowest terms, namely  $q_m/(a_{1m}, a_{2m})$ , is at least  $q_m^{1/k}$ . Hence we see that it suffices to prove the following modified version of Lemma 1.

For any integers  $r_m$   $(1 \leq m \leq n)$  as above and any rationals

$$p_m/q_m \quad (q_m > 0)$$

in their lowest terms such that  $q_m^{rm} > q_1^{qr_1}$  and  $q_1^{g_n} > 8^n$ , where  $0 < \eta \leqslant 1$ , the index with respect to the  $p_m/q_m$  and  $r_m$  of any polynomial  $P(x_1,\ldots,x_n)$  with height at most  $q_1^{g_{qr_1}}$  and degree at most  $r_m$  in  $x_m$  is at most  $\epsilon$ .

Proofs of this proposition, possibly in slightly adapted form, in particular with  $\eta=1$ , are given in several of the texts cited in the Bibliography, and our exposition can therefore be relatively brief. The result plainly holds for n=1, for if  $j_1$  is the exponent to which  $x_1-p_1/q_1$  divides  $P(x_1)$  then, by Gauss' lemma, we have

$$P(x_1) = (q_1x_1 - p_1)^{j_1}Q(x_1),$$

where Q is a polynomial with integer coefficients; thus the leading coefficient of P is at least  $q_1^{i_1}$ , whence  $j_1/r_1 < \delta \eta < \epsilon$ , as required. We now assume the validity of the proposition with n replaced by n-1 and we proceed to establish the assertion for  $n \ (\geq 2)$ .

We begin by writing P in the form

$$\phi_0 \psi_0 + \ldots + \phi_{s-1} \psi_{s-1}$$

where the  $\phi$ 's and  $\psi$ 's are polynomials in the variables  $x_1, \ldots, x_{n-1}$  and  $x_n$  respectively with rational coefficients, and we choose one such representation for which  $s \ (\leq r_n + 1)$  is minimal. Then there exist Wronskians U', V' of the  $\phi$ 's and  $\psi$ 's respectively which do not vanish identically, and clearly W = U'V' can be expressed as a determinant of order s with  $\Delta^{(j)}(i!)^{-1} (\partial/\partial x_n)^i P(x_1, \ldots, x_n)$ 

in the (i+1)th row and (j+1)th column, where the  $\Delta^{(j)}$  are operators

as in §2 with  $j_n = 0$ . Hence W is a polynomial with degree at most  $sr_j$  in  $x_j$  and with  $\|W\| \leq (8^{rn} \|P\|)^s \leq q_1^{2\delta\eta rs}$ .

where  $r=r_1=\max r_m$ ; here we are using the hypothesis  $q_1^{\delta\eta}>8^n$  and the observations that  $\Delta^{(f)}$  acting on any monomial in P introduces a factor not exceeding  $2^{rn}$ , that there are at most  $2^{rn}$  such monomials, and that the number of terms obtained on expanding the determinant, for W is  $s!\leqslant 2^{rs}$ . Now, again by Gauss' lemma, we have W=UV, where U,V are polynomials with integer coefficients in the variables  $x_1,\ldots,x_{n-1}$  and  $x_n$  respectively, given by some rational multiples of U',V'; and clearly the bound for  $\|W\|$  obtains also for  $\|U\|$  and  $\|V\|$ . Thus, by our inductive hypothesis, it follows, on taking  $2\delta$  in place of  $\delta$ , that the index of U with respect to the  $p_m/q_m$  and  $r_m$  is at most  $2^{-5+1/2^{n-1}}s\epsilon^2$ . Further, by the case n=1 of the proposition together with the hypothesis  $q_n^{rn}\geqslant q_1^{nr_1}$ , the same bound applies for the index of V. We conclude therefore that the index of W is at most  $\frac{1}{8}s\epsilon^2$ .

On the other hand, the index of the general element in the determinant for W is at least

$$\phi_4 - \sum_{m=1}^{n-1} j_m / r_m$$

where  $\phi_i = \theta - i/r_n$ ,  $\theta$  denotes the index of P, and

$$j_1+\ldots+j_{n-1}=j\leqslant s-1\leqslant r_n;$$

further, by hypothesis, we have  $\delta r_m > r_{m+1}$  and so the above sum is at most  $\delta$ . Hence the index of W is at least

$$\sum_{i=0}^{s-1} \max (\phi_i - \delta, 0) \geqslant \sum_{i=0}^{s-1} \max (\phi_i, 0) - s\delta.$$

But if  $\theta r_n < s-1$  then the last sum is

$$([\theta r_n]+1)\left(\theta-[\theta r_n]/(2r_n)\right)\geqslant \tfrac{1}{4}\theta^2s,$$

and if  $\theta r_n \geqslant s-1$  then it is

$$\theta s - \tfrac{1}{2} s(s-1)/r_n \, \geqslant \, \tfrac{1}{2} \theta s.$$

On comparing estimates, we obtain

$$\max(\frac{1}{2}\theta, \frac{1}{4}\theta^2) \leqslant \frac{1}{8}\epsilon^2 + \delta \leqslant \frac{1}{4}\epsilon^2$$
,

whence  $\theta \leqslant \epsilon$ , as required.

#### 4. A combinatorial lemma

We prove now a lemma of a combinatorial nature relating to the law of large numbers. A result of this kind occurred first in the work of Schneider, and it was utilized later by Roth who gave a simplified proof due to Davenport. Another proof, attributed to Reuter, and furnishing a slightly stronger theorem, was given by Mahler in his tract, and Schmidt subsequently obtained the generalization we establish here.

**Lemma 2.** Suppose that  $r_1, ..., r_n$  and k are positive integers and that  $0 < \epsilon < 1$ . Then the number of non-negative integers

$$j_{lm} \quad (1 \leqslant l \leqslant k, 1 \leqslant m \leqslant n)$$

satisfying

$$\sum_{l=1}^k j_{lm} = r_m \quad (1 \leqslant m \leqslant n), \qquad \sum_{m=1}^n j_{1m}/r_m < n/k - \epsilon n,$$

is at most

$$\binom{r_1+k-1}{r_1}\cdots\binom{r_n+k-1}{r_n}e^{-\frac{1}{4}\epsilon^2n}.$$

We commence the proof by observing that the required number N of integers  $j_{lm}$  is given by  $\sum_{\nu_1(j_{11})\dots\nu_n(j_{1n})} \sum_{\nu_n(j_{2n})} \nu_n(j_{2n})$ 

where the sum is over all non-negative integers  $j_1, ..., j_{1n}$  satisfying the given inequality, and  $\nu_m(j)$  denotes the number of solutions of the equation

$$\sum_{l=2}^{k} j_{lm} = r_m - j$$

in non-negative integers  $j_{2m},...,j_{km}$ , that is

$$\nu_m(j) = \binom{r_m-j+k-2}{k-2}.$$

Hence we see that the multiple sum

$$\sum_{j_1=0}^{r_1} \dots \sum_{j_m=0}^{r_m} \nu_1(j_1) \dots \nu_m(j_m) \exp \left\{ \frac{1}{2} \varepsilon \left( n/k - \sum_{m=1}^n j_m/r_m \right) \right\}$$

is at least  $Ne^{\frac{1}{2}\epsilon^2n}$ . Now the sum can be written alternatively in the form

$$\prod_{m=1}^{n} \left\{ \sum_{j_{m}=0}^{r_{m}} \nu_{m}(j_{m}) \exp\left(\frac{1}{2}\epsilon \rho_{m}\right) \right\},\,$$

† Cf. the paper of Wirsing cited earlier: Proc. Symposia Pure Math. (Amer. Math. Soc.), 20 (1971), 213-47.

## 74 RATIONAL APPROXIMATIONS TO ALGEBRAIC NUMBERS

where  $\rho_m = 1/k - j_m/r_m$ , and clearly  $|\rho_m| \le 1$ . But if  $|x| \le 1$  then  $e^x < 1 + x + x^2$ , and so

$$\exp\left(\frac{1}{2}\epsilon\rho_m\right) < \frac{1}{2}\epsilon\rho_m + \exp\left(\frac{1}{4}\epsilon^2\right).$$

Further we have

$$\sum_{i=0}^{r_m} \nu_m(j_m) \rho_m = 0;$$

for  $\rho_m$  can plainly be expressed as

$$(r_m - j_m)/r_m - (1 - 1/k),$$

and it is easily verified by induction on r that

$$\sum_{j=0}^{r} {r-j+k-2 \choose k-2} = {r+k-1 \choose r},$$

$$\sum_{j=0}^r j \binom{j+k-2}{k-2} = r \left(1-\frac{1}{k}\right) \binom{r+k-1}{r}.$$

Thus, on appealing again to the first of the above binomial identities, we obtain

 $\prod_{m=1}^{n} \left\{ \begin{pmatrix} r_m + k - 1 \\ r_m \end{pmatrix} e^{\frac{1}{4}\epsilon^2} \right\} \geqslant N e^{\frac{1}{4}\epsilon^2 n},$ 

and this gives the asserted estimate.

#### 5. Grids

Let T be a subspace of k-dimensional Euclidean space spanned by linearly independent vectors  $\mathbf{u}_1, ..., \mathbf{u}_{k-1}$ . By a grid of size s on T we shall mean the finite set of vectors of the form

$$w_1\mathbf{u}_1+\ldots+w_{k-1}\mathbf{u}_{k-1},$$

where  $w_1, ..., w_{k-1}$  run through all rational integers with  $1 \le w_l \le s$ .

Now let  $T_m$   $(1 \le m \le n)$  be any subspaces as above, and let  $\Gamma_m$  be a grid of size  $s_m$  on  $T_m$ . Further let T,  $\Gamma$  signify the cartesian products  $T_1 \times \ldots \times T_n$  and  $\Gamma_1 \times \ldots \times \Gamma_n$  respectively. We shall denote by P a polynomial as indicated at the beginning of § 3 with degree  $r_m$  in  $x_{1m}, \ldots, x_{km}$ , and we shall signify by  $\Delta_m^{(j)}$  a differential operator as in § 2, acting on  $x_{1m}, \ldots, x_{km}$ . The following simple lemma, due to Schmidt, is fundamental to the proof of Theorem 7.1.

**Lemma 3.** If, for some integers  $t_m$   $(1 \le m \le n)$  with  $s_m(t_m+1) > r_m$ , all polynomials  $\Delta_1^{(j_1)} \dots \Delta_n^{(j_n)} P$  with  $j_m \le t_m$  vanish everywhere on  $\Gamma$ , then P vanishes identically on T.

GRIDS 75

It is clear that the lemma follows at once by induction from the case n=1, and it will suffice therefore to prove the latter. Further, one can obviously assume, by applying a linear transformation, that  $T_m$  is the plane  $x_{km}=0$ , with basis consisting of the first k-1 rows of the unit matrix of order k. Thus, omitting the suffix m, we see that it is enough to prove:

A polynomial  $P(x_1, ..., x_{k-1})$  with degree r vanishes identically if all  $\Delta^{(j)}P$  with  $j \leq t$  vanish at all integer points  $(w_1, ..., w_{k-1})$  with  $1 \leq w_l \leq s$ , where s(t+1) > r.

Here  $\Delta^{(j)}$  denotes a differential operator on  $x_1, \ldots, x_{k-1}$  of order j. The assertion is clearly valid for k=2, since a polynomial in one variable with degree r cannot have more than r zeros, and we shall assume the proposition when k is replaced by k-1. If now P does not vanish identically then there is a largest integer q such that the rational function

 $Q = (x_1 - 1)^{-q} \dots (x_1 - s)^{-q} P$ 

is in fact a polynomial, and since, by hypothesis, s(t+1) > r, we have  $q \le t$ . Further, by choice of q, one at least of the polynomials  $Q(w_1, x_2, ..., x_{k-1})$  with  $1 \le w_1 \le s$  does not vanish identically; let this be R. Then  $\Delta^{(j)}R$  vanishes at all integer points  $(w_2, ..., w_{k-1})$  with  $1 \le w_l \le s$ , where  $\Delta^{(j)}$  is any differential operator on  $x_2, ..., x_{k-1}$  with order  $j \le t-q$ . But R has degree at most r-sq < (t-q+1)s, and this is plainly contrary to the inductive hypothesis. The contradiction establishes the assertion.

## 6. The auxiliary polynomial

For each m with  $1 \le m \le n$  we shall denote by  $L_{lm}$  ( $1 \le l \le k$ ) linear forms in  $x_{1m}, \ldots, x_{km}$  with real algebraic integer coefficients. Further we shall denote by d the degree of the field K generated by all the coefficients over the rationals, and we shall signify by  $c_1, c_2, \ldots$  numbers greater than 1 which depend on these coefficients only.

Let now  $r_1, ..., r_n$  be any positive integers, and let  $r = \max r_m$ . Further suppose that  $0 < \epsilon < 1$  and that  $e^{\frac{1}{4}\epsilon^2n} > 2kd$ . Adopting the notation of § 3, we have

**Lemma 4.** There is a polynomial P with degree at most  $r_m$  in  $x_{1m}, \ldots, x_{km}$  and with height at most  $c_1^r$  such that, for each l with  $1 \le l \le k$ , the index of P with respect to the  $L_{lm}$  and  $r_m$  is at least  $n/k - \varepsilon n$ .

It can be assumed, without loss of generality, that, for all l, m, the coefficient of  $x_{1m}$  in  $L_{lm}$ , say  $\alpha_{lm}$ , is not 0. Then P has to be determined such that, for all l and all non-negative integers  $j_1, \ldots, j_n$  with

$$\sum_{m=1}^{n} j_m/r_m < n/k - \epsilon n,$$

the polynomials

$$(j_1! \dots j_n!)^{-1} (\partial/\partial x_{11})^{j_1} \dots (\partial/\partial x_{1n})^{j_n} P$$

vanish identically when  $-L_{lm}$ , with  $x_{1m}$  equated to 0, is substituted for  $x_{1m}$ , and the factor  $\alpha_{lm}$  is included to multiply each of  $x_{2m}, \ldots, x_{km}$ . Now these polynomials are homogeneous in  $x_{2m}, \ldots, x_{km}$  with degree  $r_m - j_m$  and hence, by Lemma 2, they have, in total, at most  $kNe^{-\frac{1}{4}e^2n}$  coefficients, where N denotes the product of binomial factors occurring in the enunciation of the lemma. Each coefficient is a linear form in the coefficients of P, and there are precisely N of the latter. Furthermore, the coefficients in the linear forms are algebraic integers in K with sizes at most  $c_2^r$  (cf. the estimates in § 3). It follows, on utilizing an integral basis for K and recalling the hypothesis  $e^{\frac{1}{4}e^2n} > 2kd$ , that one has to satisfy at most  $\frac{1}{2}N$  linear equations with rational integer coefficients each having absolute value at most  $c_3^r$  (cf. § 3, Chapter 6). The required result is now obtained from Lemma 1 of Chapter 2.

## 7. Successive minima

We recall from the Geometry of Numbers that if R is any convex body in k-dimensional Euclidean space, then the numbers  $\lambda_l$   $(1 \le l \le k)$ , given by the infimum of all  $\lambda > 0$  such that  $\lambda R$  contains l linearly independent integer points, are termed the successive minima of R, and they have the property that  $\lambda_1 \dots \lambda_k V$ , where V denotes the volume of R, is bounded above and below by positive numbers depending only on k.

We now combine the preceding lemmas to obtain a proposition on the penultimate minimum of a certain parallelepiped, which will be the main instrument in the proof of Theorem 7.1. We shall denote by  $M_1, \ldots, M_k$  linear forms in  $x_1, \ldots, x_k$  with real algebraic integer coefficients constituting a non-singular matrix A, and we shall signify by  $M'_1, \ldots, M'_k$  the adjoint linear forms with coefficients given by the columns of  $A^{-1}$ . Further we shall signify by S some non-empty set of suffixes i such that  $M'_i$  does not represent zero for any integral values, not all 0, of the variables; the assumption that S exists involves, of course, some loss of generality. We prove:

**Lemma 5.** For any  $\zeta > 0$  there exists c > 0 such that for all positive  $\mu_1, \ldots, \mu_k$  satisfying  $\mu_1 \ldots \mu_k = 1$  and  $\mu_i \ge 1$  for i in S, the penultimate minimum  $\lambda_{k-1}$  of the parallelepiped  $|M_i| \le \mu_i$   $(1 \le l \le k)$  exceeds  $\mu^{-l}$ , where  $\mu$  denotes the maximum of  $\mu_1, \ldots, \mu_k$  and c.

It will be seen that the lemma immediately implies Roth's theorem, that is the case n = 1 of Theorem 7.1; this follows on taking

$$M_1 = \alpha_1 x_1 - x_2, \quad M_2 = x_2$$

and S to consist just of the suffix 2, as is possible since  $\alpha_1$  is irrational.

We show first that it suffices to prove a modified version of Lemma 5. Suppose that  $Q \geqslant \mu^k$  and let  $\omega_1, \ldots, \omega_k$  be defined by  $\mu_l = Q^{\omega_l}$ . Then since  $\mu_1 \ldots \mu_k = 1$  we have  $\omega_1 + \ldots + \omega_k = 0$  and clearly  $\omega_i \geqslant 0$  for i in S. Clearly also  $\omega_l \leqslant 1$  for all l and, since again  $\mu_1 \ldots \mu_k = 1$  we have  $\mu_l \geqslant Q^{-1}$ , whence  $\omega_l \geqslant -1$ . Now for any positive integer N there are rationals  $\omega_1', \ldots, \omega_n'$  with denominator N satisfying  $|\omega_l - \omega_l'| < 1/N$  and  $|\omega_l'| \leqslant 1$  for all l, and also  $\omega_1' + \ldots + \omega_k' = 0$ ; indeed one has merely to take  $N\omega_1' = [N\omega_1]$  and, having defined  $\omega_1', \ldots, \omega_{l-1}'$ , to take  $N\omega_l'$  as  $[N\omega_l]$  or  $-[-N\omega_l]$  according as  $\omega_1' + \ldots + \omega_{l-1}'$  does or does not exceed  $\omega_1 + \ldots + \omega_{l-1}$ . Plainly the  $\omega_1', \ldots, \omega_k'$  belong to a finite set of rationals independent of Q, and the minimum  $\lambda_{k-1}'$  of the parallelepiped  $|M_l| \leqslant Q^{\omega_l'}$  ( $1 \leqslant l \leqslant k$ ) exceeds  $Q^{-1/N}\lambda_{k-1}$ . Hence it is enough to prove:

For any real  $\omega_1, ..., \omega_k$  with  $\omega_1 + ... + \omega_k = 0$ ,  $|\omega_l| \le 1$   $(1 \le l \le k)$  and  $\omega_i \ge 0$  for all i in S, and for any  $\zeta > 0$ , there exists C > 0 such that, for all Q > C, the minimum  $\lambda_{k-1}$  of the parallelepiped

$$|M_l| \leqslant Q^{\omega_l} \quad (1 \leqslant l \leqslant k)$$

exceeds  $Q^{-\zeta}$ .

We shall suppose that  $\zeta \leq 1$ , as obviously we may, and we shall signify by d the degree of the field generated by the elements of A over the rationals. Let  $\varepsilon$  be any positive number less than  $\zeta/(8k)^2$ , let n be any integer satisfying the condition preceding Lemma 4, and let  $\delta$  be defined as in Lemma 1. We shall assume that there is an unbounded set of values of Q such that  $\lambda_{k-1} \leq Q^{-\zeta}$ , and we shall ultimately derive a contradiction. We select a sufficiently large  $Q_1$  in this set, that is  $Q_1 > c_1$ , where  $c_1$ , like  $c_2$ ,  $c_3$  below, depends only on A, k, n, d,  $\varepsilon$ ,  $\delta$ ,  $\zeta$  and the  $\omega$ 's. We then select further elements  $Q_2, \ldots, Q_n$  in the set such that  $Q_m^{\frac{1}{2}\delta} > Q_{m-1}$   $(1 < m \leq n)$ , whence clearly  $Q_1 < \ldots < Q_n$ . Finally we choose positive integers  $r_1, \ldots, r_n$  such that  $Q_1^{\text{tr}_1} > Q_n$  and

$$Q_1^{r_1}\leqslant Q_m^{r_m}\leqslant Q_1^{(1+\epsilon)r_1}\quad (1\leqslant m\leqslant n);$$

then plainly the condition preceding Lemma 1 is satisfied.

We observe now that the hypotheses of Lemma 4 hold when *Ifa =* JMjfXn,), where x^ denotes the vector *(xXm,...,x^)*; let *P* be the polynomial constructed there. Further we note that, for any *Q* as above, there exist linearly independent integer points ux *uk* with U| in *AtB,* where *R* denotes the given parallelepiped and *Av ...,* Afc its successive minima. Moreover, there is a linear form *L* with relatively prime integer coefficients, unique except for a factor + 1, which vanishes at *ult* ...,ufc\_x; we take uIm and *Lm* to be these u, and *L* respectively when *Q* = *Qm.* We shall verify later that, if *Q* is sufficiently large, then *q — \\L\\* satisfies *Q°* < *q* < *Q<sup>c</sup> ',* where c, c' are positive numbers depending only on £ and *d.* Assuming this for the present, it follows that all the hypotheses of Lemma 1 are satisfied with *v* = *cjc',* provided that *clt* and so also *q<sup>t</sup>* and *Qu* are large enough. Hence we conclude that the index of *P* with respect to the *Lm* and *rm* is at most *e.*

We proceed to prove that, with the notation of § 5, all polynomials AP with<sup>B</sup>

$$\Delta = \Delta_1^{(j_1)} \dots \Delta_n^{(j_n)}, \quad \sum_{m=1}^n j_m/r_m < 2\epsilon n$$

vanish everywhere on *T,* where *Tm* is the grid of size [e-1] + 1 on the space *Tm* spanned by u(m (1 < *I < k).* This implies, by Lemma 3, on taking *tm* = [erm], that all polynomials AP, with £jm/rm < *en,* vanish identically on the *n(k—* 1)-dimensional space of solutions of
