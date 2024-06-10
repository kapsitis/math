# <lo-sample/> LV.AMO.2022B.5.1

What is the smallest positive integer that uses only the digits $0$ and $2$ in its 
notation and is divisible by $15$? 

<small>

* concepts:positive-integer,digit,decimal-notation,divisibility
* questionType: Findoptimal
* domain: NT
* LTopic: The resolution

</small> 

## Solution

We show that the smallest number satisfying the conditions is $2220$. 
For a number to be divisible by $15$, it must be divisible by 
$3$ and $5$. To be divisible by $3$, the sum of its digits must be divisible by $3$.
So the number $2$ must appear at least $3$ times in that number.

To be divisible by $5$, the last digit of this number must be $0$. 
Consequently, the smallest number with that property has at least $4$ digits and equals $2220$.


# <lo-sample/> LV.AMO.2022B.5.2

Draw a hexagon with its sides on a square grid having perimeter equal to its area!  
*Note:* The area is the number of little squares that make up the hexagon and the 
perimeter is the number of sides of the little squares on its border.

<small>

* Concepts:hexagon,side,square-grid,perimeter,area,square,border
* questionType: Findexample
* domain: Geom
* LTopic: Ltpolygon

</small> 

## Solution

Consider the hexagon shown in Figure 1. Its perimeter is $20$ and the area is also $20$.

![](LV.AMO.2022B.5.2A.png)


# <lo-sample/> LV.AMO.2022B.5.3

$250$ tickets were made for the theatre performance and at least half of them were sold. It is known that exactly a third of the audience were schoolchildren, exactly one fifth of the audience were students and exactly one-seventh were retirees. How many tickets were sold? 

<small>

* cooked: for fractions, at-least
* questionType: Findall
* domain: NT
* LTopic:

</small> 

## Solution 

*Answer.* $210$ tickets were sold.

To divide viewership directly into three, into five, and 
into seven equal parts, the number of tickets sold 
should be divisible by $3$, $5$, and $7$. 
So the number of tickets sold should be divisible 
by $3 \cdot 5 \cdot 7=105$. Since at least half of the tickets 
were sold, the number of sold tickets is between $125$ and $250$. 
The only number divisible by $105$ in this interval is $210$.



# <lo-sample/> LV.AMO.2022B.5.4

The balance scales (a), (b) and (c) are all in equilibrium. 
How many arrows should be put in the place of the question mark so that the 
balance scale (d) is also in equilibrium? Justify your answer!

![](LV.AMO.2022B.5.4.png)

<small>

* Concept: Equality
* questionType: FindAll
* domain: ALG
* LTopic: LTEquationSystems

</small> 

## Solution

We need to place six arrows instead of the question mark. 
Let's express the mass of all the figures in "arrow units". 
From the balance (c), we conclude that the mass of the circle is 
four arrows. Consequently, the left side of 
balance (b) equals to six arrows that weigh 
as much as three squares. So the mass of one square is 
two arrows. 

Next, consider balance (a). By replacing the circle with four arrows 
and each square with two arrows, we get that the mass of the 
pentagon plus four arrows is ten arrows. 
So the mass of the pentagon alone is six arrows.


# <lo-sample/> LV.AMO.2022B.5.5

Each of the three girls, Elina, Guna and Maruta likes 
some color - either green, yellow, or orange. 
Each girl likes a different color, and dislikes the 
remaining two colors. 
Exactly one of the following claims is known to be true: 

* Guna doesn't like orange; 
* Elina doesn't like green; 
* Elina doesn't like orange. 

What colour does every girl like? Justify your answer! 

<small>
* Concept: true-statement
* questionType: FindAll
* domain: Comb
* LTopic: LTLogic
</small> 

## Solution 

Guna likes orange, Elina likes green, and Maruta likes yellow. 
At least one of the last two claims must be true since Elina cannot 
like both green and orange. As there is only one true statement, 
the first statement is certainly false, meaning Guna
actually likes orange. 

If Elina liked yellow, then the two last statements 
would both be true, which is impossible. Since Guna likes orange, 
we conclude that Elina likes the green. Thus, Maruta is left with
yellow.

# <lo-sample/> LV.AMO.2022B.6.1

All positive integers from $1$ to $2022$ are 
written on a piece of paper, each appearing once. 
First, Amanda circled all the numbers 
divisible by $3$ in red. She then circled all the 
numbers divisible by $5$ in blue. Finally, 
she circled all the numbers divisible by $7$ in 
green. 
How many numbers are circled with at 
least two different colors? 

<small>

* cooked: natural-numbers, divisibility
* questionType: Findcount
* domain: NT
* LTopic:

</small> 


## Solution

We show that $249$ numbers are circled with at least two colors.

We look at all numbers divisible by at least two of the given
numbers $3$, $5$, or $7$. 

* If a number is divisible by  $3$ and $5$, it is divisible by $15$. 
  Since $2022=15 \cdot 134+12$, there are $134$ numbers divisible by $15$. 
* If a number is divisible by $3$ and $7$, it is divisible by $21$. 
  Since $2022=21 \cdot 96+6$, there are $96$ numbers divisible by $21$ 
  out of those written on the paper. 
* If a number is divisible by $5$ and $7$, it is divisible by $35$. 
  Since $2022=35 \cdot 57+27$, there are $57$ numbers divisible by $35$. 
  
Note that there are several numbers divisible by all three numbers 
$3$, $5$, and $7$, so they are divisible by $3 \cdot 5 \cdot 7=105$. 
Since $2022 = 105 \cdot 19 + 27$, there are altogether $19$ 
numbers divisible by $105$. The numbers divisible by $105$ 
were counted as numbers divisible by $15$, $21$, and $35$. 
So they were counted three times. We conclude that together there are 
$134 + 96 + 57 - 2 \cdot 19 = 249$ numbers divisible by at least two 
numbers out of $3$, $5$, $7$, so they are circled with at least two colors.

# <lo-sample/> LV.AMO.2022B.6.2

Show how to cut ten shapes (as in Fig.2) from the given piece 
of grid paper (see  Fig. 1).
(Mark the lines where cuts should be made!) 
The figures can also be rotated. 

![](LV.AMO.2022B.6.2.png) 

<small>

* Concept: grid, shape, Rotation
* questionType: Findexample
* domain: Geom
* LTopic: Ltcuttingcoverscoloring

</small> 

## Solution 

See, for example, Fig.4.

![](LV.AMO.2022B.6.2A.png)



# <lo-sample/> LV.AMO.2022B.6.3

On a dark autumn night, Maris decided to add up all the 
positive integers from $1$ to $n$, where $n$ is some positive integer.
Could it happen that Maris gets a sum whose last digit is  
**(A)** $8$, **(B)** $9$? 

<small>
* cooked: natural-numbers, sum, last-digit
* questionType: Provedisprove, ProveDisprove
* domain: NT
* LTopic: Ltcongruencemodulo
</small> 

## Solution 

**(A)**  
Yes, he can. For example, be $1+2+3+4+5+6+7=28$. 

**(B)** 
No, he cannot. Here's a list of the sums $S_{n}$ for 
some small $n$: 

* $S_{1}=1$ 
* $S_{2}=1+2=3$ 
* $S_{3}=1+2+3=6$ 
* $S_{4}=1+2+3+4=S_{3}+4=6+4=10$ 
* $S_{5}=1+2+3+4+5=S_{4}+5=10+5=15$ 
* $S_{6}=S_{5}+6=15+6=21$ 
* $\circ$... 

Let's create a table showing the last digit 
of the number $n$ and the last digit of the sum $S_{n}$. 
Note that we can compute the last digit of the sum 
$S_{n}$ by adding the last digit of the previous 
sum to the last digit of $n$. 


| The last digit of $n$       | The last digit of $S_n$        | 
| --------------------------- | ------------------------------ |
| $\mathbf{1}$                | $\mathbf{1}$                   |
| 2                           | 3                              |
| 3                           | 6                              |
| 4                           | 0                              |
| 5                           | 5                              |
| 6                           | 1                              |
| 7                           | 8                              |
| 8                           | 6                              |
| 9                           | 5                              |
| 0                           | 5                              |
| 1                           | 6                              |
| 2                           | 8                              |
| 3                           | 1                              |
| 4                           | 5                              |
| 5                           | 0                              |
| 6                           | 6                              |
| 7                           | 3                              |
| 8                           | 1                              |
| 9                           | 0                              |
| 0                           | 0                              |
| $\mathbf{1}$                | $\mathbf{1}$                   |

Since the last digit of $n$ and the last digit of
the sum $S_{n}$ in the last row of this table 
are the same two numbers as in the first row, 
the values in the table will start repeating 
periodically. 
The digit $9$ never appears in the second column 
of the table, so it cannot be the last digit of any sum $S_n$.





# <lo-sample/> LV.AMO.2022B.6.4

The balance scales (a), (b) and (c) are known to be in equilibirum. 
How many circles should you put in place of the question mark so that the balance scale 
(d) is also in equilibrium? Justify your answer!

![](LV.AMO.2022B.6.4.png) 


<small>

* Concept: Equality
* questionType: FindAll
* domain: ALG
* LTopic: LTEquationSystems

</small> 

## Solution

*Answer.* The question mark should be replaced by five circles. 

We express the mass of all the shapes in "circle units". 
From the balance (c) we conclude that the mass of the pentagon 
equals to four circles. Thus the balance scale (b) has six circles 
on the left side, and this is the same as the mass of three arrows. 
So the mass of a single arrow equals to two circles. 

Next, consider the balance scale (a). By replacing the pentagon with 
four circles and each arrow with two circles, we get that the mass of 
the rectangle and five circles is the same as the mass of 
ten circles. So the rectangle has the mass of five circles.



# <lo-sample/> LV.AMO.2022B.6.5

Some of $273$ villagers always tell the truth, the remaining ones 
lie all the time. Each of the villagers has exactly one favourite 
day of the week. There was a poll of all the villagers, and they 
were asked to answer seven questions with either "Yes" or "No":

| Question                        |                |               |
| ------------------------------- | -------------- | ------------- |
| Is Monday your favorite day?    | $\square$ Yes  | $\square$ No  |
| Is Tuesday your favorite day?   | $\square$ Yes  | $\square$ No  |
| Is Wednesday your favorite day? | $\square$ Yes  | $\square$ No  |
| Is Thursday your favorite day?  | $\square$ Yes  | $\square$ No  |
| Is Friday your favorite day?    | $\square$ Yes  | $\square$ No  |
| Is Saturday your favorite day?  | $\square$ Yes  | $\square$ No  |
| Is Sunday your favorite day?    | $\square$ Yes  | $\square$ No  |


The number of "Yes" answers received to each question was as follows: 
Monday - $51$, Tuesday - $52$, Wednesday - $53$, Thursday - $55$, 
Friday - $54$, Saturday - $56$, Sunday - $57$. 
How many villagers lie all the time? 

<small>

* cooked: truth, falsehood, mapping
* questionType: Findcount
* domain: Comb
* LTopic: The ltlogic

</small> 

## Solution 

*Answer.* In the village there are $21$ liars. 

Alltogether there were $51+52+53+54+55+56+57=378$ answers “Yes”. 
Note that every villager who tells the truth answered "Yes" exactly once 
(for their favourite day) and every liar exactly six times 
(for all the days that aren't his/her favourite day). 
If we turn one resident who says the truth into a liar, then we get 
five surplus answers "Yes". In the beginning assume that 
everyone in the village is telling the truth; in this case 
there would be $273$ answers “Yes”. 
As there are $378$ answers "Yes", we have $378-273=105$ 
"redundant" answers "Yes". This can be achieved by turning $105:5=21$ 
villagers into liars.



# <lo-sample/> LV.AMO.2022B.7.1

The following text was written on the board: $A869B$. Each of the 
letters $A$ and $B$ must be replaced by one digit 
(they may or may not be the same) so that the resulting five-digit 
number is divisible by $15$. In how many ways can you do this?

<small>

* cooked: variable, Digit, divisibility
* questionType: FindCount
* domain: NT
* LTopic: The resolution

</small> 

## Solution

*Answer.* This can be done in $6$ ways. 
For a number $\overline{A869B}$ to be divisible by $15$, 
it must be divisible by both $3$ and $5$. 
Consider two possible cases for the digit $B$ such that it is disible by $5$. 

* If $B=0$, the sum of the digits is $A+8+6+9+0=A+23$. 
  To be divisible by $3$, the sum of digits must be divisible by $3$, 
  so the possible values for $A$ are $1$, $4$, or $7$. 
* If $B=5$, the sum of the digits is $A+8+6+9+5=A+28$. 
  To be divisible by $3$, the sum of digits must be divisible by $3$, 
  so the possible values for $A$ are $2$, $5$, or $8$. 
  
As a result, there are six different options for digits replacing $A$ and $B$
respectively: $(A,B) = (1,0)$, $(A,B)=(4,0)$; $(A,B)=(7,0)$, 
$(A,B)=(2,5)$; $(A,B)=(5,5)$; $(A,B)=(8,5)$.



# <lo-sample/> LV.AMO.2022B.7.2

Do there exist **(A)** $5$; **(B)** $15$ positive integers (some of them may be equal) such that their sum equals their product?

<small>

* Concept: sum, product
* questionType: Provedisprove
* domain: ALG
* LTopic: Ltequations, LTNumTheoryByCases

</small> 

## Solution 

**(A)** Yes, the numbers $1,1,2,2,2$ satisfy the condition, since 
$1+1+2+2+2=8$ and $1 \cdot 1 \cdot 2 \cdot 2 \cdot 2=8$ 

**(B)** Yes, such numbers exist. For example, $1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 15$ (13 copies of number $1$ and also numbers $2$ and $15$), 
since $13 \cdot 1+2+15=30$ and $1 \cdot 2 \cdot 15=30$. 

*Note* For (A) the solutions $1,1,1,3,3$ or $1,1,1,2,5$ are also valid.


# <lo-sample/> LV.AMO.2022B.7.3

Show how to draw $6$ lines in a plane and mark $7$ points on the lines so that 
exactly three points are marked on each line! 

<small>
* Concept: Plane, line, point
* questionType: Findexample
* domain: Geom
* LTopic: Resolution
</small> 

## Solution 

An possible answer is shown in Fig.5. 

![](LV.AMO.2022B.7.3A.png)



# <lo-sample/> LV.AMO.2022B.7.4

There's a pile of candies on the table. Karlsson and Lillebror 
(Little Brother) take turns making moves, with Karlsson starting the game. 
In one move, a player can remove from the pile and 
eat either one or two candies. The player who eats the last candy wins. 
Which player, can always win if there are initially
**(A)** $6$ candies in the heap; **(B)** $2022$ candies in the heap? 

<small>

* cooked: game, set, Remove, to-win
* questionType: Algorithm, Algorithm
* domain: NT
* LTopic:

</small> 

## Solution 

Lillebror can win in both cases. To achieve this, he can proceed 
as follows: in every move, if Karlsson eats one candy, then Lillebror 
eats two, and vice versa, if Karlsson eats two, then Lillebror eats one. 
Playing like this, after every pair of moves the number of candies 
in the pile drops by exactly $3$. Since initially the number of 
candies was divisible by $3$ (both $6$ and $2022$ are divisible by $3$), 
in either case it will become $0$ after a move by Lillebror, 
so the Lillebror will win. 

*Note.* In case (A), Lillebror will win after his second move. In case
(B), Lillebror will win after the $2022:3=674$ moves.



# <lo-sample/> LV.AMO.2022B.7.5

Some of $272$ villagers always tell the truth, the remaining ones 
lie all the time. Each of the villagers has exactly one favourite 
day of the week. There was a poll of all the villagers, and they 
were asked to answer seven questions with either "Yes" or "No":

![](LV.AMO.2022B.7.5.png) 

The number of "Yes" answers received to each question was as follows: 
Monday - $53$, Tuesday - $54$, Wednesday - $55$, Thursday - $57$, 
Friday - $56$, Saturday - $58$, Sunday - $59$. 
How many villagers lie all the time? 



<small>

* cooked: truth, falsehood, mapping
* questionType: Findcount
* domain: Comb
* LTopic: The resolution

</small>



## Solution 

*Answer.* In the village there are $24$ liars. 

Alltogether there were $53+54+55+56+57+58+59=392$ answers "Yes". 
Note that every villager who tells the truth answered "Yes" exactly once 
(for their favourite day) and every liar exactly six times 
(for all the days that aren't his/her favourite day). 

If we turn one resident who says the truth into a liar, then we get 
five surplus answers "Yes".
In the beginning assume that 
everyone in the village is telling the truth; in this case 
we would have $272$ answers “Yes”. 


Since we have 392 answers "Yes", we have $392-272=120$ "redundant" answers "Yes". 
This can be achieved by turning $120:5=24$ villagers into liars.




# <lo-sample/> LV.AMO.2022B.8.1

The following text was written on the board: $N597M$. Each of the letters 
$N$ and $M$ should be replaced by a digit (they may or may not be 
the same) so that the resulting five digit number is divisible by $12$. 
In how many ways can you do this?


<small>

* cooked: divisibility, variable, digit
* questionType: Findcount
* domain: NT
* LTopic: The resolution

</small>

## Solution 

The requirements can be satisfied in $6$ different ways. 
In order to have a number $\overline{N597M}$ divisible by $12$, 
it must be divisible by $3$ and by $4$. 
To be divisible by $4$, the last two digits must be divisible by $4$. 
Let's look at two possible cases for the digit $M$ to achieve
divisiblity by $4$. 

* If $M=2$, the sum of digits is $N+5+9+7+2=N+23$. 
  To be divisible by $3$, the sum of its digits must be divisible by $3$,
  so the possible values of $N$ are $1$, $4$, or $7$. 
* If $M=6$, the sum of digits is $N+5+9+7+6=N+27$. 
  To be divisible by $3$, the sum of its digits must divisible by $3$, 
  so the possible values of $N$ are $0$, $3$, $6$, or $9$. No number can
  begin with a $0$, so the possible values of $N$ are $3$, $6$, or $9$. 
  
As a result, there are six different options how to replace $N$ and $M$: 
$(N,M)=(1,2)$; $(N,M)=(4,2)$; $(N,M)=(7,2)$; $(N,M)=(3,6)$; 
$(N,M)=(6,6)$; $(N,M)=(9,6)$.


# <lo-sample/> LV.AMO.2022B.8.2

The student had to complete a homework with $20$ tasks. For each task 
$8$ points are added, if the solution is correct, $5$ points are 
subtracted, if the solution is wrong, and $0$ points is given, 
if the task is not attempted. How many tasks did a student solve 
correctly, if his total score is $13$? 

<small>

* cooked: add, subtract
* questionType: Findall
* domain: ALG
* LTopic: Ltequations

</small>

## Solution 

*Answer.* The student solved $6$ tasks correctly. 

Let us show that this answer is the only possibility. 
Let $x$ denote the number of tasks that were solved correctly, but $y$ denotes the number tasks that were wrong. 

Consider all solutions for the equation $8x-5y=13$. Since $8x$ is 
even, then $5y$ and $y$ must be odd. When expressing $x$, we would get $x=(13+5y):8$. As there were $20$ tasks in total, so there are only $6$ 
different values of $y$ such that $x+y \leq 20$. 
Indeed, if $y \geq 12$, then $x>9$ and $x+y>20$. 

If the calculated $x$ value is a positive integer, the resulting 
$x$ and $y$ values are valid. The table shows that the only 
valid values are $x=6$ and $y=7$, so the student solved $6$ tasks 
correctly, solved $7$ tasks incorrectly, and $7$ tasks were not attempted. 

| $\boldsymbol{y}$ | Is $x=(13+5y):8$ a positive integer? |
| ---------------- | ------------------------------------ |
| $\mathbf{1}$     | No                                   |
| $\mathbf{3}$     | No                                   |
| $\mathbf{5}$     | No                                   |
| $\mathbf{7}$     | Yes, $x=6$                           |
| $\mathbf{9}$     | No                                   |
| $\mathbf{11}$    | No                                   |




# <lo-sample/> LV.AMO.2022B.8.3

In a triangle $ABC$ on the side $BC$ there is a point $D$ 
such that $AD = BD$ and $AB = DC = AC$. Calculate the angles 
of $ABC$! 

<small>

* Concept: triangle
* questionType: Findall
* domain: Geom
* LTopic: Lttriangles

</small> 

## Solution 

Since $AD=BD$, the triangle $ABD$ is an isosceles 
triangle with the base $AB$ and both angles at the base 
are equal, hence $\sphericalangle ABD=\sphericalangle BAD=\alpha$ 
(see Figure 6). 

We get from the triangle $ABD$ that 
$\sphericalangle ADB=180^{\circ}-\alpha-\alpha=180^{\circ}-2 \alpha$. 
Note that $\sphericalangle ADC = 180^{\circ} - \sphericalangle ADB=180^{\circ}-\left(180^{\circ}-2 \alpha\right)=2 \alpha$ as 
supplementary angles. Since the $AC=DC$, the triangle $ACD$ 
is also isosceles and angles at its base are the same, hence  $\sphericalangle DAC=\sphericalangle ADC = 2\alpha$. 

Since $AB=AC$, the triangle $ABC$ is also isosceles and the angles
at its base are the same, hence 
$\sphericalangle ABC=\sphericalangle ACB=\alpha$. 
From the triangle $ACD$, we get that

$$\sphericalangle ADC+\sphericalangle DAC+\sphericalangle ACD = 2 \alpha+2 \alpha+\alpha=180^{\circ}$$ 

By solving $5 \alpha=180^{\circ}$, we get that $\alpha=36^{\circ}$. 
Find all the angles in triangle $ABC$: 

- $\sphericalangle ABC = \sphericalangle ACB = \alpha=36^{\circ}$;
- $\sphericalangle BAC = \sphericalangle BAD + \sphericalangle DAC = \alpha+2 \alpha=108^{\circ}$.

![](LV.AMO.2022B.8.3A.png)


# <lo-sample/> LV.AMO.2022B.8.4

Is it possible to arrange the numbers  
**(A)** $0;\;1;\;2;\;3;\;4;\;5;\;6;\;7;\;8;\;9$   
**(B)** $0;\;1;\;2;\;3;\;4;\;5;\;6;\;7;\;8;\;9;\;10;\;11;\;12;\;13$  
around a circle so that any two adjacent numbers differ by $3$, $4$, or $5$?


<small>

* Concepted: Integer-numbers, distance
* questionType: Provedisprove, ProveDisprove
* domain: NT
* LTopic: Ltnumtheoryexamples

</small> 

## Solution

**(A)** Let us show that it is impossible. Note that the numbers 
$0$; $1$; $2$; $8$ and $9$ cannot be written next to each other 
as the difference between any two of them is not $3$; $4$ or $5$. 
So they should be written on the circle by skipping one position 
between any two of them (See Fig.7, where the letters indicate 
places where these five numbers should go.)

You can only write $7$ next to $2$ because their difference is $5$, 
but $7$ cannot stand next to any of the other numbers $0$, $1$, $8$, or $9$. 
So it is impossible to place $7$ anywhere on the circle, so the 
given numbers cannot be written in a way that 
every two adjacent numbers differ by $3$, $4$, or $5$. 

**(B)** Yes, for example, see Fig.8. Inside the circle the numbers 
indicate by how much any two neighboring number differ. 

![](LV.AMO.2022B.8.4A.png)


# <lo-sample/> LV.AMO.2022B.8.5

Five friends started arguing, and they stated the following: 

* Elina says: "I always speak the truth."
* Guna says: "Elina and Agnese are both lying."
* Maruta says: "Everyone speaks the truth."
* Agnese says: "Elina lies."
* Emils says: "Everyone lies." 

It is known that each friend either always speaks the truth 
or always lies. 
How many friends speak the truth? 

<small>

* cooked: truth, falsehood
* questionType: Findcount
* domain: Comb
* LTopic: Ltlogic

</small> 

## Solution 

*Answer.* We show that only one of the friends speaks the truth. 
Note that: 

- If Elina speaks the truth, then Agnese lies.  
  So they cannot both speak the truth. 
- If Agnese lies, then Elina says the truth, so the cannot both lie. 

Thus, either Elina or Agnese speaks the truth and the other one lies. 
It follows that Guna, Maruta and Emils lie. 
So only one of the friends speaks the truth (it is either Elina or Agnese). 



# <lo-sample/> LV.AMO.2022B.9.1

How many four-digit numbers $\overline{ABBA}$ are there that are 
divisible by $99$? (The same letters are replaced by the same digits,
but different letters may or may not be the same.)

<small>

* concepts: divisibility, Digit, variable
* questionType: Findcount
* domain: NT
* LTopic: The solution

</small> 

## Solution 

There are $10$ numbers that satisfy the conditions: 
$1881$, $2772$, $3663$, $4554$, $5445$, $6336$, $7227$, $8118$, $9009$, $9999$. For a number to be divisible by $99$, it must 
be divisible by both $11$ and $9$. 
Note that the given number is divisible by $11$, since the 
sum of digits in odd positions 
minus the sum of digits in even positions equals $0$, so it is divisble by $11$. 

To be divisible by $9$, the sum of its digits must be divisible by $9$. 
So $A+B+B+A=2(A+B)$ should be divisible by $9$. 
Since $A$ and $B$ are numbers, two cases are possible: 
$A+B=9$ or $A+B=18$. If $A+B=9$, there may be nine cases: 
$$A+B=1+8=2+7=3+6=4+5=5+4=6+3=7+2=8+1=9+0.$$ 

If you $A+B=18$, you can only have one case $A+B=9+9$.



# <lo-sample/> LV.AMO.2022B.9.2

Is the inequality always true: $x + \frac{9}{x} > y + \frac{9}{y}$, if 
**(A)** $x > y > 0$,  **(B)** $x > y > 3$? 

<small>

* Concept: Inequality
* questionType: Provedisprove, ProveDisprove
* domain: ALG
* LTopic: Ltinequalities

</small> 

## Solution 

**(A)** 
No. For example, take $x=1$, and $y=0.1$. Then 
$x+\frac{9}{x}=10$ and $y+\frac{9}{y}=90.1$, but $10<90.1$. 

**(B)** 
We show that for $x>y>3$, the inequality given is true. 

Multiply both sides of the inequality $x+\frac{9}{x}>y+\frac{9}{y}$ 
by a positive expression $xy$, get an equivalent expression: 

$$x^{3} y+9 y>x y^{2}+9x.$$

In order to prove that the inequalities are true, 
it is sufficient to show that the $x^{2}y + 9y - xy^{2} - 9x>0$. 
Notice that we have $x-y>0$ and $xy-9>0$ since it is given that $x>y>3$. 
We look at the product of two positive expressions 
and rewrite it as follows: 

$$0 < (xy-9)(x-y) = x^{2}y - xy^{2} - 9x + 9y$$. 

So we proved the necessary inequality.


# <lo-sample/> LV.AMO.2022B.9.3

In a right triangle $ACB$ ($\sphericalangle C = 90^{\circ}$) 
$CH$ is an altitude. On the side $AC$ we mark a point $K$ 
so that $\sphericalangle CBK = \sphericalangle BAC$. 
Prove that the line $CH$ divides the segment $BK$ in half! 

<small>

* Concept: right-triangle, alter, line, segment
* questionType: Prove
* domain: Geom
* LTopic: The

</small> 
 
## Solution

Denote the intersection of $CH$ and $KB$ with $O$ and $\sphericalangle CBK=\sphericalangle BAC=\alpha$, 
$\sphericalangle ABC=\beta$ (see Fig.9). 
From the triangle $ABC$, we get that 
$\sphericalangle BAC=180^{\circ}-\sphericalangle ACB-\sphericalangle ABC$, 
or $\alpha=90^{\circ}-\beta$. 

From the triangle $BHC$ we get that 
$\sphericalangle HCB=180^{\circ}-\sphericalangle CHB-\sphericalangle HBC=90^{\circ}-\beta=\alpha$, hence the triangle $COB$, is an equilateral triangle as two of its angles are 
equal to $\sphericalangle OBC=\sphericalangle OCB=\alpha$. It follows that 
$BO = OC$ as to legs of an isosceles triangle.

We get from the triangle $KCB$ that 
$\sphericalangle BKC=180^{\circ}-\sphericalangle KCB-\sphericalangle KBC =  90^{\circ}-\alpha=\beta$.
Notice that 
$\sphericalangle ACH = \sphericalangle ACB - \sphericalangle HCB = 90^{\circ} - \alpha = \beta$. 
So the triangle in the $KOC$ is isosceles because two of its angles are equal: 
$\sphericalangle OKC=\sphericalangle KCO = \beta$ and its side edges are the same $CO=OK$. 
From the equalities $BO=OC$ and $CO=OK$, we get that $BO=OK$, hence $CH$
divides segment $BK$ in half. 

![](LV.AMO.2022B.9.3A.png)



# <lo-sample/> LV.AMO.2022B.9.4

Is it possible to arrange the numbers  
**(A)** $1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13$;  
**(B)** $1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14$  
on a circle so that any two adjacent numbers differ by $3$; $4$ or $5$? 

<small>

* Concepted: Integer-numbers, distance
* questionType: Provedisprove
* domain: NT
* LTopic: Ltnumtheoryexamples

</small> 

## Solution 

**(A)** We show that it is impossible.  
Note that the numbers $1$; $2$; $3$; $11$; $12$ and $13$ 
cannot stand next to each other because the difference between 
any two of these numbers is not $3$, $4$ or $5$. 
So they should be written on the circle by skipping one position
between any two of them; after that there are there are only two 
adjacent positions left without numbers (Fig.10). 

Number $4$ can be only next to $1$ as their difference is $3$, but 
it cannot be next to any other numbers already written ($2,3,11,12,13$). 
So the number $4$ should take one of the two adjacent unoccupied positions.

Number $10$ can be next to $13$, but it cannot be next to any other 
numbers already written ($1,2,3,11,12$). So, $10$ should take another 
one of the two adjacent unoccupied positions. 
We conclude that numbers $4$ and $10$ should be written 
next to each other, but there is a contradiction with the 
condition of the problem, as their difference is $6$. 
Hence the given numbers cannot be written around the circle so that 
any two adjacent numbers differ by $3$; $4$ or $5$. 

**(B)** Yes, for example, see Fig.11, where the inside of the 
circle shows the difference between any two adjacent numbers.


# <lo-sample/> LV.AMO.2022B.9.5

The floor plan of the art museum shall is a rectangle 
of size **(A)** $8 \times 9$; **(B)** $9 \times 11$ squares, 
where one square corresponds to a single museum room. 
The director of the museum wants to create a visitor route 
that satisfies the following properties: 

* the route starts in one of the squares (rooms) at the 
  edge of the rectangle; 
* a visitor on his route can move from one square (room) to another 
  square (room), if they share a border. 
* the visitor enters each square (room) exactly once during the route;
* the route ends in a square (room) at the edge of the rectangle 
  and is located next to the square (room) that started the route.

Can the director of the museum create such route? 

<small>

* Concept: grid, square-side, rectangle, path
* questionType: Provedisprove, ProveDisprove
* domain: Comb
* LTopic: Ltgraphs

</small> 



## Solution 

**(A)** Yes, he can. See, for example, Fig.12. 

![](LV.AMO.2022B.9.5A.png){ width=200px }

**(B)** 
We prove that the required route cannot be created. 
Let us color the rectangular squares as a chessboard 
and note that this coloring ensures that any two 
adjacent boxes have different colors. 

Assume by contradiction that such route does exist. 
Since the route passes
through all the squares with odd numbers, the transition 
from white to black or vice versa occurs even number of 
times. Hence, the route will end in a square of the same 
color as the starting square. However, this is impossible,
because that square is next to the square where the route 
started. This is a contradiction and therefore 
no such route exists.



# <lo-sample/> LV.AMO.2022B.10.1

What is the last digit of $2022^{2022}$? 

<small>
* Concept: power, last-digit
* questionType: Findall
* domain: NT
* LTopic: Ltcongruencemodulo
</small> 

## Solution 

We find the last digit of the number by looking at it 
modulo $10$ (finding its remainder when dividing by $10). 
Notice that $2022^{2022} \equiv 2^{2022}(\bmod 10)$. 
So we need to find the last digit of $2^{2022}$. 

The sequence $2^{n}, n=1,2, \ldots$, is periodic modulo $10$. 
Look at its first terms. 

* if $n=1$, then $2^{1} \equiv 2 \pmod {10}$; 
* if $n=2$, then $2^{2} \equiv 4 \pmod {10}$; 
* if $n=3$, then $2^{3} \equiv 8 \pmod {10}$; 
* if $n=4$, then $2^{4} \equiv 16 \equiv 6 \pmod {10}$; 
* If $n=5$, then $2^{5} \equiv 32 \equiv 2 \pmod {10}$. 

This information can be summarized in a table: 

| $n$   | $2^n \pmod {10}$ |
| ----- | ---------------- |
| $1$   | $\mathbf{2}$     |
| $2$   | $4$              |
| $3$   | $8$              |
| $4$   | $6$              |
| $5$   | $\mathbf{2}$     |

We see that the sequence $2^{n}(\bmod 10)$ is periodic
with a period $4$. Since $2022=4 \cdot 505+2$, the sequence 
will make $505$ full periods, and its 
$2022$-th term same as its second term, so it is equal to $4$. 

We conclude that the last digit of $2022^{2022}$ is $4$. 

 
## Solution 

The last digit of this number is determined by 
finding the congruence class of the number modulo $10$. 
Given that we $2^{4} \equiv 16 \equiv 6(\bmod 10)$ and 
$6^{n} \equiv 6(\bmod 10)$, we get that

$$2022^{2022} \equiv 2^{2022} \equiv 2^{2020} \cdot 2^{2} \equiv\left(2^{4}\right)^{505} \cdot 4 \equiv 6 \cdot 4 \equiv 4 \pmod {10}.$$ 

So the last digit of the number $2022^{2022}$ is $4$.




# <lo-sample/> LV.AMO.2022B.10.2

Consider $n$ consecutive positive integers. 
Can we divide them into two groups so that the sum 
of the numbers in each group is a prime number if 
**(A)** $n = 8$, **(B)** $n = 10$? 
Each group must contain at least $2$ numbers. 

<small>
* Concept: PRIMES, natural-numbers, disjoint-Sets, sum
* questionType: Provedisprove, ProveDisprove
* domain: NT
* LTopic: For ltnumtheoryexamples, LTDivisibility
</small> 

## Solution 

**(A)** Yes, for example, numbers from $1$ to $8$ can be 
divided into the following two groups: 

$$1+2+4=7 \text{ un } 3+5+6+7+8=29$$ 

**(B)** No, it is impossible. Among any $10$ consecutive 
numbers there are $5$ even and $5$ odd numbers, so the sum 
of all $10$ numbers is odd. 
Therefore one of the groups add up to an odd number, 
but another one to an even number. 
As the sums of both groups are larger than $2$, 
the even number cannot be a prime.



# <lo-sample/> LV.AMO.2022B.10.3

There is a right triangle $ACB$; on its hypotenuse $AB$ 
there is a point $O$, which is the centre of a circle 
of radius of $3$ touching both legs (catheti) of the triangle.
Calculate the area of triangle $ACB$, if $OB = 5$. 

<small>
* Concept: right-triangle, area, legs-in-right-triangle, circle, tangent
* questionType: Findall
* domain: Geom
* LTopic: Lttriangles
</small> 

## Solution 

Denote the points where the circle touches the legs $CB$ and $CA$ by 
$M$ and $N$ respectively (see Fig.13). Since the radius $OM$ is perpendicular 
to the tangent $CB$, the triangle $OMB$ is right. 
By Pitagorean theorem $MB=\sqrt{OB^{2}-MO^{2}}=\sqrt{25-9}=4 \mathrm{~cm}$. 

Since the radii are perpendicular to the tangents and the 
triangle $ACB$ is right, the quadrilateral $ONCM$ has three right angles: 
$\sphericalangle NCM=\sphericalangle CNO=\sphericalangle CMO=90^{\circ}$. 
In this quadrilateral $ONCM$ two sides are the same: $ON=OM$ as two radii, 
so the quadrilateral $ONCM$ is a square and 
$MC=OM=3 \mathrm{~cm}$, $CB=BM+MC=7 \mathrm{~cm}$. 
Note that $\triangle OMB \sim \triangle ACB$ because of the 
condition $\ell \ell$ since they have $\sphericalangle B$
in common and $\sphericalangle OMB=\sphericalangle ACB=90^{\circ}$. 

Then $\frac{AC}{OM}=\frac{CB}{MB'}$, and we get 
$AC=\frac{OM \cdot CB}{MB}=\frac{3 \cdot 7}{4}=5,25 \mathrm{~cm}$. 
Hence $S_{ACB}=\frac{AC \cdot CB}{2}=18 \frac{3}{8} \mathrm{~cm}^{2}$.

![](LV.AMO.2022B.10.3A.png)


# <lo-sample/> LV.AMO.2022B.10.4

Consider three real numbers $a$, $b$, $c$ with $abc = 1$. 
Prove that the equation 

$$ax^4 + (2b + a)x^2 - 2cx + b^3c + bc + bc^3 = 0$$ 

has no real roots! 

<small>
* Concept: equation, real-numbers, root
* questionType: Prove
* domain: ALG
* LTopic: The resolution
</small> 

## Solution 

Multiply both sides of the equation by $a$ and 
makes equivalent transforms (using $abc=1$): 

$$\begin{gathered}
a^{2} x^{4}+\left(2 a b+a^{2}\right) x^{2}-2 a c x+a b^{3} c+a b c+a b c^{3}=0 \\
a^{2} x^{4}+2 a b x^{2}+a^{2} b^{2}-2 a c x+b^{2}+1+c^{2}=0 \\
\left(a^{2} x^{4}+2 a b x^{2}+b^{2}\right)+\left(a^{2} x^{2}-2 a c x+c^{2}\right)+1=0 \\
\left(a x^{2}+b\right)^{2}+(a x-c)^{2}+1=0
\end{gathered}$$ 

The left side of the last equation is at least $1$, since both 
squares are nonnegative. Hence the equation does not have real roots.


# <lo-sample/> LV.AMO.2022B.10.5

Five deputies (MPs) arrived at a restaurant and some of them shook hands with each other 
before lunch. It is known that if two deputies did not shake hands with each other, 
they did at least five handshakes together. Prove that deputies can be seated around 
a circular table so that each deputy has shaken hands with both people seated next to 
him/her. 


<small>
* cooked: Graph, Vertex, edge
* questionType: Prove
* domain: Comb
* LTopic: Ltgraphs
</small> 


## Solution 

First let's justify that of any three Members at least two have shaken hands with each other. Pieṇemsim the contrary that three Members have not made any handshakes between themselves. Let's take any two of them, then together they've made ̌ I's biggest four handshakes (each with two remaining MPs) - a contradiction. (1) Secondly, let us state that each Member has made at least two handshakes. Let's just say the opposite that some MP has only done one (or no) handshake. Let us mark this Member with a $X$ and one of the Members to whom he did not shake hands, let us sign Mr Y. the Member $X$ has shaken his hand no more than once and the Member $Y$ no more than three times (because he did not shake hands with the Member in $X$), so together they have shaken hands no more than 4 times - a contradiction. (2) Thirdly, let us note that if two Members did not shake hands with each other, at least one of them shook hands with all three others. (If the pair had any “omitted” handshake, then the pair would have the biggest $2+2=4$ handshakes together). (3) Pieṇemsim that two Members did not shake hands with each other (if they all shook, then they could be placed in patrol) and put them in places in $A$ and $C$ (see Figure 14), let's put in place the $C$ who shook hands with everyone else (of (3) that is certainly the case). In the future, we will refer to these two Members as $A$ and $C$.! [] (LV.AMO.2022B.10.5A.png) two possible years: * If the $A$ has also shaken hands with all three others, then we'll put the rest in places $B$, $D$ and $E$ so that someone who has shaken hands with each other is sitting in places $D$ and $E$ (of (1) they certainly are). If the $A$ has not shaken hands with another Member, then let us put it in place of the $E$. (and let's call the Members' $E$ below). MP $A$ has certainly shaken hands with the two remaining MPs (otherwise he would have done just one handshake). MEP $E$ has certainly shaken hands with at least one of the remaining two MPs (otherwise $E$ would have done just one handshake), let's put this MP in place in $D$. It is evident that what has been demanded has been achieved with this. 


## Solution 

let us see that if any Members did not shake hands with each other, then they hate each other. It follows from the above that if any two Members hate each other, then together the two viṇi hate another larger one. It's easy to see from this that a Member can hate the biggest two other members. Our job is to put them around the table so that two who hate each other don't sit next to each other. Pieṇemsim there is an MP who hates two other MPs. Let's put this MP in place A (see Figure 14) and those he hates -- places in $C$ and $D$ (Let us refer to these Members as $A, C$ and $D$, respectively). Let's note that all three of these MPs don't hate either of the other two. Indeed, since $A$ and $C$ hate each other and $A$ hate $D$, they ($A$ and $C$) can't hate anyone else anymore. The same judgment may also be given in respect of $A$ and $D$. So by putting the two remaining members in seats in $B$ and $E$, what has been demanded has been achieved. It remains to be seen where every Member hates the biggest one other Member. Then we have the biggest two pairs of MPs who hate each other by landing them not side by side (e.g. in places in $A$ - $C$ and $B$ - $D$) the demands will have been made.


# <lo-sample/> LV.AMO.2022B.11.1

Can $2022$ be expressed as the sum of cubes of two integers? 

<small>
* cooked: sum, cube-ALG, integer-numbers
* questionType: Provedisprove
* domain: NT
* LTopic: Ltcongruencemodulo
</small> 

## Solution 

Let's first find out who can be congruent integer cubes by moduḷa $9$: * if $n \equiv 0\pmod 9$, then $n^{3} \equiv 0^{3} \equiv 0\pmod 9$; * If $n \equiv 1\pmod 9$, $n^{3} \equiv 1^{3} \equiv 1\pmod 9 ;$ * if $n \equiv 2\pmod 9$, then $n^{3} \equiv 2^{3} \equiv 8 \equiv-1\pmod 9$; * if $n \equiv 3\pmod 9$, then $n^{3} \equiv 3^{3} \equiv 27 \equiv 0\pmod 9$; * if $n \equiv 4\pmod 9$, then $n^{3} \equiv 4^{3} \equiv 64 \equiv 1\pmod 9$; * if $n \equiv 5 \equiv-4\pmod 9$, then $n^{3} \equiv(-4)^{3} \equiv-1\pmod 9$; * if $n \equiv 6 \equiv-3\pmod 9$, then $n^{3} \equiv(-3)^{3} \equiv 0\pmod 9$; * if $n \equiv 7 \equiv-2\pmod 9$, then $n^{3} \equiv(-2)^{3} \equiv 1\pmod 9$; * If $n \equiv 8 \equiv-1\pmod 9$, then $n^{3} \equiv(-1)^{3} \equiv-1\pmod 9$. So integer cubes are congruents with 0 or $\pm 1$ after moduḷa 9. Let's look at what can be the sum of two integer cubes of a congruent by moduḷa $9$. | $a^{3}\pmod 9$ | -1 | 0 | 1 | | |: ---: |: --- |: --- |: --- | | | $b^{3}\pmod 9$ | | | | | | -1 | -2 | -1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 2 | We've gotten that the sum of two such numbers by moduḷa $9$ can pieṇemt any of the values in $-2,-1,0,1,2$, but none else. Because the $2022 \equiv 6 \equiv-3 \pmod 9$ does not appear between these values, the sum of two integer cubes cannot be $2022$.

# <lo-sample/> LV.AMO.2022B.11.2

For what real $p$ values is the sum of the root squares of the equation $x^2 + x + p = 0$ $16$? 

<small>
* Concept: equation, square-ALG, sum, value
* questionType: Findall
* domain: ALG
* LTopic: The
</small> resolution of ltequations 


## Solution 

will represent the root of the square equation with $x_{1}$ and $x_{2}$. After Viet's theorem, $x_{1} x_{2}=p$ and $x_{1}+x_{2}=-1$ are known. Using the sum square formula, we can calculate that we have $$x_{1}^{2}+x_{2}^{2}=\left(x_{1}+x_{2}\right)^{2}-2 x_{1} x_{2}=1-2 p=16$$ obtained that we $2p=-15$ or $p=-7,5$.

# <lo-sample/> LV.AMO.2022B.11.3

The circle drawn into the triangle by the $ABC$ touches the edge at the $AB$ point in a $D$ way that $AD = 8$ and $BD = 1$. Calculate the $BC$ length of the edge if the $B$ size of the triangle is $120^{\circ}$. 

<small>
* Concept: triangle, inscribed-circle, angle, tangent
* questionType: Findall
* domain: Geom
* LTopic: The resolution
</small> of ltcircleandrelatedangles 

## Solution 

represents the $BC$ line's touch point to the edge of the riṇka with a $E$ and the edge $AC$ with a $F$: figure 15 As a circle is drawn nogriežṇi into the triangle, the $ABC$ of the touches are the same: $BD=BE=1$, $AD=AF=8$ and $CE=CF=x$. So $AB=9, BC=1+x, AC=8+x$. Using cosine theorem, we get $AC^{2} = AB^{2} + BC^{2} - 2 \cdot AB \cdot BC \cdot \cos \Varangle B$ $(8+x)^{2}=9^{2}+(1+x)^{2}-2 \cdot 9 \cdot(1+x) \cdot \cos 120^{\circ}$ $5x=27$ $x=5.4$. So $BC=1+x=6.4$.! [] (LV.AMO.2022B.11.3A.png)


# <lo-sample/> LV.AMO.2022B.11.4

To demonstrate that each natural number greater than the $3$ can be expressed in one single way as the sum of three $x,y,z$ ($x \leq y \leq z$) of natural numbers so that the $x$, $y$, $z$ unequal $$x^2 + y^2 + z^2 - xy - yz - xz \leq 1.$$ 

<small>
* concepted: Inequality, natural-numbers, sum
* questionType: Prove
* domain: NT
* LTopic: Lttransformsnumtheory
</small> 

## Solution 

Let's note that $$\begin{gathered}
(x-y)^{2}+(y-z)^{2}+(z-x)^{2}=x^{2}-2 x y+y^{2}+y^{2}-2 y z+z^{2}+z^{2}-2 x z+x^{2}= \\
=2\left(x^{2}+y^{2}+z^{2}-x y-y z-x z\right) \leq 2
\end{gathered}$$ So $(x-y)^{2}+(y-z)^{2}+(z-x)^{2} \leq 2$. It follows from the resulting inequality that the only possible triplets of figures in the $(x ; y ; z)$ that satisfy it are $(k;k;k)$, $(k;k;k+1)$ and $(k;k+1;k+1)$. This means that the first three can express all the numbers that are congruent with the number $0$ by module $3$; with the second three, all numbers that are congruent with the number $1$ by moduḷa $3$ and with the third three can be expressed all skaițus that are congruent with the number $2$ by moduḷa $3$. You can see that the resulting distribution is unique each time.


# <lo-sample/> LV.AMO.2022B.11.5

The art museum's layout is a rectangle with dimensions $m \times n$ ($m \geq 2$, $n \geq 2$) boxes, where one box corresponds to one museum room. The head of the museum wants to create a visitor route that fulfills the following characteristics: * the route starts in one of the boxes (rooms) at the edge of the rectangle; * a visitor can move from one box (room) to another box (room) if they share a border. * the visitor visits each box (room) directly once during the route; * the route ends in the box (room) next to the edge of the rectangle next to the route start box (room). What $m$ and $n$ values can a museum manager create the following route? 

<small>
* Concept: grid, square-side, rectangle, path
* questionType: Findall
* domain: Comb
* LTopic: Ltgraphs
</small> 

## Solution 

Resolution the Museum Manager can create the described route for all $m;n \geq 2$ values for which at least one of the $m$ or $n$ shares 2. Here are three cases. 1. If you $m=2$ and $n \geq 2$, turn the rectangle so that the $m=2$ has the number of rows. So the first part of the route leads from the bottom left corner to the bottom right corner (the entire bottom row), further to the top right corner and then the top left corner (the entire top row). You can see that the route satisfies the task names. 2. If the $m>2$ shares $2$ and $n>2$, let's rotate the rectangle so that the $m=2 k(k \geq 2)$ has the number of rows. To construct a route that satisfies task nosacijums, we implement a rūtiṇu coordinate system in $(m;n)$ where the $m$ - row number, $n$ - column number and $(1;1)$ is the lower left corner. Here's a look at a route that connects the following boxes consecutively within one row or column: * $(i ; 2)$ with $(i ; n)$ * $(i ; n)$ with $(i+1 ; n)$ * $(i+1 ; n)$ with $(i+1 ; 2)$ * $(i+1 ; 2)$ with the $(i+2 ; 2)$ where the $i$ is sequentially equal to the $\{1;3;5;\ldots;m-1=2 k-1\}$. The engineered route will close in the $(m;2)$ box. We then take the route to the $(m;1)$ and $(1;1)$ the first column accordingly. You can see that the route satisfies the task condition. An example of the route is shown in Figure 16 with values $m=4$ and $n=5$.! [] (LV.AMO.2022B.11.5A.png) 3. If both $m$ and $n$ do not share the $2$ ($m;n \neq 1$), let us demonstrate that the required route cannot be established. Let's color a rectangular rūtiṇas in the shape of a chess galdiṇa and note that such a color has a characteristic: adjacent boxes have different colors. Let's say otherwise that the required route exists. As the route passes through all bitters with odd numbers, the transitions from one rūtiṇas to another occur a number of times. Consequently, the route will end in the same colour rūtiṇā as the starting rūtiṇa. But that can't be the case if that rūtiṇas is next door because they should be in different colors. Consequently, there is a contradiction and no such route exists. Since variable $m$ and $n$ can be changed in context for places, all possible cases are considered.


# <lo-sample/> LV.AMO.2022B.12.1

Can the number $2023^2$ be expressed as the sum of three integer cubes? 

<small>
* Concept: integer-numbers, cube-ALG, sum
* questionType: Provedisprove
* domain: NT
* LTopic: Ltcongruencemodulo
</small> 

## Solution 

Let's first find out who can be congruent integer cubes by moduḷa $9$: * if $n \equiv 0 \pmod 9$, then $n^{3} \equiv 0^{3} \equiv 0 \pmod 9$; * if $n \equiv 1 \pmod 9$, then $n^{3} \equiv 1^{3} \equiv 1 \pmod 9$; * if $n \equiv 2 \pmod 9$, then $n^{3} \equiv 2^{3} \equiv 8 \equiv-1 \pmod 9$; * if $n \equiv 3 \pmod 9$, then $n^{3} \equiv 3^{3} \equiv 27 \equiv 0 \pmod 9$; * if $n \equiv 4 \pmod 9$, then $n^{3} \equiv 4^{3} \equiv 64 \equiv 1 \pmod 9$; * if $n \equiv 5 \equiv-4 \pmod 9$, then $n^{3} \equiv(-4)^{3} \equiv-4^{3} \equiv-1 \pmod 9$; * if $n \equiv 6 \equiv-3 \pmod 9$, then $n^{3} \equiv(-3)^{3} \equiv 0 \pmod 9$; * if $n \equiv 7 \equiv-2 \pmod 9$, then $n^{3} \equiv(-2)^{3} \equiv 1 \pmod 9$; * If $n \equiv 8 \equiv-1 \pmod 9$, then $n^{3} \equiv(-1)^{3} \equiv-1 \pmod 9$. So integer cubes are congruents with 0 or $\pm 1$ after moduḷa 9. Let's look at what can be the sum of two integer cubes of a congruent by moduḷa 9. | $a^{3} \pmod 9$ | -1 | 0 | 1 | | |: ---: |: --- |: --- |: --- | | $b^{3} \pmod 9$ | -2 | -1 | 0 | | -1 | -1 | 0 | 1 | 0 | 0 | 1 | 2 | 1 | | | | | | | Now we're looking at what can be the sum of congruent three whole skaitḷu cubes by MODULA 9. | $a^{3}+b^{3} \pmod 9$ | -1 | 0 | 1 | 1 | -2 | 2 |: ---: |: --- |: --- |: --- |: --- |: --- | | | -1 | -2 | -1 | 0 -3 | 1 | 0 | -1 | 0 | 1 | -2 | 2 | 1 | 0 | 1 | 1 | 2 | -1 | 3 | We have obtained that the sum of three such skaițu after moduḷa 9 may yield any of the values $-3 ;-2 ;-1 ; 0 ; 1 ; 2 ; 3$ and none. Because the $2023^{2} \equiv 7^{2} \equiv 4 \equiv-5 \pmod 9$ does not appear between these values, the sum of three whole skaitḷu cubes cannot be $2023^{2}$.


# <lo-sample/> LV.AMO.2022B.12.2

For what real $p$ values is the sum of the root cubes in the equation $x^2 + x + p$ $(-16)$? 

<small>
* Concept: real-numbers, cube-ALG, equation
* questionType: Findall
* domain: ALG
* LTopic: The
</small> 


## Solution 

Will represent the root of the square equation with $x_{1}$ and $x_{2}$. After Viet's theorem, $x_{1} x_{2}=p$ and $x_{1}+x_{2}=-1$ are known. Using the sum square formula, we can calculate that the sum of the $$x_{1}^{2}+x_{2}^{2}=\left(x_{1}+x_{2}\right)^{2}-2 x_{1} x_{2}=1-2p.$$ Sakṇu cubes can be expressed as the $$x_{1}^{3}+x_{2}^{3}=\left(x_{1}+x_{2}\right)\left(x_{1}^{2}-x_{1} x_{2}+x_{2}^{2}\right)=-1(1-2 p-p) = 3p-1 = -16.$$ So $3p=-15$ and $p=-5$.

# <lo-sample/> LV.AMO.2022B.12.3

In the triangle, the length of the height drawn $ABC$ from the $A$ of the summit is $1$, the length of the median drawn from the $C$ of the summit is also $1$ and the length of the $B$ of the height from the summit is $\sqrt{3}$. What can be the area of this triangle? 

<small>
* Concepted: triangle, Median, altitude, area
* questionType: Findall
* domain: Geom
* LTopic: The lttriangles
</small> 

## Solution 

Will mark the midpoint of the $AB$ with a $M$ and remove perpendiculars in the $MP$ and $MT$ against the edges in the $AC$ and $BC$, respectively. The foundations of height drawn from the peaks in $A$ and $B$ shall be marked with $Q$ and $N$ respectively. Because the $MT \| AQ$, the $MT \perp BC$ and the $AQ \perp BC$, the $M T$ is the centerline of the triangle $A Q B$, hence the $M T=\frac{1}{2} A Q=\frac{1}{2}$. Similarly, we get that $M P=\frac{1}{2} B N=\frac{\sqrt{3}}{2}$. We notice that the taisnleṇça in the triangle $MTC$'t work, that the $\sin \Varangle MCT=\frac{M T}{M C}=\frac{1}{2}$, hence the $\Varangle M C T=30^{\circ}$. Similarly, we get that the taisnleṇka in the triangle $MPC$'t work, that the $\sin \Varangle M C P=\frac{M P}{M C}=\frac{\sqrt{3}}{2}$, hence the $\Varangle M C P=60^{\circ}$. Here's a look at possible $\Varangle MCB$ values: * If the $T$ is on the $BC$, then $\Varangle M C B=30^{\circ}$; * If the $T$ is on the $BC$ extension, $\Varangle M C B=150^{\circ}$. As $\Varangle ACB=\Varangle MCA+\Varangle MCB$, it is not possible to $\Varangle MCB=150^{\circ}$ because the $\Varangle A C B$ will be equal to or greater than the $180^{\circ}$ at any $\Varangle M C B$ value. It follows that $\Varangle MCB=30^{\circ}$. Here's a similar look at possible $\Varangle MCA$ and $\Varangle ACB$ values: * If the $P$ is in the $AC$, then $\Varangle M C A=60^{\circ}$ and $\Varangle A C B=90^{\circ}$ * if the $P$ is on the $AC$ extension, then $\Varangle MCA = 120^{\circ}$ and $\Varangle A C B=150^{\circ}$. If $\Varangle ACB=90^{\circ}$ (see Figure 17), the heights from the peaks $A$ and $B$ coincide with the catheters $AC$ and $BC$, so in the $$S_{ABC}=\frac{AC \cdot BC}{2}=\frac{1 \cdot \sqrt{3}}{2}=\frac{\sqrt{3}}{2}.$$ If $\Varangle ACB=150^{\circ}$ (see Figure 18), we look at the right-angle triangle in the $AQC$ in which you $\Varangle A C Q=30^{\circ}$, hence the $\frac{A Q}{A C}=\sin \Varangle A C Q=\frac{1}{2}$. It follows that $A C=2 \cdot A Q=2$ and $$S_{ABC}=\frac{AC \cdot BN}{2}=2 \cdot \frac{\sqrt{3}}{2}=\sqrt{3}.$$ the area of the triangle may therefore be $\frac{\sqrt{3}}{2}$ or $\sqrt{3}$.! [] (LV.AMO.2022B.12.3A.png)


# <lo-sample/> LV.AMO.2022B.12.4

Resolve equation $3 \sin x + 4 \cos x = 6$ in real numbers. 

<small>
* Concept: equation, real-numbers, sine, cosine
* questionType: Findall
* domain: ALG
* LTopic: The resolution
</small> 

## Solution 

releases both sides of the equation with the $5$: $$\frac{3}{5} \sin x+\frac{4}{5} \cos x=\frac{6}{5}.$$, let's have a narrow leṇki $\alpha$ like this that $\sin \alpha=\frac{4}{5}$. In this case, we can rewrite the $\cos \alpha=\sqrt{1-\sin ^{2} \alpha}=\sqrt{1-\left(\frac{4}{5}\right)^{2}}=\frac{3}{5}$ and equation as 

$$\begin{gathered}
\sin x \cos \alpha+\cos x \sin \alpha=\frac{6}{5} \\
\sin (x+\alpha)=\frac{6}{5}
\end{gathered}$$ 

because the sinus values do not exceed 1, then there are no solves for this equation. So there's no solution for the given equation either. the 

## Solution 

By using double-leṇka formulas and $\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}=1$, we get that by dividing the two sides of the equation in the $$\operatorname{ctg}^{2} \frac{x}{2}-3 \operatorname{ctg} \frac{x}{2}+5=0$$ by $2 \sin ^{2} \frac{x}{2} \neq 0$, we get a square equation for the $t^{2}-3 t+5=0$ whose discriminant $D=(-3)^{2}-4 \cdot 1 \cdot 5=-11<0$, so there's no sakṇu for the square equation, so there's no solution for the equation given. the 


## Solution 

from both sides of the equation atṇemot the $4 \cos x$, we get you to $3 \sin x=6-4 \cos x$. By pushing both sides of the equation into a square, we get that by using a $\sin ^{2} x=1-\cos ^{2} x$ in the $$\begin{gathered}
9\left(1-\cos ^{2} x\right)=36-48 \cos x+16 \cos ^{2} x \\
9-9 \cos ^{2} x=36-48 \cos x+16 \cos ^{2} x \\
25 \cos ^{2} x-48 \cos x+27=0
\end{gathered}$$, we get a $\cos x=t$ of square equations with a discriminant $D=(-48)^{2}-4 \cdot 25 \cdot 27=48 \cdot 48-50 \cdot 54<0$, so that the square equation has no sakṇu, so that the equation has no roots. the 

## Solution 

will prove that the inequality in the $a \sin x+b \cos x \leq \sqrt{a^{2}+b^{2}}$ runs. Let's climb both sides of the equation into a square and use that $\sin ^{2} x+\cos ^{2} x=1$. We get that $$\begin{gathered}
(a \sin x+b \cos x)^{2} \leq\left(a^{2}+b^{2}\right)\left(\sin ^{2} x+\cos ^{2} x\right) \\
a^{2} \sin ^{2} x+2 a b \sin x \cos x+b \cos ^{2} x \leq a^{2} \sin ^{2} x+a^{2} \cos ^{2} x+b^{2} \sin ^{2} x+b^{2} \cos ^{2} x \\
0 \leq a^{2} \cos ^{2} x-2 a b \sin x \cos x+b^{2} \sin ^{2} x \\
(a \cos x-b \sin x)^{2} \geq 0
\end{gathered}$$ because inequality is true to any $a, b$ and $x$ value, then the initial inequality in $a \sin x+b \cos x \leq \sqrt{a^{2}+b^{2}}$ is true. It follows that the $3 \sin x+4 \cos x \leq \sqrt{3^{2}+4^{2}}=5$, and therefore the equation given, is sakṇu.


# <lo-sample/> LV.AMO.2022B.12.5

The table $n \times n$ is checked. Ilmari and Kim play such a game. They type a number $1$ or $-1$ in a box that is still empty. Ilmari starts the game. If a row or column is filled in after a player's move, the product of the numbers in the row or column is calculated. If it equals $-1$ then the player who made the last move gets a $1$ point (If a player completes both a row and a column at the same time with his move, and the product of each number is $-1$, then he scores twice). The game ends when the table is fully populated. The player who gets the most points wins. Which player has a winning strategy if
**(A)** $n = 2021$; **(B)** $n = 2022$? 

<small>
* Concept: game, table, row, column, product, winning-strategy
* questionType: Provedisprove
* domain: Comb
* LTopic: Ltgames
</small> 

## Solution 

**(A)** 
If $n=2021$, Ilmari wins. On his first move, he records a number in the centre box for $-1$, but plays symmetrically in the far walks relative to central Ruthin and Kim's move. In that case, if Kim scores a point after his move, Ilmari will also symmetrically score. So Ilmari will score just as much as Kim. In addition, we can note that Ilmari will be the one who will fill the middle row and middle column on the basis of symmetry. Since all skaitḷi will be symmetrical in them, izṇemot the fact that a $-1$ has been recorded in between, we can conclude that the product will be $-1$ and Ilmari will score extra $2$ points that will allow him to win. 

**(B)** 
If $n=2022$, Kim wins. He ̌ makes each of his moves symmetrically against the vertical axis of symmetry of the table and Ilmari's, izṇemot the moments when the viṇam has to make a move in a row with exactly one empty box remaining. At those moments, he chooses a number so that the product of that line is $-1$. The son of symmetry, Kim will always be the one to fill a line, and this stratēǵija will guarantee a viṇam 2,022 points per row. In addition, we can note that every time the llmar fills a column, Kim will fill the symmetric column in the next move. As a result, Ilmari will fill in exactly the $1011$ columns that give the viṇam no more than $1011$ points. So Kim will win.
