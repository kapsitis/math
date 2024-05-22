# <lo-sample/> LV.VOL.2024.9.1
Whether there are $5$ different natural numbers with the characteristic that their arithmetic mean is: * * (A) * * directly $3$ times the size; * * (B) * * * exactly $2$ times the largest common divider of all these numbers? 
<small>
* questionType: Provedisprove
* domain: ALG
</small> 
# # solution
 * * (R) * * Yes, such numbers are $1; 2; 3; 4; 5$. Their arithmetic mean is $(1 + 2 + 3 + 4 + 5) ∶ 5 = 15 ∶ 5 = 3$ and the largest common divider is $1$. * * (B) * * No, does not exist. Suppose such numbers exist and their biggest common divider is $d$. In that case, the numbers are $a_1d; a_2d; a_3d; a_4d; a_5d$, where the natural numbers are $a_1,a_2,\ldots,a_5$ obtained by dividing the initial five numbers by the $d$. Uniformity must be met: the all $a_i$ $$\frac{a_1d + a_2d + a_3d + a_4d + a_5d}{5} = 2d\;\;\text{jeb}\;\;a_1 + a_2 + a_3 + a_4 + a_5 = 10.$$ is different. but since even the sum of the five smallest different subsistence numbers is $1 + 2 + 3 + 4 + 5 = 15 > 10$, such numbers do not exist.
# <lo-sample/> LV.VOL.2024.9.2
In the rectangle, a $ABCD$ dot $E$ on the edge $BC$. The cut-off $AE$ crosses the rectangle diagonally at the $BD$ point in the $O$. A straight line drawn through a point $O$ parallel to the $BC$ crosses the edge $AB$ and $CD$ at points $F$ and $G$ respectively. The $BOF$ area of the triangle is known to be $4$, but the $AOD$ area of the triangle is $63$. Calculate square $OECG$ area! 
<small>
* questionType: Findall
* domain: Geom
</small> 
# # solution
 represents the length of the square edges with $AC = a$ and $BC = b$ (see Figure 1).! [] (LV.VOL.2024.9.2A.png) computes the trapeze $CEGB$ and triangle $AGB$ area: * $S_{CEGB} = \frac{EC + BG}{2} \cdot BC = \frac{(a+b)b}{2}$; * $S_{AGB} = \frac{AB \cdot BG}{2} = \frac{(a+b)b}{2}$. So the $S_{CEGB} = S_{AGB}$ and, minus the same size (trapeze $CHGB$ area) from both sides, the uniformity will remain: $$S_{CEGB} - S_{CHGB} = S_{AGB} - S_{CHGB}\;\;\text{un}\;\;S_{HEG} = S_{ACH}.$$
# <lo-sample/> LV.VOL.2024.9.3
The computer class includes $n$ ($n \geq 3$) computers, some of which are connected to each other. Every now and then, a computer that hasn't sent anything before sends a message to all the computers it's connected to. Prove that at any time you can find two computers that have received the same number of messages! 
<small>
* questionType: Prove
* domain: Comb
</small> 
# # solution
 Suppose the opposite is that at some point each computer has received different numbers of messages. This means that the number of messages received by computers is $0; 1; 2; \ldots ; n-1$ (in some order). Below, we label computers with $D_0; D_1; \ldots, D_{n-1}$, as appropriate, according to the number of messages you receive, that is, the computer has received directly $i$ messages in the $D_i$. Because the $D_{n-1}$ has received a $n-1$ message, it is connected to all other computers, and all other computers have sent messages to it. $D_{n-1}$ himself hasn't sent a message because $D_0$ hasn't received anything. The $D_{n-2}$ must also be connected to all other computers because otherwise there would be no $n-2$ connected to the $D_{n-2}$ and sent a message (because we already know that the $D_{n-1}$ has not yet sent a message). The computer, on the other hand, has not received $D_0$ messages, but because it is connected to the $D_{n-2}$ (and the $D_{n-2}$ has sent a message), the $D_0$ should have received a message from the $D_{n-2}$. A contradiction has been obtained. So at any time, you can find two computers that have received the same number of messages.
# <lo-sample/> LV.VOL.2024.9.4
The $\overline{abc} \cdot \overline{def} \cdot \overline{ghi} \cdot \overline{jkl}$ expression is written on the board, which is the product of four three-digit numbers. In each move, Gustav selects a nonzero digit and Maruta records it in place of a letter (Gustav sees in which). Prove that Maruta can always get the value of the expression obtained after $12$ moves to be shared with the $9$. 
<small>
* questionType: Algorithm
* domain: NT
</small> 
# # solution
 Maruta can do the following: * digits that, divided by $3$, give the remainder of the $1$ (digits $1; 4; 7$), write in the first digit; * digits that, divided by $3$, give the remainder of 2 (digits 2; 5; 8), write in the second digit; * Write numbers that are divided by $3$ (numbers $3; 6; 9$) into the third number. When all numbers are filled in, Maruta can continue typing this category of digits into the fourth number. In this way, she can get all three digits to give the same balance divided by 3 in at least two numbers, so their amount is divided by $3$. Consequently, at least two of those four three-digit numbers will share the $3$, so the product of all the numbers will share the $9$.
# <lo-sample/> LV.VOL.2024.9.5
Kim wants subsistence numbers from $1$ to $2024$ to be written around the circle in such a way that each number is written exactly once, and for every three numbers written in succession, the $a,b,c$ characteristic is that the number $a + c$ shares the $b+1$. Can Kim do this? 
<small>
* questionType: ProveDisprove
* domain: NT
</small> 
# # solution
 No, Kim can't write numbers in the plaintiff way. First of all, let's state that if you could write the numbers, then the odd and even numbers in the circle would have been typed in an alternate way. If it wasn't, two odd numbers would have been written somewhere next door. As we walk further down the circle to the nearest couple number, we'll find a place where the numbers are written in order $n,n,p$ ($n$ is odd and $p$ is even). We've gotten a contradiction because $n+p$ is an odd number and can't share $n+1$, which is an even number. We look at the number $2024$, with odd numbers written on both sides. Their amount is the even number that shares the $2025$. The smallest such odd number is $4050$, but the largest number you can get by adding up some two given odd numbers is $4044 = 2023 + 2021$, which is less than $4050$. We've gotten that you can't find numbers for $2024$ to write next to. Therefore, the figures along the circle cannot be written in the required way.
# <lo-sample/> LV.VOL.2024.10.1
Is it possible to select * * (A) * * $50$; * * (B) * * * $51$ different natural numbers that do not exceed the $100$ so that for any two selected numbers their difference (minus the smallest number) is not equal to their largest common divider? 
<small>
* questionType: Provedisprove
* domain: NT
</small> 
# # solution
 * * (a) * * Yes, can. If you select $50$ odd numbers, all their differences are even numbers, but the largest common divider of odd numbers is an odd number. * * (b) * * No, cannot. If a $51$ number had been chosen, then two adjacent numbers $x$ and $x+1$ would surely have been chosen, but the difference between those numbers is $(x+1)-x=1$ and $\operatorname{LKD}(x+1,x)=1$.
# <lo-sample/> LV.VOL.2024.10.2
A curved square is given for the $ABCD$ you want to $AB=BC=CD$. The diagonals of the rectangle intersect at a point in the $E$, while the $BAD$ of angles and $ADC$ bisectrises intersect at a point in the $F$. Prove $\sphericalangle EAF = \sphericalangle EDF$. 
<small>
* questionType: Prove
* domain: Geom
</small> 
# # solution
 Since $AB=BC=CD$, the triangles $BCD$ and $ABC$ are isosceles and have the same basic angles: $\sphericalangle BAC = \sphericalangle BCA = \alpha$ and $\sphericalangle CBD = \sphericalangle CDB = \beta$. We mark $\sphericalangle EAF = x$ and $\sphericalangle EDF = y$ (see Figure 2).! [] (LV.VOL.2024.10.2A.png) After the given $AF$ and $DF$, there are angles bisectrises, so we get: * $\sphericalangle EAD = \sphericalangle EAF + \sphericalangle FAD = x + (\alpha + x) = \alpha + 2x$. * $\sphericalangle EDA = \sphericalangle FDA - \sphericalangle FDE = (\beta - y) -y = \beta - 2y$. Because the cross angles are the same, then $\sphericalangle AED = \sphericalangle BEC = 180^{\circ} - \sphericalangle BCE - \sphericalangle EBC = 180^{\circ} - \alpha - \beta$. When you look at the sum of the inner angles of the triangle $AED$, we get: $$\begin{aligned}
180^{\circ} & = 180^{\circ} - \alpha - \beta + (\alpha + 2x) + (\beta - 2y); \\
180^{\circ} & = 180^{\circ} + 2x - 2y. \\
\end{aligned}$$ Consequently, we have obtained that the solution for the $2x = 2y$ or $x=y$ that was also required to be proved. * Note: * for other point $E$ and $F$ layouts, is analogous. 
# # solution
 because by the given $AB = BC = CD$ (see Figure 3): * $\sphericalangle BAC = \sphericalangle ACB = \alpha$ because the triangle in the $BAC$ is equilateral; * $\sphericalangle CBD = \sphericalangle CDB = \beta$ because the triangle $BCD$ is isosided. So the $\sphericalangle AED = \sphericalangle BEC = 180^{\circ} - \alpha - \beta$ (sum of the inner angles of the triangle $ABCD$) from which we get that $\sphericalangle EAD + \sphericalangle EDA = 180^{\circ} - \sphericalangle AED = \alpha + \beta$.! [] (LV.VOL.2024.10.2B.png) from the sum of the $ABC$ and triangles of the rectangle, and the $BCD$ inner angles, we get that $\sphericalangle BAD + \sphericalangle CDA = 360^{\circ} - \sphericalangle ABC - \sphericalangle BCD = 
360^{\circ} - (180^{\circ} - 2\alpha) - (180^{\circ} - 2\beta) = 2(\alpha + \beta)$. Using the definition of a bisectre, we get that we $\sphericalangle FAD + \sphericalangle FDA = \frac{1}{2}\sphericalangle BAD + \frac{1}{2} \sphericalangle CDA = 
\frac{1}{2}( \sphericalangle BAD + \sphericalangle CDA) = \alpha + \beta.$'t get that we $\sphericalangle EAD + \sphericalangle EDA = \sphericalangle FAD + \sphericalangle FDA$, then we $\sphericalangle EAF = \sphericalangle EAD - \sphericalangle FAD = \sphericalangle FDA - \sphericalangle EDA = \sphericalangle EDF$. * Note: * at the end of the task, you can also use that around the square, the $AEFD$ can circle the circle, then $\sphericalangle EAF = \sphericalangle EDF$ like retracted angles based on the same arc in the $EF$.
# <lo-sample/> LV.VOL.2024.10.3
Resolve equation system $$\left\{ \begin{array}{l}
x + \frac{1}{x} = 2y^2 \\
y + \frac{1}{y} = 2z^2 \\
z + \frac{1}{z} = 2x^2 \\
\end{array} \right.$$ 
<small>
* questionType in real numbers: Findall
* domain: The ALG
</small> # resolution equates the denominators of the equation's left-hand expressions to $$\left\{ \begin{array}{l}
\frac{x^2 + 1}{x} = 2y^2 \\
\frac{y^2 + 1}{y} = 2z^2 \\
\frac{z^2 + 1}{z} = 2x^2 \\
\end{array} \right.$$ because the right-hand expression of the first equation $2y^2 \geq 0$ and the left-hand counter $x^2 + 1 > 0$, so does the part denominator $x > 0$. Similarly, we get from the other equations that we $y>0$ and $z>0$. We note that a positive $x$ has a $x + \frac{1}{x} \geq 2$ in effect because it can be converted equivalently to $x - 2 + \frac{1}{x} \geq 0$, or $$\left( \sqrt{x} - \frac{1}{\sqrt{x}} \right)^2 \geq 0.$$ the last inequality will work because there is a square of a real number. That's why $2y^2 = x + \frac{1}{x} \geq 2$, or $y \geq 1$, too (and similarly $x \geq 1$ and $z \geq 1$). By summing up all the equations given, we get the $$\frac{x^2 + 1}{x} + \frac{y^2 + 1}{y} + \frac{z^2 + 1}{z} = 
2x^2 + 2y^2 + 2z^2;$$ $$\frac{2x^3 - x^2 - 1}{x} + \frac{2y^3 - y^2 - 1}{y} + \frac{2z^3 - z^2 - 1}{z} = 0.$$ because we $2x^3 - x^2 - 1 = x^3 - x^2 + x^3 - 1 = x^2(x-1) + (x-1)(x^2 + x + 1) = 
(x-1)(2x^2 + x + 1)$, we get the $$\frac{(x-1)(2x^2 + x + 1)}{x} + \frac{(y-1)(2y^2 + y + 1)}{y} + 
\frac{(z-1)(2z^2 + z + 1)}{z} = 0.$$ because we $x,y,z \geq 1$, and because the $2x^2 + x + 1 > 0$, $2y^2 + y + 1 > 0$, and $2z^2 + z + 1 > 0$ (because the branches of the $D < 0$ and corresponding quadratic function are facing up), we get that the only solution to the equation and given system is $x = y = z = 1$. * Note: * Alternatively, after you get the $x,y,z \geq 1$, you can complete this solution as follows: For symmetry, let's say the largest of the numbers is $x$ ($x \geq y$ and $x \geq z$). Here's a look at the $2x^2 = z + \frac{1}{z}$ of equations. We notice that if $x > 1$, then $x^2 > x \geq z$ and $x^2 > 1 \geq \frac{1}{z}$, so $2x^2 = x^2 + x^2 > z + \frac{1}{z}$. A contradiction has been obtained. So $x = 1$, and because it's the largest of the numbers, so are $y = 1$ and $z=1$. # # solve like in solution 1, we get you $x,y,z \geq 1$. Without losing generality, we can assume that $x$ is the greatest or one of the greatest values, that is, $x \geq z$ and $x \geq y$. Let's prove that in that case, $$x + \frac{1}{x} \geq z + \frac{1}{z}.$$ Weike equivalent modifications: in $$\begin{aligned} \frac{x^2 + 1}{x} & \geq \frac{z^2 + 1}{z}; \\
zx^2 + z & \geq xz^2 + x; \\
(zx - 1)(x-z) \geq 0. \\
\end{aligned}$$, because of $x,z \geq 1$ and $x \geq z$, there is a real inequality and the first inequality is true because equivalent modifications were made. When we use inequality, we get the $$\begin{aligned}
x + \frac{1}{x} & \geq z + \frac{1}{z} = 2x^2; \\
0 & \geq \frac{2x^3 - x^2 - 1}{x}; \\
0 & \geq \frac{(x-1)(2x^2 + x + 1)}{x}. \\
\end{aligned}$$ as $2x^2 + x + 1 > 0$, then inequality is true only if you $x = 1$. In that case, $y = z = 1$, because $x \geq z$ and $x \geq y$. So the solution to the given equation is $x = y = z = 1$.
# <lo-sample/> LV.VOL.2024.10.4
The school's 10 th grade Olympiad was attended by students in grades 10a and 10b. When the results were first summed up, it was found that the average score for Class 10a pupils was $37$ points, while the average score for Class 10b pupils was $11$ points. A review of the works revealed that one pupil's work had been put to the wrong grade. By recalculating the average result, it turned out to have increased by exactly a $1$ point in both classes (and now there are $38$ and $12$ points respectively). How many students participated in this Olympiad together? 
<small>
* questionType: FindCount
* domain: ALG
</small> 
# # solution
 $26$ students participated in the Olympiad altogether. First of all, let us argue that the mixed work was first added to the result of Class 10a and then transferred to Class 10b. Let's face it the opposite, the mixed work had been put to class 10b from the start but ended up being put to class 10a. As the class 10b average score increased when this job was removed, the score for this job should be less than the class average score, that is, the score is less than the $11$. Similarly, because when applied to class 10a jobs, their average score increased, the work score should be greater than the class 10a average score, that is, more than $37$ points. A contradiction has been obtained. So the mixed work ended up being transferred to class 10b jobs. Let us refer by $n$ and $m$ to the number of pupils in Classes 10a and 10b who participated in the Olympiad and whose works were not mixed, respectively. Then there's one pupil who was added to class 10b at first, but it has to be in class 10a, let's mark its score with $z$. So the total number of students participating in the Olympics is $n+m+1$. We mark the sum of points without the mixed work in class 10a with the $X$. Since the average score with the mixed work was $37$ and without it $38$, we get two equations: in the $$\frac{X+z}{n+1} = 37\;\;\text{un}\;\;\frac{X}{n} = 38;$$ $$X + z = 37n + 37\;\;\text{un}\;\;X=38n.$$, when you put the second equation in the first, you get that you $z = 37 - n$. Similarly, by marking the sum of points without mixed work in class 10b with $Y$, we get two equations: in the $$\frac{Y}{m} = 11\;\;\text{un}\;\;\frac{Y+z}{m+1} = 12;$$ $$Y = 11m\;\;\text{un}\;\;Y+z=12m+12.$$, when you put the first equation in the second, you get that you $z = m+12$. From both, we get that $37 − n = m + 12$, or $m+n = 25$. So the total number of pupils is $m+n+1 = 26$. * Note. * Let's give an example that this situation is possible. Suppose $n=2$ and $m=23$, the two “unmixed” class 10a pupils have $38$ points, all “unmixed” class 10b pupils have $11$ points. Mixed work has $35$ points.
# <lo-sample/> LV.VOL.2024.10.5
In the size table, the $9 \times 9$ boxes are shaded some of the boxes, and the others are unshaded. The following moves shall be used for colouring the boxes: if at least three boxes are colored in any row, column, or one of the two main diagonals, you can color all the remaining rows, columns, or diagonal boxes in a single step. What is the lowest possible number of boxes that are colored at the beginning, at which you may be able to color all the boxes in the table with the steps described? 
<small>
* questionType: Findoptimal
* domain: Comb
</small> 
# # solution
 the smallest number of boxes that were initially colored is $6$, for example, see fig. 4 Let's show you how to color the entire table with the allowed moves. We first color both diagonals (see Fig. 5) because each has $3$ stained boxes. After this color, we can color the first row (see Figure 6) because it has $3$ boxes. We then color columns 2, 3, 4 (see Fig. 7), then finally color all remaining rows that have not yet been colored.! [] (LV.VOL.2024.10.5A.png) We'll show that fewer boxes that were initially colored are not enough. For a row, column, or diagonal to be colored, you must have at least three boxes already colored on it. You need at least three coloured boxes again before you can make your second move, no more than one of which can be the one that was used in the first move (If there were at least two, it would be the same row, column, or diagonal). Let's say there was this box. Then, after two moves, five coloured boxes have been used and the colouring options are: two diagonals (a common central box, see figure 8, where light grey shaded the boxes where 4 shaded boxes may be located), diagonal and row (see Figure 9), diagonal and column (see Figure 10), row and column (see Figure 11). It is not possible to make another move in any of these combinations (there are no more than two coloured boxes in any blank row, column, or diagonal), so at least one more pre-coloured box is required.! [] (LV.VOL.2024.10.5B.png)
# <lo-sample/> LV.VOL.2024.11.1
Find all pairs of real numbers in $(a;b)$ that have inequality in effect: $$4a + 4b^2 + \sqrt{4a - 4b^2 - 1} \leq 1.$$ 
<small>
* questionType: Findall
* domain: ALG
</small> 
# # solution
 the Croot expression $4a - 4b^2 -1$ must be non-negative, so $4a - 4b^2 - 1 \geq 0$ or $$4a \geq 4b^2 + 1.$$ because the square root values are non-negative, we get from the given inequality that when you add up the two resulting inequalities in a $4a + 4b^2 \geq 1$ or $$a \geq 4a + 4b^2.$$, you get that you $0 \geq 8b^2$. So the only valid value is $b=0$. When we insert inequalities: $$4a \geq 1\;\;\text{un}\;\; 1 \geq 4a.$$ So $a = \frac{1}{4}$. We've gotten that the only valid pair of numbers is the ${\displaystyle \left( \frac{1}{4}; 0 \right)}$ 
# # solution
 If $a = \frac{1}{4}$ and $b = 0$, then the inequality is valid. the $4 \cdot \frac{1}{4} + 4 \cdot 0 + \sqrt{4 \cdot \frac{1}{4} - 4 \cdot 0 - 1} = 1 \geq 1$ we'll justify that the only solution to the inequality is $a = \frac{1}{4}$ and $b = 0$. Let's look at three cases. * If $a < \frac{1}{4}$, the $4a < 1$ and subroot expressions $4a - 4b^2 - 1 = 4a - 1 -4b^2$ negative because they $4a - 1 < 0$ and $-4b^2 < 0$. In this case, the expression is not defined and there is no resolution. * If $a > \frac{1}{4}$, then $4a > 1$. Because $4b^2 + \sqrt{4a - 4b^2 - 1} \geq 0$, $4a + 4b^2 + \sqrt{4a - 4b^2 - 1} > 1$, so there is no solution to the inequality. * If $a = \frac{1}{4}$, you can overwrite the inequality as follows: $1 + 4b^2 + \sqrt{-4b^2} \leq 1$ or $4b^2 + \sqrt{-4b^2} \leq 0$. For a subroot expression to be defined, the only valid value is $b = 0$.
# <lo-sample/> LV.VOL.2024.11.2
In the rectangle, a $ABCD$ dot $E$ on the edge $BC$. The cut-off $AE$ crosses the rectangle diagonally at the $BD$ point in the $O$. A straight line drawn through a point $O$ parallel to the $BC$ crosses the edge $AB$ and $CD$ at points $F$ and $G$ respectively. The $BOF$ area of the triangle is known to be $4$, but the $AOD$ area of the triangle is $63$. Calculate square $OECG$ area! 
<small>
* questionType: Findall
* domain: Geom
</small> 
# # solution
 represents the lengths of the cut-off in $OF = x_1$, $OG = x_2$, $BF = CG = y_1$, $AF = DG = y_2$ (see Figure 12).! [] (LV.VOL.2024.11.2A.png) because of the $\sphericalangle BFO = \sphericalangle DGO = 90^{\circ}$ and $\sphericalangle BOF = \sphericalangle DOG$, the $\triangle OFB \sim \triangle OGD$ for the sign $\ell\ell$. So the $\frac{x_1}{x_2} = \frac{y_1}{y_2} = k$ and ${\displaystyle \frac{S_{OFB}}{S_{OGD}} = k^2}$ we get from that we $S_{OGD} = \frac{4}{k^2}$'t. We look at the ratio of triangle areas: in the $$\frac{S_{OFB}}{S_{OFA}} = \frac{\frac{1}{2}OF \cdot BF}{\frac{1}{2}OF \cdot AF} 
= \frac{BF}{AF} = \frac{y_1}{y_2} = k\;\;\Rightarrow{}S_{OFA}=\frac{4}{k}.$$, we look at the triangle in the $AOD$ (see figure where the $OM$ is the $AOD$ height of the triangle): by $$S_{ODA} = S_{OMA} + S_{OMD} = S_{OFA} + S_{OGD} = \frac{4}{k} + \frac{4}{k^2} = 63.$$ removing the $63k^2 - 4k - 4 = 0$ of square equations obtained, we get: in $$ k = \frac{4 \pm \sqrt{16 + 4 \cdot 4 \cdot 63}}{126} = \frac{4 \pm 32}{126};$$ $$k_1 = \frac{36}{126} = \frac{2}{7}\;\;\text{un}\;\;k_2 = -\frac{28}{126}\;\text{(neder)}.$$, we have therefore gained $S_{OFA} = \frac{4}{k} = 4 : \frac{2}{7} = 14$ and $S_{OGD} = \frac{4}{k^2} = 4 : \left( \frac{2}{7} \right)^2 = 49$. Whereas the $\triangle BOE \sim \triangle DOA$ is $\ell\ell$ by the $\frac{S_{BOE}}{S_{DOA}} = \left( \frac{OB}{OD} \right)^2 = k^2$ and $$S_{BOE} = S_{DOA} \cdot k^2 = 63 \cdot \frac{4}{49} = \frac{36}{7}.$$ use of the characteristics of the area gives * $S_{ABD} = S_{BOF} + S_{OFA} + S_{DOA} = 4 + 14 + 63 = 81$; * $S_{ABD} = S_{BCD} = \frac{1}{2}S_{ABCD}$ * $S_{OECG} = S_{BCD} - S_{BOE} - S_{OGD} = 81 - \frac{36}{7} - 49 = 32 - \frac{36}{7} = \frac{188}{7} = 26\frac{6}{7}$.
# <lo-sample/> LV.VOL.2024.11.3
The computer class includes $n$ ($n \geq 3$) computers, some of which are connected to each other. Every now and then, a computer that hasn't sent anything before sends a message to all the computers it's connected to. Prove that at any time you can find two computers that have received the same number of messages! 
<small>
* seeAlso:LV.VOL.2024.9.3
* questionType: Prove
* domain: Comb
</small> 
# # solution
 Suppose the opposite is that at some point each computer has received different numbers of messages. This means that the number of messages received by computers is $0; 1; 2; \ldots ; n-1$ (in some order). Below, we label computers with $D_0; D_1; \ldots; D_{n-1}$, as appropriate, according to the number of messages you receive, that is, the computer has received directly $i$ messages in the $D_i$. Because the $D_{n-1}$ has received a $n-1$ message, it is connected to all other computers, and all other computers have sent messages to it. Your computer hasn't received $D_0$ messages, so because it's connected to a $D_{n-1}$, $D_{n-1}$ hasn't sent them yet. No other computer (except $D_{n-1}$) is connected to the computer $D_0$ (otherwise it would have received a message from it). Finally, we look at computer $D_{n-2}$. Because your computer hasn't sent $D_{n-1}$ messages yet, this computer is connected to (and received from) all other $n-2$ computers. So it's also connected to a computer $D_0$. But it's a contradiction because the $D_0$ is only connected to the $D_{n-1}$.
# <lo-sample/> LV.VOL.2024.11.4
For what natural $n$ values can you find $2n+1$ natural numbers (not necessarily different) with the characteristic that if you choose any $n+1$ of them, their amount will be divided by the sum of the remaining $n$ numbers? 
<small>
* questionType: Findall
* domain: Resolution
</small> of NT # # If $n=1$, the terms of the task are $(1; 1; 1)$ fulfilled for the numbers (the sum of any two selected numbers is divided by the remaining number). If $n=2$, the terms of the task are $(2; 1; 1; 1; 1)$ fulfilled for the numbers. Let's say there are no $2n+1$ numbers at the $n \geq 3$ that fulfill the terms of the task. Let's say the opposite, that is, for a given $n$ that is at least $3$, you can find $2n+1$ natural numbers so that the sum of any numbers you choose in the $n+1$ shares the sum of the remaining $n$ numbers. We'll sort the numbers that you give in a nondescending order and sign them with $a_1 \leq a_2 \leq \cdots a_{2n+1}$, and we'll indicate the $S_A = a_2 + \ldots + a_{n+1}$ and $S_B = a_{n+2} + \cdots + a_{2n+1}$ of the amount. It follows from the assumption that $S_A + a_1$ shares $S_B$ and $S_B + a_1$ shares $S_A$. That means $S_A + a_1 \geq S_B$. Because the 𝑆 𝐵 contains the 𝑛 largest numbers, then $S_B \geq S_A$. In addition, $a_1$ is a natural number, thus $S_B + a_1 > S_A$, and $S_B + a_1$ shares $S_A$, so we get that by adding up the two inequalities in the $$\left\{ \begin{array}{l}
S_B + a_1 \geq 2S_A; \\
S_A + a_1 \geq S_B. \\
\end{array} \right.$$, we get that $S_A + S_B +2a_1 \geq 2S_A + S_B$ or $2a_1 \geq S_A$. Because of the $n \geq 3$, the $S_A$ contains at least $3$ counts that are not smaller than $a_1$ or $S_A \geq 3a_1$. As a result, we get that $2a_1 \geq S_A \geq 3a_1$. There is a contradiction that $a_1$ is a natural number. So the assumption that the required numbers exist at the $n \geq 3$ is false.
# <lo-sample/> LV.VOL.2024.11.5
Given the natural number $n$, let's $M$ the first set of $2n$ natural numbers in the $M = \{1; 2; 3; \ldots ; 2n\}$. Two players $A$ and $B$ play the game. In each move, first the player $A$ selects the number $a$ from the set $M$, then the player $B$ selects the number $b$ from the set $M$, plus the numbers $a$ and $b$ are not the same and do not match any of the previously selected numbers. At the end of the trek, you create a square function called $y = x^2 - ax + b$ and write on the page. After the $n$ moves, all numbers from the $M$ of the set and the square function of the $n$ are selected. Here's a look at all possible pairs of these quad features: For each pair, the $y$ coordinates of all intersections of their schedules are calculated, all the $y$ coordinates thus obtained are counted. Prove that the player can $B$ get the resulting amount directly $n^3 - n$. 
<small>
* questionType: Prove
* domain: ALG
</small> # # resolve If a player $A$ chooses a number $i$, then the player $B$ have to choose a number $2n + 1 - i$. Here's a look at the intersections of the two functions you get if the player selects numbers $i$ and $j$ $A$: $$\begin{aligned}
x^2 - ix + (2n+1-i) = x^2 - jx + (2n+1 -j);\\
-(i-j) = x(i-j);\\
x=-1.\\
\end{aligned}$$ in this case, the value of the function is $y = (−1)^2 + i + 2n + 1 − i = 2(n + 1)$. As there are $\frac{n(n-1)}{2}$ pairs of different square functions in total, the sum of the $y$ coordinates is $$2(n+1) \cdot \frac{n(n-1)}{2} = n(n^2 - 1) = n^3 - n.$$
# <lo-sample/> LV.VOL.2024.12.1
Resolve equation system $$\left\{ \begin{array}{l}
x + \frac{1}{x} = y+z\\
y + \frac{1}{y} = x+z\\
z + \frac{1}{z} = x+y\\
\end{array} \right.$$ 
<small>
* questionType in real numbers: Findall
* domain: ALG
</small> # # resolve subtracting the second from the first equation, we get: in the $$x - y + \frac{1}{x} - \frac{1}{y} = y - x;$$ $$2(x - y) = \frac{1}{y} - \frac{1}{x}\;\;\Rightarrow{}2(x-y) = \frac{x-y}{xy}.$$, we look at when you $x=y$. It is then apparent from the first equation of the system that $\frac{1}{x} = z$. We get from the third equation of the system that in $$\frac{1}{x} = x+x\;\;\Rightarrow\;\;x^2=1\;\;\Rightarrow\;\;x=\pm 1.$$ we have therefore obtained solutions for $(1; 1; 1)$ and $(−1; −1; −1)$. If $x \neq y$, then $xy = \frac{1}{2}$. Analogous, the sum of equations 2 and 3 of the system and the sum of equations 1 and 3 of the system results in a $yz = xz = xy = \frac{1}{2}$. However, if the $yz = xz, xz = xy, yz=xy$ and none of the $x,y,z$ are zero (by definition set), then $y=x$, $z=y$, $z=x$, so $x=y=z$ what the case is already under consideration.
# <lo-sample/> LV.VOL.2024.12.2
On the $ABC$ edges of the various edges of the triangle, the $AB$ and $AC$ have chosen the points $D$ and $E$ respectively that they $BD = CE$. The $ABE$ and $ACD$ circles of the triangles intersect at $T$. Prove the $AT$ is an angle $BAC$ bisectre! 
<small>
* questionType: Prove
* domain: Geom
</small> # # resolve using the retracted quadrangular property and adjacent angles property, we get: * $\sphericalangle ABT = 180^{\circ} - \sphericalangle AET = \sphericalangle CET$ (from quadrangular $ABTE$); * $\sphericalangle ACT = 180^{\circ} − \sphericalangle ADT = \sphericalangle BDT$ (from quadrangular $ADTC$). Given that the $BD=EC$ is as given, we find that the $\triangle BTD = \triangle ETC$ is $\ell{}m\ell$ by the sign (see Figure 13). Because the corresponding heights of the same triangles are the same, that is to say, for $h_{BD} = h_{EC}$, the point in the $T$ is equal distances from the $BAC$ edges of the angle, so that the point in the $T$ is on the bisectre or $AT$ of that angle is the $BAC$ bisectre of the angle.! [] (LV.VOL.2024.12.2A.png)
# <lo-sample/> LV.VOL.2024.12.3
There are $200$ candy in the bowl on the table. “Brother and Carlson take turns making moves,” the brother begins. You can take either one or two candy from the bowl in one go and eat it. The player who eats the last candy wins. Who will win the right game when it's additionally known that each can eat no more than * * (R) * * $140$; * * (B) * * $110$ candy? (In case a player can no longer make a move, he loses). 
<small>
* questionType: Algorithm, Algorithm
* domain: Comb
</small> # # solve * * * (R) * a brother can always win. In this case, the $140$ is a big enough number and doesn't affect the course of the game, you can play like there's no such restriction. In that case, the first player's strategy is classic: you need to leave your opponent the number of sweets that share $3$. This means that on his first move, his brother has to eat $2$ candy, then on each subsequent move, if Carlson eats one candy, then his brother has to eat two, but if Carlson eats two, then his brother has to eat one. This will leave 198 candy ($198$ share $3$) in the bowl after their first sibling's move, and after each sibling's next move, the number of candy in the bowl will drop by $3$ and become equal to $0$ after $198 ∶ 3 = 66$'s moves. Together, his brother will have made $1 + 66 = 67$ moves and eaten no more than $2$ candy in each move, so together he'll have eaten no more than $67  \cdot 2 = 134$ candy. * * (B) * * * Carlson can always win. In this case, the previous strategy is no longer working, because if his brother tries to apply it and Carlson eats one candy every move, then his brother will have to take two, and after $55$ moves he will be overeating and unable to eat more, though only $2 + 54 \cdot 3 = 164$ candy will be eaten. Let's describe a strategy Carlson can win with. In his first $70$ moves, he eats one candy each. After these moves, at least $140$ candy will have been eaten, so there are $60$ or fewer candy left. If the number of candy does not share 3 before his 71 st move, then he can already apply a * * (a) * * case strategy by picking up $1$ or $2$ candy, respectively, in each remaining move so that the remaining number of candy shares $3$ after his move. Since he can still eat $110 − 70 = 40$ sweets, it's enough for him to have at least another $20$ of moves, and the number of moves is certainly not going to be higher, because this strategy reduces the number of sweets by a $3$ per move, so most $20$ moves should be more than $60$ sweets. More interesting is the situation when the number of candy shares $3$ before Carlson's 71 st move. In that case, it is $57$ or less. Now, in each of his moves, Carlson can continue to eat one candy until after one of his moves, the number of candy in the dish is shared with the $3$ (and then further down he can use the classic strategy again). Let's prove that such a moment when, after Carlson's move, the number of candy in the bowl is shared with $3$ is bound to come. To prevent this, his brother would have to take $2$ of candy at every move. In that case, with $0$ candy left in the bowl, Carlson would have eaten no more than $70 + 57 ∶ 3 = 89$ candy, and so his brother would have eaten at least $200 − 89 = 111$ candy, contradicting the fact that he couldn't eat more than $110$ candy.
# <lo-sample/> LV.VOL.2024.12.4
Professor digit thought of a natural number in the $n$ and wrote the numbers $2^n$ and $14^n$ (in exactly that order) on the board, one after the other, without spaces, let's mark the typed number with a $C$ (for example, if $n=2$, then $C = 4196$). Is it possible that the number $C-1$ is a primary number? 
<small>
* questionType: Provedisprove
* domain: The resolution
</small> of NT # # will justify that the $C-1$ cannot be a primary number. Let's say otherwise that a natural number $n$ that the $C-1$ is a primary number is given. The sum of digits $2^n$ by module $3$ is $(−1)^n$. Similarly, the amount of digits $14^n$ by module $3$ will be $(−1)^n$. This means that the sum of the digits $C$ by module $3$ is $(−1)^n + (−1)^n$. If the number $n$ is odd, the sum of the digits in the number $C-1$ is divided by the $3$ because it $(−1)^n + (−1)^n − 1 \equiv −1 − 1 − 1 \equiv 0 \pmod 3$. So we conclude that the $n$ should be an even number. Now we're looking at the last digit of the number $C$. This will be determined unambiguously by the last digit of the number $14^n$. Since we are only interested in the last digit, we can study the last digit of the number $4^n$. | $4$ | $2$ | $n$ | $6$ | $8$ | $6$ | $10$ | | -------------- | --- | | | | $4^n \pmod 10$ | | | | | $6$ | | | | | | | $6$ | $6$ | $6$ | We note that the last digit of the number $C$ will always be $6$ if the $n$ is an even digit. This means that the last digit of the number $C-1$ will be $5$, or the number $C − 1$ will be divided by $5$. We get a contradiction with the assumption that $C - 1$ is a prime number.
# <lo-sample/> LV.VOL.2024.12.5
Find the largest real number in $A$ with the attribute that $3x^2 + y^2 + 1 \geq A(x^2 + xy + x)$ all real numbers $x$ and $y$. 
<small>
* questionType: Findoptimal
* domain: ALG
</small> 
# # solution
 First, we modify the given inequality equivalently: in $$\begin{aligned}
(3 − A)x^2 + y^2 - Axy - Ax + 1 & \geq 0; \\
\left(y - \frac{A}{2}x \right)^2 + \left( 3 - A - \frac{A^2}{4} \right) x^2 - Ax + 1 & \geq 0 \\
\end{aligned}$$, because the ${\displaystyle \left( y - \frac{A}{2}x \right)^2}$ to be counted will always be non-negative, and at the appropriate $y$ option equals $0$, we have to find the largest $A$ value so that the inequality in the $$\left( 3 - A - \frac{A^2}{4} \right)x^2 - Ax + 1 \geq 0$$ is true for all real numbers in the $x$. The branches of the corresponding square function must therefore be facing upwards, that is to say, the ${\displaystyle \left( 3 - A - \frac{A^2}{4} \right) \geq 0}$ je $A^2 + 4A - 12 \leq 0$, and the discriminant must be non-positive, that is to say, we $$A^2 - 4 \left( 3 - A - \frac{A^2}{4} \right) = 2A^2 + 4A - 12 \leq 0.$$ note that the branches of the corresponding square function will be facing upwards for any $A$ subject to a discriminatory condition. The maximum $A$ will be when you $2A^2 + 4A − 12 = 0$, because then it's possible that the initial inequality turns into an equal, that is, we've found the biggest $A$. The $2A^2 + 4A − 12 = 0$ root of the largest equation is $\sqrt{7} - 1$. As a result, we have obtained that the highest $A$ value is $\sqrt{7} - 1$. # # resolve looks at three positive numbers for the $\alpha, \beta, \gamma$ you want to $\alpha + \beta + \gamma = 3$. Then, by applying the inequalities between the mean and the mean geometric, we get the $$3x^2 + y^2 + 1 = (\alpha + \beta + \gamma)x^2 + y^2 + 1 = 
\alpha{}x^2 + (\beta{}x^2 + y^2) + (\gamma{}x^2 + 1) \geq \alpha{}x^2 + 2\sqrt{\beta}xy + \sqrt{\gamma}x.$$ because, in the provable inequalities, the numerable factors of the right-hand expression must be the same, then we choose $\alpha$, $\beta$, and $\gamma$ values to $\alpha = 2 \sqrt{\beta} = 2\sqrt{\gamma}$ what is equivalent to the $$\begin{array}{c}
2\alpha^2 = 4\beta + 4\gamma; \\
2\alpha^2 = 4(3 − \alpha); \\
\alpha^2 + 2\alpha − 6 = 0; \\
\alpha = −1 \pm \sqrt{7}. \\
\end{array}$$ So $\alpha = \sqrt{7} - 1$, because the $\alpha$ is positive. So $\beta = \gamma = 2 - \frac{\sqrt{7}}{2}$. If you take such coefficients, you $$3x^2 + y^2 + 1 \geq (\sqrt{7} − 1)(x^2 + xy + x)$$ all real numbers to $x$ and $y$, which means that the number $\sqrt{7} - 1$'t meet the given inequality. Furthermore, if we choose numbers $x$ and $y$ with the characteristic that, in $$\begin{array}{c}
\beta x^2 = y^2 = 1;\\
\left( 2 - \frac{\sqrt{7}}{2}\right) x^2 = 1;\\
x = \frac{1 + \sqrt{7}}{3},\;\;y=1\\
\end{array}$$, the inequality will become the same, from which we conclude that all the $A$ values of the number are greater than the $\sqrt{7} - 1$ do not satisfy the terms of the task, from which it can be inferred that the largest number $A$ to the required attribute is $\sqrt{7} - 1$.
