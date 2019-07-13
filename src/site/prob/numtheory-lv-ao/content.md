# &nbsp;

<h1 style="font-size:28pt">Skaitļu teorija: LV</h1>

* Skaitļu teorijas olimpiādes (no 2010.g.)
    - LV.NO - novadu olimpiāde (2.posms)
    - LV.VO - valsts olimpiāde (3.posms)
    - <blue>LV.AO - atklātā olimpiāde</blue>



# <lo-sample/> LV.AO.2000.7.1

Dots, ka $a,b,c,d$ – naturāli skaitļi un $ab=cd$. Pierādīt, ka skaitli $a^2 + b^2 + c^2 + d^2$ 
var izsacīt kā divu veselu skaitļu kvadrātu summu. Vai to noteikti var izsacīt kā divu naturālu skaitļu kvadrātu summu?

<small>

* [alg.tra.binom.square](#)

</small>

<!--
questionType=Prove.Other
concepts=square
-->


## Kvadrātu atdalīšana

Pieskaitīt $2ab$ un atņemt tam vienādo $2cd$, atdalīt kvadrātus. $1+1+1+1 \neq x^2 + y^2$, $x, y \in \mathbb{N}$.





# <lo-sample/> LV.AO.2000.7.2

Atrast mazāko naturālo skaitli, kam visi cipari ir vienādi un kas dalās ar $49$?

<small>

* [mod.exp.fermat](#)
* [div.fta.divisors](#)
* [nt.divisibility.constructions](#)

</small>

<!--
genre=optimization
questionType=Find.Min
concpts=decimal-notation
-->


## ABC

**#PeriodiskaVirkne** **#DalījumsPirmreizinātājos** Atlikumi $1,11,111,\ldots,111111$ ar $7$: $1,4,6,5,2,0$. $777777$ der.



# <lo-sample/> LV.AO.2000.7.4

Vai naturālos skaitļus

1. no $1$ līdz $12$ ieskaitot,
2. no $1$ līdz $50$ ieskaitot

var tā sadalīt pa pāriem, lai visas pāros ieejošo skaitļu summas būtu dažādas un katra no tām būtu pirmskaitlis?
(Piemēram, skaitļus no 1 līdz 6 varētu sadalīt tā: $1+2=3$, $3+4 = 7$, $5+6=11$).

<small>

* [div.prop.primes.small](#)
* [div.prop.primes.small](#)
* [misc.extr.pigeon](#)
* [comb.full](#)

</small>

<!--
concept=partition,primes
questionType=ProveDisprove.Exists
genre=construction
-->

## ABC

**#Pirmskaitļi** **#SummasPārkārtošana** **#DirihlēPrincips** $(1,4)$, $(2,5)$, $(3,8)$, $(6,7)$, $(9,10)$, $(11,12)$. Bet $(1,100)$ ir tikai $24$ pirmskaitļi $>2$. 






# <lo-sample/> LV.AO.2000.8.3

Uz katras no vairākām kartītēm uzrakstīts pa naturālam skaitlim (starp tiem var būt arī vienādi); uz visām kartītēm uzrakstīto skaitļu summa ir $100$. Vai noteikti var atrast tādas kartītes (varbūt vienu pašu), uz kurām uzrakstīto skaitļu summa ir $50$, ja kartīšu skaits ir

1. $50$,
2. $51$?


<small>

* [misc.ind](#)
* [misc.extr.pigeon](#)

</small>

<!--
genre=construction
questionType=ProveDisprove.Exists
-->


## ABC

**#Indukcija** **#Nevienādība** **(a)** $49 \times$ "1" un $1 \times$ "51". **(b)** Noņem $2 \times$ "1" un induktīvais pieņēmums.
**#DirihlēPrincips** **#Interpretācija** **(b)** Intervālus pa apli regulāra $100$-stūra virsotnēs; $\geq 2$ punkti pretī viens otram.









# <lo-sample/> LV.AO.2001.7.2

Naturālu skaitli sauc par simetrisku, ja tā pēdējais cipars nav $0$ un, uzrakstot tā ciparus apgrieztā secībā, 
skaitlis nemainās. Piemēram, $1221$ ir simetrisks skaitlis, bet $1231$ - nav.  
(a) pierādiet: ja simetrisks sešciparu skaitlis dalās ar $13$, tad tas dalās arī ar $7$,  
(b) vai taisnība, ka katrs simetrisks sešciparu skaitlis, kas dalās ar $7$, dalās arī ar $13$?

<small>

* [notation.divrules.1001](#)
* [notation.dec.combine.poly](#)
* [mod.congr](#)

</small>

<!--
concepts=palindrome,decimal-notation
questionType=Prove.ForAll,ProveDisprove.ForAll
-->


## Ciparu algebra

(a) $13$ dala $\overline{abcabc}=1001\cdot{}\overline{abc}$ un 
arī $\overline{abccba}$ (tas ir dots), 
atņemot abus skaitļus, iegūstam $13 \mid 99|a-c|$ un $a=c$.   
(b) $108801$ ir pretpiemērs.


## Cits risinājums

(a) $\overline{abccba}$ izsaka 
$100001a + 10010b + 1100c = 13\cdot (\ldots ) + 5(a-c)$. 
Tad $a-c$ dalās ar $13$ un $a=c$; aizstāj $c$ un dala ar $7$.





# <lo-sample/> LV.AO.2001.8.3

Andrim vajadzēja sareizināt divus dažādus pozitīvus trīsciparu skaitļus. 
Izklaidības pēc viņš tos vienkārši uzrakstīja vienu otram galā. 
Iegūtais sešciparu skaitlis izrādījās $3$ reizes lielāks par reizinājumu, 
kuru Andrim vajadzēja iegūt. Kādu sešciparu skaitli Andris uzrakstīja?

<small>

* [nt.decnotation.expressions](#)
* [al.manipulate.smallexpr](#)
* [al.inequality.estimates](#)

</small>

<!--
questionType=Find.All
genre=digit-manipulation
concepts=decimal-notation
-->



## ABC

**#AlgebrisksPārveidojums** **#Nevienādība** Ja $1000a+b=3ab$, tad $b/a=3b-1000$. Veseli 3cip. $a,b$, tikai ja $b=334$.






# <lo-sample/> LV.AO.2002.7.4

Divi spēlētāji pamīšus raksta uz tāfeles pa vienam 
naturālam skaitlim no $1$ līdz $8$ ieskaitot. 
Nedrīkst rakstīt skaitļus, ar kuriem dalās kaut 
viens jau uzrakstīts skaitlis. 
Kas nevar izdarīt gājienu, zaudē.
Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

<small>

* [comb.constr.partition](#)

</small>

<!--
genre=game
concepts=divisibility
questionType=Algorithm
strategy=contradiction
-->



## Pierādījums no pretējā

**#GadījumuPārlase** **#Spēles** Ja skaitļiem $\{ 2,3,\ldots,7,8\}$ uzvar 1.sp., atkārto viņa stratēģiju. Ja uzvar 2.sp., sāk ar gāj. "$1$".


## Konstruktīva stratēģija

Sāk ar $2$, tad uz katru $(5; 7)$, $(6; 8)$ un $(4; 3)$ atbild ar otru sk. no pārīša.





# <lo-sample/> LV.AO.2002.7.5

Kādu lielāko daudzumu dažādu naturālu skaitļu, kas nepārsniedz $100$, var izvēlēties tā, 
lai nekādu divu izvēlēto skaitļu starpība nebūtu ne $3$, ne $4$, ne $7$?

<small>

* [al.sym.grouping](#)
* [misc.extr.pigeon](#)

</small>


<!--
genre=optimization
questionType=Find.Max
-->


## ABC

**#DirihlēPrincips** **#GadījumuPārlase** Ja $>30$, tad no $10$ sk., jāizvēlas $4$. No $\{1,4,8\}$, $\{2,5,9\}$, $\{2,6,10\}$, $\{7\}$ jāņem pa $1$ – neiespējami.
**#Simetrija** Lai izvēlētos $4$ no *ABCABCXABC*, jāņem arī $X$, bet līdzīgi arī *ABCYABCABC* un $X$,$Y$ starpība ir $3$.






# <lo-sample/> LV.AO.2002.8.2

Andrim vajadzēja sareizināt divus dažādus divciparu skaitļus. Izklaidības pēc 
viņš tos vienkārši uzrakstīja vienu otram galā. Iegūtais četrciparu skaitlis izrādījās 
$3$ reizes lielāks par reizinājumu, kuru Andrim vajadzēja iegūt. 
Kādu četrciparu skaitli Andris uzrakstīja?

<small>

* [nt.decnotation.expressions](#)
* [al.manipulate.smallexpr](#)
* [al.inequality.estimates](#)

</small>


<!--
seeAlso=LV.AO.2001.8.3
questionType=Find.All
genre=digit-manipulation
concepts=decimal-notation
-->




## ABC

**#AlgebrisksPārveidojums** **#Nevienādība** Ja $100a+b=3ab$, tad $b/a=3b-100$. Veseli 2cip. $a,b$, tikai ja $b=34$.





# <lo-sample/> LV.AO.2002.8.3

Par Fibonači skaitļiem sauc skaitļus $1; 2; 3; 5; 8; \ldots$ 
(katru nākošo iegūst, saskaitot divus iepriekšējos).
Vai var pastāvēt vienādība $a+b=c+d$,
ja $a$, $b$, $c$, $d$ ir dažādi Fibonači skaitļi?

<small>

* [al.inequality.extremalelement](#)

</small>


<!--
concepts=fibonacci-sequence
questionType=ProveDisprove.Exists
-->



## ABC

**#Nevienādība** Ja $d$ ir lielākais, tad $a+b=d$, kur $a$,$b$ ir tieši pirms $d$. Bet $c>0$, t.i. $a+b<c+d$. 





# <lo-sample/> LV.AO.2003.7.3

Divi spēlētāji pamīšus raksta uz tāfeles pa vienam naturālam 
skaitlim no $1$ līdz $9$ ieskaitot. Nedrīkst rakstīt skaitļus, ar kuriem dalās 
kaut viens jau uzrakstīts skaitlis. Kas nevar izdarīt gājienu, zaudē. 
Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

<small>

* [comb.constr.partition](#)

</small>

<!--
genre=game
concepts=divisibility
questionType=Algorithm
strategy=contradiction
-->


## No pretējā

**#GadījumuPārlase** **#Spēles** Ja skaitļiem $\{ 2,3,\ldots,8,9\}$ uzvar 1.sp., atkārto viņa stratēģiju. Ja uzvar 2.sp., sāk ar gāj. "$1$".


## Konstruktīva stratēģija

Sāk ar $2$, tad katrā grupā $(5;7)$, $(3;8)$ un $(4;6;9)$ uzvar izolēti.






# <lo-sample/> LV.AO.2003.7.5

Uz tāfeles pa reizei uzrakstīti visi naturālie skaitļi no $1$ līdz $n$ ieskaitot. 
Ar vienu gājienu var izvēlēties divus uz tāfeles uzrakstītus skaitļus 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt $\left| a^2-b^2 \right|$. 
Pēc $n-1$ gājiena uz tāfeles paliek viens skaitlis.  
Vai tas var būt $0$, ja **(a)** $n=8$, **(b)** $n=9$?

<small>

* [misc.invar.parity](#)
* [al.sym.progressions](#)
* [comb.full](#)

</small>

<!--
concepts=absolute-value
genre=making-moves
isProgramming=true
programmingTask=Skaitļu komplektam atrast mazāko, ko var iegūt ar šiem gājieniem.
questionType=Algorithm
-->


## ABC

**#Invariants** **#ProgresijasSumma** Ar $n=8$ var: veido $9$, $32$, $32$ utt. Ja $n=9$, tad $1+2+\ldots+9=45$, bet summas paritāte nemainās.





# <lo-sample/> LV.AO.2003.8.3

Kādā lielākajā daudzumā dažādu naturālu saskaitāmo, 
kas visi lielāki par $1$, var sadalīt skaitli $56$ tā, lai katru divu 
saskaitāmo lielākais kopīgais dalītājs būtu $1$?

<small>

* [al.inequality.extremalelement](#)
* [div.prop.primes.small](#)

</small>

<!--
genre=optimization
concepts=gcd,coprimes
questionType=Find.Count
-->


## ABC

**#EkstrēmaisElements** **#Nevienādība** $3,5,7,11,13,17$ der, bet 7 saskaitāmos nevar, jo pat mazāko pirmsk. summa $>56$. 





# <lo-sample/> LV.AO.2003.8.5

Uz katras no divām lapām jāuzraksta pa $n$ veseliem pozitīviem skaitļiem. 
Visiem $2n$ uzrakstītajiem skaitļiem jābūt dažādiem. Pie tam uz lapām uzrakstīto 
skaitļu summām jābūt vienādām savā starpā, un uzrakstīto skaitļu 
kvadrātu summām arī jābūt vienādām savā starpā.  
Vai tas iespējams, ja **(a)** $n=3$, **(b)** $n=4$, **(c)** $n=2003$?

<small>

* [al.sym.grouping](#)
* [al.manipulate.smallexpr](#)
* [comb.full](#)

</small>

<!--
concepts=square
isHard=true
isProgramming=true
questionType=ProveDisprove.Exists
-->


## ABC

**#Konstrukcija** **#Simetrija** **(a)** $(1,5,6)$, $(2,3,7)$. **(b)** $(1,4,6,7)$, $(2,3,5,8)$. **(c)** $2003$ veido **"(b)"** pieskaitot $k_i$.





# <lo-sample/> LV.AO.2004.7.3

Kādam mazākajam naturālajam $n$ visas daļas
$$\frac{5}{n+7}, \frac{6}{n+8}, \frac{7}{n+9}, \ldots, \frac{35}{n+37}, \frac{36}{n+38}$$
ir nesaīsināmas?

<small>

* [div.common.gcd.euclid](#)
* [div.prop.primes.small](#)

</small>

<!--
concepts=fractions,gcd
questionType=Find.Min
-->


## Eiklīda algoritms

* Visas daļas izskatās šādi: $\frac{k}{n+(k+2)}$. 
* Vajag, lai $\mbox{LKD}(k,n+(k+2))=1$. 
* $\mbox{LKD}(k,n+(k+2))=\mbox{LKD}(k,n+2)=1$, $k=5,\ldots,36$.

$n+2=37$ ir savstarpējs pirmskaitlis ar visiem $k$, t.i. $n=35$.




# <lo-sample/> LV.AO.2004.8.3

Dots, ka $A$ un $B$ – naturāli divciparu skaitļi. Skaitli $X$ iegūst, 
pierakstot skaitlim $A$ galā skaitli $B$; skaitli $Y$ iegūst, 
pierakstot skaitlim $B$ galā skaitli $A$. Dots, ka $X-Y$ dalās ar $91$. Pierādīt, ka $A=B$.

<small>

* [nt.decnotation.expressions](#)
* [nt.divisibility.multiples](#)

</small>

<!--
concepts=decimal-notation,divisibility
genre=digit-manipulation
questionType=Prove.ForAll
-->


## ABC

**#AlgebrisksPārveidojums** **#Dalāmība** $(100A+B)-(100B+A) = 99(A-B)$ un $A-B$ dalās ar $91$. Divciparu skaitļiem tas nozīmē $A=B$.





# <lo-sample/> LV.AO.2004.8.5

Virknē augošā kārtībā izrakstīti naturālie skaitļi no $1$ līdz $2004$ ieskaitot, katrs vienu reizi.
Izsvītrojam no tās skaitļus, kas atrodas $1., 4., 7., 10., \ldots$ vietās. No palikušās virknes atkal
izsvītrojam skaitļus, kas tajā atrodas $1., 4., 7., \ldots$ vietās. Ar iegūto virkni rīkojamies tāpat, utt.,
kamēr paliek neizsvītrots viens skaitlis. Kurš tas ir?

<small>

* [seq.recur](#)
* [al.inequality.intervals](#)

</small>

<!--
concepts=sequence
genre=making-moves
isHard=true
questionType=Find.Only
-->


## ABC

**#KonstrukcijaNoBeigām** **#RekurentaVirkne** Pirms pēdējās izsvītrošanas pēdējais skaitlis bija \#2, pirms tam \#3, \#5, \#8, \#12, utt.
**#GadījumuPārlase** Pēc $n$ svītrošanām pirmais palikušais ir $x_n$. Pamato $x_{n+1} = \left\lceil 3x_n/2 \right\rceil$ pāru un nepāru $x_n$.





# <lo-sample/> LV.AO.2005.7.4

Triju veselu pozitīvu skaitļu summa ir $407$. 
Ar kādu lielāko daudzumu nuļļu var beigties šo
skaitļu reizinājums?

<small>

* [notation.divrules.composite.zeroes](#)
* [mod.congr.sumdiff](#)

</small>

<!--
genre=optimization
concepts=decimal-notation
questionType=Find.Max
-->


## ABC

**#DalīšanaArAtlikumu** **#DalījumsPirmreizinātājos** **#GadījumuPārlase** 

* $407 = 250+125+32$, tad $p = 1000000$. 
* Divi saskaitāmie nevar beigties ar "5", jo atlikušajam tad jābeidzas ar "7". Tātad vismaz
viens saskaitāmais beigsies ar nulli. 
* Vairāk kā sešus $5$-pirmreizinātājus nevar iegūt ($125=5^3$ un $250=5^3\cdot{}2$ ir optimāli).





# <lo-sample/> LV.AO.2005.8.3

Kā var sadalīt naturālos skaitļus no 1 līdz 9 ieskaitot divās daļās tā, lai vienas daļas visu skaitļu
summa būtu vienāda ar otras daļas visu skaitļu reizinājumu?

<small>

* [comb.full.backtrack](#)

</small>

<!--
concepts=partition
genre=construction
questionType=Find.Any
-->



## ABC

**#DalījumsPirmreizinātājos** **#GadījumuPārlase** **#ProgresijasSumma** Ja $a,b,c$ ir reizināti, tad var $abc=32$ un $a+b+c=45-32=13$. $(a,b,c)=(1,4,8)$.






# <lo-sample/> LV.AO.2006.7.1

Vilcienā Rīga-Mehiko vietas numurētas ar naturāliem skaitļiem, sākot ar $1$ 
(numerācija ir vienota visam vilcienam, t.i., ir tikai viena vieta ar numuru $1$, 
viena vieta ar numuru $2$ utt; numuri piešķirti virzienā no lokomotīves uz vilciena "asti"). 
Visos vagonos ir vienāds vietu skaits. Vietas ar numuriem $1996$ un $2015$ ir vienā vagonā,
bet vietas ar numuriem $630$ un $652$ – dažādos vagonos, 
kas pie tam nav blakus viens otram. Cik vietu ir katrā vagonā?

<small>

* [al.inequality.intervals](#)
* [nt.divisibility.multiples](#)
* [mod.congr](#)

</small>

<!--
concepts=sequence
questionType=Find.All
-->



## ABC

**#GadījumuPārlase** **#Nevienādība** Vietu skaits $k \geq 20$ (1.nosac.) un $\leq 21$ (2.nosac.). $1995$ vai $1994$ jādalās ar $k$.





# <lo-sample/> LV.AO.2006.8.3

Naturāla skaitļa $x$ ciparu summu apzīmēsim ar $S(x)$. 
Pieņemsim, ka $n$ – tāds naturāls skaitlis, kam vienlaicīgi 
izpildās īpašības $S(n)=10$ un $S(5n)=5$. 

1. atrodiet kaut vienu tādu skaitli,
2. vai tādu skaitļu ir bezgalīgi daudz?
3. vai kāds no tādiem skaitļiem ir nepāra?


<small>

* [notation.divrules.2or5or10.divides](#)
* [nt.decnotation.sumofdigits](#)

</small>

<!--
genre=special-numbers,sum-of-digits
questionType=Find.Any,ProveDisprove.Other,ProveDisprove.Exists
-->


## ABC

**#Decimālpieraksts** $22222$ der, var arī starpā salikt $0$ (arī $64\cdot 10^k$ der). Ja $n$ nepāra, $5n$ beigtos ar $5$. 





# <lo-sample/> LV.AO.2007.7.1

Kādu lielāko daudzumu dažādu ciparu var izrakstīt pa apli tā, 
lai katri divi blakus uzrakstīti cipari, lasot tos vienalga 
kādā virzienā, veidotu pirmskaitļa pierakstu?


<small>

* [comb.graph.cycle](#)
* [div.prop.primes.small](#)

</small>

<!--
genre=optimization
concepts=primes
questionType=Find.Max
-->




## ABC

**#Grafi** Iespējamie pāri $(1,3)$, $(1,7)$, $(3,7)$, $(7,9)$. $4$-cikla nav, jo $9$ tikai viens kaimiņš. $3$-cikls $1-3-7-1$.





# <lo-sample/> LV.AO.2007.7.3

Uz tāfeles sākumā uzrakstīti $6$ divciparu naturāli skaitļi. 
Andris ar savu gājienu var pieskaitīt dažiem skaitļiem $1$, bet pārējiem skaitļiem $2$. 
(Var arī pieskaitīt visiem skaitļiem $1$ vai visiem skaitļiem $2$.) 
Pēc tam Maija ar savu gājienu var nodzēst jebkuru skaitli, kas dalās ar $7$ 
vai kam ciparu summa dalās ar $7$. Pēc tam gājienu izdara Andris, pēc tam – Maija, utt. 
Pierādīt, ka Maija var panākt, lai skaitļu uz tāfeles vairs nebūtu 
(pieņemsim, ka tiek spēlēts pietiekoši ilgi).


<small>

* [seq.gaps](#)
* [misc.ind.descent](#)

</small>

<!--
concepts=decimal-notation,divisibility,sum-of-digits
genre=game
questionType=Algorithm,Prove.ForAll
-->


## ABC

**#Dalāmība** **#Decimālpieraksts** **#Spēles** Pārīšiem $(105;106)$, $(160;161)$, $(167;168)$, $(175;176)$ utt. Andris nevar tikt pāri.





# <lo-sample/> LV.AO.2007.8.3

Juliata iedomājās naturālu skaitli, sareizināja visus tā ciparus un iegūto 
rezultātu pareizināja ar iedomāto skaitli. Gala rezultātā Juliata ieguva $1716$. 
Kādu skaitli viņa iedomājās sākumā?

<small>

* [div.fta](#)
* [alg.ineq.equations](#)

</small>

<!--
concepts=decimal-notation
genre=digit-manipulation
questionType=Find.All
-->


## ABC

**#Dalāmība** **#DalījumsPirmreizinātājos** $1716=2^2 \cdot 3 \cdot 11 \cdot 13$. Sk. $11$ un $13$ nav cipari. Atbilde ir formā $11 \cdot 13 \cdot k$.






# <lo-sample/> LV.AO.2008.7.2

Dots, ka $x$ un $y$ – tādi naturāli skaitļi, ka  $x \cdot y = 10^{12}$. 
Vai var būt, ka ne $x$, ne $y$ nesatur savā pierakstā nevienu ciparu $0$?

<small>

* [notation.divrules.composite.zeroes](#)
* [alg.tra.pow.prod](#)

</small>

<!--
concepts=decimal-notation
questionType=ProveDisprove.Exists
-->



## Izmantojam 10^12 dalījumu pirmreizinātājos

Nē. $x$ vai $y = 2^{12} = 4096$. (Vai arī sareizināsies $2$ un $5$.)





# <lo-sample/> LV.AO.2008.8.3

Dots, ka $n>1$ – naturāls skaitlis, kas nav pirmskaitlis. 
Pierādīt, ka var atrast vismaz trīs dažādus naturālus skaitļus $a_1,a_2,\ldots,a_k$, 
kas apmierina sakarību
$$a_1 + a_2 + \ldots + a_k = n \cdot \left( \frac{1}{a_1} + 
\frac{1}{a_2} + \ldots + \frac{1}{a_k} \right).$$

<small>

* [div.fta.divisors.num](#)
* [div.fta.divisors.pair](#)
* [alg.series.sum](#)

</small>

<!--
concepts=primes,series
questionType=Prove.Exists
-->


## Dalītājus sadala pārīšos

* Sadala pa pāriem $a_1a_k = a_2a_{k-1} = \ldots = n$ (un $k \geq 3$).
* Tad $a_1 + \ldots + a_k = a_k + \ldots + a_1$.

$$1+3+9 = 9 \cdot \left( \frac{1}{1} + \frac{1}{3} + \frac{1}{9} \right). $$





# <lo-sample/> LV.AO.2009.7.3

Tabula sastāv no $3 \times 3$ rūtiņām. Rūtiņās ierakstīti naturāli skaitļi no $1$
līdz $9$ (katrā rūtiņā cits skaitlis). Skaitļu summas rindās un kolonnās
visas ir dažādas. Kāds lielākais daudzums šo summu var būt pirmskaitļi?

<small>

* [mod.fix.parity](#)
* [div.prop.primes.small](#)
* [al.sym.progressions](#)
* [comb.full](#)

</small>

<!--
concepts=primes
genre=fill-in-table
questionType=Find.Max
isHard=true
-->



## ABC

**#Paritāte** **#Pirmskaitļi** **#ProgresijasSumma** **#SummasPārkārtošana** Nepāri kā pentomino "V". $(5,6,4)$,$(9,8,2)$,$(7,3,1)$. Nevar būt $p_1+p_2+p_3=45$.






# <lo-sample/> LV.AO.2009.7.5

Vairākiem rūķīšiem ir vienādi naudas daudzumi. Brīdi pa brīdim
kāds no rūķīšiem paņem daļu savas naudas un sadala to pārējiem
vienādās daļās. Pēc kāda laika izrādījās, ka vienam no rūķīšiem ir $8$
dālderi, bet citam – $25$ dālderi. Cik pavisam ir rūķīšu? (Dālderis ir
vienīgā rūķīšiem pieejamā naudas vienība.)

<small>

* [misc.invar.congr](#)

</small>

<!--
concepts=divisibility
genre=making-moves
questionType=Find.All
-->


## ABC

**#Dalāmība** **#Invariants** Ja rūķu ir $a$, pārdalot $k$ dāld., starpība mainās par $(a-1)k+k = ak$. Ja beigu starp. ir $17$, tad $a=17$.





# <lo-sample/> LV.AO.2009.8.4



Profesors Cipariņš ar savu ārzemju kolēģi ieradās Ziemassvētku
eglītes pasākumā, kurā piedalījās universitātes darbinieki, viņu
draugi, ģimenes locekļi, paziņas utt. Norādot uz trim viesiem,
Cipariņš piezīmēja: "Šo cilvēku vecumu reizinājums ir $2450$, bet
summa – divas reizes lielāka nekā Jūsu vecums." Kolēģis atteica:
"Es nezinu un nevaru noskaidrot, cik veci ir šie ļaudis." Tad Cipariņš
piebilda: "Es esmu vecāks par jebkuru citu šai eglītē." Tagad kolēģis
uzreiz pateica minēto $3$ viesu vecumus. Cik gadu tai laikā bija
Cipariņam un cik – viņa kolēģim? (Visus vecumus izsaka veselos
gados.)

<small>

* [div.fta](#)
* [comb.full](#)

</small>

<!--
genre=word-problem
isHard=true
questionType=Find.All
-->



## ABC

**#DalītājuSkaits** **#GadījumuPārlase** Kolēģa 1.atbildei atbilst $(5,10,49)$ vai $(7,7,50)$. Otrā P.C. piebilde neļauj tos atšķirt.






# <lo-sample/> LV.AO.2010.7.1

Uz tāfeles uzrakstīti pieci dažādi pirmskaitļi, kas nepārsniedz $100$. Par tiem
zināms, ka

1. pirmais ir $7$;
2. trešais ir par $4$ lielāks nekā piektais;
3. skaitlim, kuru iegūst, ceturto sareizinot ar piekto, visi cipari ir vienādi;
4. pirmais un ceturtais summā dod pieckāršotu otro.

Atrodi visus šos skaitļus!

<small>

* [div.prop.primes.small](#)
* [div.prop.primes.small](#)
* [div.fta](#)

</small>

<!--
concepts=primes
genre=construction
questionType=Find.All
-->

## ABC

**#GadījumuPārlase** (a) $p_1=7$, (b) $p_5 \neq 11$, (d) $p_4 \neq 11$, (c) $p_4 p_5 = 3 \cdot 37$, (d) $p_4 \neq 37$. Tātad $(7,2,41,3,37)$.





# <lo-sample/> LV.AO.2010.7.3

Ieraksti tabulas ar izmēriem $4 \times 4$ rūtiņas katrā rūtiņā vienu naturālu skaitli
tā, lai vienlaicīgi izpildītos šādas divas īpašības:

1. visi ierakstītie skaitļi ir dažādi;
2. jebkuru četru skaitļu, nekādi divi no kuriem neatrodas ne vienā rindā, 
nedz vienā kolonnā, summa ir $2010$.

Pietiek parādīt vienu veidu, kā to var izdarīt.

<small>

* [alg.linear.comb](#)
* [comb.full.backtrack](#)

</small>

<!--
genre=construction
questionType=Find.Any
-->


## ABC

**#MaģiskaisKvadrāts** **#SummasPārkārtošana** Saskaita 2 tabulas: $((1,2,3,4),\ldots,(1,2,3,4))$ un   $(0,\ldots,0),(4,\ldots,4),(996,\ldots,996),(1000,\ldots,1000)$.





# <lo-sample/> LV.AO.2010.7.4

Vairākiem bērniem visiem ir vienāds skaits konfekšu. Brīdi pa brīdim kāds
no bērniem paņem daļu savu konfekšu un sadala to pārējiem vienādās
daļās. Pēc kāda laika izrādījās, ka vienam no bērniem ir $4$ konfektes, bet
citam – $23$ konfektes. Cik pavisam ir bērnu? (Konfektes netiek dalītas
daļās, apēstas vai izmestas.)


<small>

* [misc.invar.congr](#)

</small>

<!--
questionType=Find.All
-->


## ABC

**#Dalāmība** **#Invariants** Ja bērnu ir $a$, pārdalot $k$ konf., starpība mainās par $(a-1)k+k = ak$. Ja beigu starp. ir $19$, tad $a=19$.





# <lo-sample/> LV.AO.2010.8.1

Starp skaitļiem
$$6\;\;1\;\;3\;\;4,$$
nemainot to secību, ievieto aritmētisko darbību zīmes ("$+$", "$-$", "$\ast$",
"$:$") un iekavas tā, lai iegūtās izteiksmes vērtība būtu **(a)** $25$,
**(b)** $24$.  
Vai to var izdarīt?

<small>

* [comb.full.syntax](#)

</small>

<!--
questionType=ProveDisprove.Exists
-->




## ABC

**#GadījumuPārlase** **#SintaksesKoks** **(a)** $(6 + 1)\ast 3 + 4 = 25$; **(b)** $6 : (1 - 3:4)=24$.






# <lo-sample/> LV.AO.2010.8.2

Andris un Juris katrs izvēlas trīs secīgus naturālus skaitļus tā, ka visi
seši skaitļi ir atšķirīgi. Katru Andra skaitli sareizināja ar katru Jura
skaitli, ieguva deviņus reizinājumus. Pierādi, ka starp iegūtajiem
deviņiem skaitļiem vismaz astoņi būs savā starpā atšķirīgi!

<small>

* [alg.expr.prop](#)
* [comb.full](#)

</small>

<!--
questionType=Prove.ForAll
-->



## Algebriski iztulkots vārds "secīgi"

Ja iedomāti $(a-1,a,a+1)$ un $(b-1,b,b+1)$ tad 2 vienādi reizinājumi, ja $b \pm 1 = 2a$ vai $a \pm 1 = 2b$.



# <lo-sample/> LV.AO.2010.10.4

Cik dažādos veidos skaitli $2010$ var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu? Saskaitāmo secība nav svarīga. 

### LV.AO.2011.10.1

Cik dažādos veidos skaitli $2011$ var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu? Saskaitāmo secība nav svarīga. 

<small>

* [seq.arithm.summation](#)
* [div.fta.proc](#)
* [comb.full](#)

</small>

<!--
questionType=Find.Count
-->






# <lo-sample/> LV.AO.2011.7.1

Uz tāfeles augošā secībā uzrakstīti seši dažādi pirmskaitļi, kas
nepārsniedz $100$. Par tiem zināms, ka

1. visu skaitļu pēdējie cipari ir atšķirīgi;
2. sestais skaitlis ir par $14$ lielāks nekā trešais;
3. ceturtā skaitļa pirmais cipars ir vienāds ar otrā skaitļa pēdējo ciparu;
4. piektā un sestā skaitļa pirmie cipari ir vienādi.

Atrodi visus šos skaitļus!

<small>

* [div.prop.primes.small](#)
* [div.prop.primes.small](#)

</small>

<!--
questionType=Find.All
-->



## ABC

**#GadījumuPārlase** **#Pirmskaitļi** (a) $p_1=2$,$p_2=5$. (b),(d) $(p_3;p_6)=(53,67)$. (c) $p_4=59$.






# <lo-sample/> LV.AO.2011.7.3

Atrodi naturālu skaitli, kuru, dalot ar $2010$, atlikumā iegūst $13$, bet,
dalot ar $2011$, atlikumā iegūst $3$.

<small>

* [mod.eq.chinese](#)
* [nt.divisibility.constructions](#)

</small>

<!--
questionType=Find.Any
-->


## ABC

**#LineārasKongruences** $2010k+13$ dod atlikumus $13-k$ dalot ar $2011$. 





# <lo-sample/> LV.AO.2011.8.1

Starp skaitļiem
$$8\;\;3\;\;5\;\;2,$
nemainot to secību, ievieto aritmētisko darbību zīmes ("$+$", "$-$", "$\ast$",
"$:$") un iekavas tā, lai iegūtās izteiksmes vērtība būtu **(a)** $15$, **(b)** $16$.

<small>

* [comb.full.syntax](#)

</small>

<!--
questionType=Find.Any
-->


## ABC

**#GadījumuPārlase** **#SintaksesKoks** **(a)** $8 - 3 + 5 \ast 2 = 8 - (3 - 5 \ast 2) = 15$; **(b)** $8 : (3 - 5:2) = 16$.





# <lo-sample/> LV.AO.2011.8.4

Leonards izvēlējās patvaļīgu trīsciparu skaitli, pareizināja to ar $2$ un
tam galā pierakstīja sākotnējo skaitli. Vai viņa jauniegūtais skaitlis
noteikti dalās ar **(a)** $17$; **(b)** $23$?

<small>

* [nt.decnotation.expressions](#)
* [div.fta](#)

</small>

<!--
questionType=ProveDisprove.ForAll
-->



## ABC

**#Dalāmība** **#Decimālpieraksts** Ja 3-cip. sk. ir $\overline{abc}$, tad jaunais ir $2001\overline{abc}$ dalās ar $23$. Bet $17 \nmid 2001$. 





# <lo-sample/> LV.AO.2011.8.5

Jānis un Anna spēlē šādu spēli. Uz tāfeles ir uzrakstīts naturāls
skaitlis. Spēlētāji pēc kārtas veic gājienu: no uzrakstītā skaitļa atņem
kādu šī skaitļa ciparu (izņemot $0$), nodzēš uz tāfeles esošo skaitli un
tā vietā uzraksta iegūto starpību. Uzvar tas, kurš pēc sava gājiena
iegūst nulli.  
Sākumā ir uzrakstīts skaitlis $2011$, pirmo gājienu izdara Anna. Kurš
no spēlētājiem, pareizi spēlējot, uzvarēs? Apraksti, kā uzvarētājam
jārīkojas!

<small>

* [misc.invar.game](#)

</small>

<!--
questionType=Algorithm,Prove.ForAll
-->



## ABC

**#Invariants** **#Spēles** Pēc katra Annas gājiena skaitlim jādalās ar $10$. 





# <lo-sample/> LV.AO.2012.7.1

Vai var atrast tādus veselus skaitļus $a$ un $b$, kuriem izpildās vienādība
$$ab(3a + 5b) = 1234567?$$


<small>

* [mod.fix.parity](#)

</small>

<!--
questionType=ProveDisprove.Exists
-->

## ABC

**#Paritāte** Nepāru reizinājums nozīmē, ka $a,b$ ir nepāru. Bet tad $3a+5b$ ir pāru, kas ir pretruna. 





# <lo-sample/> LV.AO.2012.8.1

Starp skaitļiem
$$4\;\;1\;\;5\;\;7,$$
nemainot to secību, ievieto aritmētisko darbību zīmes ("$+$", "$-$", "$\ast$",
"$:$") un iekavas tā, lai iegūtās izteiksmes vērtība būtu **(a)** $13$, **(b)** $14$. 


<small>

* [comb.full.syntax](#)

</small>

<!--
questionType=Find.Any
-->


## ABC

**#GadījumuPārlase** **#SintaksesKoks** **(a)** $4 \ast 1 \ast 5 - 7 = 13$; **(b)** $4:(1-5:7) = 14$ bet arī $(4-1-5)\ast(-7)=14$.






# <lo-sample/> LV.AO.2012.8.3

Skolas matemātikas olimpiādē piedalījās ne vairāk kā $60$ skolēnu.
Vidējais punktu skaits, ko ieguva zēni, bija $21,6$. Vidējais punktu
skaits, ko ieguva meitenes, bija $15$. Vidējais punktu skaits, ko ieguva
visi skolēni, bija $20$. Cik skolēnu piedalījās olimpiādē?


<small>

* [alg.series.mean](#)
* [alg.ineq.equations](#)

</small>

<!--
questionType=Find.All
-->


## ABC

**#MasuCentrs** $**MKD**$ Pleci $1.6=|21.6-20|$ un $5=|15-20|$ attiecas kā $8$ un $25$. Zēnu ir $25$ un meiteņu $8$.





# <lo-sample/> LV.AO.2012.8.4

Pa apli uzrakstīti $11$ veseli skaitļi. Jebkuru trīs pēc kārtas ņemtu
skaitļu summa dalās ar $5$. Pierādi, ka visi uzrakstītie skaitļi dalās ar
$5$.


<small>

* [mod.period](#)

</small>

<!--
questionType=Prove.ForAll
-->



## ABC

**#DalīšanaArAtlikumu** **#PeriodiskaVirkne** Atlikumi $(\operatorname{mod} 5)$ ik pēc $3$ atkārtojas, tātad tie visi vienādi (un vienādi $0$).








# <lo-sample/> LV.AO.2012.10.1

Pierādi: ja $p$ un $14p^2+1$ ir pirmskaitļi, tad $14p^2-1$ ir naturāla
skaitļa kubs.

<small>

* [mod.congr.pow](#)
* [mod.congr.sumdiff](#)

</small>


<!--
questionType=Prove.ForAll
-->

## Secinājumu ķēdīte:

* Ja $p$ nedalās ar $3$, tad $p^2$ atlikums, dalot ar $3$, ir $1$. 
* Tad $14p^2$ dod atlikumu $2$, dalot ar $3$, jo skaitli ar atlikumu $2$ 
reizina ar skaitli ar atlikumu $1$.
* Tad $14p^2+1$ dod atlikumu $0$, dalot ar $3$. Tas nav pirmskaitlis. 

Secinām, ka $p=3$ (citi pirmskaitļi nedalās ar $3$). Tādēļ 
$14p^2 +1 = 127$ un $14p^2 - 1 = 125$, kas tiešām ir pilns kubs $5^3$.






# <lo-sample/> LV.AO.2013.7.1

Naturālā divciparu skaitlī neviens no cipariem nav $0$. Pierādīt, ka,
dalot šo skaitli ar tā ciparu reizinājumu, dalījums ir vismaz $\frac{11}{9}$.


<small>

* [alg.ineq.monotonicity](#)
* [notation.dec.combine.poly](#)
* [misc.extr.param](#)

</small>


<!--
questionType=Prove.ForAll
-->


## ABC

$\frac{10a+b}{ab}=\frac{10}{b}+\frac{1}{a}$ ir vismazākā, ja $a=b=9$.





# <lo-sample/> LV.AO.2013.7.3

Pierādīt, ka skaitlis $1234567891011\ldots{}175176$ (pēc kārtas uzrakstīti
visi naturālie skaitļi no $1$ līdz $176$) nav naturāla skaitļa kvadrāts.
(Skaitļa kvadrāts ir skaitļa reizinājums pašam ar sevi.)


<small>

* [notation.divrules.pow2or5.divides](#)
* [notation.divrules.3or9.remainder](#)
* [div.fta.pow.square](#)
* [seq.arithm.summation](#)

</small>


<!--
questionType=Prove.NotExists
-->


## 1.risinājums (dalāmība ar 3)

* Minētajam skaitlim ciparu summa kongruenta pēc moduļa $9$ ar
$1+\ldots+176$. (Decimālciparu pārvietojot, atlikums nemainās).
* Summējam aritmētisku progresiju: 
$1+\ldots+176=(176\cdot 177)/2$ - dalās ar $3$, bet ne ar $9$.
* Pilns kvadrāts nevar saturēt pirmskaitli $3$ nepāru pakāpē.

## 2.atrisinājums (dalāmība ar 2)

* Pilnu kvadrātu dalījums pirmreizinātājos 
nevar dalīties ar $8$ un nedalīties ar $16$ – 
saturēt pirmskaitli $2$ nepāru pakāpē.






# <lo-sample/> LV.AO.2013.8.1

Atrast visus naturālos skaitļus, kas nepārsniedz $1000000$ un kuri,
nosvītrojot to pirmo ciparu, samazinās $36$ reizes.


<small>

* [alg.expr](#)
* [notation.dec.combine.poly.pieces](#)

</small>


<!--
questionType=Find.All
-->


## Pirmā cipara nodalīšana no pārējā gabala

$a$ - 1.cipars; $a \cdot 10^k + b = 36b$; $a \cdot 10^k = 35b$. 
Tad $a = 7$, $b=2\cdot 10^{k-1}$. 





# <lo-sample/> LV.AO.2013.10.4

No pirmajiem $100$ naturālajiem skaitļiem izvēlēts $51$ skaitlis.
Pierādīt, ka no tiem var izvēlēties divus, no kuriem viens dalās ar
otru.

<small>

* [seq.geom](#)
* [misc.extr.pigeon](#)

</small>

<!--
questionType=Prove.Other
-->


## Konstrukcija

Izrakstām ģeometriskas progresijas, kas sākas ar nepāru skaitļiem un $q=2$: 

$$(1,2,4,8,16,32,64),\;(3,6,12,24,48,96),$$
$$(5,10,20,40,80),\ldots,(97),\;(99).$$

* Būs tieši $50$ progresijas (dažās būs tikai pa vienam loceklim), jo līdz $100$ ir tieši $50$ nepāru skaitļi.
* Katrs skaitlis pieder tieši vienai progresijai, jo katram pāru skaitlim atbilst tieši viens nepāru 
skaitlis, kurš rodas, ja atkārtoti dala ar $2$. 
* Izvēloties $k+1$ skaitļus, vismaz divi būs no vienas progresijas (Dirihlē princips).


## Pretpiemērs

* Ja skaitļu ir tikai $50$, tad līdzīgi secināt nevar. 
* Var izvēlēties $51,\ldots,100$ - no tiem neviens nedalās ar otru.






# <lo-sample/> LV.AO.2014.7.2

Vai var atrast tādus veselus skaitļus $a$ un $b$, 
kuriem izpildās vienādība $a \cdot (3a + 5b) \cdot 7b = 7654321$. 


<small>

* [mod.fix.parity](#)

</small>


<!--
questionType=ProveDisprove.Exists
-->


## ABC

**#Paritāte** Nepāru reizinājums nozīmē, ka $a,b$ ir nepāru. Bet tad $3a+5b$ ir pāru, kas ir pretruna. 






# <lo-sample/> LV.AO.2014.7.4

Tabulas $3 \times 3$ rūtiņās katrā rūtiņā jāieraksta pa vienam naturālam skaitlim tā, 
lai katrā rindā,
katrā kolonnā un katrā diagonālē ierakstīto skaitļu summas būtu vienādas. Ir zināmi divās
rūtiņās ierakstītie skaitļi (skat.\ zīm.). Kādam skaitlim jābūt rūtiņā, kas apzīmēta ar
jautājuma zīmi? Atrodiet visas iespējamās vērtības un pamatojiet, ka citu nav!

![magicsquare](LV.AO.2014.7.4.png)


<small>

* [alg.expr.selectvar](#)

</small>


<!--
questionType=Find.All
genre=magic-configuration
-->


## ABC

Ja $a_{22}=x$, tad summas ir $3x$. Un $a_{13}=2x-13$, $a_{11}=x-11$, $a_{33}=x+11$, $a_{23}=2$.






# <lo-sample/> LV.AO.2014.8.1

Skaitli $\frac{1}{13}$
pārveidoja par bezgalīgu decimāldaļu un tajā izsvītroja 2014. ciparu aiz komata.
Kurš skaitlis lielāks – sākotnējais vai iegūtais?


<small>

* [mod.period](#)
* [notation.algor](#)

</small>

<!--
questionType=Find.Only
concepts=decimal-fractions
genre=digit-manipulation
-->


## ABC

**#Decimālpieraksts** **#PeriodiskaVirkne** $1/13=0.(076923076923)$ (periods $12$ cipari). $2014$-tais jeb $10$-tais cipars ir $9$.






# <lo-sample/> LV.AO.2014.8.2

Atrast visus naturālos skaitļus, kas nepārsniedz 
$1000000$ un kuri, nosvītrojot to pirmo
ciparu, samazinās $15$ reizes!


<small>

* [alg.expr](#)
* [notation.dec.combine.poly.pieces](#)

</small>

<!--
questionType=Find.All
-->



## Pirmais cipars un viss pārējais

$a$ - 1.cipars; $a \cdot 10^k + b = 15b$; $a \cdot 10^k = 14b$. 
Tad $a = 7$, $b=5\cdot 10^{k-1}$. 





# <lo-sample/> LV.AO.2014.8.5

Tabulas $3 \times 3$ rūtiņās katrā rūtiņā jāieraksta pa vienam naturālam skaitlim tā, lai katrā rindā,
katrā kolonnā un katrā diagonālē ierakstīto skaitļu summas būtu vienādas. Augšējās rindas
vidējā rūtiņā ierakstīts skaitlis $24$ (skat.\ zīm.). Vai rūtiņā, kas apzīmēta ar jautājuma
zīmi, var būt ierakstīts skaitlis **(a)** $7$,  **(b)** $17$?

![magicsquare](LV.AO.2014.8.5.png)


<small>

* [alg.expr.selectvar](#)
* [comb.full.backtrack](#)

</small>

<!--
questionType=ProveDisprove.Exists
-->

## ABC

**#AlgebrisksPārveidojums** **#MaģiskaisKvadrāts** Apz. $a_{22}=x$, $a_{31}=b$. Tad $a_{13}=2x-b$, $a_{11}=x+b-24$, $a_{33}=x-b+24$, $a_{23}=2b-24$. Pie $b=7$, $a_{23}<0$.








# <lo-sample/> LV.AO.2014.10.4

Doti septiņi dažādi naturāli skaitļi; katriem diviem 
no dotajiem skaitļiem aprēķināja to
summu. Kāds lielākais skaits no šīm summām var būt pirmskaitļi?

<small>

* [mod.fix.parity](#)
* [comb.graph.bipartite](#)
* [mod.congr.sumdiff](#)
* [comb.constr.iterative](#) 

</small>


<!--
questionType=Find.Max
-->

**Uzdevuma lasīšana:** Jānoskaidro lielākais *skaits*, kas vispār var būt 
pirmskaitļi. Nevis, teiksim, lielākais *dažādu pirmskaitļu* skaits, ko 
var šādi iegūt.


## Spriedumi ar paritāti

* Dažādu naturālu skaitļu summa nevar būt $2$.
* Tātad, lai divu skaitļu summa būtu (nepāru) pirmskaitlis, 
viens no tiem ir pāru, otrs ir nepāru. 


## Cik no 7 ir pāru un cik nepāru skaitļu?

$$7=0+7=1+6=2+5=3+4=4+3=5+2=6+1=7+0$$

Lielākais teorētiski iespējamais $(n,p)$ pārīšu skaits ir tad, 
ja $4$ no septiņiem skaitļiem ir nepāru un $3$ ir pāru (vai otrādi): 

$$4\cdot{}3=12$$


## Divdaļīgi grafi

<hgroup>

![bipartite](LV.AO.2014.10.4-01.svg)

* Nepāru skaitļi veido kopu $A$ ar $4$ elementiem, 
pāru skaitļi veido kopu $B$ ar $3$ elementiem. 
* Ir tikai $4\cdot{}3$ pāri, kam ir cerība būt pirmskaitļiem. 
(Saskaitot $p+p$ vai $n+n$ pirmskaitli iegūt nevar.)

</hgroup>

<hgroup>

**Definīcija:** Ja grafā visas virsotnes var sadalīt divās nepārklājošās apakškopās $A$ un $B$ tā, 
ka jebkura grafa šķautne iet no virsotnes kopā $A$ uz virsotni kopā $B$, tad grafu sauc 
par *divdaļīgu*.  
**Apgalvojums:** Ja divdaļīgā grafā apakškopās $A$ un $B$ ir attiecīgi $a$ un $b$ virsotnes, 
tad tajā ir ne vairāk kā $a\cdot{}b$ šķautnes.

</hgroup>


## Atlikumi, dalot ar 3


![bipartite](LV.AO.2014.10.4-02.svg)

* Izvēloties vismazākos nepāru un pāru skaitļus, tikai $9$ no $12$ teorētiski iespējamajiem 
ir pirmskaitļi (citas summas dalās ar $9$ - apzīmētas ar raustītu līniju). 
* Ja papildus prasa, lai visi $7$ skaitļi dotu atlikumu $1$ (vai, izņēmuma gadījumā, atlikumu $0$), 
dalot ar $3$, var panākt, lai visas $12$ summas būtu pirmskaitļi.






# <lo-sample/> LV.AO.2015.7.3


1. Atrast tādu naturālu skaitli, kura ciparu summa ir $13$, pēdējie divi
cipari ir $13$ un kurš dalās ar $13$.
2. Vai var atrast tādu naturālu skaitli, kura ciparu summa ir $11$, pēdējie
divi cipari ir $11$ un kurš dalās ar $11$?


<small>

* [notation.divrules.11](#)
* [notation.divrules.3or9.divides](#)

</small>


<!--
questionType=Find.Any,ProveDisprove.Exists
-->


## Dalāmība aar 9 un 11

**(a)** $117$ cip.summa $9$, dalās ar $13$. $11713$ der.  
**(b)** $99k$ pāru/nepāru poz.cip.summa nevar būt $9$.





# <lo-sample/> LV.AO.2015.8.1

Nosaki, vai izteiksmes $\sqrt{6 + 2\sqrt{5}} + \sqrt{6 - 2\sqrt{5}}$ 
vērtība ir racionāls skaitlis!


<small>

* [alg.tra.binom.square](#)
* [misc.ind.descent](#)

</small>

<!--
questionType=Find.Only
-->



## ABC

**#AlgebriskaIdentitāte** **#QĪpašības** Kāpinot kvadrātā sanāk $20$, bet $\sqrt{20}=2\sqrt{5}$ nav racionāls.





# <lo-sample/> LV.AO.2015.8.3

Atrast vienu naturālu skaitli, kas lielāks nekā $2015$ un ko nevar izteikt kā
naturāla skaitļa kvadrāta un pirmskaitļa summu.


<small>

* [alg.tra.factor.sqdiff](#)
* [div.prop.primes.small](#)

</small>


<!--
questionType=Find.Any
-->


## ABC

**#AlgebriskaIdentitāte** **#Nevienādība** Ja $N = n^2$ liels pilns kvadrāts, tad $n^2 - a^2$ dalās reizinātājos $>2$.  




# <lo-sample/> LV.AO.2015.10.3

Atrast visus naturālos skaitļus, kas ir vienādi ar savu ciparu reizinājumu.
(Par viencipara skaitļa ciparu reizinājumu sauc tā vienīgo ciparu.)

<small>

* [misc.try](#) 
* [alg.ineq.transitive](#)

</small>

<!--
questionType=Find.All
-->


## Nevienādību izmantošana

* Pārbaudot dažādus skaitļus var novērot, ka ciparu reizinājums allaž mazāks par pašu skaitli.
* Pamatojam to 2-ciparu un 3-ciparu skaitļiem $\overline{ab}$ un $\overline{abc}$

$$a\cdot{}b < 10a \leq 10^1\cdot{}a + b = \overline{ab},$$
$$a\cdot{}b\cdot{}c < 10^2\cdot{}a < 100a + 10b + c = \overline{abc}.$$

Skaitļa pirmo decimālciparu reizinot ar $k$ turpmākajiem cipariem, iegūsim 
mazāku rezultātu nekā reizinot ar $10^k$, jo katrs cipars ir mazāks par $10$. 





# <lo-sample/> LV.AO.2016.7.2

Karlsons sev pusdienām nopirka $8$ pīrādziņus un $15$ magoņmaizītes, bet
Brālītis – vienu pīrādziņu un vienu magoņmaizīti. Karlsons par savām
pusdienām samaksāja tieši divus eiro (katra maizīte un pīrādziņš maksā veselu
skaitu centu). Cik samaksāja Brālītis?


<small>

* [alg.expr](#)
* [alg.expr.prop](#)
* [alg.ineq.equations](#)

</small>

<!--
questionType=Find.All
-->




## ABC

**#Dalāmība** **#Nevienādība** $200-8p=15m$, t.i. $m$ dalās ar $8$. Un $m$ nevar būt $16$, citādi $p<0$.  






# <lo-sample/> LV.AO.2016.8.1

Aprēķini dotās izteiksmes vērtību!
$$\frac{2000016 \cdot 1999984}{5^{12} \cdot 2^{13} - 128}$$


<small>

* [al.manipulate.smallexpr](#)
* [alg.tra.factor.sqdiff](#)

</small>

<!--
questionType=Find.Only
-->




## ABC

**#AlgebriskaIdentitāte** **#AlgebrisksPārveidojums** $\frac{4(10^6 - 8)(10^6 + 8)}{2(10^{12} -64)} = \frac{4}{2}=2$. 






# <lo-sample/> LV.AO.2016.8.2

Vai var atrast tādus veselus skaitļus $a$ un $b$, ka $ab(a+43b) = 434343$?


<small>

* [mod.fix.parity](#)

</small>

<!--
questionType=ProveDisprove.Exists
-->





## ABC

**#Paritāte** Reizinājums ir nepāru, t.i. $a,b$ ir nepāru. Bet tad $a+43b$ ir pāru. 





# <lo-sample/> LV.AO.2016.8.3

Zināms, ka skaitlis dalās ar $2016$ un ka visi tā cipari ir dažādi. Kāds ir lielākais
ciparu skaits, kas var būt šajā skaitlī?


<small>

* [notation.divrules.pow2or5.divides](#)
* [notation.divrules.3or9.divides](#)
* [notation.divrules.composite](#)
* [comb.full](#)

</small>

<!--
questionType=Find.Max
-->



## ABC

**#DalījumsPirmreizinātājos** Visi $10$ cipari: $32 \mid 45312$. Cip.summa dalās ar $9$. Samaisa $6,7,8,9,0$, lai dalās ar $7$.



# <lo-sample/> LV.AO.2016.10.2

Vai var atrast tādus veselus skaitļus $x$, $y$ un $z$, ka
$x^3 − 2016xyz = 120$?

<small>

* [div.fta.proc](#)
* [notation.divrules.3or9.remainder](#)
* [mod.congr.poly](#)
* [mod.eq.contradict](#) - pretrunas modulis: atlikumi pēc 9

</small>

<!--
questionType=ProveDisprove.Exists
-->









# <lo-sample/> LV.AO.2016.10.3

Aritmētiskās progresijas četri pēc kārtas ņemti locekļi ir veseli
skaitļi $A$, $B$, $C$ un $D$. Pierādīt, ka
$A^2+2B^2+3C^2+4D^2$
var izteikt kā divu
veselu skaitļu kvadrātu summu!

<small>

* [seq.arithm.expr](#)
* [alg.tra.binom.square](#)
* [alg.tra.binom.complsquare](#)

</small>

<!--
questionType=Prove.Exists
-->




# <lo-sample/> LV.AO.2017.7.5

Cik ir tādu naturālu divciparu skaitļu, kuriem ciparu reizinājums ir tieši divas
reizes mazāks nekā pats skaitlis?

<!--
questionType=Find.Count
-->



# <lo-sample/> LV.AO.2017.8.5

Vai var atrast tādu desmitciparu skaitli, kas ir vienāds ar visu savu ciparu
reizinājumu?

<!--
questionType=ProveDisprove.Exists
-->


# <lo-sample/> LV.AO.2017.10.5

Pierādīt, ja no trim naturāliem skaitļiem $n$; $n+11$ un $n+22$ divi ir
pirmskaitļi, tad trešais skaitlis dalās ar $6$.

<small>

* [div.prop.prod](#)
* [seq.arithm.mod.all](#)
* [comb.full](#) (gadījumus $n=2,3$ aplūko atsevišķi)

</small>

<!--
questionType=Prove.ForAll
-->



# <lo-sample/> LV.AO.2018.7.4

Atrast tādu veselu skaitli $n$, lai vienādība
$$(n - 2021)(n - 2018)(n - 2017)(n - 2016) = 2016$$
būtu patiesa!

<!--
questionType=Find.Any
-->



# <lo-sample/> LV.AO.2018.8.2

Naturālu skaitļu virknes $1; 8; 8; 64; 192; 432; \ldots$ 
katrs loceklis, sākot ar trešo, ir vienāds ar divu iepriekšējo 
locekļu nenulles ciparu reizinājumu. Kāds ir šīs
virknes 2018. loceklis?

<!--
questionType=Find.Only
-->



# <lo-sample/> LV.AO.2018.10.4

Pierādīt, ja $x$ - naturāls skaitlis, tad
$x^8 - x^2$ dalās ar $252$.

<small>

* [notation.divrules.3or9.divides](#)
* [div.prop.prod](#)
* [mod.congr.poly](#)

</small>

<!--
questionType=Prove.ForAll
-->


## Pārbaudām dalāmību ar 252 reizinātājiem

> **Apgalvojums:** Lai naturāls skaitlis $N$ dalītos ar $252=2^2\cdot{}3^2\cdot{}7^1$
> ir nepieciešami un pietiekami, lai $N$ dalītos ar pirmreizinātāju 
> augstākajām pakāpēm: $2^2 = 4$, $3^2 = 9$ un $7^1 = 7$. 

* $x^8 - x^2$ dalās ar $4$:
    - Ja $x$ ir pāru skaitlis, tad $x^2$ dalās ar $4$. 
    - Ja $x$ ir nepāru skaitlis, tad $(x^4-x)(x^4+x)$ ir divu pāru skaitļu reizinājums. Tātad arī dalās ar $4$.
* $x^8 - x^2$ dalās ar $9$:  
    - Ja $x$ dalās ar $3$, tad $x^2$ dalās ar $9$.
    - Ja $x = 3k+1$, tad $x^3 - 1 = (3k+1)^3 - 1$ dalās ar $9$ (pārbauda, atverot iekavas)
    - Ja $x = 3k-1$, tad $x^3 + 1 = (3k-1)^3 + 1$ dalās ar $9$ (pārbauda, atverot iekavas)


## Dalāmība ar 7

Pamatosim, ka $x^8 - x^2 = x^2(x^6-1)$ dalās arī ar $7$.

* Ja $x$ dalās ar $7$, tad $x^2$ dalās ar $7$. 
* Ja $x$ nedalās ar $7$, varam izmantot Mazo Fermā teorēmu pie $p=7$. 

> **Mazā Fermā teorēma:** Ja $p$ ir pirmskaitlis un $a$ nedalās ar $p$, tad
> $a^{p-1}$ dod atlikumu $1$, dalot ar $p$. 

Citiem vārdiem, $a^{p-1}-1$ dalās ar $p$.  
Ievietojot $p-7$, iegūstam, ka 
$a^6 - 1$ dalās ar $7$, ja vien $a$ nedalās ar $7$.


## Empīriska teorēmas pārbaude, ja p=7

Mazo Fermā teorēmu atcerēties ir derīgi, bet var pamatot citādi.

Pārbaudīsim, ka $x^6$ dod atlikumu $1$, dalot ar $7$ 
visiem $x=1,2,3,4,5,6$. (Lielākām $x$ vērtībām $x$ var aizstāt
ar tā atlikumu, polinoma $x^6$ vērtības atlikums no tā nemainīsies). 

<table>
<tr><th>$x$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr>
<tr><th>$x^3$</th><td>1</td><td>8</td><td>27</td><td>64</td><td>125</td><td>216</td></tr>
<tr><th>Atlikums $x^3\;\mbox{mod}\;7$</th><td>1</td><td>1</td><td>6</td><td>1</td><td>6</td><td>6</td></tr>
<tr><th>$(x^3\;\mbox{mod}\;7)^2$</th><td>1</td><td>1</td><td>36</td><td>1</td><td>36</td><td>36</td></tr>
<tr><th>Atlikums $x^6\;\mbox{mod}\;7$</th><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
</table>


## Polinoma vērtību atlikumi 

> **Apgalvojums:** Ja $P(x)$ ir polinoms ar veseliem koeficientiem, 
> ja $x_1, x_2, m$ ir naturāli skaitļi, pie tam $x_1$ un $x_2$ dod vienādus 
> atlikumus, dalot ar $m$ , tad 
> arī polinomu vērtības $P(x_1)$ un $P(x_2)$ dod vienādus atlikumus, dalot ar $m$. 

> **Definīcija:** Apgalvojumu, ka $x_1$ un $x_2$ dod vienādus atlikumus, dalot ar $m$ pieraksta šādi:
> $x_1 \equiv x_2\;(\mbox{mod}\,m)$. To lasa: $x_1$ un $x_2$ ir *kongruenti* pēc moduļa $m$. 

Šajos apzīmējumos katram polinomam $P(x)$ var secināt:

$$ x_1 \equiv x_2\;(\mbox{mod}\,m)\;\;\Rightarrow\;\;P(x_1) \equiv P(x_2)\;(\mbox{mod}\,m)$$



# <lo-sample/> LV.AO.2019.7.5

Kādai mazākajai naturālai $n$ vērtībai skaitli $10^n$
iespējams izteikt kā septiņu
naturālu skaitļu reizinājumu tā, lai to visu pēdējie cipari ir dažādi (tas ir,
nevienam no tiem pēdējais cipars nesakrīt ar kāda cita skaitļa pēdējo ciparu)?

<!--
questionType=Find.Min
-->


# <lo-sample/> LV.AO.2019.8.5

Kādai mazākajai naturālai $n$ vērtībai skaitli $10^n$
iespējams izteikt kā sešu
naturālu skaitļu reizinājumu tā, ka neviens 
no tiem nav mazāks kā $10$ un to
visu pēdējie cipari ir dažādi (tas ir, 
nevienam no tiem pēdējais cipars nesakrīt
ar kāda cita skaitļa pēdējo ciparu)?

<!--
questionType=Find.Min
-->


# <lo-sample/> LV.AO.2019.10.1

Pierādīt, ka visām naturālām $n$ vērtībām ir spēkā vienādība
$$6 + 24 + 60 + \cdots + n(n + 1)(n + 2) =$$
$$=\frac{n(n+1)(n+2)(n+3)}{4}.$$

<small>

* [misc.ind](#)

</small>

<!--
questionType=Prove.ForAll
-->

# <lo-sample/> LV.AO.2019.10.4

Kādām naturālām $n$ vērtībām izteiksme 
$n^2 + n + 19$ ir kāda naturāla skaitļa kvadrāts?

<small>

* [alg.tra.binom.square](#)

</small>

<!--
questionType=Find.All
-->










