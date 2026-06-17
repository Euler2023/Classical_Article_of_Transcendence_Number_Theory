
$$L_1 = \ldots = L_n = 0.$$

But the latter contradicts the above conclusion concerning the index of P, and the contradiction establishes the lemma. To prove the proposition, let AP be any of the polynomials in question and let P' be the polynomial in new variables *ylm* obtained from AP by the linear substitution *ylm* = Xjm. Then it is readily verified that P' has height at most c£, where *r* = max *rm.* Further, since, by assumption, AJk\_1 < *Q~t,* we have for any xm on T

$$|y_{lm}| < k(\epsilon^{-1}+1) Q_m^{\omega_l-\zeta} < Q_m^{\omega_l-\frac{1}{2}\zeta}$$

Thus, by Lemma 4, it follows that, for all points on F, we have |AP| < c^e\*, where

$$s = \sum_{l=1}^{k} \sum_{m=1}^{n} (\omega_{l} - \frac{1}{2}\zeta) j_{lm} \log Q_{m},$$

and*<sup>j</sup> <sup>l</sup> <sup>m</sup>* are some non-negative integers with

$$\sum_{l=1}^{k} j_{lm} \leqslant r_{m} \quad (1 \leqslant m \leqslant n), \quad n/k - \sum_{m=1}^{n} j_{lm}/r_{m} < 3\epsilon n \quad (1 \leqslant l \leqslant k).$$

Denoting, for brevity, the left-hand side of the last inequality by  $h_l$ , we see that, by the first inequality,  $h_1 + \ldots + h_k \ge 0$ , and so both inequalities together imply that  $|h_l| < 3kne$ . Further, since  $|\omega_l| \le 1$ , we obtain, in view of the initial choice of  $r_1, \ldots, r_n$ ,

$$s\leqslant r_1\log Q_1\sum_{l=1}^k\sum_{m=1}^n\{(\omega_l-\tfrac12\zeta)j_{lm}/r_m+2\epsilon\}.$$

But now, by virtue of our estimate for  $h_1$  and the hypothesis

$$\omega_1 + \ldots + \omega_k = 0,$$

the double sum here differs from  $-\frac{1}{2}\zeta n$  by at most  $8k^2n\epsilon$ . Since, by definition,  $\epsilon < \zeta/(8k)^2$ , it follows that  $|\Delta P| < Q_1^{-\frac{1}{4}\zeta nr} < 1$ , provided  $Q_1$  is sufficiently large. On the other hand,  $\Delta P$  is a rational integer for all points on  $\Gamma$ , and hence  $\Delta P = 0$ , as required.

It remains only to prove the assertion concerning q = ||L||. Let U be the matrix with columns  $\mathbf{u}_1, ..., \mathbf{u}_k$  and let  $\mathbf{v}_1, ..., \mathbf{v}_k$  be the rows of  $U^{-1}$ . Then clearly  $\rho \mathbf{v}_k$  is the coefficient vector of L for some rational  $\rho$ . Since  $L(\mathbf{u}_k)$  is an integer and  $\mathbf{v}_k \mathbf{u}_k = 1$ ,  $\rho$  is in fact an integer. Further  $\rho$ divides det U, for plainly  $U^{-1} = \operatorname{adj} U/\operatorname{det} U$ . Furthermore we have det  $U \leq 1$ , where the implied constant depends only on A, for certainly R has volume  $\gg 1$  and hence, by the property of successive minima quoted at the beginning,  $\det(AU) \leqslant 1$ . It follows that each element of  $(\det \mathbf{U}) \mathbf{v}_k$  is a rational integer  $\leqslant q$ . Hence the element in the kth row and lth column of adj (AU), namely  $(\det(AU)) M'_{1}(\mathbf{v}_{k})$ , is an algebraic integer with size  $\leq q$ . But by hypothesis we have  $\lambda_{k-1} < Q^{-\zeta}$  and  $\omega_1 + \ldots + \omega_k = 0$ , and thus the element is also  $\ll Q^{-\omega_l-(k-1)\zeta}$ . We conclude that, for l in S, the element is both  $\Rightarrow q^{-d}$  and  $\leqslant Q^{-(k-1)\zeta}$ , and, since S is assumed non-empty, this gives the required lower bound for q. The upper bound follows from the identity  $U^{-1} = (AU)^{-1} A$ , on observing, as above, that the elements in the kth row of  $(AU)^{-1}$  are  $\leqslant Q$ .

## 8. Comparison of minima

We prove first a general lemma of Davenport, and we proceed then to show that, with some proviso, the minima  $\lambda_{k-1}$  and  $\lambda_k$  of the parallelepiped of Lemma 5 differ only by a small factor. Constants implied by  $\leq$  will depend only on k.

<sup>† &#</sup>x27;det' and 'adj' are abbreviations for determinant and adjoint respectively.

<sup>‡</sup> We are using Vinogradov's notation; by  $a \le b$  one means |a| < bc for some constant c, and similarly for  $\gg$ .

**Lemma 6.** Let  $L_1, ..., L_k$  be real linear forms with determinant 1 and let  $\lambda_1, ..., \lambda_k$  be the successive minima of the parallelepiped

$$|L_l| \leqslant 1 \quad (1 \leqslant l \leqslant k).$$

Suppose that  $\rho_1 \ge ... \ge \rho_k > 0$  and that

$$\rho_1 \lambda_1 \leqslant \ldots \leqslant \rho_k \lambda_k, \quad \rho_1 \ldots \rho_k = 1.$$

Then for some permutation  $\rho'_1, \ldots, \rho'_k$  of  $\rho_1, \ldots, \rho_k$ , the successive minima  $\lambda'_1, \ldots, \lambda'_k$  of the parallelepiped  $\rho'_l | L_l | \leq 1$   $(1 \leq l \leq k)$  satisfy

$$\rho'_l \lambda_l \leqslant \lambda'_l \leqslant \rho'_l \lambda_l \quad (1 \leqslant l \leqslant k).$$

**Proof.** There certainly exist linearly independent integer points  $\mathbf{x}_1, \ldots, \mathbf{x}_k$  such that one at least of  $|L_1|, \ldots, |L_k|$  assumes the value  $\lambda_l$  at  $\mathbf{x}_l$ , and we denote by  $S_l$  the space spanned by  $\mathbf{x}_1, \ldots, \mathbf{x}_l$ . Further, for each  $l \geq 2$ , there is a non-trivial linear relation  $a_1 L_1 + \ldots + a_l L_l = 0$  satisfied identically on  $S_{l-1}$ , and  $L_1, \ldots, L_k$  can be permuted so that  $|a_l|$  is maximal; this gives

$$|L_1| + \ldots + |L_{l-1}| > \frac{1}{2}(|L_1| + \ldots + |L_l|)$$

identically on  $S_{l-1}$ , whence by induction

$$|L_1| + \ldots + |L_l| \ge 2^{l-k}(|L_1| + \ldots + |L_k|)$$

identically on  $S_i$  for i = 1, 2, ..., k. Now for any j it is clear that every point in  $S_i$  not in  $S_{i-1}$  satisfies

$$\max\left(|L_1|,...,|L_k|\right) \geqslant \lambda_j,$$

and thus, in view of the inequality obtained above, it satisfies also

$$\max(\rho_1|L_1|,\ldots,\rho_k|L_k|) \gg \rho_i \lambda_i.$$

By hypothesis,  $\rho_j \lambda_j \geqslant \rho_l \lambda_l$  for  $j \geqslant l$ , and the required lower bound for  $\lambda_l'$  follows on taking  $\rho_1', \ldots, \rho_k'$  to be the permutation of  $\rho_1, \ldots, \rho_k$  inverse to that associated with  $L_1, \ldots, L_k$ . The upper bound is a consequence of the equation  $\rho_1 \ldots \rho_k = 1$  together with the property, noted earlier, that  $\lambda_1 \ldots \lambda_k$  and  $\lambda_1' \ldots \lambda_k'$  are both  $\leqslant 1$  and  $\geqslant 1$ .

**Lemma 7.** The last two minima of the parallelepiped of Lemma 5 satisfy  $\lambda_{k-1} \gg \lambda_k \mu^{-k\zeta}$ , provided that  $\lambda_1 \mu_i > \mu^{-\zeta}$  for all i in S.

**Proof.** The hypotheses of Lemma 6 hold with  $L_l$   $(1 \le l \le k)$  given by  $\mu_l^{-1}M_l$  and  $\rho_l = \rho/\lambda_l$   $(1 \le l < k)$ ,  $\rho_k = \rho/\lambda_{k-1}$ ,

where  $\rho$  is defined by the equation  $\rho_1 \dots \rho_k = 1$ . Let  $\rho_1', \dots, \rho_k'$  be the permutation of  $\rho_1, \dots, \rho_k$  indicated in the lemma, and let  $\mu_l' = \mu_l/\rho_l'$ . Assume first that  $\mu_i' \geqslant 1$  for all i in S. Then from Lemma 5 with  $\mu_l$  replaced by  $\mu_l'$ , we infer that, for any  $\zeta' > 0$ , there exists c' > 0 such that  $\lambda_{k-1}' > \mu'^{-\zeta'}$ , where  $\mu'$  denotes the maximum of  $\mu_1', \dots, \mu_k'$  and c'. On the other hand, from Lemma 6,  $\lambda_{k-1}' \ll \rho_{k-1} \lambda_{k-1} = \rho$ , and clearly, since  $\lambda_1 \dots \lambda_k \ll 1$ , we have  $\rho^k \ll \lambda_{k-1}/\lambda_k$ . Thus it suffices to prove that  $\mu'^{\zeta'} \ll \mu^{\zeta}$  if  $\zeta'$  is chosen sufficiently small. But by hypothesis, since S is assumed non-empty, we have  $\lambda_1 \mu > \mu^{-\zeta}$ ; further, since  $\lambda_l \geqslant \lambda_1$  for all l, we see that  $\rho \gg \lambda_1$  and  $\lambda_1^{k-1} \lambda_{k-1} \ll 1$ . Hence we obtain

$$\mu' \leqslant \mu \lambda_{k-1}/\rho \ll \mu \lambda_1^{-k} < \mu^{k(\zeta+1)+1},$$

and the required result follows. If, contrary to the above assumption,  $\mu'_i < 1$  for some i in S, then, on observing that by hypothesis

$$\rho \mu_i' \geqslant \lambda_1 \mu_i > \mu^{-\zeta}$$

we obtain  $\rho > \mu^{-\zeta}$  and the required result again follows.

## 9. Exterior algebra

For any vectors  $\mathbf{x}_1, ..., \mathbf{x}_l$  in  $R^k$  with  $1 \leq l < k$ , one denotes by  $\mathbf{x}_1 \wedge ... \wedge \mathbf{x}_l$  the vector in  $R^m$  whose elements are the  $m = \binom{k}{l}$  subdeterminants of order l formed from the k by l matrix with columns  $\mathbf{x}_1, ..., \mathbf{x}_l$ . We shall utilize some well-known properties of this product; in particular, we shall require Laplace's identity

$$(\mathbf{x}_1 \wedge \ldots \wedge \mathbf{x}_l) (\mathbf{y}_1 \wedge \ldots \wedge \mathbf{y}_l) = \det(\mathbf{x}_i \mathbf{y}_i),$$

where on the left one has the usual vector dot product, and also the relation  $\det \mathbf{A}_{\sigma} = (\det \mathbf{A})^{lm/k},$ 

which holds for any matrix A of order k with column vectors  $\mathbf{a}_1, \ldots, \mathbf{a}_k$ , say, where  $\mathbf{A}_{\sigma} = \mathbf{a}_{i_1} \wedge \ldots \wedge \mathbf{a}_{i_l}$  and  $\sigma$  runs through all sets of l distinct integers  $i_1, \ldots, i_l$  from  $1, \ldots, k$ .

We shall need, in addition, the following lemma, due to Mahler, on compound convex bodies. A will signify a matrix as above with  $\det A = 1$ , and, as in § 8, constants implied by  $\ll$  will depend only on k. Further we shall denote by ax the linear form in the elements of x with coefficient vector a.

<sup>†</sup> Short proofs are given in Schmidt's tract (Bibliography).

**Lemm a 8.** *The successive minima* Alt *...,Ak and vl,...,vm of the parallelepipeds* |a <sup>&</sup>lt; x|<l(l<i<A; ) *and \A.aX\* < 1, *respectively,*

*where r runs through all sets a as above,* AT = II Ay, *the product being taken over all j in T, and A.* < A. ^ ... ^ A. . <sup>T</sup> W l

\*\* '1\* 1

*Proof.* Let **xx xt** be linearly independent integer points such that **|a<Xy|** < Aj (1 < j < *k),* and let XT be defined like A, above, with x in place of a. By Laplace's identity we have

$$|\mathbf{A}_{\sigma} \mathbf{X}_{\tau}| = |\det(\mathbf{a}_{i} \mathbf{x}_{j})| \leq m! \lambda_{\tau},$$

where *i, j* run through all elements of *a, j* respectively. Hence, for each *i* with 1 ^ *i*; ^ TO, we have lA^X^I < AT| and so *v( <£* ATj. But since, by hypothesis, det A = 1, we have det *\ <sup>a</sup>* = 1, and thus the volume of the parallelepiped |AffX| ^ 1 is *2m.* Thus *vt... vm* > 1 and since ATl... ATm < 1 it follows that *vl* > AT, as required.

# **10. Proof of main theorem**

It will suffice to prove Theorem 7.1 under the assumption that a1(..., an are real algebraic integers, for clearly the general result then follows on multiplying each a,- by the leading coefficient in its minimal polynomial. We shall signify by a,- (1 ^ *j* < *n)* the vector in i?n+1 given by (e^, *a.j),* where elt..., en denote the rows of the unit matrix of order n. Further, for brevity, we shall write *k* = n + 1, and we shall denote by afc the vector (0, ..., 0, 1) in *Rk .* Constants implied by ^ or > will depend only ona, an,it,e and the quantities £, £ to be defined below.

We show first that the theorem is a consequence of the following proposition.

*For any* £ > 0 *and any positive numbers /ilt* ••-,/\*\* *with /ii--.uk=* 1 *and /tj <* 1 (1 < *j < k), the first minimum* Ax *of the parallelepiped \atx\* s£ */if* (1 < *j* < *k) exceeds p-l if /i* > *fik and fi p* **1.**

The proof proceeds by induction on n; we have already remarked that the case *n* = 1 is an immediate consequence of Lemma 5, and we assume now that the theorem holds when *n* is replaced by *n* — 1. Let *q* be a positive integer satisfying the inequality occurring in the enunciation, and let

$$\mu_j = q^{\epsilon/(2n)} \|q\alpha_j\| \quad (1 \leqslant j \leqslant n).$$

Further let  $\mu_k = (\mu_1 \dots \mu_n)^{-1}$ , where k = n+1 as above. Then clearly  $\mu_k > q^{1+\frac{1}{2}\epsilon}$  and moreover the first minimum  $\lambda_1$  of the parallelepiped  $|\mathbf{a}_j \mathbf{x}| \leq \mu_j$   $(1 \leq j \leq k)$  is at most  $q^{-\epsilon/(2n)}$ . But, on appealing again to the given inequality and applying the inductive hypothesis, we see that, if  $q \gg 1$ , then  $\mu_j < 1$  for all j < k. Hence the proposition above shows that  $\lambda_1 > \mu^{-\xi}$  for any  $\xi > 0$  and any  $\mu$  with  $\mu \gg 1$  and  $\mu \gg \mu_k$ . Furthermore, by the case n = 1 of the theorem, we have  $\mu_j > q^{-1}$   $(1 \leq j \leq n)$ , whence  $\mu_k \leq q^n$ . Plainly the estimates for  $\lambda_1$  are inconsistent if  $\xi$  is sufficiently small, and the contradiction proves the theorem.

Preliminary to the proof of the proposition, we observe that, with the notation of § 9, the linear forms  $M_{\tau} = \mathbf{A}_{\tau} \mathbf{X}$  satisfy the hypotheses of § 7 with S given by those sets  $\tau$  which include k. For it is easily verified from the Laplace expansions of A that, as  $\sigma$  runs through the complement of  $\tau$  in 1, ..., k, the forms  $\mathbf{A}_{\sigma} \mathbf{X}$  constitute the set adjoint to the  $M_{\tau}$ , except possibly for a sign change; further, if  $\sigma$  does not include k, we have

 $\mathbf{A}_{\sigma}\mathbf{X} = X_{\sigma} + \Sigma(\pm \alpha_{j}) X_{\sigma-j+k},$ 

where the summation is over all j in  $\sigma$ , on the right there occur the co-ordinates of X, and  $\sigma - j + k$  denotes the set  $\sigma$  with k in place of j. By hypothesis 1,  $\alpha_1, \ldots, \alpha_n$  are linearly independent over the rationals, and thus we see that  $A_{\sigma}X \neq 0$  for all integer vectors  $X \neq 0$ , as required.

The proof of the proposition proceeds by induction on k; the result plainly holds for k=2 by Lemma 5, and we assume now that it has been verified for all values up to k-1. Let l be any integer with  $1\leqslant l < k$  and, for any set  $\tau$  of l distinct integers from  $1,\ldots,k$ , let  $\mu_{\tau}=\Pi\mu_{j}$ , where the product is over all j in  $\tau$ . By Lemma 7 we see that the successive minima  $\nu_{1},\ldots,\nu_{m}$  of the parallelepiped  $|M_{\tau}|\leqslant \mu_{\tau}$  satisfy  $\nu_{m-1}\gg\nu_{m}\mu^{-k\zeta}$  for any  $\zeta>0$ , provided that  $\mu\gg1$ ,  $\mu\gg\mu_{\tau}$  for all  $\tau$  and  $\nu_{1}\mu_{\tau}>\mu^{-\zeta}$  for  $\tau$  in S. Further, with the notation of Lemma 8, it is clear that  $\tau_{m}$  and  $\tau_{m-1}$  consist of the integers  $k-l+1,k-l+2,\ldots,k$  and  $k-l,k-l+2,\ldots,k$  respectively. Thus, under the above conditions, we have

$$\lambda_{k-l}\lambda_{k-l+2}\dots\lambda_k\gg\lambda_{k-l+1}\dots\lambda_k\mu^{-k\zeta},$$

that is  $\lambda_{k-l} \gg \lambda_{k-l+1} \mu^{-k\zeta}$ . The required inequality  $\lambda_1 > \mu^{-\xi}$  follows on applying the latter with l=1,2,...,k-1, noting that  $\lambda_k \gg 1$ , and taking  $\zeta$  sufficiently small.

Since evidently  $\mu_{\tau} \leq \mu_{k}$  for all  $\tau$ , it remains only to prove that, for  $\tau$  in S,  $\nu_{1}\mu_{\tau} > \mu^{-\zeta}$  for any  $\mu$  with  $\mu \geqslant 1$  and  $\mu \geqslant \mu_{k}$ . In fact it suffices to show that  $\lambda_{1}\mu_{\tau}^{1l} > \mu^{-\zeta}$ , for, again from Lemma 8, we have  $\nu_{1} \geqslant \lambda_{1} \dots \lambda_{l} \geqslant \lambda_{1}^{l}$ . Now, by the definition of  $\lambda_{1}$ , the parallelepiped  $|\mathbf{a}_{j}\mathbf{x}| \leq \lambda_{1}\mu_{j}(1 \leq j \leq k)$ 

## 84 RATIONAL APPROXIMATIONS TO ALGEBRAIC NUMBERS

contains an integer point  $x \neq 0$ ; in fact the kth co-ordinate of x is not 0 since  $\lambda_1 \leq 1$  by Minkowski's linear forms theorem, whence

$$\lambda_1 \mu_i < 1 \quad (1 \leqslant j < k),$$

and  $\mathbf{a}_j \mathbf{x}$  is simply the jth co-ordinate of  $\mathbf{x}$  when the kth co-ordinate vanishes. It follows that, if  $\tau$  is any element of S, then the parallel-epiped in  $R^l$  given by  $|\mathbf{a}_t \mathbf{x}| \leq \lambda_1 \mu_i$ , where i is restricted to  $\tau$  and the co-ordinates of  $\mathbf{x}$  with suffixes not in  $\tau$  are disregarded, also contains an integer point  $\mathbf{x} \neq 0$ . Hence the first minimum  $\lambda_1'$  of the parallelepiped  $|\mathbf{a}_i \mathbf{x}| \leq \mu_i'$  in  $R^l$ , where  $\mu_i' = \mu_i/\mu_\tau^{1l}$ , is at most  $\lambda_1 \mu_\tau^{1l}$ . It is therefore enough to prove that  $\lambda_1' > \mu^{-l}$ ; but this follows from the inductive hypothesis since clearly  $\Pi \mu_i' = 1$  and  $\mu_\tau > 1$ . The theorem is herewith established.

## MAHLER'S CLASSIFICATION

## 1. Introduction

A classification of the set of all transcendental numbers into three disjoint aggregates, termed S-, T- and U-numbers, was introduced by Mahler<sup>†</sup> in 1932, and it has proved to be of considerable value in the general development of the subject. The first classification of this kind was outlined by Maillet<sup>‡</sup> in 1906, and others were described by Perna<sup>‡</sup> and Morduchai-Boltovskoj; but to Mahler's classification attaches by far the most interest.

As in the previous chapter, we define the height of a polynomial as the maximum of the absolute values of its coefficients, and we shall speak of the height only for polynomials with integer coefficients, not all 0. Let now  $\xi$  be any complex number, and for each pair of positive integers n, h, let P(x) be a polynomial with degree at most n and height at most h for which  $|P(\xi)|$  takes the smallest positive value; and define  $\omega(n,h)$  by the equation  $|P(\xi)| = h^{-n\omega(n,h)}$ . Further define

$$\omega_n = \limsup_{h \to \infty} \omega(n, h), \quad \omega = \limsup_{n \to \infty} \omega_n,$$
