# <lo-sample/> LV.AMO.2000.7.1

Dots, ka $a,b,c,d$ – naturāli skaitļi un $ab=cd$. Pierādīt, ka skaitli $a^2 + b^2 + c^2 + d^2$ 
var izsacīt kā divu veselu skaitļu kvadrātu summu. Vai to noteikti var izsacīt kā divu naturālu skaitļu kvadrātu summu?

<small>

* topic:StandardIdentities
* questionType:Prove
* domain:NT
* concepts:square-Alg

</small>



## Atrisinājums

Izteiksmei var pieskaitīt $2ab$ un atņemt tam vienādo $2cd$, tad atdalīt kvadrātus:

$$a^2 + 2ab + b^2 + c^2 - 2cd + d^2 = (a+b)^2 + (c-d)^2.$$

Tādēļ vienmēr to var izteikt kā divu veselu skaitļu kvadrātu summu.

Ne vienmēr $a^2 + b^2 + c^2 + d^2$ var būt divu naturālu kvadrātu summa. Piemēram,
$1^2+1^2+1^2+1^2 = 4$ nav izsakāms kā $m^2 + n^2$, kur $m, n \in \mathbb{N}$.






# <lo-sample/> LV.AMO.2000.7.2

Atrast mazāko naturālo skaitli, kam visi cipari ir vienādi un kas dalās ar $49$?

<small>

* topic:LittleFermatAndEuler
* topic:IntegerFactorization
* genre:optimization
* questionType:FindOptimal
* domain:NT
* concepts:decimal-notation,digit,divisibility

</small>



## Atrisinājums

Aprēķinām atlikumus, dalot $1,11,111,1111,11111,111111$ ar $7$. 
Atlikumi ir $1,4,6,5,2,0$. Tādēļ $111111$ dalās ar $7$ un 
septiņreiz lielāks skaitlis $777777$ dalās ar $49$. 

*Piezīme.* Fakts, ka $111111$ dalās ar $7$ seko no 
tā, ka $10^6 - 1 = 999999$ dalās ar $7$. 
Šī apgalvojuma vispārinājums ir Mazā Fermā teorēma: 
Katram pirmskaitlim $p$ un katram $a$, kas nedalās ar $p$, 
$a^{p-1} - 1$ dalās ar $p$. 



# <lo-sample/> LV.AMO.2000.7.4

Vai naturālos skaitļus

**(A)** no $1$ līdz $12$ ieskaitot,
**(B)** no $1$ līdz $50$ ieskaitot

var tā sadalīt pa pāriem, lai visas pāros ieejošo skaitļu summas būtu dažādas un katra no tām būtu pirmskaitlis?
(Piemēram, skaitļus no $1$ līdz $6$ varētu sadalīt tā: $1+2=3$, $3+4=7$, $5+6=11$).

<small>

* topic:PrimesDistribution
* topic:NumTheoryPigeonhole
* topic:ExhaustionMethod
* concepts:partition,primes,sum
* questionType:ProveDisprove
* domain:NT
* genre:construction

</small>



## Atrisinājums

**(A)** Var sadalīt, piemēram, tā: $(1,4)$, $(2,5)$, $(3,8)$, $(6,7)$, $(9,10)$, $(11,12)$. 

**(B)** Bet $(1,100)$ ir tikai $24$ pirmskaitļi, kas lielāki par $2$.
Tāpēc nav iespējams izveidot $25$ pārus no skaitļiem $[1;50]$ tā, lai iegūtu $25$ dažādus 
pirmskaitļus -- tas būtu pretrunā ar Dirihlē principu.



# <lo-sample/> LV.AMO.2000.8.3

Uz katras no vairākām kartītēm uzrakstīts pa naturālam skaitlim (starp tiem var būt arī vienādi); uz visām kartītēm uzrakstīto skaitļu summa ir $100$. Vai noteikti var atrast tādas kartītes (varbūt vienu pašu), uz kurām uzrakstīto skaitļu summa ir $50$, ja kartīšu skaits ir

**(A)** $50$,
**(B)** $51$?


<small>

* topic:NumTheoryMathInduction
* topic:NumTheoryPigeonhole
* genre:construction
* questionType:ProveDisprove
* domain:Comb
* strategy:Interpretation
* concepts:sum

</small>




## Atrisinājums

**(A)** Ne vienmēr. Ir šāds pretpiemērs: $49$ kartītes ar "1" un $1$ kartīte ar "51". 

**(B)** Ieviešam sekojošu interpretāciju: Uzzīmējam riņķa līniju, kuru regulāra $100$-stūra
virsotnes sadala $100$ vienādos lokos. Vispirms nokrāsojam vienu no regulārā $100$-stūra virsotnēm sarkanu un 
atbilstoši katras kartītes skaitlim $n_i$ ($i=1,2,\ldots,51$) nokrāsojam sarkanu virsotni, kuru no 
iepriekšējās atdala $n_i$ vienādie loki (virzoties pretēji pulksteņa rādītāju virzienam).
Saliekot visus $51$ lokus, pēdējā sarkanā virsotne būs tā, kuru atzīmēja pašā sākumā 
(jo visu skaitļu $n_i$ summa ir tieši $100$). 

Esam ieguvuši $51$ sarkanu punktu uz riņķa līnijas. 
Visas $100$-stūra virsotnes var sagrupēt pa pāriem (kur vienā pārī ietilpst divas virsotnes, kuras 
ir tieši pretī viena otrai -- kuras atdala tieši $50$ riņķa līnijas loki). 
Pēc Dirihlē principa, vismaz vienā no pāriem abas pretējās virsotnes būs sarkanas, jo pāru 
pavisam ir $50$ (un katrai sarkanajai virsotnei nevar iedot pārī ne-sarkanu). 

Iegūtais pāris ar abām sarkanajām virsotnēm, kas ir tieši pretī viena otrai der kā atrisinājums, 
jo no vienas uz otru var aiziet tieši $50$ soļos, izmantojot skaitļus $n_i$. 




# <lo-sample/> LV.AMO.2000.9.2

Vai skaitli  
**(A)** skaitli $2$,  
**(B)** skaitli $\frac{1}{8}$  
var izsacīt kā četriem dažādiem naturālu skaitļu 
kvadrātiem apgriezto lielumu summu?

<small>

* concepts:sum,square-Alg,inverse-number
* questionType:ProveDisprove,ProveDisprove
* domain:Alg

</small>


# <lo-sample/> LV.AMO.2000.9.4

Apskatām pirmos $n$ naturālos skaitļus. No tiem jāizvēlas divus tā, 
lai to reizinājums būtu vienāds ar visu pārējo skaitļu summu. 
Vai tas ir iespējams, ja  
**(A)** $n=10$,  
**(B)** $n=15$?

<small>

* concepts:sum,product
* questionType:ProveDisprove,ProveDisprove
* domain:NT

</small>


# <lo-sample/> LV.AMO.2000.10.2

Divu pirmskaitļu starpība ir $100$. Uzrakstot pirmo 
galā otrajam, atkal iegūst pirmskaitli. 
Atrast šos pirmskaitļus un pierādīt, ka citu bez 
Jūsu atrastajiem nav.

<small>

* concepts:primes,digit-manipulation
* questionType:FindAll
* domain:NT

</small>




# <lo-sample/> LV.AMO.2000.11.1

Dots, ka $x^2+y^2+z^2 = t^2$, kur $x,y,z,t$ – naturāli skaitļi. 
Cik no skaitļiem $x,y,z,t$ var būt pāra skaitļi?

<small>

* concepts:even-number
* questionType:FindCount
* domain:NT

</small>




# <lo-sample/> LV.AMO.2000.11.4

Funkcijas $f(x)$ argumenti un vērtības ir naturāli skaitļi. 
Katram naturālam $x$ izpildās vienādība

$$f(f(x))+f(x) = 2x.$$

Atrast visas šādas funkcijas $f(x)$ un pierādīt, 
ka citu bez atrastajām nav.

<small>

* concepts:function,argument,value
* questionType:FindAll
* domain:NT

</small>




# <lo-sample/> LV.AMO.2000.12.2

Atrisināt naturālos skaitļos vienādojumu

$$\left( 2a+b \right) \cdot \left( 2b + a \right) = 2^c.$$

<small>

* concepts:equation
* questionType:FindAll
* domain:NT

</small>


# <lo-sample/> LV.AMO.2000.12.5

Naturālu skaitļu virkni sauc par $F$-virkni, 
ja tā ir augoša, bezgalīga un katrs tās loceklis, 
sākot ar trešo, vienāds ar abu iepriekšējo locekļu summu. 
Vai eksistē  
**(A)** galīgs daudzums,  
**(B)** bezgalīgs daudzums  
$F$-virkņu ar īpašību: katrs naturāls skaitlis pieder 
tieši vienai no tām.

<small>

* concepts:sequence
* questionType:ProveDisprove,ProveDisprove
* domain:NT

</small>



# <lo-sample/> LV.AMO.2001.7.2

Naturālu skaitli sauc par simetrisku, ja tā pēdējais cipars 
nav $0$ un, uzrakstot tā ciparus apgrieztā secībā, 
skaitlis nemainās. Piemēram, $1221$ ir simetrisks skaitlis, bet $1231$ - nav.  
**(A)** pierādiet: ja simetrisks sešciparu skaitlis dalās ar $13$, tad tas dalās arī ar $7$,  
**(B)** vai taisnība, ka katrs simetrisks sešciparu skaitlis, kas dalās ar $7$, dalās arī ar $13$?

<small>

* topic:DivisibilityRulesOther
* topic:NotationPolynomial
* topic:IntegerCongruence
* concepts:palindrome,decimal-notation
* questionType:Prove,ProveDisprove
* domain:NT

</small>




## Atrisinājums

**(A)** $13$ dala $\overline{abcabc}=1001\cdot{}\overline{abc}$ un 
arī $\overline{abccba}$ (tas ir dots). 
Atņemot abus skaitļus, iegūstam $13 \mid 99|a-c|$ un $a=c$.

**Piezīme:** Ievērojam, ka $\overline{abccba}$ var izteikt 
$100001a + 10010b + 1100c = 13\cdot (\ldots ) + 5(a-c)$. 
Tad $a-c$ dalās ar $13$ un $a=c$; aizstāj $c$ un dala ar $7$.

**(B)** $108801$ ir pretpiemērs.





# <lo-sample/> LV.AMO.2001.8.3

Andrim vajadzēja sareizināt divus dažādus pozitīvus trīsciparu skaitļus. 
Izklaidības pēc viņš tos vienkārši uzrakstīja vienu otram galā. 
Iegūtais sešciparu skaitlis izrādījās $3$ reizes lielāks par reizinājumu, 
kuru Andrim vajadzēja iegūt. Kādu sešciparu skaitli Andris uzrakstīja?

<small>

* topic:NotationShift
* topic:StandardIdentities
* topic:NumTheoryInequalityMethod
* questionType:FindAll
* domain:NT
* genre:digit-manipulation
* concepts:decimal-notation

</small>




## Atrisinājums

* Apzīmē $a$ un $b$ - abi ir trīsciparu skaitļi
* Ja $1000a+b=3ab$, tad $b/a=3b-1000$. 
* Veseli trīsciparu skaitļi $a,b$ rodas tikai tad, ja $b=334$.



# <lo-sample/> LV.AMO.2001.9.4

Dots, ka $x,y,z$ - naturāli skaitļi un katrs no 
skaitļiem $xy-z$, $xz-y$ un $yz-x$ dalās ar $3$. 
Pierādiet, ka $x^2+y^2+z^2$ dalās ar $3$.

<small>

* concepts:divisibility
* questionType:Prove
* domain:NT

</small>


# <lo-sample/> LV.AMO.2001.10.3

Kāds ir mazākais pirmskaitlis $p$, kuram nevar atrast tādus 
nenegatīvus veselus skaitļus $x$ un $y$, ka 
${\displaystyle p = \left| 2^x - 3^y \right|}$?

<small>

* concepts:primes
* questionType:FindOptimal
* domain:NT

</small>


# <lo-sample/> LV.AMO.2001.11.3

Skaitļu virknes elementi ir naturāli skaitļi. 
Pirmo elementu izvēlas patvaļīgi, bet katrs nākošais 
elements ir vienāds ar iepriekšējā elementa naturālo dalītāju skaitu. 
(Piemēram, ja virknes pirmais elements ir $14$, 
tad virkne ir $14, 4, 3, 2, 2, 2, \ldots$).
Kāds var būt virknes pirmais elements, 
ja neviens tās elements nav naturāla skaitļa kvadrāts?

<small>

* concepts:sequence,divisibility,square-Alg
* questionType:FindAll
* domain:NT

</small>


# <lo-sample/> LV.AMO.2001.12.2

Atrisināt naturālos skaitļos vienādojumu $(2a+b)(2b+a)=2c$.

<small>

* concepts:equation
* questionType:FindAll
* domain:NT

</small>


# <lo-sample/> LV.AMO.2002.7.4

Divi spēlētāji pamīšus raksta uz tāfeles pa vienam 
naturālam skaitlim no $1$ līdz $8$ ieskaitot. 
Nedrīkst rakstīt skaitļus, ar kuriem dalās kaut 
viens jau uzrakstīts skaitlis. 
Kas nevar izdarīt gājienu, zaudē.
Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

<small>

* genre:game
* concepts:divisibility
* questionType:Algorithm
* strategy:Contradiction
* domain:NT

</small>



## Atrisinājums

Ja skaitļiem $\{ 2,3,\ldots,7,8\}$ uzvar 1.sp., 
atkārto viņa stratēģiju. Ja uzvar 2.spēlētājs, sāk ar gājienu "$1$".


## Atrisinājums

Sāk ar $2$, tad uz katru $(5; 7)$, $(6; 8)$ un $(4; 3)$ atbild ar otru skaitli no pārīša.



# <lo-sample/> LV.AMO.2002.7.5

Kādu lielāko daudzumu dažādu naturālu skaitļu, kas nepārsniedz $100$, var izvēlēties tā, 
lai nekādu divu izvēlēto skaitļu starpība nebūtu ne $3$, ne $4$, ne $7$?

<small>

* topic:SequencePeriodicity
* topic:NumTheoryPigeonhole
* genre:optimization
* questionType:FindOptimal
* domain:Comb
* strategy:ExhaustiveSearch,Symmetry

</small>





## Atrisinājums

Ja $>30$, tad no $10$ sk., jāizvēlas $4$. No $\{1,4,8\}$, $\{2,5,9\}$, $\{2,6,10\}$, $\{7\}$ 
jāņem pa $1$ – neiespējami.

Lai izvēlētos $4$ no *ABCABCXABC*, jāņem arī $X$, bet līdzīgi arī *ABCYABCABC* 
un $X$,$Y$ starpība ir $3$.






# <lo-sample/> LV.AMO.2002.8.2

Andrim vajadzēja sareizināt divus dažādus divciparu skaitļus. Izklaidības pēc 
viņš tos vienkārši uzrakstīja vienu otram galā. Iegūtais četrciparu skaitlis izrādījās 
$3$ reizes lielāks par reizinājumu, kuru Andrim vajadzēja iegūt. 
Kādu četrciparu skaitli Andris uzrakstīja?

<small>

* topic:NotationShift
* topic:StandardIdentities
* topic:NumTheoryInequalityMethod
* seeAlso:LV.AMO.2001.8.3
* questionType:FindAll
* domain:NT
* genre:digit-manipulation
* concepts:decimal-notation

</small>



## Atrisinājums

Ja $100a+b=3ab$, tad $b/a=3b-100$. Abi cipari $a,b$ ir veseli tad, ja $b=34$.



# <lo-sample/> LV.AMO.2002.8.3

Par Fibonači skaitļiem sauc skaitļus $1; 2; 3; 5; 8; \ldots$ 
(katru nākošo iegūst, saskaitot divus iepriekšējos).
Vai var pastāvēt vienādība $a+b=c+d$,
ja $a$, $b$, $c$, $d$ ir dažādi Fibonači skaitļi?

<small>

* topic:NumTheoryExtremeElement
* concepts:fibonacci-sequence
* questionType:ProveDisprove
* domain:NT
* strategy:ExtremeElement

</small>





## Atrisinājums

Ja $d$ ir lielākais no Fibonači skaitļiem, tad $a+b=d$, 
kur $a$,$b$ ir Fibonači skaitļi tieši pirms $d$. Bet tā kā $c>0$ arī 
ir Fibonači skaitlis, tad $a+b<c+d$. 



# <lo-sample/> LV.AMO.2002.9.3

Dots, ka $x, y, z$ naturāli skaitļi un katrs no 
skaitļiem $xy-z$, $xz-y$ un $yz-x$ dalās ar $3$. 
Pierādīt, ka $x^2+y^2+z^2$ dalās ar $3$.

<small>

* seeAlso:LV.AMO.2001.9.4
* concepts:divisibility
* questionType:Prove
* domain:NT

</small>



# <lo-sample/> LV.AMO.2002.10.3

Katrs naturāls skaitlis nokrāsots vienā krāsā. 
Ir zināms: ja divu naturālu skaitļu starpība ir pirmskaitlis, 
tad tie ir nokrāsoti dažādās krāsās. 
Kāds ir mazākais iespējamais krāsu skaits?

<small>

* concepts:primes
* questionType:FindOptimal
* domain:NT

</small>



# <lo-sample/> LV.AMO.2002.11.3

Zināms, ka naturāls skaitlis $n$ dalās ar pirmskaitli 
$p$ un $p>\sqrt{n}$. Pierādīt, ka ne $n-1$, $n^3-1$ 
nav divu tādu naturālu skaitļu reizinājums, kuru starpība ir $2$.

<small>

* concepts:primes
* questionType:Prove
* domain:NT

</small>



# <lo-sample/> LV.AMO.2002.12.4

Skaitļu virkni $a_1, a_2, a_3, \ldots$ veido sekojoši 
$a_1=0$; $a_2=1$; pie $n>2$ skaitli $a_n$ iegūst, 
pierakstot skaitlim $a_{n-1}$ pa labi galā skaitli $a_{n-2}$. 
(Piemēram, $a_3=10$; $a_4=101$, $a_5=10110$ utt.) 
Kādiem $n$ skaitlis $a_n$ dalās ar $11$?

<small>

* concepts:sequence
* questionType:FindAll
* domain:NT

</small>


# <lo-sample/> LV.AMO.2003.7.3

Divi spēlētāji pamīšus raksta uz tāfeles pa vienam naturālam 
skaitlim no $1$ līdz $9$ ieskaitot. Nedrīkst rakstīt skaitļus, ar kuriem dalās 
kaut viens jau uzrakstīts skaitlis. Kas nevar izdarīt gājienu, zaudē. 
Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

<small>

* genre:game
* concepts:divisibility
* questionType:Algorithm
* domain:NT
* strategy:Contradiction

</small>



## Atrisinājums

Ja skaitļiem $\{ 2,3,\ldots,8,9\}$ 
uzvar 1.spēlētājs, atkārto viņa stratēģiju. Ja uzvar 2.spēlētājs, 
sāk ar gājienu "1".


## Atrisinājums

Sāk ar $2$, tad katrā grupā $(5;7)$, $(3;8)$ un $(4;6;9)$ uzvar izolēti.






# <lo-sample/> LV.AMO.2003.7.5

Uz tāfeles pa reizei uzrakstīti visi naturālie skaitļi no $1$ līdz $n$ ieskaitot. 
Ar vienu gājienu var izvēlēties divus uz tāfeles uzrakstītus skaitļus 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt $\left| a^2-b^2 \right|$. 
Pēc $n-1$ gājiena uz tāfeles paliek viens skaitlis.  
Vai tas var būt $0$, ja **(A)** $n=8$, **(B)** $n=9$?

<small>

* topic:InvariantParity
* topic:SeriesMembersSumsClosedFormulas
* topic:ExhaustionMethod
* concepts:absolute-value
* genre:making-moves
* questionType:Algorithm
* domain:NT
* strategy:Invariant

</small>

## Ieteikums

Skaitļu komplektā var ar programmēšanas līdzekļiem 
atrast mazāko, ko var iegūt ar šiem gājieniem.



## Atrisinājums

**(A)**
Pie $n=8$ sākotnējais skaitļu komplekts ir $\{ 1,2,3,4,5,6,7,8 \}$. 
Izdarām šādus gājienus: 

* $(4,5) \rightarrow 5^2 - 4^2 = 9$, jaunie skaitļi ir $\{1,2,3,6,7,8,9\}$,
* $(7,9) \rightarrow 9^2 - 7^2 = 32$, jaunie skaitļi ir $\{1,2,3,6,8,32\}$,
* $(2,6) \rightarrow 6^2 - 2^2 = 32$, jaunie skaitļi ir $\{1,3,8,32,32\}$,
* $(1,3) \rightarrow 3^2 - 1^2 = 8$, jaunie skaitļi ir $\{8,8,32,32\}$,
* $(8,8) \rightarrow 8^2 - 8^2 = 0$, jaunie skaitļi ir $\{0,32,32\}$,
* $(32,32) \rightarrow 32^2 - 32^2 = 0$, jaunie skaitļi ir $\{0,0\}$,
* $(0,0) \rightarrow 0^2 - 0^2 = 0$, paliek skaitlis $\{ 0 \}$.


**(B)**
Ja $n=9$, tad visu skaitļu summa ir $1+2+\ldots+9=45$. 
Izdarot gājienu (nodzēšot $a$ un $b$ un uzrakstot $\left| a^2-b^2 \right|$) 
summas paritāte nemainās. Tāpēc pēc katra soļa visu uz tāfeles uzrakstīto 
skaitļu summa būs nepāra skaitlis.





# <lo-sample/> LV.AMO.2003.8.3

Kādā lielākajā daudzumā dažādu naturālu saskaitāmo, 
kas visi lielāki par $1$, var sadalīt skaitli $56$ tā, lai katru divu 
saskaitāmo lielākais kopīgais dalītājs būtu $1$?

<small>

* topic:NumTheoryExtremeElement
* topic:PrimesDistribution
* genre:optimization
* concepts:gcd,coprimes
* questionType:FindOptimal
* domain:NT
* strategy:ExtremeElement

</small>



## Atrisinājums

Ar sešu saskaitāmo summu var izteikt $56$ šādi:
$3,5,7,11,13,17$. 

Ar septiņiem vai vairāk saskaitāmajiem nevar, jo 
pat izvēloties visus septiņus mazākos pirmskaitļus, to 
summa ir $2+3+5+7+11+13+17 = 58 > 56$. 



# <lo-sample/> LV.AMO.2003.8.5

Uz katras no divām lapām jāuzraksta pa $n$ veseliem pozitīviem skaitļiem. 
Visiem $2n$ uzrakstītajiem skaitļiem jābūt dažādiem. Pie tam uz lapām uzrakstīto 
skaitļu summām jābūt vienādām savā starpā, un uzrakstīto skaitļu 
kvadrātu summām arī jābūt vienādām savā starpā.  
Vai tas iespējams, ja **(A)** $n=3$, **(B)** $n=4$, **(C)** $n=2003$?

<small>

* topic:SequencePeriodicity
* topic:ExhaustionMethod
* topic:StandardIdentities
* concepts:square
* questionType:ProveDisprove,ProveDisprove,ProveDisprove
* domain:NT
* strategy:Symmetry

</small>





## Atrisinājums

**(A)** Aplūkojam divas grupas: $\{ 1,5,6 \}$, $\{ 2,3,7 \}$.
Abās grupās skaitļu summas ir $12$, bet kvadrātu summas ir $62$. 

**(B)** Aplūkojam grupas $(1,4,6,7)$, $(2,3,5,8)$. 

**(C)** Arī šai vērtībai $n = 2003$ to var izdarīt. 
Pamatosim ar indukciju, ka to var izdarīt katram $n = 4m+3$, ja $m \geq 0$ ir 
vesels skaitlis.

*Bāze:* Pie ie $n=3$ var izdarīt kā punktā **(A)**.  
*Induktīvais pieņēmums:* Pieņemsim, ka to var izdarīt kādai vērtībai $n=3+4m$. 
Pamatosim, ka var izdarīt arī lielākai vērtībai:
$n=3+4(m+1)$.
*Induktīvā pāreja:* Sadala pirmos $3+4m$ skaitļus atbilstoši induktīvajam pieņēmumam. 
Ar $k$ apzīmējam lielāko no skaitļiem, kas izmantoti šajā konstrukcijā. 
Pievienosim astoņus jaunus skaitļus, tos sadalot grupās (līdzīgi kā **(B)** punktā):

$$(k+1, k+4, k+6, k+7)\;\;\text{un}\;\;(k+2, k+3, k+5, k+8)$$. 

Visi šie astoņi skaitļi ir savstarpēji dažādi. 

* Vienā grupā summa ir $(k+1) + (k+4) + (k+6) + (k+7) = 4k + 18$. Tāda pati summa ir arī 
  otrajā grupā: $(k+2) + (k+3) + (k+5) + (k+8)$. 
* Vienā grupā kvadrātu summa ir $(k+1)^2 + (k+4)^2 + (k+6)^2 + (k+7)^2 = 4k^2 + 36k + 102$. 
  Arī otrā grupā: $(k+2)^2 + (k+3)^2 + (k+5)^2 + (k+8)^2 = 4k^2 + 36k + 102$. 

Tāpēc pievienojot jaunās abas grupas katru savai pusei, gan skaitļu summas, gan 
to kvadrātu summas joprojām sakritīs.


# <lo-sample/> LV.AMO.2003.9.3

Noskaidrot, kādiem dažādiem pirmskaitļiem 
$p_1, p_2, \ldots, p_n$ pastāv īpašība: 
$p_1p_2p_3\ldots{}p_n$ dalās ar 
$(p_1-1)(p_2-1)\ldots(p_n-1)$.

<small>

* concepts:primes,divisibility
* questionType:FindAll
* domain:NT

</small>



# <lo-sample/> LV.AMO.2003.10.3

Dots, ka $n$ - vesels pozitīvs skaitlis un skaitļi 
$2n+1$ un $3n+1$ ir veselu skaitļu kvadrāti.  
**(A)** atrodiet kaut vienu tādu $n$,  
**(B)** vai $5n+3$ var būt pirmskaitlis?

<small>

* concepts:primes,square-Alg
* questionType:FindExample,ProveDisprove
* domain:NT

</small>


# <lo-sample/> LV.AMO.2003.11.3

Vai eksistē tāds naturāls skaitlis $n$, 
ka $6^n-1$ dalās ar $4^n-1$?

<small>

* concepts:divisibility
* questionType:ProveDisprove
* domain:NT

</small>



# <lo-sample/> LV.AMO.2003.12.2

Vai eksistē tāds vesels pozitīvs skaitlis $n$, 
ka skaitlim $n^2$ ir tikpat daudz naturālu dalītāju, 
kas dod atlikumu $1$, dalot ar $3$, 
cik naturālu dalītāju, kas dod atlikumu $2$, dalot ar $3$?


<small>

* concepts:divisibility,divisors
* questionType:ProveDisprove
* domain:NT

</small>





# <lo-sample/> LV.AMO.2004.7.3

Kādam mazākajam naturālajam $n$ visas daļas

$$\frac{5}{n+7}, \frac{6}{n+8}, \frac{7}{n+9}, \ldots, \frac{35}{n+37}, \frac{36}{n+38}$$

ir nesaīsināmas?

<small>

* topic:EuclideanAlgorithm
* topic:PrimesDistribution
* concepts:fractions,gcd
* questionType:FindOptimal
* domain:NT

</small>





## Atrisinājums

Izmantojam Eiklīda algoritmu.

* Visas daļas izskatās šādi: $\frac{k}{n+(k+2)}$. 
* Vajag, lai $\mbox{LKD}(k,n+(k+2))=1$. 
* $\mbox{LKD}(k,n+(k+2))=\mbox{LKD}(k,n+2)=1$, $k=5,\ldots,36$.

$n+2=37$ ir savstarpējs pirmskaitlis ar visiem $k$, t.i. $n=35$.




# <lo-sample/> LV.AMO.2004.8.3

Dots, ka $A$ un $B$ – naturāli divciparu skaitļi. Skaitli $X$ iegūst, 
pierakstot skaitlim $A$ galā skaitli $B$; skaitli $Y$ iegūst, 
pierakstot skaitlim $B$ galā skaitli $A$. 
Dots, ka $X-Y$ dalās ar $91$. Pierādīt, ka $A=B$.

<small>

* topic:NotationShift
* topic:IntegerFactorization
* concepts:decimal-notation,divisibility
* genre:digit-manipulation
* questionType:Prove
* domain:NT

</small>






## Atrisinājums

$(100A+B)-(100B+A) = 99(A-B)$ un $A-B$ dalās ar $91$. Divciparu skaitļiem tas nozīmē $A=B$.





# <lo-sample/> LV.AMO.2004.8.5

Virknē augošā kārtībā izrakstīti naturālie skaitļi no $1$ līdz $2004$ ieskaitot, 
katrs vienu reizi. Izsvītrojam no tās skaitļus, kas atrodas 
$1., 4., 7., 10., \ldots$ vietās. No palikušās virknes atkal
izsvītrojam skaitļus, kas tajā atrodas $1., 4., 7., \ldots$ vietās. 
Ar iegūto virkni rīkojamies tāpat, utt.,
kamēr paliek neizsvītrots viens skaitlis. Kurš tas ir?

<small>

* topic:MultiplesInInterval
* topic:DefiningRecurrentSequences
* topic:NonlinearRecurrences
* concepts:sequence
* genre:making-moves
* questionType:FindAll
* domain:NT
* strategy:WorkingBackwards

</small>





## Atrisinājums

Pirms pēdējās izsvītrošanas pēdējais skaitlis bija \#2, pirms tam \#3, \#5, \#8, \#12, utt.
**#GadījumuPārlase** Pēc $n$ svītrošanām pirmais palikušais ir $x_n$. Pamato $x_{n+1} = \left\lceil 3x_n/2 \right\rceil$ pāru un nepāru $x_n$.



# <lo-sample/> LV.AMO.2004.9.5

Kvadrāts sastāv no $n \times n$ rūtiņām. 
Katrā rūtiņā jāieraksta viens no skaitļiem $-1; 0; 1$ tā, lai $n$ rindās
un $n$ kolonnās ierakstīto skaitļu summas visas būtu dažādas.
Vai to var izdarīt, ja **(A)** $n=4$; **(B)** $n=5$?

<small>

* concepts:sum
* questionType:ProveDisprove,ProveDisprove
* domain:NT

</small>


# <lo-sample/> LV.AMO.2004.10.3

Dots, ka $n$ – naturāls skaitlis.  
**(A)** pierādīt, ka $n^2 + 11n + 30$ nav naturāls skaitlis,  
**(B)** atrast šī skaitļa pirmo ciparu aiz komata atkarībā no $n$.

<small>

* questionType:Prove,FindAll
* domain:NT

</small>


# <lo-sample/> LV.AMO.2004.10.5

Vai, izmantojot tikai $3$ dažādus ciparus, var uzrakstīt 
$16$ trīsciparu skaitļus, kas visi dod dažādus
atlikumus, dalot ar $16$?

<small>

* concepts:remainder,divisibility
* questionType:ProveDisprove
* domain:NT

</small>


# <lo-sample/> LV.AMO.2004.11.1

Vai eksistē tāds naturāls skaitlis $n$, ka $2004^n-1$ dalās ar $1500^n-1$?

<small>

* concepts:divisibility
* questionType:ProveDisprove
* domain:NT

</small>


# <lo-sample/> LV.AMO.2004.12.1

Dots, ka $n$ – naturāls skaitlis, $n>1$. Vai izteiksmi

$$\left( x^n + x^{n-1} + \ldots + x + 1 \right)^2 - x^n$$

noteikti var izsacīt kā divu polinomu reizinājumu tā, 
lai neviens no šiem polinomiem nebūtu
konstante un visi abu polinomu 
koeficienti būtu veseli skaitļi?

<small>

* concepts:integer-polynomial
* questionType:ProveDisprove
* domain:NT

</small>




# <lo-sample/> LV.AMO.2004.12.3

Funkcijai $f(n)$ gan argumenti, gan vērtības 
ir naturāli skaitļi, un katriem diviem naturāliem
skaitļiem $x$ un $y$ pastāv vienādība

$$xf(y)+yf(x)=(x+y)f(x^2+y^2).$$

Atrast visas šādas funkcijas $f$ un pierādīt, ka citu bez jūsu atrastajām nav.

<small>

* concepts:function,argument,value
* questionType:FindAll
* domain:NT

</small>


# <lo-sample/> LV.AMO.2004.12.4

Ar $n$ apzīmējam patvaļīgu nepāra naturālu skaitli, 
kas lielāks par $1$. Pierādīt: abi skaitļi $n$ un $n+2$
vienlaicīgi ir pirmskaitļi tad un tikai tad, ja 
$(n-1)!$ nedalās ne ar $n$, ne ar $n+2$.

<small>

* concepts:primes,divisibility
* questionType:Prove
* domain:NT

</small>



# <lo-sample/> LV.AMO.2005.7.4

Triju veselu pozitīvu skaitļu summa ir $407$. 
Ar kādu lielāko daudzumu nuļļu var beigties šo
skaitļu reizinājums?

<small>

* topic:DivisibilityRulesLastDigits
* topic:ModularArithmetic
* genre:optimization
* concepts:decimal-notation
* questionType:FindOptimal
* seeAlso:LT.VILNIUS.2008.12.1

</small>



## Atrisinājums

Ievērojam, ka $407 = 250+125+32$, tad $p = 1000000$. 

Pamatosim, ka vēl vairāk nuļļu dabūt nevar dabūt.

* Divi saskaitāmie nevar beigties ar "5", jo atlikušajam tad jābeidzas ar "7". 
  Tātad vismaz viens saskaitāmais beigsies ar nulli. 
* Vairāk kā sešus $5$-pirmreizinātājus nevar iegūt 
  ($125=5^3$ un $250=5^3\cdot{}2$ ir optimāli).




# <lo-sample/> LV.AMO.2005.8.3

Kā var sadalīt naturālos skaitļus no 1 līdz 9 ieskaitot divās daļās tā, 
lai vienas daļas visu skaitļu summa būtu vienāda ar otras daļas 
visu skaitļu reizinājumu?

<small>

* topic:TreeTraversalBacktracking
* concepts:partition
* genre:construction
* questionType:FindExample
* strategy:CaseAnalysis

</small>


## Atrisinājums

Ja $a,b,c$ ir reizināti, tad var $abc=32$ un $a+b+c=45-32=13$. $(a,b,c)=(1,4,8)$.



# <lo-sample/> LV.AMO.2005.9.1

Atrast mazāko naturālo skaitli, kas dalās ar $225$
un kura decimālajā pierakstā neizmanto nevienu
no cipariem $3; 4; 5; 6; 7; 8; 9$.

<small>

* concepts:divisibility,decimal-notation
* questionType:FindOptimal

</small>


# <lo-sample/> LV.AMO.2005.10.3

Kādiem naturāliem skaitļiem $n$ abi skaitļi 
$2^n-1$ un $2^n+1$ ir pirmskaitļi?

<small>

* concepts:primes
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2005.10.4

Funkcijas $f(t)$ definīcijas apgabals un vērtību 
apgabals ir kopa $\{ 1; 2; \ldots; n\}$, pie tam visas vērtības
ir dažādas. Vai iespējams, ka visi skaitļi $f(x)-x$, 
$x=1; 2; \ldots; n$, ir dažādi, ja  
**(A)** $n=15$, **(B)** $n=16$?

<small>

* concepts:function
* questionType:ProveDisprove,ProveDisprove

</small>



# <lo-sample/> LV.AMO.2005.11.4

Dots, ka $a < b \leq c < d$ ir pozitīvi veseli skaitļi, 
$ad=bc$ un $d - a \leq 1$. Pierādīt, ka $a$ ir vesela skaitļa
kvadrāts.

<small>

* concepts:square-Alg
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2005.12.1

Vai eksistē tāds vesels pozitīvs skaitlis $n$, 
ka skaitlim $n^2$ ir tikpat daudz naturālu dalītāju, 
kas dod atlikumu $1$, dalot ar $3$, 
cik naturālu dalītāju, kas dod atlikumu $2$, dalot ar $3$?

<small>

* seeAlso:LV.AMO.2003.12.2
* concepts:divisibility,remainder
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2005.12.5

Divi spēlētāji spēlē sekojošu spēli, izdarot gājienus 
pēc kārtas. Sākumā doti divi stieņi: viens ar
garumu $n$, otrs ar garumu $n+1$ ($n$ – pozitīvs vesels skaitlis). 
Ar vienu gājienu var vai nu salauzt
vienu stieni divos īsākos, kuru garumi ir pozitīvi 
veseli skaitļi, vai arī izslēgt no turpmākās spēles
gaitas $k$ stieņus, katram no kuriem garums ir $k$ 
($k$ – jebkurš vesels pozitīvs skaitlis). Spēlētājs,
kurš izdara pēdējo gājienu, uzvar.
Kurš spēlētājs uzvar, pareizi spēlējot?

<small>

