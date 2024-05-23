# <lo-sample/> LV.VOL.2000.9.1
Given that $n$ is an integer. How many of the numbers in $n^2+1$, $n(n+1)$, and $3n^3-2$ are even numbers? 
<small>
* questionType: FindCount
</small>
# <lo-sample/> LV.VOL.2000.9.4
Which of the figures are $1$; $55$; $56$; $7$; $36$ can be expressed in the $\frac{1}{a_1} + \frac{2}{a_2} + \ldots + \frac{10}{a_{10}}$ form, where $a_1, a_2, \ldots, a_{10}$ - natural numbers, which can also be the same? 
<small>
* questionType: Findcount
</small>
# <lo-sample/> LV.VOL.2000.10.2
What lower natural number can I get as a value by inserting parentheses in $15:14:13:12:11:10:9:8:7:6:5:4:3:2$? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2000.11.2
Given that $a$ and $b$ - natural numbers. The $a + \frac{b}{a} - \frac{1}{b}$ value of an expression is also known to be a natural number. * * (R) * * to prove that the value of that expression is a square of a natural number. * * (B) * * can any natural $n$ be found with such natural $a$ and $b$ that $a + \frac{b}{a} - \frac{1}{b} = n^2$? 
<small>
* questionType: Prove, ProveDisprove
</small>
# <lo-sample/> LV.VOL.2000.11.4
Six different irrational figures are given. Prove that you can choose $3$ numbers from them (let's label them $x$, $y$, $z$) so that all three numbers $x+y$, for $x+z$, $y+z$ are irrational. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2000.12.5
Different natural numbers are given in the $12$. For each $5$, the smallest common digit is the same number in the $M$. It is known that $x$ numbers can be selected from the given $12$ numbers in such a way that each of the two selected is preceded by each other. * * (R) * * to demonstrate that $x \leq 4$, * * (B) * * to prove: you may $x=4$. 
<small>
* questionType: Prove, prove
</small>
# <lo-sample/> LV.VOL.2001.9.1
The length of the grasshopper jump is $5$. He is initially at a point with coordinates in the $(0;0)$ and can only travel through points for which both coordinates are integers. * * (R) * * to demonstrate that the grasshopper can reach a point with coordinates in the $(1;0)$, * * (B) * * can the grasshopper reach any point with whole coordinates? 
<small>
* Topic: Pythagoreantriples
* Topic: Outidentity
* questionType: Prove, ProveDisprove
</small>
# <lo-sample/> LV.VOL.2001.9.2
The $A$ numbers of a natural number were typed in reverse order and obtained the number $B$. $B$ appeared to be sharing the $A$. What can the split be? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2001.10.5
What natural numbers $n$ have the following characteristics: by striping the first digit of the number $2^n$, you get a double digit with a natural climber? 
<small>
* Topic: Countingobjects
* Topic: Periodicremainders
* topic:DivisibilityRulesFor3And9
* Topic: Integerfactorization
* questionType: Findall
</small> 
# # solution with experimentation finds two-tier $32$ and $64$ fit. The value ($30$ or $60$) of the striped portion of a number is a multiple of $15$ in both cases. For example: $$2^6-2^2 = 2^2(2^4-1)=2^2(8+4+2+1).$$ for a $2^n - 2^m = 2^m(2^{n-m}-1)$ to be a number that you want to underline, you must share the expression with a $5$. The following residues shall be obtained by dividing the grade $2^{n-m}$ by the $5$: | $n-m$ | 0 | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | --------------- | --- | --- | --- | --- | | --- | | | | $2^{n-m} \pmod 5$ | 1 | 2 | 4 | 3 | 1 | 1 | 3 | 1 | 2 | 2 | 2 | 1 | | $2^{n-m} \pmod 3$ | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | as $n-m \neq 0$ and necessary to share $2^{n-m}-1$ with $5$, we get $n-m > 0$ sharing with $4$. Then the $2^{n-m}$ is $16$, $256$, $4096$, $65536$, etc. * * conclusion: * * If $2^{n-m} - 1$ is shared with $5$, it is also shared with $3$. You can see it in Tablin because the leftovers (MOD 3) are also periodic. And as $n-m$ shares the $4$, it will also share the $2$. The number crossed out multiplied by the $10$ is $2^m\cdot{}(2^{n-m}-1)$. The sum of the digits of this number must be divided by $3$, but not by $9$. Only the numbers $3$, the $6$ satisfies that characteristic, so the $2^m\cdot{}(2^{n-m}-1)$ is either $3 \cdot 10^k$ or $6 \cdot 10^k$. But if these numbers are greater than $30$ or $60$, then dividing the $300$, $600$ (or $3000$, $6000$, etc.) by the ranks of two, let's only get first-time multipliers for $3$ and $5$.
# <lo-sample/> LV.VOL.2001.11.1
Prove $\sqrt[3]{5\sqrt{2} + 7} - \sqrt[3]{5\sqrt{2} - 7} = 2$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2001.11.3
Resolve equation $x^2+3^x=y^2$ in natural numbers. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2001.12.3
Resolve equation $x^2-y!=2001$ in natural numbers. (Note: $y!$ means the product of all natural numbers from $1$ to $y$ inclusive.) 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2002.9.1
For subsistence numbers, $x$ and $y$ know that $30<x<40<y<50$ and $xy$ are cubes of an integer. What are the $x$ and $y$ values? 
<small>
* Topic: Factorizationandproperties
* Topic: Exhaustionmethod
* questionType: Findall
</small> 
# # solution What numbers are full cubes * the product $xy$ is the full cube if each $xy$'s first-time multiplier rank is divided by $3$. * Many $x,y$ values (which contain first-time multipliers for $p$ other than a square that cannot be multiplied by $p^2$) can be turned off: $$\left\{ 
\begin{array}{l}
x \neq 31;\;33;\;34;\;35;\;37;\;38;\;39\\
y \neq 41;\;42;\;43;\;44;\;45;\;46;\;47;\;49\\
\end{array} \right.$$ sorts cases: * It is not possible to use first-time multipliers for $5$ and $7$ because the $y=49$ could only be put together with the $x=35$, but then the climber at the $5$ would not share three (because the $x,y \in (25;50)$). * only the first numbers for $2$ and $3$ and the following values remain: $$x = 32;\;36\;\;\mbox{un}\;\;y=48.$$ only works for $x=36$, $y=48$. Then $xy=2^63^3$ and $\sqrt[3]{xy}=12$.
# <lo-sample/> LV.VOL.2002.10.4
For which natural numbers is the $n$ number $n\cdot{}2^{n-1}$ a square of a natural number? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2002.10.5
On the board, initial integers from $0$ to $1024$ inclusive are written from time to time. Players $A$ and $B$ play the following game. First, the $A$ clears the $2^9=512$ numbers. The $B$ then clears the $2^8=256$ numbers. The $A$ then clears the $2^7=128$ numbers. The $B$ then clears the $2^6 =64$ numbers, etc., while the $B$ clears the $2^0=1$ number with the last move. Two numbers remain on the board; let's label them $x$ and $y$. The player $A$ wants the $\left| x-y \right|$ to be as big as possible; $B$ wants the $\left| x-y \right|$ to be as small as possible. How much $\left| x-y \right|$ value can $A$ achieve? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2002.11.2
There are $m$ candy in one pile, $n$ candy in the other. One move can either eat one candy, or eat one candy at a time from each pile, or transfer one candy from one pile to another. Who can't make a move loses. Andris and Juris make one move in a row; Andris goes first. Who wins by playing properly? 
<small>
* questionType: Algorithm
</small>
# <lo-sample/> LV.VOL.2002.11.5
For which natural numbers in $n$ greater than $3$ and not shared with $3$, the following characteristic shall be fulfilled: all those subsistence numbers below $n$, whose largest common divider with $n$ is $1$, make an arithmetic progression? 
<small>
* Topic: Integerfactorization
* Topic: Arithmeticandgeometricseries
* questionType: The Findall
</small> 
# # solution * fits all the source numbers in the $n>3$ because the numbers below the $n$ that are the primary numbers with the $n$ are the following: $1,2,\ldots,n-2,n-1$ * is valid for all grades of $2^k > 3$ because the interchangeable primary numbers are all odd numbers: $1,3,5,\ldots,2^k-3,2^k-1$. Other numbers Don't work Let's say $n = (2k+1)2^m$ is a paired number that isn't a $2$ grade and doesn't share $3$. If the $n$ is a paired number, then the $2k+1 > 1$ and it have an odd divider. So there $1,3,\ldots,n-1$ be some number $n$ divider in progression. For similar reasons, odd numbers other than primary numbers but not shared with $3$ are also not valid.
# <lo-sample/> LV.VOL.2002.12.1
If $a$ and $b$ - natural numbers, then we $(a,b)$ the $a$ and $b$ the largest common divider. Find the highest possible $(4n+3,6n+1)$ value if $n$ is a natural number. 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2003.9.1
A natural number is called symmetric if reading its decimal note from the other end produces the same number. For example, the numbers in the $111$ are symmetrical; $424$; $88$; $5225$; $7$. All six-digit symmetric subsistence numbers are known to share the natural number $x$. What can $x$ values be? 
<small>
* topic:DivisibilityRuleFor11
* Topic: Extremeelementmethod
* Topic: Euclideanalgorithm
* questionType: Findall
</small> 
# # solution number $\overline{abccba} = 100001a + 010010b + 001100c$ sure shares $11$ (a sign of division, as well as $100001$, $10010$, $1100$ share $11$). Is $11$ the largest common divider for all six-digit symmetric numbers (So - the highest possible $x$ value)? We find the largest common divider for symmetric six-digit numbers in $100001$ and $101101$: $$\mbox{LKD}(101101,100001) = \mbox{LKD}(100001,1100).$$ * number $1100 = 2^2 \cdot 5^2 \cdot 11$, but $2$ and $5$ do not share $100001$. So $x=11$ is the biggest value of $x$. You can also have a value of $x=1$.
# <lo-sample/> LV.VOL.2003.10.2
Given that $a$ and $b$ are natural numbers, the $a$ does not share $5$. The string of numbers in the $x_1, x_2, x_3, \ldots$ is composed of the following: for $x_1 = 5$, for $x_{n+1} = ax_n + b$, if $n=1;2;3;\ldots$. What major $k$ value is it possible that all numbers in the $x_1;x_2;x_3;\ldots;x_k$ are primary numbers? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2003.11.2
In a string of natural numbers, the first Member of the $a_1, a_2, \ldots$ is arbitrarily chosen by the $a_1$ and there is an equal $a_{n+1} = a_n^3 + 2003$ at the $n \geq 1$. What is the largest amount of string members that can be natural number squares? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2003.12.1
Is there a * * (B) * * natural numbers $x$, $y$ and $z$ greater than the $1$ that $x! \cdot y! = z!$? * * (B) * * natural numbers $a, b, c, d, e$ larger than the $1$ that $a! \cdot b! \cdot c! \cdot d! = e!$? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2003.12.4
In the “table”, the upper line is divided into natural figures from $1$ to $5$; in the following lines, each number equals the sum of the two numbers written above it. What number is at the bottom “top” of a table that is similar and has natural numbers from $1$ to $2003$ inclusive written on the top line?! [] (LV.VOL.2003.12.4.png) 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2004.9.3
John wants to write $n$ different natural numbers so that the sum of any six numbers he writes doesn't share with $6$. Is this possible if * * (R) * * * $n=10$, * * (B) * * $n=11$? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2004.10.3
Various source numbers are written on the board, the arithmetic mean of which is $27$. What is the highest source number that can be written on the board? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2004.11.2
What source numbers does $a$ and $b$ number $a^2 + 3ab + b^2$ have a natural number square? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2004.12.5
Given that there is a relationship between $x_1 = 3$, $y_1 = 4$, and each subsistence $n$ in $$x_{n+1} = 3x_n + 2 y_n,\;\; y_{n+1} = 4x_n + 3y_n.$$ to prove that none of the numbers in the $y_1, y_2, y_3, \ldots$ is a subsistence number cube. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2005.9.2
Given that $B$ is a natural number, a sum of $A=7\cdot{}B$ and $A$ digits twice the sum of $B$ digits. The number $C$ is obtained by writing down the number $B$ at the end of the $A$. * * ((R) * * Find any such $C$, * * (B) * * proving that there are infinite numbers of such $C$, * * (C) * * proving that each such $C$ shares $9$, * * (D) * 
<small>
*
* is the $C$ sure to share $27$?
* questionType: Findexample, prove, ProveDisprove
</small>
# <lo-sample/> LV.VOL.2005.9.4
Given that in $a$ and $b$, real figures such that a + b is a whole number and $a^2+b^2=2$. Find all such pairs of $a$ and $b$ and prove there are no others without what you find. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2005.9.5
Each natural number, from $1$ to $2005$ inclusive, is painted in one of the $n$ colors. It is known: if $a$, $b$, and $c$ have different numbers, $a$ share $b$, and $b$ share $c$, then $a$, $b$, and $c$ aren't all painted the same color. Find the smallest possible $n$ value. 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2005.10.3
What functions do $f$ have at the same time the following characteristics: a. the $f$ definition area is $\{1; 2; 3; 4; 5; 6; 7; 8; 9; 10\}$, b. $f$ values are natural numbers that do not exceed $100$, C. $f$ is a growing function, d. for all $x$ and $y$ from the definition area, the number $x\cdot{}f(x)+y\cdot{}f(y)$ is divided by the $x+y$? 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2005.11.4
Given that $p$ is the primary number. To prove that the claims &quot;exist in such a whole $x$ that $x^2+x+3$ share $p$” and “there exists such a whole $y$ that $y^2+y+25$ share $p$” either both are correct or both are wrong. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2005.12.4
About a string of numbers, it is $x_1, x_2, x_3, \ldots$ known that * $x_1=1$ * $x_{2n}=1+x_n$ to all natural $n$ * $x_{2n+1} = \frac{1}{x_{2n}}$ to all natural $n$. * * (R) * * Specify that all members of the string are different. * * (B) * * which numbers are members of this string? 
<small>
* questionType: Prove, FindAll
</small>
# <lo-sample/> LV.VOL.2006.9.1
Resolve equation $x + y = 1025$ when $x$ and $y$ have natural numbers - number $640000$ dividers. 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2006.10.2
For which source numbers do $p$ and $q$ that do not exceed $100$, all numbers in $p+6$, $p+10$, $q+4$, $q+10$, and $p+q+1$ also have primary numbers? 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2006.10.5
One of the smallest subsistence numbers in $n$ has the following characteristics: by painting some of the natural numbers in the $1$ in any way; $2$; $3$; $\ldots$; when you $n$ white and the rest red, a resolution exists for equation $x + y + z = t$, where the values of all four variables are the same color (these values can also be the same with each other)? 
<small>
* questionType: Findoptimal
</small>
# <lo-sample/> LV.VOL.2006.11.2
In a series of real numbers, the $(a_n)$, for $n = 1; 2; 3; \ldots$, selects the first Member arbitrarily in the $a_1$, and calculates each subsequent Member according to the formula $a_{n+1} = a_n(a_n+2)$, for $n=1; 2; 3; \ldots$. What values can $a_{2006}$ accept? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2006.11.3
Resolve equation $(x+y)(xy+1) = 2^z$ in natural numbers. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2006.12.1
Prove $$\left( 1 + tg 1^{\circ} \right) 
\left( 1 + tg 2^{\circ} \right) 
\left( 1 + tg 3^{\circ} \right) 
\ldots
\left( 1 + tg 44^{\circ} \right) 
\left( 1 + tg 45^{\circ} \right) = 2^{23}.$$ 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2006.12.4
The natural numbers $m$ and $n$ satisfy the following characteristic: $m$ shares any of the numbers in the $1; 2; 3; \ldots ; n$, but does not share $n + 1$, $n + 2$, or $n + 3$. What are the possible $n$ values? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2007.9.2
* * (R) * * can it happen that for each of the square equations, $x^2 + (p+1)x + (q+1) = 0$, $x^2 + px + q = 0$, and $x^2 + (p+2)x + (q+2) = 0$, both roots are integers? * * (B) * * can it happen that, besides, for each of the square equations, the $x^2 + (p-1)x + (q-1)=0$ and $x^2 + (p-2)x + (q-2) = 0$ both roots are integers? (Roots can also be the same.) 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2007.9.5
! [Squares] (LV.VOL.2007.9.5 png) * * (y) * * * or you can type natural numbers from $1$ to $9$ (another number in each box) in the boxes in the table shown in Figure 1 so that the property is fulfilled: if the row and column are labeled in the same letters, the multiplication of the numbers that you type in them is the same? * * (B) * * can you type natural numbers from $1$ to $81$ (another number in each box) in the boxes in the table shown in Figure 2 so that the same attribute is true? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2007.10.1
Do you have natural numbers $x$ and $y$ that the expression $x^2 - y^2 - x + y$ value is * * (P) * * $10$, * * (B) * * $2007$? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2007.10.3
If $n$ is a natural number greater than $1$, then we $x(n)$ the largest primary number that does not exceed $n$, and the lowest primary number that exceeds $n$ is $y(n)$. For example, $x(6) = 5$; $x(5) = 5$; $y(5) = 7$. Prove $$\frac{1}{x(2)\cdot{}y(2)}+
\frac{1}{x(3)\cdot{}y(3)}+
\frac{1}{x(4)\cdot{}y(4)}+\ldots+
\frac{1}{x(600)\cdot{}y(600)} = \frac{1}{2} - \frac{1}{601}.$$ 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2007.10.5
A sheet of paper shall bear n different natural numbers not exceeding $14$. It is known: each of the subsistence numbers in the $1;2;3;\ldots;27$ can be pronounced either as a $x$, as a $2x$, or as a $x + y$ where you $x$ and $y$ - some sort of written numbers. Prove that * * (R) * * $n \geq 6$, * * (B) * * $n \geq 7$. 
<small>
* questionType: prove, prove
</small>
# <lo-sample/> LV.VOL.2007.11.1
Given that $n$ - a natural number. * * (R) * * can the numbers $n$ and $n+2007$ have the same numbers? * * (B) * * can the numbers $n$ and $n+199$ have the same amounts? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2007.11.5
A string of real numbers $a_1, a_2, a_3, \ldots$ that $a_{11} = 4$, $a_{22} = 2 un $ a _ {33} = 1 $.
Bez tam visiem naturāliem $ n $ pastāv vienādība
§id1§
Pierādīt, ka  
**(A)** neviens virknes loceklis nav $ 0 $,  
**(B)** virkne ir periodiska,  
**(C)** $ a_1^k + a_2^k +\ ldots + a _ {100} ^ k $
ir naturāla skaitļa kvadrāts, ja $ k $- arbitrary natural number. 
<small>
* questionType: Prove, prove, prove
</small>
# <lo-sample/> LV.VOL.2007.12.5
The set of subsistence numbers is divided into parts so that each subsistence number ends up in exactly one part and each part contains infinite numbers. Will there definitely be one between the parts that contains a multiple of any natural number? Answer this question if * * (R) * * parts are final, * * (B) * * parts are endless. 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2008.9.1
Given that $x$ and $y$ are natural numbers. Prove that the smallest subsistence number that shares both $x$ and $y$ is not $x+y$. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2008.10.2
Which natural numbers $x$ have the following characteristics: by deleting the last three digits of the $x$, you get the $\sqrt[3]{x}$? 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2008.10.3
If $x$ and $y$ - natural numbers (maybe the same), then we $[x,y]$ denote their smallest common dividend. What natural numbers can $n$ express in the $n = [x,y] + [y,z] + [z,x]$ form? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2008.11.2
Resolve equation $$\left| \ldots 
\left|\left|\left| x-1 \right| - 10 \right| - 10^2 \right| - 
\ldots - 10^{2007} \right| = 10^{2008}$$ 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2008.11.3
Given that the $n$ - a natural number and the $n^2$ of a number in the decimal note - one digit is “2” and the other digits are “1”. Prove $n$ is sharing $11$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2008.12.3
Resolve equation $$x^2 + \left( x + 1 \right)^2 = y^2,\;\;\mbox{ja $ x\ Leq 200 $}.$ $
<small>
* questionType: FindAll
</small> in natural numbers
# <lo-sample/> LV.VOL.2009.9.2
A natural number is called simple if it is the product of two (equal or different) primary numbers. For example, the $9=3\cdot{}3$ is simple and the $18=2\cdot{}3\cdot{}3$ is not. What's the greatest amount of consecutive natural numbers can all be simple? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2009.10.2
We look at a string that contains all non-$3$ subsistence numbers in ascending order. The beginning of the series is therefore $$1; 2; 4; 5; 7; 8; 10; 11; \ldots$$ given that the sum of the $2n$ successive members of the string is $300$ (for $n$, some kind of natural number). What are the possible $n$ values? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2009.11.1
We look at a string of numbers in the $F_1=1$; $F_2=2$; $F_{n+2}=F_{n+1}+F_n$ to the $n \geq 1$. What is the largest amount of elements in this string that can make one arithmetic progression? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2009.11.2
Find a $3^3-3$ of numbers. $5^5-5$; $7^7-7$; $\ldots$; $2009^{2009}-2009$ the largest shared divider. 
<small>
* questionType: Findexample
</small>
# <lo-sample/> LV.VOL.2009.12.2
Catherine wrote a three-digit number for $n$, whose numbers are all different and all different from $0$. Maya wrote all five other three-digit numbers made up of the same numbers as the $n$. The sum of the numbers Maya has written is $3434$. What can the number $n$ be? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2010.9.1
Is it possible that the $x^2-ax+b=0$, $a$, and $b$ of the square equation - natural numbers, roots are squares of two different natural numbers? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2010.9.3
Let's call a natural number that doesn't share any of the digits in its decimal note * beautiful * (No number shares $0$). What the greatest amount of consecutive natural numbers can all be * beautiful *? 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2010.11.4
A string of Fibonacci numbers is called a string of $F_1=1$; $F_2=1$; $F_{i+2}=F_i+F_{i+1}$ at the $i \geq 1$. Prove that each natural number in a $n$ string of Fibonacci numbers has a string Member that shares $n$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2010.12.2
Given number string $a_1=1$; $a_2 = 1$; $a_i = p\cdot{}a_{i-1} + q\cdot{}a_{i-2}$ at $i \geq 3$ (for $p$, for $q$, subsistence figures are given). It is known that for each natural number in the $n$, such a string Member $a_k$ that the $a_k$ shares the $n$ exists. Prove $p=q=1$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2010.12.4
Natural numbers from $1$ to $k$ are written around the circle in some order (each exactly once). Each $d$ is known, for $2 \leq d \leq k-1$, to have the following characteristics: dividing by $k$ all possible amounts of $d$ sequential numbers gives all possible balances. Is it possible that * * (R) * * $k=7$, * * (B) * * $k=8$? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2011.9.1
The $4023$ square equations in the $x^2 + ax + b = 0$ form are given. All integers from $-2011$ to $2011$ (inclusive) are present among the $a$ values of all equations, and all integers from $-2011$ to $2011$ (inclusive) are present among the $b$ values. Can all given equations have roots in integers? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2011.9.3
Show that of all three-digit numbers whose notation does not contain a numeric $0$, you can select an 81-digit number so that the following three characteristics can be met simultaneously: 1. by deleting the first digit in all selected numbers, each double digit number, which does not contain $0$, is obtained directly once; 2. by deleting the second digit in all selected numbers, each double digit number, which does not contain $0$, is obtained directly once; 3. by deleting the third digit in all selected numbers, each double digit number that contains no $0$ is obtained exactly once. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2011.10.5
Polynomial $f(x)$ with whole coefficients is given. May be $f(2011) = 100$ but $f(11) = 1000$? 
<small>
* Topic: PolynomialDifferenceDivisibility
* Topic: AdvancedIdentities
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2011.11.3
Find all source numbers for $p$ for which $p^{p^2 - 5} + 2$ is also a primary number. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2011.12.3
Prove that there are no subsistence numbers for $n$ and $m$ that have true uniformity in $\left( 2n \right)^{2n}-1 = m^3$. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2012.9.1
* * * (B) * * * can the product of five consecutive natural numbers be a number $20112012$? * * (B) * * * or can the product of four consecutive natural numbers be a number $20112012$? 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2012.10.3
The decimal note for a natural number $N$ uses only the number $6$. Prove that the number $N^2$ in the decimal notation does not contain a number $0$. 
<small>
* strategy: Trialanderror
* Topic: Seriesmemberssumsclosedformulae
* Topic: Periodicdigitgroups
* questionType: Prove
</small> 
# # resolve shows you how to increase the $66\ldots{}66$ square $$6^2=36,\;\;66^2=4356=4455-99,\;\;666^2=443556=444555-999,\ldots$$, let's say that $$\begin{aligned}
(\underbrace{6\ldots6}_n)^2 & = \overline{\underbrace{4\ldots{}4}_n\underbrace{5\ldots{}5}_n}-\underbrace{9\ldots{}9}_n, \\
\left( 6\cdot(10^n-1)/9 \right)^2 & = 10^n \cdot (4 \cdot (10^n - 1)/9) +(5 \cdot (10^n - 1)/9) - (10^n-1), \\
\frac{4}{9}(10^n-1)^2 & = 10^n \cdot \frac{4}{9}(10^n - 1) +\frac{5}{9}(10^n-1) - (10^n - 1), \\
4(10^n - 1)^2 & = 4\cdot{}10^{2n}-4\cdot{}10^n + 5\cdot{}10^n-5 - 9\cdot{}10^n +9.
\end{aligned}$$ So the $\overline{6\ldots6}^2$ note contains only the numbers “4”, “3”, “5”, and “6”: $$(\underbrace{6\ldots6}_n)^2=\overline{\underbrace{4\ldots{}4}\_{n-1}3\underbrace{5\ldots{}5}\_{n-1}6}$$
# <lo-sample/> LV.VOL.2012.11.1
Prove that there are endless $a$ of natural numbers for which the number $n^4 + a$ is a composite number for all natural numbers $n > 1$. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2012.11.4
Provides a string of natural numbers in the $(a_i)$ where you want to $a_1=5$ and $a_n = a_1 a_2 \ldots a_{n-1}+4$ each $n>1$. Prove that all $n \geq 1$ have a $a_n - \sqrt{a_{n+1}}=2$ relationship. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2012.12.1
Two strings of natural numbers, $(a_i)$ and $(b_i)$, have a relationship for each $i \geq 1$: $$a_{b_i} = b_{a_i}\;\;\mbox{un}\;\;a_i-b_i > 2012.$$ to find one example of the following strings. 
<small>
* questionType: Findexample
</small>
# <lo-sample/> LV.VOL.2012.12.3
Resolve equation $$n = \left\lfloor \frac{n}{2} \right\rfloor + 
\left\lfloor \frac{n}{3} \right\rfloor + 
\left\lfloor \frac{n}{4} \right\rfloor + 
\ldots + 
\left\lfloor \frac{n}{n+2012} \right\rfloor.$$ in natural numbers ($\lfloor x \rfloor$ is the whole of the $x$ - the largest integer not exceeding the $x$; e.g., $\lfloor 3 \rfloor=3$, $\lfloor 4,6 \rfloor =4$, $\lfloor 0,2 \rfloor =0$, etc.) 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2013.9.1
Find numeric $a$, $b$, $c$, and $d$ values for $\overline{abcd} + \overline{abc} + \overline{ab} + a = 2013$. 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2013.9.3
Gives a string of $a_1, a_2, a_3,\ldots$ where the $a 1 = a 2 = 1$ and all $n > 2$ run the calculate $a_{2013}$ $$a_{n+1} = \left\lfloor
\frac{2a_n + a_{n-1}}{3} 
\right\rfloor + 4.$$. ($\lfloor x \rfloor$ is the whole of the $x$ — the largest integer not exceeding the $x$; for example, $\lfloor 3 \rfloor =3$, $\lfloor 4,6 \rfloor =4$, $\lfloor 0,2 \rfloor =0$, etc.) 
<small>
* questionType: Findexample
</small>
# <lo-sample/> LV.VOL.2013.10.1
Prove that equation $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2}=\frac{1}{2}$ has no solution in natural numbers. 
<small>
* Topic: Countingusingsymmetry
* Topic: Numtheoryinequalitylargeintervals
* questionType: Prove
</small> # solution initial conclusions on variables assume $a \leq b$ (If not, the $a$ and $b$ are replaced). * If $a \geq 6$, then $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} < \frac{1}{2}$ * If $a \leq 2$, the case of $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} > \frac{1}{2}$ * $a=3$: - If $b=6$, then $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} > \frac{1}{2}$ - at the $b=7$, then the case of $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} < \frac{1}{2}$ * $a=4$: - If $b=4$, then $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} > \frac{1}{2}$ - If $b=5$, you may not look at $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} < \frac{1}{2}$ other $b$ values, because for a given $a$ ($a=3$ or $a=4$), the expression $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2}$ decreases as the $b$ increases.
# <lo-sample/> LV.VOL.2013.10.4
Dot Fibonacci's string of numbers in $F_1 = F_2 = 1$, $F_{i+2} = F_i + F_{i+1}$. Prove that this string contains infinite numbers other than the squares of a natural number. 
<small>
* Topic: Fibonaccinumbers
* Topic: Periodicremainders
* Topic: Modularithmetic
* questionType: Prove
</small> 
# # resolve finds Fibonacci String remnants divided by 3: | $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | | --------- | $F_n$ | 1 | 2 | 3 | 5 | 8 | 13 | 21 34 | 55 | | $F_n \pmod 3$ | 1 1 1, 2 | 2 | 2 | 1 | 0 1, 1, 1, | | $F_1 \equiv F_9 \equiv 1$ $3$ module (So starting with the ninth Member, the same eight-remainder period will repeat again: $1,1,2,0,2,2,1,0$). * No full square can give the remainder to the $2$, divided by $3$, as $(3k+1)^2$ and $(3k+2)^2$ give the remainder to the $1$. * in Fibonacci's string, the remainder $2$, divided by $3$, will appear infinitely often - $x_3$, $x_5$, $x_6$ (and also $x_{2+8k}$, $x_{2+8k}$, $x_{2+8k}$ for any $k$). * all of these will not be squares of a natural number. Sure, the * * actually * * squares between members of the Fibonacci String are even considerably less (of the above, only $1=1^2$ and $144=12^2$). In this exercise, however, it should be justified that the behaviour of a string cannot change from one place to another in such a way that all sufficiently large members of the string are squares. * * claim: * * (1) divided by any fixed number, the residual members of the Fibonacci string form the period. (2) the periodic series of balances does not have a precursor and is infinitely characterised by the presence of a residual $0$. * * proof: * * (1) Each remaining Member of the Fibonacci String is determined by the balances of the two previous members. As soon as the pair of two consecutive balances coincide with the one that used to be, the Fibonacci string remains start to recur, a cycle develops. (2) preperiods cannot occur in the balance string because balances can also be calculated in reverse order: unequivocally finding the $F_i$ balance from $F_{i+2}$ and $F_{i+1}$ residues. So the series of balances is periodic in both directions (rather than just becoming periodic from somewhere). As the $0$ Fibonacci figure $F_0 = 0$, the remainder will $0$ appear infinitely frequently (at least once in each period).
# <lo-sample/> LV.VOL.2013.11.1
Prove that there is no subsistence n value that the $n^2 + 4n + 16$ shares with the $36$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2013.12.3
The $f$ function meets the following requirements: 1) the $f$ is defined for all non-negative integers and its values are integers; 2) Each $n$ (for $n$, a whole nonnegative number) has a relationship that $$f(n) \cdot (f(n+1 )-2) = 4n^2-1.$$ you to find all of the following functions in the $f$ and prove that there are no others. 
<small>
* questionType: Findall
</small>
# <lo-sample/> LV.VOL.2013.12.4
By $d_i$, for $i = 1,2,\ldots,k$, let's refer to all the subsistence divisions of the $n$ of the subsistence number, plus $d_1 < d_2 < d_3 < \ldots < d_k$. Given that $d_3^2 d_4^2 \left( d_3^2 + d_4^2 \right) = n^2$. Find all possible $n$ values. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2014.9.2
The first three members of a string of natural numbers are equal to the $1$, and each subsequent is equal to the sum of the preceding three numbers. How many of the first * * (R) * * * $100$, * * (B) * * * $2014$ members of the string are those sharing $5$? 
<small>
* questionType: Findcount, FindCount
</small>
# <lo-sample/> LV.VOL.2014.10.2
Find all integer $n$ values that have integers in both $\frac{n^3+3}{n+3}$ and $\frac{n^4+4}{n+4}$. 
<small>
* Topic: Polynomiallongdivision
* Topic: Divisornumberandsum
* questionType: Findall
</small> 
# # solve polynomials (like natural numbers) can be divided by remainder. * * claim: * * If $A(x)$ and $B(x)$ are polynomial, the degree of $A(x)$ is at least as large as $B(x)$, then there are two other polynomial $Q(x), R(x)$ $A(x)=Q(x)B(x)+R(x).  
$ Q (x) $ sauc par *dalījumu*, bet $ R (x) $ - par *atlikumu*.  
$ R (x) $ pakāpe ir mazāka nekā $ B (x) $ pakāpe.

Var gadīties, ka atlikums $ R (x) = 0 $, ja $ A (x) $ izdalās ar $ B (x) $ bez atlikuma. 
Var arī gadīties, ka $ R (x) $ ir konstante – t.i. $ 0 $-tās pakāpes polinoms.

**Pirmais dalīšanas piemērs:**

§id1§

Vajag, lai $ 24 $ dalās ar $ n +3 $.

**Otrais dalīšanas piemērs:**

§id2§

Vajag, lai $ 260 = 2\ cdot {} 2\ cdot {} 5\ cdot {} 13 $ dalās ar $ n +4 $ jeb 

§id3§ 
§id4§


Atradīsim tos veselos $ z $, kuriem dalījums $\ FRAC {24} {x} $ (vai $\ FRAC {260} {x} $) ir vesels?
Dalām pirmreizinātājos.

§id5§

Cik šādiem skaitļiem ir dalītāju?

**Apgalvojums:** Ja skaitlis $ N $ dalās ar $ 2 $ dažādiem pirmskaitļiem
($ N=p_1^ {A_1} p_2^ {a_2} $) tad visi veselie $ N $ dalītāji ir formā:  
$ d =\ pm p_1^ {b_1}\ cdot {} p_2^ {b_2} $, kur $ b_1\ Leq A_1 $ un $ b_2\ Leq a_2 $.  
(Analoģiski arī lielākam pirmskaitļu skaitam.)

Piemēram, $ N = 24 = 2 ^ 3\ cdot {} 3 ^ 1 $ dalītāji ir $ d = 2 ^ {b_1} 3 ^ {b_2} $,
kur $ b_1\ in\ {0.1, 2.3\} $, $ b_2\ in\ {0.1\} $.


Meklējam divu kopu šķēlumu:

§id6§

un

§id7§

No šejienes $ (n +4)\ in\ {-5, -2, -1, 2, 4, 5, 13\} $ jeb
$ n\ in\ {-9, -6, -5, -2, 0, 1, 9\} $.
# <lo-sample/> LV.VOL.2014.10.3
There are unlimited $7$ and $13$ cent postage stamps available that are used to pay mailings. Sorry, some amounts can't be paid with these postage stamps alone (for example, if the item pays $6$, $8$ or $25$ centers). What is the highest amount that cannot be paid with these postage stamps alone? 
<small>
* Topic: Arithmeticseriesall
* Topic: Numtheoryinequalitylargeintervals
* questionType: Findoptimal
</small> 
# # solution sorted based on how many $13$ cent postage stamps used * $0\cdot{}13 + 7a$ - divided by $7$, remainder is $0$ * $1\cdot{}13 + 7a$ - divided by $7$, remainder is $6$ * $2\cdot{}13 + 7a$ - divided by $7$, remainder is $5$ * $3\cdot{}13 + 7a$ - divided by $7$, remainder is $4$ * $4\cdot{}13 + 7a$ - divided by $7$, remainder is $3$ * $5\cdot{}13 + 7a$ - divided by dalot, remainder is $2$ * $6\cdot{}13 + 7a$ - divided by $7$, remainder is dalot * * - divided by $7$, remainder is $1$ * conclusion: * * It takes at least six $13$ cent stamps to pay off $8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, \ldots$ cents. The smallest such amount is $6\cdot{}13 = 78$. Therefore, the $71$ of amounts in this string immediately prior to the $78$ (and also gives the balance to the $1$ divided by the $7$) will not be able to be paid, as using less than six $13$ - cent stamps cannot give the balance to the $1$ divided by the $7$.
# <lo-sample/> LV.VOL.2014.11.2
Determine the highest number, how many of the five natural numbers $a$, $a+14$, $a+22$, $a+46$, $a+32$ can be primary numbers. 
<small>
* questionType: Findoptimal
</small>
# <lo-sample/> LV.VOL.2014.11.5
Natural numbers are $a$, $b$, and $c$ bound by the relationship in $c^2 = a^2 + b^2$. Prove that each of the numbers $c^2+ab$ and $c^2-ab$ can be expressed as the sum of two squares of natural numbers. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2014.12.2
$f(n)=\frac{1}{1} + \frac{1}{2} + \ldots + \frac{1}{n}$ is defined for each natural number in the $n$. Prove that all $n > 1$ have a $$n + f(1) + f(2) + \ldots + f(n-1) = n\cdot{}f(n).$$ 
<small>
* questionType: prove
</small> relationship
# <lo-sample/> LV.VOL.2014.12.5
Can a natural $n$ value with a characteristic be found: the sum of all the $n$ subdivisions except $1$ and $n$ in a number is equal to $n^2$. 
<small>
* questionType: Provedisprove
</small>
# <lo-sample/> LV.VOL.2015.9.1
Find all natural numbers for $n$ and $m$ that also have a natural number in the $\frac{2015}{n^4 - m^4}$! 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2015.9.3
Aija selects a natural number in the $n \leq 100$ and creates a string of numbers where each subsequent Member of the string is obtained by the following law: * If $2n \leq 100$, the next Member of the string shall be $2n$; * If $2n > 100$, the next Member of the string is $2n-100$. If the number $n$ ever appears again in the string, we'll call the number $n$ * pleasant *. How many perfectly pleasant numbers do not exceed $100$? For example, the number $40$ is pleasant because $\underline{40}; 80; 60; 20; \underline{40}; \ldots$ and $25$ is not because $25; 50; 100; 100; \ldots$ (There are no numbers different from $100$ in the string below). 
<small>
* questionType: FindCount
</small>
# <lo-sample/> LV.VOL.2015.10.2
Prove that for each natural $n$, the expression $3n^5+5n^4-8n$ shares $10$. 
<small>
* Topic: Divisibilityproperties
* Topic: Modularparity
* Topic: Modularithmetic
* questionType: Prove
</small> 
# # solve * divide by $10$ checks divided by $2$ and $5$ * $3n^5 + 5n^4 - 8n$ is always a paired number (see if $n$ is paired/odd) * $3n^5 + 5n^4 - 8n$ divided by $5$ gives the same balance as $3n^5 - 3n$ - If $n$ shares $5$, then $3n(n^4-1)$ shares $5$ (so also $5$). - all other $n$ balances divided by $n$ (balances $1,2,3,4$) get: $n^4 - 1$ shares $5$ to insert numbers in $n=1,2,3,4$ expression $n^4-1$: will always share the $5$. For larger numbers ($n=6,7,8,9$), these balances will start to recur.
# <lo-sample/> LV.VOL.2015.11.1
The $$(1+\sqrt{5})x^2 - \sqrt[4]{7}\cdot{}(1 + \sqrt{5})^2x + \sqrt[4]{7} = 0$$ roots of the square equation are numbers $a$ and $b$. Prove expression $a^4b + ab^4+ 3a^3b^2 + 3a^2b^3 + 16a^4b^3 + 16a^3b^4$ value is Integer! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2015.11.4
Natural numbers in $a$, $b$ and $c$ are each other's primary numbers and all are larger than $50$. $a+b$ is known to share $c$ and $b+c$ is known to share $a$. Find the smallest possible $b$ value! 
<small>
* questionType: FindOptimal
</small>
# <lo-sample/> LV.VOL.2015.12.3
Prove that for any natural odd number, the $n$ expression $2269^n + 2151^n + 1389^n - 1779^n$ shares the $2015$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2016.9.1
$x$ and $y$ are known to have subsistence numbers that $xy^2$ is a cube of a natural number. Prove $x^2y$ is a subsistence number cube too! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2016.9.4
Find the smallest first time multiplier for a number $\frac{2016^{2016}-3}{3}$! 
<small>
* questionType: FindExample
</small>
# <lo-sample/> LV.VOL.2016.9.5
A series of natural numbers shall be $(s_i)$ by the model “2016” as follows: * the first Member of the string is $2$ $s_1$; * Second Member of the string in $s_2$ - the smallest natural number greater than the $s_1$ and the number $0$ in its notation; * third Member of the string in $s_3$ - the smallest natural number greater than the $s_2$ and the number $1$ in its notation; * the fourth Member of the string $s_4$ – the smallest natural number greater than the $s_3$ and the number $6$ in its notation. Then the digits you're looking for recur cyclically: 2-0-1-6-2-0 - $\ldots$. The first members of the string are $2; 10; 11; 16; 20; 30; 31; 36; 42; 50$. What are the next four numbers that follow the number $2016$ in a string? 
<small>
* questionType: FindExample
</small>
# <lo-sample/> LV.VOL.2016.10.1
$x$ and $y$ are known to have subsistence numbers such that the $xy^{10}$ is grade 33 of a natural number. Prove that $x^{10}y$ is also the 33 rd tier of a natural number! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2016.10.4
In the Pythagor triangle, the lengths of all sides are larger than the $5$. Can it happen that its * * (a) * * three-edge, * * (b) * * two-edge lengths are primary numbers? * Note: * a pitagor triangle is a rectangular triangle for which all edge lengths are natural numbers. 
<small>
* questionType: Provedisprove
</small> 
# # Recommendation can use parity - analyze instances where edge lengths are even (odd numbers). 
# # Recommendation to insert Pitagor's three numbers into an algebraic identity - a square difference formula. 
# # resolution * * (R) * * No, three edge lengths cannot be primary numbers. In a rectangular triangle, the edges lengths $a$, $b$ and $c$ satisfy Pitagor's theorem: $a^2 + b^2 =  c^2$. At least one of the numbers in the $a$, $b$, $c$ is an even number because the $a^2$ and $b^2$ amount of two odd numbers cannot be an odd number in the $c^2$. Because $a,b,c>5$, the even number is certainly not a prime number. * * (B) * * Yes, the two-edge lengths can be prime numbers. For example, the length of the edges $11, 60, 61$ because two of them are primary numbers and the Pitagor theorem condition, that is, $11^2 + 60^2 = 61^2$ or $121 + 3600 = 3721$, is met. * Note: * The question remains unanswered - how do you guess these numbers $(11,60,61)$? Infinitely many Pitagorian triplets in $(a,b,c)$ for which the $b + 1 = c$ (1 unit shorter than hypotenuse) can be obtained by an algebraic relationship: in $$a^2 = c^2 - b^2 = (c+b)(c-b) = (c + b) \cdot 1 = c+b.$$, we can find different pairs of adjacent numbers in $(b,c)$ that amount to an odd square of $a^2$: * $3^2 = 9 = 4 + 5$, so $(a,b,c) = (3,4,5)$ is a Pitagor trio. * $5^2 = 25 = 12 + 13$, so $(a,b,c) = (5,12, 13)$ is a Pitagor trio. * $7^2 = 49 = 24 + 25$, so $(7,24,25)$ is a Pitagor trio. * $9^2 = 81 = 40 + 41$, so $(9, 40,41)$ is a Pitagor trio. * $11^2 = 121 = 60 + 61$, so $(11,60,61)$ is a Pitagor trio. And the three $(11,60,61)$ is one that contained two primaries. Some other solutions, such as $(19, 180, 181)$, also work. See [Euclid formula for Pitagor triplets] (https://en.wikipedia.org/wiki/pythagorean_triple#generating_a_triple).
# <lo-sample/> LV.VOL.2016.11.1
$x$ and $y$ are known to have subsistence numbers that $xy^{433}$ is the 2016 rank of a natural number. Prove that $x^{433}y$ is also the 2016 rank of a natural number! 
<small>
* Topic: Factorizationandproperties
* Topic: Linearsystemstransforms
* questionType: Prove
</small> 
# # Resolution * * claim: * * number $N$ is the 2016 rank of a natural number, and only if, when you divide the first-time $N=p_1^{a_1}\cdot{}p_2^{a^2}\cdot\ldots\cdot{}p_k^{a_k}$, all the climbers $a_i$ share the $2016$. (I.e. either the primary number $p_i$ does not participate in the $N$ breakdown at all or participates in the $a_i = 2016m$ of the climbers.) * * division into first-time multipliers: * * We look at the degree of $p$ of one particular prime by which it falls into the distribution of $x$ and $y$ in first-time multipliers. Let's say these climbers are $a$ and $b$ accordingly: $$x=p^a\cdot\ldots,\;\;y=p^b\cdot\ldots,$$ $$xy^{433} = p^{a+433b}\ldots,\;\;x^{433}y = p^{433a+b}.$$ * * claim: * * If $a+433b$ is shared with $2016$, $433a+b$ is also shared with $2016$. * * proof: * * We mark the $a+433b=2016k$. Multiplied by $433$: $433a+433^2b=2016\cdot{}433k$. Let's just say that the difference between this and $433a+b$ also shares $2016$: it $$(433a+433^2b) - (433a+b)=(433^2-1)b = 187488b.$$'t easy to see $187488=2016\cdot{}93$ sharing $2016$.
# <lo-sample/> LV.VOL.2016.11.3
Prove that for each natural number $n$ ($n>1$), natural numbers $x$ and $y$ ($x \leq y$) can be found that $$\frac{1}{n}=\frac{1}{x(x+1)}+\frac{1}{(x+1)(x+2)}+\cdots{}+\frac{1}{y(y+1)}.$$ 
<small>
* Topic: Standardidentities
* Topic: Telescopicsums
* questionType: Prove
</small> 
# # Recommendation to convert each subexpression to a difference. 
# # Resolution * * claim: * * identity in $\frac{1}{n(n+1)} = \frac{1}{n}-\frac{1}{n+1}$ is valid. Examples include: each part of the $$\frac{1}{6}=\frac{1}{2\cdot{}3} = \frac{1}{2}-\frac{1}{3},$$ $$\frac{1}{12}=\frac{1}{3\cdot{}4} = \frac{1}{3}-\frac{1}{4},$$ $$\frac{1}{20}=\frac{1}{4\cdot{}5} = \frac{1}{4}-\frac{1}{5}.\;\cdots$$ denominated by the product of two subsequent numbers may be expressed as a difference. We use this identity to convert an expression: $$\frac{1}{n}=\frac{1}{x(x+1)}+\frac{1}{(x+1)(x+2)}+\cdots{}+\frac{1}{y(y+1)}.$$ $$\frac{1}{n}=\left( \frac{1}{x} - \frac{1}{x+1} \right) + \left( \frac{1}{x+1} - \frac{1}{x+2} \right) +$$ $$+\cdots+\left( \frac{1}{y} - \frac{1}{y+1} \right) = \frac{1}{x} - \frac{1}{y+1}$$, can any part of the $\frac{1}{n}$ be expressed as $\frac{1}{x} - \frac{1}{y+1}$? We use the equals from the previous slide. For example, if $n=5$: $$\frac{1}{5} = \frac{1}{4} - \frac{1}{20}.$$
# <lo-sample/> LV.VOL.2016.11.4
A series of natural numbers shall be $(s_i)$ by the model “2016” as follows: * the first Member of the string is $2$ $s_1$; * Second Member of the string in $s_2$ - the smallest natural number greater than the $s_1$ and the number $0$ in its notation; * third Member of the string in $s_3$ - the smallest natural number greater than the $s_2$ and the number $1$ in its notation; * the fourth Member of the string $s_4$ – the smallest natural number greater than the $s_3$ and the number $6$ in its notation. Then the digits you're looking for recur cyclically: 2-0-1-6-2-0 - $\ldots$. The first members of the string are $2; 10; 11; 16; 20; 30; 31; 36; 42; 50$. Does this string contain the number * * (R) * * 2001, * * (B) * * 2006? 
<small>
* questionType: The solution to the provedisprove
</small> 
# # is a total of four types of moves: $2 \rightarrow 0$ (a number contains $2$ and looks for the next number that contains $0$), $0 \rightarrow 1$, $1 \rightarrow 6$, and $6 \rightarrow 2$. We note that no move allows you to jump from a number $N$ to a number greater than $N+10$. The string will contain one of the numbers $1906$, $1916$, $1926$, or $1936$ after the move is made. Let's look at the following string of numbers in each case: * $1906 \xrightarrow{6 \rightarrow 2} 1912 \xrightarrow{2 \rightarrow 0} 1920 \xrightarrow{0 \rightarrow 1} 1921 \xrightarrow{1 \rightarrow 6} 1926 \xrightarrow{6 \rightarrow 2} 1927 \xrightarrow{2 \rightarrow 0} 1930 \xrightarrow{0 \rightarrow 1} 1931 \xrightarrow{1 \rightarrow 6} 1936$. * $1916 \xrightarrow{6 \rightarrow 2} 1920 \xrightarrow{2 \rightarrow 0} 1930 \xrightarrow{0 \rightarrow 1} 1931 \xrightarrow{1 \rightarrow 6}$. As you can see, in all cases, the string after the $1 \rightarrow 6$ of the move contains the number $1936$. Thus, as we proceed, we will get the $$1936 \xrightarrow{6 \rightarrow 2} 1942 \xrightarrow{2 \rightarrow 0} 1950 \xrightarrow{0 \rightarrow 1} 1951 \xrightarrow{1 \rightarrow 6} 1956  \xrightarrow{6 \rightarrow 2} 1962 \xrightarrow{2 \rightarrow 0} 1970 \xrightarrow{0 \rightarrow 1} 1971 \xrightarrow{1 \rightarrow 6} 1976,$$ $$1976 \xrightarrow{6 \rightarrow 2} 1982 \xrightarrow{2 \rightarrow 0} 1990 \xrightarrow{0 \rightarrow 1} 1991 \xrightarrow{1 \rightarrow 6} 1996 \xrightarrow{6 \rightarrow 2} 2000 \xrightarrow{2 \rightarrow 0} 2001 \xrightarrow{0 \rightarrow 1} 2010.$$. Consequently, we have shown that the number $2001$ belongs to a string and the number $2006$ does not.
# <lo-sample/> LV.VOL.2016.12.1
$x$, $y$ and $z$ are known to have natural numbers such that $x^3y^5z^6$ is the seventh degree of a natural number. Prove that $x^5y^6z^3$ is also the seventh degree of a natural number! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2016.12.3
Prove that at least one of the $18$ consecutive three-digit numbers shares their number amount! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2016.12.4
Two functions are defined as $f(a) = a^2 + 3a + 2$ and $g(b; c) = b^2 − b + 3c^2 + 3c$. Demonstrate that any natural $a$ value can be found with natural $b$ and $c$ values that $f(a) = g(b; c)$. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2017.9.1
Various natural numbers are given in the $63$, the amount of which is $2017$. Find these numbers and justify that there are no others! 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2017.9.3
In a natural five-digit number, the same numbers were replaced by the same letters and the different numbers were replaced by different letters, and the $\overline{GANGA}$ of the notation was obtained. It is known that the $\overline{GANGA}$, divided by the $7$, gives the remainder to the $A$, the $\overline{GANGA}$, divided by the $11$, gives the remainder to the $G$ and the $\overline{GANGA}$, divided by the $13$. What could the original number have been? 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2017.10.2
A primary number containing at least 4 different digits is given. Prove that its digits can be rearranged in a different order so that the newly acquired number is not a primary! 
<small>
* topic:DivisibilityRulesFor2And4
* Topic: Notationshift
* Topic: Modularithmetic
* Topic: Exhaustionmethod
* questionType: Prove
</small> 
# # Recommendation with exclusions finds 4 digits that don't provide an immediate solution. 
# # Recommendation looks at a single number consisting of the last four different digits and rearranges digits only there. 
# # Recommendation Find a small number to easily justify division after the digits are rearranged. 
# # Recommendation bags digits so that the $1,3,7,9$ (one at a time) ends up in the last $4$ positions of the decimal record of a number. # Recommendation These last $4$ digits are sacked so to get the balance you want. the resolution of 
# #, we note that any number in the $0,2,4,5,6,8$ number notation allows you to move it to the end and get a non-primary number. Therefore, the only interesting case is if four different digits are $1,3,7,9$ in the number notation, but some may also be repeated. If you allow cases where some of the numbers in the $n$ notation are more than once in the $1,3,7,9$, you designate a $n_1 = 10000x + 1379$ where the $1379$ contains four different numbers placed at the end of the number, and the $10000x$ is a number composed of all the remaining numbers, if any. We'll leave the number $10000x$ unchanged, but we'll only rearrange the numbers in $1379$. You can do this in $4! = 24$ different ways - these are all four-digit permutations. * If the original prefix is $1973$, then $10000x = 0$, $n_2 = 1397$, $n_1 = 1379$, and all other numbers in ascending order to $n_{24} = 9731$. * If the original prefix is $31379$, then $10000x = 30000$, $n_2 = 31397$, $n_1 = 31379$, and all others in ascending order to $n_{24} = 39731$. (In all of these numbers, only the last four digits change in places, while the first three stays the same). Let's say that regardless of the $10000x$ value, you can rearrange the numbers in the $1379$ so that any number $n_i$ share the $7$. You can easily see this by looking at some of the $24$ permutations in noting that you can get any residue divided by the $7$: [x% 7 for x in [1379, 1397, 1739, 1793, 1937, 1973, 3179, 3197, 3719, 3791, 3917, 3971]] [0, 4, 3, 1, 5, 6, 1, 5, 2, 4, 4, 2] * $1379 \equiv 0 \pmod 7$ * $1739 \equiv 3 \pmod 7$ * $1793 \equiv 1 \pmod 7$ * $1397 \equiv 4 \pmod 7$ * $1937 \equiv 5 \pmod 7$ * Piezīme * $1973 \equiv 6 \pmod 7$ * $3971 \equiv 2 \pmod 7$ * Note. * Let's note, that the number in the $7$ we try to divide has been chosen “naturally,” because separability with $2$ or $5$ is not possible in our case (if there are only numbers in the $1,3,7,9$) at all. Breakability with $3$ is not affected by changing digits for places (the attribute of division by $3$, or the sum of digits, does not depend on the order of the numbers). The comparability with $11$ does not change when you change digits in odd positions (or even even positions) -- so you can't expect many balances when you divide by $11$ either.
# <lo-sample/> LV.VOL.2017.11.4
Prove that you can choose $9$ numbers from any $17$ subsistence numbers so that their sum shares $9$. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2017.12.4
Let's call a natural number * beautiful * if its sum of all the subdivisions (including the $1$ and the number itself) is an odd number. Find the smallest natural number in $k$ with the property: among any arbitrarily selected $k$ beautiful numbers, you can choose two different numbers so that their product is the square of a natural number! 
<small>
* questionType: Findoptimal
</small>
# <lo-sample/> LV.VOL.2018.9.2
Three different subsistence numbers have been selected and their multiplications have been calculated in pairs, giving three multiplications. Prove that when these multiplications are divided by $4$, at least two give the same residuals! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2018.10.3
We'll call numbers $a,b,c$ a beautiful trio if they have the following characteristics: * They're three consecutive natural numbers; * each shares its own sum of digits. For example, a beautiful triple is $8$, $9$, $10$. * * (R) * * Find a beautiful triple with the smallest number greater than $10$. * * (B) * * proving endless numbers of beautiful triplets exist! 
<small>
* topic:DivisibilityRulesFor2And4
* topic:DivisibilityRulesFor3And9
* Topic: Notationinsert
* questionType: The Findexample, prove
</small> 
# # solution looks at the simpler task of $2$ a chain of “good numbers.” You can view numbers in the middle of which you can insert an unlimited number of nuts. * the first number in the $(20,21)$ is divided by the $2$ and the second number by the $3$. * the same for pairs of $(200, 201)$, $(2000, 2001)$, and so on. You can create a Headline 3 as follows: $110,111,112$ shares numbers with $2,3,4$, respectively. $$1\underbrace{0\ldots0}_n10,\;\;1\underbrace{0\ldots0}_n11,\;\;1\underbrace{0\ldots0}_n12$$
# <lo-sample/> LV.VOL.2018.11.3
We'll call the numbers $a, b, c, d, e$ * beautiful five * if they have the following characteristics: * These are five consecutive natural numbers; * Each of them shares their number amount. A beautiful five, for example, is $6, 7, 8, 9, 10$. * * (R) * * Find a beautiful five with the smallest number greater than $10$. * * (B) * * prove endless numbers of beautiful five exist! 
<small>
* questionType: Findexample, prove
</small>
# <lo-sample/> LV.VOL.2018.12.3
Resolve equation $x^6 + 3x^3 + 1 = y^4$ in integers. 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2019.9.3
Can the numeric sum of a natural number square be * * (R) * * $19$, * * (B) * * $2019$? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2019.10.1
Demonstrate that all subsistence numbers greater than $100$ can be expressed as the sum of the source and composite numbers! 
<small>
* strategy: Trialanderror
* Topic: Modularparity
* questionType: Prove
</small> 
# # resolve attempts to express $101$ in various ways, for example: $$101 \;=\; 2+99 \;=\; 3+98 \;=\; 4+97 \;=\;$$ $$\;=\; 5+96 \;=\; 7+94 \;=\; \cdots$$ numbers greater than $100$ ($101,102,103,\ldots$) are infinite; you can also express in a lot of ways. The procedure shall be implemented by sorting cases: * If the $n$ is paired, then the $n-2$ is definitely not a primary number. * If the $n$ is odd, then the $n-3$ is definitely not a primary number.
# <lo-sample/> LV.VOL.2019.10.3
Prove that the expression $$13^n + 7^n + 2019$$ value is not a natural number square for any natural $n$ value! 
<small>
* Topic: Periodicremainders
* Topic: Divisibilityrulesother
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2019.11.3
Prove that the expression $13^n + 10^n + 7^n + 3^n$ value is not a natural number square for any native n value! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2019.12.3
Prove that the expression $$4^n+5^n+6^n+7^n+8^n+9^n+10^n+11^n+12^n+13^n$$ value is not a natural number square for any natural $n$ value! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2019.12.5

Find
* * (A) * * one pair of natural numbers in the $(a;b)$,
* * (B) * * $ trīs tādus naturālu skaitļu pārus $ (a; (b) $, $ a < b $,  
ka lielākais skaitlis, ko nevar izteikt formā $ an + bm $, 
kur $ m $ un $ n $ ir nenegatīvi veseli skaitļi, ir $ 2019 $.


<small>
* questionType: FindExample, FindExample
</small>




# <lo-sample/> LV.VOL.2020.10.4
Here's a look at a series of numbers in the $7; 737; 73737; 7373737; \ldots$, the first Member of which is $7$ and gets each next one by recording the $37$ at the end of the previous one. Prove that no Member of this string shares $17$. 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2020.11.4
The three-digit number $\overline{abc}$ is known to be the primary number and that the equation $ax^2 + bx + c = 0$ has two real roots. Can these roots happen to be * * (R) * * whole numbers, * * (B) * * rational numbers? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2021.10.4
An equation $2019x^2 + 2020x + 2021 = 0$ is written on the board at the beginning. Two players in a row make moves, the first player starts. In one move, you can select any of the three coefficients on the left side of the equation (at the $x^2$, at the $x$, or at the free limb) and subtract a single from it. That player loses, after whose move the equation written on the board has some whole root. Which player - first or second - will win by playing correctly? 
<small>
* questionType: Algorithm
</small>
# <lo-sample/> LV.VOL.2021.11.3
Let's call a natural number * elegant * if there are no zeros in its decimal note and that number shares its number. (Easy are all single digits, and for example, numbers in $36$ and $322$.) Prove there are endless numbers of elegant! 
<small>
* questionType: prove
</small>
# <lo-sample/> LV.VOL.2022.10.3
Prove that you can find a natural number for each natural $K>1$ that shares $13$ and has a $K$ sum of digits. 
<small>
* questionType: Prove
</small>
# <lo-sample/> LV.VOL.2022.11.3
At the beginning, a number $16$ is written on a piece of paper. If a number $x$ is written * on the page, the number $x^2$ may also be written on it; * the numbers $x$ and $y$ are written, and the number $|x-y|+1$ is also allowed. Can I get the number $2022$ written on the page (no number you typed is cleared)? 
<small>
* questionType: ProveDisprove
</small>
# <lo-sample/> LV.VOL.2023.10.3
All the subsistence numbers from $1$ to $2023$ are written in a row in some order. In one step, each two adjacent numbers is multiplied and the sum of the digits of that multiplication is written below them. this results in a new row that contains one number less than the original row. After the first move, you get a new row that contains $2022$ numbers, after the second move you get a new row that contains a $2021$ number, and so on, until after the 2022 move you get the last new row that contains only one number. Find all possible values for this last number! 
<small>
* questionType: FindAll
</small>
# <lo-sample/> LV.VOL.2023.11.4
Prove that there are infinitely many subsistence numbers in the quadrangular $(a_1; b_1; a_2; b_2)$ that $a_1 \neq a_2$, $b_1 \neq b_2$, and $$2^{a_1} - \left( b_1 \right)^2 = 2^{a_2} - \left( b_2 \right)^2 > 0.$$ 
<small>
* questionType: Prove
</small> 
# # solution TBD
