# <lo-exercise/> BBK2012.P1.E4.2

Ar Eiklīda algoritmu aprēķināt:  
**(A)** $(33,18)$,  
**(B)** $(1260,406)$,  
**(C)** $(56,39)$,  
**(D)** $(312,138)$.

## Atrisinājums

**(A)**

$$\begin{aligned}
33 & = 18 \times 1+15\\
18 & = 15 \times 1+3 \\
15 & = 3 \times 5 \\
\end{aligned}

Tātad, $\gcd(33,18)=3$. Eiklīda algoritmu (kas no lielākā skaitļa arvien 
patur atlikumu, kas rodas, dalot ar mazāko skaitli) var pierakstīt arī tā:

$$\gcd(33,18) = \gcd(18,15) = \gcd(15,3) = 3.$$

**(B)**

$$\gcd(1260, 406) = \gcd(406, 42) = \gcd(42, 28) = \gcd(28,14) = 14.$$ 


**(C)**

$$\gcd(56, 39) = \gcd(39, 17) = \gcd(17, 5) = \gcd(5,2) = \gcd(2,1) = 1.$$ 


**(D)**

$$\gcd(312, 138) = \gcd(128, 36) = \gcd(36,30) = \gcd(30, 6) = 6.$$




