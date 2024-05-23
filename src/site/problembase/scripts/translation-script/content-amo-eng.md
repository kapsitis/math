# <lo-sample/> LV.AMO.2000.7.1
The $a,b,c,d$ is given as natural numbers and $ab=cd$. Prove that the number $a^2 + b^2 + c^2 + d^2$ can be expressed as the sum of two squares of integers. Surely that can be said as the sum of two squares of natural numbers? 
<small>
* Topic: Standardidentities
* questionType: Prove
* cooked: the Square-ALG
</small> 
# # resolution can add a $2ab$ to an expression and subtract the same $2cd$ from it, and then separate the squares: $$a^2 + 2ab + b^2 + c^2 - 2cd + d^2 = (a+b)^2 + (c-d)^2.$$ Therefore, it can always be expressed as the sum of two squares of integers. The sum of two natural squares may not always be $a^2 + b^2 + c^2 + d^2$. For example, $1^2+1^2+1^2+1^2 = 4$ is not to be expressed as a $m^2 + n^2$ where to $m, n \in \mathbb{N}$.
# <lo-sample/> LV.AMO.2000.7.2
Find the smallest natural number for which all numbers are the same and which shares $49$? 
<small>
* Topic: Littlefermatandeuler
* Topic: Integerfactorization
* Genre: optimization
* questionType: Findoptimal
* cooked: resolution of decimal-NOTATION, digit, divisibility
</small> 
# # # calculates residuals by dividing $1,11,111,1111,11111,111111$ by $7$. The leftovers are $1,4,6,5,2,0$. Therefore, $111111$ shares $7$ and seven times the number $777777$ shares $49$. * Note * the fact that $111111$ shares $7$ follows $7$. The generalisation of this statement is the theorem of small farm: For each pioneer, $p$ and each non-$p$ $a^{p-1} - 1$ share $p$.
# <lo-sample/> LV.AMO.2000.7.4
Can the subsistence numbers * * (P) * * from $1$ to $12$ inclusive, * * (B) * * * from $1$ to $50$ inclusive be paired so that all amounts of numbers entering pairs are different and each is a primary number? (For example, numbers between 1 and 6 could be divided into: $1+2=3$, $3+4=7$, $5+6=11$). 
<small>
* Topic: Primesdistribution
* Topic: Numtheorypigeonhole
* Topic: Exhaustionmethod
* concept: partition, PRIMES, sum
* questionType: Provedisprove
* Genre: Construction
</small> 
# # Resolution * * (R) * * can be divided, for example: $(1,4)$, $(2,5)$, $(3,8)$, $(6,7)$, $(9,10)$, $(11,12)$. * * (B) * * But $(1,100)$ are just $24$ primaries larger than $2$. So it's impossible to make $25$ pairs of numbers in $[1;50]$ so that you get $25$ different primaries -- that would run counter to the Dirichlee principle.
# <lo-sample/> LV.AMO.2000.8.3
Each card has a natural number written on it (which can be the same); the sum of the numbers written on each card is $100$. Can you definitely find cards (maybe alone) on which the sum of the numbers you type is $50$ when the number of cards is * * (P) * * $50$, * * (B) * * $51$? 
<small>
* Topic: Numtheorymathinduction
* Topic: Numtheorypigeonhole
* Genre: construction
* questionType: Provedisprove
* strategy: Interpretation
* cooked: sum
</small> 
# # solution * * (P) * * not always. There is the following counterexample: $49$ cards with “1” and a $1$ card with “51”. * * (B) * * * introduces the following interpretation: We draw a circle whose regular $100$ - corner peaks divide the $100$ into equal circles. First we paint one of the peaks of the regular $100$ - the corner red and, according to the number of each card, $n_i$ ($i=1,2,\ldots,51$) paints a red top separated from the previous one by the same arcs of the $n_i$ (moving counterclockwise). Bending all the $51$ circles, the last red peak will be the one celebrated at the very beginning (because the sum of all number $n_i$ is directly $100$). We've scored a $51$ red dot on the hoops line. All $100$ - corner peaks can be grouped in pairs (where one pair includes two peaks directly opposite each other -- separated by directly $50$ circles). On the Dirichlee principle, in at least one of the pairs, both opposite peaks will be red because the pairs are entirely $50$ (and you can't give each red top a pairing of non-red). The resulting pair with both red peaks, which are right opposite each other as a solution because you can go from one to the other in exactly $50$ steps using numbers in the $n_i$.
# <lo-sample/> LV.AMO.2000.9.2
Can the number * * (P) * * * in $2$, * * (B) * * * in $\frac{1}{8}$ be expressed as the sum of the inverse of four different squares of natural numbers? 
<small>
* Concept: sum, square-ALG, inverse-number
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2000.9.4
We look at the first $n$ subsistence numbers. Two of them must be chosen so that their product is equal to the sum of all other numbers. Is this possible if * * (R) * * * $n=10$, * * (B) * * $n=15$? 
<small>
* cooked: sum, product
* questionType: ProveDisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2000.10.2
The difference between the two primary numbers is $100$. Typing the first at the end of the second gets the prime number again. Find these source numbers and prove that there are no others without what you find. 
<small>
* cooked: PRIMES, digit-manipulation
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2000.11.1
Given that, in the $x^2+y^2+z^2 = t^2$ where the $x,y,z,t$ is made, natural numbers. How many of the numbers in the $x,y,z,t$ can there be even numbers? 
<small>
* cooked: even-number
* questionType: FindCount
</small>
# <lo-sample/> LV.AMO.2000.11.4
The arguments and values in the $f(x)$ function are natural numbers. The uniformity of each natural $x$ $$f(f(x))+f(x) = 2x.$$ you to find all of the following functions in the $f(x)$ and prove that there are no others without those found. 
<small>
* Concept: function, ARGUMENT, value
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2000.12.2
Resolve equation $$\left( 2a+b \right) \cdot \left( 2b + a \right) = 2^c.$$ 
<small>
* concepts: equation
* questionType: FindAll in
</small> natural numbers
# <lo-sample/> LV.AMO.2000.12.5
A string of natural numbers is called $F$ - a string if it's growing, infinite and each Member of it, starting with the third, equals the sum of the two previous members. Is there a * * (P) * * final quantity, * * (B) * * infinite quantity of $F$ - strings with characteristic: each natural number belongs to exactly one of them. 
<small>
* cooked: sequence
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2001.7.2
A natural number is called symmetric if its last digit is not $0$ and the number does not change when you type its digits in reverse order. For example, $1221$ is a symmetric number and $1231$ is not. * * (R) * * prove: if a symmetric six-digit number shares $13$, it also shares $7$, * * (B) * * * is it true that every symmetric six-digit number that shares $7$ also shares $13$? 
<small>
* Topic: Divisibilityrulesother
* Topic: Notationpolynomial
* Topic: Integercongruence
* Concept: palindrome, decimal-NOTATION
* questionType: Prove, ProveDisprove
</small> 
# # solution * * (R) * * $13$ divides $\overline{abcabc}=1001\cdot{}\overline{abc}$ and also $\overline{abccba}$ (this is given). By subtracting both numbers, we get $13 \mid 99|a-c|$ and $a=c$. * * Note: * * We note that $\overline{abccba}$ can be made $100001a + 10010b + 1100c = 13\cdot (\ldots ) + 5(a-c)$. The $a-c$ then shares $13$ and $a=c$; replaces $c$ and divides by $7$. * * (B) * * $108801$ is a counterexample.
# <lo-sample/> LV.AMO.2001.8.3
Andri had to multiply two different positive three-digit numbers. For distraction, he simply wrote them to each other at the end. The resulting six-digit figure proved to be $3$ times the product Andri should have obtained. What six-digit number did Andris write? 
<small>
* Topic: Notationshift
* Topic: Standardidentities
* Topic: Numtheoryinequalitymethod
* questionType: Findall
* Genre: Digit-manipulation
* Concept: decimal-NOTATION
</small> 
# # solution * stands for $a$ and $b$ - both are three-digit numbers * If $1000a+b=3ab$, then $b/a=3b-1000$. * whole three-digit numbers $a,b$ occur only if you $b=334$.
# <lo-sample/> LV.AMO.2001.9.4
Given that $x,y,z$ - natural numbers and each of the numbers $xy-z$, $xz-y$ and $yz-x$ share $3$. Prove $x^2+y^2+z^2$ is sharing $3$. 
<small>
* cooked: divisibility
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2001.10.3
What is the lowest prefix for a $p$ who can't find nonnegative integers like that in a $x$ and $y$ that ${\displaystyle p = \left| 2^x - 3^y \right|}$? 
<small>
* cooked: PRIMES
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2001.11.3
The elements of a number string are natural numbers. The first element shall be chosen arbitrarily, but each subsequent element shall be equal to the number of natural dividers of the previous element. (For example, if the first element of a string is $14$, the string is $14, 4, 3, 2, 2, 2, \ldots$). What can be the first element of a string if none of its elements are a natural number square? 
<small>
* cooked: sequences, divisibility, square-ALG
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2001.12.2
Resolve equation $(2a+b)(2b+a)=2c$ in natural numbers. 
<small>
* cooked: equation
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2002.7.4
Two players write alternately on the board, one natural number at a time, from $1$ to $8$ inclusive. You cannot type numbers that are shared by any number that you have already typed. Who can't make a move loses. Show how whoever makes the first move can win. 
<small>
* Genre: game
* cooked: divisibility
* questionType: Algorithm
* strategy: Contradiction
</small> 
# # resolve If the numbers $\{ 2,3,\ldots,7,8\}$ win sp. 1, resumes his strategy. If player 2 wins, starts with the move “$1$.” the 
# # resolution starts with $2$, then answers each $(5; 7)$, $(6; 8)$ and $(4; 3)$ with a second number from the pair.
# <lo-sample/> LV.AMO.2002.7.5
What greater quantity of different natural numbers than the $100$ can be chosen so that the difference between the two selected numbers is neither $3$, $4$ nor $7$? 
<small>
* Topic: Sequenceperiodicity
* Topic: Numtheorypigeonhole
* Genre: optimization
* questionType: Findoptimal
* strategy: Exhaustivesearch, SYMMETRY
</small> 
# # solution If $>30$, select a $4$ from the $10$, see. $\{1,4,8\}$, $\{2,5,9\}$, $\{7\}$, $\{2,6,10\}$ should be taken by $1$ – impossible. To select $4$ from * ABCABCXABC *, you must also take $X$, but similarly * ABCYABCABC * and $X$, the $Y$ difference is $3$.
# <lo-sample/> LV.AMO.2002.8.2
Andri had to multiply two different double digits. For distraction, he simply wrote them to each other at the end. The resulting four-digit figure proved to be $3$ times the product Andris should have obtained. What four-digit number did Andris write? 
<small>
* Topic: Notationshift
* Topic: Standardidentities
* Topic: Numtheoryinequalitymethod
* seeAlso:LV.AMO.2001.8.3
* questionType: Findall
* Genre: Digit-manipulation
* Concept: resolution of decimal-NOTATION
</small> 
# # If $100a+b=3ab$, then $b/a=3b-100$. Both digits $a,b$ be whole if you $b=34$.
# <lo-sample/> LV.AMO.2002.8.3
Fibonacci numbers are called $1; 2; 3; 5; 8; \ldots$ numbers (each coming one is obtained by adding up the previous two). Can there be equality in $a+b=c+d$ when $a$, $b$, $d$, $c$ have different Fibonacci numbers? 
<small>
* Topic: Numtheoryextremeelement
* cooked: Fibonacci-sequence
* questionType: Provedisprove
* strategy:
</small> Resolution of extremeelement 
# # If the $d$ is the largest of the Fibonacci numbers, then the Fibonacci numbers just before the $d$ are $a+b=d$ in the $b$ where you $a$. But since $c>0$ is also a Fibonacci figure, then $a+b<c+d$.
# <lo-sample/> LV.AMO.2002.9.3
Given that $x, y, z$ natural numbers and each of the numbers $xy-z$, $xz-y$ and $yz-x$ share $3$. Prove $x^2+y^2+z^2$ shares $3$. 
<small>
* seeAlso:LV.AMO.2001.9.4
* Concept: divisibility
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2002.10.3
Each natural number is painted in the same color. It is known that if the difference between two natural numbers is a primary number, they are painted in different colours. What is the lowest possible number of colors? 
<small>
* cooked: PRIMES
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2002.11.3
A natural number is known to $n$ share the primary number $p$ and $p>\sqrt{n}$. To show that no $n-1$, $n^3-1$ is not the product of two natural numbers whose difference is $2$. 
<small>
* Concept: PRIMES
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2002.12.4
A series of numbers in the $a_1, a_2, a_3, \ldots$ is composed of the following $a_1=0$; $a_2=1$; at the $n>2$, the number $a_n$ is obtained by writing down the number $a_{n-1}$ at the right end of the number $a_{n-2}$. (For example, $a_3=10$; $a_4=101$, $a_5=10110$, etc.) What $n$ does $a_n$ share with $11$? 
<small>
* concepts: sequences
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2003.7.3
Two players write alternately on the board, one natural number at a time, from $1$ to $9$ inclusive. You cannot type numbers that are shared by any number that you have already typed. Who can't make a move loses. Show how whoever makes the first move can win. 
<small>
* Genre: game
* cooked: divisibility
* questionType: Algorithm
* strategy: Contradiction
</small> 
# # resolve If player 1 wins the numbers $\{ 2,3,\ldots,8,9\}$, repeats his strategy. If player 2 wins, starts with the move “1.” the 
# # resolution starts with $2$, then in each group, $(5;7)$, $(3;8)$ and $(4;6;9)$ win in isolation.
# <lo-sample/> LV.AMO.2003.7.5
All the subsistence numbers from $1$ to $n$ inclusive are written on the board from time to time. With one go, you can select two numbers written on the board (let's label them $a$ and $b$), clear them, and write $\left| a^2-b^2 \right|$ instead. One figure remains on the board after a $n-1$ move. Can it be $0$ if * * (R) * * * $n=8$, * * (B) * * $n=9$? 
<small>
* Topic: Invariantparity
* Topic: Seriesmemberssumsclosedformulae
* Topic: Exhaustionmethod
* cooked: absolute-value
* Genre: making-moves
* questionType: Algorithm
* strategy: Invariant
</small> 
# # Recommendation in a set of numbers you can find with programming features the least you can get with these moves. 
# # Resolution * * * (R) * * at the $n=8$, the original set of numbers is $\{ 1,2,3,4,5,6,7,8 \}$. We make the following moves: * $(4,5) \rightarrow 5^2 - 4^2 = 9$, new numbers are $\{1,2,3,6,7,8,9\}$, * $(7,9) \rightarrow 9^2 - 7^2 = 32$, new numbers are $\{1,2,3,6,8,32\}$, * $(2,6) \rightarrow 6^2 - 2^2 = 32$, new numbers are $\{1,3,8,32,32\}$, * $(1,3) \rightarrow 3^2 - 1^2 = 8$, new numbers are $\{8,8,32,32\}$, * $(8,8) \rightarrow 8^2 - 8^2 = 0$, new numbers are $\{0,32,32\}$, * $(32,32) \rightarrow 32^2 - 32^2 = 0$, new numbers are $\{0,0\}$, * $(0,0) \rightarrow 0^2 - 0^2 = 0$, remain number $\{ 0 \}$. * * (B) * * If $n=9$, then the sum of all numbers is $1+2+\ldots+9=45$. When you make a move (by deleting the $a$ and $b$ and typing the $\left| a^2-b^2 \right|$), the parity of the amount does not change. Therefore, after each step, the sum of all the numbers on the board will be an odd number.
# <lo-sample/> LV.AMO.2003.8.3
In what greater quantity of different natural totals, all larger than $1$, can you split a number into $56$ so that the largest common divisor of each two counts is $1$? 
<small>
* Topic: Numtheoryextremeelement
* Topic: Primesdistribution
* Genre: optimization
* cooked: GCD, coprimes
* questionType: Findoptimal
* strategy:
</small> The resolution of the 
# # extremeelement with a sum of six can be $56$ as follows: $3,5,7,11,13,17$. You can't add up to seven or more because even if you choose all seven of the smallest primaries, their amount is $2+3+5+7+11+13+17 = 58 > 56$.
# <lo-sample/> LV.AMO.2003.8.5
Each of the two pages shall bear positive $n$ numbers. All numbers you type in the $2n$ must be different. In addition, the amounts of the numbers written on the pages must be the same with each other, and the square amounts of the numbers written must also be the same with each other. Is this possible if * * (R) * * * $n=3$, * * (B) * * $n=4$, * * (C) * * $n=2003$? 
<small>
* Topic: Sequenceperiodicity
* Topic: Exhaustionmethod
* Topic: Standardidentities
* cooked: quare
* questionType: Provedisprove, ProveDisprove, ProveDisprove
* strategy: The solution
</small> for Symmetric 
# # # * * (R) * * looks at two groups: $\{ 1,5,6 \}$, $\{ 2,3,7 \}$. In both groups, the number amounts are $12$, but the square amounts are $62$. * * (B) * * We look at the group $(1,4,6,7)$, for $(2,3,5,8)$. * * (C) * * * You can also do this for this value $n = 2003$. Let's be guided by the induction that you can do this for each $n = 4m+3$ if the $m \geq 0$ is an integer. * Base: * These $n=3$ can be made as in * * (a) * *. * inductive assumption: * Let's say you can do this for a value in the $n=3+4m$. Let's say you can also do more: $n=3+4(m+1)$. * inductive transition: * Divides the first $3+4m$ numbers according to the inductive assumption. We $k$ the largest of the numbers used in this construction. Let's add eight new numbers by dividing them into groups (similar to * * (b) * *): $$(k+1, k+4, k+6, k+7)\;\;\text{un}\;\;(k+2, k+3, k+5, k+8)$$. All of these eight numbers are different from each other. * in one group, the amount is $(k+1) + (k+4) + (k+6) + (k+7) = 4k + 18$. The same amount is found in the second group: $(k+2) + (k+3) + (k+5) + (k+8)$. * in one group, the sum of squares is $(k+1)^2 + (k+4)^2 + (k+6)^2 + (k+7)^2 = 4k^2 + 36k + 102$. Also in the other group: $(k+2)^2 + (k+3)^2 + (k+5)^2 + (k+8)^2 = 4k^2 + 36k + 102$. So when you add the new two groups to each of your sides, both the sum of numbers and the sum of their squares will still match.
# <lo-sample/> LV.AMO.2003.9.3
Find out which different source numbers $p_1, p_2, \ldots, p_n$ have a characteristic: $p_1p_2p_3\ldots{}p_n$ shares $(p_1-1)(p_2-1)\ldots(p_n-1)$. 
<small>
* cooked: PRIMES, divisibility
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2003.10.3
Given that $n$ - a whole positive number and numbers $2n+1$ and $3n+1$ are squares of integers. * * (R) * * Find one such $n$, * * (B) * * can $5n+3$ be a primary? 
<small>
* Concept: PRIMES, square-ALG
* questionType: Findexample, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2003.11.3
Is there a natural number $n$ that $6^n-1$ shares $4^n-1$? 
<small>
* Concept: divisibility
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2003.12.2
Is there such a positive whole number in $n$ that the number $n^2$ has as many subsistence dividers that give the remainder to $1$ divided by $3$ as a subsistence divider that gives the remainder to $2$ divided by $3$? 
<small>
* cooked: divisibility, divisor
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2004.7.3
For what smaller subsistence $n$ are all part $$\frac{5}{n+7}, \frac{6}{n+8}, \frac{7}{n+9}, \ldots, \frac{35}{n+37}, \frac{36}{n+38}$$ unshort? 
<small>
* Topic: Euclideanalgorithm
* Topic: Primesdistribution
* cooked: for fractions, GCD
* questionType: Findoptimal
</small> 
# # solution uses the Euclide algorithm. * all parts look like this: $\frac{k}{n+(k+2)}$ * must be $\mbox{LKD}(k,n+(k+2))=1$. * $\mbox{LKD}(k,n+(k+2))=\mbox{LKD}(k,n+2)=1$, $k=5,\ldots,36$. $n+2=37$ is a cross-primary number with all $k$, i.e. $n=35$.
# <lo-sample/> LV.AMO.2004.8.3
Given that $A$ and $B$ are natural double digits. The number $X$ is obtained by writing down the number $B$ at the end of the $A$. the number $Y$ is obtained by writing down the number $A$ at the end of the $B$. $X-Y$ is given to share $91$. Prove $A=B$. 
<small>
* Topic: Notationshift
* Topic: Integerfactorization
* Concept: decimal-NOTATION, divisibility
* Genre: Digit-manipulation
* questionType: Prove
</small> 
# # resolve $(100A+B)-(100B+A) = 99(A-B)$ and $A-B$ share $91$. For double digits, that means $A=B$.
# <lo-sample/> LV.AMO.2004.8.5
A series of ascending natural numbers from $1$ to $2004$ inclusive, each once. We remove the numbers in the $1., 4., 7., 10., \ldots$ places from it. Again, we remove the numbers in the remaining string from the $1., 4., 7., \ldots$. We treat the resulting string the same way, etc., until one number remains uncrossed. Who is that? 
<small>
* Topic: Multiplesininterval
* Topic: Definingrecurrentsequences
* Topic: Nonlinearrecurrences
* cooked: sequence
* Genre: making-moves
* questionType: Findall
* strategy: Workingbackwards
</small> 
# # resolve before the last strikeout, the last number was\ #2, before that\ #3,\ #5,\ #8,\ #12, etc. * * #GoodParlasse * * After deleting the $n$, the first remaining is $x_n$. The $x_n$ of $x_{n+1} = \left\lceil 3x_n/2 \right\rceil$ couples and odd couples shall be justified.
# <lo-sample/> LV.AMO.2004.9.5
The square consists of $n \times n$ boxes. In each box, you type one of the numbers in the $-1; 0; 1$ so that the amounts of the numbers that you type in the $n$ rows and $n$ columns are all different. Can you do this if * * (R) * * * $n=4$; * * (B) * * $n=5$? 
<small>
* cooked: sum
* questionType: ProveDisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2004.10.3
Given that the $n$ is a natural number. * * (R) * * to prove that the $n^2 + 11 n + 30$ is not a natural number, * * (B) * * to find the first decimal place of this number, depending on the $n$. 
<small>
* questionType: Prove, FindAll
</small>
# <lo-sample/> LV.AMO.2004.10.5
Can you write $16$ three-digit numbers using only $3$ different digits, all of which give different residuals divided by $16$? 
<small>
* cooked: remainder, divisibility
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2004.11.1
Is there a natural number $n$ that $2004^n-1$ shares $1500^n-1$? 
<small>
* Concept: divisibility
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2004.12.1
Given that $n$ is a natural number, $n>1$. Can the expression $$\left( x^n + x^{n-1} + \ldots + x + 1 \right)^2 - x^n$$ necessarily be expressed as a product of two polynomials so that none of these polynomials are constant and all of the coefficients of both polynomials are integers? 
<small>
* Concept: Integer-polynomial
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2004.12.3
The $f(n)$ function has both arguments and values as natural numbers, and every two natural numbers in the $x$ and $y$ have the same $$xf(y)+yf(x)=(x+y)f(x^2+y^2).$$ to find all of the following functions in the $f$ and prove that there are no others without what you find. 
<small>
* Concept: function, ARGUMENT, value
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2004.12.4
We $n$ an arbitrary odd natural number greater than $1$. Prove: both numbers in $n$ and $n+2$ are both primary numbers at the same time and only if the $(n-1)!$ does not share $n$ or $n+2$. 
<small>
* Concept: PRIMES, divisibility
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2005.7.4
The sum of three positive integers is $407$. What is the biggest amount of nuts that can end up multiplying these numbers? 
<small>
* Topic: Divisibilityruleslastdigits
* Topic: Modularithmetic
* Genre: optimization
* cooked: decimal-NOTATION
* questionType: Findoptimal
* seeAlso:LT.VILNIUS.2008.12.1
</small> 
# # solution we notice that $407 = 250+125+32$, then $p = 1000000$. Let's justify that you can't get even more nuts. * two counts can't end with a “5” because what's left then has to end with a “7.” So at least one count will end in zero. * more than six $5$ - you can't get first-time multipliers ($125=5^3$ and $250=5^3\cdot{}2$ are optimal).
# <lo-sample/> LV.AMO.2005.8.3
How can you split subsistence numbers from 1 to 9 into two parts so that the sum of all numbers in one part is equal to the sum of all numbers in the other part? 
<small>
* Topic: Treetraversalbacktracking
* cooked: partition
* Genre: construction
* questionType: Findexample
* strategy:
</small> Resolution of caseanalysis 
# # If $a,b,c$ are multiplied, you can $abc=32$ and $a+b+c=45-32=13$. $(a,b,c)=(1,4,8)$.
# <lo-sample/> LV.AMO.2005.9.1
Find the smallest subsistence number that shares $225$ and does not use any of the digits $3; 4; 5; 6; 7; 8; 9$ in the decimal note. 
<small>
* Concept: divisibility decimal-NOTATION
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2005.10.3
For which subsistence numbers do the $n$ two numbers $2^n-1$ and the $2^n+1$ have primary numbers? 
<small>
* Concept: PRIMES
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2005.10.4
The definition area and value area of the $f(t)$ function are set $\{ 1; 2; \ldots; n\}$, and all values are different. Is it possible that all numbers $f(x)-x$, for $x=1; 2; \ldots; n$, are different if * * (R) * * $n=15$, * * (B) * * $n=16$? 
<small>
* cooked: function
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2005.11.4
Given that $a < b \leq c < d$ have positive whole numbers, $ad=bc$ and $d - a \leq 1$. Prove the $a$ is an integer square. 
<small>
* cooked: square-ALG
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2005.12.1
Is there such a positive whole number $n$ that the number $n^2$ has as many natural dividers that give the remainder to $1$ divided by $3$ as a natural divider that gives the remainder to $2$ divided by $3$? 
<small>
* seeAlso:LV.AMO.2003.12.2
* Concept: divisibility, remainder
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2005.12.5
Two players play a subsequent game, making moves in a row. At first two bars are given: one with a length of $n$, the other with a length of $n+1$ ($n$ - positive integer). With one move, you can either break one bar in two shorter lengths of positive integers, or you can exclude $k$ bars, each of which has a $k$ length, from going forward in the game (for $k$, any positive integer). The player who makes the final move wins. Which player wins by playing properly? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2006.7.1
On the Riga-Mexico City train, the places are numbered with natural numbers starting with $1$ (numbering is uniform for the whole train, i.e. there is only one place with the number $1$, one place with the number $2$ etc; numbers allocated from locomotive to train tail). All wagons shall have the same number of seats. Spaces with numbers for $1996$ and $2015$ shall be in the same wagon and spaces with numbers for $630$ and $652$ in different wagons which are not adjacent to each other. How many seats do each wagon have? 
<small>
* Topic: Seriesmemberssumsclosedformulae
* Topic: Sequencegaps
* Topic: Exhaustionmethod
* cooked: sequence
* questionType: Findall
</small> 
# # Resolution * number of seats per $k \leq 22$ (because $1996$ and $2015$ are in the same wagon) * number of seats per $k \geq 21$ (for $630$ and $652$, in different wagons which are not adjacent to each other). * the $1995$ or $1994$ must share the $k$, because this place ends with another wagon.
# <lo-sample/> LV.AMO.2006.8.3
In the $x$ of a natural number, we'll refer to the sum of the digits as $S(x)$. Let's say $n$ - a natural number that simultaneously performs the $S(n)=10$ and $S(5n)=5$ properties. * * (R) * * Find even one such number, * * (B) * * are there infinitely many? * * (C) * * * are any such numbers odd? 
<small>
* topic:DivisibilityRulesFor2And4
* Topic: Notationinsert
* Genre: special-numbers, sum-of-digits
* questionType: Findexample, ProveDisprove, ProveDisprove
* strategy: Trialanderror
</small> 
# # solution raised example (the number of pairs decreases twice when multiplied by $5$). * * (R) * * $22222$ der * * (B) * * You can insert a $0$ (including $64\cdot 10^k$ der) in the middle of the $22222$. * * (C) * * * If the odd $n$, the $5n$ would end in $5$, it is not possible because you $n \neq 1$.
# <lo-sample/> LV.AMO.2006.9.1
What is the highest possible amount of digits for a seven-digit natural number that shares $8$? 
<small>
* cooked: sum, divisibility
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2006.9.5
We look at subsistence numbers from $1$ to $100$ inclusive. What greater quantity of these can be chosen so that no two selected numbers share each other and for each two selected numbers the largest common divider is greater than $1$? 
<small>
* cooked: for divisibility, GCD
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2006.10.3
It is given that multiplying all subsistence numbers from $1$ to $33$ inclusive gives you the $$86833176188xy8864955181944012zt000000,$$ where $x, y, z, t$ are numbers. Find out the $x$, $y$, $z$, and $t$ values. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2006.11.2
Given that $a<b \leq c < d$ have positive whole numbers, $ad = bc$ and $\sqrt{d}-\sqrt{a} \leq 1$. Prove the $a$ is an integer square. 
<small>
* cooked: square-ALG
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2006.12.1
Is there such a positive whole number in $n$ that the number $n^2$ has as many subsistence dividers that give the remainder to $1$ divided by $3$ as a subsistence divider that gives the remainder to $2$ divided by $3$? 
<small>
* cooked: divisibility, divisor, remainder
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2007.7.1
What larger number of different digits can be written around a circle so that every two digits next to each other, read in any direction, make up a prenumbered note? 
<small>
* Topic: Hamiltoncircuits
* Topic: Primesdistribution
* Genre: optimization
* cooked: PRIMES
* questionType: Findoptimal
* seeAlso:LV.AMO.2008.7.2
</small> 
# # solution is looking for a loop in the graph. Possible couples $(1,3)$, $(1,7)$, $(3,7)$, $(7,9)$. $4$ - There is no cycle because only one neighbor $9$. $3$ - cycle $1-3-7-1$.
# <lo-sample/> LV.AMO.2007.7.3
$6$ two-digit natural numbers are written on the board at the beginning. Andris can add some numbers to the $1$ with his move, while the rest of the numbers $2$. (You can also add all numbers to the $1$ or to all numbers in the $2$.) Maya can then clear any number that shares $7$ or has a sum of digits divided by $7$ with her move. The move is then made by Andris, then by Maya, etc. Prove that May can get the numbers on the board to no longer exist (let's say playing long enough). 
<small>
* Topic: Sequencegaps
* Topic: Infinitedescent
* cooked: decimal-NOTATION, divisibility, sum-of-digits
* Genre: game
* questionType: Prove
</small> 
# # the solution is endless many “erasure couples”. For couples, $(160;161)$, $(167;168)$, $(105;106)$, $(175;176)$, etc. Andris can't get over it.
# <lo-sample/> LV.AMO.2007.8.3
Juliata thought of a natural number, multiplied all its digits, and multiplied the result with the imaginary number. Juliata gained $1716$ as a result of the end. What figure did she think at first? 
<small>
* Topic: Canonicalfactorization
* Topic: Numtheoryinequalitymethod
* Concept: decimal-NOTATION
* Genre: Digit-manipulation
* questionType: Findall
</small> 
# # Resolution breakdowns: $1716=2^2 \cdot 3 \cdot 11 \cdot 13$ * But numbers $11$ and $13$ are not numbers. * all replies are in the $11 \cdot 13 \cdot k$ form.
# <lo-sample/> LV.AMO.2007.9.1
A square table consists of $10 \times 10$ boxes. Each box contains a nonzero number. One ten-digit natural number is created from the numbers of each line and each column in arbitrary order. Can it happen that exactly $19$ of these numbers (no more and no less) share $3$? 
<small>
* cooked: divisibility
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2007.9.3
* * (A) * * Each of the natural numbers in $a$ and $b$ is expressed as the sum of two squares of integers. Prove that the product is also pronounced as follows. * * (B) * * Find two polynomials with whole coefficients for $f(x)$ and $g(x)$ that all $x$ have the same $$\left( f(x) \right)^2 + \left( g(x) \right)^2 =$$ $$= \left( x^2+1 \right)\left( x^2 + 4 \right)
\left(x^2 + 2x + 2 \right)\left( x^2 - 2x + 2 \right).$$ 
<small>
* cooked: sum, square-ALG, equation
* questionType: Prove, FindExample
</small>
# <lo-sample/> LV.AMO.2007.10.1
A ten-digit natural number divides by $999\,999$. Can it also share $1\,000\,001$? 
<small>
* seeAlso:LV.AMO.2008.10.1
* cooked: divisibility
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2008.8.1
What is the largest number of different digits that can be written around a circle so that every two digits next to each other, read in any direction, form a prenumbered note? 
<small>
* seeAlso:LV.AMO.2007.7.1
* Concept: PRIMES
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2008.7.2
It is given that $x$ and $y$ - natural numbers such as $x \cdot y = 10^{12}$. Can neither $x$ nor $y$ contain any digital $0$ in their note? 
<small>
* Topic: Divisibilityruleslastdigits
* Topic: Standardidentities
* cooked: decimal-NOTATION
* questionType: Provedisprove
</small> 
# # solution No. We use a 10 ^ 12 split in first-time $x$ or $y = 2^{12} = 4096$. (Or $2$ and $5$ will multiply.)
# <lo-sample/> LV.AMO.2008.8.3
Given that $n>1$ is a non-primary natural number. Demonstrate that at least three different natural numbers can be found in the $a_1,a_2,\ldots,a_k$ satisfying the relationship $$a_1 + a_2 + \ldots + a_k = n \cdot \left( \frac{1}{a_1} + 
\frac{1}{a_2} + \ldots + \frac{1}{a_k} \right).$$ 
<small>
* Topic: Divisornumberandsum
* Topic: Integerfactorization
* Topic: Telescopicsums
* cooked: PRIMES, series
* questionType: Prove
</small> 
# # Resolution * pairs $a_1a_k = a_2a_{k-1} = \ldots = n$ (and $k \geq 3$). * Then $a_1 + \ldots + a_k = a_k + \ldots + a_1$. $$1+3+9 = 9 \cdot \left( \frac{1}{1} + \frac{1}{3} + \frac{1}{9} \right). $$
# <lo-sample/> LV.AMO.2008.9.1
A square table consists of $12 \times 12$ boxes. Each box contains a nonzero number. One twelve-digit natural number is created from the numbers of each line and each column in arbitrary order. Can it happen that exactly $23$ of these numbers (no more and no less) share $3$? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2008.9.4
The natural numbers from $1$ to $2008$ inclusive shall be divided into groups in such a way that the relationship is fulfilled: if $a$ shares $b$ and $b$ shares $c$ ($a$, $b$, $c$ - different natural numbers), then $a$, $b$, and $c$ do not all belong to the same group. What is the lowest possible number of groups
<small>
?
* concepted: groups
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2008.10.1
A ten-digit natural number divides by 9,999,999. Can it also share 10,000,001? 
<small>
* seeAlso:LV.AMO.2007.10.1
* cooked: divisibility
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2008.10.4
The $50$ cards contain natural numbers from $1$ to $50$ inclusive (each number on another card). There are $2008$ boxes in the row behind each other. The cards are somehow placed on the $50$ boxes (no more than one card on each box). If the box on the right-hand side of a $n$, $1 \leq n < 50$, card $n$ is free, it is allowed to move the card $n+1$ to this free box. it's called one move. Prove you can't do more than $1250$ moves. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2008.11.2
The $f(n)$ function is defined for all whole $n$ and accepts whole values. All healthy $x$ and $y$ have the same $$f(f(x) + y) = x + f(y+2008).$$ to find all such functions $f$ and prove that there are no others without what you find. 
<small>
* Concept: function, equation
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2008.11.3
Given that $n$ is a natural number. Find out: * * (B) * * can it happen that different natural dividers are directly $10$ to the number $n^2 - 1$? * * (B) * * can it happen that different natural dividers are directly $10$ to the number $n^2 - 4$ if the $n$ is a pair number? 
<small>
* Concept: divisor
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2008.12.2
For some natural $n$, a set of numbers can be divided into two parts so that the following conditions are met simultaneously: a. Each number would end up in exactly one part, b. both parts would have the same number, C. the arithmetic mean of all numbers in each part would also belong to that part? 
<small>
* Concept: arithmetic-mean
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2008.12.4
Are there three natural numbers, all larger than the $1$, having a characteristic: the square of each number, reduced by $1$, shares each of the other two numbers? 
<small>
* cooked: divisibility, square-ALG
* questionType: The provedisprove
</small> # LV.AMO.2009.7.2 triangle $T$ has all sides of different lengths. All you know about the dots $M$ and $N$ is that they are inside the triangle $T$. * * (R) * * can a notch $MN$ longer than two sides of the $T$? * * (B) * * can a notch $MN$ longer than all sides of the $T$? 
<small>
* cooked: triangle
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2009.7.3
The table consists of $3 \times 3$ boxes. The boxes contain natural numbers from $1$ to $9$ (each box contains a different number). The amounts of numbers in rows and columns are all different. What's the biggest amount these amounts can be in the primaries? 
<small>
* Topic: Modularparity
* Topic: Primesdistribution
* Topic: Seriesmemberssumsclosedformulae
* Topic: Exhaustionmethod
* cooked: PRIMES, sum, table, row, column, natural-numbers
* Genre: ill-in-table
* questionType: Findoptimal
* isHard: true
</small> 
# # solution never pairs as a pentomino “V”. $(5,6,4)$, $(9,8,2)$, $(7,3,1)$. Cannot be $p_1+p_2+p_3=45$.
# <lo-sample/> LV.AMO.2009.7.4
The triangle $ABC$ is narrow-angle. The triangles $AMB$ and $BNC$ are both equilateral and are outside the $\bigtriangleup ABC$. Prove you $AN=CM$'t.! [LV.AMO.2016.7.3] (Geometry-grade07/LV.AMO.2009.7.4.png) 
<small>
* cooked: triangle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2009.7.5
Several gnomes have the same amounts of money. From time to time, one of the gnomes takes some of his money and divides it into equal parts for the others. After a while it turned out that one of the gnomes had $8$ Dahler and another had $25$ Dahler. How many gnomes are there? (Daller is the only currency available to the Dwarfs.) 
<small>
* Topic: Invariantremainder
* cooked: divisibility
* Genre: making-moves
* questionType: Findall
</small> 
# # solution If the Dwarfs are $a$ by redistributing the $k$ Dahlders, the difference between the amounts of money from the donor and the recipient varies by $(a-1)k+k = ak$. If at first the difference was $0$, but the closing difference is $17$, then $a=17$.
# <lo-sample/> LV.AMO.2009.8.4
Professor number arrived with his foreign counterpart at a Christmas tree event attended by university staff, their friends, family members, acquaintances, etc. Pointing to the three guests, the number commented: “the product of these people's ages is $2450$ and the amount is twice your age.” The colleague replied: “I don't know and can't find out how old these people are.” The number then added: “I'm older than anyone else on this tree.” Now a colleague immediately told the ages of those $3$ guests. How many years did Zipparins have at the time and how many years did his colleague have? (All ages are expressed in whole years.) 
<small>
* Topic: Canonicalfactorization
* Topic: Exhaustionmethod
* Genre: word-problem
* isHard: true
* questionType: Findall
</small> 
# # resolution for colleague response 1 matches $(5,10,49)$ or $(7,7,50)$. The second remark by Professor Chipper does not allow them to be distinguished.
# <lo-sample/> LV.AMO.2009.9.4
In the $n$ of a natural number, we refer to the number of positive dividers as $d(n)$. For example, $d(1)=1$; $d(6)=4$, etc. Let's call a number $n$ plump if it shares $d(n)$. * * (R) * * Find five plump numbers, * * (B) * * prove that plump numbers are infinitely abundant. 
<small>
* Concept: divisor
* questionType: Findexample, prove
</small>
# <lo-sample/> LV.AMO.2009.10.2
Given that $p$ and $q$ have two odd primary numbers following each other (e.g. $13$ and $17$). Prove: you can divide the number $p+q$ into three subsistence numbers that are all larger than the $1$ (these three numbers can also be the same). 
<small>
* Concept: PRIMES
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2009.11.2
OP! $n$ players ($n \geq 2$) are in attendance. The game takes place for days. Every day one player wins and the others lose. Conscious of the rules in $i$ - on that day ($i = 1, 2, \ldots$) the winner scores $i(n-1)$, while each loser loses by $i$ points. Everyone has $0$ points at the start of the game. After what small number of days can it happen that everyone has $0$ points again? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2009.11.3
Given that $a$ and $b$ - natural numbers and the last digit of the number $S = a^2 + ab + b^2$ are $0$. What is the penultimate digit of a number $S$? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2009.12.3
Given that $n$ - a natural couple number. We look at the product $$R = n(n + 1)(n + 2)(n + 3).$$ * * (P) * * can it be that the $R$ has a square of a natural number? * * (B) * * can it be that the $R$ has a cube of a natural number? 
<small>
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2009.12.5
There are $n$ sweets on the table, $n$ a natural number. Two players alternately eat through $x^2$ candy, where $x$ -- a natural number (the $x$ can change from a move to a move). What has nothing to eat loses. Prove: There are infinitely many such $n$ that when you play properly, the second player can win. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2010.7.1
Five different source numbers, not exceeding $100$, are written on the board. They are known to be $7$ 1. 2. the third is $4$ greater than the fifth; 3. for a number obtained by multiplying the fourth by the fifth, all the digits are the same; 4. the first and fourth amounts to a five-fold second. Find all these numbers! 
<small>
* Topic: Primesdistribution
* Topic: Primesdistribution
* Topic: Canonicalfactorization
* cooked: PRIMES
* Genre: construction
* questionType: Findall
* strategy: Caseanalysis
</small> 
# # solution (a) $p_1=7$, (b) $p_5 \neq 11$, (d) $p_4 \neq 11$, (c) $p_4 p_5 = 3 \cdot 37$, (d) $p_4 \neq 37$. So $(7,2,41,3,37)$.
# <lo-sample/> LV.AMO.2010.7.2
Through the $ABC$ peak of the triangle, the straight line drawn $t$ divides the triangle $A$ into two equal triangles. Could $AB>AC$ happen? 
<small>
* cooked: equal-triangles
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2010.7.3
Records tables with dimensions $4 \times 4$ the boxes in each box for one natural number so that the following two characteristics can be met at the same time: 1. all recorded figures are different; 2. the sum of any four numbers, no two of which are in either row or column, is $2010$. It's enough to show you one way you can do it. 
<small>
* Topic: Linearsystemsapplications
* Topic: Treetraversalbacktracking
* Genre: construction
* questionType: Findexample
* Genre: magic-Construction
</small> 
# # Resolution Count 2 Tables: $((1,2,3,4),\ldots,(1,2,3,4))$ and $(0,\ldots,0),(4,\ldots,4),(996,\ldots,996),(1000,\ldots,1000)$.
# <lo-sample/> LV.AMO.2010.7.4
Several children all have the same number of candy. Occasionally, one of the children picks up some of their candy and divides it into equal parts for the others. After a while, it turned out that one of the children had $4$ candy and another had $23$ candy. How many children? (The sweets are not divided into parts, eaten or discarded.) 
<small>
* Topic: Invariantremainder
* questionType: Findall
</small> 
# # solution If a child is $a$ by redistributing $k$ candy, the difference changes by $(a-1)k+k = ak$. If the difference in the number of two children's sweets is $19$ after a while, then $a=19$.
# <lo-sample/> LV.AMO.2010.8.1
Inserts arithmetic action marks (“$+$”, “$25$”, “$:$”, “$-$”, “$\cdot$”) and parentheses between the numbers, without changing their order, so that the value of the resulting expression is * * * ((B) * * $24$. Can you do that? 
<small>
* Topic: Algorithmsonsyntaxtrees
* questionType: Provedisprove, ProveDisprove
</small> 
# # solution * * (R) * * $(6 + 1) \cdot 3 + 4 = 25$; * * (B) * * * $6 : (1 - 3:4)=24$.
# <lo-sample/> LV.AMO.2010.8.2
Andris and Juris each choose three consecutive natural numbers in such a way that all six numbers are different. Every Andri number was multiplied by every Juris number, got nine multiplications. Show that among the nine numbers you get, at least eight will be different from each other! 
<small>
* Topic: Numtheoryexprforconcepts
* Topic: Exhaustionmethod
* questionType: Prove
</small> # solution If you have fanciful $(a-1,a,a+1)$ and $(b-1,b,b+1)$, 2 equal multiplications can occur only if you $b \pm 1 = 2a$ or $a \pm 1 = 2b$.
# <lo-sample/> LV.AMO.2010.9.1
Natural numbers from $1$ to $2N$ should be divided into $N$ pairs so that the sum of each pair's numbers is a primary number, and these $N$ amounts should be different. Can you do this if * * (R) * * * $N = 5$; * * (B) * * $N = 10$? 
<small>
* cooked: PRIMES, sum
* questionType: ProveDisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2010.9.3
In the $n$ of a natural number, we refer to the number of positive dividers as $d(n)$. For example, $d(1)=1$; $d(6)=4$, etc. Let's call a number $n$ plump if it shares a $d(n)$. * * (R) * * Find five plump pairing numbers, * * (B) * * prove that plump pairing numbers are infinitely abundant. 
<small>
* baked: divisor
* questionType: Findexample, prove
</small>
# <lo-sample/> LV.AMO.2010.9.4
in a large square of the $2010 \times 2010$ box, starting with the lower left box, you type the subsistence numbers in turn, as shown in the drawing (one number is typed in each box). For example, the number $19$ entered in the fourth row, in the third column. * * (R) * * * which number is entered in row 20, column 10? * * (B) * * 
<small>
* which row and which column contains the box that contains the number $2010$?! [Quadrant] (LV.AMO.2010.9.4.png)
* questionType: Findall, FindAll
</small>
# <lo-sample/> LV.AMO.2010.10.4
How many different ways can a number $2010$ be expressed as the sum of at least two consecutive natural numbers? The order of the counts is irrelevant. 
<small>
* Topic: Seriesmemberssumsclosedformulae
* Topic: Canonicalfactorization
* Topic: Exhaustionmethod
* questionType: Findcount
* cooked: sum, consecutive-numbers
</small>
# <lo-sample/> LV.AMO.2010.11.1
Three arithmetic progressions are given: (1) $8, 19, 30, 41, 52, \ldots$ (2) $8, 21, 34, 47, 60, \ldots$ (3) $4, 21, 38, 55, 72, \ldots$ (a) Find the smallest number belonging to all three given strings! (b) Specify that there are infinite numbers belonging to all three given strings! 
<small>
* Concept: arithmetic-progression, sequence
</small>
# <lo-sample/> LV.AMO.2010.11.4
The number $2010$ is written on the board. Two players play the following game. In one move, you must select one of the $N$ dividers of the number currently written on the board in the $d > 1$, subtract it from the $N$, delete the $N$ from the board, and write the resulting difference in the $N-d$ instead. Moves shall be made in turn. The one who gets the $0$ loses. Which player, playing correctly, will win -- whoever starts or whoever makes the second move? 
<small>
* cooked: divisor
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2010.12.3
Find all such natural numbers $n$ that numbers $n$, $d(n)$, and $d(d(n))$ form a descending arithmetic progression. ($d(x)$ is the number of natural dividers $x$ by a number.) 
<small>
* Concept: arithmetic-progression, divisor
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2010.12.5
There are $n$ biscuits on the table, where $n$ is a natural number. Two players alternately eat through $x^3$ biscuits, where $x$ -- a natural number ($x$ may vary for different moves). What has nothing to eat loses. Prove it: There are infinitely many such $n$ that when you play properly, the second player wins! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2011.5.1
In the multiplication example, the numbers were replaced by letters and the expression $$AB \cdot CD = EEE.$$ was obtained. Restores the original multiplication example if the same letters are known to represent the same numbers and different letters to different numbers, and neither $A$ nor $C$ is $0$. Find all possible solutions! 
<small>
* Topic: IntegerFactorization
* Topic: ExhaustionMethod
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2011.5.2
In the following $3 \times 3$ box tables, you must type one natural number at a time in each box so that the three numbers in each row, column, and diagonal are the same. The three numbers entered in the boxes are known (see Figure 1). Fill in the other boxes in the table! [for example 1] (LV.AMO.2011.5.2.png) 
<small>
* Topic: NumTheoryExprVariables
* Topic: AlgebraicTransformations
* questionType: FindAll
* Concept: sum
</small>
# <lo-sample/> LV.AMO.2011.5.3
Show how the square can be divided into multiple wide-angle triangles! 
<small>
* Topic: Constructionstriangulate
* Topic: Constructionssmallmovements
* Topic: Circleinscribedangles
* questionType: Prove
* cooked: Square-Geo, Triangle
</small>
# <lo-sample/> LV.AMO.2011.5.4
Whether the natural numbers from $1$ to $12$, each being used directly once, can be written around the circle in such order that the difference between any two adjacent numbers is * * (a) * * $2$ or $3$; * * (b) * * $3$ or $4$? 
<small>
* Topic: Treetraversalbacktracking
* Topic: Graphproblems
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2011.5.5
In a square with dimensions, $7 \times 7$ boxes should be placed in the $n$ “corners” (figures shown in Figure 2) so that no other such “corners” can be inserted more. (The edges of corners must walk along the edges of the boxes. Corners can also be rotated differently.) Show me how you can do this if * * (R) * * $n=9$; * * (B) * * $n=8$.! [Figure 2] (LV.AMO.2011.5.png) 
<small>
* Topic: CountingUsingSymmetry
* Topic: TreeTraversalBacktracking
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2011.6.1
Are there natural numbers for $a$ and $b$ that meet the equation $$a \cdot b \cdot (a+b) = 20102011 ?$$ 
<small>
* Topic: Integerfactorization
* questionType: Provedisprove
* cooked: equation
</small>
# <lo-sample/> LV.AMO.2011.6.2
Sixty pensioners each day * on the social network * correspondence with each other. Each gentleman is in correspondence with directly $17$ ladies, while each mistress is in correspondence with directly Mr $13$. How many of these pensioners are Mr and how many crooks? 
<small>
* Topic: BipartiteGraphs
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2011.6.3
In a square with dimensions, the $8 \times 8$ boxes are initially all white. What is the smallest number of boxes in this square to color green so that no fully white rectangles with size $1 \times 3$ boxes (placed horizontally or vertically) can be found in it
<small>
?
* Topic: Exhaustionmethod
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2011.6.4
figure 3 shows a table of $3 \times 3$ boxes that contains integers. In one move, you can select two different table boxes -- let's label the numbers you type in them with $a$ and $b$, delete the two numbers, and type them instead: instead of a, you $5a-2b$ a number, and instead of b, you $5b-2a$ a number. Can I get the table illustrated in Figure 4 by making such moves several times?! [Figure 3] (LV.AMO.2011.6.4A.png)! [Fig. 4] (LV.AMO.2011.6.4B.png) 
<small>
* Topic: InvariantRemainder
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2011.6.5
Beth had $50$ candy, while Alma and Dane had the same number of candy. Beth lost one candy and was saddened. Alma felt sorry for Beth and returned half of her candy to her sister. Beth calmed down and decided she now had too many candy and gave half of her Dane away. Dana also decided to share with Alma and returned half of her candy to Alma. Now Alma and Beth have the same number of candy. How many candy did each of the sisters have at the start? 
<small>
* Topic: AlgebraicTransformations
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2011.7.1
Six different source numbers up to the $100$ are written in ascending order on the board. It is known that 1. the last digits of all numbers are different; 2. the sixth figure is $14$ greater than the third; 3. the first digit of the fourth digit is equal to the last digit of the second digit; 4. the first digits of the fifth and sixth digits are the same. Find all these numbers! 
<small>
* Topic: Primesdistribution
* questionType: Findall
* cooked: PRIMES
</small> 
# # Resolution * * (a) * * $p_1=2$, $p_2=5$. * * (b) * *, * * (d) * * $(p_3;p_6)=(53,67)$. * * (c) * * $p_4=59$.
# <lo-sample/> LV.AMO.2011.7.3
Find a natural number that, divided by $2010$, results in $13$ in the remainder and $2011$ in the remainder. 
<small>
* Topic: Arithmeticseriesdivisibility
* Topic: Chineseremaindertheorem
* questionType: Findexample
* cooked: remainder
</small>
# <lo-sample/> LV.AMO.2011.7.4
The square is divided into five rectangles so that the lengths of the edges of these rectangles in centimeters are all the natural numbers from $1$ to $10$. Show one example of how you can do it! 
<small>
* cooked: square-Geo, rectangle
* questionType: FindExample
</small>
# <lo-sample/> LV.AMO.2011.7.5
The straight is painted $10$ in different colours. Show that you can find two dots of the same color on it, between which the distance in centimeters is an integer
<small>
.
* cooked: line, point, distance, integer-numbers
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2011.8.1
Inserts arithmetic action marks (“$+$”, “$15$”, “$\cdot$”, “$-$”) and parentheses between $:$ without changing their order so that the value of the resulting expression is * * * ((B) * * $16$. 
<small>
* Topic: Algorithmsonsyntaxtrees
* questionType: Findexample
* seeAlso:LV.AMO.2010.8.1
</small> 
# # solution * * * (A) * * $8 - 3 + 5 \ast 2 = 8 - (3 - 5 \ast 2) = 15$; * * (B) * * * $8 : (3 - 5:2) = 16$.
# <lo-sample/> LV.AMO.2011.8.4
Leonard opted for an arbitrary three-digit number, multiplied it with a $2$, and recorded the original number at the end of it. Whether his newly acquired figure necessarily shares * * (R) * * $17$; * * (B) * * $23$? 
<small>
* Topic: Notationshift
* Topic: Canonicalfactorization
* questionType: Provedisprove
* cooked:
</small> resolution of divisibility 
# # If the 3-digit number is $\overline{abc}$, the new number is $2001\overline{abc}$ shared with the $23$. But $17 \nmid 2001$.
# <lo-sample/> LV.AMO.2011.8.5
John and Anne play a game like this. A natural number is written on the board. Players take turns making the move: subtracts a digit of that number from the number you type (except $0$), erases the number on the board, and writes the resulting difference instead. Whoever gets zero after his move wins. The number $2011$ is written at first, the first move by Anna. Which of the players, playing properly, will win? Descriptions of how the winner should behave! 
<small>
* Topic: GameInvariant
* questionType: Algorithm, prove
</small> 
# # Recommendation After every move by Anna, the number must share the $10$.
# <lo-sample/> LV.AMO.2011.9.1
Find all pairs of natural numbers $(x, y)$ such that $x\neq y$ and $$\frac{1}{x^2 + 24} + \frac{1}{y^2 + 24} = \frac{2}{xy + 24}.$$ 
<small>
* cooked: natural-numbers, pair
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2011.9.3
Equation $\# x^2 − \# x + \# = 0$ is given. Two gnomes play the game - the former names three different numbers and the latter bends them into “$\#$” places in some order. Can the first gnome always get the equation to have at least one rational root? 
<small>
* cooked: equation
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2011.9.4
What is the highest number of consecutive natural numbers that can be represented by the characteristic that each is expressed as the difference between two squares of natural numbers? 
<small>
* Concept: Square-Geo, rectangle
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2011.10.1
How many different ways can a number $2011$ be expressed as the sum of at least two consecutive natural numbers? The order of the counts is irrelevant. 
<small>
* seeAlso:LV.AMO.2010.10.4
* cooked: sum, consecutive-numbers
* questionType: FindCount
</small>
# <lo-sample/> LV.AMO.2011.11.1
Three arithmetic progressions are given: (1) $1, 15, 29, 43, 57, 71, \ldots$ (2) $2, 17, 32, 47, 62, 77, \ldots$ (3) 3, 19, 35, 51, 67, 83,\ ldots $* * (P) * * Find the smallest number belonging to all three given strings! * * (B) * * * Specify that there are infinite numbers belonging to all three given strings! 
<small>
* seeAlso:LV.AMO.2010.11.1
* Concept: arithmetic-progression, sequence
* questionType: Findoptimal, prove
</small>
# <lo-sample/> LV.AMO.2011.11.5
Can $2011$ different natural numbers be placed along the circle so that for any two adjacent numbers, the largest number to the smallest is the primary number? 
<small>
* Concept: circumference, PRIMES
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2011.12.1
The natural numbers from $1$ to $9$ are divided into three groups of three numbers and the sum of the numbers in each group is calculated. Can it be that * * (R) * * * all amounts are primary numbers? * * (B) * * all amounts are different primary numbers? 
<small>
* Concept: sum, PRIMES
* questionType: ProveDisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2012.5.1
The notation of two natural numbers uses only the numbers $1$, $4$, $6$, and $9$. Can one number happen to be exactly seven times higher than the other? 
<small>
* Topic: ExhaustionMethod
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2012.5.2
Show how the square can be divided into multiple wide-angle triangles. (A triangle is called a wide-angle triangle if it has one wide angle and two narrow angles.) 
<small>
* Topic: Constructionstriangulate
* Topic: Circleinscribedangles
* sameAs:LV.AMO.2011.5.3
* questionType: Provedisprove
* cooked: Square-Geo, Triangle
</small>
# <lo-sample/> LV.AMO.2012.5.3
The bag contains white, green and red buttons (no other color buttons in the bag). What the smallest number of buttons for good luck (not seeing them) should be removed to be sure to have either $2$ white or $3$ green or $4$ red buttons 
<small>
* Topic checked out: Numtheorypigeonholenewsets
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2012.5.4
$24$ - the steep house has an elevator that has two buttons. When you press one button, it rises (if possible) $17$ upright by pressing the other -- descends $8$ upright (if possible). Find out which floor you can get to any other floor in this house with this elevator. (Lyft can't climb above 24 th floor and below 1 st floor.) 
<small>
* Topic: NumTheoryMathInduction
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2012.5.5
Distribute the figure represented in Figure 1 into three equal figures. (We call the figure and its mirror image the same shapes.).! [for example 1] (LV.AMO.2012.5.png) 
<small>
* Topic: SquareGridCutting
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2012.7.1
Can you find integers for $a$ and $b$ that match $$ab(3a + 5b) = 1234567?$$ 
<small>
* Topic: Modularparity
* questionType: Provedisprove
* cooked: equation
</small> 
# # solution Uneven multiplication means that the $a,b$ is odd. But then there are couples in the $3a+5b$, which is a contradiction.
# <lo-sample/> LV.AMO.2012.7.2
Six lengths of $1\mbox{cm}$, $3\mbox{cm}$,, $11\mbox{cm}$, $5\mbox{cm}$, $9\mbox{cm}$, $7\mbox{cm}$ are given. How many different ways can you choose three notches from them so you can create a triangle from them (each triangle has one notch at the edge)? 
<small>
* cooked: triangle, segment
* questionType: Findcount
</small>
# <lo-sample/> LV.AMO.2012.8.1
Inserts arithmetic action marks (“$+$”, “$13$”, “$\ast$”, “$-$”) and parentheses between $:$ without changing their order so that the value of the resulting expression is * * * ((B) * * $14$. 
<small>
* Topic: Algorithmsonsyntaxtrees
* questionType: Findexample
</small> 
# # solution * * (R) * * $4 \ast 1 \ast 5 - 7 = 13$; * * (B) * * $4:(1-5:7) = 14$ but also $(4-1-5)\ast(-7)=14$.
# <lo-sample/> LV.AMO.2012.8.3
No more than a $60$ of pupils attended the school's math Olympiad. The average score the boys scored was $21,6$. The average score the girls scored was $15$. The average score all students scored was $20$. How many students took part in the Olympics? 
<small>
* Topic: Baricentercoordinates
* Topic: Numtheoryinequalitymethod
* questionType: Findall
</small> 
# # solution shoulders $1.6=|21.6-20|$ and $5=|15-20|$ apply as $8$ and $25$. The boys are $25$ and girls $8$.
# <lo-sample/> LV.AMO.2012.8.4
$11$ integers are written around the circle. The sum of any three numbers taken in succession shall be divided by the $5$. Show that all the numbers you type are divided by $5$. 
<small>
* Topic: Periodicremainders
* questionType: Prove
* cooked: sum, divisibility
</small> 
# # resolve balances $(\operatorname{mod} 5)$ repeats every $3$, so all of them are the same (and the same $0$).
# <lo-sample/> LV.AMO.2012.9.1
Find one number that directly $12$ healthy positive dividers. 
<small>
* Topic: Modularithmetic
* Topic: Modularithmetic
* questionType: Findexample
* cooked: divisor
</small>
# <lo-sample/> LV.AMO.2012.9.2
A $\angle ABC = 90^{\circ}$ $ABC$ in the triangle and the dot $P$ is on the edge $AB$. Points $M$ and $N$ are the $AC$ and $PC$ midpoints of the cut-offs respectively. Show you $\angle BAC = \angle BMN$. 
<small>
* Topic: TriangleCongruence
* questionType: prove
* cooked: Triangle
</small>
# <lo-sample/> LV.AMO.2012.9.3
The $x^2 − 507x + a = 0$ roots of the square equation are $p^2$ and $q$, where $p$ and $q$ are primary numbers. Calculations $a$ a numeric value. 
<small>
* Topic: ModularArithmetic
* Topic: ModularArithmetic
* questionType: FindAll
* Concept: quadratic-equation, PRIMES
</small>
# <lo-sample/> LV.AMO.2012.9.4
Nine star $\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;$ are written on the board. John writes any number from $1$ to $9$ instead of an asterisk. Peter then records two digits instead of any two other Zvaigznisi (they can also happen again). They then repeat the action twice more. Peteri wins if the resulting nine-digit number shares the $37$. Can Peter always win? 
<small>
* Topic: ModularArithmetic
* Topic: ModularArithmetic
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2012.9.5
A trapeze is given, the lengths of the edges of which are $3$ and $13$. Prove it can't be split into five single triangles. (The figures are called monolarge if they have the same areas.) 
<small>
* Topic: TriangleAreaBaseHeight
* Topic: Trapezoids
* questionType: prove
* cept: TRAPEZOID, triangle
</small>
# <lo-sample/> LV.AMO.2012.10.1
Show up: if $p$ and $14p^2+1$ are primary numbers, the $14p^2-1$ is a cube of a natural number. 
<small>
* Topic: Modularithmetic
* Topic: Modularithmetic
* questionType: Prove
* cooked: PRIMES
</small> 
# # solution * If the $p$ does not share the $3$, then the $p^2$ balance divided by the $3$ is $1$. * the $14p^2$ then gives the remainder to the $2$ divided by the $3$ because the number multiplied by the remainder $2$ by the remainder $1$. * the $14p^2+1$ then gives the remainder to the $0$ divided by the $3$. It's not a prime number. We conclude that $p=3$ (other primary numbers do not share $3$). So $14p^2 +1 = 127$ and $14p^2 - 1 = 125$ what a full cube $5^3$ really is.
# <lo-sample/> LV.AMO.2012.11.1
Show that there is no natural number $n$ that the number $n^2 − 3n − 1$ shares with the $169$. 
<small>
* Concept: divisibility
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2012.12.1
Numbers in $A$ and $B$ are two different $7$ - numbers that each contain all numbers from $1$ to $7$. Show that $A$ is not sharing $B$. 
<small>
* Concept: divisibility
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.5.1
How many times a day do the clock hour and minute figures match? (Close 00:00 and 24:00 count once.) * justify reply! * 
<small>
* questionType: FindCount
</small>
# <lo-sample/> LV.AMO.2013.5.2
$24$ - the steep house has an elevator that has two buttons. When one button is pressed, it rises (if possible) $17$ upright by pressing the other - descends $8$ upright (if possible). Find out which floor you can get to any other floor in this house with this elevator. (Lyft can't climb above 24 th floor and below 1 st floor.) 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2013.5.3
in Figure 1, enter one digit in each circle, another in each circle, so that the sum of the numbers entered in each of the three circles on the same line is the same. [Figure 1] (LV.AMO.2013.5.3.png) 
<small>
* Concept: sum
* questionType: FindExample
</small>
# <lo-sample/> LV.AMO.2013.5.4
From the figures in Figure 2, assemble a rectangle with a $40$ box area. The shapes must not overlap and each type of figure must be used at least once. (Figures can be turned or turned upside down.). [Figure 2] (LV.AMO.2013.5.4.png) 
<small>
* questionType: FindExample
</small>
# <lo-sample/> LV.AMO.2013.5.5
Each cube is divided into four equal squares. Can these squares be painted (a) in two; (b) in three colours so that the squares sharing a border are painted in different colours? Each square must be completely colored. * justify reply! * 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2013.6.1
Ten numbers are written on the board: $$1\;\;2\;\;3\;\;4\;\;5\;\;6\;\;7\;\;8\;\;9\;\;10.$$ Alfon clears any two of them (let's sign them with $a$ and $b$) and writes a number equal to the $a+b+2$ instead. He repeats this operation while one number remains on the board. Justifies that regardless of the order in which Alfon performs operations, the same number is ultimately obtained. What is it like? 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.6.2
Whether two consecutive natural numbers can be found, one of which shares $3$ and whose * * * (R) * * numerical amounts differ by 3; * * (B) * * * digit multiplications vary by 3? 
<small>
* Concept: for divisibility, sum
* questionType: Provedisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2013.6.3
Cut the $20$ of figures in Figure 3 into equal smaller figures (the figures may be rotated or inverted).! [Fig. 3] (LV.AMO.2013.6.3.png) 
<small>
* questionType: FindExample
</small>
# <lo-sample/> LV.AMO.2013.6.4
Can numbers from $100$ to $200$ be divided into two groups so that the product of numbers in both groups is the same? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2013.6.5
Una and Ivo, moving sequentially, type their name in the three * * empty * * one row or column * * next to * * * boxes of a square with dimensions of 5x5, typing each letter in another box. The player who last records his name wins. Una makes the first move. Which player can always get their win? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2013.7.1
In a natural double digit number, none of the digits are $0$. To show that, by dividing this number by its numeric multiplication, the division is at least $\frac{11}{9}$. 
<small>
* Topic: Numtheoryinequalitylargeintervals
* Topic: Notationpolynomial
* Topic: Numtheoryextremeelement
* questionType: Prove
</small> 
# # resolve $\frac{10a+b}{ab}=\frac{10}{b}+\frac{1}{a}$ is the least if $a=b=9$.
# <lo-sample/> LV.AMO.2013.7.2
Six lengths of $1\mbox{cm}$, $3\mbox{cm}$,, $11\mbox{cm}$, $5\mbox{cm}$, $9\mbox{cm}$, $7\mbox{cm}$ are given. How many different ways can you choose three notches from them so that you can create a triangle (each triangle has one notch at the edge)? 
<small>
* sameAs:LV.AMO.2012.7.2
* Concept: triangle
* questionType: Findcound
</small>
# <lo-sample/> LV.AMO.2013.7.3
Prove that the number $1234567891011\ldots{}175176$ (all the subsistence numbers from $1$ to $176$ written in turn) is not a square of a subsistence number. (Number square: the product of a number by itself.) 
<small>
* Topic: Divisibilityruleslastdigits
* Topic: Divisibilityrulesforremainders
* Topic: Primefactorizationandpowers
* Topic: Seriessmemberssumsclosedformulae
* questionType: Prove
</small> 
# # solution can use severability with $3$ in the following judgment: * For this number, the sum of the digits of the congruent by module $9$ with the $1+\ldots+176$. (The balance does not change when decimal digits are moved). * sum up an arithmetic progression: $1+\ldots+176=(176\cdot 177)/2$ - shares $3$, but not $9$. * a full square cannot contain a primary number in the $3$ odd degree. Another solution uses severability with $2$: * The division of full squares into first-time multipliers cannot share $8$ or $16$ – contain a primary number to the $2$ odd degree.
# <lo-sample/> LV.AMO.2013.7.4
Whether the $5 \times 5$ boxes in the square can be coloured * * (a) * * $6$ boxes; * * (b) * * * $5$ boxes so that no figure shown in Figure 4 can be inserted in the remainder (it may be turned or upside down)? [for example 4] (LV.AMO.2013.7.4.png) 
<small>
* questionType: FindExample
</small>
# <lo-sample/> LV.AMO.2013.7.5
Una and Ivo, moving sequentially, type their name in the boxes of the three * * empty * * * one row or column * * next to * * box of the square with dimensions, typing each letter in another box. The player who last records his name wins. Una makes the first move. Which player can always get their win? 
<small>
* questionType: FindExample
</small>
# <lo-sample/> LV.AMO.2013.8.1
Find all subsistence numbers up to $1000000$ that decrease $36$ times by deleting their first digit. 
<small>
* Topic: Numtheoryexpr
* Topic: Notationfragment
* questionType: Findall
</small> 
# # solve spells algebraically, meaning separating the first digit from the rest of the piece $a$ - 1.c pepper; $a \cdot 10^k + b = 36b$; $a \cdot 10^k = 35b$. Then $a = 7$, $b=2\cdot 10^{k-1}$.
# <lo-sample/> LV.AMO.2013.8.2
A triangle is given for the $ABC$ and a point is $P$ inside it. Please note that the sum of the distances from the $P$ of the point to the peaks of the given triangle is more than half the perimeter of the triangle. 
<small>
* Concept: triangle, perimeter
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2013.8.3
They give such real figures to $t$ and $a$ that they $t^2 - t \cdot sqrt(t) + a = 0$'t. Prove $t \geq 4a$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.8.4
Can a regular hexagon be split * * (R) * * into nine; * * (B) * * into eight equal polygons? 
<small>
* questionType: ProveDisprove, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2013.8.5
The Dwarf has imagined numbers in $x_1,x_2,x_3,x_4$, each of them either $0$ or $1$. If a gnome is asked, “What's the $i$ - that number?” ($i = 1, 2, 3\ \mbox{vai}\ 4$ optional), then he tells the $x_i$ value. To prove that $3$ questions are enough to find out whether a series of $x_1,x_2,x_3,x_4$ are monotonous. Number string $x_1,x_2,x_3,x_4$ is monotonous if it is non-descending or non-rising (i.e. $x_1 \leq x_2 \leq x_3 \leq x_4$ or $x_1 \geq x_2 \geq x_3 \geq x_4$). 
<small>
* cooked: monotonic-sequences
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.9.1
A trapeze is given, the lengths of the edges of which are $3$ and $13$. To prove that it cannot be split into five single triangles. (The shapes are called monolarge if they have the same areas.) 
<small>
* cooked: TRAPEZOID, triangle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.9.2
The $4 \times 4$ box of a square with dimensions has each box top painted in one of two colors. Prove that you can definitely find three dots painted in the same color at the peaks of the equilateral right-angle triangle. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.9.3
Four different digits are given, none of which are $0$. The sum of all double digits that can be created from these digits is $484$. Find the given four digits. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2013.9.4
Gives a string of numbers in the $x_0,x_1,x_2_,x_3,\ldots$ in which you want to $x_0 \geq 0$ and $x_{n+1}=x_n + \frac{2}{x_n}$ all $n \geq 0$. Prove $x_{100} \geq 20$. 
<small>
* cooked: sequences
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.9.5
A curved square is given. Four circles with rectangular edges in diameter are drawn. Prove these circles completely cover a given square. 
<small>
* cooked: square-Geo, circle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.10.1
Given that the $x_1$ is the $x^2+px+q=0$ root of the equation, and the $x_2$ is the $-x^2+px+q=0$ root of the equation. Prove that equation ${\displaystyle \frac{1}{3}x^2+px+q=0 }$ must have a root in the $x_3$ between $x_1$ and $x_2$ (i.e., $x_1 \leq x_3 \leq x_2$ or $x_2 \leq x_3 \leq x_1$). 
<small>
* cooked: equation, root
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.10.2
In the triangle, the $ABC$ cut-off $CD$ is a bisectre. A circle is $C$ drawn through the point, touching the edge at the $AB$ point in the $D$. It crosses the edge $AC$ and $BC$ at points $P$ and $Q$ respectively. Prove $AB \parallel PQ$. 
<small>
* cooked: circumference
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.10.3
$n$ - hexa, let's call a plane figure made up of $n$ regular hexagons so that each hexagon shares a border with at least one other hexagon. What smaller $n$ ($n \geq 2$) does such a $n$ exist - hexa, with which you can't cover the figure depicted in Figure 5 (it consists of regular hexagons with a hole in the centre)?! [for example 5] (LV.AMO.2013.10.3.png) 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2013.10.4
A $51$ number is selected from the first $100$ native numbers. Prove you can choose two of them, one of which shares with the other. 
<small>
* Topic: Arithmeticandgeometricseries
* Topic: Numtheorypigeonhole
* questionType: Prove
* cooked: divisibility
</small> 
# # resolve prescribes geometric progressions that begin with odd numbers and $q=2$: $$(1,2,4,8,16,32,64),\;(3,6,12,24,48,96),$$ $$(5,10,20,40,80),\ldots,(97),\;(99).$$ * will have exactly $50$ progressions (some will have only one Member at a time) because odd numbers are directly $50$ to the $100$. * Each number belongs to exactly one progression, because each number of pairs corresponds to exactly one odd number that occurs when you redivide by $2$. * When you choose to $k+1$ numbers, at least two will come from the same progression (Dirichlee principle). * Note: * If numbers are only $50$, you cannot similarly conclude. You can choose $51,\ldots,100$ - none of which share with the other.
# <lo-sample/> LV.AMO.2013.10.5
Can you type $2013$ Naturals around the circle so that the ratio of any two adjacent numbers is $2$, $3$, $12$, or $18$? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2013.11.1
Prove that there is no natural number $n$ that the number $n^2-3n-1$ with the $169$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.11.2
Does there exist a regular polygon with the length of one diagonal equal to the sum of the lengths of two other diagonals? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2013.11.3
Different odd natural numbers in the $a_1, a_2, \ldots, a_n$ are given. None of them share any prime number greater than $5$. Prove $$\frac{1}{a_1} + \frac{1}{a_2} + \frac{1}{a_3} + \ldots \frac{1}{a_n} < 2.$$ 
<small>
* cooked: PRIMES, divisibility
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.11.4
There are $2013$ cities in a country, you can fly a plane from each to each. Some of these flights are operated by $A$, others by $B$ (It's possible that an airline $A$ plane flies from the city $X$ to the city $Y$, but from $Y$ to $X$ -- the airline's $B$ plane). To demonstrate that airlines' responsibility for the flights can be mapped so that the traveller, when departing from any city in $Z$, visiting one or more cities on the way and then returning to the city in $Z$, * * will definitely * * have flown on both airlines &quot;planes, no matter which route they have taken and which is the original city in $Z$. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2013.11.5
On a rectangular tabletop there are several equal pieces of square paper, the edges of which are parallel to the edges of the table (the squares may also overlap). Prove that you can stab some needles in the table so that each piece of paper will be pinned to the table directly with one needle. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.12.1
Resolve equation ${\displaystyle \log_{10} x  \cdot \log_{10} (4-x)=\frac{1}{4}}$ in real numbers. 
<small>
* cooked: equation
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2013.12.2
In the triangle, the $ABC$ points $M$, $N$ and $K$ are the mid-points of the edge $AB$, $BC$ and $CA$ respectively. Three doughnut lines are drawn: through points $K$, $A$, $M$; through points $M$, $B$, $N$; through points $N$, $C$, $K$. Prove that all drawn doughnut lines intersect at one point. 
<small>
* cooked: circumference
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.12.3
Prove that subsistence numbers do not exist $x, y, z$ that the equation $6^x + 13^y = 29^z$. 
<small>
* concepted: equation
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.12.4
The alphabet of a language contains $i$ vowels ($i \geq 2$) and $j$ consonants ($j \geq 2$). In this language, any final string of letters (vowels and consonants) containing at least one letter and in which no two vowels appear in succession and consecutive consonants are not more than two (for example, if “A” is a vowel and “B” is a consonant, for example, “ABBA” is a word, whereas “BAAB” and “ABBBA” are not words). Let's $S(n)$ the number of words that are made up of $n$ letters, $n \geq 1$. Prove that all natural numbers n have the same $$S(n+3) = i \cdot j \cdot S(n+1) + i \cdot j^2 \cdot S(n).$$ 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2013.12.5
Given the plane of square boxes, the length of each edge of the box is $1$. Demonstrate the existence of a triangle whose peaks are at the top of the boxes of this plane and the lengths of any two sides of it differ by no more than the ${\displaystyle \frac{1}{2013 \cdot \sqrt{P}}}$ where the $P$ is the perimeter of this triangle. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2014.5.1
For the children of fluffy village, the Easter bunny brought eggs. Each was painted exactly in one of the colors, red, yellow, blue. $20\%$, or $40$, eggs were known to be red, $\frac{3}{4}$ of what remained were yellow and the rest were blue. Calculations: * * * (R) * * How many eggs were blue? * * (B) * * What proportion of all eggs were blue? * * (C) * * How percent of all eggs were yellow? 
<small>
* Topic: Algebraicequations
* questionType: Findall, FindAll, FindAll
</small>
# <lo-sample/> LV.AMO.2014.5.2
The notation of two natural numbers uses only the numbers $2$, $3$, $7$, and $8$. Can one number happen to be exactly three times higher than the other? 
<small>
* Topic: IntegerCongruence
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2014.5.3
The length of the edges of the rectangular ABCD shall be expressed in whole centimetres. The area of the coloured part is $6$ $\mbox{cm}^2$ (see Figure 1). The cut-off $AE$ is $\frac{1}{3}$ from the edge of the rectangle in the $AD$. Calculate the rectangular area and perimeter if the edge of one rectangle is known to be $5$ $\mbox{cm}$ longer than the other.! [Figure 1] (LV.AMO.2014.5.3.png) 
<small>
* Topic: Rectangles
* questionType: FindAll
* Concept: rectangle, area, perimeter
</small>
# <lo-sample/> LV.AMO.2014.5.4
The square consists of $8 \times 8$ identical square boxes. It's cut into parts in such a way that the cuts go along the boundaries of the boxes. What is the largest number of parts that can be like the figure shown in Figure 2 (the figures can be rotated in any position)?! [Figure 2] (LV.AMO.2014.5.4.png) 
<small>
* Topic: SquareGridCutting
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2014.5.5
What is the smallest of * * (a) * *, * * (b) * * * the largest number that can be expressed as a product of both three and two different two-digit natural numbers? 
<small>
* Topic: Numtheoryinequalitylargeintervals
* questionType: Findoptimal, FindOptimal
* cooked: product
</small>
# <lo-sample/> LV.AMO.2014.7.2
Can you find integers for $a$ and $b$ that match $a \cdot (3a + 5b) \cdot 7b = 7654321$. 
<small>
* Topic: Modularparity
* questionType: Provedisprove
</small> 
# # solution Uncouple multiplication means the $a,b$ is odd. But then there are couples in the $3a+5b$, which is a contradiction.
# <lo-sample/> LV.AMO.2014.7.1
The triangle $ABC$ a $BD$ height and a median $BE$. What can the length of the $AC$ be if you $ED = 4\mbox{cm}$ and $DC = 5\mbox{cm}$? 
<small>
* cooked: Triangle, height, Median
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2014.7.4
In the $3 \times 3$ boxes of the table, you must type one natural number at a time in each box so that the amounts for each row, column, and each diagonal are the same. The numbers entered in the two boxes are known (see Figure\). What number should be in the box labeled with a question mark? Find all possible values and justify that there are no others!! [] (LV.AMO.2014.7.4.png) 
<small>
* Topic: Numtheoryexprvariables
* questionType: Findall
* Genre: magic-Configuration
</small> 
# # resolve If $a_{22}=x$, the amounts are $3x$. And $a_{13}=2x-13$, $a_{11}=x-11$, $a_{33}=x+11$, $a_{23}=2$.
# <lo-sample/> LV.AMO.2014.8.1
$\frac{1}{13}$ converted the number to an infinite decimal place and crossed out the 2014 digit after the decimal point. Which number is higher – original or obtained? 
<small>
* Topic: Periodicremainders
* Topic: Numericalgorithm
* questionType: Findall
* cooked: decimal-fractions
* Genre: digit-manipulation
</small> 
# # resolution $1/13=0.(076923076923)$ (period $12$ digits). $2014$ - the digit is the same as $10$ - the digit is the $9$ followed by the digit $2$. Deleting this number $9$ replaces it with a $2$, so the number becomes smaller.
# <lo-sample/> LV.AMO.2014.8.2
Find all subsistence numbers up to $1000000$ that decrease $15$ times by deleting their first digit! 
<small>
* Topic: Numtheoryexpr
* Topic: Notationfragment
* questionType: Findall
</small> 
# # solution $a$ - 1.c pepper; $a \cdot 10^k + b = 15b$; $a \cdot 10^k = 14b$. Then $a = 7$, $b=5\cdot 10^{k-1}$.
# <lo-sample/> LV.AMO.2014.8.5
In the $3 \times 3$ boxes of the table, you must type one natural number at a time in each box so that the amounts for each row, column, and each diagonal are the same. The number $24$ is entered in the middle box of the top row (see\ remark). Can the box marked with a question mark contain the number * * (a) * * $7$, * * (b) * $17$?! [magicsquare] (LV.AMO.2014.8.5.png) 
<small>
* Topic: Numtheoryexprvariables
* Topic: Treetraversalbacktracking
* questionType: Provedisprove
</small> 
# # solution designates $a_{22}=x$, $a_{31}=b$. Then $a_{13}=2x-b$, $a_{11}=x+b-24$, $a_{33}=x-b+24$, $a_{23}=2b-24$. $b=7$, $a_{23}<0$.
# <lo-sample/> LV.AMO.2014.9.2
Four different digits have been given, none of them $0$. The sum of all double digits that can be created from these digits is $1276$. Find the given four digits! 
<small>
* Concept: sum
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2014.9.4
In the $3 \times 3$ boxes of the table, you must type one natural number at a time in each box so that the amounts of the numbers that you type in each row, column, and diagonal are the same, but all the numbers that you type in the table are different from each other. The numbers entered in the two boxes are known (see note). What is the smallest number that can be typed in the center box of the table?! [Magic square] (LV.AMO.2014.9.4.png) 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.AMO.2014.10.4
Seven different natural numbers are given; for each of the two figures given, their amount was calculated. What is the highest number of these amounts that can be primaries? 
<small>
* Topic: Modularparity
* Topic: Bipartitegrapher
* Topic: Modularithmetic
* Topic: Treetraversalbacktracking
* questionType: Findoptimal
* cooked: sum, PRIMES
</small> 
# # resolve note that you need the highest * number *, which can be primary numbers. Not the largest * number of different primes * you can get this way. The sum of different natural numbers cannot be $2$. So for the sum of two numbers to be a (odd) prime number, one is couples, the other is odd. How many of the 7 are couples and how many odd numbers? in $$7=0+7=1+6=2+5=3+4=4+3=5+2=6+1=7+0$$, the highest theoretically possible number of $(n,p)$ couples is when $4$ of the seven numbers are odd and $3$ are couples (or vice versa): $4\cdot{}3=12$. Draw graph:! [] (LV.AMO.2014.10.4A.png) * Uneven numbers make up a set of $A$ with $4$ elements, paired numbers make up a set of $B$ with $3$ elements. * There are only $4\cdot{}3$ pairs that have a hope of being source numbers. (You cannot get the primary number of a $p+p$ or $n+n$ when you add it.) * * Definition: * * If all the peaks in the graph can be divided into two non-overlapping subsets in the $A$ and $B$ so that any edge of the graph goes from the summit together $A$ to the summit together in the $B$, then the graph is called * two-part *. * * statement: * * If the two-part graph has $a$ and $B$ peaks respectively in the subsets of the $A$ and $b$, it shall have no more than $a\cdot{}b$ edges. We look at balances divided by 3 rd! [] (LV.AMO.2014.10.4B.png) * When choosing the smallest odd and even numbers, only $9$ of the $12$ theoretically possible are prime numbers (other amounts are divided by $9$ - marked by a twisted line). * If all $7$ numbers are additionally required to give a $1$ of balances (or, exceptionally, a $0$ of balances), dividing by $3$, all $12$ amounts can be primed.
# <lo-sample/> LV.AMO.2014.11.2
The number string $(a_i)$ has a $a_1 + a_2 + \ldots + a_n = n^2 a_n$ relationship for all $n>1$. Calculate $a_{50}$ if you know to $a_1 = 1000$. 
<small>
* cooked: sequences
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2014.11.4
$99$ natural numbers are given. It is known that there is no number to share all these numbers, and that the product of any $50$ numbers is divided by the product of the remaining $49$ numbers. Prove that the product of all $99$ numbers is a square of a natural number. 
<small>
* cooked: product, square-ALG
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2014.12.3
Find all source numbers for $p$ that also have a primary number in the $p^4 − 6$! 
<small>
* Concept: PRIMES
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2015.7.3
* * (R) * * Find a natural number whose digits are $13$, the last two digits are $13$, and which shares $13$. * * (B) * * can you find a natural number whose digits are $11$, the last two digits are $11$, and who shares $11$? 
<small>
* topic:DivisibilityRuleFor11
* topic:DivisibilityRulesFor3And9
* questionType: Findexample, ProveDisprove
* cooked: sum
</small> 
# # Resolution * * (R) * * $117$ cip.sum MA $9$, shares $13$. $11713$ der. * * (B) * * $99k$ pairs/odd pos.cip.amount cannot be $9$.
# <lo-sample/> LV.AMO.2015.7.4
In an equilateral triangle, an inner dot $D$ marked on the base edge $BC$ $ABC$ so that the triangles $ABD$ and the $ACD$ are also equilateral. Calculate triangle $ABC$ angles! Find all cases and justify that there are no others! 
<small>
* cooked: isosceles-triangle
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2015.8.1
Determine whether the expression $\sqrt{6 + 2\sqrt{5}} + \sqrt{6 - 2\sqrt{5}}$ value is a rational number! 
<small>
* Topic: Standardidentities
* Topic: Infinitedescent
* questionType: Provedisprove
* cooked: the resolution of the national-numbers
</small> 
# # # is $20$ when you square, but the $\sqrt{20}=2\sqrt{5}$ is not rational.
# <lo-sample/> LV.AMO.2015.8.3
Find one natural number greater than $2015$ that cannot be expressed as the sum of a natural number square and a source number. 
<small>
* Topic: Standardidentities
* Topic: Primesdistribution
* questionType: Findexample
* cooked: PRIMES, sum, square-ALG
</small> 
# # solution If a large full square $N = n^2$, then the $n^2 - a^2$ divides the multipliers $>2$.
# <lo-sample/> LV.AMO.2015.9.3
Show that the $x^5 - 5x^3 + 4x$ is sharing $120$ when the $x$ is an integer! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2015.10.3
Find all subsistence numbers that are equal to their numeric product. (The numeric multiplication of a single digit is called its only digit.) 
<small>
* strategies: Trialanderror
* Topic: Inequalityprovingstronger
* questionType: Findall
* cooked: product
</small> 
# # solution * When you check different numbers, you can see that the number multiplication is always less than the number itself. * We base it on 2-digit and 3-digit numbers in the $\overline{ab}$ and multiply the first decimal digit of the $k$ $$a\cdot{}b < 10a \leq 10^1\cdot{}a + b = \overline{ab},$$ number by the $\overline{abc}$ digits that follow, we'll get a smaller result than multiplied by the $10^k$ because each digit is less than the $10$.
# <lo-sample/> LV.AMO.2015.11.1
We look at all nine-digit numbers that do not contain $0$, and for which all digits are different. Prove that there are exactly twice as many even numbers among them as those that share $3$ but do not share $5$. 
<small>
* cooked: divisibility
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2015.11.3
For a natural number $n$ with a $M(n)$, let's represent the smallest natural number that ends with a $n$ and whose sum of digits is $n$. Like $M(13)=913$. To prove that there are infinite numbers of $n$ that $M(n)$ shares with $n$. 
<small>
* cooked: divisibility
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2015.12.5
Find all subsistence triplets in $(a,b,c)$, such that $a \geq b \geq c \geq 2$ and $ab-1$ share C, $bc-1$ share $a$, $ac-1$ share $b$. 
<small>
* cooked: divisibility
* questionType: Findall
</small>
# <lo-sample/> LV.AMO.2016.7.2
Carlson bought himself $8$ pies and $15$ poppy buns for lunch, and his brother bought one pie and one poppy bun. Carlson paid exactly two euros for his lunch (every bun and pie costs a whole lot of cents). How much did his brother pay? 
<small>
* Topic: Numtheoryexpr
* Topic: Numtheoryexprforconcepts
* Topic: Numtheoryinequalitymethod
* questionType: Findall
</small> 
# # solution $200-8p=15m$, i.e. $m$ shares $8$. And $m$ can't be $16$ or $p<0$.
# <lo-sample/> LV.AMO.2016.7.3
Given that $AB\parallel{}CD$ and $AD\parallel{}BC$ (see Figure 1). The intersection of the cut-off $AC$ and $BD$ is $M$. A point selected on the straight $AB$ $N$ that you $AM=MN$. Prove you $\angle ANC=90^{\circ}$'t.! [Fig. 1] (Geometry-grade07/LV.AMO.2016.7.3.png) 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2016.8.1
Calculations the value of the given expression! $$\frac{2000016 \cdot 1999984}{5^{12} \cdot 2^{13} - 128}$$ 
<small>
* Topic: Standardidentities
* questionType: Findall
* cooked: expression
</small> 
# # resolve is writing an algebraic conversion: $\frac{4(10^6 - 8)(10^6 + 8)}{2(10^{12} -64)} = \frac{4}{2}=2$.
# <lo-sample/> LV.AMO.2016.8.2
Can you find integers like that in $a$ and $b$ you $ab(a+43b) = 434343$? 
<small>
* Topic: Modularparity
* questionType: The product of the provedisprove
</small> 
# # resolution is odd, i.e. the $a,b$ is odd. But then there are couples in the $a+43b$.
# <lo-sample/> LV.AMO.2016.8.3
A number is known to share $2016$ and that all its digits are different. What is the highest number of digits that can be in this number? 
<small>
* Topic: Divisibilityruleslastdigits
* topic:DivisibilityRulesFor3And9
* Topic: Divisibilityrulesother
* Topic: Exhaustionmethod
* questionType: Findoptimal
* cooked:
</small> resolution of divisibility 
# # all $10$ digits: $32 \mid 45312$. The sum of digits is divided by the $9$. Stir in the $6,7,8,9,0$ to share with the $7$.
# <lo-sample/> LV.AMO.2016.9.2
Can you find integers such as $x$, $y$, and $z$ that you $x^3 − 2016xyz = 10$? 
<small>
* seeAlso:LV.AMO.2016.10.2
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2016.9.4
In the $1; 2; 2; 4; 8; 32; 48; \ldots$ of a string of natural numbers, each Member, starting with the third, shall be equal to the non-null numerical multiplication of the two preceding members. What is the 2016 Member of this string? 
<small>
* cooked: sequence, product
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2016.10.2
Can you find integers like that for $x$, $y$, and $z$ you $x^3 − 2016xyz = 120$? 
<small>
* Topic: Divisibilityrulesforremainders
* Topic: Modularithmetic
* Topic: Modularithmeticcontradiction
* questionType: Provedisprove
* seeAlso:LV.AMO.2016.9.2
</small> 
# # Resolution contradictory Module: we look at the balances of both sides of the same, divided by $9$. Because $2016$ shares $9$, then $x^3 \equiv 3 \pmod {9}$. When checking all cubes in the $0^3,1^3,\ldots,8^3$, none of them give any residual $3$, divided by $9$.
# <lo-sample/> LV.AMO.2016.10.3
The arithmetic progression's four consecutive members are whole numbers for $A$, $B$, $C$ and $D$. Prove that $A^2+2B^2+3C^2+4D^2$ can be expressed as the sum of two squares of integers! 
<small>
* Topic: Seriesmemberssumsclosedformulae
* Topic: Standardidentities
* Topic: Completingsquare
* questionType: Prove
* cooked: arithmetic-progression, sum, square-ALG
</small>
# <lo-sample/> LV.AMO.2016.11.2
Can you find such natural numbers for $x$, $y$, and $z$ that you $x^2 + y^2 + z^2 = \underbrace{1111 \ldots 1}_{2016}$? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2016.12.2
Prove equation $10^x + 12^y = 34^z$ has no solution in natural numbers! 
<small>
* Concept: equation
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2017.7.3
Two corners of the rectangle leaf were folded as shown in Figure 3. It turned out that the bottom edge of the leaf was divided into three sections of the same length and the top edge into two sections of the same length. Prove the coloured triangle equilateral! [LV.AMO.2017.7.3] (LV.AMO.2017.7.3.png) 
<small>
* cooked: equilateral-triangle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2017.7.5
How many natural double digit numbers have a numeric multiplication exactly twice the number itself? 
<small>
* questionType: FindCount
* concepts: product
</small>
# <lo-sample/> LV.AMO.2017.8.5
Can I find a ten-digit number equal to the product of all my digits? 
<small>
* questionType: ProveDisprove
* concepts: product
</small>
# <lo-sample/> LV.AMO.2017.9.5
Resolve equation $x^3 + (x+1)^3 = (x+3)^3 + 1$ in natural numbers. 
<small>
* cooked: equation
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2017.10.5
Prove if three natural numbers $n$; $n+11$ and $n+22$ two are primary numbers, and then the third number is divided by $6$. 
<small>
* Topic: Divisibilityproperties
* Topic: Arithmeticseriesall
* strategy: Caseanalysis
* questionType: Prove
* cooked: PRIMES
</small> 
# # Recommendation treats cases $n=2,3$ separately.
# <lo-sample/> LV.AMO.2017.11.5
Given subsistence numbers for $k$ and $n$, $k \leq n$. * * (R) * * * are certain $C_n^k$ shared with $n$ when $k$ and $n$ are preceded by each other? * * (B) * * are $k$ and $n$ necessarily preceded by each other when $C_n^k$ are shared with $n$? * Note: * number of $C_n^k$-labeled combinations of $n$ elements by $k$ element. 
<small>
* Concept: coprimes
* questionType: Prove
</small>
# <lo-sample/> LV.AMO.2017.12.5
* * (A) * * natural numbers from $1$ to $11$ are given. Select nine of them and type them in the table in the $3 \times 3$ boxes so that the sum of the numbers typed in each row, each column, and both major diagonals is divided by the $7$. * * (B) * * can you do the same if you give subsistence numbers from $1$ to $10$? 
<small>
* questionType: Findexample, ProveDisprove
</small>
# <lo-sample/> LV.AMO.2018.7.3
Arbitrary internal point $D$ is selected on the $AB$ edge of the triangle $ABC$. Prove $CD > \frac{1}{2}(CA+CB-AB)$. 
<small>
* cooked: triangle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2018.7.4
Find an integer $n$ to make the equation $$(n - 2021)(n - 2018)(n - 2017)(n - 2016) = 2016$$ true! 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2018.8.2
In the $1; 8; 8; 64; 192; 432; \ldots$ of a string of natural numbers, each Member, starting with the third, shall be equal to the non-null numerical multiplication of the two preceding members. What is the 2018 Member of this string? 
<small>
* questionType: FindAll
* concepts: sequence, product
</small>
# <lo-sample/> LV.AMO.2018.9.4
Find the largest natural number that shares a $7$ whose digit amount is $100$ and for which no digits are $0$. 
<small>
* Concept: for divisibility, sum
* questionType: Findoptimal
</small>
# <lo-sample/> LV.AMO.2018.10.4
Prove if $x$ - a natural number, then $x^8 - x^2$ shares $252$. 
<small>
* topic:DivisibilityRulesFor3And9
* Topic: Divisibilityproperties
* Topic: Modularithmetic
* Topic: Polynomialdifferencedivisibility
* questionType: Prove
* cooked:
</small> resolution of divisibility 
# # Check dividibility with 252 multipliers. * * claim: * * for a natural number to $N$ share $252=2^2\cdot{}3^2\cdot{}7^1$, it is necessary and sufficient for the $N$ to share the highest grades of the first-time multipliers: $2^2 = 4$, $3^2 = 9$, and $7^1 = 7$. * $x^8 - x^2$ shares $4$: - If the $x$ is a paired number, then the $x^2$ is divided by the $4$. - If the $x$ is an odd number, then the $(x^4-x)(x^4+x)$ is the product of two paired numbers. So also shares $4$. * $x^8 - x^2$ shares $9$: - If $x$ shares $3$, then $x^2$ shares $9$. - If $x = 3k+1$, then $x^3 - 1 = (3k+1)^3 - 1$ shares $9$ (checked by opening parentheses) - If $x = 3k-1$, then $x^3 + 1 = (3k-1)^3 + 1$ shares $9$ (checked by opening parentheses), let's justify that $x^8 - x^2 = x^2(x^6-1)$ also shares $7$. * If $x$ shares $7$, then $x^2$ shares $7$. * If $x$ doesn't share $7$, we can use the small farm theorem at the $p=7$. * * on a small farm, theorem: * * If the $p$ is a primary number and the $a$ does not share the $p$, then the $a^{p-1}$ gives the remainder to the $1$ divided by the $p$. In other words, $a^{p-1}-1$ shares $p$. When you insert a $p-7$, we get that the $a^6 - 1$ shares the $7$, unless the $a$ shares the $7$. * * Empirical theorem testing, if p = 7 * * in the small farm, remembering the theorem is valid, but can be justified otherwise. Let's check that the $x^6$ gives the remainder to the $1$, divided by the $7$ for all $x=1,2,3,4,5,6$. (For larger $x$ values, the $x$ can be replaced by its remainder, the balance of the polynomial $x^6$ value will not change from it). | $x$ | $2$ | $3$ | $1$ | $4$ | $5$ | | -------------- | ----- ------ | ------------------ | -------------- | ------------- | $x^3          | $ 1 $   | $ 8 $   | $ 27 $          | $ 125 $         | $ 216 $        | 
| $ x ^ 3\ pmod 7 $ | $ 1 1 pmod 1 $   | $ 6 $          |
| $ 6 $   | $ 6 $   | $ 1 $   | $ 6 $  | $ 6 $           | $ 6 $ | $ 6 $           | $ 6\ mod 1 $   | $ 6 $6$ $ | $ 1 $   | $ 36\ equiv 1 $ | 36 \equiv 1$ | * * claim: * * If the $P(x)$ is a polynomial with whole coefficients, if the $x_1, x_2, m$ has natural numbers, then the $x_1$ and $x_2$ give the same residuals divided by the $m$, then the $P(x_1)$ and $P(x_2)$ of the polynomial value give the same residuals divided by the $m$. * * Definition: * * the claim that $x_1$ and $x_2$ give the same balance shall be recorded by $m$ as follows: $x_1 \equiv x_2\;(\mbox{mod}\,m)$. Read it: $x_1$ and $x_2$ are * congruents * by module $m$. In those signs, for each polynomial $P(x)$, the following can be inferred: $$ x_1 \equiv x_2\;(\mbox{mod}\,m)\;\;\Rightarrow\;\;P(x_1) \equiv P(x_2)\;(\mbox{mod}\,m)$$
# <lo-sample/> LV.AMO.2018.11.1
Prove that all natural $n$ values run $$1^3 + 2^3 + 3^3 + \ldots + n^3 = (1 + 2 + 3 + \ldots + n)^2.$$ 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2018.11.4
Do you have subsistence numbers $m$ and $n$ you $m^2 - n^2 = 2mn$? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.AMO.2018.12.4
The natural number $B$ is derived from the $A$ of a natural number by changing its digits. Known to $A + B = 10^{45}$. Prove that both $A$ and $B$ share $5$. 
<small>
* cooked: divisibility
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2019.7.5
For one of the smallest natural $n$ values, the number $10^n$ can be expressed as the product of seven natural numbers so that the last digits of all of them are different (that is, none of them match the last digit of another number)? 
<small>
* questionType: FindOptimal
* concepts: product
</small>
# <lo-sample/> LV.AMO.2019.8.5
For one of the smallest natural $n$ values, the number $10^n$ can be expressed as a multiplication of six natural numbers so that none of them is less than the $10$ and the last digits of all of them are different (that is, none of them match the last digit of another number)? 
<small>
* questionType: FindOptimal
* concepts: product
</small>
# <lo-sample/> LV.AMO.2019.9.4
If you replaced all odd digits of a six-digit natural number with a $7$, you would get a number that is $5998$ greater than the original number. On the other hand, if the original number were to replace all the numbers in the pair with $7$, the resulting number would be $500290$ greater than the original number. Find the given six-digit number! 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2019.9.5
Is there a square equation with whole coefficients with the root $$\left( \sqrt{2020} − 2\sqrt{2019} + \sqrt{2018} \right)
\left( \sqrt{2020} + \sqrt{2019} \right) \times$$ $$\times \left( \sqrt{2019} + \sqrt{2018} \right)
\left( \sqrt{2020} + \sqrt{2018} \right)?$$ 
<small>
* cooked: quadratic-equation
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2019.10.1
Demonstrate that all natural $n$ values have the same $$6 + 24 + 60 + \cdots + n(n + 1)(n + 2) =$$ $$=\frac{n(n+1)(n+2)(n+3)}{4}.$$ 
<small>
* Topic: Numtheorymathinduction
* questionType: Prove
* cooked: equation
</small>
# <lo-sample/> LV.AMO.2019.10.4
What natural $n$ values does the expression $n^2 + n + 19$ have a square of a natural number? 
<small>
* Topic: Standardidentities
* questionType: Findall
* cooked: quare-ALG
</small>
# <lo-sample/> LV.AMO.2019.11.1
Resolve inequality $$\frac{(x-20)^{19} \cdot (x + 4)}{\left( \sqrt{x^2 + 4} \right) \left( 9-x^2 \right)} \geq 0.$$ 
<small>
* concepts: Inequality
* questionType: FindAll
</small>
# <lo-sample/> LV.AMO.2019.11.2
Two players alternately write $216$ subsistence dividers on the board number. The following rules shall be complied with in each move: * You may not rewrite an already written divider. * You may not write a divider that is directly $2$ or $3$ times larger or smaller than any divider you have already written. Loses that player who can't make a move. Which player - first or second - can always win? 
<small>
* Topic: Factorizationanddivisibility
* Topic: Gameinvariant
* seeAlso:LV.AMO.2019.12.2
* Concept: divisor
* questionType: Provedisprove
</small>
# <lo-sample/> LV.AMO.2019.11.3
On the $ABC$ edges of the triangle, the $AB$ and $BC$ have chosen the respective points in the $D$ and $E$ that they $AC \parallel DE$. The cut-offs $AE$ and $CD$ intersect at a point in the $F$. The dots $B$, $D$, $E$ and $F$ are on the same circle. The straight line $BF$ crosses the edge at the $AC$ point in the $H$ and $ABC$ the circumference of the triangle at the point in the $G$. Prove $FH = GH$. 
<small>
* cooked: Triangle, circumscribed-circle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2019.11.4
The sum of several natural numbers is known to be * * (R) * * $2019$, * * (B) * * $2020$. What is the biggest possible product of these numbers? 
<small>
* Topic: InequalityProvingStronger
* concepts: product
* questionType: FindOptimal, FindOptimal
</small>
# <lo-sample/> LV.AMO.2019.12.2
Two players alternately write $144$ subsistence dividers on the board number. The following rules shall be complied with in each move: * You may not rewrite an already written divider. * You may not write a divider that is directly $2$ or $3$ times larger or smaller than any divider you have already written. Loses that player who can't make a move. Which player - first or second - can always win? 
<small>
* seeAlso:LV.AMO.2019.11.2
* cooked: divisor
* questionType: Provedisprove
</small> 
# # solution * all dividers form a rectangular structure, where multiplication by $2$ is one axis and multiplication by $3$ is another. * This rectangle has a center of symmetry: $12 = \sqrt{144}$. * the first player starts with a $12$, then answers each division $d$ with a $144/d$.
# <lo-sample/> LV.AMO.2019.12.3
A square is given for the $ABCD$ you want to $AB = AD$ and $BC = CD$. The circle passing through the points $A$, $B$ and $C$ crosses the cut-off $AD$ and $CD$ at their inner points $E$ and $F$ respectively and the cut-off at the $BD$ point $G$. Prove $EG = FG$. 
<small>
* cooked: rectangle
* questionType: prove
</small>
# <lo-sample/> LV.AMO.2019.12.4
The sports camp has $100$ pupils. We $N$ how many ways these $100$ pupils can be divided into $50$ pairs (the order of pairs and also the order of pupils in pairs is irrelevant). What is the biggest rank of three shared by $N$? 
<small>
* Topic: Rouleofproduct
* Topic: Valuationproperties
* questionType: Findall
</small> 
# # solution calculates $N$ using the multiplication rule. For the youngest (shortest, etc.) pupil, couples can be found in $99$ ways. Of the remaining youngest student, couples can be found in $97$ ways. The last pupil is left with a directly $1$ couple. The full number of variants is expressed by the product: $$N = 99\cdot{}97\cdot{}95\cdot\ldots\cdot{}3\cdot{}1.$$ groups multipliers based on the triple they share. * $(99-3)/6 + 1 = 17$ multipliers are divided by $3$: $3 \cdot 9 \cdot 15 \cdot 21 \cdot 27 \cdot \ldots \cdot 99$. * $(99-9)/18 + 1 = 6$ multipliers are divided by $3^2$: $9 \cdot 27 \cdot 45 \cdot 63 \cdot 81 \cdot 99$ * $(81 - 27)/54 +1 = 2$ multipliers are divided by $3^3$ ($27, 81$). * one multiplier is divided by $3^4$ ($81$). When you add up the $17 + 6 + 2 + 1 = 26$ of this grade. * Note * a similar idea for adding up is also in Legander's formula, which finds the largest degree of prime that $n!$ share.
# <lo-sample/> LV.AMO.2019.12.5
The millionaire club's richest Member has exactly $8$ times less money than all the other members combined, the fourth richest Member has exactly $11$ times less money than all the other members combined, while the poorest Member has exactly $13$ times less money than all the other members combined. How many members are at this club? 
<small>
* questionType: FindCount
</small>
