# <lo-sample/> BBK2012.P1.86

Ar $p_{n}$ apzīmēsim $n$-to pēc kārtas pirmskaitli. Pierādiet, ka visiem naturāliem 
$n$ izpildās nevienādība $p_{n}<2^{2^{n}}$.



## Atrisinājums

Apgalvojumu pierādīsim ar indukciju.

Ja $n=1$, tad $p_{1}=2<2^{2^{1}}$.

Pien̦emsim, ka apgalvojums izpildās, ja $n \leq s$, un pierādīsim, ka tas izpildās, ja $n=s+1$. 
Aplūkosim skaitļa $a=p_{1} p_{2} \cdots p_{s}+1$ pirmreizinātāju $p$. 
Skaidrs, ka $p \neq p_{i}$. Tātad $p \quad p_{s+1}$. No šejienes

$$\begin{aligned}
& p_{s+1} \leq p \leq a \leq 2^{2^{1}} \cdot 2^{2^{2}} \cdot \ldots \cdot 2^{2^{s}}+1= \\
& 2^{2^{1}+2^{2}+\cdots+2^{s}}+1=2^{2^{s+1}-2}+1<2^{2^{s+1}}
\end{aligned}$$

Apgalvojums pierādīts.





