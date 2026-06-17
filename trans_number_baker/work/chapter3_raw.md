Various conditions were obtained in Chapter 2 for the non-vanishing of the linear form

$$\Lambda = \beta_0 + \beta_1 \log \alpha_1 + \ldots + \beta_n \log \alpha_n,$$

where the  $\alpha$ 's and  $\beta$ 's denote algebraic numbers; in particular, it suffices if  $\beta_0 \neq 0$ , or if  $\beta_1, \ldots, \beta_n$  are linearly independent over the rationals, assuming that the  $\alpha$ 's are not 0 or 1. In the present chapter, quantitative extensions of the work will be discussed, giving positive lower bounds for  $|\Lambda|$  in terms of the degrees and heights of the  $\alpha$ 's and  $\beta$ 's; it will be recalled from Chapter 1 that the height of an algebraic number is the maximum of the absolute values of the relatively prime integer coefficients in its minimal defining polynomial. Theorems of this kind were first proved by Morduchai-Boltovskoj<sup>†</sup> in 1923, in the case n=1, and by Gelfond<sup>‡</sup> in 1935, in the case n=2,  $\beta_0=0$ . A lower bound for  $|\Lambda|$ , valid for arbitrary n, was established in 1966, on the basis of the work described in Chapter 2, and a variety of improvements have been obtained subsequently. In particular, when the  $\alpha$ 's and also the degrees of the  $\beta$ 's are regarded as fixed, a result that is essentially best possible has now been derived.

**Theorem 3.1.** Let  $\alpha_1,\ldots,\alpha_n$  be non-zero algebraic numbers with degrees at most d and heights at most A. Further, let  $\beta_0,\ldots,\beta_n$  be algebraic numbers with degrees at most d and heights at most  $B \ (\geqslant 2)$ . Then either  $\Lambda = 0$  or  $|\Lambda| > B^{-C}$ , where C is an effectively computable number depending only on n, d, A and the original determinations of the logarithms.

The estimate for C takes the form  $C'(\log A)^n$ , where  $\kappa$  depends only on n, and C' depends only on n and d. In the case when  $\beta_0 = 0$  and  $\beta_1, \ldots, \beta_n$  are rational integers, it has been shown that in fact the theorem holds with  $C = C'\Omega \log \Omega$ , where  $\Omega = (\log A)^n$ ; and moreover,

<sup>†</sup> C.R. 176 (1923), 724-7.

if it is assumed that the height of  $\alpha_j$  does not exceed  $A_j$  ( $\geqslant 4$ ), then  $\Omega$  can be taken as  $\log A_1 \ldots \log A_n$ . Still stronger results have been obtained in the special case, of considerable importance in applications, when one of the  $\alpha$ 's, say  $\alpha_n$ , has a large height relative to the remainder. Indeed it has been proved that if  $\alpha_1, \ldots, \alpha_{n-1}$  and  $\alpha_n$  have heights at most A' and A ( $\geqslant 4$ ) respectively, then

$$|\Lambda| > (B\log A)^{-C\log A},$$

where C > 0 is effectively computable in terms of A', n and d only.<sup>‡</sup> Further, when  $\beta_0 = 0$  and  $\beta_1, \ldots, \beta_n$  are rational integers, the bracketed factor  $\log A$  has been eliminated to yield

$$|\Lambda| > C^{-\log A \log B},$$

which is clearly best possible with respect to A when B is fixed, and with respect to B when A is fixed. Furthermore, under the additional specialization  $\beta_n = -1$ , it has been shown that

$$|\Lambda| > A^{-C} e^{-\epsilon B}$$

for any  $\epsilon > 0$ , where now C depends only on A', n, d and  $\epsilon$ . As we shall see later, these results have particular value in connexion with the study of Diophantine problems.

It will be noted that, from the case n = 1 of Theorem 3.1, we have

$$|\log \alpha - \beta| > B^{-C}$$

for any algebraic number  $\alpha$ , not 0 or 1, and for all algebraic numbers  $\beta$  with degrees at most d and heights at most B ( $\geqslant 2$ ), where C depends only on d and  $\alpha$ ; more especially we have

$$|\pi - \beta| > B^{-C}$$

for some C depending only on d. Estimates of the latter kind with, in fact, precise values for C were derived long before the general result. Indeed Feldman,  $^{\P}$  extending work of Mahler,  $^{\dagger\dagger}$  obtained the first of these inequalities with C of order  $(d \log d)^2$ , assuming that B is sufficiently large, and the second with C of order  $d \log d$ . Moreover, when  $\beta$  is rational, some striking inequalities of the type

$$|\pi-p/q|>q^{-42},$$

<sup>†</sup> Acta Arith. 27 (1974), 247-52.

<sup>‡</sup> Diophantine approximation and its applications (Academic Press, 1973) pp. 1-23.

<sup>§</sup> Acta Arith. 21 (1972), 117-29.

Acta Arith. 24 (1973), 33-6 ¶ I.A.N. 24 (1960), 357-68, 475-92.

<sup>††</sup> J.M. 166 (1932), 118-50.

valid for all rationals p/q  $(q \ge 2)$ , were established by Mahler,<sup>†</sup> and, more recently, by similar methods, values of C arbitrarily close to the conjecturally best possible d+1 were derived in connexion with approximations to the logarithms of certain rational  $\alpha$ .<sup>‡</sup> Several further estimates of this character, classically termed transcendence measures, are furnished by the results cited after Theorem 3.1. They imply, for instance, that, subject to the hypotheses of Theorems 2.3 or 2.4, we have  $|e^{\beta_0}\alpha\beta_1\dots\alpha_n^{\beta_n}-\gamma|>H^{-C\log\log H}$ 

for all algebraic numbers  $\gamma$  with height at most  $H ( \geq 4)$ , where C depends only on the  $\alpha$ 's,  $\beta$ 's and the degree of  $\gamma$ ; in particular

$$|e^{\pi} - p/q| > q^{-c \log \log q}$$

for all rationals p/q  $(q \ge 4)$ , where c denotes an absolute constant, and this is the best measure of irrationality for  $e^{\pi}$  obtained to date.

We shall prove here only Theorem 3.1; the demonstrations of the other results are similar, though the underlying auxiliary functions are modified, the inductive nature of the argument is more complicated, and certain lemmas appertaining to Kummer theory are employed in the latter part of the exposition in place of the determinant that occurs here. The reader is referred to the original memoirs for details. Applications of the results to various branches of number theory will be discussed in subsequent chapters.

#### 2. Preliminaries

We begin with some observations concerning the heights of algebraic numbers. First we note that if  $\alpha$  is an algebraic number with degree d and height H then  $|\alpha| \leq dH$ ; for if  $\alpha$  satisfies

$$a_0\alpha^d + a_1\alpha^{d-1} + \ldots + a_d = 0,$$

where the  $a_j$  denote rational integers with absolute values at most H and  $a_0 \ge 1$ , then either  $|\alpha| < 1$  or

$$|\alpha| \leqslant |a_0\alpha| = |a_1 + a_2\alpha^{-1} + \ldots + a_d\alpha^{-d+1}| \leqslant dH.$$

Secondly we observe that if  $\alpha$ ,  $\beta$  are algebraic numbers with degrees at most d and heights at most H, then  $\alpha\beta$  and  $\alpha + \beta$  have degrees at most  $d^2$  and heights at most H', where  $\log H'/\log H$  is bounded above by a

<sup>†</sup> Philos. Trans. Roy. Soc. London, A 245 (1953), 371-98; I.M. 15 (1953), 30-42. ‡ Acta Arith. 10 (1964), 315-23.

number depending only on d. For let  $\alpha^{(i)}$ ,  $\beta^{(j)}$  denote the respective conjugates of  $\alpha$  and  $\beta$ . Then  $\alpha\beta$  and  $\alpha + \beta$  are zeros of the polynomials

$$(ab)^{d^2} \prod_{i,j} (x - \alpha^{(i)}\beta^{(j)}), (ab)^{d^2} \prod_{i,j} (x - \alpha^{(i)} - \beta^{(j)})$$

respectively, which clearly have integer coefficients and degrees at most  $d^2$ . The zeros of the minimal polynomials of  $\alpha\beta$  and  $\alpha + \beta$  are thus given by some subsets of the  $\alpha^{(i)}\beta^{(j)}$  and  $\alpha^{(i)}+\beta^{(j)}$ , and the leading coefficients divide  $(ab)^{d^2}$ . The assertion now follows on noting that the  $\alpha^{(i)}$ ,  $\beta^{(j)}$  have absolute values at most dH.

For any integers  $k \ge 1$ ,  $l \ge 0$  we shall signify by  $\nu(l;k)$  the least common multiple of  $l+1, \ldots, l+k$ . Further, for brevity, we shall write

$$\Delta(x; k) = (x+1) \dots (x+k)/k!,$$

and we shall put  $\Delta(x; k, l, m) = \frac{1}{m!} \frac{d^m}{dx^m} (\Delta(x; k))^l$ .

The functions have the following properties:

**Lemma 1.** When x is a positive integer then also  $(\nu(x;k))^m \Delta(x;k,l,m)$  is a positive integer and we have

$$\Delta(x; k, l, m) \leq 4^{l(x+k)}, \quad \nu(x; k) \leq \{c(x+k)/k\}^{2k}$$

for some absolute constant c.

**Proof.** First we observe that

$$\Delta(x; k, l, m) = (\Delta(x; k))^{l} \Sigma \{(x+j_1) \dots (x+j_m)\}^{-1},$$

where the summation is over all selections of m integers  $j_1, \ldots, j_m$  from the set  $1, \ldots, k$  repeated l times, and the right-hand side is read as 0 if m > kl. Clearly  $x+j_r$  divides  $\nu(x;k)$  for each r, and since certainly  $\Delta(x;k)$  is a rational integer, the first part of the proposition follows. Further, we see that

$$\Delta(x; k, l, m) \leqslant {x+k \choose k}^{l} {kl \choose m} \leqslant 2^{l(x+k)+kl},$$

and this gives the required estimate.

To obtain the estimate for  $\nu$ , we write  $\nu(x; k) = \nu' \nu''$ , where all prime factors of  $\nu'$ ,  $\nu''$  are  $\leq k$  and > k respectively. Since the exponent to which a prime p divides  $\nu'$  is at most  $\log (x+k)/\log p$ , we have

$$\log \nu' \leq \Sigma \log (x+k) \leq c' k \log (x+k)/\log k$$

where the summation is over all primes  $p \leq k$ , and c', like c, c'', c''' below, denotes an absolute constant. Now we can assume that k > c'' and that x > c''k for some sufficiently large c'', for otherwise the desired conclusion would follow at once from the simple upper bounds  $(x+k)^k$  and  $c^{x+k}$  for  $\nu(x;k)$ . Thus we see that

$$\nu' \leqslant \{c'''(x+k)/k\}^k.$$

But clearly  $\nu''$  divides  $\Delta(x; k)$ , and this does not exceed  $(x+k)^k/k!$ ; the required estimate is now apparent. The exponent 2 can in fact be reduced easily to 1, which is best possible, but the refinement is not needed here.

We prove next a simple lemma giving a special basis for the space of polynomials with bounded degree.

**Lemma 2.** If P(x) is a polynomial with degree n > 0 and if K is a field containing its coefficients then, for any integer m with  $0 \le m \le n$ , the polynomials  $P(x), P(x+1), \ldots, P(x+m)$  and  $1, x, \ldots, x^{n-m-1}$  are linearly independent over K.

**Proof.** The assertion is readily verified for n = 1. We assume the result for n = n' and we proceed to prove the validity for n = n' + 1. Suppose therefore that  $0 \le m \le n' + 1$ , that P(x) is a polynomial with degree n' + 1 and that

$$R(x) = \lambda_0 P(x) + \lambda_1 P(x+1) + \dots + \lambda_m P(x+m)$$

has degree at most n'-m for some elements  $\lambda_j$  of K. We have

$$R(x) = (\lambda_0 + \ldots + \lambda_m) P(x+m+1) + \sum_{j=0}^m (\lambda_0 + \lambda_1 + \ldots + \lambda_j) Q(x+j),$$

where Q(x) = P(x) - P(x+1). But Q(x) has degree n' and since P(x+m+1) has degree n'+1 we see that  $\lambda_0 + \ldots + \lambda_m = 0$ . It follows from the inductive hypothesis that

$$\lambda_0 + \lambda_1 + \dots + \lambda_i = 0 \quad (0 \le j \le m),$$

and so  $\lambda_0 = \dots = \lambda_m = 0$ , as required.

Finally we establish the non-vanishing of a particular determinant; the result will play a similar rôle to Lemma 7 of Chapter 2.

**Lemma 3.** If  $\omega_0, \ldots, \omega_{l-1}$  are any distinct non-zero complex numbers then the determinant of order kl with  $i^*\omega_s^i$  in the (i+1)-th row and (j+1)-th column, where j=r+sk  $(0 \le r < k, 0 \le s < l)$ , is not zero.

† Here 
$$i^0 = 1$$
 for all  $i$  including  $i = 0$ .

**Proof.** The determinant  $\Omega$  in question can plainly be expressed as a polynomial  $\Omega(\omega_0, ..., \omega_{l-1})$  in the  $\omega$ 's with integer coefficients. We write  $\Omega(z) = \Omega(z, \omega_1, ..., \omega_{l-1}),$ 

and we observe from the Laplace expansion of  $\Omega$ , taking minors formed from the first k columns, that  $\Omega(z)$  is a polynomial in z with degree at most

 $\sum_{i=1}^{k} (kl - j) = k^2 l - \frac{1}{2} k(k+1),$ 

and moreover that it has a factor  $z^{\frac{1}{4}k(k-1)}$ . We shall prove in a moment that it also has a factor  $(z-\omega_s)^{k^2}$  for each s with  $1 \le s < l$ . This gives

$$\Omega(z) = C z^{\frac{1}{2}k(k-1)} \prod_{s=1}^{l-1} (z - \omega_s)^{k^2},$$

where C is the coefficient of the highest power of z in  $\Omega(z)$ . It is easily verified that C is the product of the Vandermonde determinant of order k with typical element  $(k(l-1)+i)^j$ , and the determinant of order k(l-1) formed like  $\Omega$ , that is, with typical element  $i^r\omega_s^i$ , where now  $1 \le s < l$ . The lemma follows by induction.

To prove the above proposition we begin by noting that the mth derivative  $\Omega_m(z)$  of  $\Omega(z)$  is given by

$$\sum (m!/(m_0! \ldots m_{k-1}!))\Omega'(m_0, \ldots, m_{k-1}, z),$$

where the summation is over all non-negative integers  $m_0, \ldots, m_{k-1}$  with sum m, and  $\Omega'(m_0, \ldots, m_{k-1}, z)$  is obtained from  $\Omega(z)$  by replacing the element in the (i+1)th row and (j+1)th column for j < k by

$$i^{r+1}(i-1)\ldots(i-m_r+1)z^{i-m_r}$$
.

It suffices now to prove that if  $m < k^2$  then the 2k polynomials  $1, x, ..., x^{k-1}$  and

$$x^{r+1}(x-1)\dots(x-m_r+1) \quad (0 \le r < k)$$

are linearly dependent; for then some non-trivial linear combination of the 2k columns of  $\Omega'(m_0, ..., m_{k-1}, \omega_s)$ , given by

$$j < k$$
 and  $j = r + (s-1)k$ ,

vanishes and so  $\Omega_m(\omega_s) = 0$ . To establish the linear dependence we arrange the degrees of the polynomials in ascending order, say  $n_1 \leq n_2 \leq \ldots \leq n_{2k}$ , and we observe that their sum is

$$\label{eq:kappa} \tfrac{1}{2}k(k-1) + \sum_{r=0}^{k-1} (r+m_r) = k(k-1) + m < 2k^2 - k.$$

Thus we have  $n_j < j-1$  for some j; this implies that there are j polynomials amongst the original set each with degree at most j-2, and these are certainly linearly dependent. The above argument clearly yields an explicit value for  $\Omega$ , but only the non-vanishing is required here.

## 3. The auxiliary function

We come now to the proof of Theorem 3.1 and we assume accordingly that  $\alpha_1, \ldots, \alpha_n$  are non-zero algebraic numbers with degrees and heights at most d and A respectively. By C, c,  $c_1$ ,  $c_2$ , ... we signify numbers, greater than 1, that depend only on n, d, A and the given determinations of the logarithms of the  $\alpha$ 's. We suppose that  $\beta_0, \ldots, \beta_{n-1}$  are algebraic numbers with degrees and heights at most d and B ( $\geq 2$ ) respectively such that

$$|\beta_0 + \beta_1 \log \alpha_1 + \dots + \beta_{n-1} \log \alpha_{n-1} - \log \alpha_n| < B^{-C}, \tag{1}$$

for some sufficiently large C, and we proceed to show that there exist then rational integers  $b'_1, \ldots, b'_n$ , not all 0, with absolute values at most  $c_1$ , satisfying  $b'_1 \log \alpha_1 + \ldots + b'_n \log \alpha_n = 0$ . (2)

An inductive argument will then complete the proof of the theorem.

The subsequent work rests on the construction of an auxiliary function analogous to that obtained in Lemma 2 of Chapter 2. We signify by k an integer exceeding a sufficiently large number c as above, and we write

$$h = [\log{(kB)}], \quad L_{-1} = h-1, \quad L = L_0 = \dots = L_n = [k^{1-1/(4n)}].$$

We adopt the notation of Chapter 2 with regard to partial derivatives.

**Lemma 4.** There are integers  $p(\lambda_{-1},...,\lambda_n)$ , not all 0, with absolute values at most  $c_2^{hk}$ , such that the function

$$\begin{split} \Phi(z_0, \, \dots, z_{n-1}) &= \sum_{\lambda_{-1} = 0}^{L_{-1}} \dots \sum_{\lambda_n = 0}^{L_n} p(\lambda_{-1}, \, \dots, \lambda_n) \\ &\qquad \times (\Delta(z_0 + \lambda_{-1}; h))^{\lambda_0 + 1} e^{\lambda_n \beta_0 z_0} \alpha_1^{\gamma_1 z_1} \dots \alpha_{n-1}^{\gamma_{n-1} z_{n-1}}, \end{split}$$

where  $\gamma_r = \lambda_r + \lambda_n \beta_r$   $(1 \le r < n)$ , satisfies

$$|\Phi_{m_0, \dots, m_{n-1}}(l, \dots, l)| < B^{-\frac{1}{2}C}$$
 (3)

for all integers l with  $1 \le l \le h$  and all non-negative integers  $m_0, ..., m_{n-1}$  with  $m_0 + ... + m_{n-1} \le k$ .

**Proof.** We determine the  $p(\lambda_{-1}, ..., \lambda_n)$  such that

$$\sum_{\lambda_{-1}=0}^{L_{-1}} \dots \sum_{\lambda_{n}=0}^{L_{n}} p(\lambda_{-1}, \dots, \lambda_{n}) q(\lambda_{-1}, \lambda_{0}, \lambda_{n}, l) \alpha_{1}^{\lambda_{1}l} \dots \alpha_{n}^{\lambda_{n}l} \gamma_{1}^{m_{1}} \dots \gamma_{n-1}^{m_{n-1}} = 0$$
(4)

for the above ranges of l and  $m_0, ..., m_{n-1}$ , where

$$q(\lambda_{-1}, \lambda_0, \lambda_n, z) = \sum_{\mu_0=0}^{m_0} \binom{m_0}{\mu_0} \mu_0! \Delta(z + \lambda_{-1}; h, \lambda_0 + 1, \mu_0) (\lambda_n \beta_0)^{m_0 - \mu_0}.$$

We shall verify subsequently that (4) implies (3). Following the proof of Lemma 2 of Chapter 2, and defining the a's and b's and P' as there, we derive the same equation involving summation over  $s_1, \ldots, s_n, t_0, \ldots, t_{n-1}$  as arises there, but with

$$A(s,t) = \sum_{\lambda_{n}=0}^{L_{-1}} \dots \sum_{\lambda_{n}=0}^{L_{n}} \sum_{\mu_{n}=0}^{m_{n}} \dots \sum_{\mu_{n}=0}^{m_{n-1}} p(\lambda_{-1},\dots,\lambda_{n}) q'q''q''',$$

where now

$$q''' = \binom{m_0}{\mu_0} \mu_0! \, \Delta(l+\lambda_{-1}; \, h, \lambda_0+1, \mu_0) \, \lambda_n^{m_0-\mu_0} b_n^{\mu_0} b_{0, \, t_0}^{(m_0-\mu_0)}$$

and the  $b_{rt}^{(j)}$  have absolute values at most  $(2B)^j$ . Thus we conclude that (4) will be satisfied if the  $d^{2n}$  equations A(s,t)=0 hold. Now these represent  $M \leq d^{2n}h(k+1)^n$  linear equations in the

$$N = (L_{-1} + 1) \dots (L_n + 1)$$

unknowns  $p(\lambda_{-1}, ..., \lambda_n)$ . Further, Lemma 1 shows that, after multiplying by  $(\nu(0; 3h))^{m_0}$ , the coefficients in these equations will be rational integers. Furthermore we have

$$\Delta(l+\lambda_{-1}; h, \lambda_0+1, \mu_0) \leq c_3^{Lh},$$

and, since  $kB \leq e^{h+1}$ , we see that

$$\begin{aligned} |q'| &\leqslant c_4^{Lh}, \quad |q''| \leqslant e^{2h(m_1 + \dots + m_{n-1})}, \\ |q'''| &\leqslant 2^{m_0} (\mu_0 b_n)^{\mu_0} (2B\lambda_n)^{m_0 - \mu_0} c_2^{Lh} \leqslant e^{2hm_0} c_2^{Lh}. \end{aligned}$$

Since also  $\nu(0;3h)\leqslant c_5^h$ , it follows that the coefficients have absolute values at most  $U=c_5^{hk}$ . Now  $N>hk^{n+\frac{1}{2}}>2M$  and hence, by Lemma 1 of Chapter 2, the system of equations A(s,t)=0 can be solved nontrivially and the integers  $p(\lambda_{-1},\ldots,\lambda_n)$  can be chosen to have absolute values at most  $NU\leqslant c_2^{hk}$ .

It remains only to verify that (4) implies (3). Now the left-hand side of (4) is obtained from the number on the left of (3), omitting modulus signs and a factor

$$P = (\log \alpha_1)^{m_1} \dots (\log \alpha_{n-1})^{m_{n-1}},$$

by substituting  $\alpha_n$  for  $\alpha'_n = e^{\beta_0} \alpha_1^{\beta_1} \dots \alpha_{n-1}^{\beta_{n-1}}$ . From (1) we have

$$|\log \alpha_n' - \log \alpha_n| < B^{-C},$$

for some value of the first logarithm and since, for any complex number z,  $|e^z-1| \le |z| e^{|z|}$ , we obtain

$$\left|\alpha_n'-\alpha_n\right| < B^{-\frac{1}{4}C}. \tag{5}$$

Also we have

$$\left|\alpha_n^{\prime\,\lambda_n\,l}-\alpha_n^{\lambda_n\,l}\right|\,\leqslant\,c_7^{L\,l}\left|\alpha_n^{\prime}-\alpha_n\right|,$$

and estimates similar to those employed above show that

$$|P| \leqslant c_8^k, \quad |q(\lambda_{-1}, \lambda_0, \lambda_n, l)| \leqslant c_9^{(L+m_0)h}, \quad |\gamma_r| \leqslant e^{2h}, \quad |\alpha_r^{\lambda_r l}| \leqslant c_{10}^{Lh}.$$

Thus we see that the number on the left of (3) is at most  $Nc_{11}^{hk}B^{-\frac{3}{4}C}$ . But clearly  $N \leq e^{2hn}$  and  $h \leq \log{(kB)}$ , and hence (3) follows if  $C > c_{12}k\log{k}$ .

**Lemma 5.** Let  $m_0, ..., m_{n-1}$  be any non-negative integers with

$$m_0+\ldots+m_{n-1}\leqslant k,$$

and let

$$f(z) = \Phi_{m_0, ..., m_{n-1}}(z, ..., z).$$

Then, for any number z, we have  $|f(z)| \le c_{13}^{hk+L|z|}$ . Further, for any integer l with  $h < l \le hk^{8n}$ , either  $|f(l)| < B^{-\frac{1}{2}C}$  or

$$|f(l)| > c_{14}^{-hk(1+\log(l/h))-Ll}.$$
 (6)

**Proof.** The function f(z) is given by

$$\begin{split} P \sum_{\lambda_{-1}=0}^{L_{-1}} \dots \sum_{\lambda_{n}=0}^{L_{n}} p(\lambda_{-1}, \dots, \lambda_{n}) \, q(\lambda_{-1}, \lambda_{0}, \lambda_{n}, z) \\ & \times e^{\lambda_{n} \beta_{0} z} \alpha_{n-1}^{\gamma_{1} z} \dots \alpha_{n-1}^{\gamma_{n-1} z} \gamma_{1}^{m_{1}} \dots \gamma_{n-1}^{m_{n-1}}, \end{split}$$

where P and  $q(\lambda_{-1}, \lambda_0, \lambda_n, z)$  are defined as in Lemma 4. Now (5) implies that  $|\alpha_n'^z| \leq c_1^{|z|}$  and clearly

$$\left|\alpha_1^{\lambda_1 z} \dots \alpha_{n-1}^{\lambda_{n-1} z}\right| \leqslant c_{16}^{L|s|}.$$

Furthermore, since

$$|z+\lambda_{-1}| \leqslant [|z|]+h,$$

we deduce from Lemma 1 that

$$|\Delta(z+\lambda_{-1}; h, \lambda_0+1, \mu_0)| \leq c_{12}^{L(|z|+h)}$$
.

This gives

$$|q(\lambda_{-1}, \lambda_0, \lambda_n, z)| \leq e^{2hm_0} c_{17}^{L(|z|+h)},$$

and the required estimate now follows easily as in the latter part of the proof of Lemma 4.

To prove the second assertion, we begin by noting that the expression on the left of (4), say Q, is an algebraic number with degree at most  $d^{2n}$ . Further, by estimates similar to those given above, it is readily verified that each conjugate of Q, obtained by substituting arbitrary conjugates for the  $\alpha$ 's and  $\beta$ 's, has absolute value at most  $c_{18}^{hk+Ll}$ . Furthermore, from Lemma 1, we see that on multiplying Q by

$$(\nu(l;2h))^{m_0}P'\leqslant (c_{19}l/h)^{4hm_0}c_{20}^{hk+Ll},$$

one obtains an algebraic integer. Hence we conclude that either Q=0 or  $|Q|\geqslant c_{21}^{-hk-Ll}(l/h)^{-c_{22}hm_0}.$ 

Since  $m_0 \leq k$ , the number on the right of the last inequality exceeds the right-hand side of (6) for some  $c_{14}$ . Further, as above, we deduce easily from (5) that  $P^{-1}f(l)$  differs from Q by at most  $c_{23}^{lk}B^{-\frac{3}{4}C}$ . But if  $l \leq hk^{8n}$  and  $C > k^{8n+2}$ , then this is at most  $\frac{1}{2}|Q|$ , and hence, if  $Q \neq 0$ , we obtain  $|f(l)| > \frac{1}{2}|PQ|$ , which gives (6).

**Lemma 6.** Suppose that  $0 < \epsilon < c^{-1}$  for some sufficiently large c. Then, for any integer J with  $0 \le J < 8n/\epsilon$ , (3) is satisfied for all integers l with  $1 \le l \le hk^{\epsilon J}$  and all non-negative integers  $m_0, \ldots, m_{n-1}$  with  $m_0 + \ldots + m_{n-1} \le k/2^J$ .

**Proof.** The lemma holds for J=0 by Lemma 4. We suppose that K is an integer with  $0 \le K \le (8n/\epsilon) - 1$  and we assume that the lemma has been verified for J=0,1,...,K. We proceed to prove the proposition for J=K+1.

It suffices to show that for any integer l with  $R_K < l \le R_{K+1}$  and any set of non-negative integers  $m_0, \ldots, m_{n-1}$  with  $m_0 + \ldots + m_{n-1} \le S_{K+1}$ , we have  $|f(l)| < B^{-\frac{1}{2}C}$ , where f(z) is defined as in Lemma 5, and

$$R_J = [hk^{eJ}], \quad S_J = [k/2^J] \quad (J = 0, 1, ...).$$

From our inductive hypothesis we deduce, as in Lemma 4 of Chapter 2, that  $|f_m(r)| < n^k B^{-\frac{1}{2}C}$   $(1 \le r \le R_K, 0 \le m \le S_{K+1}).$  (7)

We write, for brevity,

$$F(z) = \{(z-1) \dots (z-R_K)\}^{S+1},$$

where  $S = S_{K+1}$ , and we denote by  $\Gamma$  the circle in the complex plane, described in the positive sense, with centre the origin and radius  $R = R_{K+1} k^{1/(8n)}$ . By Cauchy's residue theorem we have

$$\frac{1}{2\pi i} \int_{\Gamma} \frac{f(z) dz}{(z-l) F(z)} = \frac{f(l)}{F(l)} + \frac{1}{2\pi i} \sum_{r=1}^{R_K} \sum_{m=0}^{S} \frac{f_m(r)}{m!} \int_{\Gamma_r} \frac{(z-r)^m dz}{(z-l) F(z)}, \tag{8}$$

where  $\Gamma_r$  denotes the circle in the complex plane, described in the positive sense, with centre r and radius  $\frac{1}{2}$ ; for the residue of the pole of the integrand on the left at z=r is given by

$$\frac{1}{S!} \frac{d^S}{dz^S} \left\{ \frac{(z-r)^{S+1} f(z)}{(z-l) F(z)} \right\},$$

evaluated at z = r, and the integral over  $\Gamma_r$  on the right is given by

$$\frac{2\pi i}{(S-m)!}\frac{d^{S-m}}{dz^{S-m}}\left\{\frac{(z-r)^{S+1}}{(z-l)\,F(z)}\right\},\,$$

again evaluated at z = r, and (8) now follows by Leibnitz's theorem. Since, for z on  $\Gamma_r$ ,

$$|(z-r)^m/F(z)| \leq \{\frac{1}{8}(R_K-r-1)!(r-2)!\}^{-S-1} \leq 8^{R_KS}(R_K!)^{-S-1},$$

we deduce from (7) that the absolute value of the double sum on the right of (8) is at most

$$R_{\kappa}(S+1) 8^{R_{\kappa}S+1} (R_{\kappa}!)^{-S-1} B^{-\frac{1}{2}C}$$

Further, for  $R_K < l \leqslant R_{K+1}$ , we have

$$|F(l)| = \{(l-1)!/(l-R_K-1)!\}^{S+1} \leqslant (2^{R_{K+1}}R_K!)^{S+1},$$

and, since  $R_{K+1} \leq hk^{8n}$ , we see that if (6) holds then  $|f(l)| > B^{-\frac{1}{2}C}$ , whence the number on the right of (8) exceeds  $\frac{1}{2}|f(l)/F(l)|$ . We proceed to show that the assumption that (6) is valid leads to a contradiction.

Let  $\theta$  and  $\Theta$  denote respectively the upper bound of |f(z)| and the lower bound of |F(z)| with z on  $\Gamma$ . Since 2|z-l| with z on  $\Gamma$  exceeds the the radius of  $\Gamma$ , we obtain from (8)

$$4\theta |F(l)| > \Theta |f(l)|. \tag{9}$$

Now clearly we have  $\Theta \geqslant (\frac{1}{2}R)^{R_{\mathbb{Z}}(S+1)}$  and thus

$$\log \left(\Theta |F(l)|^{-1}\right) \geqslant R_{K}(S+1)\log \left(\frac{1}{2}k^{1/(8n)}\right). \tag{10}$$

Further, from Lemma 5, we see that  $\theta \leq c_{13}^{hk+LR}$  and so, by virtue of (6),

$$\log (\theta |f(l)|^{-1}) \le c_{25} \{ LR + hk \log (R_{K+1}/h) \}. \tag{11}$$

But the number on the right of (10) is at least

$$2^{-K-6}n^{-1}hk^{\epsilon K+1}\log k,$$

and that on the right of (11) is at most

$$c_{25}hk\{\epsilon(K+1)\log k + k^{\epsilon(K+1)-1/(8n)}\}.$$

If  $e^{-1} > c > 2^{2}nc_{25}$  and k is sufficiently large, the estimates are plainly inconsistent. The contradiction implies the validity of (3) and the lemma follows by induction.

**Lemma 7.** For all integers l with  $0 \le l \le hk^{4n}$  we have

$$\sum_{\lambda_{-1}=0}^{L_{-1}} \dots \sum_{\lambda_{n}=0}^{L_{n}} p(\lambda_{-1}, \dots, \lambda_{n}) \left( \Delta(\lambda_{-1} + l/k; h) \right)^{\lambda_{0}+1} \alpha_{1}^{\lambda_{1} l/k} \dots \alpha_{n}^{\lambda_{n} l/k} = 0.$$
(12)

**Proof.** From Lemma 6 we see that (3) holds for all integers l with  $1 \le l \le X$  and all non-negative integers  $m_0, \ldots, m_{n-1}$  with

$$m_0+\ldots+m_{n-1}\leqslant Y,$$

where

$$X = [hk^{7n}], \quad Y = [c_{26}^{-1}k],$$

and  $c_{26} = 2^{8n/\epsilon}$ . It follows as in the proof of Lemma 6 that

$$f(z) = \Phi(z, ..., z)$$

satisfies

$$|f_m(r)| < n^k B^{-\frac{1}{2}C} \quad (1 \le r \le X, \ 0 \le m \le Y).$$
 (13)

Now let l be any integer with  $0 \le l \le hk^{4n}$  and define

$$E(z) = \{(z-1) \dots (z-X)\}^{Y+1},$$

with the proviso that the factor (z-l/k) is excluded if l/k is an integer. Denoting by  $\Gamma$  the circle in the complex plane, described in the positive sense, with centre the origin and radius  $R = Xk^{1/(8n)}$ , we deduce from Cauchy's residue theorem

$$\frac{1}{2\pi i} \int_{\Gamma} \frac{f(z) dz}{(z - l/k) E(z)} = \frac{f(l/k)}{E(l/k)} + \frac{1}{2\pi i} \sum_{r=1}^{X'} \sum_{m=0}^{Y} \frac{f_m(r)}{m!} \int_{\Gamma_r} \frac{(z - r)^m dz}{(z - l/k) E(z)},$$

where the dash signifies that r=l/k, if an integer, is excluded from the summation, and  $\Gamma_r$  denotes the circle in the complex plane, described in the positive sense, with centre r and radius 1/(2k). Since, for z on  $\Gamma_r$ ,

$$\left| (z-r)^m/E(z) \right| \leq \left\{ (8kX)^{-1} (X-r-1)! (r-2)! \right\}^{-Y-1} \leq 8^{3XY} (X!)^{-Y-1},$$

it follows from (13) that the absolute value of the double sum on the right of the above equation is at most

$$X(Y+1) 8^{3XY}(X!)^{-Y-1} B^{-\frac{1}{4}C}$$

Further, by virtue of Lemma 5, we have, for any z on  $\Gamma$ ,  $|f(z)| < c_{13}^{hk+LR}$ , and it is clear that  $|E(z)| \ge (\frac{1}{2}R)^{(X-1)(Y+1)}$ ,

$$|E(l/k)| \leq (2X)^{X(Y+1)} \leq 8^{X(Y+1)}(X!)^{Y+1}.$$

Thus we obtain

$$|f(l/k)| < c_{13}^{hk+LR} (8^{-3}k^{1/(8n)})^{-XY} + B^{-\frac{1}{2}C},$$

and, since  $Lk^{1/(8n)} < k$ , we deduce easily that the number on the right is at most  $e^{-XY}$ .

Now clearly the left-hand side of (12), say Q, is an algebraic number with degree at most  $(dk)^n$ , and each conjugate has absolute value at most  $c_2^{hk^{4n}}$ . Further, it is readily verified that on multiplying Q by

$$(a_1 \dots a_n)^{Ll} k^{2h(L+1)} \leqslant c_{28}^{hk^{4n+1}}$$

one obtains an algebraic integer; for certainly the denominator of either  $k^h/h!$  or  $\Delta(\lambda_{-1}+l/k;h)$ , expressed in lowest terms, is free of a given prime p according as p does or does not divide k. Thus, if  $Q \neq 0$ , we have  $|Q| > c_{29}^{-hk^{4n}}$ . But it is easily seen from (5) that

$$|Q - f(l/k)| < B^{-\frac{1}{2}C},$$

whence  $|f(l/k)| > \frac{1}{2}|Q|$ . The estimate for |Q| given above is plainly inconsistent with the upper bound  $e^{-XY}$  for |f(l/k)| obtained earlier, and thus we conclude that Q = 0, as required.

## 4. Proof of main theorem

First we observe that, by virtue of Lemma 2, the polynomials

$$(\Delta(\lambda_{-1}+x;\,h))^{\lambda_0+1} \quad (0\leqslant \lambda_{-1}\leqslant L_{-1},\,0\leqslant \lambda_0\leqslant L_0)$$

are linearly independent over the rationals. Thus, on writing

$$\sum_{\lambda_{-1}=0}^{L_{-1}} \sum_{\lambda_{0}=0}^{L_{0}} p(\lambda_{-1},...,\lambda_{n}) \left(\Delta(\lambda_{-1}+x;h)\right)^{\lambda_{0}+1} = \sum_{\lambda'=0}^{L'} p'(\lambda',\lambda_{1},...,\lambda_{n}) x^{\lambda'},$$

where L' = h(L+1), we see that one at least of the  $L'' = (L'+1)(L+1)^n$  numbers  $p'(\lambda', \lambda_1, ..., \lambda_n)$  is not 0. Now (12) can be written in the form

$$\sum_{\lambda'=0}^{L'}\sum_{\lambda_1=0}^{L_1}\dots\sum_{\lambda_n=\hat{\gamma}}^{L_n}p'(\lambda',\lambda_1,\dots,\lambda_n)(l/k)^{\lambda'}(\alpha_1^{\lambda_1/k}\dots\alpha_n^{\lambda_n/k})^l=0,$$

and, by Lemma 7, the equation holds in particular for  $0 \le l \le L''$ . It follows that the determinant of order L'', given by the terms involving l only, vanishes. But the determinant is of the kind indicated in Lemma 3, and thus we conclude that

$$\alpha_1^{\lambda_1/k} \dots \alpha_n^{\lambda_n/k} = \alpha_1^{\lambda_1'/k} \dots \alpha_n^{\lambda_n'/k}$$

for some distinct sets Ax,*..*., An and AJ,..., *A'n.* This gives

$$b_1'\log\alpha_1+\ldots+b_n'\log\alpha_n=(2\pi i)jk$$

for some rational integerj, where *b'r* = Ar — A^. Clearly we have|6, | < *2L,* and since *L* < £i-i/(«n> it follows that the number on the left has absolute value less than *2nk.* Hence we conclude that *j —* 0, and so (2) holds, as required.

The proof of the theorem is now completed by induction. Suppose that *ft0,*..., *fin* are given as in the enunciation and that 0 < | A | < *B~2C* for some sufficiently large *C.* Then one at least of *filt..*., /?" is not 0, and we shall assume that in fact /?" 4= 0. By the preliminary observations in §2, we see that (1) holds with /?,• (1 < j < *n)* replaced by /?y = — *ftjlfin* and further that the *fi'j* have degrees at most *d?* and heights at most *B'* < *B°* for some c depending only on *d.* Hence we conclude that (2) holds for some *b [,* ...,6^asindicatedin§3.Nowif6^ 4= Owe have

$$0<\left|\Lambda'\right|< c_1B^{-C},$$

where A' is obtained from A by replacing /?3 with

$$\beta_i'' = b_r' \beta_i - b_i' \beta_r \quad (0 \le j < n),$$

*b'o* being defined as 0. Further, the observations in § 2 show that /?" has degree at most *d2* and height at most *B"* < *B°* for some c = *c(n, d,A).* Furthermore we have *fi"r* = 0. But the theorem is plainly valid for *n* = 0, and if we assume that it holds for fewer than *n* logarithms then the above shows that it will also hold for *n* logarithms. This establishes the result.

It will be noted that the inductive argument would not be needed if log *av ...,* log *an* were linearly independent over the rationals, and moreover Lemma 7 would not be required if <x1(..., *an* were multiplicatively independent.

## DIOPHANTINE EQUATIONS

## 1. Introduction

Diophantine analysis pertains, in general terms, to the study of the solubility of equations in integers. Although researches in this field have their roots in antiquity and a history of the subject amounts, more or less, to a history of mathematics itself, it is only in relatively recent times that there have emerged any general theories, and we shall accordingly begin our discussion in 1900 by referring again to Hilbert's famous list of problems.

The tenth of these asked for a universal algorithm for deciding whether or not a given Diophantine equation, that is, an equation  $f(x_1, ..., x_n) = 0$ , where f denotes a polynomial with integer coefficients, is soluble in integers  $x_1, ..., x_n$ . Though Hilbert posed his question in terms of solubility, there are, of course, many other sorts of information that one might like to have in this connexion; for instance, one might enquire as to whether a particular equation has infinitely many solutions, or one might seek some description of the distribution or size of the solutions. In 1970, Matijasevic, developing work of Davis, Robinson and Putnam, proved that a general algorithm of the type sought by Hilbert does not in fact exist. A more realistic problem arises, however, if one limits the number of variables, and for, in particular, polynomials in two unknowns our knowledge is now quite substantial.

A full account of the early results in this field is furnished by Dickson's celebrated *History of the theory of numbers*; here references are given to a diverse multitude of Diophantine problems that were investigated by a wide variety of ad hoc methods mainly during the last two centuries. The first major advance towards a coherent theory was made by Thue' in 1909 when he proved that the equation F(x,y) = m, where F denotes an irreducible binary form with integer coefficients and degree at least 3, possesses only a finite number of solutions in integers x, y. Thue established the result by way of his

<sup>†</sup> D.A.N. 191 (1970), 279-82.
