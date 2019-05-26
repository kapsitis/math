# Skaitļu teorija: 10.kl. LV

* 10.kl. skaitļu teorija (no 2010.g.)
    - LV.NO - novadu olimpiāde (2.posms)
    - LV.VO - valsts olimpiāde (3.posms)
    - LV.AO - atklātā olimpiāde


# <lo-sample/> LV.AO.2010.10.4

Cik dažādos veidos skaitli $2010$ var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu? Saskaitāmo secība nav svarīga. 

### LV.AO.2011.10.1

Cik dažādos veidos skaitli $2011$ var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu? Saskaitāmo secība nav svarīga. 

<small>

* [seq.arithm.summation](#)
* [div.pfactor.algorithm](#)
* [misc.exhaustive](#)

</small>





# <lo-sample/> LV.AO.2012.10.1

Pierādi: ja $p$ un $14p^2+1$ ir pirmskaitļi, tad $14p^2-1$ ir naturāla
skaitļa kubs.

<small>

* [mod.expr.square](#)
* [mod.expr.sum](#)

</small>


## Secinājumu ķēdīte:

* Ja $p$ nedalās ar $3$, tad $p^2$ atlikums, dalot ar $3$, ir $1$. 
* Tad $14p^2$ dod atlikumu $2$, dalot ar $3$, jo skaitli ar atlikumu $2$ 
reizina ar skaitli ar atlikumu $1$.
* Tad $14p^2+1$ dod atlikumu $0$, dalot ar $3$. Tas nav pirmskaitlis. 

Secinām, ka $p=3$ (citi pirmskaitļi nedalās ar $3$). Tādēļ 
$14p^2 +1 = 127$ un $14p^2 - 1 = 125$, kas tiešām ir pilns kubs $5^3$.





# <lo-sample/> LV.AO.2013.10.4

No pirmajiem $100$ naturālajiem skaitļiem izvēlēts $51$ skaitlis.
Pierādīt, ka no tiem var izvēlēties divus, no kuriem viens dalās ar
otru.

<small>

* [seq.geom](#)
* [misc.pigeonhole](#)

</small>


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





# <lo-sample/> LV.AO.2014.10.4

Doti septiņi dažādi naturāli skaitļi; katriem diviem no dotajiem skaitļiem aprēķināja to
summu. Kāds lielākais skaits no šīm summām var būt pirmskaitļi?

<small>

* [mod.parity.cases](#)
* [misc.graphs.bipartite](#)
* [misc.bounds](#)
* [mod.expr.sum](#)
* [misc.construct.iterative](#) 

</small>

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


# <lo-sample/> LV.AO.2015.10.3

Atrast visus naturālos skaitļus, kas ir vienādi ar savu ciparu reizinājumu.
(Par viencipara skaitļa ciparu reizinājumu sauc tā vienīgo ciparu.)

<small>

* [misc.experiment](#) 
* [alg.ineq.transitive](#)

</small>


## Nevienādību izmantošana

* Pārbaudot dažādus skaitļus var novērot, ka ciparu reizinājums allaž mazāks par pašu skaitli.
* Pamatojam to 2-ciparu un 3-ciparu skaitļiem $\overline{ab}$ un $\overline{abc}$

$$a\cdot{}b < 10a \leq 10^1\cdot{}a + b = \overline{ab},$$
$$a\cdot{}b\cdot{}c < 10^2\cdot{}a < 100a + 10b + c = \overline{abc}.$$

Skaitļa pirmo decimālciparu reizinot ar $k$ turpmākajiem cipariem, iegūsim 
mazāku rezultātu nekā reizinot ar $10^k$, jo katrs cipars ir mazāks par $10$. 





# <lo-sample/> LV.AO.2016.10.2

Vai var atrast tādus veselus skaitļus $x$, $y$ un $z$, ka
$x^3 − 2016xyz = 120$?

<small>

* [div.pfactor.algorithm](#)
* [notation.divrules.3or9.remainder](#)
* [mod.expr.poly](#)
* [mod.equation.contradict](#) - pretrunas modulis: atlikumi pēc 9

</small>





# <lo-sample/> LV.AO.2016.10.3

Aritmētiskās progresijas četri pēc kārtas ņemti locekļi ir veseli
skaitļi $A$, $B$, $C$ un $D$. Pierādīt, ka
$A^2+2B^2+3C^2+4D^2$
var izteikt kā divu
veselu skaitļu kvadrātu summu!

<small>

* [seq.arithm.expr](#)
* [alg.expand.binom.squares](#)
* [alg.completesquare](#)

</small>





# <lo-sample/> LV.AO.2017.10.5

Pierādīt, ja no trim naturāliem skaitļiem $n$; $n+11$ un $n+22$ divi ir
pirmskaitļi, tad trešais skaitlis dalās ar $6$.

<small>

* [div.pfactor.prop.divisibility](#)
* [seq.arithm.mod.all](#)
* [misc.exhaustive](#) (gadījumus $n=2,3$ aplūko atsevišķi)

</small>





# <lo-sample/> LV.AO.2018.10.4

Pierādīt, ja $x$ - naturāls skaitlis, tad
$x^8 - x^2$ dalās ar $252$.

<small>

* [notation.divrules.3or9.divides](#)
* [div.pfactor.prop.divisibility](#)
* [mod.expr.poly](#)

</small>


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



# <lo-sample/> LV.AO.2019.10.1

Pierādīt, ka visām naturālām $n$ vērtībām ir spēkā vienādība
$$6 + 24 + 60 + \cdots + n(n + 1)(n + 2) =
\frac{n(n+1)(n+2)(n+3)}{4}.$$

<small>

* [misc.induction](#)


</small>


# <lo-sample/> LV.AO.2019.10.4

Kādām naturālām $n$ vērtībām izteiksme 
$n^2 + n + 19$ ir kāda naturāla skaitļa kvadrāts?

<small>

* [alg.expand.binom.squares](#)

</small>



