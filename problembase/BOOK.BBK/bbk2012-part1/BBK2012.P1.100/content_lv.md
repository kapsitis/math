# <lo-sample/> BBK2012.P1.100

Sešciparu skaitļa $N$ pirmais cipars ir $7$, piektais - $2$, 
bet pēdējais - nepāra skaitlis. Zināms, ka dalot $N$ ar skaiţ̧iem $3$, $4$, $7$, $9$, $11$ un $13$, 
rezultātā iegūstam vienādus atlikumus. Atrodiet skaitli $N$.



## Atrisinājums

Ar $r$ apzīmēsim atlikumu, ko iegūstam, dalot skaitli $N$ ar $3,4,7,9,11,13$. 
Protams, $0 \leq r<3$, un tā kā $N$ ir nepāra skaitlis, tad $r=1$. 
Tātad $N-1$ dalās ar visiem skaitliem $3$, $4$, $7$, $9$, $11$, $13$ un arī ar to mazāko 
kopīgo dalāmo 36036. Iegūstam vienādību

$$\overline{7 \ast \ast \ast 2 \ast} = x \cdot 36036+1.$$

No nevienādībām $700000<x \cdot 36036+1<800000$ seko， ka $20 \leq x \leq 22$. Pārbaudot šīs 
vērtības redzam, ka der tikai skaitlis $x=20$, un meklētais skaitlis $N$ ir $720721$.




