# &nbsp;

<h1 style="font-size:28pt">Skaitļu teorija: 10.kl. LV</h1>

* 10.kl. skaitļu teorija (no 2010.g.)
    - <blue>LV.NO - novadu olimpiāde (2.posms)</blue>
    - LV.VO - valsts olimpiāde (3.posms)
    - LV.AO - atklātā olimpiāde



# <lo-sample/> LV.NO.2010.10.2

Dots, ka $a$ un $b$ ir naturāli skaitļi, $a^2$
dalās ar $b$ un $b^2$ dalās ar $a$. 
Pierādīt, ka $(a-b)^3$
dalās ar $a\cdot{}b$. Vai noteikti
$(a-b)^2$ dalās ar $a\cdot{}b$?

<small>

* [alg.expand.binom.cubes](#)
* [div.properties.add](#)
* [div.properties.product](#)

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


# <lo-sample/> LV.NO.2010.10.4

Atrisināt naturālos skaitļos vienādojumu $x^3 = y! + 2$.

<small>

* [misc.experiment](#)
* [mod.parity.cases](#) 
* [alg.powers.prod](#)
* [div.idx.properties.product](#)
* [div.idx.properties.sumdiff](#)
* [mod.equation.contradict](#)

</small>



## Faktoriālu un pilno kubu tabulas

<table>
<tr><th>$x$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>
<tr><th>$x^3$</th><td>1</td><td>8</td><td>27</td><td>64</td><td>125</td><td>216</td><td>343</td><td>512</td><td>729</td><td>1000</td></tr>
</table>

<table>
<tr><th>$y$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>
<tr><th>$y!$</th><td>1</td><td>2</td><td>6</td><td>24</td><td>120</td><td>720</td><td>5040</td><td>40320</td><td>362880</td><td>3628800</td></tr>
<tr><th>$y!+2$</th><td>3</td><td>4</td><td>8</td><td>26</td><td>122</td><td>722</td><td>5042</td><td>40322</td><td>362882</td><td>3628802</td></tr>
</table>

* Redzam, ka $2^3 = 3!+2$ (ja $x=2, y=3$). 
* Vai ir citas saknes, kur $y>3$? 
* Aplūkojam $x$ paritāti. Vienīgā iespēja: $x$ ir pāru skaitlis: $x=2k$.
    - Tad $(2k)^3 = y!+2$ jeb $8k^3 = y! + 2$.
    - Kreisā puse dalās ar $8$, bet labā (pie $y>3$) dod atlikumu $2$, dalot ar $8$.



# <lo-sample/> LV.NO.2012.10.3

Doti seši pēc kārtas sekojoši naturāli skaitļi. Pierādīt, ka var atrast tādu
pirmskaitli $p$, ka tieši viens no dotajiem skaitļiem dalās ar $p$.

<small>

* [seq.arithm.mod.gaps](#)
* [misc.contradiction](#)

</small>


# <lo-sample/> LV.NO.2012.10.4

Ir aprēķinātas skaitļu $2^{2012}$ un $5^{2012}$ vērtības 
un iegūtie skaitļi uzrakstīti viens aiz otra. 
Cik cipari uzrakstīti?

### LV.NO.2013.10.4

Ansītis aprēķināja skaitļu $2^{2013}$ un $5^{2013}$ vērtības 
un iegūtos skaitļus uzrakstīja
vienu aiz otra. Cik cipari uzrakstīti?

<small>

* [misc.experiment](#)
* [notation.dec.numdigits.prod](#)

</small>



# <lo-sample/> LV.NO.2014.10.2

Pierādīt, ka, izvēloties $52$ no aritmētiskās progresijas 
$1, 4, 7, 10, \ldots$ locekļiem, kas nepārsniedz
$300$, vienmēr starp šiem skaitļiem var atrast divus skaitļus, kuru summa ir $302$.

<small>

* [seq.arithm.expr](#)
* [seq.arithm.numestimate](#)
* [seq.arithm.pairsum](#)
* [misc.pigeonhole](#)

</small>



## Progresijā ir 100 locekļu zem 300

$$1, 4, 7, \ldots, 148, 151, 154, \ldots, 298$$

* Diviem locekļiem - $1$, $151$ - nav pāra, ar ko summa ir $302$.
* Vēl ir 49 pārīši - $(4,298)$, $(7,295)$, $\ldots$, $(148,154)$.
* Izvēloties $52$ skaitļus, vismaz $50$ no tiem būs $\neq 1$, $\neq 151$. 
* Dirihlē princips - divi būs no viena pārīša.


# <lo-sample/> LV.NO.2015.10.2

Ar naturālu skaitli atļauts veikt šādas darbības:

* pieskaitīt $6$;
* dalīt ar $4$, ja skaitlis dalās ar $4$;
* mainīt vietām skaitļa ciparus (skaitļa sākumā nedrīkst atrasties nulle).

Vai, atkārtoti izpildot šīs darbības, no skaitļa $30$ var iegūt skaitli $2015$?

<small>

* [notation.divrules.3or9.divides](#)
* [misc.invariant](#)

</small>



## Invariants ir dalāmība ar $3$

Ja sākotnējais skaitlis $x$ dalījās ar $3$, tad pēc katras darbības arī rezultāts dalīsies ar $3$:

* $x+6$ dalās ar $3$, ja $x$ dalās ar $3$
* $x/4$ dalās ar $3$, ja $x$ dalās ar $3$ (un arī ar $4$, lai varētu izdalīt).
* $x'$ (pārkārtotiem cipariem) arī dalās ar $3$, jo ciparu summa nemainās.

$30$ dalās ar $3$, bet $2015$ nedalās. Tātad pārveidot par $2015$ nevar. 



# <lo-sample/> LV.NO.2015.10.3

Vairāku pēc kārtas sekojošu naturālu skaitļu summa ir $177$. 
Kādas vērtības var pieņemt
mazākais no šiem saskaitāmajiem?

<small>

* [seq.arithm.summation](#)
* [div.pfactor.algorithm](#)
* [misc.exhaustive](#)

</small>


## Aritmētiskas progresijas locekļu summa

$$S=a_1 + a_2 + \ldots + a_n = \frac{a_1 + a_n}{2}\cdot{}n$$

> Aritmētiskās progresijas summu iegūst, reizinot "vidējo elementu": 
> $a_v = \frac{a_1+a_n}{2}$ ar progresijas locekļu skaitu: $S = a_v\cdot{}n$.  
> Ja $n$ ir nepāru skaitlis, tad vidējais elements $a_v$ tiešām progresijā ir.  
> Ja $n$ ir nepāru skaitlis, tad "vidējais elements" ir abu vidējo locekļu 
> aritmētiskais vidējais. 

Abos gadījumos $2\cdot{}177 = (a_1+a_n)\cdot{}n$ jeb
$$2 \cdot 3 \cdot 59 = (a_1+a_n)\cdot{}n$$


## Gadījumu pārlase

Skaitlim $2 \cdot 3 \cdot 59$ ir tikai galīgs skaits dalītāju $n$:

* Ja $n=2$, tad $177 = 88\frac{1}{2}\cdot{}2 = 88+89$,
* Ja $n=3$, tad $177 = 59\cdot{}3 = 58+59+60$,
* Ja $n=6$, tad $177 = 29\frac{1}{2}\cdot{}6=$
$=27+28+29+30+31+32$. 

Vēl lielāki $2 \cdot 3 \cdot 59$ dalītāji ($n=59$ u.c.) novestu pie ļoti garām aritmētiskām 
progresijām, kurās būtu arī negatīvi locekļi.
Tās neder, jo $177$ bija vairāku pēc kārtas sekojošu **naturālu** skaitļu summa.


# <lo-sample/> LV.NO.2015.10.4

Vai eksistē tāds vesels skaitlis $x$, ka visi skaitļi

1. $x$, $x+23$, $x+45$, $x+121$
2. $x$, $x+23$, $x+46$, $x+121$

ir veselu skaitļu pakāpes ar naturālu kāpinātāju, 
kas lielāks nekā 1 (kāpinātāji var būt dažādi)?

<small>

* [misc.experiment](#)
* [div.primes.powers.higher](#)
* [mod.parity.cases](#)
* [misc.contradiction](#)

</small>


## Ievieto nelielas vērtības

* $x$ arī ir vesela skaitļa pakāpe
* Pārbaudām $x=1,4,8,9,16,25,32,36,49,\ldots$
* Jau $x=4$ der (pirmajā piemērā)

## Kas notiek otrajā piemērā?

* Vai $x$ un $x+46$ var *vienlaikus* būt naturālu skaitļu pakāpes?
* Ja $x$ ir pāru, tad **gan** $x$, **gan** $x+46$ dalās ar $4$.
* Ja $x$ ir nepāru, tad **gan** $x+23$, **gan** $x+121$ dalās ar $4$.



# <lo-sample/> LV.NO.2016.10.1

Pierādīt, ka katram naturālam $n$ ir patiesa vienādība
$$1\cdot{}4 + 2\cdot{}7 + 3\cdot{}10 + \cdots + n\cdot{}(3n + 1) = n(n+1)^2.$$

<small>

* [seq.summation.difference](#)
* [misc.induction](#)

</small>


## Definējam virkni 

$$a_n = 1\cdot{}4 + 2\cdot{}7 + 3\cdot{}10 + \cdots + n\cdot{}(3n + 1)$$

* Katrs nākamais šīs virknes loceklis ir par $n\cdot{}(3n+1)$ lielāks kā iepriekšējais

Tikpat liela ir starpība starp $n(n+1)^2$ un izteiksmi, kur $n$ aizstāj ar $n-1$: $(n-1)n^2$:

$$n(n+1)^2 - (n-1)n^2 = n(n^2 + 2n + 1) - n^3 + n^2 =$$
$$= n^3+2n^2+n - n^3+n^2 = 3n^2 + n = n(3n+1).$$

## Matemātiskā indukcija

* Ja $n=1$, tad $a_1 = 1\cdot{}4 = 4$ un arī $n(n+1)^2 = 4$. 
* Arī vēlāk gan virkne $a_n$, gan formula $n(n+1)^2$ pieaug vienādiem soļiem. 


# <lo-sample/> LV.NO.2016.10.2

Pierādīt, ka no jebkuriem trim naturālu skaitļu kvadrātiem var izvēlēties divus tā, 
ka to summa vai starpība dalās ar $5$.

<small>

* [mod.expr.square](#)
* [mod.cases.squares](#)
* [misc.pigeonhole](#)

</small>


## Pilnu kvadrātu atlikumi, dalot ar 5

$$(1^2,2^2,3^2,4^2,5^2)=(1,4,9,16,25).$$

* Atlikumi, dalot ar $5$, ir sekojoši: $(1,4,4,1,0)$. Pēc tam tie atkārtojas.
* Starp tiem ir tikai $3$ dažādi atlikumi: $0,1,4$. 
* Izvēloties trīs kvadrātus:
    - Vai nu divi no tiem sakritīs,
    - No katra būs pa vienam - tad $1+4$ dalās ar $5$.




# <lo-sample/> LV.NO.2017.10.5

Desmitciparu skaitlī vienādus ciparus aizvietojot ar vienādiem burtiem, 
bet dažādus – ar dažādiem, ieguva
vārdu $MATEMĀTIKA$ (īsais "A" un garais "Ā" aizstāj atšķirīgus ciparus). 
Papildus zināms, ka skaitlis $\overline{MA}$
dalās ar $2$, $\overline{MAT}$ - ar 3, $\overline{MATE}$ - ar 4, 
$\overline{MATEM}$ - ar 5, $\overline{MATEMĀ}$ - ar 6, $\overline{MATEMĀT}$ - ar 7,
$\overline{MATEMĀTI}$ - ar 8, $\overline{MATEMĀTIK}$ - ar 9, 
$\overline{MATEMĀTIKA}$ - ar 10. Noteikt, kāds bija sākotnējais
desmitciparu skaitlis!

<small>

* [notation.divrules.2or5or10.divides](#)
* [notation.divrules.pow2or5.divides](#)
* [notation.divrules.3or9.divides](#)
* [notation.divrules.composite](#)
* [misc.exhaustive](#)

</small>


## Gadījumu pārlase

* $\overline{MATEMĀTIKA}$ dalās ar $10$ ($A=0$)
* $\overline{MATEM}$ dalās ar $5$ ($M=5$)
* $\overline{MAT}=\overline{50T}$ dalās ar $3$ ($T = 1,4,7$)
* Dalāmība ar $2,4,6,8$ ($E$, $Ā$, $I$ ir pāru cipari $\neq 0$)
* Dalāmība ar $4$ ($TI$ un $TE$ dalās ar $4$, t.i $T \neq 4$)
* Dalāmība ar $6$ ($\overline{MATEMĀ}$ ciparu summa ir $5+0+(1|7)+(2|6)+5+(4|8)$
t.i. $\overline{EMĀ}=258$ vai $\overline{EMĀ}=654$.
* Dalāmība ar $7$: $50(1|7)(2|6)5(4|8)(1|7)$
($\overline{MATEMĀT}$ ir $5012581$ vai $5076547$)
* Dalāmība ar $8$: $50125816$, $50765472$
* $5076547290$ der (bet $5012581680$ neder, jo cipari $K$ un $Ā$ nedrīkst sakrist).



# <lo-sample/> LV.NO.2018.10.4

No cipariem $1, 2, 3, 4, 5, 6, 7, 8, 9$, katru izmantojot 
divas reizes, izveidoti trīs sešciparu skaitļi. Ar kādu lielāko
nuļļu skaitu var beigties trīs izveidoto skaitļu summa?

<small>

* [notation.divrules.3or9.divides](#)
* [notation.dec.numdigits.sum](#)
* [misc.contradiction](#)
* [misc.construct.alpha](#)

</small>

## No pretējā

* Katrs sešciparu skaitlis ir mazāks par 1 miljonu. 
* 3 šādu skaitļu summa ir zem 10 miljoniem (7-cipari). 
* Vai var beigties ar 6 nullēm?
* Ciparu summas dēļ jādalās ar $9$, bet $9000000$ ir par daudz.

## Vai var beigties ar 5 nullēm? 

Konstruējam, ikreiz liekot mazākos iespējamos ciparus.

![Saskaitīšana stabiņā](LV.NO.2018.10.4.svg)



# <lo-sample/> LV.NO.2019.10.5

Atrast visus pirmskaitļu pārus $(m,n)$, kuriem 
$20m + 18n = 2018$.

<small>

* [notation.divrules.2or5or10.divides](#)
* [div.primes.factorize.small](#)

</small>

## Risinājums

* Īsinām $20m+18n=2018\;\Rightarrow\;10m+9n=1009$. 
* Lai $1009 - 9n$ dalītos ar $10$, $n$ pēdējais cipars ir "1":  
$m=(1009-9n)/10$ ir vesels, ja $n=1,11,21,31,41,51,61,71,81,91,101,111$
* Atbilstošie pāri: $(100,1)$, $(91,11)$, $(82,21)$, <red>$(73,31)$</red>, $(64,41)$, 
$(55,51)$, $(46,61)$, <red>$(37,71)$</red>, $(28,81)$, $(19,91)$, $(10,101)$, $(1,111)$. 

No tiem der tikai divi: $(73,31)$, $(37,71)$



