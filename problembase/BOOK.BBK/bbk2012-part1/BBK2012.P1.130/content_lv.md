# <lo-sample/> BBK2012.P1.130

Pierādīt, ka vienādība
$$\sum_{k=1}^n \left\lfloor \frac{n}{k} \right\rfloor = 
2 + \sum_{k=1}^{n-1} \left\lfloor \frac{n-1}{k} \right\rfloor,\;
n \in \mathbb{N}, n\geq 2$$
izpildās tad un tikai tad, kad $n$ ir pirmskaitlis.





## Atrisinājums

Ievērosim, ka  
$$\sum_{k=1}^{n}\left[\frac{n}{k}\right]=\left[\frac{n}{1}\right]+\sum_{k=2}^{n-1}\left[\frac{n}{k}\right]+\left[\frac{n}{n}\right]=n+1+\sum_{k=2}^{n-1}\left[\frac{n}{k}\right]$$  
bet  
$$\sum_{k=1}^{n-1}\left[\frac{n-1}{k}\right]=\left[\frac{n-1}{1}\right]+\sum_{k=2}^{n-1}\left[\frac{n-1}{k}\right]=n-1+\sum_{k=2}^{n-1}\left[\frac{n-1}{k}\right]$$   
un pierādāmā vienādība ir ekvivalenta ar sekojošu vienādību:

$$\sum_{k=2}^{n-1}\left(\left[\frac{n}{k}\right]-\left[\frac{n-1}{k}\right]\right)=0$$

Tā kā  
$$\left(\left[\frac{n}{k}\right]-\left[\frac{n-1}{k}\right]\right)=\left\{\begin{array}{c}
0, \text { ja } k \text { nedala } n \\
1, \text { ja } k \text { dala } n,
\end{array}\right.$$  
tad dotā vienādība izpildās tad un tikai tad, kad $n$ nedalās 
ne ar vienu no skaitliem $2,3, \ldots, n-1$; t.i., kad $n$ ir pirmskaitlis.



