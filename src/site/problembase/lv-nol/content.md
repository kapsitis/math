# <lo-sample/> LV.NOL.2000.7.4 

Naturālu skaitli sauc par interesantu, ja tā ciparu summa dalās ar $5$. 

**(A)** atrast kaut vienu tādu interesantu $x$, ka arī $x+9$ ir interesants,   
**(B)** cik pavisam ir tādu interesantu $x$, kādi minēti **(A)** punktā?  
**(C)** pierādīt: starp jebkuriem $9$ pēc kārtas ņemtiem naturāliem skaitļiem ir 
vismaz viens interesants.


<small>

* topic:DivisibilityRulesForRemainders
* topic:SequenceGaps
* topic:ArithmeticSeriesDivisibility
* questionType:FindExample,FindCount,Prove
* genre:SpecialNumbers

</small>




## Atrisinājums 

**(A)** un **(B)** gadījumā
$x$ un $x+9$ ciparu summas mēdz atšķirties par
$9$ daudzkārtni, tie var atšķirties par $0$ vai $45$, utt. 

* Par $0$ atšķiras, piemēram, $5$ un $14$ ciparu summas. 
* Par $45$ atšķiras, piemēram, $1999999$ un $2000008$ ciparu summas. 


**(C)** Skaitļu ciparu summas veido virknes, kas deviņus soļus aug pa $1$ (vienu 
ciparam pieaugot no $0$ līdz $9$), 
pēc tam vienu soli par kaut kādu daudzumu sadilst (vienu cipars no $9$ pēkšņi 
pārvēršas par $0$). Virknīte garumā $9$ (neatkarīgi no tā, kurā brīdī 
vienu cipars pārlec uz $0$), saturēs augošu gabalu garumā $5$.



# <lo-sample/> LV.NOL.2000.7.5 

Uz tāfeles uzrakstīti skaitļi $\frac{3}{2}$; $\frac{4}{5}$; $\frac{5}{3}$. 
Ar vienu gājienu atļauts izvēlēties divus no uzrakstītajiem skaitļiem 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt 
uz tāfeles skaitļus $\frac{b^2}{a}$ un $\frac{a^2}{b}$. Vai, izdarot vairākus 
šādus gājienus pēc kārtas, var panākt, lai uz tāfeles vienlaicīgi 
atrastos skaitļi $\frac{4}{3}$; $\frac{4}{5}$; $\frac{5}{2}$? 

<small>

* topic:InvariantAlgebraic
* strategy:Invariant
* questionType:ProveDisprove
* genre:MakingMoves
* seeAlso:LV.NOL.2019.8.4

</small>




## Atrisinājums
 
Trīs skaitļu reizinājums nemainās. Tomēr šajā piemērā reizinājumiem 
sākumā un beigās jāatšķiras. Pretruna.

$$\frac{3}{2}\cdot\frac{4}{5}\cdot\frac{5}{3} = \frac{2}{1}$$
$$\frac{4}{3}\cdot\frac{4}{5}\cdot\frac{5}{2} = \frac{8}{3}$$



# <lo-sample/> LV.NOL.2000.8.5 

Tabula sastāv no $n \times n$ rūtiņām. Katrā rūtiņā jāieraksta
$0$, $1$ vai $2$ tā, lai, aprēķinot rindiņās un kolonnās 
ierakstīto skaitļu summas, iegūtu visus naturālos skaitļus no $1$ līdz $2n$, 
katru vienu reizi. Vai to var izdarīt, ja  
**(a)** $n = 5$, **(b)** $n=6$? 

<small>

* topic:InvariantAlgebraic
* topic:TelescopicSums
* topic:CountingObjects

</small>

<!--
genre=magic-configuration
questionType=ProveDisprove
-->



## Neiespējamība

$n=5$ nevar, jo $1+2+\ldots+10=55$ ir nepāru skaitlis, bet 
tam jābūt pāru (summas pa rindiņām un kolonnām sakrīt).



## Piemēra konstruēšana

$n=6$ var ($1,2,3,10,11,12$ pa vertikāli).

| 0   | 0   | 0   | 1   | 1   | 2   |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 1   | 2   | 2   |
| 0   | 0   | 0   | 2   | 2   | 2   |
| 0   | 0   | 1   | 2   | 2   | 2   |
| 0   | 1   | 1   | 2   | 2   | 2   |
| 1   | 1   | 1   | 2   | 2   | 2   |



# <lo-sample/> LV.NOL.2000.9.2 

Kvadrāts sastāv no $3 \times 3$ rūtiņām. Tajās ieraksta veselus skaitļus no $1$ līdz $9$ (katrā rūtiņā -
citu skaitli). Pēc tam katrām divām rūtiņām, kurām ir kopīga mala, aprēķina tajās ierakstīto
skaitļu summu (pavisam būs $12$ summas). Kādu mazāko skaitu dažādu vērtību var iegūt?

<small>

* topic:ExtremeElementMethod

</small>

<!--
genre=fill-in-table
questionType=FindOptimal
-->



## Piemēra konstrukcija

Mazāk kā $4$ vērtības nevar, jo skaitli vidū saskaita ar $4$ dažādiem skaitļiem. 
Četras var: $((3,8,1),(4,5,6),(9,2,7))$. 

| 3   | 8   | 1   |
| --- | --- | --- | 
| 4   | 5   | 6   |
| 9   | 2   | 7   |





# <lo-sample/> LV.NOL.2000.9.4 

Uz $5$ kartītēm uzrakstīts pa naturālam skaitlim (starp tiem var būt arī vienādi). Uz katrām
trim kartītēm uzrakstīto skaitļu summa dalās ar to skaitļu summu, kas uzrakstīti uz abām
pārējām kartītēm.

1. atrodiet kaut vienu piemēru, kur šis nosacījums izpildās,
2. vai tas var izpildīties, ja uz visām kartītēm uzrakstīti dažādi skaitļi?

<small>

* topic:NumTheoryExpr

</small>

<!--
questionType=FindExample,ProveDisprove
-->



## Gadījumu šķirošana

* Ja visi $5$ skaitļi vienādi ar $a$, tad nevar gadīties, ka $3a$ dalās ar $2a$. 
* Ja četri skaitļi vienādi un viens atšķiras, var izvēlēties komplektu $(1,1,1,1,2)$. 






# <lo-sample/> LV.NOL.2000.10.1 

Dots, ka $A$ un $B$ ir trīsciparu naturāli skaitļi, 
pie tam $A$ simtu cipars sakrīt ar $A$ vienu
ciparu. Zināms arī, ka $A-B=297$ un $B$ ciparu summa ir $23$. Atrast $A$ un $B$.


<!--
concepts=sum-of-digits
questionType=FindAll
-->



# <lo-sample/> LV.NOL.2000.10.2 

Kvadrāts sastāv no $3 \times 3$ rūtiņām. 
Katrā rūtiņā jāieraksta pa naturālam skaitlim, kas
nepārsniedz n (visiem skaitļiem jābūt dažādiem) tā, lai 
no katriem diviem skaitļiem, kas
ierakstīti rūtiņās ar kopīgu malu, viens dalītos ar otru.  
Vai to var izdarīt, ja (a) $n=15$, (b) $n=13$?

<!--
genre=fill-in-table
questionType=ProveDisprove
-->





# <lo-sample/> LV.NOL.2000.10.5 

No pirmajiem $20$ naturālajiem skaitļiem izvēlēti 
$10$ skaitļi tā, ka to summa ir $105$, bet
nekādu divu izvēlēto skaitļu summa nav $21$. 
Aprēķināt visu izvēlēto skaitļu kvadrātu
summu.

<!--
questionType=FindAll
-->



## ABC

**#MasuCentrs** No katra pāra $(n,21-n)$ ņemts tieši viens. 



# <lo-sample/> LV.NOL.2000.11.1 

Ar $\lfloor a \rfloor$ apzīmējam lielāko veselo skaitli, kas nepārsniedz $a$. 
Piemēram, $\lfloor 4.8 \rfloor=4$; $\lfloor 5 \rfloor=5$.
Atrisināt pozitīvos skaitļos vienādojumu
$$ x \left\lfloor x \left\lfloor x \right\rfloor \right\rfloor = 41. $$


<!--
seeAlso=LV.NOL.2001.11.1
questionType=FindAll
-->



## ABC

**#Nevienādība** **#GadījumuPārlase** $x \in [3;4)$. Tad $x \lfloor 3x \rfloor = 41$. Trīs gadījumi: $x \cdot 9 = 41$, $x \cdot 10 = 41$, $x \cdot 11 = 41$. Vienīgi $x = 41/11$ der.



# <lo-sample/> LV.NOL.2000.11.4 

Naturāls skaitlis $n$, kas nedalās ar $4$, vienāds ar savu četru mazāko naturālo dalītāju
kvadrātu summu.

1. pierādīt, ka $n$ noteikti ir pāra skaitlis,
2. atrast vienu tādu skaitli $n$,
3. pierādīt, ka citu tādu $n$ nav.

<!--
questionType=Prove,FindExample,Prove
-->



## ABC

**#Paritāte** **#Polinomi** Četru nepāru summa nav nepāru. $N = 1^2 + 2^2 + p^2 + (2p)^2 = 5(p^2+1)$, t.i. mazākais nepāru $p\,\mid\,N$ ir $5$, un $5(5^2+1) = 130$. 



# <lo-sample/> LV.NOL.2000.12.1 

Skaitļu virknē pirmais un otrais loceklis abi ir 1, bet katrs nākošais vienāds ar abu
iepriekšējo summu. Vai ar $5$ dalās šīs virknes
(a) $21$-ais, (b) $2000$-ais loceklis?

<!--
seeAlso=LV.NOL.2001.12.1
seeAlso=LV.NOL.2003.12.1
seeAlso=LV.NOL.2004.12.1
questionType=FindAll
-->



## ABC

**#Kongruences** **#PeriodiskaVirkne**  Pirmie $20$ atlikumi: $1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0$, tālāk periods. $F_{21}$ dos atlikumu $1$, bet $F_{2000}$ dalīsies ar $5$. 







# <lo-sample/> LV.NOL.2001.7.1 

Divos pēc kārtas sekojošos gados katrā ir $365$ dienas. 
Pirmajā no tiem sestdienu ir vairāk nekā trešdienu. 
Kuru nedēļas dienu otrajā gadā ir visvairāk? 

<small>

* topic:IntegerCongruence
* topic:MultiplesInInterval

</small>

<!--
questionType=FindAll
-->



## 365:7 - dalīšana ar atlikumu
 
$365$ dienu gads sākas un beidzas ar to pašu dienu. 
1.gads sākas/beidzas ar sestdienu (visu citu dienu ir vienāds skaits). 
Bet nākamais sākas un beidzas ar svētdienu.



# <lo-sample/> LV.NOL.2001.7.4 

Virknē uzrakstīti cipari no $1$ līdz $9$ (skat. zīmējumu):
$$1\;\;2\;\;3\;\;4\;\;5\;\;6\;\;7\;\;8\;\;9$$
Kādu lielāko daudzumu semikolu var ievietot starp blakus esošiem 
cipariem, lai tie sadalītu ciparu virkni tādu naturālu skaitļu pierakstos, 
no kuriem katriem diviem lielākais kopīgais dalītājs ir $1$? 
(Piemēram, $123;45678;9$ neder, jo $123$ un $9$ abi dalās ar $3$.)

<small>

* topic:NumTheoryPigeonhole
* topic:ExhaustionMethod

</small>

<!--
concepts=coprimes
questionType=FindOptimal
-->



## ABC
 
**#DirihlēPrincips** **#LKD** Ja ir $6$ semikoli, aiz 2 pāru cipariem beigtos skaitlis. Ar pieciem: $1;23;4;5;67;89$.




# <lo-sample/> LV.NOL.2001.8.3 

Uzrakstiet kaut vienu desmitciparu skaitli, kam visi 
cipari ir dažādi un kam piemīt īpašība: izsvītrojot jebkurus $n$ ciparus
($n$ – jebkurš naturāls skaitlis, kas nepārsniedz $6$), 
atlikušie cipari (tai pašā secībā) veido saliktu skaitli. 
Pamatojiet savu risinājumu. 

<small>

* topic:DivisibilityRulesFor2And4
* topic:ExhaustionMethod

</small>


<!--
concepts=primes,composite-numbers
genre=digit-manipulation
questionType=FindOptimal
-->



## Dalāmība ar 2 un 5

* Ja skaitļa beigās pāru cipari un $5$, tad tie visi jāizsvītro. 
* Pārkārtojot $(1,3,7,9)$ dažādā secībā, meklējam saliktu skaitli. 
* $1379$ dalās ar $7$. Tātad $1379502468$ der. 



# <lo-sample/> LV.NOL.2001.9.1 

Dots, $n$ – naturāls skaitlis. 
Pierādiet, ka vismaz viens no skaitļiem  $n^3 - n$
un $n^3 + n$
dalās ar $10$.

<!--
questionType=Prove
-->



## ABC

**#GadījumuPārlase** **#Kongruences** $0^3+0$, $1^3-1$, $2^3+2$, $3^3+3$, 
$4^3-4$, $5^5-5$, $6^6 - 6$, $7^3 + 7$, $8^3 + 8$, $9^9-9$.  




# <lo-sample/> LV.NOL.2001.9.5 

Plakne sadalīta kvadrātiņos kā rūtiņu lapa; 
rūtiņas malas garums ir $1$.
Uzzīmēta slēgta lauzta līnija, kuras visi posmi iet pa 
rūtiņu malām, un katra
posma garums ir nepāra skaitlis. 
Vai šai līnijai var būt tieši  
(a) $2000$, (b) $2001$, (c) $2002$ posmi?


<!--
questionType=ProveDisprove
-->



## ABC

**#Invariants** Ar $2000$ var (saliek kopā 2 "trepes"). $2001$ nevar, 
jo mijas horizontāli un vertikāli posmi. $2002$ nevar, 
jo $1001$ nepāra (horizontālo) pārvietojumu summa nevar būt $0$.   



# <lo-sample/> LV.NOL.2001.10.1 

Dots, ka $A$ un $B$ ir trīsciparu naturāli skaitļi, 
pie tam $A$ simtu cipars sakrīt
ar $B$ vienu ciparu, bet $B$ simtu cipars sakrīt ar 
$A$ vienu ciparu. Zināms arī, ka
$A - B = 297$ un $B$ ciparu summa ir $23$. Atrast $A$ un $B$.


<!--
concepts=sum-of-digits
questionType=ProveDisprove
-->



# <lo-sample/> LV.NOL.2001.10.4 

Izsacīt izteiksmes 
$$\sqrt{1 + \frac{1}{1^2} + \frac{1}{2^2}}
+ \sqrt{1 + \frac{1}{2^2} + \frac{1}{3^2}} +$$
$$+ \sqrt{1 + \frac{1}{3^2} + \frac{1}{4^2}}
+ \cdots + \sqrt{1 + \frac{1}{9^2} + \frac{1}{10^2}}$$
vērtību kā galīgu decimāldaļskaitli. 

<!--
concepts=square-root,decimal-fractions
questionType=FindAll
-->




# <lo-sample/> LV.NOL.2001.11.3 

Kādiem naturāliem $k$ skaitlis $k^k + 1$ ir pirmskaitlis, kas mazāks par
$10^{19}$. 


<!--
questionType=FindAll
concepts=primes
seeAlso=LV.NOL.2002.11.1
-->



## ABC

**#Nevienādība** **#AlgebriskaIdentitāte** Ja $k >1$ ir nepāra dalītājs, tad dalās reizinātājos kā $a^{2n+1}+b^{2n+1}$. Arī $8^8+1 = (2^8)^3 + 1^3$ dalās reizinātājos, bet $16^{16}+1>10^{19}$. Tāpēc $k=1,2,4$.




# <lo-sample/> LV.NOL.2001.12.1 

Skaitļu virknē pirmais un otrais loceklis abi ir 1, bet katrs nākošais
vienāds ar abu iepriekšējo summu. Vai ar 5 dalās šīs virknes

1. $21$-ais,
2. $2000$-ais loceklis? 


<!--
questionType=FindAll
concepts=fibonacci-sequence
-->








# <lo-sample/> LV.NOL.2002.7.3 


Uz tāfeles uzrakstīti naturālie skaitļi no $3$ līdz $10$ ieskaitot, 
katrs vienu reizi. 
Ar vienu gājienu atļauts diviem uz tāfeles esošiem 
skaitļiem vienlaicīgi pieskaitīt pa vieniniekam. 
Kāds lielākais dažādu pirmskaitļu daudzums var vienlaikus atrasties uz tāfeles?


<small>

* topic:PrimesDistribution
* topic:InvariantParity

</small>

<!--
genre=optimization
questionType=FindOptimal
-->



## ABC
 
**#Invariants** **#Konstrukcija** $8$ nepāru pirmskaitļu summa var būt $52+2k$; visi var būt pirmskaitļi. 




# <lo-sample/> LV.NOL.2002.8.3 

Burtnīcā ir $100$ lapas; tās lappuses sanumurētas dabīgā kārtībā ar numuriem 
no $1$ līdz $200$. Vai izrauto lappušu numuru summa var būt $1000$, ja tiek izrautas  
**(a)** $31$ lapa;   
**(b)** $30$ lapas?   
*Piezīme.* Lapas var neraut pēc kārtas.

<small>

* topic:InvariantParity
* topic:InvariantRemainder
* topic:NumTheoryInequalityLargeIntervals
* topic:SeriesMembersSumsClosedFormulas


</small>

<!--
concepts=arithmetic-progression
questionType=ProveDisprove
-->



## Paritāte
 
**(a)** summa būtu nepāru. 
**(b)** trīsdesmit $4k_i-1$ summa nedalītos ar $4$.

Var pamatot arī ar nevienādību:  
Jau $1+\ldots+60 > 1000$, tādēļ pat vismazāko lapu numuru summa ir par lielu.



# <lo-sample/> LV.NOL.2002.9.1 

Jānis uzrakstīja $n$ pēc kārtas sekojošus naturālus skaitļus.
Neviens no tiem nedalās ar diviem vai vairāk dažādiem 
pirmskaitļiem. Kāda ir
lielākā iespējamā $n$ vērtība?

<!--
concepts=primes
questionType=FindOptimal
-->



## ABC

**#Dalāmība** Tādi ir $1,2,3,4,5$. Vairāk kā $n=5$ nevar būt, jo katram sestajam ($6$ dalītājiem) ir divi pirmskaitļu dalītāji.



# <lo-sample/> LV.NOL.2002.9.4 

Ar $p(n)$ apzīmēsim naturāla skaitļa n ciparu reizinājumu. 
Piemēram,
$p(26)=12$; $p(8)=8$; $p(102)=0$.
Aprēķināt summu $p(1)+p(2)+p(3)+\ldots +p(2001)+p(2002)$.



## ABC

**#AlgebrisksPārveidojums** Trīsciparu skaitļiem $p(n)$ summa būs $(1+2+\ldots+9)^3$ (pārbauda, atverot iekavas). Visiem prasītajiem: $45+45^2+2\cdot 45^3 = 184320$. 




# <lo-sample/> LV.NOL.2002.10.3 

Naturālu skaitļu $m$ un $n$ lielākais kopīgais dalītājs 
ir $d$, bet mazākais
kopīgais dalāmais ir $D$. Pierādiet: 
$2m+n=2D+d$ tad un tikai tad, ja $m$ dalās ar $n$.



## ABC

**#MKD** **#LKD**  **#AlgebriskaNevienādība** Ja $m$ dalās ar $n$, tad $D=m$, $d=n$ un $2m+n=2D+d$. 
Reizinājums $Dd=mn$ ir fiksēts; $2D+d = 2D+mn/D$ monotoni aug, ja $D \geq \sqrt{mn/2}$.




# <lo-sample/> LV.NOL.2002.10.5 

Dotas $2002$ konfekšu kastes. Katrā kastē ir 
vismaz viena konfekte, un
nekādās divās kastēs konfekšu daudzumi nav vienādi. 
Nevienā kastē nav vairāk par $2002$ konfektēm. 
Ar vienu gājienu atļauts no dažām
kastēm apēst vienādu skaitu konfekšu 
(drīkst arī ēst konfektes tikai no
vienas kastes).  
Kāds ir mazākais gājienu skaits, ar kuru var apēst visas konfektes?




## ABC

**#Binārais pieraksts** Katru no $2002$ skaitļiem var pierakstīt ar $11$ binārā pieraksta cipariem. 
$2002_{10}=11111010010_{2}$. Katrā gājienā noēd bināro ciparu, kur tas ir.
Ja ēd $10$ dienas, tad var noēst tikai $2^{10}$ dažādus skaitļus.



# <lo-sample/> LV.NOL.2002.11.2 

Andris izvēlējās 5 dažādus naturālus skaitļus un katriem diviem
izvēlētajiem skaitļiem aprēķināja to summu. Kādu mazāko daudzumu
dažādu rezultātu Andris varēja iegūt?

<!--
seeAlso=LV.NOL.2003.11.1  
seeAlso=LV.NOL.2004.11.1  
questionType=FindOptimal
-->



# <lo-sample/> LV.NOL.2002.12.1 

Dots, ka $\sin x$ - racionāls skaitlis. Vai $\sin 2x$ var būt  
(a) racionāls, (b) iracionāls, (c) nedefinēts?

<!--
concepts=irrational-numbers,rational-numbers
questionType=ProveDisprove
-->



## ABC

**#PitagoraTrijnieki** **#IracionalitātesPierādījumi** Racionāls: $\sin x = 4/5$; $\sin 2x = 2 \sin x \cos x = 2 \cdot \frac{4}{5} \cdot \frac{3}{4} = \frac{24}{25}$. Iracionāls: $\sin (\pi / 3) = \frac{\sqrt{3}}{2}$. Sinuss definēts visiem $x \in \mathbb{R}$.






# <lo-sample/> LV.NOL.2003.7.4/LV.NOL.2005.7.1 


Kādu mazāko daudzumu no skaitļiem   
$1;2;3;\ldots;12;13$ var izsvītrot, lai 
katru divu atlikušo summa būtu salikts skaitlis? 

<small>

* topic:BipartiteGraphs
* topic:ModularParity

</small>

<!--
questionType=FindOptimal
concepts=primes,composite-numbers
-->



## ABC
 
**#DirihlēPrincips** **#Paritāte** **#Pirmskaitļi** Var svītrot $6$ pāru skaitļus. Mazāk nevar, jo jāizjauc $6$ pāri $(1;12)$ utt.




# <lo-sample/> LV.NOL.2003.8.3 

Kādu mazāko daudzumu no naturāliem skaitļiem $1;2;3;\ldots;12$ var izsvītrot, 
lai atlikušos varētu sadalīt divās grupās ar īpašību: 
vienas grupas visu skaitļu reizinājums vienāds ar otras grupas visu skaitļu reizinājumu. 

<small>

* topic:CanonicalFactorization

</small>


<!--
questionType=FindOptimal
-->



## ABC
 
**#EiklīdaLemma** Jāsvītro $7, 11$ un viens $3$ daudzkārtnis. $1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 8 \cdot 9 \cdot 10$.




# <lo-sample/> LV.NOL.2003.9.1 

Jānis uzrakstīja $n$ pēc kārtas sekojošus naturālus skaitļus. 
Neviens no tiem nedalās ar trim vai vairāk dažādiem 
pirmskaitļiem. Kāda ir lielākā iespējamā $n$ vērtība?

<!--
concepts=primes
questionType=FindOptimal
-->



## ABC

**#Dalāmība** Tādi ir $1,2,\ldots,29$. Vairāk kā $n=29$ nevar būt, jo katram trīsdesmitajam ($30$ dalītājiem) ir trīs pirmskaitļu dalītāji.





# <lo-sample/> LV.NOL.2003.9.5 

Uz galda atrodas $n$ konfektes. Andris un Pēteris pēc kārtas 
izdara gājienus; pirmais iet Andris. 
Ar vienu gājienu tiek paņemtas dažas
konfektes; pie tam jāņem vismaz $1$ konfekte, 
bet nedrīkst ņemt vairāk
par pusi uz galda esošo konfekšu. 
Tas zēns, pēc kura gājiena uz galda
paliek 1 konfekte, zaudē.
Kas uzvar, pareizi spēlējot, ja  
(a) $n = 47$,  
(b) $n = 2003$?

<!--
questionType=Algorithm,Prove
-->



# <lo-sample/> LV.NOL.2003.10.1 

Dots, ka $x$ un $y$ – naturāli skaitļi. Vai var gadīties, ka

1. $(2x+3y)(3x+2y)$ dalās ar $5$, bet nedalās ar $25$?
2. $(2x+3y)(3x+2y)$ dalās ar $2003$, bet nedalās ar $2003^2$?

<!--
questionType=ProveDisprove
-->



# <lo-sample/> LV.NOL.2003.11.4 

Ir zināms, ka skaitlis $38$ ir mazākais naturālais skaitlis, kura kvadrāts
beidzas ar $3$ četriniekiem: $38^2 = 1444$.

1. vai šādu naturālu skaitļu ir bezgalīgi daudz?
2. atrodiet otro mazāko naturālo skaitli ar šādu īpašību.

<!--
questionType=ProveDisprove,FindOptimal
-->



## ABC

**#AlgebriskaIdentitāte** (a) Jā; visi $1000n + 38$ der. Atverot iekavas, $(500-38)^2$ arī beidzas ar $444$. 
Mazāku nav: ja $x \in [39;49]$, $x^2$ nebeidzas ar $44$. Tātad $(n*100 \pm 38)^2$, 
kur $n \in \{ 1,2,3,4,5 \}$ - pārlasa visiem simtu ciparus. 




# <lo-sample/> LV.NOL.2003.12.1 

Skaitļu virknē pirmais un otrais loceklis abi ir $1$, bet katrs nākošais
vienāds ar abu iepriekšējo summu. Vai ar $5$ dalās šīs virknes  
(a) $20$-ais,  
(b) $2003$-ais loceklis?

<!--
seeAlso=LV.NOL.2000.12.1
questionType=FindAll
-->




## ABC

**#Kongruences** **#PeriodiskaVirkne**  Pirmie $20$ atlikumi: $1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0$, tālāk periods. $F_{20}$ dalīsies ar $5$, bet $F_{2003}$ dos atlikumu $2$, dalot ar $5$. 



# <lo-sample/> LV.NOL.2003.12.5 

Vai eksistē tādas $12$ ģeometriskas progresijas, kas sastāv no reāliem
skaitļiem, ka katrs naturāls skaitlis no $1$ līdz $100$ ieskaitot pieder vismaz
vienai no šīm progresijām?

<!--
concepts=geometric-progression,real-numbers
questionType=ProveDisprove
-->






# <lo-sample/> LV.NOL.2004.7.1 

Kādu mazāko daudzumu no skaitļiem $1; 2; 3; \ldots; 14; 15$ var izsvītrot, 
lai katru divu atlikušo summa būtu salikts skaitlis?

<small>

* topic:BipartiteGraphs
* topic:PrimesDistribution
* topic:InvariantParity

</small>

<!--
concepts=composite-numbers
questionType=FindOptimal
-->



## ABC
 
**#DirihlēPrincips** **#Paritāte** **#Pirmskaitļi** Var svītrot $7$ pāru skaitļus. Mazāk nevar, jo jāizjauc $7$ pāri $(1,12)$ utt. 


# <lo-sample/> LV.NOL.2004.8.1 

Kādu mazāko daudzumu no naturāliem skaitļiem $1;2;3;\ldots;14;15$ var izsvītrot, 
lai atlikušos varētu sadalīt divās grupās ar īpašību: 
vienas grupas visu skaitļu reizinājums vienāds ar otras grupas visu skaitļu reizinājumu?

<small>

* topic:CanonicalFactorization

</small>

<!--
questionType=FindOptimal
seeAlso=LV.NOL.2003.8.3
-->




## ABC
 
**#EiklīdaLemma** Jāsvītro $11,13$ un pa vienam $2$ un $5$ daudzkārtnim ($10$). $3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 \cdot 12 = 1 \cdot 2 \cdot 8 \cdot 9 \cdot 14 \cdot 15$




# <lo-sample/> LV.NOL.2004.8.2 

Ir zināms, ka skaitļa $2^{200}$ decimālajā pierakstā ir $61$ cipars. 
Cik daudziem no skaitļiem $2^1; 2^2; 2^3; \ldots; 2^{199}; 2^{200}$ 
decimālais pieraksts sākas ar ciparu $1$?

<small>

* topic:DecimalNotationDigits
* topic:DefiningRecurrentSequences

</small>

<!--
questionType=FindCount
seeAlso=[Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law)
seeAlso=[Ideal Voting](https://meduza.io/feature/2017/01/13/itogi-vyborov-v-gosdumu-okazalis-slishkom-idealnymi)
seeAlso=LV.NOL.2005.8.1
-->




## Grupēšana pēc ciparu skaita

* Visas divnieku pakāpes var grupēt pēc ciparu skaita
* Katrā grupā (izņemot viencipara sk.) tieši viena pakāpe sākas ar "1". 



# <lo-sample/> LV.NOL.2004.9.2 

Dots, ka $x$ – naturāls skaitlis. 
Kāds lielākais daudzums no skaitļiem
$$x;\; x + 2;\; x + 4;\; x + 6;\; x + 8$$
var vienlaicīgi būt pirmskaitļi?



# <lo-sample/> LV.NOL.2004.9.4 

Uz tāfeles uzrakstīti $2004$ skaitļi; viens no tiem ir $1$. 
Ar vienu gājienu atļauts
nodzēst vienu skaitli un tā vietā uzrakstīt skaitli 
$a + b - c$, kur $a$, $b$ un $c$ – kaut
kādi trīs no nenodzēstajiem skaitļiem. Vai, atkārtojot 
šādus gājienus vairākas
reizes, var panākt, lai uz tāfeles vienlaicīgi 
būtu uzrakstīti $2004$ skaitļi, kas
visi vienādi ar $1$?




# <lo-sample/> LV.NOL.2004.10.2 

Naturālu skaitli sauc par palindromu, ja tā decimālais
pieraksts ir simetrisks.
Piemēram, palindromi ir $11$; $505$; $4774$ utt.
Visi palindromi, sākot ar $11$, izrakstīti 
virknē augošā secībā. Kāda var būt
blakus uzrakstītu palindromu starpība, ja zināms, 
ka tā ir pirmskaitlis?

<!--
concepts=palindrome
-->




# <lo-sample/> LV.NOL.2004.11.2 

Atrast mazāko tādu naturālu skaitli $n$, $n > 1$, 
ka katram veselam $x$ skaitlis $x^n  - x$
dalās ar $10$.




# <lo-sample/> LV.NOL.2004.12.1 

Skaitļu virknē $1; 1; 2; 3; 5; \ldots$ katrs loceklis, sākot ar trešo, vienāds ar abu
iepriekšējo locekļu summu. Noskaidrot, vai ar $6$ dalās

1. virknes $24$-ais loceklis,
2. virknes $2004$-ais loceklis.

<!--
seeAlso=LV.NOL.2000.12.1
-->






# <LO-REFFF/> LV.NOL.2005.7.1 


Kādu mazāko daudzumu no skaitļiem   
$1;2;3;\ldots;12;13$ var izsvītrot, lai 
katru divu atlikušo summa būtu salikts skaitlis? 



<!--
mainEntry=LV.NOL.2003.7.4
-->







# <lo-sample/> LV.NOL.2005.7.4 

Naturālu skaitli $n$ sauc par īpašu, ja tas ir vienāds ar četru savu dažādu 
dalītāju summu.  
(a) atrodiet kaut vienu īpašu skaitli,  
(b) pierādiet, ka īpašu skaitļu ir bezgalīgi daudz,  
(c) pierādiet, ka visi īpaši skaitļi ir pāru skaitļi. 

<small>

* topic:IntegerFactorization
* topic:NumTheoryExtremeElement
* topic:ModularParity

</small>

<!--
seeAlso=[Semiperfect number](https://en.wikipedia.org/wiki/Semiperfect_number)
-->




## Dalītāju izteikšana
 
**(a,b)** $n=n/2+n/3+n/7+n/42$; tātad $42k$ ir īpaši. 

**Nav nepāru īpašu skaitļu:**

* Pat "ekstrēmākie" dalītāji ir par mazu:
$$\frac{n}{3}+\frac{n}{5}+\frac{n}{7}+\frac{n}{9} < n.$$
* Nepāru skaitļiem visi dalītāji ir nepāru; 
četru nepāru summa nevar būt pāru.




# <lo-sample/> LV.NOL.2005.8.1 

Ir zināms, ka skaitļa $2^{100}$ decimālajā pierakstā ir $31$ cipars. 
Cik daudziem no skaitļiem $2^1; 2^2; 2^3; \ldots; 2^{99}; 2^{100}$ 
decimālais pieraksts sākas ar ciparu $1$?


<small>

* topic:DecimalNotationDigits
* topic:DefiningRecurrentSequences

</small>

<!--
seeAlso=LV.NOL.2004.8.2
-->



## ABC
 
**#Nevienādība** Katram ciparu skaitam, izņemot 1-cipara sk., ir tieši viens $2^n$, kas sākas ar ciparu $1$.



# <lo-sample/> LV.NOL.2005.8.3 

Andris iedomājās patvaļīgu naturālu skaitli $n$. Juris ar vienu gājienu 
var pateikt Andrim piecus dažādus naturālus skaitļus
$x_1,x_2,x_3,x_4,x_5$, un Andris pateiks Jurim **vienu**
no skaitļiem $nx_1$, $nx_2$, $nx_3$, $nx_4$, $nx_5$ (bet nepaskaidros, 
**kura** reizinājuma vērtību viņš saka). 
Ar kādu mazāko jautājumu skaitu Juris var noteikti noskaidrot $n$? 

<small>

* topic:GcdAndLcm
* topic:PrimesInfinityProof
* topic:CanonicalFactorization

</small>

<!--
genre=games
questionType=FindOptimal
-->




## Ar 1 gājienu nepietiek
 
Pirmajā gājienā Andris var atbildēt ar tādu $x$, 
kas dalās ar vairākiem $x_i$. 



## Ar 2 gājieniem pietiek

Otrajā gājienā Juris nosauc 5 pirmskaitļus $p_i > x_1$ (kur $x_1$ - 
Andra pirmais nosauktais skaitlis). 
Atkarībā no tā, ar kuru pirmskaitli dalās Andra atbilde $x_2$, 
var noteikt $n$.



# <lo-sample/> LV.NOL.2005.9.2 

Kāda var būt četru tādu divciparu pirmskaitļu summa, 
kas sastādīti no cipariem $1$;
$2$; $3$; $4$; $5$; $6$; $7$; $9$, 
izmantojot katru no tiem tieši vienu reizi?



# <lo-sample/> LV.NOL.2005.9.4 

Vai eksistē tādi $6$ skaitļi, ka, aprēķinot visas 
iespējamās to summas pa diviem,
iegūst visus naturālos skaitļus no $1$ līdz 
$15$ ieskaitot?



# <lo-sample/> LV.NOL.2005.9.5 

Ciparu virkni veido sekojoši: tās pirmie cipari 
ir $1; 2; 3; 4$, bet katrs nākošais
vienāds ar četru iepriekšējo summas pēdējo ciparu. 
(Tātad virkne ir $1; 2; 3; 4; 0; 9; 6; 9; \ldots$)

1. Vai virknē kādreiz pēc kārtas parādīsies 
cipari $2; 0; 0; 5$ tieši šādā secībā?
2. Vai virknē kādreiz pēc kārtas citur nekā 
sākumā parādīsies cipari $1; 2; 3; 4$?




# <lo-sample/> LV.NOL.2005.10.1 

Sākumā uz tāfeles uzrakstīti naturāli skaitļi no 
$1$ līdz $10$, katrs vienu reizi. Ar vienu
gājienu atļauts izvēlēties jebkuru uz tāfeles 
uzrakstītu skaitļu grupu, nodzēst to un
vietā uzrakstīt atlikumu, kādu dod nodzēsto 
skaitļu summa, dalot ar $3$. Pēc
vairākiem šādiem gājieniem uz tāfeles palika 
divi skaitļi; viens no tiem bija $8$.
Kāds varēja būt otrs skaitlis?




# <lo-sample/> LV.NOL.2005.10.5 

Uz papīra lapas uzrakstīti vairāki dažādi naturāli 
skaitļi; neviens no tiem
nepārsniedz $100$. Zināms, ka:

1. $1$ un $100$ ir uzrakstīti uz lapas,
2. ja $n$ uzrakstīts uz lapas un $n \neq 1$, 
tad var atrast vai nu tādu uz lapas uzrakstītu
skaitli $x$, ka $n=2x$, vai divus tādus uz lapas
uzrakstītus skaitļus $x$ un $y$, ka $n=x+y$.

Kāds mazākais daudzums skaitļu var būt uzrakstīti 
uz lapas?




# <lo-sample/> LV.NOL.2005.11.1 

Aprēķināt $\sqrt{2005 \cdot 2003 \cdot 1999 \cdot 1997 + 36}$. 



# <lo-sample/> LV.NOL.2005.11.3 

Naturālu skaitli $n$ sauksim par līdzsvarotu, ja tā visus naturālos dalītājus 
(ieskaitot $1$ un pašu $n$) var sadalīt trīs daļās ar vienādām summām.

1. atrast kaut vienu līdzsvarotu skaitli,
2. pierādīt, ka līdzsvarotu skaitļu ir bezgalīgi daudz.




# <lo-sample/> LV.NOL.2005.12.5 

Trijstūra malu garumi izsakās ar pirmskaitļiem. Vai tā laukums var būt naturāls
skaitlis? (Malas mēra metros, laukumu – kvadrātmetros.)









# <lo-sample/> LV.NOL.2006.7.4/LV.NOL.2007.7.4


Kuri naturālie skaitļi ir vienādi ar trīs savu dažādu pozitīvu dalītāju summu?


<small>

* topic:IntegerFactorization
* topic:NumTheoryInequalityLargeIntervals

</small>



## Pāreja uz daļām
 
* $n = (n/2) + (n/3) + (n/6)$ jeb $1 = 1/2+1/3+1/6$. (Tātad der visi, kas
dalās ar $6$.)
* Citādi skaitli $1$ sadalīt dažādu daļu summā nevar - var pamatot ar nevienādībām.



# <lo-sample/> LV.NOL.2006.8.1 


Ir zināms, ka visiem $x$ pastāv vienādība  
$$x^4 + 64 = (x^2 - 4x + 8)\cdot A,$$
kur $A$ ir izteiksme, kas izveidota no $x$ un naturāliem skaitļiem ar 
saskaitīšanas, atņemšanas un reizināšanas operāciju palīdzību. 
Atrast $A$. 


<small>

* topic:CompletingSquare

</small>



## ABC
 
**#AlgebriskaIdentitāte** Kreisajai pusei var pieskaitīt un atņemt $16x^2$, tad atdalīt pilno kvadrātu.



# <lo-sample/> LV.NOL.2006.8.3 

Vai var izrakstīt rindā visus naturālos skaitļus no $1$ līdz $2006$ ieskaitot 
katru vienu reizi tā, lai katru $3$ pēc kārtas uzrakstīto skaitļu summa dalītos ar $4$. 


<small>

* topic:PeriodicRemainders
* topic:CongruenceClasses

</small>



## ABC
 
**#Invariants** **#PeriodiskaVirkne** Atlikumi, dalot ar $4$ šādā virknē atkārtosies ar periodu $3$, t.i.\ viens no atlikumiem neparādīsies vispār.



# <lo-sample/> LV.NOL.2006.9.4 

Kuri naturālie skaitļi $x$ 
apmierina vienlaicīgi visas sekojošās prasības:
\begin{itemize}
1. $x \leq 2006$,
2. $x$ dalās ar $5$,
3. $x+1$ dalās ar $7$,
4. $x+2$ dalās ar $9$,
5. $x+3$ dalās ar $11$?
\end{itemize}



# <lo-sample/> LV.NOL.2006.9.5 

Gunārs un Dzintars pamīšus raksta uz 
tāfeles pa vienam naturālam skaitlim,
kas nepārsniedz $1000$. Sāk 
Dzintars, uzrakstot skaitli $1$. 
Neviens jau uzrakstīts
skaitlis netiek nodzēsts; nevienu skaitli 
nedrīkst rakstīt otrreiz.
Ja kaut kāds skaitlis $x$ jau ir uz tāfeles, 
tad ar kārtējo gājienu drīkst uzrakstīt
vai nu $x+1$, vai $2x$ (ja izvēlētais 
rakstāmais skaitlis nepārsniedz $1000$). 
Tas, kurš uzraksta $1000$, uzvar. 
Kurš no zēniem uzvar, pareizi spēlējot?



# <lo-sample/> LV.NOL.2006.10.1 

Atrodiet lielāko $12$-ciparu skaitli 
ar īpašību: katri divi blakus uzrakstīti cipari
veido pirmskaitli, un visi šie $11$ pirmskaitļi ir dažādi.




# <lo-sample/> LV.NOL.2006.11.1 

Doti $6$ viens otram sekojoši naturāli skaitļi. 
Pierādīt: eksistē pirmskaitlis, ar kuru
dalās tieši viens no šiem skaitļiem.




# <lo-sample/> LV.NOL.2006.11.5 

Andrim, Dzintaram un Gunāram ir liels daudzums zīmīšu. Uz katras zīmītes ir
uzrakstīts viens no skaitļiem $2$; $3$; $4$; $5$; $6$; $7$; $8$. 
Maija uzlīmēja katram no viņiem uz
pieres pa vienai zīmītei. Katrs zēns redz zīmītes uz abu draugu pierēm, bet neredz
zīmīti uz savas pieres. Maija, visiem dzirdot, paziņoja: "Ne visi skaitļi uz jūsu
pierēm ir dažādi. Visu triju skaitļu reizinājums ir vesela skaitļa kvadrāts."
Vai zēni nesarunājoties var noskaidrot, kādi skaitļi ir uz viņu pierēm?



# <lo-sample/> LV.NOL.2006.12.3 

Kuriem pirmskaitļiem p piemīt īpašība: skaitlim  $p^2 + 11$
ir mazāk nekā $11$
naturālu dalītāju?



# <lo-sample/> LV.NOL.2006.12.5 

Pa apli izvietotas $n$ spuldzes; sākotnēji tās visas ir izslēgtas. Viena spuldze
apzīmēta ar $S$. Atrodam visus skaitļa $n$ pozitīvos dalītājus, ieskaitot $1$ un $n$.
Katram šādam dalītājam $d$ veicam sekojošu operāciju: mainām katras $d$-tās
spuldzes stāvokli (sākot ar spuldzi $S$), pavisam izdarot $n$ maiņas.
Kurām $n$ vērtībām, beidzot šīs darbības, visas spuldzes būs ieslēgtas?

<!--
seeAlso=LV.NOL.2007.12.2
-->










# <lo-sample/> LV.NOL.2007.7.1 


Kurus naturālos skaitļus $n$ var izsacīt formā ${\displaystyle n=\frac{x}{y}}$, 
kur $x = a^5$, $y = b^3$, $a$ un $b$ – naturāli skaitļi? 


<small>

* topic:BezoutIdentity
* topic:CanonicalFactorization
* topic:StandardIdentities

</small>

<!--
seeAlso=LV.NOL.2008.7.1
seeAlso=LV.NOL.2009.7.1
-->



## ABC
 
**#DalījumsPirmreizinātājos** **#LineārasKongruences** Katru pirmskaitļa pakāpi $p^k$ skaitļa $n$ sadalījumā var izteikt $p^{5c}/p^{3d}$ kaut kādiem naturāliem $c,d$.
**#AlgebriskaIdentitāte** $n = n^{10}/n^{9} = (n^2)^5/(n^3)^3$. 



# <lo-sample/> LV.NOL.2007.8.4 


Atrast mazāko naturālo skaitli, kas dalās ar katru no kaut kādiem $12$ pēc kārtas
ņemtiem naturāliem skaitļiem.


<small>

* topic:MultiplesInInterval
* topic:GcdAndLcm

</small>



## Abi novērtējumi

Apzīmējam ar $M$ mazāko skaitli, kas dalās ar $12$ pēc kārtas sekojošiem $\mathbb{N}$ 
elementiem.

* Skaitlis, kas dalās ar $k$, $k+1$, $\ldots$, $k+11$, dalās arī ar $1,2,\ldots,12$. Šo skaitļu mazākais kopīgais dalāmais ir $8\cdot 9\cdot 5\cdot 7\cdot 11 = 27720$, tātad $M \geq 27720$. 
* Tieši $M =  8\cdot 9\cdot 5\cdot 7\cdot 11 = 27720$ dalās ar $12$ pēc kārtas ņemtiem skaitļiem (no $1$ līdz $12$). Tātad $M \leq 27720$.




# <lo-sample/> LV.NOL.2007.9.5 

Kvadrāts sastāv no $10 \times 10$ 
rūtiņām. Katrā rūtiņā ierakstīts 
naturāls skaitlis, kas
nepārsniedz $10$. Ja divām rūtiņām ir kopēja 
mala vai kopējs stūris, tad tajās
ierakstīto skaitļu lielākais kopīgais dalītājs ir $1$.

1. pierādīt, ka kāds skaitlis ierakstīts 
vismaz $15$ rūtiņās,
2. pierādīt, ka kāds skaitlis ierakstīts 
vismaz $17$ rūtiņās.




# <lo-sample/> LV.NOL.2007.10.3 

Sauksim naturālu skaitli $n > 1$ par labu, 
ja visus tā pozitīvos dalītājus var
sadalīt divās daļās, kuru summas ir vienādas.

1. atrodiet kaut vienu labu skaitli, kas lielāks 
par $10$,
2. vai eksistē labi skaitļi, kas lielāki 
par $20072007$?




# <lo-sample/> LV.NOL.2007.11.1 

Atrisināt naturālos skaitļos vienādojumu $x^2 + 3x = 2^y$. 



# <lo-sample/> LV.NOL.2007.12.3 

Kādiem naturāliem skaitļiem $n$ vienlaicīgi piemīt sekojošas īpašības:

1. $n-1$ un $n+1$ ir pirmskaitļi,
2. skaitļa n visu naturālo dalītāju summa (ieskaitot $1$ un $n$) ir $2n$?










# <lo-sample/> LV.NOL.2008.7.1 

Kurus naturālos skaitļus $n$ var izsacīt formā $n=\frac{x}{y}$, kur $x = a^3$, 
$y = b^4$, $a$ un $b$ – naturāli skaitļi? 


<small>

* topic:BezoutIdentity
* topic:CanonicalFactorization
* topic:StandardIdentities

</small>

<!--
seeAlso=LV.NOL.2007.7.1
seeAlso=LV.NOL.2009.7.1
-->



## ABC
 
**#DalījumsPirmreizinātājos** **#LineārasKongruences** Katru pirmskaitļa pakāpi $p^k$ skaitļa $n$ sadalījumā var izteikt $p^{3c}/p^{4d}$ kaut kādiem naturāliem $c,d$.
**#AlgebriskaIdentitāte** $n = n^{9}/n^{8} = (n^3)^3/(n^2)^4$.  



# <lo-sample/> LV.NOL.2008.7.3 


Sporta klubā sapulcējušies cīkstoņi un vingrotājas. 
Cīkstoņu vidējais svars ir $84$ kg; vingrotāju vidējais svars ir $54$ kg; 
visu sportistu vidējais svars ir $71$ kg. 
Pierādīt, ka cīkstoņu skaits dalās ar $17$. 

<small>

* topic:BaricenterCoordinates
* topic:NumTheoryInequalityMethod
* topic:IntegerFactorization

</small>



## ABC
 
**#MasuCentrs** **#LKD** Lai $71$ būtu līdzsvara punkts starp $84k$ un $54m$, attiecībai $k/m$ jābūt $17/13$ un $\operatorname{LKD}(13,17)=1$.



# <lo-sample/> LV.NOL.2008.8.1 


Sešciparu naturālu skaitli sauc par laimīgu, ja kaut kādu $3$ ciparu summa vienāda 
ar pārējo $3$ ciparu summu. Divi viens otram sekojoši skaitļi ir laimīgi. 
Pierādīt, ka viens no tiem dalās ar $10$.


<small>

* topic:SequenceGaps
* topic:InvariantParity

</small>



## ABC
 
**#Decimālpieraksts** **#Paritāte** Palielinot skaitli par $1$ bez pārnesuma, tā ciparu summas paritāte mainās par $1$.  



# <lo-sample/> LV.NOL.2008.9.1 

Atrodiet vismaz $5$ dažādus pirmskaitļus, ar kuriem dalās skaitlis $3^{32} - 2^{32}$. 



# <lo-sample/> LV.NOL.2008.10.1 

Atrodiet mazāko naturālo skaitli, ko var izsacīt gan kā $15$, gan kā $16$, gan kā 
$17$ pēc kārtas ņemtu naturālu skaitļu summu. 



## ABC

**#AritmētiskaProgresija** **#MKD** Mazākais skaitlis, kas dalās ar $15$, $8$ un $17$ ir $2040$.



# <lo-sample/> LV.NOL.2008.11.4 

Apzīmējam $f(n) = 1^n + 2^n + 3^n + 4^n$, $n=1;2;3;\ldots$. Ar kādu lielāko 
daudzumu nuļļu var beigties skaitlis $f(n)$?



# <lo-sample/> LV.NOL.2008.12.2 

Kādiem naturāliem skaitļiem $n$ vienlaicīgi piemīt sekojošas īpašības:

1. $n-1$ un $n+1$ ir pirmskaitļi, 
2. skaitļa $n$ visu naturālo dalītāju summa (ieskaitot $1$ un $n$) ir $2n$?







# <lo-sample/> LV.NOL.2009.7.1 


Kurus naturālos skaitļus $n$ var izsacīt formā ${\displaystyle n=\frac{x}{y}}$, 
kur $x = a^3$, $y = b^5$, $a$ un $b$ – naturāli skaitļi? 


<small>

* topic:BezoutIdentity
* topic:CanonicalFactorization
* topic:StandardIdentities

</small>

<!--
seeAlso=LV.NOL.2007.7.1
seeAlso=LV.NOL.2008.7.1
-->



## ABC
 
**#DalījumsPirmreizinātājos** **#LineārasKongruences** 
Jebkuru pirmskaitļa pakāpi $p^v$ var izteikt kā $(p^k)^3/(p^m)^5$. 
**#AlgebriskaIdentitāte** $n = n^{21}/n^{20} = (n^7)^3/(n^4)^5$. 



# <lo-sample/> LV.NOL.2009.7.3 

Naturālam skaitlim $a$ ir tieši $4$ dalītāji, bet naturālam skaitlim $b$ –
tieši $6$ dalītāji. Pierādiet, ka reizinājumam $ab$ ir **vismaz** $9$ dalītāji. 
Vai var gadīties, ka šim reizinājumam ir **tieši** $9$ dalītāji?  
*Piezīme.* Apskatām tikai tādus dalītājus, kas paši ir naturāli skaitļi. 
Pie skaitļa dalītājiem pieskaita gan viņu pašu, gan vieninieku.)


<small>

* topic:DivisorNumberAndSum
* topic:ExhaustionMethod

</small>



## Dalītāju skaita noteikšana

* Tieši četri dalītāji var būt tādam $a$, kas ir vai nu 
$p^3$ vai $pq$. ($p,q$ - pirmskaitļi)
* Līdzīgi $b$ ir $r^5$ vai $r^2s$. ($r,s$ - pirmskaitļi)
* Ja $p=r$, var dabūt $ab = p^3p^5 = p^8$.



## Gadījumu pārlase

Mazāk kā $9$ dalītāji var rasties $3$ veidos:

* $p^a$, kur $a+1 < 9$,
* $p^aq^b$, kur $(a+1)(b+1) < 9$,
* $p^aq^br^c$, kur $(a+q)(b+1)(c+1) < 9$. 

Neviens no šiem gadījumiem neatbilst mūsu nosacījumam.



# <lo-sample/> LV.NOL.2009.8.1 


Tabulā (sk. zīmējumu) Katrīnai jāizvēlas $4$ rūtiņas tā, ka katrā rindā un 
katrā kolonnā tika izvēlēta tieši viena rūtiņa. Pierādiet: neatkarīgi no tā, kuras 
$4$ rūtiņas saskaņā ar šiem noteikumiem Katrīna izvēlēsies, tajās ierakstīto skaitļu summa būs $64$. 

![tabula](LV.NOL.2009.8.1.png)

<small>

* topic:LinearSystemsApplications
* topic:CongruenceClasses

</small>



## ABC
 
**#DalīšanaArAtlikumu** **#SummasPārkārtošana** Sadala divu tabuliņu summā: vienā $1\ldots 7$, otrā $8k$. Vienmēr $(1+3+5+7) + (0+8+16+24) = 64$.





# <lo-sample/> LV.NOL.2009.8.3 

Atrodiet skaitļa $113^{113} - 19^{19}$ pēdējo ciparu. 

<small>

* topic:PeriodicRemainders
* topic:CongruenceClasses

</small>




## ABC
 
**#PeriodiskaVirkne** **#PēdējieCipari** $113$ pakāpes mainās ar periodu $(1,3,9,7)$, bet $19$ pakāpes ar periodu $(1,9)$. 



# <lo-sample/> LV.NOL.2009.9.2 

Kuri četrciparu naturāli skaitļi vienādi ar savu divu pēdējo ciparu 
veidotā naturālā skaitļa kvadrātu?



# <lo-sample/> LV.NOL.2009.10.1 

Atrodiet mazāko naturālo skaitli, kuru var izsacīt gan kā 
$11$, gan $12$, gan kā $13$ pēc kārtas ņemtu naturālu skaitļu summu. 



# <lo-sample/> LV.NOL.2009.10.3 

Dots, ka $a$ un $b$ ir naturāli skaitļi, $a^2$ dalās ar $b$ un 
$b^2$ dalās ar $a$. Pierādīt, ka $(a+b)^3$ dalās ar $a \cdot b$. 
Vai noteikti $(a + b)^2$ dalās ar $a \cdot b$? 




# <lo-sample/> LV.NOL.2009.11.2 

Atrisināt veselos skaitļos vienādojumu ${\displaystyle \frac{x^2}{2} + \frac{5}{y} = 7}$. 



# <lo-sample/> LV.NOL.2009.12.2 

Dots, ka $p$ ir pirmskaitlis un $n = \left( p^2 - 1 \right) \left( p^2 - 4 \right) + 9$. 
Kāda ir mazākā iespējamā $n$ ciparu summa? Kuriem $p$ tā tiek sasniegta?



# <lo-sample/> LV.NOL.2010.11.1 

Dots, ka $p$ un $q$ ir naturāli skaitļi un kvadrātvienādojuma 
$x^2 + px + q = 0$ saknes ir $x_1$ un $x_2$. Pierādīt, ka 

1. $x_1^2 + x_2^2$, 
2. $x_1^8 + x_2^8$, 
3. $x_1^5 + x_2^5$

ir vesels skaitlis. 









# <lo-sample/> LV.NOL.2010.7.3 


Cik ir tādu naturālu skaitļu $x$ robežās no $1$ līdz $2010$ ieskaitot, ka
$(x+1)(x+2)(x+3)$ dalās ar $343$? 

<small>

* topic:MultiplesInInterval
* topic:FactorizationAndDivisibility

</small>



## ABC
 
**#Dalāmība** **#DalījumsPirmreizinātājos** Katrs septītais skaitlis dalās ar $7$, tādēļ $x+1$, $x+2$ vai $x+3$ dalās ar $7^3 = 343$.



# <lo-sample/> LV.NOL.2010.8.1 


Kuru no skaitļiem 
$$102^2 \cdot 103^2 \cdot \ldots \cdot 199^2\;\;\mbox{un}\;\;(102^2 - 1)(103^2 - 1)\ldots(199^2-1)$$
sadalot pirmskaitļu reizinājumā, iegūst vairāk **dažādu** pirmskaitļu? Par cik vairāk?  
*Piezīme.* $24 = 2 \cdot 2 \cdot 2 \cdot 3$ satur divus dažādus pirmskaitļus; $2$ un $3$.

<small>

* topic:StandardIdentities
* topic:PrimesDistribution
* topic:TelescopicSums

</small>



## ABC
 
**#AlgebriskaIdentitāte** **#Pirmskaitļi** Dala reizinātājos $102^2 - 1=(102-1)(102+1)$ utt., īsina. Labajā pusē par pirmreizinātāju $101$ vairāk.  



# <lo-sample/> LV.NOL.2010.8.3 


Četrciparu skaitlim pārlika ciparus citā kārtībā. 
Pierādīt: sākotnējā un iegūtā skaitļa starpība dalās ar $9$. 

<small>

* topic:DivisibilityRulesForRemainders
* topic:NotationManipulate

</small>



## ABC
 
**#DalāmībaAr3Un9** **#DalīšanaArAtlikumu** $n$ atlikums dalot ar $9$ (arī pārkārtotā $n$ atlikums) vienādi ar $n$ ciparu summas atl.


# <lo-sample/> LV.NOL.2010.9.1 

Atrodiet kaut vienu kvadrātvienādojumu ar veseliem koeficientiem, 
kam viena no saknēm ir 

1. $\sqrt{2} + 1$
2. $\sqrt{7 + 4\sqrt{3}}$

*Piezīme.* Katrā uzdevuma daļā runā par **citu** kvadrātvienādojumu.



# <lo-sample/> LV.NOL.2010.9.5 

Atrisināt naturālos skaitļos vienādojumu sistēmu 
${\displaystyle \left\{ 
\begin{array}{rcl}
x^2 + y & = & z^2\\
y^2 + x & = & t^2
\end{array}
\right.}$





# <lo-sample/> LV.NOL.2010.10.2

Dots, ka $a$ un $b$ ir naturāli skaitļi, $a^2$
dalās ar $b$ un $b^2$ dalās ar $a$. 
Pierādīt, ka $(a-b)^3$
dalās ar $a\cdot{}b$. Vai noteikti
$(a-b)^2$ dalās ar $a\cdot{}b$?

<small>

* topic:AdvancedIdentities
* topic:DivisibilityProperties
* topic:DivisibilityProperties

</small>



## Algebrisks pārveidojums

$$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

Katrs no $4$ saskaitāmajiem dalās ar $ab$:

* $\frac{a^3}{ab} = \frac{a^2}{b}$ (zināms, ka dalās)
* $\frac{3a^2b}{ab} = 3a$ un $\frac{3ab^2}{ab}=3b$ (abus var saīsināt)
* $\frac{b^3}{ab} = \frac{b^2}{a}$ (zināms, ka dalās)



## Pretpiemērs (der ļoti daudz kas)

* Ja $a=9$, $b=3$, tad $(a-b)^2 = 36$ nedalās ar $ab=27$.
* Ja $a=18$, $b=12$, tad $(a-b)^2 = 36$ nedalās ar $ab=216$.




# <lo-sample/> LV.NOL.2010.10.4

Atrisināt naturālos skaitļos vienādojumu $x^3 = y! + 2$.

<small>

* topic:CountingObjects
* LTopic:LTEquationsNumTheory
* topic:StandardIdentities
* topic:ValuationProperties
* topic:ValuationProperties
* topic:ModularArithmeticContradiction

</small>




## Faktoriālu un pilno kubu tabulas

| $x$  | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $x^3 | 1    | 8    | 27   | 64   | 125  | 216  | 343  | 512  | 729  | 1000 |


| $y$    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8     | 
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- |
| $y!    | 1    | 2    | 6    | 24   | 120  | 720  | 5040 | 40320 |  
| $y!+2$ | 3    | 4    | 8    | 26   | 122  | 722  | 5042 | 40322 |


* Redzam, ka $2^3 = 3!+2$ (ja $x=2, y=3$). 
* Vai ir citas saknes, kur $y>3$? 
* Aplūkojam $x$ paritāti. Vienīgā iespēja: $x$ ir pāru skaitlis: $x=2k$.

    - Tad $(2k)^3 = y!+2$ jeb $8k^3 = y! + 2$.
    - Kreisā puse dalās ar $8$, bet labā (pie $y>3$) dod atlikumu $2$, dalot ar $8$.




# <lo-sample/> LV.NOL.2010.11.2 

Atrisināt veselos skaitļos vienādojumu 
${\displaystyle \frac{x^2}{2} + \frac{5}{y} = 7}$. 



# <lo-sample/> LV.NOL.2010.12.1 

Dots, ka  $n$ – naturāls skaitlis, kas nedalās ar $5$. 
Kāda ir mazākā iespējamā ciparu summa skaitlim 
${\displaystyle \left( n^2 - 1 \right)\left( n^2 - 4 \right) + 7}$? 
Pie kādām $n$ vērtībām tā tiek sasniegta?






# <lo-sample/> LV.NOL.2011.7.1 

Atrodiet skaitļa $1^2 + 2^2 + \ldots + 99^2$ pēdējo ciparu. 

<small>

* topic:SequencePeriodicity
* topic:CongruenceClasses

</small>



## ABC
 
**#Simetrija** **#PēdējieCipari** $10$ grupas: $\left( 1^2 + 2^2 + \ldots + 8^2 + 9^2 \right)$ katra ar pēdējo ciparu $(1+4+9+6)\cdot 2 + 5 = 5$.




# <lo-sample/> LV.NOL.2011.7.2 


Cik ir tādu naturālu skaitļu $n$ no $1$ līdz $2011$ ieskaitot, 
ka skaitlis $(n+1)(n+2)(n+3)$ dalās ar $125$. 


<small>

* topic:MultiplesInInterval
* topic:FactorizationAndDivisibility

</small>



## ABC
 
**#Dalāmība** **#DalījumsPirmreizinātājos** Katrs piektais skaitlis dalās ar $5$, t.i. $n+1$, $n+2$ vai $n+3$ jādalās ar $5^3 = 125$. 



# <lo-sample/> LV.NOL.2011.8.1 

Piecciparu skaitlis $B$ ir iegūts no mazāka piecciparu skaitļa $A$, 
samainot vietām tā ciparus. Pierādīt, ka $B-A$ dalās ar $9$.


<small>

* topic:NotationManipulate
* topic:DivisibilityRulesForRemainders

</small>



## ABC

**#DalāmībaAr3Un9** **#DalāmībaAr3Un9** **#DalīšanaArAtlikumu** $A$ atlikums dalot ar $9$ (arī $B$ atlikums) vienādi ar $A$ ciparu summas atl.



# <lo-sample/> LV.NOL.2011.9.4 

Pierādīt, ka nav tādu naturālu skaitļu $a$, $x$, $y$ un $z$, ka 
$7^a = 7^x + 7^y + 7^z$. 



# <lo-sample/> LV.NOL.2011.10.3 

Ar $\lfloor a \rfloor$ apzīmējam lielāko veselo skaitli, kas nepārsniedz $a$. 
Atrisināt pozitīvos skaitļos vienādojumu 
${\displaystyle x \cdot \left\lfloor x \cdot \lfloor x \rfloor \right\rfloor = 41}$. 




# <lo-sample/> LV.NOL.2011.11.4 

Zināms, ka $a$ un $b$ ir naturāli skaitļi, pie tam $a^b + 1$ dalās ar $21$. 
Kāda ir mazākā iespējamā summas $a+b$ vērtība? 



# <lo-sample/> LV.NOL.2011.12.3 

Naturālu skaitli sauksim par *fantastisku*, ja tas ir vienāds ar sava kvadrāta ciparu 
reizinājumu. Piemēram, $1$ ir fantastisks (jo $1^2 = 1$ un $1 = 1$), bet 
$4$ – nē (jo $4^2 = 16$, bet $1 \cdot 6 = 6 \neq 4$). 
Pierādīt, ka visi nepāra skaitļi, kas lielāki par $1$, nav fantastiski. 








# <lo-sample/> LV.NOL.2012.7.1 

Ar naturālu skaitli var veikt divu veidu operācijas:

1. reizināt ar $7$
2. nodzēst skaitļa lielāko (vienu no lielākajiem, ja tādi ir vairāki) ciparu. 

Vai ar šādām operācijām no skaitļa $9$ var iegūt skaitli $27$, 
atkārtojot tās vairākas reizes jebkādā secībā?

<small>

* topic:GraphAlgorithms

</small>



## Koka apstaigāšana, lai meklētu
 
$9 \rightarrow 63 \rightarrow 441 \rightarrow 41 \rightarrow 287 \rightarrow 27$. 



# <lo-sample/> LV.NOL.2012.7.4 

Pierādīt, ka $1004041$ nav pirmskaitlis. 


<small>

* topic:DivisibilityRulesOther

</small>



## Dalāmības pazīme ar 101
 
Ar $101$ dalās skaitļi, kam apaļajās un kvadrātiekavās liktās summas atšķiras par $101k$: $[01](00)[40](41)$.



# <lo-sample/> LV.NOL.2012.8.1 

Skaitli $3999991$ uzrakstīt kā divu veselu skaitļu reizinājumu tā, 
lai katrs no reizinātājiem ir lielāks nekā $1$. 

<small>

* topic:StandardIdentities

</small>



## Kvadrātu starpības formula
 
$3999991 = 4000000 - 9 = 2000^2 - 3^2$. 



# <lo-sample/> LV.NOL.2012.8.3 

Vai naturāla skaitļa ciparu reizinājums var būt skaitlis $\overline{aabbcc}$? 
(Pieraksts $\overline{kmn}$ nozīmē, ka skaitlī ir $k$ simti, $m$ desmiti un 
$n$ vieni.)

<small>

* topic:DivisibilityRuleFor11
* topic:EuclideanLemma

</small>




## Dalāmība ar 11
 
* $\overline{aabbcc}$ dalās ar $11$ jo ciparu summas pāru un nepāru pozīcijās sakrīt. 
* Neviens cipars nav $11$. Tāpēc arī šādu ciparu reizinājums nevar dalīties ar $11$.



# <lo-sample/> LV.NOL.2012.9.4 

Dota skaitļu virkne $1,1,2,5,9,6,\ldots$. Tā tiek veidota pēc likuma: 
virknes pirmie divi locekļi ir $1$, bet katrs nākamais ir vienāds ar divu 
iepriekšējo locekļu kvadrātu summas pēdējo ciparu. 

1. Noteikt, vai šīs virknes $2012$. loceklis ir pāra vai nepāra skaitlis. 
2. Aprēķināt virknes $2012$. locekli. 




# <lo-sample/> LV.NOL.2012.9.5 

Dots naturāls skaitlis $n \geq 3$. Aplūkojam visus naturālos skaitļus no $1$ līdz $n-1$
ieskaitot, kas ir savstarpēji pirmskaitļi ar skaitli $n$. 
Pierādīt, ka šo skaitļu summa dalās ar $n$. 






# <lo-sample/> LV.NOL.2012.10.3

Doti seši pēc kārtas sekojoši naturāli skaitļi. Pierādīt, ka var atrast tādu
pirmskaitli $p$, ka **tieši viens** no dotajiem skaitļiem dalās ar $p$.

<small>

* topic:ArithmeticSeriesGaps
* strategy:contradiction

</small>



# <lo-sample/> LV.NOL.2012.10.4

Ir aprēķinātas skaitļu $2^{2012}$ un $5^{2012}$ vērtības 
un iegūtie skaitļi uzrakstīti viens aiz otra. 
Cik cipari uzrakstīti?




# <lo-sample/> LV.NOL.2013.10.4

Ansītis aprēķināja skaitļu $2^{2013}$ un $5^{2013}$ vērtības 
un iegūtos skaitļus uzrakstīja
vienu aiz otra. Cik cipari uzrakstīti?

<small>

* topic:CountingObjects
* topic:DigitsInOperationResult

</small>


<!--
sameAs=LV.NOL.2012.10.4
-->










# <lo-sample/> LV.NOL.2012.11.1 

Vai eksistē tāds naturāls skaitlis $m$, kura ciparu reizinājums ir vienāds
ar simetrisku 8-ciparu skaitli?  
(Par *simetrisku* sauc skaitli, kas vienādi lasāms no abiem galiem.)

<!--
concepts=palindrome
-->



# <lo-sample/> LV.NOL.2012.11.4 

Atrast augošu aritmētisku progresiju, kuras visi elementi ir 
naturāli skaitļi un kurai piemīt īpašība: neviens tās elements **nav**
naturāla skaitļa $k$-tā pakāpe jebkuram naturālam $k \geq 2$. 



# <lo-sample/> LV.NOL.2012.12.4 

Kādiem pirmskaitļiem $p$ skaitlim $p^2 + 23$ ir tieši četri naturāli dalītāji?



