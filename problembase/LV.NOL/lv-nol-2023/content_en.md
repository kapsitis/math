# <lo-sample/> LV.NOL.2023.5.1

Write a number in each empty cell (see Figure 1) so that the sum of the 
numbers in any three consecutive cells is the same, and the total sum 
of all the numbers written in the cells (including the two given numbers) 
is $223$. It is sufficient to show one example of how to achieve this.

![](LV.NOL.2023.5.1.png){ width=300px }


## Solution

The required solution can be achieved as shown in Figure 2, where the sum 
of every three consecutive numbers is $51$.

![](LV.NOL.2023.5.1A.png){ width=300px }

Let's explain how these numbers can be found. Consider four consecutive 
cells that contain the numbers $x;a;b$ and $y$ (see Figure 3).

![](LV.NOL.2023.5.1B.png){ width=150px }

Since the sum of the numbers in any three consecutive cells is the same, 
we have $x+a+b=a+b+y$, which implies $x=y$, and thus the numbers $x$ and 
$y$ must be the same. Therefore, the numbers written in the cells repeat 
with a period of $3$ (see Figure 4), where $n$ is an unknown number 
(the same everywhere).

![](LV.NOL.2023.5.1C.png){ width=300px }

If we remove the very last number $19$, we find that in four blocks of 
three cells $(19;20;n)$, the total sum of the numbers is $223-19=204$. 
Hence, the sum of the numbers in one such block $(19;20;n)$ is $204:4=51$. 
Therefore, the number $n$ must be $51-19-20=12$.



# <lo-sample/> LV.NOL.2023.5.2

In the forest, gnomes have built eight houses and created several paths 
between them. Each path connects two houses, and paths can intersect. 
Is it possible that the houses have the following number 
of paths coming out of them:  
**(A)** $2, 2, 2, 4, 4, 4, 4, 4$ paths respectively;  
**(B)** $1, 2, 2, 2, 2, 3, 4, 5$ paths respectively?


## Solution

**(A)** Yes, for example, see Fig. 5, where dots represent houses, lines 
represent paths, and the number of lines emanating from each point is 
noted next to each point.

**(B)** Let us show that this is not possible. Since each path has two 
endpoints, the total number of path ends must be an even number. 
From the given data, we get that there are $1+2+2+2+2+3+4+5=21$ 
endpoints. Since $21$ is an odd number, the required configuration 
is not possible.

![](LV.NOL.2023.5.2A.png){ width=200px }


# <lo-sample/> LV.NOL.2023.5.3

Show how the figure in Fig.2 (a $6 \times 8$ rectangle, 
from which a $3 \times 4$ rectangle has been removed), 
by cutting along the grid lines, can be subdivided into three identical shapes! 
The shapes are considered identical if they can be placed one on top of 
the other so that they coincide (the shapes may be rotated and flipped).

![](LV.NOL.2023.5.3.png){ width=200px }

<small>

* questionType:FindExample
* domain:Geom

</small>

## Solution

See Fig. 7.

![](LV.NOL.2023.5.3A.png){ width=200px }



# <lo-sample/> LV.NOL.2023.5.4

Show how the number $174$ can be written as the sum of $3$ distinct natural numbers such 
that the sum of any two of these numbers is divisible by the third number!


<small>

* questionType:FindExample
* domain:NT

</small>


## Solution

This can be done as follows: $174=29+58+87$. Let's verify that the sum of any two of 
these numbers is divisible by the third number:

$$\begin{aligned}
& \circ \quad(29+58): 87=87: 87=1 \\
& \circ \quad(29+87): 58=116: 58=2 \\
& \circ \quad(58+87): 29=145: 29=5
\end{aligned}$$


# <lo-sample/> LV.NOL.2023.5.5

If a red coin is inserted into the machine, it gives out $5$ blue coins, 
but if a blue coin is inserted into the machine, it gives out $3$ red coins. Is it 
possible, by repeatedly using the machine, to obtain equal numbers 
of red and blue coins if initially one red coin is given?

<small>

* questionType:ProveDisprove
* domain:Comb
* subdomain:DOM_FixedInvariant

</small>


## Solution

No, this is not possible. Observe that initially there is one coin, and with each 
operation the number of coins increases by $4$ coins (if you insert $1$ red coin, 
it outputs $5$ blue coins) or by $2$ coins (if you insert $1$ blue coin, it outputs 
$3$ red coins), so the total number of coins will always be an odd number. 
But if the blue and red coins were in equal numbers, then the total number 
of coins would be even. Therefore, this is impossible.




# <lo-sample/> LV.NOL.2023.6.1

Find one set of natural numbers to substitute for $x, y$, and $z$ so that the equality

$$2+\frac{1}{x+\frac{1}{y+\frac{1}{z}}}=\frac{37}{13}$$

holds!

<small>

* questionType:FindExample
* domain:Alg

</small>

## Solution

The values $x=1$; $y=5$ and $z=2$ work. With these values the equality holds, since

$$2+\frac{1}{1+\frac{1}{5+\frac{1}{2}}}=2+\frac{1}{1+\frac{2}{11}}=2+\frac{1}{1 \frac{2}{11}}=2+\frac{11}{13}=2 \frac{11}{13}=\frac{37}{13}$$

*Note.* We will show how one can obtain the required values. Observe that $\frac{37}{13}=2 \frac{11}{13}$, 
hence $\frac{1}{x+\frac{1}{y+\frac{1}{Z}}}=\frac{11}{13}$, from which we get that 
$x+\frac{1}{y+\frac{1}{z}}=\frac{13}{11}$. Since $\frac{13}{11}=1 \frac{2}{11}$, then $x=1$ 
and $\frac{1}{y+\frac{1}{z}}=\frac{2}{11}$, from which we obtain that $y+\frac{1}{z}=\frac{11}{2}$. 
Noting that $\frac{11}{2} = 5\frac{1}{2}$, we obtain $y=5$ and $z=2$.




# <lo-sample/> LV.NOL.2023.6.2

The dwarfs in the forest have built ten houses and created several 
paths between them. Each path connects two houses, and the paths may cross. 
Is it possible that the numbers of paths leaving the houses are respectively:
**(A)** $2, 2, 2, 2, 2, 3, 3, 3, 3, 7$ paths;   
**(B)** $2, 2, 2, 2, 4, 4, 4, 4, 4, 4$ paths?

<small>

* questionType:ProveDisprove
* domain:Comb
* subdomain:DOM_FixedInvariant

</small>

## Solution

**(A)** We will prove that this is not possible. Since each path has two ends, 
the total number of path ends must be even, but from the given we get that 
$2+2+2+2+2+3+3+3+3+7=29$ path ends. Since $29$ is an odd number, 
the required configuration is impossible.

**(B)** Yes, for example, see Fig. 8, where the houses are represented by points, 
the paths by lines, and next to each point the number of lines leaving it is indicated.

![](LV.NOL.2023.6.2A.png){ width=200px }




# <lo-sample/> LV.NOL.2023.6.3

Show how, by cutting along the grid lines, the figure given in Fig. 1 can be cut into 
$4$ identical shapes! The shapes are identical if they can be placed one on top of 
the other so that they coincide (the shapes may be rotated and flipped).

![](LV.NOL.2023.6.3.png){ width=200px }


<small>

* questionType:FindExample
* domain:Geom

</small>

## Solution

See, for example, Fig. 10 or Fig. 11.

![](LV.NOL.2023.6.3A.png){ width=250px }





# <lo-sample/> LV.NOL.2023.6.4

Can the number: **(A)** $72$, **(B)** $73$ be expressed as the sum of three distinct 
natural numbers such that the sum of any two of these numbers is divisible by the remaining number?

<small>

* questionType:ProveDisprove,ProveDisprove
* domain:NT

</small>

## Solution

**(A)** Yes, for example: $72=12+24+36$. Let us check that the sum of any two of these 
numbers is divisible by the third number:

$$\begin{aligned}
& \circ \quad(12+24): 36=36: 36=1 \\
& \circ \quad(12+36): 24=48: 24=2 \\
& \circ \quad(24+36): 12=60: 12=5
\end{aligned}$$

**(B)** We show that this is not possible. 
By contradiction, assume that $a+b+n=73$ and $a+b$ is divisible by $n$. 

If $a+b$ is divisible by some number $n$, then the sum of all three numbers $a+b+n$ is 
also divisible by $n$. Therefore, $73=a+b+n$, must be 
divisible by $a$, $b$, and $n$. But the number $73$ is prime, divisible 
only by $1$ and $73$. Hence three distinct numbers can only take two 
values $1$ or $73$, which is impossible.



# <lo-sample/> LV.NOL.2023.6.5


We start with the number $17$. We can repeatedly apply any of the following operations:

1. Multiply the current number by $2$.
2. Delete any of the digits $0$, $3$, $6$, or $9$ from the number.

Is it possible to obtain **(A)** the number 1? **(B)** the number 15?


<small>

* questionType:ProveDisprove,ProveDisprove
* domain:NT
* subdomain:DOM_FixedInvariant

</small>


## Solution

**(A)** Yes, for example, as follows:

$$17 \rightarrow 34 \rightarrow 4 \rightarrow 8 \rightarrow 16 \rightarrow 1$$

**(B)** No, it is not possible. The initial number $17$ is not divisible by $3$. 
If a number is not divisible by $3$, then after performing the allowed operations 
the resulting number will not be divisible by $3$:

- if a number not divisible by $3$ is multiplied by $2$, the product is also not divisible by $3$;
- if from a number not divisible by $3$ one deletes a digit $0,3,6,9$, 
  then the resulting number is also not divisible by $3$ (the digit sum of the initial 
  number is not divisible by $3$ (the divisibility rule for $3$); deleting $0,3,6,9$ 
  yields a digit sum that is still not divisible by $3$).

Therefore, even after several operations, the resulting number will not be divisible by $3$. 
This means that the number $15$ cannot be obtained, since it is divisible by $3$.

