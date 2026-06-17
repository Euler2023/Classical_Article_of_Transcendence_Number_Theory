
# **CLASS NUMBERS OF IMAGINARY QUADRATIC FIELDS**

# **1. Introduction**

The foundations of the theory of binary quadratic forms, the forerunner of our modern theory of quadratic fields, were laid by Gauss in his famous *Disquisitionea Arithmeticoe.* Gauss showed, amongst other things, how one could divide the set of all binary quadratic forms into classes such that two forms belong to the same class if and only if there exists an integral unimodular substitution relating them, and he showed also how one could combine the classes into genera so that two forms are in the same genus if and only if they are rationally equivalent. He also raised a number of notorious problems; in particular, in Article 303, he conjectured that there are only finitely many negative discriminants associated with any given class number, and moreover that the tables of discriminants which he had drawn up in the cases of relatively small class numbers were in fact complete. The first part of the conjecture was proved, after earlier work of Hecke, Mordell and Deuring, by Heilbronn\* in 1934, and the techniques were later much developed by Siegel and Brauer to give a general asymptotic class number formula; but the arguments are non-effective and cannot lead to a verification of the class number tables as sought by Gauss. In 1966, two distinct algorithms were discovered for determining all the imaginary quadratic fields with class number 1, which amounts to a confirmation of the simplest case of the second part of the conjecture.

**Theorem 5.1.** *The only imaginary quadratic fields Q{J(-d)) with class number* 1, *where d is a square-free positive integer, are given by d=* 1,2,3,7,11,19,43,67,163.

One of the original methods of proof, and that which we shall adopt here, is based on the work of Chapters 2 and 3 together with an idea of Gelfond and Linnik;\* the other is due to Stark' and is motivated by an earlier paper of Heegner" which related the problem to the study of

**t** *Quart. J. Math. Oxford Ser.* **5 (1934), 150-flO.**

**J** *D.A.N.* **61 (1948), 773-8.**

**<sup>§</sup>** *Michigan Math. J.* **14 (1967), 1-27. ||** *M.Z.* **56 (1952), 227-53.**

elliptic modular functions and the solution of certain Diophantine equations. The former method has recently been extended to resolve the analogous problem for class number 2, and we shall describe the solution in § 5. Neither method, however, would seem to generalize readily to higher class numbers.

Nevertheless, transcendental number theory has led to new results in several associated subjects. For instance, it has been used by Anferteva and Chudakov\* to make effective certain theorems of Linnik on the average of the minimum of the norm function over ideals in a given class, and it has been employed by Schinzel and the author in studies relating to the *'numeri idonei'* of Euler.\* Furthermore, it has been applied to resolve in the negative a well-known problem of Chowla as to whether there exists a rational-valued function /(n), periodic with prime period *p,* such that 2/(n)/ra = 0.' In fact it has provided a description of all such functions/that take algebraic values and are periodic with any modulus *q;* thus, in particular, it has revealed that the numbers *L(l,x)* taken over all nonprincipal characters *%* (modg) are linearly independent over the rationale, provided only that *(q, <j>{q))* = 1, and this plainly generalizes Dirichlet's famous result on the non-vanishing of *L(i,x)-* It would be of interest to know whether the theorem remains valid when

$$(q,\phi(q))>1.$$

Some further results will be mentioned in § 5.

## **2. L-functions**

We record here some preliminary observations on products of Dirichlet's Z-functions.

Let — *d <* 0 and *k >* 0 denote the discriminants of the quadratic fields *Q(J( — d))* and *Q(Jk)* respectively, and suppose that *(k,d)* = 1.

be the usual Kronecker symbols. Then, for any *8 >* 1, we have

$$L(s,\chi)L(s,\chi\chi') = \frac{1}{2}\sum_{f}\sum_{x,y}\chi(f)f^{-s},\tag{1}$$

where x, *y* run through all integers, not both 0, and

$$f = f(x, y) = ax^2 + bxy + cy^2$$

t *Mat. Sb.* 82 (1970), 66-ftd; = 11 (1970), 47-58.

*X Ada Arith.* 18 (1971), 137-14. j *J. Number Tk.* 5 (1973), 224-36.

runs through a complete set of inequivalent quadratic forms with discriminant -d. To verify this assertion, we observe that the left-hand side of (1) is given by

$$\sum_{m=1}^{\infty}\sum_{n=1}^{\infty}\left(\frac{k}{m}\right)\left(\frac{-kd}{n}\right)(mn)^{-s}=\sum_{l=1}^{\infty}\left(\frac{k}{l}\right)l^{-s}\sum_{n|l}\left(\frac{-d}{n}\right),$$

and the last sum is one half the number of representations of l by the forms f.

Now the right-hand side of (1) can be written

$$\sum_{f} \sum_{x=1}^{\infty} \chi(ax^2) (ax^2)^{-s} + \sum_{f} \sum_{y=1}^{\infty} \sum_{x=-\infty}^{\infty} \chi(f) f^{-s}.$$

The first term here is

$$\zeta(2s) \prod_{p|k} (1-p^{-2s}) \sum_{f} \chi(a) a^{-s},$$

and the second term can be expanded as a Fourier series

$$\sum_{f} \sum_{r=-\infty}^{\infty} A_r(s) e^{\pi i r b/(ka)},$$

where

$$A_r(s) = k^{-1} \int_0^k \sum_{v=1}^{\infty} \sum_{x=-\infty}^{\infty} \chi(f) g^{-s} e^{-2\pi i r v/k} dv,$$

and

$$g = g(v) = a(x+vy)^2 + (d/4a)y^2$$

so that f = g(b/2a). On substituting u for v by the equation

$$x+vy=uy(\sqrt{d/2a}),$$

writing x = m + kyn, where  $0 \le m < ky$ , and interchanging the order of integration and summation, as one may by dominated convergence, one obtains

$$\begin{split} A_r(s) &= k^{-1} a^{-s} (\sqrt{d}/2a)^{1-2s} I_r(s) \sum_{y=1}^{\infty} \sigma(y) \, y^{-2s}, \\ I_r(s) &= \int_{-\infty}^{\infty} \frac{e^{-\pi i u r \sqrt{d}/(ka)}}{(u^2+1)^s} \, du \end{split}$$

where

and

$$\sigma(y) = \sum_{m=0}^{ky-1} \chi(f(m,y)) e^{2\pi i r m/(ky)};$$

the integral in fact arises from summation over n of the partial integrals from  $c_n$  to  $c_{n+1}$ , where

$$c_n = 2a(m + kyn)/(y\sqrt{d}).$$

<sup>†</sup> See Landau's Vorlesungen über Zahlentheorie (Leipzig, 1927), Satz 204.

On putting m = j + kl, where  $1 \le j \le k$ , one sees that

$$\sigma(y) = y \sum_{j=1}^{k} \chi(f(j,y)) e^{2\pi i r j/(ky)}$$

if y divides r, and  $\sigma(y) = 0$  otherwise, and this completes the pre-liminary observations.

## 3. Limit formula

All solutions to date of the class number 1 problem depend on an analogue for products of L-functions of the classical Kronecker limit formula. On writing, with the notation of the previous section,

$$A_0 = \lim_{s \to 1} A_0(s), \quad A_r = A_r(1) \quad (r \neq 0),$$

and taking limits as  $s \to 1$ , we obtain

$$L(1,\chi)L(1,\chi\chi') = \frac{\pi^2}{6} \prod_{p|k} \left(1 - \frac{1}{p^2}\right) \sum_{f} \frac{\chi(a)}{a} + \sum_{f} \sum_{r=-\infty}^{\infty} A_r e^{\pi i r b/(ka)}. \quad (2)$$

Our purpose here is to prove that

$$\left|A_r\right|\leqslant \frac{2\pi}{\sqrt{d}}\left|r\right|e^{-\pi|r|\sqrt{d}/(ka)}$$

for  $r \neq 0$ , and

$$A_0 = \frac{-2\pi}{k\sqrt{d}} \chi(a) \log p$$

if k is the power of a prime p,  $A_0 = 0$  otherwise.

To begin with, we observe that, for  $r \neq 0$ ,

$$A_r = (\frac{1}{2}k\sqrt{d})^{-1}I_r(1)\sum_{y}\sum_{j=1}^k y^{-1}\chi(f(j,y))e^{2\pi i r j/(ky)},$$

where y runs through all positive divisors of r. It is easily confirmed that  $L(1) = \pi e^{-\pi |r| \sqrt{d}/(ka)}.$ 

and clearly the sum over y in  $A_r$  has absolute value at most k|r|. The first assertion follows at once. To establish the second assertion, we note that

$$A_0(s) = k^{-1}a^{s-1}(\tfrac{1}{2}\sqrt{d})^{1-2s}I_0(s)\sum_{y=1}^{\infty}y^{1-2s}\sum_{j=1}^k\chi(f(j,y)),$$

and

$$I_0(s) = \sqrt{\pi} \, \Gamma(s - \frac{1}{2}) / \Gamma(s).$$

Further, by well-known estimates for the Gaussian sums, we obtain, for any positive integer *y* and any odd *k,*

$$\sum_{j=1}^{k} \chi(f(j,y)) = \chi(a) \sum_{j=1}^{k} \chi(j^{2}) e^{2\pi i j y/k};$$

we shall be concerned in the sequel only with odd values of *k,* but the equation in fact holds also for even *k,* as has been shown by Stark.\* The sum over *j* on the right can be expressed alternatively as a sum of terms *d/i(kjd)* over all common divisors *d* of *k* and *y\** and hence we see that the sum over *y* in the above expression for *A0(s)* is given by

$$\chi(a) \zeta(2s-1) k^{2-2s} \prod_{p|k} (1-p^{2s-2}).$$

The required result is now readily verified.

# 4. Class number 1

Suppose that *Q(<J( — d))* has class number 1. Then, by the theory of genera, *d* is a prime congruent to 3 (mod 4), and there is just one form / which can be taken as

$$x^2 + xy + \frac{1}{4}(1+d)y^2.$$

We select *k* = 21 and we note that *Q(«Jk)* has class number 1 and fundamental unit e = £(5 + ^/21). Further we note that *(k,d)* = 1 for *d > k,* and that *Ao* = 0. Hence the double sum on the right of (2) has absolute value at most*<sup>m</sup>*

$$(4\pi/\sqrt{d})\sum_{r=1}^{\infty}r\eta^{r},$$

where *ij* = e~"v<"\*. The sum over *r* is precisely *7/1(1—i/)<sup>2</sup> ,* and *tf < \* if *Jd > k;* thus the above expression is at most

Now classical results of Dirichlet give

$$L(1,\chi) = 2\log \epsilon/\sqrt{k}, \quad L(1,\chi\chi') = h\pi/\sqrt{(kd)},$$

where *h* denotes the class number of *Q{-J( — kd)),* and, on substituting into (2), we readily derive the inequality

$$\left|h\log\epsilon - \frac{32}{21}\pi\sqrt{d}\right| < e^{-\pi\sqrt{d}/100},$$

assuming that *d >* 10<sup>20</sup> , say. But *n =* — 2ilogf and so we have on the left a linear form A in two logarithms of the kind considered

**t** *Ada Arith.* **14 (1968), 36-60.**

*<sup>\</sup>* **See Hardy and Wright'\*,** *An introduction to the theory of number\** **(Oxford, 1960), Theorem 271.**

in Theorem 3.1; since clearly  $h < 4\sqrt{d}$  and  $\log \epsilon$ ,  $\log i$  are linearly independent, we conclude that the inequality is untenable if d is larger than some effectively computable number. To calculate the latter, it is convenient to take a second inequality arising from (2) with k = 33, namely

 $|h'\log\epsilon' - \frac{80}{33}\pi\sqrt{d}| < e^{-\pi\sqrt{d}/100},$ 

where h',  $\epsilon'$  are defined like h,  $\epsilon$  above with the new value of k. By subtraction we obtain

$$|b\log\epsilon + b'\log\epsilon'| < e^{-bB},$$

where 
$$\delta^{-1} = 14 \times 10^3$$
,  $B = 140 \sqrt{d}$ ,  $b = 35h$ ,  $b' = -22h'$ ,

and clearly b, b' have absolute values at most B. Since, furthermore,  $\epsilon$ ,  $\epsilon'$  are multiplicatively independent, one can apply the result quoted in § 5 of Chapter 4, with n=2, d=4, A=46, to obtain  $B<10^{250}$ . This gives  $d<10^{500}$ , and a determination of the solutions of the above inequality below this figure is quite feasible. But the computation is in fact not needed here, for it was proved by Heilbronn and Linfoot<sup>†</sup> in 1934 that, apart from the nine discriminants listed in Theorem 5.1, there could be at most one more, and calculations<sup>‡</sup> had shown that the tenth d, if it existed, would exceed  $\exp(10^7)$ .

The above argument is similar to that described by Gelfond and Linnik in 1949, but they had access to the formulae of § 3 only for prime values of k, and in this case  $A_0$  is not 0; thus they were led to an inequality involving three logarithms of algebraic numbers which could not be dealt with effectively at that time. It is a remarkable coincidence that both the formulae for composite k and the desired effective inequality involving three logarithms became available simultaneously in 1966.

## 5. Class number 2

We now indicate briefly how the above arguments can be extended to treat the analogous problem for class number 2.

If  $Q(\sqrt{(-d)})$  has class number 2 and d > 15 then d is congruent to 3 or  $4 \pmod{8}$ ; for if  $d \equiv 7 \pmod{8}$  there are three inequivalent quadratic forms with discriminant -d, namely

$$x^2 + xy + \frac{1}{4}(1+d)y^2$$
,  $2x^2 \pm xy + \frac{1}{8}(1+d)y^2$ .

<sup>†</sup> Quart. J. Math. Oxford Ser. 5 (1934), 293-301.

<sup>1</sup> Trans. Amer. Math. Soc. 122 (1966), 112-19 (H. M. Stark).

<sup>§</sup> For the original solutions see Ann. Math. 94 (1971), 139-52 (A. Baker); 153-73 (H. M. Stark).

When  $d \equiv 4 \pmod{8}$ , two inequivalent quadratic forms with discriminant -d are given by  $x^2 + \frac{1}{2}dy^2$ , and either

$$2x^2 + 2xy + \frac{1}{2}(4+d)y^2$$
 or  $2x^2 + \frac{1}{2}dy^2$ ,

according as  $\frac{1}{4}d \equiv 1$  or 2 (mod 4), and the method of proof of Theorem 5.1 is applicable with only simple modifications.<sup>†</sup> There remains the case  $d \equiv 3 \pmod{8}$ . The theory of genera shows that then d = pq, where p, q are primes congruent to 1 and 3 (mod 4) respectively. On signifying by  $\chi'(n)$  one of the generic characters associated with forms of discriminant -d and writing

$$\chi_{pq}(n) = \left(\frac{-pq}{n}\right), \quad \chi_p(n) = \left(\frac{p}{n}\right), \quad \chi_q(n) = \left(\frac{-q}{n}\right), \quad \chi(n) = \left(\frac{k}{n}\right),$$

where  $k \equiv 1 \pmod{4}$  and (k, pq) = 1, we deduce from classical results of Dirichlet and Kronecker that

$$\begin{split} L(1,\chi)\,L(1,\chi\chi_{pq}) + L(1,\chi\chi_p)\,L(1,\chi\chi_q) \\ &= \tfrac{1}{2} \sum_F \sum_{x,y} (\chi(F) + \chi\chi'(F))\,(F(x,y))^{-1}, \end{split}$$

where F runs through a pair f, f' of inequivalent quadratic forms with discriminant -d and x, y take all integer values, not both 0. We can assume that f is the principal form, whence  $\chi'(f) = 1$ ,  $\chi'(f') = -1$  for all x, y. On appealing to Dirichlet's formulae we thus obtain

$$(k/2\pi)\sqrt{(pq)}\sum_{x,y}\chi(f)/f=h(k)\,h(-kpq)\log\epsilon+h(kp)\,h(-kq)\log\eta,$$

where h(l) denotes the class number of  $Q(\sqrt{l})$  and  $\epsilon$ ,  $\eta$  denote the fundamental units in  $Q(\sqrt{k})$ ,  $Q(\sqrt{(kp)})$  respectively. Finally taking k=21 and employing arguments similar to those applied in the proof of Theorem 5.1, we reach the inequality

$$|h(-21d)\log \epsilon + h(21p)h(-21q)\log \eta - \frac{64}{21}\pi\sqrt{d}| < e^{(-1/10)\sqrt{d}}.$$

This has the form

$$\left|\beta\log\alpha+\beta'\log\alpha'+\beta''\log\alpha''\right|< e^{-\delta B},$$

where the  $\beta$ 's denote algebraic numbers with degrees at most 2, and  $\alpha = \eta$ ,  $\alpha' = \epsilon$ ,  $\alpha'' = -1$ ,  $B = \sqrt{d}$ ,  $\delta = \frac{1}{10}$ . Clearly the heights of the  $\beta$ 's are bounded above by an absolute power of B and the height A of  $\alpha$  is bounded above by  $p^{c\sqrt{p}}$  for some absolute constant c. If  $q \leq d^{\frac{1}{4}}$  then we can take f' as  $qx^2 + qxy + \frac{1}{4}(p+q)y^2.$ 

† See Bull. Lond Math. Soc. 1 (1969), 98-102.

and again the method of proof of Theorem 5.1 is applicable. Thus we can assume that  $q > d^{\frac{1}{4}}$  whence  $p < d^{\frac{1}{4}}$ . We now appeal to the first inequality for  $|\Lambda|$  recorded after the enunciation of Theorem 3.1 and, on noting that the maximum A' of the heights of  $\alpha'$ ,  $\alpha''$  is absolutely bounded, we conclude that  $B < C(\log A)^{1+\zeta}$  for any  $\zeta > 0$ , where  $C = C(\zeta)$  is effectively computable. Hence we have

$$\sqrt{d} < C(c\sqrt{p}\log p)^{1+\zeta}$$

and, recalling that  $p < d^{\frac{1}{4}}$ , this plainly gives an effective upper estimate for d when  $\zeta < \frac{1}{3}$ . In practice<sup>†</sup> the bound for d turns out to be a little over  $10^{1000}$ , and computational work on the zeros of the  $\zeta$ -function has yielded all d in question below this figure; thus it has been checked that the largest d for which  $Q(\sqrt{(-d)})$  has class number 2 is 427.

Progress in this and other fields of application of the theory of linear forms in the logarithms of algebraic numbers is continuing, and, before leaving the topic, we record five further results that have been obtained with its aid. First it has been utilized by E. E. Whitacker<sup>‡</sup> to determine certain imaginary quadratic fields with the Klein four-group as class group. Secondly it has been employed by K. Ramachandra and T. N. Shorey! in researches on a problem of Erdős in prime-number theory; in particular, they have shown that if k is a natural number and if  $n_1, n_2, \dots$  is the sequence, in ascending order, of all natural numbers which have at least one prime factor exceeding k, then the maximum f(k) of  $n_{i+1} - n_i$  (i = 1, 2, ...) satisfies  $f(k) \log k/k \to 0$  as  $k \to \infty$ . Thirdly, in a similar context, R. Tijdeman' has used an inequality for  $|\Lambda|$  of the kind appearing after Theorem 3.1 to resolve in the affirmative a question of Wintner as to whether there exists a sequence of primes such that the sequence  $n_1, n_2, \dots$  of all natural numbers formed from their power products satisfies  $n_{i+1} - n_i \to \infty$  as  $i \to \infty$ . Fourthly, A. Schinzel has applied the second inequality for |A| recorded after Theorem 3.1 to settle an old problem concerning primitive prime factors of  $\alpha^n - \beta^n$ . And, finally, we mention that in 1967, A. Brumer<sup>††</sup> obtained a natural p-adic analogue of an early version of Theorem 3.1 which, in combination with work of Ax, tresolved a well-known problem of Leopoldt on the non-vanishing of the p-adic regulator of an Abelian number field.

```
† Ann. Math. 96 (1972), 174-209 (H. M. Stark).

‡ Ph.D. Thesis, University of Maryland, 1972.

§ Acta Arith. 24 (1973), 99-111; 25 (1974), 365-73.

|| Compositio Math. 26 (1973), 319-30. ¶ J.M. 269 (1974), 27-33.

†† Mathematika, 14 (1967), 121-4. ‡‡ Illinois J. Math. 9 (1965), 584-9.
```

## **ELLIPTIC FUNCTIONS**

## 1. Introduction

Siegel<sup>†</sup> proved in 1932 that if  $\wp(z)$  is a Weierstrass  $\wp$ -function such that the invariants  $g_2$ ,  $g_3$  in the equation

$$(\wp'(z))^2 = 4(\wp(z))^3 - g_2\wp(z) - g_3$$

