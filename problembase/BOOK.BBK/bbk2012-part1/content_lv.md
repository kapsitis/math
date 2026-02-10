# 1.Daļa: SKAITĻU DALĀMĪBA

## Dalītāji un dalāmība

Viens no galvenajiem skaitļu teorijas jēdzieniem ir skaitļu dalāmība.

**Definīcija:**
Saka, ka vesels skaitlis $m$ dalās ar veselu skaitli $n$, jeb $n$ ir $m$ dalītājs, 
ja eksistē tāds vesels skaitlis $k$, kuram $m = n \cdot k$. 
To pieraksta šādi $m \mathrel{\vdots} n$ jeb $n \mid m$.

**Dalāmības īpašības:**	

**D1.** Ja $a \mid b$ un $a \mid c$, tad $a \mid b+c$ un $a \mid b-c$;  
**D2.** Ja $a \mid b$, tad $a \mid b \cdot k$;  
**D3.** Ja $a \mid b_1$, $a\mid b_2$, $\ldots$, $a \mid b_n$, 
tad $a \mid \left(b_1k_1 + b_2k_2 + \cdots + b_nk_n \right)$;  
**D4.** Ja $a \mid b$ un $b \mid c$, tad $a \mid c$;  
**D5.** Ja $a \mid x$ un $b \mid y$, tad $ab \mid xy$;  
**D6.** Ja $a,b \in \mathbb{N}$, $a \mid b$ un $b \mid a$, tad $a =b$.


## Dalīšana ar atlikumu

**Definīcija:**
Izdalīt veselu skaitli $m$ ar naturālu skaitli $n$ ar atlikumu 
nozīmē uzrakstīt skaitli formā $m=nq+r$, turklāt $q$ un $r$ 
ir veseli skaitļi, un $0 \leq r \leq n-1$.

Praktiski dalīšanu ar atlikumu izpilda kā parastu dalīšanu, 
tikai šo procesu pabeidz, tiklīdz atlikums kļūst mazāks par dalītāju.

Mēs parasti neuzdodam sev jautājumu, vai vienmēr var izdalīt ar atlikumu 
un vai atlikums nosakāms viennozīmīgi. 

**Teorēma:** 
Jebkuram veselam skaitlim $m$ un jebkuram naturālam skaitlim $n$ 
eksistē tieši viens veselu skaitļu pāris $(q,r)$, kuram izpildās nosacījumi:
$$m = q \cdot n + r,\;\;0 \leq r < n.$$


**Pierādījums.** 

**Eksistence (Izdalīt ar atlikumu vienmēr var).**  
Ar $q$ apzīmēsim lielāko veselo skaitli, 
kurš nepārsniedz $\frac{m}{n}$; tad  $q \leq \frac{m}{n} < q+1$ un $qn \leq m < qn+n$. 
Ar $r$ apzīmēsim skaitli $m-qn$; tātad $m = q \cdot n + r$. 
No nevienādībām $qn \leq m < qn+n$ seko, ka $0 \leq r < n$.

**Unitāte (Izdalīt ar atlikumu var tikai vienā veidā).**  
Pieņemsim, ka to pašu skaitli $m$ var izteikt divos dažādos veidos: 
$$\left\{ \begin{array}{ll}
m = q_1 \cdot n + r_1, & 0 \leq r_1 < n\\
m = q_1 \cdot n + r_1, & 0 \leq r_1 < n.\\
\end{array} \right.$$

Atņemot no pirmās vienādības otro, iegūstam:

$$0 = (q_1 - q_2) \cdot n + (r_1 - r_2)\;\;\text{jeb}\;\; (q_2 - q_1) \cdot n = (r_1 - r_2).$$

Tātad $r_1 - r_2$ dalās ar $n$. Tā kā $|r_1 - r_2 | < n$, tad 
$r_1 - r_2 = 0$ un tādēļ arī $r_1 = r_2$ un $q_1 = q_2$.  
Unitāte pierādīta.



## LKD un MKD 

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



## Eiklīda algoritms

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
\end{array} \right.$$
	
**Teorēma:** Pēdējais nenulles atlikums, ko iegūst, 
realizējot Eiklīda algoritmu ar skaitļiem $a_0$ un $a_1$, 
ir skaitļu $a_0$ un $a_1$ LKD. 
Turklāt, eksistē tādi veseli skaitļi $t$ un $s$, ka $a_k = ta_0 + sa_1$.


## Pirmskaitļi

**Definīcija:**  
Naturālu skaitli $n>1$ sauc par pirmskaitli, ja tam nav citu dalītāju, 
izņemot $1$ un $n$.

**Pirmskaitļu īpašības:**

1. Naturāls skaitlis $n>1$ nav pirmskaitlis tad un tikai tad, 
   kad eksistē tāds skaitļa $n$ dalītājs $m>1$, kurš nepārsniedz $\sqrt{n}$.
2. *Eiklīda lemma.* Ja $p$ ir pirmskaitlis, un $p \mid ab$, tad $p \mid a$ vai $p \mid b$.
3. Eksistē bezgalīgi daudz pirmskaitļu.
4. *Bertrāna postulāts.* Jebkuram naturālam skaitlim $n \geq 2$ 
   eksistē pirmskaitlis $p$, kurš atrodas intervālā $n < p < 2n$.
5. *Dirihlē teorēma.* Ja $(a,b)=1$, tad eksistē bezgalīgi daudz 
   tādu naturālu skaitļu $n$, ka $an+b$ ir pirmskaitlis.


## Dalāmības pazīmes

Šīs tēmas uzdevumos izmantojamas dalāmības pazīmes ar 
$3$, $9$ un $11$. Tās ir šādas:

* Skaitlis dalās ar $3$, ja tā ciparu summa dalās ar $3$.
* Skaitlis dalās ar $9$, ja tā ciparu summa dalās ar $9$. 
* Skaitlis dalās ar $11$, ja tā ciparu summa, kas atrodas pāra pozīcijās,    
  mīnus ciparu summa, kas atrodas nepāra pozīcijās, dalās ar $11$.


Uzdevumi, kas izmanto dalāmības pazīmes ar $2$, $4$, $8$, $5$, $25$ 
tiks aplūkoti citās tēmās, jo dalāmības pazīmes ar šiem skaitļiem 
izmanto tikai skaitļu pēdējos ciparus. 
Aplūkot skaitļa pēdējos ciparus, nozīmē aplūkot skaitli pēc moduļa $10^n$.





{!BBK2012.P1.1/content_lv.md!}


{!BBK2012.P1.2/content_lv.md!}


{!BBK2012.P1.3/content_lv.md!}


{!BBK2012.P1.4/content_lv.md!}


{!BBK2012.P1.5/content_lv.md!}


{!BBK2012.P1.6/content_lv.md!}


{!BBK2012.P1.7/content_lv.md!}


{!BBK2012.P1.8/content_lv.md!}


{!BBK2012.P1.9/content_lv.md!}


{!BBK2012.P1.10/content_lv.md!}


{!BBK2012.P1.11/content_lv.md!}


{!BBK2012.P1.12/content_lv.md!}


{!BBK2012.P1.13/content_lv.md!}


{!BBK2012.P1.14/content_lv.md!}


{!BBK2012.P1.15/content_lv.md!}


{!BBK2012.P1.16/content_lv.md!}


{!BBK2012.P1.17/content_lv.md!}


{!BBK2012.P1.18/content_lv.md!}


{!BBK2012.P1.19/content_lv.md!}


{!BBK2012.P1.20/content_lv.md!}


{!BBK2012.P1.21/content_lv.md!}


{!BBK2012.P1.22/content_lv.md!}


{!BBK2012.P1.23/content_lv.md!}


{!BBK2012.P1.24/content_lv.md!}


{!BBK2012.P1.25/content_lv.md!}


{!BBK2012.P1.26/content_lv.md!}

# Dalāmības īpašības

Dalāmības īpašības sk. [Jēdziens: dalītājs](Concept-p1.1-divisor.md), 
šeit papildus izmantojam sekojošus apgalvojumus:

* Ja $p$ ir pirmskaitlis un $p \mid ab$, tad $p \mid a$ vai $p \mid b$.
* Ja $a_1 \mid m$, $a_2 \mid m$, $\ldots$, $a_n \mid m$, tad
  $\operatorname{lcm}(a_1,a_2,\ldots,a_n)\,\mid\,m$. 
* Ja $a$ un $b$ ir savstarpēji pirmskaitļi un $a \mid bc$, tad $a \mid c$.

Pirmās un trešās īpašības pierādījumi nebūt nav vienkārši.
To pamatā ir teorēma par Eiklīda algoritmu un šīs īpašība tiks pierādītas otrajā nodaļā. 
Otrā īpašība seko no MKD definīcijas. Taču, rēķinot uzdevumus par skaitļu dalāmību, 
mums pašreiz nav vajadzības zināt aritmētikas pamatteorēmas pierādījumu, 
un tāpēc pagaidām izmantosim šīs īpašības uzdevumu risināšanā, atceroties, 
ka to pierādījumi tiks aplūkoti vēlāk, kad tiks pierādīta aritmētikas pamatteorēma.
Risinot uzdevumus, jāizmanto arī skaitļa sadalījums pirmreizinātājos 
un jāmāk uzrakstīt visi skaitļa dalītāji. Arī šajā gadījumā mēs faktiski 
lietojam aritmētikas pamatteorēmu, kas pagaidām nav pierādīta.

## Jautājumi paškontrolei

Pamatojiet norādītās atbildes.

1. Dots, ka naturāls skaitlis dalās ar $3$ un $4$. Vai šis 
   skaitlis noteikti dalās ar $12$?  
   Atbilde: jā.
2. Dots, ka naturāls skaitlis dalās ar $6$ un $4$. Vai šis skaitlis 
   noteikti dalās ar 24?  
   Atbilde: nē. 
3. Kur ir būtiskā atšķirība starp pirmo un otro jautājumu?  
   Atbilde: $3$ un $4$ ir savstarpēji pirmskaitļi, bet $6$ un $4$ – nē. 
4. Skaitlis $A$ nedalās ar $3$. Vai skaitlis $2A$ var dalīties ar $3$?
   Atbilde: nē.
5. Dots, ka $A$ ir pāra skaitlis. Vai skaitlis $3A$ 
   noteikti dalās ar $6$?  
   Atbilde: jā.
6. Skaitlis $5A$ dalās ar $3$. Vai skaitlis $A$ noteikti 
   dalās ar $3$?  
   Atbilde: jā.
7. Skaitlis $15A$ dalās ar $6$. Vai skaitlis $A$ 
   noteikti dalās ar $6$?  
   Atbilde: nē.





# Dalāmības īpašības: Ievaduzdevumi


{!BBK2012.P1.E2.1/content_lv.md!}


{!BBK2012.P1.E2.2/content_lv.md!}


{!BBK2012.P1.E2.3/content_lv.md!}


{!BBK2012.P1.E2.4/content_lv.md!}


{!BBK2012.P1.E2.5/content_lv.md!}


{!BBK2012.P1.E2.6/content_lv.md!}


{!BBK2012.P1.E2.7/content_lv.md!}


{!BBK2012.P1.E2.8/content_lv.md!}


{!BBK2012.P1.E2.9/content_lv.md!}


{!BBK2012.P1.E2.10/content_lv.md!}


{!BBK2012.P1.E2.11/content_lv.md!}


{!BBK2012.P1.E2.12/content_lv.md!}


{!BBK2012.P1.E2.13/content_lv.md!}


{!BBK2012.P1.E2.14/content_lv.md!}


{!BBK2012.P1.E2.15/content_lv.md!}


{!BBK2012.P1.E2.16/content_lv.md!}


{!BBK2012.P1.E2.17/content_lv.md!}


{!BBK2012.P1.E2.18/content_lv.md!}


{!BBK2012.P1.E2.19/content_lv.md!}


{!BBK2012.P1.E2.20/content_lv.md!}


{!BBK2012.P1.E2.21/content_lv.md!}


{!BBK2012.P1.E2.22/content_lv.md!}


{!BBK2012.P1.E2.23/content_lv.md!}


{!BBK2012.P1.E2.24/content_lv.md!}


{!BBK2012.P1.E2.25/content_lv.md!}


{!BBK2012.P1.E2.26/content_lv.md!}


{!BBK2012.P1.E2.27/content_lv.md!}


{!BBK2012.P1.E2.28/content_lv.md!}


{!BBK2012.P1.E2.29/content_lv.md!}


{!BBK2012.P1.E2.30/content_lv.md!}


{!BBK2012.P1.E2.31/content_lv.md!}


{!BBK2012.P1.E2.32/content_lv.md!}


{!BBK2012.P1.E2.33/content_lv.md!}


{!BBK2012.P1.E2.34/content_lv.md!}


{!BBK2012.P1.E2.35/content_lv.md!}


{!BBK2012.P1.E2.36/content_lv.md!}


{!BBK2012.P1.E2.37/content_lv.md!}


{!BBK2012.P1.E2.38/content_lv.md!}


{!BBK2012.P1.27/content_lv.md!}


{!BBK2012.P1.28/content_lv.md!}


{!BBK2012.P1.29/content_lv.md!}


{!BBK2012.P1.30/content_lv.md!}


{!BBK2012.P1.31/content_lv.md!}


{!BBK2012.P1.32/content_lv.md!}


{!BBK2012.P1.33/content_lv.md!}


{!BBK2012.P1.34/content_lv.md!}


{!BBK2012.P1.35/content_lv.md!}


{!BBK2012.P1.36/content_lv.md!}


{!BBK2012.P1.37/content_lv.md!}


{!BBK2012.P1.38/content_lv.md!}


{!BBK2012.P1.39/content_lv.md!}


{!BBK2012.P1.40/content_lv.md!}


{!BBK2012.P1.41/content_lv.md!}


{!BBK2012.P1.42/content_lv.md!}


{!BBK2012.P1.43/content_lv.md!}


{!BBK2012.P1.44/content_lv.md!}


{!BBK2012.P1.45/content_lv.md!}


{!BBK2012.P1.46/content_lv.md!}


{!BBK2012.P1.47/content_lv.md!}


{!BBK2012.P1.48/content_lv.md!}


{!BBK2012.P1.49/content_lv.md!}


{!BBK2012.P1.50/content_lv.md!}


{!BBK2012.P1.51/content_lv.md!}


{!BBK2012.P1.52/content_lv.md!}


{!BBK2012.P1.53/content_lv.md!}


{!BBK2012.P1.54/content_lv.md!}


{!BBK2012.P1.55/content_lv.md!}


{!BBK2012.P1.56/content_lv.md!}


{!BBK2012.P1.57/content_lv.md!}


{!BBK2012.P1.58/content_lv.md!}


{!BBK2012.P1.59/content_lv.md!}


{!BBK2012.P1.60/content_lv.md!}


{!BBK2012.P1.61/content_lv.md!}


{!BBK2012.P1.62/content_lv.md!}


{!BBK2012.P1.63/content_lv.md!}


{!BBK2012.P1.64/content_lv.md!}


{!BBK2012.P1.65/content_lv.md!}


{!BBK2012.P1.66/content_lv.md!}


{!BBK2012.P1.67/content_lv.md!}


{!BBK2012.P1.68/content_lv.md!}


{!BBK2012.P1.69/content_lv.md!}


{!BBK2012.P1.70/content_lv.md!}


{!BBK2012.P1.71/content_lv.md!}


{!BBK2012.P1.72/content_lv.md!}


{!BBK2012.P1.73/content_lv.md!}


{!BBK2012.P1.74/content_lv.md!}


{!BBK2012.P1.75/content_lv.md!}


{!BBK2012.P1.76/content_lv.md!}


{!BBK2012.P1.77/content_lv.md!}


{!BBK2012.P1.78/content_lv.md!}

## Skaiţ̦a n! Dalītāji

Pirmo $n$ naturālo skaitlu reizinājumu apzīmē ar $n!$. Skaidrs, ka visi naturālie skaitļi 
(tai skaitā arī pirmskaitļi), kas nepārsniedz $n$ ir skaitļa $n!$ dalītāji. 
Šis vienkāršais apgalvojums tiks izmantots sekojošo uzdevumu risināšanai.

Vispirms aplūkosim, kā šo ideju bija izmantojis Eiklīds, lai pierādītu, ka pirmskaitļu 
skaits ir bezgalīgs. Pien̦emsim pretējo, ka pirmskaitļu skaits ir galīgs. 
Tādā gadījumā aplūkosim visus pirmskaitļus $p_{1}<p_{2}<\cdots<p_{n}$. Ņemsim skaitli 
$N=p_{1} p_{2} \cdots p_{n}+1$. Skaitlis $N$ dalās ar kādu pirmskaitli $p$. Skaidrs, ka 
$p \neq p_{i}$, jo pretējā gadījumā iegūstam, ka $p \mid\left(p_{1} p_{2} \cdots p_{n}+1\right)$, tātad

$$p \mid\left(\left(p_{1} p_{2} \cdots p_{n}+1\right)-\left(p_{1} p_{2} \cdots p_{n}\right)\right)=1,$$

kas nav iespējams. Šī pretruna pierāda, ka pirmskaitļu skaits ir bezgalīgs.

Šis rezultāts ir pirmais jautājumā par to, cik daudz ir pirmskaitļu - precīzāk: 
cik bieži naturālo skaiţ̦u virknē ir sastopami pirmskaitļi? 
Šis jautājums faktiski ir pamatā veselam skaitļu teorijas virzienam, ko sauc par 
pirmskaitļu sadalījuma teoriju. Lai novērtētu pirmskaitļu daudzumu, tiek aplūkota 
funkcija $\Pi(x)$, kuru definē šādi: $\Pi(x)$ ir pirmskaitļu skaits, kuri nepārsniedz $x$. 
Apgalvojumu, ka pirmskaitļu skaits ir bezgalīgs var pierakstīt šādi:

$$\lim _{x \rightarrow \infty} \prod_{0}(x)=\infty .$$

Taču, kā zināms, funkcijas, kuras bezgalībā tiecas un bezgalību, var augt ātrāk vai lēnāk. 
Precīzs funkcijas $\Pi(x)$ augšanas ātruma novērtējums redzams teorēmā par 
pirmskaitļu sadalījumu. Šo hipotēzi 16 gadu vecumā izteica Gauss, un 1896. gadā 
neatkarīgi pierādīja Adamārs un Valle-Pusens.



**Teorēma (par pirmskaitļu izvietojumu):** Ir spēkā sekojoša robeža:

$$\lim _{x \rightarrow \infty}\left(\prod(x) \cdot \frac{\ln x}{x}\right)=1.$$

Teorēma būtībā nozīmē, ka starp pirmajiem $n$ naturālajiem skaițiem ir apmēram 
$\frac{n}{\ln n}$ pirmskaitļu.

Tomēr uzdevumi par pirmskaitļu sadalījumu ir ļoti sarežğîti, un daudzi no tiem 
arī pašreiz nav atrisināti. Neatrisināti, piemēram, ir šādi uzdevumi.

- Vai eksistē bezgalīgi daudz pirmskaitļu, kas uzrakstāmi formā $n^{2}+1$ ?
- Vai eksistē bezgalīgi daudz pirmskaitļu, kas uzrakstāmi formā $2^{n}+1$ ? (Fermā pirmskaitlii).
- Vai eksistē bezgalīgi daudz pirmskaitļu, kas uzrakstāmi formā $2^{n}-1$ ? (Mersena pirmskaitļi).
- Vai eksistē bezgalīgi daudz tādu pirmskaitļu $p$, kuriem skaitlis $p+2$ arī ir pirmskaitlis? (Dvīņu problēma).

Tagad paskatīsimies, kā Eiklīda ideja tiek izmantota uzdevumu risināšanā.






{!BBK2012.P1.79/content_lv.md!}


{!BBK2012.P1.80/content_lv.md!}


{!BBK2012.P1.81/content_lv.md!}


{!BBK2012.P1.82/content_lv.md!}


{!BBK2012.P1.83/content_lv.md!}


{!BBK2012.P1.84/content_lv.md!}


{!BBK2012.P1.85/content_lv.md!}


{!BBK2012.P1.86/content_lv.md!}


{!BBK2012.P1.87/content_lv.md!}


{!BBK2012.P1.88/content_lv.md!}


{!BBK2012.P1.89/content_lv.md!}

## Lielākais kopīgais dalītājs un mazākais kopīgais dalāmais



{!BBK2012.P1.E4.1/content_lv.md!}


{!BBK2012.P1.E4.2/content_lv.md!}


{!BBK2012.P1.E4.3/content_lv.md!}


{!BBK2012.P1.E4.4/content_lv.md!}


{!BBK2012.P1.E4.5/content_lv.md!}


{!BBK2012.P1.E4.6/content_lv.md!}


{!BBK2012.P1.E4.7/content_lv.md!}


{!BBK2012.P1.E4.8/content_lv.md!}


{!BBK2012.P1.E4.9/content_lv.md!}


{!BBK2012.P1.E4.10/content_lv.md!}


{!BBK2012.P1.E4.11/content_lv.md!}


{!BBK2012.P1.E4.12/content_lv.md!}


{!BBK2012.P1.E4.13/content_lv.md!}


{!BBK2012.P1.E4.14/content_lv.md!}


{!BBK2012.P1.E4.15/content_lv.md!}


{!BBK2012.P1.E4.16/content_lv.md!}


{!BBK2012.P1.E4.17/content_lv.md!}


{!BBK2012.P1.E4.18/content_lv.md!}


{!BBK2012.P1.E4.19/content_lv.md!}


{!BBK2012.P1.E4.20/content_lv.md!}


{!BBK2012.P1.E4.21/content_lv.md!}


{!BBK2012.P1.E4.22/content_lv.md!}


{!BBK2012.P1.E4.23/content_lv.md!}


{!BBK2012.P1.E4.24/content_lv.md!}


{!BBK2012.P1.E4.25/content_lv.md!}


{!BBK2012.P1.E4.26/content_lv.md!}


{!BBK2012.P1.90/content_lv.md!}


{!BBK2012.P1.91/content_lv.md!}


{!BBK2012.P1.92/content_lv.md!}


{!BBK2012.P1.93/content_lv.md!}


{!BBK2012.P1.94/content_lv.md!}


{!BBK2012.P1.95/content_lv.md!}


{!BBK2012.P1.96/content_lv.md!}


{!BBK2012.P1.97/content_lv.md!}


{!BBK2012.P1.98/content_lv.md!}


{!BBK2012.P1.99/content_lv.md!}


{!BBK2012.P1.100/content_lv.md!}


{!BBK2012.P1.101/content_lv.md!}


{!BBK2012.P1.102/content_lv.md!}


{!BBK2012.P1.103/content_lv.md!}


{!BBK2012.P1.104/content_lv.md!}


{!BBK2012.P1.105/content_lv.md!}


{!BBK2012.P1.106/content_lv.md!}


{!BBK2012.P1.107/content_lv.md!}


{!BBK2012.P1.108/content_lv.md!}


{!BBK2012.P1.109/content_lv.md!}


{!BBK2012.P1.110/content_lv.md!}


{!BBK2012.P1.111/content_lv.md!}


{!BBK2012.P1.112/content_lv.md!}


{!BBK2012.P1.113/content_lv.md!}


{!BBK2012.P1.114/content_lv.md!}


{!BBK2012.P1.115/content_lv.md!}


{!BBK2012.P1.116/content_lv.md!}


{!BBK2012.P1.117/content_lv.md!}


{!BBK2012.P1.118/content_lv.md!}


{!BBK2012.P1.119/content_lv.md!}


{!BBK2012.P1.120/content_lv.md!}


{!BBK2012.P1.121/content_lv.md!}

## Skaitļa n daudzkārtņu skaits intervālā

**Teorēma (par daudzkārtņu skaitu intervālā):** Starp pirmajiem $m$ naturālajiem skaitļiem 
ir tieši $\left\lfloor \frac{m}{n}\right\rfloor$ skaitla $n$ daudzkārtņu.

*Pierādījums.* Skaiț̣a $n$ daudzkārtņi, kas nepārsniedz $m$ ir uzrakstāmi formā 
$1 \cdot n, 2 \cdot n, \ldots, k \cdot n$, turklāt $kn \leq m$ un $(k+1)n > m$. Šādu daudzkārtṇu skaits ir $k$.

Pārveidojot nevienādības, iegūstam $k \leq \frac{m}{n}<k+1$. Tātad $k=\left\lfloor \frac{m}{n} \right\rfloor$.









{!BBK2012.P1.122/content_lv.md!}


{!BBK2012.P1.123/content_lv.md!}


{!BBK2012.P1.124/content_lv.md!}


{!BBK2012.P1.125/content_lv.md!}


{!BBK2012.P1.126/content_lv.md!}


{!BBK2012.P1.127/content_lv.md!}


{!BBK2012.P1.128/content_lv.md!}


{!BBK2012.P1.129/content_lv.md!}


{!BBK2012.P1.130/content_lv.md!}


{!BBK2012.P1.131/content_lv.md!}


{!BBK2012.P1.132/content_lv.md!}

