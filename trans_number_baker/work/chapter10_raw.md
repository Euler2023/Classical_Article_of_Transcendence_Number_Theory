
and let  $\nu$  be the least positive integer n for which  $\omega_n = \infty$ , writing  $\nu = \infty$  if, in fact,  $\omega_n < \infty$  for all n. Mahler characterizes the set of all complex numbers as follows:

A-number 
$$\omega = 0, \quad \nu = \infty,$$
  
S-number  $0 < \omega < \infty, \nu = \infty,$   
T-number  $\omega = \infty, \nu = \infty,$   
U-number  $\omega = \infty, \nu < \infty.$ 

We shall prove in § 2 that the A-numbers are just the algebraic numbers; thus a transcendental number  $\xi$  is an S-number if  $\omega(n,h)$  is uniformly bounded for all n, h, a U-number if, for some n,  $\omega(n,h)$  is unbounded, and a T-number otherwise. Further we have:

```
† J.M. 166 (1932), 118-36.

‡ Bibliography.

§ Giorn. Mat. Battaglini, 52 (1914), 305-65.

|| Mat. Sbornik, 41 (1934), 221-32.
```

**Theorem 8.1.** Algebraically dependent numbers belong to the same class.

## Theorem 8.2. Almost all numbers are S-numbers.

Here 'almost all' is interpreted in the sense of Lebesgue measure theory, the linear and planar measures being taken for the real and complex numbers respectively.

The integer  $\nu$  defined above is called the degree of  $\xi$ . It is clear that the Liouville numbers, mentioned in Chapter 1, are U-numbers of degree 1, and LeVeque<sup>†</sup> proved in 1953 the existence of U-numbers of each degree; we shall establish the latter in § 6. For many years it was an open question whether any T-numbers existed but, in 1968, an affirmative answer was obtained by Schmidt; on the basis of Wirsing's early version of Theorem 7.2, and this will be the theme of § 7. It is customary to subclassify the S-numbers according to 'type', defined as the supremum of the sequence  $\omega_1, \omega_2, \ldots$  We shall show in §2 that, for any transcendental  $\xi$ ,  $\omega_n$  is at least 1 or  $\frac{1}{2}(1-1/n)$  according as  $\xi$  is real or complex, whence the type of  $\xi$  is respectively at least 1 or  $\frac{1}{2}$ . In 1965, Sprindžuk, confirming a conjecture of Mahler, proved that almost all real and complex numbers are S-numbers of type 1 and  $\frac{1}{2}$ respectively. Moreover it was recently demonstrated by a refinement of this result that there exist S-numbers of arbitrarily large type. Thus, apart from a small gap in the kind of T-numbers that have so far been exhibited, the transcendental spectrum is, in a sense, complete. The latter measure-theoretical propositions will be the topic of the next chapter.

In the light of Theorem 8.2, one would expect any naturally defined number such as e,  $\pi$ ,  $e^{\pi}$  and  $\log \alpha$  for algebraic  $\alpha$  not 0 or 1 to be an S-number. In 1929, Popken proved that indeed e is an S-number of type 1, and we shall confirm the result in Chapter 10. Theorem 3.1 shows that  $\pi$ , and in fact any non-vanishing linear combination of logarithms of algebraic numbers with algebraic coefficients, is either an S- or a T-number, but the latter possibility has not, as yet, been excluded. From the case n = 1 of Theorem 7.1 one sees, for instance, that  $\sum_{n=1}^{\infty} a^{-b^n}$  is transcendental for any integers  $a \ge 2$ ,  $b \ge 3$ , and, in the same context, Mahler proved in 1937 that also the decimal  $\cdot 1234 \ldots$ 

<sup>†</sup> J. London Math. Soc. 28 (1953), 220-9.

<sup>‡</sup> Symposia Math. IV (Academic Press, 1970), pp. 3-26.

<sup>§</sup> N.A.W. 40 (1937), 421-8.

where the natural numbers are written in ascending order, is transcendental; and here again it has been proved that these are either S-or T-numbers. For  $e^{\pi}$ , however, the possibility that it is a Liouville number has not even been excluded at present. Note that, by virtue of Theorem 8.1, the above results enable one to furnish many examples of algebraically independent numbers; indeed if  $\xi$  is any U-number, such as for instance  $\Sigma 10^{-n\,1}$ , and if  $\eta$  is, say, e or  $\pi$  or  $\Sigma 10^{-10^n}$  or Mahler's decimal, then certainly  $\xi$ ,  $\eta$  are algebraically independent.

In 1939, Koksma introduced a classification closely analogous to that of Mahler, which has also proved illuminating. Let  $\xi$  be any complex number and for each pair of positive integers n, h, let  $\alpha$  be an algebraic number with degree at most n and height at most h such that  $|\xi - \alpha|$  takes the smallest positive value; and define  $\omega^*(n, h)$  by the equation  $|\xi - \alpha| = h^{-n\omega^*(n, h)-1}.$ 

Koksma classified the complex numbers as  $A^{*-}$ ,  $S^{*-}$ ,  $T^{*-}$  or  $U^{*-}$  numbers in the same way as Mahler, but with  $\omega^{*}$  in place of  $\omega$ . Thus a transcendental number  $\xi$  is an  $S^{*-}$ -number if  $\omega^{*}(n,h)$  is uniformly bounded, a  $U^{*-}$ -number if, for some n,  $\omega^{*}(n,h)$  is unbounded, and a  $T^{*-}$ -number otherwise. There is an exact correspondence between the two classifications, the  $S^{*-}$ ,  $T^{*-}$  and  $U^{*-}$ -classes being in fact identical with the  $S^{-}$ ,  $T^{-}$  and  $U^{-}$ -classes respectively; moreover, the functions  $\omega_{n}$  and  $\omega_{n}^{*}$  take comparable values. Indeed it is easily verified that  $\omega_{n}^{*} \leq \omega_{n}$ , and simple lower bounds for  $\omega_{n}^{*}$  in terms of  $\omega_{n}$  were obtained by Wirsing. These imply, in particular, that  $\omega_{n}^{*} = 1$  when  $\omega_{n} = 1$ , whence, in view of Sprindžuk's theorem, we have  $\omega_{n}^{*} = 1$  for almost all real  $\xi$ . But it remains an open question whether  $\omega_{n}^{*} \geqslant 1$  for all real  $\xi$ .

## 2. A-numbers

We prove here that the A-numbers are just the algebraic numbers. Suppose first that  $\xi$  is a real transcendental number. We consider the set of all numbers  $Q(\xi)$ , where Q denotes a polynomial, not identically 0, with degree at most n and with integer coefficients between 0 and n inclusive. The set evidently contains  $(n+1)^{n+1}-1$  elements each with absolute value at most n for some n0. If now we divide the interval n1 into n2 into n3 into n3 disjoint subintervals each of length n3 then there will be two distinct numbers n3 and n3 in the same

<sup>†</sup> Acta Math. 111 (1964), 97-120.

<sup>1</sup> For references and further discussion see Schneider (Bibliography).

<sup>§</sup> J.M. 206 (1961), 67-77.

subinterval. Thus the polynomial  $P = Q_1 - Q_2$  satisfies  $|P(\xi)| < 2ch^{-n}$  and so  $\omega_n \ge 1$ . Similarly, if  $\xi$  is complex, we divide the intervals [-ch, ch] on the real and imaginary axes into at most  $h^{\frac{1}{2}(n+1)}$  disjoint subintervals each of length at most  $c'h^{-\frac{1}{2}(n-1)}$  for some  $c' = c'(n, \xi)$ , and there will be two distinct numbers  $Q_1(\xi)$  and  $Q_2(\xi)$  with real and imaginary parts in the same subintervals. Thus we have

$$\omega_n \geqslant \frac{1}{2}(1-1/n).$$

Now if  $\xi$  is algebraic with degree m, then for any polynomial P as above,  $P(\xi)$  is an algebraic number with degree at most m and height at most ch for some  $c = c(n, \xi)$ . Hence either  $P(\xi) = 0$  or  $|P(\xi)| > c'h^{-m}$  for some  $c' = c'(n, \xi) > 0$ . It follows that  $n\omega(n, h)$  is uniformly bounded for all n, h, and this proves the assertion.

## 3. Algebraic dependence

Our purpose here is to prove Theorem 8.1. Suppose that  $\xi$ ,  $\eta$  are algebraically dependent. Then they satisfy an equation  $Q(\xi,\eta)=0$ , where Q(x,y) is a polynomial with, say, degree k in x, l in y, and with algebraic coefficients, not all 0. Without loss of generality we can suppose that  $\xi$ ,  $\eta$  are transcendental, for otherwise they would both be algebraic and so belong to the same class; also we can suppose that the coefficients of Q are rational integers, for this can evidently be ensured by taking, in place of Q, a product of its conjugates. Moreover we can suppose that all the zeros  $\xi_1 = \xi$ ,  $\xi_2, \ldots, \xi_k$  of  $Q(x, \eta)$  are transcendental; for if one of these were algebraic then its minimal defining polynomial, say p(x), would divide all the coefficients of Q(x,y) regarded as a polynomial in y, and it would therefore suffice to consider Q(x,y)/p(x) in place of Q(x,y).

Let now P and  $\omega(n, h)$  be defined as at the beginning of § 1 and put

$$J=P(\xi_1)\dots P(\xi_k).$$

Clearly we have

$$|J| \leqslant c_1 h^{-n\omega(n, h)+k-1},$$

where  $c_1$ , like  $c_2$ ,  $c_3$  below, depends only on  $\xi$ ,  $\eta$ , n and Q. Further, J is symmetric in  $\xi_1, \ldots, \xi_k$  and so, by the fundamental theorem on symmetric functions, it can be expressed as a polynomial in the elementary symmetric functions with total degree at most n and with height at most  $c_2h^k$ . Now each elementary symmetric function is given by  $\pm q_i/q_0$ , where

$$Q(x, \eta) = q_0(\eta) x^k + q_1(\eta) x^{k-1} + \ldots + q_k(\eta).$$

Hence  $q_0^n J$  is a polynomial in  $\eta$  with degree at most ln and height at most  $h' = c_3 h^k$ . If therefore  $\omega'(n, h')$ ,  $\omega'_n$  and  $\omega'$  are defined for  $\eta$  in the same way as  $\omega(n, h)$ ,  $\omega_n$  and  $\omega$  were defined for  $\xi$ , we have

$$h'^{ln\omega'(ln,h')} \geqslant c_1 h^{n\omega(n,h)-k+1}$$
.

This gives  $kln\omega'_{ln} \ge n\omega_n - k + 1$ , whence  $kl\omega' \ge \omega$ . Similarly, on interchanging  $\xi$  and  $\eta$  we obtain  $kl\omega \ge \omega'$  and Theorem 8.1 follows.

## 4. Heights of polynomials

We establish now two lemmas which will be employed in the proof of Theorem 8.2 and in the next chapter. The propositions will be proved for polynomials with arbitrary complex coefficients, and here no restriction will attach to the definition of the height. P(x) will denote a polynomial with degree n and height h, and constants implied by  $\leq$  or > will depend only on n.

**Lemma 1.** For some integer j with  $0 \le j \le n$  we have

$$h \leqslant |P(j)| \leqslant h.$$

**Proof.** It is readily verified that

$$P(x) = \sum_{j=0}^{n} \frac{P(j) A(x)}{A'(j) (x-j)},$$

where  $A(x) = x(x-1) \dots (x-n)$ , and A' denotes the derivative of A. Now we have  $|A'(j)| \ge 1$ , and clearly also the coefficients in the polynomials A(x)/(x-j) are  $\le 1$ . Thus we see that  $|P(j)| \ge h$  for some j, and obviously we have  $|P(j)| \le h$  for all j. This proves the lemma.

**Lemma 2.** If  $P = P_1 P_2 \dots P_k$ , where  $P_i$  is a polynomial with height  $h_i$ , then  $h_1 h_2 \dots h_k \leqslant h \leqslant h_1 h_2 \dots h_k.$ 

**Proof.** The right-hand estimate follows at once from the observation that every coefficient in P can be expressed as a sum of  $\leq 1$  terms each given by a product of k coefficients, one from each of the  $P_i$ .

To establish the left-hand estimate, we begin by choosing an integer j to satisfy Lemma 1, and we denote by  $H_i$  the height of the polynomial  $P_i(x+j)$ . It is clear, on expressing  $P_i(x)$  as a polynomial in x-j, that  $h_i \leq H_i$ . Now if  $\eta$  is any zero of P(x+j), we deduce from the mean value theorem

 $h \ll |P(j)| = |P(\eta+j) - P(j)| = |\eta| |P'(\xi+j)|$ 

for some  $\xi$  with  $|\xi| \leq |\eta|$ . Hence if  $|\eta| < 1$ , we have  $h \leq |\eta| h$ , that is  $|\eta| \gg 1$ . But the zeros of  $P_i(x+j)$  are included in those of P(x+j), and each coefficient in  $P_i(x+j)$  can be written as the product of the constant coefficient  $P_i(j)$  together with an elementary symmetric function in the reciprocals of the zeros. Thus we obtain  $|P_i(j)| \gg H_i$ , and the lemma follows since  $P(j) = P_1(j) \dots P_k(j)$ .

#### 5. S-numbers

We proceed now to prove Theorem 8.2 for complex numbers in terms of planar Lebesgue measure; the argument for real numbers is similar. Again we shall speak of the height only for polynomials with integer coefficients.

We note first that if  $\xi$  is any complex number and P is any irreducible polynomial with degree at most n and height at most h, then the nearest zero  $\alpha$  of P to  $\xi$  satisfies

$$|\xi - \alpha| \le 2^n |P(\xi)| |P'(\alpha)|^{-1}$$
;

for if  $\alpha'$  is any other zero of P we have

$$|\alpha - \alpha'| \leq |\xi - \alpha| + |\xi - \alpha'| \leq 2|\xi - \alpha'|$$

Further we observe that  $|P'(\alpha)| \gg h^{-n}$ ; for if p denotes the leading coefficient of P and if  $\alpha_1, \ldots, \alpha_m$  are any distinct conjugates of  $\alpha$  then, on applying Lemma 2 with  $P_i$  given by  $x-\alpha_i$ , one sees that the algebraic integer  $p\alpha_1 \ldots \alpha_m$  is  $\ll h$ , whence the norm of  $P'(\alpha)$  multiplied by  $p^{n-1}$  is  $\ll h^n |P'(\alpha)|$ . If now  $\xi$  is a T- or U-number then, by Lemma 2, there exist, for some n, infinitely many polynomials P as above such that  $|P(\xi)| < h^{-4n}$ , and so the nearest zero  $\alpha$  of P to  $\xi$  satisfies  $|\xi-\alpha| \ll h^{-3n}$ . Hence every T- and U-number belongs to the elements of infinitely many sets S(n,h) for some n, where S(n,h) consists of all discs centred on the algebraic numbers with degree at most n and height at most n, and with radius  $n^{-2n}$ . But there are n0 definitely many sets of all n1 due to n2. Since n3 since n4 due to n4 and thus their total area is n5. Since n6 since n6 due to n6 and n7 and n8 due to n8 and n9 and thus their total area is n9. Since n9 are a sequired.

## 6. U-numbers

We establish here the existence of *U*-numbers of each degree. In fact we shall show that, for any positive integer n,  $\zeta^{1/n}$  is a *U*-number of degree n, where  $\zeta = \frac{1}{3} + \sum_{m=1}^{\infty} 10^{-m!}$ . Indeed we shall prove, more

† It is well known that this is an algebraic integer; see e.g. Hecke (Bibliography).

generally, that  $\xi$  is a *U*-number of degree n if there exists a sequence  $\alpha_1, \alpha_2, \ldots$  of distinct algebraic numbers, with degree n, satisfying

$$|\xi - \alpha_j| < h_j^{-\omega_j}, \tag{1}$$

where  $h_j$  denotes the height of  $\alpha_j$  and  $\omega_j \to \infty$  as  $j \to \infty$ , provided that, for some  $r \ge 1$ , we have  $h_i < h_{i+1} < h_i^{r\omega_j}$ (2)

for all sufficiently large j. Clearly  $\xi = \zeta^{1/n}$  satisfies (1) and (2) with  $\alpha_i = (p_i/q_i)^{1/n}$ , where

$$p_j = 10^{j!} \left( 1 + 3 \sum_{m=1}^{j} 10^{-m!} \right), \quad q_j = 3.10^{j!},$$

and with  $\omega_j = j$ , r = 2; also  $\alpha_j$  has exact degree n since  $q_j$  is not a perfect power.

It suffices to show that if (1) and (2) hold then there are only finitely many algebraic numbers  $\beta$  with degree at most n-1 satisfying

$$|\xi - \beta| < b^{-(2n)^{4r}},\tag{3}$$

where b denotes the height of  $\beta$ . For then n is the least positive integer for which there exist sequences  $\alpha_1, \alpha_2, \ldots$  and  $\omega_1, \omega_2, \ldots$  as above satisfying (1), whence  $\xi$  is a  $U^*$ -number of degree n and so also a U-number of the same degree. To verify this connexion between U- and  $U^*$ -numbers, note that if  $P_j(x)$  is the minimal defining polynomial of  $\alpha_j$  then (1) gives, for all sufficiently large j,

$$\left|P_j(\xi)\right| \ll h_j^{-\omega_j+n} \leqslant h_j^{-\frac{1}{2}\omega_j},$$

where the implied constant depends only on  $\xi$  and n, and, conversely, if there were a sequence of polynomials  $P_j(x)$  (j = 1, 2, ...) with degree at most n-1 and height at most  $h_j$  such that  $|P_j(\xi)| < h_j^{-\omega_j}$  then the nearest zero  $\alpha_j$  of  $P_j$  to  $\xi$  would satisfy (1) with  $\omega_j$  replaced by  $\omega_j/n$ .

Now suppose that  $\beta$  is an algebraic number with degree at most n-1 such that (3) holds, and let j be the integer which, for b sufficiently large, satisfies  $h_i < b^{4n^2r} < h_{i+1}; \tag{4}$ 

in the sequel we shall write briefly  $\alpha$ , h,  $\omega$  for  $\alpha_j$ ,  $h_j$ ,  $\omega_j$ . From (1) and (3) we have  $|\alpha - \beta| \leq |\xi - \alpha| + |\xi - \beta| < h^{-\omega} + b^{-(2n)^4 r}$ ,

and, from (2) and (4), the terms on the right are at most  $(bh)^{-2n^2}$ , provided that  $\omega > 4n^2$ . On the other hand,  $\alpha - \beta$  is a non-zero algebraic number with degree at most  $n^2$ , and each conjugate has absolute value  $\leqslant bh$ , where the implied constant depends only on n; further, the

same estimate obtains for the leading coefficient in the minimal defining polynomial. Hence

$$|\alpha - \beta| \gg (bh)^{-n^2},$$

and thus we have a contradiction if b is sufficiently large; the contradiction establishes the result.

We remark finally that the inequality  $|\alpha - \beta| \gg (ab)^{-n^2}$  implicit in the above argument, where  $\alpha$ ,  $\beta$  denote distinct algebraic numbers with degrees at most n and heights a, b respectively, and the implied constant depends only on n, can be much improved. Indeed, by considering the norm of  $\alpha - \beta$  and using the result employed in § 5 on products of conjugates of algebraic numbers, one easily obtains  $|\alpha - \beta| \gg a^{-l}b^{-m}$ , where l, m denote the degrees of the fields generated by  $\beta$  over  $Q(\alpha)$  and  $\alpha$  over  $Q(\beta)$  respectively. A special case of the latter inequality was discovered by A. Brauer† in 1929, but, curiously, the full result was recorded only relatively recently.‡

## 7. T-numbers

These exist, as we now show. To begin with, let  $\alpha_1, \alpha_2, \ldots$  be any non-zero algebraic numbers and let  $\nu_1, \nu_2, \ldots$  be any real numbers exceeding 1. We shall prove that there exists a sequence  $\gamma_1, \gamma_2, \ldots$  of non-zero numbers with  $\gamma_j/\alpha_j$  rational such that, if  $h_j$  denotes the height of  $\gamma_j$ , then  $H_{j+1} > 2H_j$ , where  $H_j = h_j^{\nu_j}$ , and furthermore,  $\gamma_{j+1}$  lies in the interval  $I_j$  consisting of all real x with

$$\tfrac{1}{4}H_{j}^{-1} < x - \gamma_{j} < \tfrac{1}{2}H_{j}^{-1};$$

in addition, we shall show that the sequence can be chosen so that, for some numbers  $\lambda_1, \lambda_2, \dots$  between 0 and 1 exclusive, we have

$$|\gamma_j - \beta| > B^{-1}$$

for all algebraic numbers  $\beta$  with degree  $n \leq j$  distinct from  $\gamma_1, \ldots, \gamma_j$ , where  $B = \lambda_n^{-1} b^{(3n)^4}$  and b denotes the height of  $\beta$ . Clearly then,  $\gamma_1, \gamma_2, \ldots$  tends to a limit  $\xi$  which satisfies  $|\xi - \beta| \geq B^{-1}$  for all algebraic numbers  $\beta$  distinct from  $\gamma_1, \gamma_2, \ldots$ , and also

$$\tfrac14 H_i^{-1} \leqslant \xi - \gamma_i \leqslant H_i^{-1}$$

for all j. We now take  $\nu_j = (3n_j)^4$ , where  $n_j$  denotes the degree of  $\alpha_j$ ,

<sup>†</sup> J.M. 160 (1929), 70-99.

<sup>‡</sup> For references and further work in this context see Michigan Math. J. 8 (1961), 149-59 (R. Güting).

and we select  $\alpha_1, \alpha_2, \ldots$  so that the equation  $n_j = n$  has infinitely many solutions for each positive integer n. Then  $\xi$  is a  $T^*$ -number and hence, by observations similar to those recorded in § 6, also a T-number.

We shall in fact construct  $\gamma_1, \gamma_2, \ldots$  so that four further conditions are satisfied. Let  $J_j$  be the set of all x in  $I_j$  such that  $|x-\beta| > 2B^{-1}$  for all algebraic numbers  $\beta$  with degree  $n \leq j$  which are distinct from  $\gamma_1, \ldots, \gamma_j$  and satisfy  $B > H_j$ . Then we shall ensure that (i)  $\gamma_j$  is in  $J_{j-1}$ , (ii) the measures of  $I_j$  and  $J_j$  satisfy  $|J_j| > \frac{1}{2} |I_j|$ , (iii) we have  $|\gamma_j - \beta| > 2B^{-1}$  for all  $\beta \neq \gamma_j$  with degree j, (iv) if  $\gamma_j/\alpha_j = p_j/q_j$  as a fraction in its lowest terms, with  $q_j > 0$ , then  $|\gamma_j - \beta| > q_j^{-1}$  for all  $\beta$  with degree  $n \leq j$  and with  $b^{3n} \leq q_j$ .

To define  $\gamma_1$ , we note first that, for every large prime  $q_1$ , there are  $\geqslant q_1$  numbers  $\gamma$  of the form  $(p_1/q_1)\alpha_1$  in the interval (1,2), where the implied constant depends only on  $\alpha_1$ , and these have mutual distances  $\geqslant q_1^{-1}$ . Further, there are  $\leqslant q_1^{-1}$  rationals  $\beta$  with  $b^3 \leqslant q_1$  and so there are  $\leqslant q_1^{-1}$  numbers  $\gamma$  satisfying  $|\gamma - \beta| \leqslant q_1^{-1}$  for at least one such  $\beta$ . We can therefore select  $\gamma_1$  so that (iv) holds, and then, by Theorem 7.2, we can choose  $\lambda_1$  so that the conditions concerning  $|\gamma_1 - \beta|$  are satisfied. We shall show in a moment that also (ii) holds in the case j = 1 if  $q_1 \geqslant 1$ .

Now suppose that  $\gamma_1, \ldots, \gamma_{j-1}$  have already been defined to satisfy the above conditions; we proceed to construct  $\gamma_j$ . Constants implied by  $\leqslant$  or  $\geqslant$  will depend only on the numbers so far specified, including possibly  $\lambda_1, \ldots, \lambda_{j-1}$ . First let  $J'_{j-1}$  be defined like  $J_{j-1}$  but with the additional restriction that the heights of the  $\beta$  in question satisfy  $b^{3n} \leqslant q_j$ . Clearly the number of  $\beta$  for which the latter inequality holds is  $\leqslant q_j^{\frac{n}{2}}$  and so  $J'_{j-1}$  consists of  $\leqslant q_j^{\frac{n}{2}}$  intervals. Further,  $J'_{j-1}$  includes  $J_{j-1}$  and so, by (ii), we have  $|J'_{j-1}| \geqslant \frac{1}{2} |I_{j-1}| \geqslant 1$ . It follows that, for any large prime  $q_j$ , there are  $\geqslant q_j$  numbers  $\gamma$  in  $J'_{j-1}$  of the form  $(p_j/q_j)\alpha_j$ , where  $p_j$  is an integer  $\leqslant q_j$  with  $(p_j,q_j)=1$ . Furthermore, any such  $\gamma$  is in fact in  $J_{j-1}$ , for if the height of  $\beta$  satisfies  $b^{3n}>q_j$  then  $B>q_j^{(3n)^2}$  and thus, on noting that  $(q_j/p_j)\beta$  has height  $\leqslant q_j^{n}b$ , we obtain from Theorem 7.2

$$|\gamma - \beta| \gg q_i^{-1} (q_i^n b)^{-3n} > 2B^{-1}.$$

Now, as above, there are  $\leqslant q_j^{\frac{1}{2}}$  numbers  $\beta$  satisfying the hypotheses of (iv) and hence one can select  $\gamma = \gamma_j$  in  $J_{j-1}$  so that this condition is valid. Then clearly we have  $|\gamma_j - \beta| > B^{-1}$  for all  $\beta$  distinct from  $\gamma_1, \ldots, \gamma_{j-1}$  with degree n < j and with  $B > H_{j-1}$ ; and indeed this holds also for  $B \leqslant H_{j-1}$ , for then, taking k as the least suffix  $\geqslant n$  for which  $B \leqslant H_k$  and appealing to (i) or (iii) with j = k according as k > n or

k = n, we obtain

$$|\gamma_i - \beta| \ge |\gamma_k - \beta| - |\gamma_i - \gamma_k| > 2B^{-1} - H_k^{-1} \ge B^{-1}$$
.

We now use Theorem 7.2 and choose  $\lambda_j$  so that  $|\gamma_j - \beta| > 2B^{-1}$  for all algebraic numbers  $\beta \neq \gamma_j$  with degree n = j.

It remains only to show, as in the case j=1, that (ii) will be satisfied if  $q_j$  is sufficiently large. Now we have  $|x-\beta|>2B^{-1}$  for all x in  $I_j$  and all  $\beta\neq\gamma_j$  with degree  $n\leqslant j$  and with  $H_j< B\leqslant H_j^3$ . For if  $b^{3n}\leqslant q_j$  then, since  $H_j\geqslant q_j^{n_j}$  and  $\nu_j>1$ , it follows from (iv) that

$$|x-\beta| \geqslant |\gamma_i - \beta| - |\gamma_i - x| \geqslant q_i^{-1} - H_i^{-1} \geqslant 2H_i^{-1} > 2B^{-1},$$

and if  $b^{3n} > q_j$  then, on appealing again to Theorem 7.2, we obtain

$$|x-\beta|\geqslant q_{j}^{-4n^{3}}b^{-3n}-H_{j}^{-1}\geqslant B^{-\frac{1}{6}}-B^{-\frac{1}{6}}>2B^{-1}.$$

Hence any x in the complement of  $J_j$  in  $I_j$  satisfies  $|x-\beta| \leq 2B^{-1}$  for some  $\beta$  with degree  $n \leq j$  and with  $B > H_j^3$ . But the number of  $\beta$  with degree n and height b is  $\leq b^n$ , and so the complement has measure  $\leq \Sigma B^{-1}b^n$ , where the sum is over all n, b with  $n \leq j$  and  $B > H_j^3$ . This is plainly  $\leq H_j^{-2} < \frac{1}{8}H_j^{-1}$ , and the required result follows.

It will be seen that the above argument allows one to construct a T-number with  $\omega_n$  taking any value  $\geq (3n)^4$ . This can easily be reduced to a bound of order  $n^2$ , but at present, apparently, not readily to one of order n as would be needed to fill the spectrum.

## METRICAL THEORY

#### 1. Introduction

As remarked previously, Mahler conjectured in 1932 that almost all real numbers are S-numbers of type 1 and almost all complex numbers are S-numbers of type  $\frac{1}{2}$ . He originally proved that, certainly, they are both of type at most 4, and 4 was reduced to 3 and  $\frac{5}{2}$  in the real and complex cases respectively by Koksma in 1939. LeVeque improved these in 1953 to 2 and  $\frac{5}{3}$ , and Volkmann further reduced them in 1964 to  $\frac{4}{3}$  and  $\frac{2}{3}$ . Moreover, proofs of Mahler's conjecture in the special cases with n=2 and n=3 were given by Kubilyus, Kasch and Volkmann. Finally, in 1965, Sprindžuk<sup>‡</sup> obtained a complete proof of Mahler's conjecture for all n, and indeed with the best possible value of  $\omega_n$ .

We shall establish here a refinement of Sprindžuk's result which was derived by the author in 1966. Denoting by  $\psi(h)$  a positive monotonic decreasing function of the integer variable h>0 such that  $\Sigma\psi(h)$  converges, we prove:

**Theorem 9.1.** For almost all real  $\theta$  and any positive integer n there exist only finitely many polynomials P with degree n and integer coefficients such that  $|P(\theta)| < (\psi(h))^n$ , where h denotes the height of P.

A similar result holds for almost all complex numbers  $\theta$  with the exponent n replaced by  $\frac{1}{2}(n-1)$ . It is clear from, for instance, Minkowski's linear forms theorem, that the assertion would not remain valid with  $\psi(h) = 1/h$ , and indeed it is easily verified that almost no  $\theta$  would have the properties required in the case n = 1 if  $\Sigma \psi(h)$  were divergent. But it seems likely that the function  $(\psi(h))^n$  can be replaced by  $h^{-n+1}\psi(h)$ , and this conjecture has in fact been established for  $n \leq 3$ .

The theorem has recently been applied to evaluate the Hausdorff dimension of certain sets; in particular, it has been employed to show that, for any  $\lambda \geq 1$  and any positive integer n, the set of all real  $\xi$  such that, for any  $\lambda' < \lambda$ , there exist infinitely many algebraic numbers  $\beta$ 

<sup>†</sup> M.A. 106 (1932), 131-9.

<sup>‡</sup> Bibliography; this contains references to the earlier works.

<sup>§</sup> Proc. Roy. Soc. London, A 292 (1966), 92-104.

with degree at most n satisfying  $|\xi - \beta| < b^{-(n+1)\lambda'}$ , where b denotes the height of  $\beta$ , has dimension  $1/\lambda$ . This generalizes a well-known theorem of Jarník and Besicovitch; and it immediately implies the result mentioned in the last chapter on the existence of S-numbers of arbitrarily large type.

Various avenues for further investigation are suggested by the work here. For instance it would be of interest to obtain results analogous to Theorem 9.1 for polynomials in several variables, and in fact some progress in this connexion, more especially for cubic polynomials in two unknowns, has been made by R. Slesoraitene. In another direction, it follows from Theorem 9.1, by a classical transference principle, that, for any  $\epsilon > 0$  and any positive integer n, there exist, for almost all real  $\theta$ , only finitely many positive integers q such that

$$\max \|q\theta^j\| < q^{-(1/n)-\epsilon} \quad (1 \leqslant j \leqslant n),$$

and this raises the problem of confirming the stronger proposition in which the above inequality is replaced by

$$q^{1+\epsilon}\|q\theta\|\ldots\|q\theta^n\|<1,$$

where the notation is that of Theorem 7.1. The problem seems quite difficult.

## 2. Zeros of polynomials

We record here, for later reference, some simple inequalities concerning the distances between the zeros of polynomials. Let P(x) be a polynomial with degree n and distinct zeros  $\kappa_1, \ldots, \kappa_n$ . We note first that if  $\theta$  is any real number with  $|\theta - \kappa_1| \leq |\theta - \kappa_i|$  for all j then

$$|P(\theta)| \geqslant 2^{-n} |P'(\kappa_1)| |\theta - \kappa_1|, \tag{1}$$

where P' denotes the derivative of P. For clearly  $|\kappa_1 - \kappa_j| \leq 2 |\theta - \kappa_j|$ , and we have  $P'(\kappa_1) = a(\kappa_1 - \kappa_2) \dots (\kappa_1 - \kappa_n),$ 

where a denotes the leading coefficient of P. Similarly we obtain

$$|P(\theta)| |\kappa_1 - \kappa_2| \ge 2^{-n} |P'(\kappa_1)| |\theta - \kappa_1|^2.$$
 (2)

Further we observe that if  $|\theta - \kappa_1| \leq |\kappa_1 - \kappa_j|$  for all  $j \geq 2$  then  $|\theta - \kappa_j| \leq 2|\kappa_1 - \kappa_j|$  and so

$$|P(\theta)| \leq 2^n |P'(\kappa_1)| |\theta - \kappa_1|. \tag{3}$$

<sup>†</sup> Proc. London Math. Soc. 21 (1970), 1-11 (A. Baker and W. M. Schmidt).

See various papers in Litovek. Mat. Sb. since 1969; see also Sprindžuk's address in Actes, Congrès international math. (1970).

Now suppose that P(x), Q(x) are polynomials with integer coefficients and degree  $n \ge 2$ ; let their leading coefficients be a, b and their zeros be  $\kappa_1, \ldots, \kappa_n$  and  $\lambda_1, \ldots, \lambda_n$  respectively, all of which are supposed to be distinct and have absolute values at most K. We shall write, for brevity,

 $p = |a^n(\kappa_1 - \kappa_3) \dots (\kappa_1 - \kappa_n)|,$ 

and we shall denote by q the analogous function of Q. Our purpose is to prove that if  $|\kappa_1 - \kappa_2| \leq |\kappa_1 - \kappa_j|$  for all  $j \geq 2$ , if  $|\kappa_1 - \kappa_2| < p^{-\frac{1}{2}}$ , and if also the analogous inequalities hold for Q, then

$$|\kappa_1 - \lambda_1| \gg \min(p^{-\frac{1}{2}}, q^{-\frac{1}{2}}),$$
 (4)

where the implied constant depends only on n and K.

For the proof, we suppose that (4) does not hold and we shall obtain a contradiction if the implied constant is sufficiently large. First we observe that  $|\kappa_1 - \kappa_j| \gg p^{-\frac{1}{2}}$  for all  $j \geqslant 3$ . This is a consequence of the fact that the discriminant of P, namely

$$a^{2n-2}\prod_{i< j}(\kappa_i-\kappa_j)^2,$$

has absolute value at least 1; for, in view of the inequality  $|\kappa_i - \kappa_j| \le 1$  valid for all i, j, it follows that

$$\left|\left(\kappa_1-\kappa_2\right)(\kappa_2-\kappa_j)\right|\gg p^{-1}\quad (j\geqslant 3),$$

and, by hypothesis, we have

$$|\kappa_2 - \kappa_j| \leq 2 |\kappa_1 - \kappa_j|$$
 and  $|\kappa_1 - \kappa_2| < p^{-\frac{1}{2}}$ .

Hence, from the converse of (4), we obtain  $|\kappa_1 - \kappa_j| \gg |\kappa_1 - \lambda_1|$  and so

$$|\kappa_j - \lambda_1| \leq |\kappa_j - \kappa_1| + |\kappa_1 - \lambda_1| \leq |\kappa_j - \kappa_1|$$

for all  $j \ge 3$ . This gives

$$\left|a^{n-1}P(\lambda_1)\right| \ll p\left|\left(\kappa_1 - \lambda_1\right)\left(\kappa_2 - \lambda_1\right)\right|,\tag{5}$$

