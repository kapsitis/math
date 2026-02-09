# <lo-sample/> BBK2012.P1.131

Atrodiet visus tādus naturālus skaitļus $k$, kuriem virkne $k+1,k+2,\ldots,k+100$
satur maksimālo iespējamo pirmskaitļu skaitu.




## Atrisinājums

Eksistē tikai viens šāds skaitlis $k=1$.

Šajā gadījumā virkne $k+1, k+2, \ldots, k+100$ satur $26$ pirmskaitļus.
Ja $k \in\{2,3,4\}$, tad virknē ir $25$ pirmskaitļi. 
Ja $k \in\{5,6\}$, tad virknē $24$ pirmskaitļi. Tālāk aplūkosim $k \geq 7$. Tādā gadījumā jebkurš no skaițliem, 
kurš dalās ar $2$, $3$, $5$ vai $7$, ir salikts skaitlis. Pakāpeniski pierādām sekojošu apgalvojumus:

a. Tieši $50$ skaitļi virknē dalās ar $2$.
b. Virknē ir ne mazāk kā $16$ skaitli, kas dalās ar $3$, bet nedalās ar $2$.
c. Virknē ir ne mazāk kā $6$ skaitli, kas dalās ar $5$, bet nedalās ar $2$ vai $3$.
d. Virknē ir ne mazāk kā $3$ skaiți, kas dalās ar $7$, bet nedalās ar $2$, $3$ vai $5$.

Tātad virknē ir ne vairāk kā $100-50-16-6-3=25$ pirmskaitļi.




