# <lo-sample/> BBK2012.P1.129
	
Dots naturāls skaitlis $n$. Aprēķināt summu
$$\left\lfloor \frac{n+1}{2} \right\rfloor +
\left\lfloor \frac{n+2}{2^2} \right\rfloor + \ldots + 
\left\lfloor \frac{n+2^k}{2^{k+1}} \right\rfloor + \ldots.$$




## Atrisinājums

Apzīmēsim doto summu ar $S_{n}$. Tad

$$S_{n+1}-S_{n}=\sum_{k=0}^{\infty}\left(\left[\frac{n+2^{k}+1}{2^{k+1}}\right]-\left[\frac{n+2^{k}}{2^{k+1}}\right]\right)$$

Aprakstīsim šīs starpības

$$\left[\frac{n+2^{k}+1}{2^{k+1}}\right]-\left[\frac{n+2^{k}}{2^{k+1}}\right]=\left\{\begin{array}{c}
0, \text { ja } 2^{k+1} \text { nedala }\left(n+2^{k}+1\right) \\
1, \text { ja } 2^{k+1} \text { dala }\left(n+2^{k}+1\right) .
\end{array}\right.$$

Pien̦emsim, ka $n+1=2^{m} \cdot A$, un $A$ nedalās ar $2$. 
Skaidrs, ka $n+2^{k}+1=2^{m} \cdot A+2^{k}$ dalās ar $2^{k+1}$ tad un tikai tad, 
kad $m=k$. Tātad aplūkotā starpība nav 0 tikai vienai skaiț̣a $k$ vērtībai. 
Rezultātā iegūstam vienādību $S_{n+1}-S_{n}=1$, kas izpildās visiem $n$. 
Tā kā $S_{1}=1$, tad $S_{n}=n$.




