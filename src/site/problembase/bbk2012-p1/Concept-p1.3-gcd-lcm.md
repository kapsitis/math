#  LKD un MKD 

Pievērsiet īpašu  uzmanību LKD un MKD definīcijām. Tās atšķiras no  
no skolas programmas. Šajās definīcijās neizmanto attiecības  
"lielāks" un "mazāks", tikai dalāmības attiecību. 
Šīs definīcijas var izmantot, lai ieviestu LKD un MKD jēdzienus arī 
situācijās, kad objekti nav salīdzināmi. 
(Piemēram, var tādā pašā veidā definēt arī LKD vai MKD diviem polinomiem kaut 
arī polinomi nav salīdzināmi tāpat kā skaitļi.)

**Definīcija:** Veselu skaitli $d$ sauc par veselu skaitļu $a$ un $b$ 
*lielāko kopīgo dalītāju* un apzīmē $d = \operatorname{gcd}(a, b)$, 
ja izpildās sekojošas īpašības:
	
1. $d \mid a$ un $d \mid b$;
2. ja $t$ ir tāds vesels skaitlis, ka $t \mid a$ un $t \mid b$, tad $t \mid d$.


**Definīcija:** 
Veselu skaitli $m$ sauc par veselu skaitļu $a$ un $b$ mazāko kopīgo dalāmo 
un apzīmē $\operatorname{lcm}(a, b)$, ja tam izpildās sekojošas īpašības:

1. $a \mid m$ un $b \mid m$;
2. ja $s$ ir tāds vesels skaitlis, ka $a \mid s$ un $b \mid s$, tad $m \mid s$.

Izmantojot definīcijas, var pierādīt, ka skaitļu LKD un MKD ir noteikti viennozīmīgi, 
ja neņem vērā skaitļu zīmi. Taču LKD un MKD eksistence, ievērojot doto definīciju, 
ir pietiekami sarežģīts apgalvojums. Eksistences pierādījums ir saistīts ar 
Eiklīda algoritmu – metodi, kas aprēķina skaitļu 
(un ne tikai skaitļu, bet, piemēram, arī polinomu) lielāko kopīgo dalītāju.

**LKD īpašības:**

1. $\operatorname{gcd}(a,b) = \operatorname{gcd}(b,a)$,
2. $\operatorname{gcd}(a,b) = \operatorname{gcd}(a, b+ka)$,
3. $\operatorname{gcd}(a,b,c) = \operatorname{gcd}(\operatorname{gcd}(a,b),c)$,
4. $\operatorname{gcd}(ta,tb) = t \cdot \operatorname{gcd}(a,b)$,
5. $\operatorname{gcd}(a,b) \cdot \operatorname{lcm}(a,b) = a \cdot b$.
6. Ja $\operatorname{gcd}(x,y) = 1$, $x \mid a$ un $y \mid b$, tad  $xy \mid a$,
7. Ja $\operatorname{gcd}(a,x) = 1$ un $x \mid ab$, tad $x \mid b$.