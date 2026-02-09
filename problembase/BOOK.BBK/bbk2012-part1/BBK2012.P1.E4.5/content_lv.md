# <lo-exercise/> BBK2012.P1.E4.5

Ar Eiklīda algoritmu aprēķināt $d=(a,b)$, un izteikt skaitli $d$ formā $ua + vb$.  
**(A)** $(15,9)$,  
**(B)** $(187,68)$,  
**(C)** $(200,325)$,  
**(D)** $(200,40)$.


## Atrisinājums

**(A)**

$$\begin{aligned}
15 & = 9 \times 1+6 \\ 
9 & = 6 \times 1+3 \\
6 & = 3 \times 2 \\
(15,9) & = 3.\\
\end{aligned}$$

Pārrakstām šādā formā:

$$\begin{aligned}
a_{1} & = a_{2} \times 1+a_{3} \\
a_{2} & = a_{3} \times 1+a_{4} \\
a_{3} & = a_{4} \times 2 \\
\end{aligned}$$

$\left(a_{1}, a_{2}\right) = a_{4} = a_{2}-a_{3} = a_{2}-\left(a_{1}-a_{2}\right) = -a_{1}+2 a_{2}$.
Tātad $(15,9)=3=(-1) \times 15+2 \times 9$;

**(B)** $(187,68)=17=(-1) \times 187+3 \times 68$;  
**(C)** $(200,325)=25=5 \times 200-3 \times 325$;  
**(D)** $(200,40)=40=0 \times 200+1 \times 40$.






