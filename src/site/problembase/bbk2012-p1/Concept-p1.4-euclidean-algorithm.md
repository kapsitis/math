# Eiklīda algoritms

Doti naturāli skaitļi $a_0$ un $a_1$; pieņemsim, ka $a_0 > a_1$. 
Izdalīsim skaitli $a_0$ ar $a_1$ ar atlikumu: 
$a_0 = a_1q_1 + a_2$, $0 \leq a_2 < a_1$.  
Pēc tam izdalīsim  $a_1$ ar $a_2$ ar atlikumu, atlikumu apzīmēsim ar $a_3$. 
Šo procesu turpināsim, kamēr atlikumā iegūsim $0$. 
Process beigsies, jo virkne $(a_n)$ ir stingri dilstoša nenegatīvu skaitļu virkne. 
Rezultātā  iegūsim šādu sistēmu:  

$$\left\{ \begin{array}{ll}
a_0 = a_1q_1 + a_2, & a_2 < a_1,\\
a_1 = a_2q_2 + a_3, & a_3 < a_2,\\
\ldots & \\
a_{k-2} = a_{k-1}q_{k-1} + a_k, & a_k < a_{k-1},\\
a_{k-1} = a_kq_k. & \\
\end{array} \right\}$$
	
**Teorēma:** Pēdējais nenulles atlikums, ko iegūst, 
realizējot Eiklīda algoritmu ar skaitļiem $a_0$ un $a_1$, 
ir skaitļu $a_0$ un $a_1$ LKD. 
Turklāt, eksistē tādi veseli skaitļi $t$ un $s$, ka $a_k = ta_0 + sa_1$.

