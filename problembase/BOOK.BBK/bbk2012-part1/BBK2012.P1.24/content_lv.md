# <lo-sample/> BBK2012.P1.24

Pierādiet, ka skaitlis $\overline{a_1a_2\cdots{}a_{3m}}$ dalās ar $7$
($11$ vai $13$) tad un tikai tad, kad 
skaitlis 

$$\overline{a_1a_2a_3} - \overline{a_4a_5a_6} + \cdots + 
(-1)^{m-1}\overline{a_{3m-2}a_{3m-1}a_{3m}}$$

dalās ar $7$ ($11$ vai $13$).



## Atrisinājums

Tā kā $1000^k \equiv (-1)^k \pmod {1001}$, tad 
$$\overline{a_1a_2a_3\cdots{}a_{3m-2}a_{3m-1}a_{3m}} \equiv \overline{a_1a_2a_3} \cdot 10^{3m-3} + \cdots + \overline{a_{3m-2}a_{3m-1}a_{3m}} \equiv$$
$$\equiv \overline{a_1a_2a_3} \cdot (-1)^{m-1} + \overline{a_4a_5a_6} \cdot (-1)^{m-2} + \cdots + \overline{a_{3m-2}a_{3m-1}a_{3m}} \equiv$$
$$\equiv (-1)^{m-1}\left( \overline{a_1a_2a_3} - \overline{a_4a_5a_6}  + \cdots + (-1)^{m-1}\overline{a_{3m-2}a_{3m-1}a_{3m}}  \right) \pmod {1001}.$$


