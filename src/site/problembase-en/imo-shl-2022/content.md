# <lo-sample/> IMO.SHL.2022.A1

Let $(a_n)_{n\geq 1}$ be a sequence of positive real numbers with the property that

$$(a_{n+1})^2 + a_na_{n+2} \leq a_n + a_{n+2}$$

for all positive integers $n$. Show that $a_{2022}\leq 1$.

<small>

* source:Nigeria
* questionType:Prove
* domain:Alg

</small>

## Solution

We begin by observing that 
$\left(a_{n+1}\right)^{2}-1 \leqslant a_{n}+a_{n+2}-a_{n} a_{n+2}-1$, which is equivalent to

$$\left(a_{n+1}\right)^{2}-1 \leqslant\left(1-a_{n}\right)\left(a_{n+2}-1\right)$$

Suppose now that there exists a positive integer $n$ such that $a_{n+1}>1$ and $a_{n+2}>1$. 
Since $\left(a_{n+1}\right)^{2}-1 \leqslant\left(1-a_{n}\right)\left(a_{n+2}-1\right)$, 
we deduce that $0<1-a_{n}<1<1+a_{n+2}$, thus 
$\left(a_{n+1}\right)^{2}-1<\left(a_{n+2}+1\right)\left(a_{n+2}-1\right)=\left(a_{n+2}\right)^{2}-1$.

On the other hand, 
$\left(a_{n+2}\right)^{2}-1 \leqslant\left(1-a_{n+3}\right)\left(a_{n+1}-1\right)<\left(1+a_{n+1}\right)\left(a_{n+1}-1\right)=\left(a_{n+1}\right)^{2}-1$, 
a contradiction. We have shown that we cannot have two consecutive terms, 
except maybe $a_{1}$ and $a_{2}$, strictly greater than $1$.

Finally, suppose $a_{2022}>1$. This implies that $a_{2021} \leqslant 1$ and $a_{2023} \leqslant 1$. 
Therefore $0< \left(a_{2022}\right)^{2}-1 \leqslant\left(1-a_{2021}\right)\left(a_{2023}-1\right) \leqslant 0$, 
a contradiction. We conclude that $a_{2022} \leqslant 1$.






# <lo-sample/> IMO.SHL.2022.A2

Let $k \ge 2$ be an integer. Find the smallest integer $n \ge k+1$ with the property that there 
exists a set of $n$ distinct real numbers such that each of its elements can be written as a 
sum of $k$ other distinct elements of the set.

<small>

* source:Slovakia
* questionType:FindOptimal
* domain:Alg

</small>


## Solution

*Answer:* $n=k+4$.

First we show that $n \geqslant k+4$. Suppose that there exists such a set 
with $n$ numbers and denote them by $a_{1}<a_{2}<\cdots<a_{n}$.

Note that in order to express $a_{1}$ as a sum of $k$ distinct elements of the set, 
we must have $a_{1} \geqslant a_{2}+\cdots+a_{k+1}$ and, similarly for $a_{n}$, 
we must have $a_{n-k}+\cdots+a_{n-1} \geqslant a_{n}$. We also know that $n \geqslant k+1$.

If $n=k+1$ then we have $a_{1} \geqslant a_{2}+\cdots+a_{k+1}>a_{1}+\cdots+a_{k} \geqslant a_{k+1}$, 
which gives a contradiction.

If $n=k+2$ then we have $a_{1} \geqslant a_{2}+\cdots+a_{k+1} \geqslant a_{k+2}$, 
that again gives a contradiction.

If $n=k+3$ then we have 
$a_{1} \geqslant a_{2}+\cdots+a_{k+1}$ and $a_{3}+\cdots+a_{k+2} \geqslant a_{k+3}$. 
Adding the two inequalities we get $a_{1}+a_{k+2} \geqslant a_{2}+a_{k+3}$, again a contradiction.

It remains to give an example of a set with $k+4$ elements satisfying the 
condition of the problem. We start with the case when $k=2 l$ and $l \geqslant 1$. 
In that case, denote by $A_{i}=\{-i, i\}$ and take the set $A_{1} \cup \cdots \cup A_{l+2}$, 
which has exactly $k+4=2 l+4$ elements. We are left to show that this set satisfies the required condition.

Note that if a number $i$ can be expressed in the desired way, 
then so can $-i$ by negating the expression. 
Therefore, we consider only $1 \leqslant i \leqslant l+2$.

If $i<l+2$, we sum the numbers from some $l-1$ sets 
$A_{j}$ with $j \neq 1, i+1$, and the numbers $i+1$ and -1 .

For $i=l+2$, we sum the numbers from some $l-1$ sets $A_{j}$ with $j \neq 1, l+1$, 
and the numbers $l+1$ and 1 .

It remains to a give a construction for odd $k=2 l+1$ with $l \geqslant 1$ 
(since $k \geqslant 2$ ). To that end, we modify the construction for $k=2 l$ 
by adding 0 to the previous set.

This is a valid set as 0 can be added to each constructed expression, 
and 0 can be expressed as follows: take the numbers $1,2,-3$ and all the numbers 
from the remaining $l-1$ sets $A_{4}, A_{5}, \cdots, A_{l+2}$.




# <lo-sample/> IMO.SHL.2022.A3

Let $\mathbb{R}^+$ denote the set of positive real numbers. Find all functions 
$f: \mathbb{R}^+ \to \mathbb{R}^+$ such that for each $x \in \mathbb{R}^+$, there is exactly one 
$y \in \mathbb{R}^+$ satisfying $$xf(y)+yf(x) \leq 2$$

<small>

* source:Netherlands
* questionType:FindAll
* domain:Alg

</small>


## Solution

*Answer:* The function $f(x)=1/x$ is the only solution.

First we prove that the function $f(x)=1/x$ satisfies the condition of the problem statement. 
The AM-GM inequality gives

$$\frac{x}{y}+\frac{y}{x} \geqslant 2$$

for every $x, y>0$, with equality if and only if $x=y$. 
This means that, for every $x>0$, there exists a unique $y>0$ such that

$$\frac{x}{y}+\frac{y}{x} \leqslant 2$$

namely $y=x$.

Let now $f: \mathbb{R}_{>0} \rightarrow \mathbb{R}_{>0}$ be a function that satisfies 
the condition of the problem statement. We say that a pair of positive real numbers $(x, y)$ 
is good if $x f(y)+y f(x) \leqslant 2$. Observe that if $(x, y)$ is good, then so is $(y, x)$.

*Lemma 1.0.* If $(x, y)$ is good, then $x=y$.

*Proof.* Assume that there exist positive real numbers $x \neq y$ such that $(x, y)$ is good. 
The uniqueness assumption says that $y$ is the unique positive real number such that $(x, y)$ 
is good. In particular, $(x, x)$ is not a good pair. This means that

$$x f(x)+x f(x)>2$$

and thus $x f(x)>1$. Similarly, $(y, x)$ is a good pair, so $(y, y)$ is not a good pair, 
which implies $y f(y)>1$. We apply the AM-GM inequality to obtain

$$x f(y)+y f(x) \geqslant 2 \sqrt{x f(y) \cdot y f(x)}=2 \sqrt{x f(x) \cdot y f(y)}>2$$

This is a contradiction, since $(x, y)$ is a good pair.

By assumption, for any $x>0$, there always exists a good pair containing $x$, 
however Lemma 1 implies that the only good pair that can contain $x$ is $(x, x)$, so

$$x f(x) \leqslant 1 \quad \Longleftrightarrow \quad f(x) \leqslant \frac{1}{x}$$

for every $x>0$.

In particular, with $x=1/f(t)$ for $t>0$, we obtain

$$\frac{1}{f(t)} \cdot f\left(\frac{1}{f(t)}\right) \leqslant 1$$

Hence

$$t \cdot f\left(\frac{1}{f(t)}\right) \leqslant t f(t) \leqslant 1$$

We claim that $(t, 1 / f(t))$ is a good pair for every $t>0$. Indeed,

$$t \cdot f\left(\frac{1}{f(t)}\right)+\frac{1}{f(t)} f(t)=t \cdot f\left(\frac{1}{f(t)}\right)+1 \leqslant 2$$

Lemma 1 implies that $t=1 / f(t) \Longleftrightarrow f(t)=1 / t$ for every $t>0$.

Solution 1.1. We give an alternative way to prove that 
$f(x)=1/x$ assuming $f(x) \leqslant 1 / x$ for every $x>0$.

Indeed, if $f(x)<1/x$ then for every $a>0$ with $f(x)<1/a<1/x$ 
(and there are at least two of them), we have

$$a f(x)+x f(a)<1+\frac{x}{a}<2$$

Hence $(x, a)$ is a good pair for every such $a$, a contradiction. We conclude that $f(x)=1/x$.

Solution 1.2. We can also conclude from Lemma 1 and $f(x) \leqslant 1 / x$ as follows.

*Lemma 2.* The function $f$ is decreasing.

*Proof.* Let $y>x>0$. Lemma 1 says that $(x, y)$ is not a good pair, but $(y, y)$ is. Hence

$$x f(y)+y f(x)>2 \geqslant 2 y f(y)>y f(y)+x f(y)$$

where we used $y>x$ (and $f(y)>0$ ) in the last inequality. This implies that $f(x)>f(y)$, showing that $f$ is decreasing.

We now prove that $f(x)=1 / x$ for all $x$. Fix a value of $x$ and note that for $y>x$ 
we must have $x f(x)+y f(x)>x f(y)+y f(x)>2$ (using that $f$ is decreasing for the first step), 
hence $f(x)>\frac{2}{x+y}$. The last inequality is true for every $y>x>0$. 
If we fix $x$ and look for the supremum of the expression $\frac{2}{x+y}$ over all $y>x$, we get

$$f(x) \geqslant \frac{2}{x+x}=\frac{1}{x}$$

Since we already know that $f(x) \leqslant 1/x$, we conclude that $f(x)=1/x$.



## Solution

*Answer:* The function $f(x)=1/x$ is the only solution.

As in the first solution, we note that $f(x)=1 / x$ is a solution, 
and we set out to prove that it is the only one. We write $g(x)$ for the unique 
positive real number such that $(x, g(x))$ is a good pair. 
In this solution, we prove Lemma 2 without assuming Lemma 1.

*Lemma 2.* The function $f$ is decreasing.

*Proof.* Consider $x<y$. It holds that $y f(g(y))+g(y) f(y) \leqslant 2$. 
Moreover, because $y$ is the only positive real number such that $(g(y), y)$ 
is a good pair and $x \neq y$, we have $x f(g(y))+g(y) f(x)>$ 2. 
Combining these two inequalities yields

$$x f(g(y))+g(y) f(x)>2 \geqslant y f(g(y))+g(y) f(y)$$

or $f(g(y))(x-y)>g(y)(f(y)-f(x))$. Because $g(y)$ and $f(g(y))$ are both positive while 
$x-y$ is negative, it follows that $f(y)<f(x)$, showing that $f$ is decreasing.

We now prove Lemma 1 using Lemma 2. Suppose that $x \neq y$ but $x f(y)+y f(x) \leqslant 2$. 
As in the first solution, we get $x f(x)+x f(x)>2$ and $y f(y)+y f(y)>2$, which implies $x f(x)+y f(y)>2$. Now

$$x f(x)+y f(y)>2 \geqslant x f(y)+y f(x)$$

implies $(x-y)(f(x)-f(y))>0$, which contradicts the fact that $f$ is decreasing. 
So $y=x$ is the unique $y$ such that $(x, y)$ is a good pair, 
and in particular we have $f(x) \leqslant 1 / x$.

We can now conclude the proof as in Solution 1.



## Solution

As in the other solutions we verify that the function $f(x)=1/x$ is a solution. 
We first want to prove the following lemma:

*Lemma 3.* For all $x \in \mathbb{R}_{>0}$ we actually have $x f(g(x))+g(x) f(x)=2$ 
(that is: the inequality is actually an equality).

*Proof.* We proceed by contradiction: Assume there exists some number $x>0$ 
such that for $y=g(x)$ we have $x f(y)+y f(x)<2$. 
Then for any $0<\epsilon<\frac{2-x f(y)-y f(x)}{2 f(x)}$ we have, by uniqueness 
of $y$, that $x f(y+\epsilon)+(y+\epsilon) f(x)>2$. Therefore

$$\begin{align*}
f(y+\epsilon) & >\frac{2-(y+\epsilon) f(x)}{x}=\frac{2-y f(x)-\epsilon f(x)}{x} \\
& >\frac{2-y f(x)-\frac{2-x f(y)-y f(x)}{2}}{x} \\
& =\frac{2-x f(y)-y f(x)}{2 x}+f(y)>f(y) \tag{1}
\end{align*}$$

Furthermore, for every such $\epsilon$ we have 
$g(y+\epsilon) f(y+\epsilon)+(y+\epsilon) f(g(y+\epsilon)) \leqslant 2$ and 
$g(y+\epsilon) f(y)+y f(g(y+\epsilon))>2$ (since $y \neq y+\epsilon=g(g(y+\epsilon)))$. 
This gives us the two inequalities

$$f(g(y+\epsilon)) \leqslant \frac{2-g(y+\epsilon) f(y+\epsilon)}{y+\epsilon} \quad 
\text { and } \quad f(g(y+\epsilon))>\frac{2-g(y+\epsilon) f(y)}{y}$$

Combining these two inequalities and rearranging the terms leads to the inequality

$$2 \epsilon<g(y+\epsilon)[(y+\epsilon) f(y)-y f(y+\epsilon)]$$

Moreover combining with the inequality (1) we obtain

$$2 \epsilon<g(y+\epsilon)\left[(y+\epsilon) f(y)-y\left(\frac{2-x f(y)-y f(x)}{2 x}+f(y)\right)\right] = 
g(y+\epsilon)\left[\epsilon f(y)-y \frac{2-x f(y)-y f(x)}{2 x}\right]$$

We now reach the desired contradiction, since for $\epsilon$ sufficiently small we have 
that the left hand side is positive while the right hand side is negative.

With this lemma it then follows that for all $x, y \in \mathbb{R}_{>0}$ we have

$$x f(y)+y f(x) \geqslant 2$$

since for $y=g(x)$ we have equality and by uniqueness for $y \neq g(x)$ the inequality is strict.

In particular for every $x \in \mathbb{R}_{>0}$ and for $y=x$ we have $2 x f(x) \geqslant 2$, 
or equivalently $f(x) \geqslant 1 / x$ for all $x \in \mathbb{R}_{>0}$. 
With this inequality we obtain for all $x \in \mathbb{R}_{>0}$

$$2 \geqslant x f(g(x))+g(x) f(x) \geqslant \frac{x}{g(x)}+\frac{g(x)}{x} \geqslant 2$$

where the first inequality comes from the problem statement. Consequently each of these 
inequalities must actually be an equality, and in particular we obtain 
$f(x)=1/x$ for all $x \in \mathbb{R}_{>0}$.

## Solution

Again, let us prove that $f(x)=1 / x$ is the only solution. 
Let again $g(x)$ be the unique positive real number such that $(x, g(x))$ is a good pair.

*Lemma 4.* The function $f$ is strictly convex.

Proof. Consider the function $q_{s}(x)=f(x)+s x$ for some real number $s$. 
If $f$ is not strictly convex, then there exist $u<v$ and $t \in(0,1)$ such that

$$f(t u+(1-t) v) \geqslant t f(u)+(1-t) f(v)$$

Hence

$$\begin{aligned}
q_{s}(t u+(1-t) v) & \geqslant t f(u)+(1-t) f(v)+s(t u+(1-t) v) \\
& =t q_{s}(u)+(1-t) q_{s}(v)
\end{aligned}$$

Let $w=t u+(1-t) v$ and consider the case $s=f(g(w)) / g(w)$. For that particular choice of $s$, 
the function $q_{s}(x)$ has a unique minimum at $x=w$. However, since 
$q_{s}(w) \geqslant t q_{s}(u)+(1-t) q_{s}(v)$, it must hold 
$q_{s}(u) \leqslant q_{s}(w)$ or $q_{s}(v) \leqslant q_{s}(w)$, a contradiction.

*Lemma 5.* The function $f$ is continuous.

*Proof.* Since $f$ is strictly convex and defined on an open interval, it is also continuous.

As in Solution 1, we can prove that $f(x) \leqslant 1 / x$. If $f(x)<1 / x$, 
then we consider the function $h(y)=x f(y)+y f(x)$ which is continuous. 
Since $h(x)<2$, there exist at least two distinct $z \neq x$ such that 
$h(z)<2$ giving that $(x, z)$ is good pair for both values of $z$, 
a contradiction. We conclude that $f(x)=1/x$ as desired.

*Comment.* Lemma 5 implies Lemma 3, using an argument similar as in the end of Solution 4.





# <lo-sample/> IMO.SHL.2022.A4

Let $n \geqslant 3$ be an integer, and let $x_1,x_2,\ldots,x_n$ be real numbers in the interval 
$[0,1]$. Let $s=x_1+x_2+\ldots+x_n$, and assume that $s \geqslant 3$. 
Prove that there exist integers $i$ and $j$ with $1 \leqslant i<j \leqslant n$ such that

$$2^{j-i}x_ix_j>2^{s-3}.$$

<small>

* source:Trinidad and Tobago
* questionType:Prove
* domain:Alg

</small>


## Solution.

Let $1 \leqslant a<b \leqslant n$ be such that $2^{b-a} x_{a} x_{b}$ is maximal. 
This choice of $a$ and $b$ implies that $x_{a+t} \leqslant 2^{t} x_{a}$ for all 
$1-a \leqslant t \leqslant b-a-1$, and similarly $x_{b-t} \leqslant 2^{t} x_{b}$ 
for all $b-n \leqslant t \leqslant b-a+1$. 
Now, suppose that $x_{a} \in\left(\frac{1}{2^{u+1}}, \frac{1}{2^{u}}\right]$ and 
$x_{b} \in\left(\frac{1}{2^{v+1}}, \frac{1}{2^{v}}\right]$, 
and write $x_{a}=2^{-\alpha}, x_{b}=2^{-\beta}$. Then

$$\sum_{i=1}^{a+u-1} x_{i} \leqslant 2^{u} x_{a}\left(\frac{1}{2}+\frac{1}{4}+\ldots+\frac{1}{2^{a+u-1}}\right) 
< 2^{u} x_{a} \leqslant 1$$

and similarly,

$$\sum_{i=b-v+1}^{n} x_{i} \leqslant 2^{v} x_{b}\left(\frac{1}{2}+\frac{1}{4}+\ldots+\frac{1}{2^{n-b+v}}\right)
< 2^{v} x_{b} \leqslant 1$$

In other words, the sum of the $x_{i}$ 's for $i$ outside of the interval $[a+u, b-v]$ 
is strictly less than 2. Since the total sum is at least $3$, and each term is at most $1$, 
it follows that this interval must have at least two integers. 
i.e., $a+u<b-v$. Thus, by bounding the sum of the $x_{i}$ for $i \in[1, a+u] \cup[b-v, n]$ 
like above, and trivially bounding each $x_{i} \in(a+u, b-v)$ by 1 , we obtain

$$s<2^{u+1} x_{a}+2^{v+1} x_{b}+((b-v)-(a+u)-1)=b-a+\left(2^{u+1-\alpha}+2^{v+1-\beta}-(u+v+1)\right)$$

Now recall $\alpha \in(u, u+1]$ and $\beta \in(v, v+1]$, so applying Bernoulli's inequality yields $\left.2^{u+1-\alpha}+2^{v+1-\beta}-u-v-1 \leqslant(1+(u+1-\alpha))\right)+(1+(v+1-\beta))-u-v-1=3-\alpha-\beta$.

It follows that $s-3<b-a-\alpha-\beta$, and so

$$2^{s-3}<2^{b-a-\alpha-\beta}=2^{b-a} x_{a} x_{b}$$

*Comment 1.* It is not hard to see that the inequality is tight. 
Suppose that $n = 2k+1$, and we set $x_{k+1}=1, x_{k}=x_{k+2}=\frac{1}{2}+\frac{1}{2^{k}}$, 
and $x_{k+1-t}=x_{k+1+t}=\frac{1}{2^{t}}$. Then $s=3$ (so the right hand side is 1), and

$$\max _{i<j} 2^{j-i} x_{i} x_{j}=2^{2}\left(\frac{1}{2}+\frac{1}{2^{k}}\right)^{2}$$

which can be made arbitrarily close to 1 . Note that $s$ can be made larger by putting in more $1$s in the middle (and this accommodates even $n$ as well).

*Comment 2.* An alternative formulation of the problem is to show that there exists 
a positive constant $c$ (or find the best such $c$ ) such that

$$\max _{i<j} 2^{j-i} x_{i} x_{j}>c 2^{s}$$

The above shows that $c=1 / 8$ is the best possible. A somewhat simpler ending to the proof can be given for $c=1 / 32$.

End of solution for $c=1/32$.

As in the original solution, we arrive at

$$s<2^{u+1} x_{a}+2^{v+1} x_{b}+((b-v)-(a+u)-1)=b-a+\left(2^{u+1-\alpha}+2^{v+1-\beta}-(u+v+1)\right)$$

Now $2^{b-a} x_{a} x_{b} \geqslant 2^{b-a} 2^{-u-1} 2^{-v-1}$, so it is enough to show $s-5<b-a-u-v-2$, 
or $s<b-a-$ $u-v+3$. The fact that $u+1-\alpha<1$ and $v+1-\beta<1$ implies 
$2^{u+1-\alpha}+2^{v+1-\beta}<4$, and so $s<b-a+(2+2-u-v-1)=b-a-u-v-3$.




# <lo-sample/> IMO.SHL.2022.A5

Find all positive integers $n \geqslant 2$ for which there exist $n$ real numbers 
$a_1<\cdots<a_n$ and a real number $r>0$ such that the $\tfrac{1}{2}n(n-1)$ differences 
$a_j-a_i$ for $1 \leqslant i<j \leqslant n$ are equal, in some order, to the numbers 
$r^1,r^2,\ldots,r^{\frac{1}{2}n(n-1)}$.

<small>

* source:Czech Republic
* questionType:FindAll
* domain:Alg

</small>

## Solution

*Answer:* $n \in\{2,3,4\}$.

We first show a solution for each $n \in\{2,3,4\}$. We will later show the impossibility of 
finding such a solution for $n \geqslant 5$.

For $n=2$, take for example $\left(a_{1}, a_{2}\right)=(1,3)$ and $r=2$.

For $n=3$, take the root $r>1$ of $x^{2}-x-1=0$ (the golden ratio) and set 
$\left(a_{1}, a_{2}, a_{3}\right)=$ $\left(0, r, r+r^{2}\right)$. Then

$$\left(a_{2}-a_{1}, a_{3}-a_{2}, a_{3}-a_{1}\right)=\left(r, r^{2}, r+r^{2}=r^{3}\right)$$

For $n=4$, take the root $r \in(1,2)$ of $x^{3}-x-1=0$ (such a root exists because $1^{3}-1-1<0$ 
and $\left.2^{3}-2-1>0\right)$ and set 
$\left(a_{1}, a_{2}, a_{3}, a_{4}\right)=\left(0, r, r+r^{2}, r+r^{2}+r^{3}\right)$. Then

$$\left(a_{2}-a_{1}, a_{3}-a_{2}, a_{4}-a_{3}, a_{3}-a_{1}, a_{4}-a_{2}, a_{4}-a_{1}\right) = 
\left(r, r^{2}, r^{3}, r^{4}, r^{5}, r^{6}\right)$$

For $n \geqslant 5$, we will proceed by contradiction. Suppose there exist numbers 
$a_{1}<\cdots<a_{n}$ and $r>1$ satisfying the conditions of the problem. We start with a lemma:

*Lemma.* We have $r^{n-1}>2$.

Proof. There are only $n-1$ differences $a_{j}-a_{i}$ with $j=i+1$, 
so there exists an exponent $e \leqslant n$ and a difference $a_{j}-a_{i}$ 
with $j \geqslant i+2$ such that $a_{j}-a_{i}=r^{e}$. This implies

$$r^{n} \geqslant r^{e}=a_{j}-a_{i}=\left(a_{j}-a_{j-1}\right)+\left(a_{j-1}-a_{i}\right)>r+r=2r$$

thus $r^{n-1}>2$ as desired.

To illustrate the general approach, we first briefly sketch the idea behind the argument 
in the special case $n=5$. In this case, we clearly have $a_{5}-a_{1}=r^{10}$. 
Note that there are 3 ways to rewrite $a_{5}-a_{1}$ as a sum of two differences, namely

$$\left(a_{5}-a_{4}\right)+\left(a_{4}-a_{1}\right),\left(a_{5}-a_{3}\right)+\left(a_{3}-a_{1}\right),
\left(a_{5}-a_{2}\right)+\left(a_{2}-a_{1}\right)$$

Using the lemma above and convexity of the function $f(n)=r^{n}$, 
we argue that those three ways must be $r^{10}=r^{9}+r^{1}=r^{8}+r^{4}=r^{7}+r^{6}$. 
That is, the "large" exponents keep dropping by 1 , while the "small" exponents 
keep increasing by $n-2, n-3, \ldots, 2$. Comparing any two such equations, 
we then get a contradiction unless $n \leqslant 4$.

Now we go back to the full proof for any $n \geqslant 5$. 
Denote $b=\frac{1}{2} n(n-1)$. Clearly, we have $a_{n}-a_{1}=r^{b}$. Consider the $n-2$ equations of the form:

$$a_{n}-a_{1}=\left(a_{n}-a_{i}\right)+\left(a_{i}-a_{1}\right) \text { for } i \in\{2, \ldots, n-1\}$$

In each equation, one of the two terms on the right-hand side must be at least 
$\frac{1}{2}\left(a_{n}-a_{1}\right)$. But from the lemma we have 
$r^{b-(n-1)}=r^{b} / r^{n-1}<\frac{1}{2}\left(a_{n}-a_{1}\right)$, 
so there are at most $n-2$ sufficiently large elements in 
$\left\{r^{k} \mid 1 \leqslant k<b\right\}$, namely $r^{b-1}, \ldots, r^{b-(n-2)}$ 
(note that $r^{b}$ is already used for $a_{n}-a_{1}$ ). 
Thus, the "large" terms must be, in some order, precisely equal to elements in

$$L=\left\{r^{b-1}, \ldots, r^{b-(n-2)}\right\}$$

Next we claim that the "small" terms in the $n-2$ equations must be equal to the elements in

$$S=\left\{\left.r^{b-(n-2)-\frac{1}{2} i(i+1)} \right\rvert\, 1 \leqslant i \leqslant n-2\right\}$$

in the corresponding order (the largest "large" term with the smallest 
"small" term, etc.). Indeed, suppose that

$$r^{b}=a_{n}-a_{1}=r^{b-i}+r^{\alpha_{i}} \text { for } i \in\{1, \ldots, n-2\}$$

where $1 \leqslant \alpha_{1}<\cdots<\alpha_{n-2} \leqslant b-(n-1)$. 
Since $r>1$ and $f(r)=r^{n}$ is convex, we have

$$r^{b-1}-r^{b-2}>r^{b-2}-r^{b-3}>\ldots>r^{b-(n-3)}-r^{b-(n-2)}$$

implying

$$r^{\alpha_{2}}-r^{\alpha_{1}}>r^{\alpha_{3}}-r^{\alpha_{2}}>\ldots>r^{\alpha_{n-2}}-r^{\alpha_{n-3}}$$

Convexity of $f(r)=r^{n}$ further implies

$$\alpha_{2}-\alpha_{1}>\alpha_{3}-\alpha_{2}>\ldots>\alpha_{n-2}-\alpha_{n-3}$$

Note that $\alpha_{n-2}-\alpha_{n-3} \geqslant 2$ : Otherwise we would have $\alpha_{n-2}-\alpha_{n-3}=1$ and thus

$$r^{\alpha_{n-3}} \cdot(r-1)=r^{\alpha_{n-2}}-r^{\alpha_{n-3}}=r^{b-(n-3)}-r^{b-(n-2)}=r^{b-(n-2)} \cdot(r-1)$$

implying that $\alpha_{n-3}=b-(n-2)$, a contradiction. Therefore, we have

$$\begin{aligned}
\alpha_{n-2}-\alpha_{1} & =\left(\alpha_{n-2}-\alpha_{n-3}\right)+\cdots+\left(\alpha_{2}-\alpha_{1}\right) \\
& \geqslant 2+3+\cdots+(n-2) \\
& =\frac{1}{2}(n-2)(n-1)-1=\frac{1}{2} n(n-3)
\end{aligned}$$

On the other hand, from $\alpha_{n-2} \leqslant b-(n-1)$ and $\alpha_{1} \geqslant 1$ we get

$$\alpha_{n-2}-\alpha_{1} \leqslant b-n=\frac{1}{2} n(n-1)-n=\frac{1}{2} n(n-3)$$

implying that equalities must occur everywhere and the claim about the small terms follows.

Now, assuming $n-2 \geqslant 2$, we have the two different equations:

$$r^{b}=r^{b-(n-2)}+r^{b-(n-2)-1} \text { and } r^{b}=r^{b-(n-3)}+r^{b-(n-2)-3}$$

which can be rewritten as

$$\begin{equation*}
r^{n-1}=r+1 \quad \text { and } \quad r^{n+1}=r^{4}+1 \tag{1}
\end{equation*}$$

Simple algebra now gives

$$r^{4}+1=r^{n+1}=r^{n-1} \cdot r^{2}=r^{3}+r^{2} \Longrightarrow(r-1)\left(r^{3}-r-1\right)=0$$

Since $r \neq 1$, using Equation (1) we conclude $r^{3}=r+1=r^{n-1}$, 
thus $n=4$, which gives a contradiction.




# <lo-sample/> IMO.SHL.2022.A6

Let $\mathbb R$ be the set of real numbers. We denote by 
$\mathcal F$ the set of all functions $f\colon\mathbb R\to\mathbb R$ such that

$$f(x + f(y)) = f(x) + f(y)$$

for every $x,y\in\mathbb R$ Find all rational numbers $q$ such that 
for every function $f\in\mathcal F$, there exists some $z\in\mathbb R$ satisfying $f(z)=qz$.

<small>

* source:Indonesia
* questionType:FindAll
* domain:Alg

</small>

## Solution

*Answer:* The desired set of rational numbers is 
$\left\{\frac{n+1}{n}: n \in \mathbb{Z}, n \neq 0\right\}$.

Let $Z$ be the set of all rational numbers $q$ such that for every function 
$f \in \mathcal{F}$, there exists some $z \in \mathbb{R}$ satisfying $f(z)=q z$. Let further

$$S=\left\{\frac{n+1}{n}: n \in \mathbb{Z}, n \neq 0\right\}$$

We prove that $Z=S$ by showing the two inclusions: $S \subseteq Z$ and $Z \subseteq S$.

We first prove that $S \subseteq Z$. Let $f \in \mathcal{F}$ and let $P(x, y)$ be the relation 
$f(x+f(y))=f(x)+$ $f(y)$. First note that $P(0,0)$ gives $f(f(0))=2 f(0)$. 
Then, $P(0, f(0))$ gives $f(2 f(0))=3 f(0)$. We claim that

$$f(k f(0))=(k+1) f(0)$$

for every integer $k \geqslant 1$. The claim can be proved by induction. 
The cases $k=1$ and $k=2$ have already been established. 
Assume that $f(k f(0))=(k+1) f(0)$ and consider $P(0, k f(0))$ which gives

$$f((k+1) f(0))=f(0)+f(k f(0))=(k+2) f(0)$$

This proves the claim. We conclude that $\frac{k+1}{k} \in Z$ for every integer 
$k \geqslant 1$. Note that $P(-f(0), 0)$ gives $f(-f(0))=0$. We now claim that

$$f(-k f(0))=(-k+1) f(0)$$

for every integer $k \geqslant 1$. The proof by induction is similar to the one above. 
We conclude that $\frac{-k+1}{-k} \in Z$ for every integer $k \geqslant 1$. 
This shows that $S \subseteq Z$.

We now prove that $Z \subseteq S$. Let $p$ be a rational number outside the set $S$. 
We want to prove that $p$ does not belong to $Z$. To that end, we construct a function 
$f \in \mathcal{F}$ such that $f(z) \neq p z$ for every $z \in \mathbb{R}$. 
The strategy is to first construct a function

$$g:[0,1) \rightarrow \mathbb{Z}$$

and then define $f$ as $f(x)=g(\{x\})+\lfloor x\rfloor$. This function $f$ belongs to $\mathcal{F}$. Indeed,

$$\begin{aligned}
f(x+f(y)) & =g(\{x+f(y)\})+\lfloor x+f(y)\rfloor \\
& =g(\{x+g(\{y\})+\lfloor y\rfloor\})+\lfloor x+g(\{y\})+\lfloor y\rfloor\rfloor \\
& =g(\{x\})+\lfloor x\rfloor+g(\{y\})+\lfloor y\rfloor \\
& =f(x)+f(y)
\end{aligned}$$

where we used that $g$ only takes integer values.

*Lemma 1.* For every $\alpha \in[0,1)$, there exists $m \in \mathbb{Z}$ such that

$$m+n \neq p(\alpha+n)$$

for every $n \in \mathbb{Z}$.

*Proof.* Note that if $p=1$ the claim is trivial. If $p \neq 1$, then the claim is 
equivalent to the existence of an integer $m$ such that

$$\frac{m-p \alpha}{p-1}$$

is never an integer. Assume the contrary. That would mean that both

$$\frac{m-p \alpha}{p-1} \text { and } \frac{(m+1)-p \alpha}{p-1}$$

are integers, and so is their difference. The latter is equal to

$$\frac{1}{p-1}$$

Since we assumed $p \notin S, 1 /(p-1)$ is never an integer. This is a contradiction.

Define $g:[0,1) \rightarrow \mathbb{Z}$ by $g(\alpha)=m$ for any integer $m$ 
that satisfies the conclusion of Lemma 1. Note that $f(z) \neq p z$ if and and only if

$$g(\{z\})+\lfloor z\rfloor \neq p(\{z\}+\lfloor z\rfloor)$$

The latter is guaranteed by the construction of the function $g$. We conclude that 
$p \notin Z$ as desired. This shows that $Z \subset S$.





# <lo-sample/> IMO.SHL.2022.A7

For a positive integer $n$ we denote by $s(n)$ the sum of the digits of $n$. 
Let $P(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$ be a polynomial, where $n \geqslant 2$ 
and $a_i$ is a positive integer for all $0 \leqslant i \leqslant n-1$. 
Could it be the case that, for all positive integers $k$, $s(k)$ 
and $s(P(k))$ have the same parity?


<small>

* source:Belarus
* questionType:ProveDisprove
* domain:Alg

</small>

## Solution

*Answer:* No. For any such polynomial there exists a positive integer $k$ such 
that $s(k)$ and $s(P(k))$ have different parities.

With the notation above, we begin by choosing a positive integer $t$ such that

$$10^{t}>\max \left\{\frac{100^{n-1} a_{n-1}}{\left(10^{\frac{1}{n-1}}-9^{\frac{1}{n-1}}\right)^{n-1}}, 
\frac{a_{n-1}}{9} 10^{n-1}, \frac{a_{n-1}}{9}\left(10 a_{n-1}\right)^{n-1}, \ldots, 
\frac{a_{n-1}}{9}\left(10 a_{0}\right)^{n-1}\right\}$$

As a direct consequence of $10^{t}$ being bigger than the first quantity listed in the above set, we get that the interval

$$I=\left[\left(\frac{9}{a_{n-1}} 10^{t}\right)^{\frac{1}{n-1}},\left(\frac{1}{a_{n-1}} 
10^{t+1}\right)^{\frac{1}{n-1}}\right)$$

contains at least $100$ consecutive positive integers.

Let $X$ be a positive integer in $I$ such that $X$ is congruent to 
$1 \bmod 100$. Since $X \in I$ we have

$$9 \cdot 10^{t} \leqslant a_{n-1} X^{n-1}<10^{t+1}$$

thus the first digit (from the left) of $a_{n-1} X^{n-1}$ must be $9$.

Next, we observe that 
$a_{n-1}\left(10 a_{i}\right)^{n-1}<9 \cdot 10^{t} \leqslant a_{n-1} X^{n-1}$, 
thus $10 a_{i}<X$ for all $i$, which immediately implies that $a_{0}<a_{1} X<\cdots<a_{n} X^{n}$, 
and the number of digits of this strictly increasing sequence forms a 
strictly increasing sequence too. In other words, if $i<j$, the number 
of digits of $a_{i} X^{i}$ is less than the number of digits of $a_{j} X^{j}$.

Let $\alpha$ be the number of digits of $a_{n-1} X^{n-1}$, thus 
$10^{\alpha-1} \leqslant a_{n-1} X^{n-1}<10^{\alpha}$. We are now going to look at 
$P\left(10^{\alpha} X\right)$ and $P\left(10^{\alpha-1} X\right)$ 
and prove that the sum of their digits has different parities. 
This will finish the proof since 
$s\left(10^{\alpha} X\right)=s\left(10^{\alpha-1} X\right)=s(X)$.

We have $P\left(10^{\alpha} X\right)=10^{\alpha n} X^{n}+a_{n-1} 10^{\alpha(n-1)} X^{n-1}+\cdots+a_{0}$, 
and since $10^{\alpha(i+1)}>10^{\alpha i} a_{n-1} X^{n-1}>$ $10^{\alpha i} a_{i} X^{i}$, 
the terms $a_{i} 10^{\alpha i} X^{i}$ do not interact when added; 
in particular, there is no carryover caused by addition. 
Thus we have $s\left(P\left(10^{\alpha} X\right)\right)=s\left(X^{n}\right)+s\left(a_{n-1} X^{n-1}\right)+\cdots+s\left(a_{0}\right)$.

We now look at $P\left(10^{\alpha-1} X\right)=10^{(\alpha-1) n} X^{n}+a_{n-1} 10^{(\alpha-1)(n-1)} X^{n-1}+\cdots+a_{0}$. 
Firstly, if $i<n-1$, then $a_{n-1} X^{n-1}$ has more digits than 
$a_{i} X^{i}$ and $a_{n-1} X^{n-1} \geqslant 10 a_{i} X^{i}$. It now follows that 
$10^{(\alpha-1)(i+1)+1}>10^{(\alpha-1) i} a_{n-1} X^{n-1} \geqslant 10^{(\alpha-1) i+1} a_{i} X^{i}$, 
thus all terms $10^{(\alpha-1) i} a_{i} X^{i}$ for $0 \leqslant i \leqslant n-1$ 
come in 'blocks', exactly as in the previous case.

Finally, $10^{(\alpha-1) n+1}>10^{(\alpha-1)(n-1)} a_{n-1} X^{n-1} \geqslant 10^{(\alpha-1) n}$, 
thus $10^{(\alpha-1)(n-1)} a_{n-1} X^{n-1}$ has exactly $(\alpha-1) n+1$ digits, 
and its first digit is 9 , as established above. On the other hand, 
$10^{(\alpha-1) n} X^{n}$ has exactly $(\alpha-1) n$ zeros, 
followed by 01 (as $X$ is $1 \bmod 100$). Therefore, when we add the terms, 
the 9 and 1 turn into 0 , the 0 turns into 1 , and nothing else is affected.

Putting everything together, we obtain

$$
s\left(P\left(10^{\alpha-1} X\right)\right)=s\left(X^{n}\right)+s\left(a_{n-1} X^{n-1}\right)+\cdots+s\left(a_{0}\right)-9=s\left(P\left(10^{\alpha} X\right)\right)-9
$$

thus $s\left(P\left(10^{\alpha} X\right)\right)$ and $s\left(P\left(10^{\alpha-1} X\right)\right)$ 
have different parities, as claimed.




# <lo-sample/> IMO.SHL.2022.A8

For a positive integer $n$, an $n$-sequence is a sequence $(a_0,\ldots,a_n)$ 
of non-negative integers satisfying the following condition: if $i$ and $j$ 
are non-negative integers with $i+j \leqslant n$, then $a_i+a_j \leqslant n$ and $a_{a_i+a_j}=a_{i+j}$.

Let $f(n)$ be the number of $n$-sequences. Prove that there exist positive real numbers 
$c_1$, $c_2$, and $\lambda$ such that \[c_1\lambda^n<f(n)<c_2\lambda^n\]for all positive integers $n$.

<small>

* source:Canada
* questionType:Prove
* domain:Alg

</small>


## Solution

*Answer:* Such constants exist with $\lambda=3^{1 / 6}$; we will discuss 
appropriate values of $c_{1}$ and $c_{2}$ in the solution below.

In order to solve this, we will give a complete classification of $n$-sequences.

Let $k=\lfloor n / 2\rfloor$. We will say that an $n$-sequence is large if 
$a_{i}>k$ for some $i$, and small if no such $i$ exists. 
For now we will assume that $\left(a_{i}\right)$ is not the identity sequence 
(in other words, that $a_{i} \neq i$ for some $i$ ).

*Lemma 1.* If $a_{r}=a_{s}$ and $r, s<n$, then $a_{r+1}=a_{s+1}$.

*Proof.* We have $a_{r+1}=a_{a_{r}+a_{1}}=a_{a_{s}+a_{1}}=a_{s+1}$.

*Lemma 2.* If $i \leqslant k$, then $a_{i} \leqslant k$.

*Proof.* We have $i+i \leqslant n$, so $a_{i}+a_{i} \leqslant n$ whence $a_{i} \leqslant k$.

*Lemma 3.* There exist $r, s$ such that $a_{r}=a_{s}$ and $r \neq s$.

*Proof.* If $a_{0} \neq 0$ then $a_{2 a_{0}}=a_{0}$. 
Otherwise, $a_{a_{i}}=a_{i}$ for all $i$, so take $i$ such that 
$a_{i} \neq i$ (which we can do by our earlier assumption).

*Lemma 4.* Let $r$ be the smallest index such that $a_{s}=a_{r}$ for some $s>r$, 
and let $d$ be the minimum positive integer such that $a_{r+d}=a_{r}$. Then

1. The subsequence $\left(a_{r}, a_{r+1}, \ldots, a_{n}\right)$ 
   is periodic with minimal period $d$. That is, for $u<v$, we have $a_{u}=a_{v}$ 
   if and only if $u, v \geqslant r$ and $d \mid v-u$.
2. $a_{i}=i$ for $i<r$ and $a_{i} \geqslant r$ for $i \geqslant r$.

In this case we say $\left(a_{i}\right)$ has period $d$ and offset $r$.

*Proof.* We prove each in turn:

1. The "if" implication is clear from Lemma 1. For the reverse direction, 
   suppose $a_{u}=a_{v}$. Then there are integers $r \leqslant u_{0}, v_{0}<r+d$ 
   such that $d \mid u-u_{0}, v-v_{0}$, so $a_{u_{0}}=a_{u}=a_{v}=$ $a_{v_{0}}$. 
   If $u_{0}<v_{0}$ then $a_{r+d+u_{0}-v_{0}}=a_{r+d}=a_{r}$, 
   contradicting the minimality of $d$. There is a similar contradiction when 
   $u_{0}>v_{0}$. Thus $u_{0}=v_{0}$, so $d \mid u-v$.
2. If $r=0$ there is nothing to prove. Otherwise $a_{0}=a_{2 a_{0}}$ so $2 a_{0}=0$. 
   Then we have $a_{a_{i}}=a_{i}$ for all $i$, so $a_{i}=i$ for $i<r$.

*Lemma 5.* Either

1. $d \mid a_{i}-i$ for all $i$, or
2. $r=0$ and $d \mid a_{i}-i-d / 2$ for all $i$.

*Proof.* Note that Lemma 4 tells us that if $a_{u}=a_{v}$ then $d \mid u-v$. 
Since $a_{a_{i}+a_{0}}=a_{i}$ for all $i$, we have $d \mid a_{i}-i+a_{0}$. 
For $i=0$, this means that $d \mid 2 a_{0}$. If $d \mid a_{0}$ then that 
means that $d \mid a_{i}-i$ for all $i$. Otherwise, if $d \nmid a_{0}$, 
then $d \mid a_{0}-d / 2$ and thus $d \mid a_{i}-i-d / 2$ for all $i$. 
In addition, part 2 of Lemma 4 says that we must have $r=0$ in this case.

*Lemma 6.* If $d$ is even and $d \mid a_{0}-d / 2$, then $\left(a_{i}\right)$ is small. 
(Note that we must have $r=0$ in this case.)

*Proof.* Note that if $d \leqslant k+1$, then by Lemma 
$2,\left(a_{0}, \ldots, a_{d-1}\right)$ is a period for the sequence consisting 
of elements at most $k$, so $\left(a_{i}\right)$ must be small. 
Now suppose $d>k+1$. We show that $a_{i} \leqslant k$ for all $i$ by induction. 
Note that Lemma 2 already establishes this for $i \leqslant k$. 
We must have $d \mid a_{d / 2}$ and $a_{d / 2} \leqslant k<d$ so $a_{d / 2}=0$. 
Thus, for $i>k$, if 
$a_{j} \leqslant k$ for $j<i$, then $a_{i-d / 2} \leqslant k$, so $a_{i}=a_{(i-d / 2)+d / 2}=a_{a_{i-d / 2}} \leqslant k$.

*Lemma 7.* If $\left(a_{i}\right)$ is small, then $r+d \leqslant k+1$.

*Proof.* Since $\left(a_{i}\right)$ is small, there exists $u, v \leqslant k+1$ 
such that $u<v$ and $a_{u}=a_{v}$. Thus $u \leqslant r$ and $d \mid v-u$, so $r+d \leqslant v \leqslant k+1$.

*Lemma 8.* If $\left(a_{i}\right)$ is large, then $r+d>k+1$ and $a_{i}=i$ 
for all $0 \leqslant i<r+d$.

*Proof.* Since $\left(a_{i}\right)$ is large and has period $d$ and offset $r$, 
the period $\left(a_{r}, \ldots, a_{r+d-1}\right)$ must have an element that 
is larger than $k$, so by Lemma 2 we must have $r+d-1>k$.

We already have $a_{i}=i$ for $i<r$. Now we show that $a_{i}=i$ for 
$r \leqslant i \leqslant k$. By Lemma 6 we have $d \mid a_{i}-i$ but 
$r \leqslant i \leqslant k$. Since $k-r+1>d$, this means that $a_{i}=i$ for $i \leqslant k$.

Finally, one can show inductively that $a_{i}=i$ for $k<i<r+d$. 
Indeed, if $a_{j}=j$ for all $j<i$, then $a_{i} \geqslant i$ 
(otherwise $a_{i}=a_{j}$ for some $j<i$, but then $r \leqslant j$ and $i<r+d$ 
means that $d \nmid j-i$.) However, $a_{i}+(n-i)=a_{i}+a_{n-i} \leqslant n$, so $a_{i}=i$.

Thus large sequences are determined by $r$ and $d$. It is not hard to 
check that all sequences of the form $a_{i}=i$ for $i<r+d$ and with period 
$d$ and offset $r$ are $n$-sequences. There are $(n-k-1)(n+k+2) / 2$ 
possible choices of $(r, d)$ where $0 \leqslant r<n, d \geqslant 1$, and $k+1<r+d \leqslant n$.

For small sequences, for a given period $d$ and offset $r$, we need to choose 
the period $\left(a_{r}, \ldots, a_{r+d-1}\right)$ satisfying 
$r \leqslant a j \leqslant k$ and $d \mid a_{j}-j$ for $r \leqslant j<r+d$. 
There are $g(k+1-r, d)$ such choices, where we define $g(x, d)$ to be 
$(p+1)^{q} p^{d-q}$ with $p=\lfloor x / d\rfloor$ and $q=x-d p$.

Furthermore, if $d$ is even then there are $g(k+1, d)$ choices for the period 
$\left(a_{0}, \ldots, a_{d-1}\right)$ satisfying $d \mid a_{j}-j-d / 2$ for $j<d$. 
Again it is not hard to check that, once these choices are made, then the resulting sequence is an $n$-sequence.

Thus the total number of $n$-sequences is

$$\begin{equation*}
f(n)=1+\frac{(n-k-1)(n+k+2)}{2}+\sum_{d^{\prime}=1}^{\lfloor(k+1) / 2\rfloor} 
g\left(k+1,2 d^{\prime}\right)+\sum_{r=0}^{k} \sum_{d=1}^{k+1-r} g(k+1-r, d) \tag{1}
\end{equation*}$$

Now, to show that $f(n)>c_{1} \lambda^{n}$ for some $c_{1}$, we note that

$$f(n)>g\left(k+1,\left\lfloor\frac{k+1}{3}\right\rfloor\right) \geqslant 3^{\lfloor(k+1) / 3\rfloor}>3^{n / 6}-1$$

To show that $f(n)<c_{2} \lambda^{n}$ for some $c_{2}$, it actually suffices 
to show that there is a positive real number $c_{3}$ such that for all positive integers $x$,

$$\sum_{d=1}^{x} g(x, d) \leqslant c_{3} 3^{x / 3}$$

In fact, the following lemma suffices, as it bounds the left hand side of the above 
inequality by a pair of geometric series with initial term $3^{x / 3}$ :

*Lemma.* For positive $d, x$, we have:

$$g(x, d) \leqslant \begin{cases}3^{x / 3}\left(\frac{64}{81}\right)^{x / 3-d}, & 
\text { if } d \leqslant x / 3 \\ 3^{x / 3}\left(\frac{8}{9}\right)^{d-x / 3}, & 
\text { if } d \geqslant x / 3\end{cases}$$

Proof. There are a few key observations needed, all of which are immediate from the definition:

- $(x, d)$ is the maximum product of a sequence of $d$ integers that sums to $x$.
- For any positive integer $k$, we have $g(k x, k d)=g(x, d)^{k}$.
- If $2 d \leqslant x \leqslant 3 d$, then $g(x, d)=2^{3 d-x} 3^{x-2 d}$. Likewise, if $3 d \leqslant x \leqslant 4 d$ then $g(x, d)=$ $3^{4 d-x} 4^{x-3 d}$.

With these observations, if $d \leqslant x / 3$, then

$$3^{4(x-3 d)} g(3 x, 3 d) \leqslant g(3 x+12(x-3 d), 3 d+4(x-3 d))=g(15 x-36 d, 4 x-9 d)$$

To calculate $g(15 x-36 d, 4 x-9 d)$, note that

$$\begin{aligned}
& 3(4 x-9 d)=12 x-27 d \leqslant 15 x-36 d \\
& 4(4 x-9 d)=16 x-36 d \geqslant 15 x-36 d
\end{aligned}$$

so

$$g(15 x-36 d, 4 x-9 d)=3^{4(4 x-9 d)-(15 x-36 d)} 4^{(15 x-36 d)-3(4 x-9 d)}=3^{x} 4^{3(x-3 d)}$$

Thus

$$g(x, d)^{3}=g(3 x, 3 d)=\frac{3^{4(x-3 d)} g(3 x, 3 d)}{3^{4(x-3 d)}} \leqslant 
\frac{3^{x} 4^{3(x-3 d)}}{3^{4(x-3 d)}}=3^{x}\left(\frac{64}{81}\right)^{x-3 d}$$

which completes the proof of the first claim. Likewise, if $d \geqslant x / 3$,

$$3^{2(3 d-x)} g(3 x, 3 d) 3 \leqslant g(3 x+6(3 d-x), 3 d+2(3 d-x))=g(18 d-3 x, 9 d-2 x)$$

Again we have

$$2(9 d-2 x) \leqslant 18-3 x \leqslant 18-3 x+3(3 d-x)=3(9 d-2 x)$$

so

$$g(18 d-3 x, 9 d-2 x)=2^{3(9 d-2 x)-(18 d-3 x)} 3^{(18 d-3 x)-2(9 d-2 x)}=2^{3(3 d-x)} 3^{x}$$

Thus

$$g(x, d)^{3}=g(3 x, 3 d)=\frac{2^{3(3 d-x)} g(3 x, 3 d)}{3^{2(3 d-x)}} \leqslant 
\frac{2^{3(3 d-x) 3^{x}}}{3^{2(3 d-x)}}=3^{x}\left(\frac{8}{9}\right)^{3 d-x}$$

from which the second claim follows.

Common remarks. The best possible value of $c_{1}$ is constrained by $n=1$: 
in this case, $f(1)=2$, which means that $c_{1}>2 \cdot 3^{-1 / 6} \approx 1.66537$.

With a careful analysis one can show that the best possible value of $c_{2}$ is 
$\frac{236567}{4930} 3^{1 / 3} \approx$ 69.20662$.






# <lo-sample/> IMO.SHL.2022.C1

A $\pm 1$-sequence is a sequence of $2022$ numbers $a_1, \ldots, a_{2022},$ 
each equal to either $+1$ or $-1$. Determine the largest $C$ so that, 
for any $\pm 1$-sequence, there exists an integer $k$ and indices 
$1 \le t_1 < \ldots < t_k \le 2022$ so that $t_{i+1} - t_i \le 2$ for all $i$, 
and $$\left| \sum_{i = 1}^{k} a_{t_i} \right| \ge C.$$


<small>

* questionType:FindOptimal
* domain:Comb

</small>


# <lo-sample/> IMO.SHL.2022.C2

The Bank of Oslo issues two types of coin: aluminum (denoted A) and bronze (denoted B). 
Marianne has $n$ aluminum coins and $n$ bronze coins arranged in a row 
in some arbitrary initial order. A chain is any subsequence of consecutive 
coins of the same type. Given a fixed positive integer $k \leq 2n$, 
Gilberty repeatedly performs the following operation: 
he identifies the longest chain containing 
the $k^{th}$ coin from the left and moves all coins in that chain to the left end of the row. 
For example, if $n=4$ and $k=4$, the process starting from the ordering 
$AABBBABA$ would be $AABBBABA \to BBBAAABA \to AAABBBBA \to BBBBAAAA \to ...$

Find all pairs $(n,k)$ with $1 \leq k \leq 2n$ such that for every initial ordering, 
at some moment during the process, the leftmost $n$ coins will all be of the same type.


<small>

* questionType:FindAll
* domain:Comb

</small>



# <lo-sample/> IMO.SHL.2022.C3

In each square of a garden shaped like a $2022 \times 2022$ board, there is initially a tree of height $0$. A gardener and a lumberjack alternate turns playing the following game, with the gardener taking the first turn:

* The gardener chooses a square in the garden. Each tree on that square and all the 
  surrounding squares (of which there are at most eight) then becomes one unit taller.
* The lumberjack then chooses four different squares on the board. Each tree of 
  positive height on those squares then becomes one unit shorter.

We say that a tree is majestic if its height is at least $10^6$. Determine the largest $K$ such 
that the gardener can ensure there are eventually $K$ majestic trees on the board, 
no matter how the lumberjack plays.


<small>

* questionType:FindOptimal
* domain:Comb

</small>



# <lo-sample/> IMO.SHL.2022.C4

Let $n > 3$ be a positive integer. Suppose that $n$ children are arranged in a circle, and $n$ 
coins are distributed between them (some children may have no coins). At every step, a child with at 
least 2 coins may give 1 coin to each of their immediate neighbors on the right and left. 
Determine all initial distributions of the coins from which it is possible that, 
after a finite number of steps, each child has exactly one coin.


<small>

* questionType:FindAll
* domain:Comb

</small>


# <lo-sample/> IMO.SHL.2022.C5

Let $m,n \geqslant 2$ be integers, let $X$ be a set with $n$ elements, and let 
$X_1,X_2,\ldots,X_m$ be pairwise distinct non-empty, not necessary disjoint subset of $X$. 
A function $f \colon X \to \{1,2,\ldots,n+1\}$ is called nice if there exists an index $k$ such that 

$$\sum_{x \in X_k} f(x)>\sum_{x \in X_i} f(x) \quad \text{for all } i \ne k.$$

Prove that the number of nice functions is at least $n^n$.


<small>

* questionType:Prove
* domain:Comb

</small>




# <lo-sample/> IMO.SHL.2022.C6

Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially 
containing a single pebble. One can perform moves of the following form: choose two piles, 
take an equal number of pebbles from each pile and form a new pile out of these pebbles. 
Find (in terms of $n$) the smallest number of nonempty piles that one can obtain by 
performing a finite sequence of moves of this form.


<small>

* questionType:FindOptimal
* domain:Comb

</small>



# <lo-sample/> IMO.SHL.2022.C7

Lucy starts by writing $s$ integer-valued $2022$-tuples on a blackboard. 
After doing that, she can take any two (not necessarily distinct) tuples 
$\mathbf{v}=(v_1,\ldots,v_{2022})$ and $\mathbf{w}=(w_1,\ldots,w_{2022})$ 
that she has already written, and apply one of the following operations 
to obtain a new tuple:

\begin{align*}
\mathbf{v}+\mathbf{w}&=(v_1+w_1,\ldots,v_{2022}+w_{2022}) \\ 
\mathbf{v} \lor \mathbf{w}&=(\max(v_1,w_1),\ldots,\max(v_{2022},w_{2022}))
\end{align*}

and then write this tuple on the blackboard.

It turns out that, in this way, Lucy can write any integer-valued 
$2022$-tuple on the blackboard after finitely many steps. 
What is the smallest possible number $s$ of tuples that she initially wrote?


<small>

* questionType:FindOptimal
* domain:Comb

</small>



# <lo-sample/> IMO.SHL.2022.C8

Let $n$ be a positive integer. A Nordic square is an $n \times n$ board containing 
all the integers from $1$ to $n^2$ so that each cell contains exactly one number. 
Two different cells are considered adjacent if they share a common side. 
Every cell that is adjacent only to cells containing larger numbers is called a valley. 
An uphill path is a sequence of one or more cells such that:

(i) the first cell in the sequence is a valley,  
(ii) each subsequent cell in the sequence is adjacent to the previous cell, and  
(iii) the numbers written in the cells in the sequence are in increasing order.

Find, as a function of $n$, the smallest possible total number of uphill paths in a Nordic square.

<small>

* Author:Nikola Petrović
* questionType:FindOptimal
* domain:Comb

</small>




# <lo-sample/> IMO.SHL.2022.C9

Let $\mathbb Z_{\ge 0}$ be the set of non-negative integers, and let 
$f:\mathbb Z_{\ge 0}\times \mathbb Z_{\ge 0} \to \mathbb Z_{\ge 0}$ be a 
bijection such that whenever $f(x_1,y_1) > f(x_2, y_2)$, we have 

$$f(x_1+1, y_1) > f(x_2 + 1, y_2)$ and $f(x_1, y_1+1) > f(x_2, y_2+1).$$

Let $N$ be the number of pairs of integers $(x,y)$ with $0\le x,y<100$, 
such that $f(x,y)$ is odd. Find the smallest and largest possible values of $N$.


<small>

* questionType:FindOptimal
* domain:Comb

</small>


# <lo-sample/> IMO.SHL.2022.G1

Let $ABCDE$ be a convex pentagon such that $BC=DE$. Assume that there is a point $T$ inside 
$ABCDE$ with $TB=TD,TC=TE$ and $\angle ABT = \angle TEA$. 
Let line $AB$ intersect lines $CD$ and $CT$ at points $P$ and $Q$, respectively. 
Assume that the points $P,B,A,Q$ occur on their line in that order. 
Let line $AE$ intersect $CD$ and $DT$ at points $R$ and $S$, respectively. 
Assume that the points $R,E,A,S$ occur on their line in that order. 
Prove that the points $P,S,Q,R$ lie on a circle.


<small>

* questionType:Prove
* domain:Geom

</small>


# <lo-sample/> IMO.SHL.2022.G2

In the acute-angled triangle $ABC$, the point $F$ is the foot of the altitude 
from $A$, and $P$ is a point on the segment $AF$. The lines through $P$ parallel 
to $AC$ and $AB$ meet $BC$ at $D$ and $E$, respectively. 
Points $X \ne A$ and $Y \ne A$ lie on the circles $ABD$ and $ACE$, 
respectively, such that $DA = DX$ and $EA = EY$.

Prove that $B, C, X,$ and $Y$ are concyclic.

<small>

* questionType:Prove
* domain:Geom

</small>


# <lo-sample/> IMO.SHL.2022.G3

Let $ABCD$ be a cyclic quadrilateral. Assume that the points 
$Q, A, B, P$ are collinear in this order, in such a way that the 
line $AC$ is tangent to the circle $ADQ$, and the line $BD$ is 
tangent to the circle $BCP$. Let $M$ and $N$ be the midpoints 
of segments $BC$ and $AD$, respectively. Prove that the following three 
lines are concurrent: line $CD$, the tangent of circle $ANQ$ at point $A$, 
and the tangent to circle $BMP$ at point $B$.


<small>

* questionType:Prove
* domain:Geom

</small>


# <lo-sample/> IMO.SHL.2022.G4

Let $ABC$ be an acute-angled triangle with $AC > AB$, let $O$ be its circumcentre, 
and let $D$ be a point on the segment $BC$. The line through $D$ perpendicular 
to $BC$ intersects the lines $AO, AC,$ and $AB$ at $W, X,$ and $Y,$ respectively. 
The circumcircles of triangles $AXY$ and $ABC$ intersect again at $Z \ne A$.

Prove that if $W \ne D$ and $OW = OD,$ then $DZ$ is tangent to the circle $AXY.$


<small>

* questionType:Prove
* domain:Geom

</small>


# <lo-sample/> IMO.SHL.2022.G5

Let $ABC$ be a triangle and $\ell_1,\ell_2$ be two parallel lines. 
Let $\ell_i$ intersects line $BC,CA,AB$ at $X_i,Y_i,Z_i$, respectively. 
Let $\Delta_i$ be the triangle formed by the line passed through $X_i$ and 
perpendicular to $BC$, the line passed through $Y_i$ and perpendicular to $CA$, 
and the line passed through $Z_i$ and perpendicular to $AB$. 
Prove that the circumcircles of $\Delta_1$ and $\Delta_2$ are tangent.


<small>

* questionType:Prove
* domain:Geom

</small>


# <lo-sample/> IMO.SHL.2022.G6

Let $ABC$ be an acute triangle with altitude $\overline{AH}$, and let $P$ be 
a variable point such that the angle bisectors $k$ and $\ell$ of $\angle PBC$ 
and $\angle PCB$, respectively, meet on $\overline{AH}$. Let $k$ meet 
$\overline{AC}$ at $E$, $\ell$ meet $\overline{AB}$ at $F$, and 
$\overline{EF}$ meet $\overline{AH}$ at $Q$. Prove that as $P$ varies, 
line $PQ$ passes through a fixed point.


<small>

* questionType:Prove
* domain:Geom

</small>



# <lo-sample/> IMO.SHL.2022.G7

Two triangles $ABC, A’B’C’$ have the same orthocenter $H$ and the same 
circumcircle with center $O$. Letting $PQR$ be the triangle formed by 
$AA’, BB’, CC’$, prove that the circumcenter of $PQR$ lies on $OH$.


<small>

* questionType:Prove
* domain:Geom

</small>


# <lo-sample/> IMO.SHL.2022.G8

Let $AA'BCC'B'$ be a convex cyclic hexagon such that $AC$ is tangent 
to the incircle of the triangle $A'B'C'$, and $A'C'$ is tangent to the 
incircle of the triangle $ABC$. Let the lines $AB$ and $A'B'$ meet at 
$X$ and let the lines $BC$ and $B'C'$ meet at $Y$.

Prove that if $XBYB'$ is a convex quadrilateral, then it has an incircle.


<small>

* questionType:Prove
* domain:Geom

</small>



# <lo-sample/> IMO.SHL.2022.N1

A number is called Norwegian if it has three distinct positive divisors 
whose sum is equal to $2022$. Determine the smallest Norwegian number.

(Note: The total number of positive divisors of a Norwegian number 
is allowed to be larger than $3$.)


<small>

* questionType:FindOptimal
* domain:NT

</small>



# <lo-sample/> IMO.SHL.2022.N2

Find all positive integers $n>2$ such that

$$ n! \mid \prod_{ p<q\le n, p,q \, \text{primes}} (p+q)$$


<small>

* questionType:FindAll
* domain:NT

</small>




# <lo-sample/> IMO.SHL.2022.N3

Let $a > 1$ be a positive integer and $d > 1$ be a positive integer 
coprime to $a$. Let $x_1=1$, and for $k\geq 1$, define

$$x_{k+1} = \begin{cases} 
x_k + d &\text{if } a \text{ does not divide } x_k \\ 
x_k/a & \text{if } a \text{ divides } x_k 
\end{cases}$$

Find, in terms of $a$ and $d$, the greatest positive integer $n$ 
for which there exists an index $k$ such that $x_k$ is divisible by $a^n$.


<small>

* questionType:FindOptimal
* domain:NT

</small>

# <lo-sample/> IMO.SHL.2022.N4

Find all triples $(a,b,p)$ of positive integers with 
$p$ prime and \[ a^p=b!+p. \]


<small>

* questionType:FindAll
* domain:NT

</small>


# <lo-sample/> IMO.SHL.2022.N5

For each $1\leq i\leq 9$ and $T\in\mathbb N$, define $d_i(T)$ 
to be the total number of times the digit $i$ appears when 
all the multiples of $1829$ between $1$ and $T$ inclusive 
are written out in base $10$.

Show that there are infinitely many $T\in\mathbb N$ such that there are 
precisely two distinct values among $d_1(T)$, $d_2(T)$, $\dots$, $d_9(T)$.


<small>

* questionType:Prove
* domain:NT

</small>



# <lo-sample/> IMO.SHL.2022.N6

Let $Q$ be a set of prime numbers, not necessarily finite. 
For a positive integer $n$ consider its prime factorization: 
define $p(n)$ to be the sum of all the exponents and 
$q(n)$ to be the sum of the exponents corresponding 
only to primes in $Q$. A positive integer $n$ is called 
special if $p(n)+p(n+1)$ and $q(n)+q(n+1)$ are both even integers. 
Prove that there is a constant $c>0$ independent of the set 
$Q$ such that for any positive integer $N>100$, 
the number of special integers in $[1,N]$ is at least $cN$.

(For example, if $Q=\{3,7\}$, then $p(42)=3$, $q(42)=2$, $p(63)=3$, 
$q(63)=3$, $p(2022)=3$, $q(2022)=1$.)


<small>

* questionType:Prove
* domain:NT

</small>



# <lo-sample/> IMO.SHL.2022.N7

Let $k$ be a positive integer and let $S$ be a finite set of odd prime numbers. 
Prove that there is at most one way (up to rotation and reflection) 
to place the elements of $S$ around the circle such that the product 
of any two neighbors is of the form $x^2+x+k$ for some positive integer $x$.


<small>

* questionType:Prove
* domain:NT

</small>



# <lo-sample/> IMO.SHL.2022.N8

Prove that $5^n-3^n$ is not divisible by $2^n+65$ for any positive integer $n$.


<small>

* questionType:Prove
* domain:NT

</small>