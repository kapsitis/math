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