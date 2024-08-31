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

**#Nevienādība** **#GadījumuPārlase** $x \in [3;4)$. 
Tad $x \lfloor 3x \rfloor = 41$. Trīs gadījumi: $x \cdot 9 = 41$, $x \cdot 10 = 41$, $x \cdot 11 = 41$. Vienīgi $x = 41/11$ der.



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






