# <lo-sample/> BBK2012.P1.132

Ar $d(i)$ apzīmēsim skaitļa $i$ naturālo dalītāju skaitu. 
Pierādiet, ka jebkuram naturālam skaitlim $n$ izpildās vienādība 
$$d(1)+d(2)+\ldots+d(n)= \left\lfloor \frac{n}{1} \right\rfloor + 
\left\lfloor \frac{n}{2} \right\rfloor + \ldots + 
\left\lfloor \frac{n}{n} \right\rfloor.$$




## Atrisinājums

Aplūkosim funkciju, kas definēta visiem naturāliem skaitlu pāriem $(i, j)$ :

$$
f(i, j)=\left\{\begin{array}{l}
0, \text { ja } i \text { nedala } j \\
1, \text { ja } i \text { dala } j
\end{array}\right.
$$

Aprēķināsim summu $\sum_{i=1}^{n} \sum_{j=1}^{n} f(i, j)$ divos dažādos veidos:

$$\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n} f(i, j)=\sum_{i=1}^{n}\left[\frac{n}{i}\right] \\
& \sum_{i=1}^{n} \sum_{j=1}^{n} f(i, j)=\sum_{j=1}^{n} \sum_{i=1}^{n} f(i, j)=\sum_{j=1}^{n} d(j)
\end{aligned}$$

No šejienes seko pierādāmā vienādība.






