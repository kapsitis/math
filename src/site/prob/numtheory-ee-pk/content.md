# &nbsp;

<h1 style="font-size:28pt">Skaitļu teorija: Igaunijas olimpiādes, 10.kl.</h1>

* <blue>**EE.PK** - **Eesti Piirkonnavoor** (Igaunijas reģionu kārta)</blue>
* **EE.LO** - Eesti Lõppvoor (Igaunijas gala/valsts kārta)
* **EE.LVS** - Eesti Sügisene lahtine võistlus (Igaunijas rudens atvērtais konkurss)
* **EE.LVT** - Eesti Talvine lahtine võistlus (Igaunijas ziemas atvērtais konkurss)

[Matemaatikaolümpiaadid ](http://www.math.olympiaadid.ut.ee/html/index.php)




# <lo-sample/> EE.PK.2010.10.5

Pierādīt, ka jebkuram veselam $n \geq 3$ atradīsies tāds $n$-ciparu
skaitlis, kurš ir vesela skaitļa kvadrāts, un, pierakstot tam sākumā 
ciparu 1, arī rodas kāda vesela skaitļa kvadrāts.


<small>

* [misc.beginatend](#)
* [misc.experiment](#)
* [notation.algor.square5](#)
* [notation.dec.numdigits.square](#)
* [alg.factorize.sqdiff](#)

</small>

<!--
ru=
Доказать, что для каждого целого числа $n \geq 3$ найдётся такое $n$-значное
число, которое является квадратом целого числа и при добавлении в его
начало цифры 1 также получится квадрат некоторого целого числа.
-->

<!--
questionType=Prove.ForAll
-->


## Vienādojumu sistēmas

* Ja $n=3$, var aplūkot pilnus kvadrātus, kas satur četrus ciparus un
sākas ar "1": $32^2=1024$, $33^2 = 1089$, $34^2 = 1156$ un 
$35^2 = 1225$. Tas arī ir pirmais skaitlis, kuram nometot pirmo ciparu 
iegūst kvadrātu: $225 = 15^2$. 
* Redzam arī, ka $35^2 - 15^2 = (35-15)(35+15)=20\cdot 50 = 1000$. 
* Nākamā sistēmiņa: $a+b=200$, $a-b=50$. Tātad 
$$a = 125,\;\; b = 75,\;\;125^2 - 75^2=10000.$$


## Algebriskās identitātes

* Skaitļus $15$, $35$, $75$, $125$ u.c. var ātri kāpināt kvadrātā:

$75^2 = 5625$, jo $7 \cdot 8 = 56$.  
$125^2 = 15625$, jo $12 \cdot 13 = 156$.




# <lo-sample/> EE.PK.2011.10.3

Matemātikas stundā Jüri dalīja naturālu skaitli $n$ ar naturālu 
skaitli $m$, iegūstot dalījumu un atlikumu.  
a) Pierādīt, ka, ja dalījums un atlikums ir savā starpā vienādi, 
tad $n$ dalās ar $m+1$.  
b) Vai izpildās arī apgrieztais apgalvojums: Vienmēr, kad skaitlis
$n$ dalās ar $m+1$, tad dalījums un atlikums, ja $n$ dala ar $m$, ir 
savā starpā vienādi? 

<small>

* [mod.rem.expr](#)
* [mod.rem.values](#)

</small>

<!--
ru=
На уроке математики Юра должен был поделить положительное целое
число $n$ на положительное целое число $m$, чтобы найти частное и остаток.
а) Доказать, что если найденные частное и остаток равны между собой,
то число n делится на число m + 1.
б) Выполняется ли обратное утверждение: всегда, когда число n делится 
на число m + 1, частное и остаток при делении числа n на число
m равны между собой?
-->

<!--
questionType=Prove.ForAll,ProveDisprove.ForAll
-->

## Algebriski pateikts apgalvojums par atlikumu

Ja $n$ dalot ar $m$ rezultāts ir $a$ un atlikums ir $a$, tad
$$n = am + a$$
jeb $n = a(m+1)$. Redzam, ka $n$ dalās ar $(m+1)$. 

Otrā virzienā secināt nevar, jo var gadīties, ka $a\geq m$, bet
atlikumi, dalot ar $m$ var būt tikai no kopas $\{ 0,\ldots,m-1 \}$.

Teiksim, $n = 100$, $m=4$. Tad $100$ dalās ar $m+1= 5$. 
Bet dalījums ($100$ dalot ar $4$) ir $25$, bet atlikums ir $0$
un $0 \neq 25$. 




# <lo-sample/> EE.PK.2012.10.4

Cik ir veselu skaitļu komplektu $(a, b, c)$, 
kuri apmierina vienādojumu $(a + b)(b + c)(c + a) = 123456789$?

<small>

* [notation.divrules.2or5or10.divides](#)
* [mod.parity.cases](#)

</small>

<!--
ru=
Сколько существует комплектов целых чисел $(a, b, c)$, 
которые удовлетворяют уравнению $(a + b)(b + c)(c + a) = 123456789$?
-->

<!--
questionType=Find.Count
-->

## Dalāmības pazīmes

* $123456789$ ir nepāru skaitlis (pēdējais cipars)
* $123456789$  arī dalās ar $9$ (ciparu summa)

Ko var secināt par reizinājumu $(a+b)(b+c)(c+a)$? 

* Izdevīgāk lietot pazīmes, ka reizinājums ar kaut ko *nedalās* 
(jo tad neviens reizinātājs nedalās). 

## Paritāte

Ja $(a + b)(b + c)(c + a)$ ir nepāru skaitlis, tad 

* $a$ un $b$ ir atšķirīga paritāte
* $b$ un $c$ ir atšķirīga paritāte
* $c$ un $a$ ir atšķirīga paritāte

Iegūta pretruna: Ja $a$ ir pāru, tad $b$ ir nepāru, tad $c$ ir pāru, tad $a$ ir nepāru utml.


# <lo-sample/> EE.PK.2013.10.3

Atrast mazāko naturālo skaitli $n$, kuram starp jebkuriem $n$
veselu skaitļu kvadrātiem atradīsies divi tādi, kuru starpība
dalās ar $10$. 

<small>

* [mod.expr.square](#)
* [misc.exhaustive](#)
* [misc.pigeonhole](#)

</small>

<!--
ru=
Найти наименьшее натуральное число $n$, при котором среди любых n
квадратов целых чисел найдутся два таких, разность которых делится
на $10$.
-->

<!--
questionType=Find.Min
-->



## Dirihlē princips

* Ievērojam, ka skaitļa kvadrāta atlikums, dalot ar $10$, atkarīgs tikai no paša skaitļa atlikuma.
* Pārbaudām pilno kvadrātu atlikumus:

<table>
<tr><th>$x$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>
<tr><th>$x^2$</th><td>1</td><td>4</td><td>9</td><td>16</td><td>25</td><td>36</td><td>49</td><td>64</td><td>81</td><td>100</td></tr>
<tr><th>$x^2\;\mbox{mod}\;10$</th><td>1</td><td>4</td><td>9</td><td>6</td><td>5</td><td>6</td><td>9</td><td>4</td><td>1</td><td>0</td></tr>
</table>

* Starp šiem atlikumiem ir seši atšķirīgi: $1,4,9,6,5,0$.
* Ja izvēlas septiņus, tad divi sakritīs (Dirihlē princips). 



# <lo-sample/> EE.PK.2014.10.3

Vienādmalu trijstūra virsotnēs ierakstīti naturāli skaitļi $14$, $20$ un $n$.. 
Jebkuru divu virsotņu skaitļu reizinājums dalās ar skaitli trešajā virsotnē. 
Atrast visas iespējamās $n$ vērtības.

<small>

* [div.common.lcm](#)
* [div.common.lcm.mult](#)
* [misc.exhaustive](#)

</small>

<!--
ru=
В вершины равностороннего треугольника записаны положительные целые числа 14, 20 и $n$. 
Произведение чисел любых двух вершин делится на
число в третьей вершине. Найти все возможные значения числа $n$.
-->

<!--
questionType=Find.All
-->



## Par mazāko kopīgo dalāmo

* Prasības: $14 \cdot 20$ dalās ar $n$, $14n$ dalās ar $20$, $20n$ dalās ar $14$
* $n$ ir $280$ dalītājs, vienlaikus $n$ dalās ar $2$, $5$, $7$. 
* Tātad $n = 2 \cdot 5 \cdot 7 k = 70k$, kas ir $280$ dalītājs.
* Trīs $n$ vērtības: $(70, 140, 280)$. 




# <lo-sample/> EE.PK.2015.10.3

а) Zināms, ka $x^2 − y^2 = 100$, kur $x$ и $y$ ir naturāli skaitļi. Atrast izteiksmes 
$x − y$ mazāko iespējamo vērtību.  
b) Tas pats jautājums, ja $x$ un $y$ ir veseli skaitļi.

<small>

* [alg.factorize.sqdiff](#)
* [mod.parity.cases](#)
* [misc.exhaustive](#)
* [alg.linear](#)

</small>

<!--
ru=
а) Известно, что $x^2 − y^2 = 100$, где $x$ и $y$ − натуральные числа. Найти
наименьшее возможное значение выражения $x − y$.  
б) Тот же вопрос, при условии, что $x$ и $y$ − целые числа
-->

<!--
questionType=Find.Min
-->


## Dalīšana reizinātājos

1. $x^2 - y^2$ dalās reizinātājos: $(x-y)(x+y)$. Lai iegūtu $100$, 
gan $x-y$, gan $x+y$ ir $100$ dalītāji.
2. $x-y$ un $x+y$ ir vienāda paritāte; lai reizinājums būtu $100$, 
tie abi ir pāru skaitļi. 
3. Aplūkojam visus gadījumus, kā $100$ var izteikt kā divu pāru 
skaitļu reizinājumu: 
$$2 \cdot 50 = 10 \cdot 10 = (-2) \cdot (-50) = (-10) \cdot (-10)$$
4. Citi veidi: $1 \cdot 100$, $4 \cdot 25$ vai $5 \cdot 20$ neder, 
jo reizinātāju paritātes ir dažādas - neeksistēs veselos skaitļos atrisinājumi
lineāru vienādojumu sistēmai  $x-y=1$ un $x+y=100$ utml.


# <lo-sample/> EE.PK.2015.10.6

Vai eksistē tāds naturāls skaitlis $n$, ka vairāk nekā pusei 
veselo skaitļu no $1$ līdz $n$ ciparu summa ir pāru skaitlis?

<small>

* [seq.define](#)
* [misc.experiment](#)
* [misc.induction](#)

</small>

<!--
ru=
Существует ли такое положительное целое число $n$, что у более половины
из целых чисел от $1$ до $n$ сумма цифр чётна?
-->

<!--
questionType=ProveDisprove.Exists
-->


## Eksperimentēšana

Definējam funkcijas:

* $N(n)$ - cik daudziem skaitļiem no $1$ līdz $n$ ciparu summa ir nepāru skaitlis
* $P(n)$ - cik daudziem skaitļiem no $1$ līdz $n$ ciparu summa ir pāru skaitlis
* $f(n) = N(n) - P(n)$ - par cik nepāru ciparu summu bija vairāk nekā
pāru ciparu summu skaitļiem intervālā $[1;n]$.

**Apgalvojums:** Visiem $n$ ir spēkā $f(n) \geq 0$. T.i. vienmēr $N(n) \geq P(n)$. 

## Induktīvā pāreja

Aplūkojam $f(n)$ vērtības dažiem pirmajiem $n$: 

<table>
<tr>
<th>$n$</th><td>1</td><td>2</td><td>3</td><td>4</td></tr>
</tr>
<tr>
<th>$f(n)$</th><td>1</td><td>0</td><td>1</td><td>0</td></tr>
</tr>
</table>

Tālāk - tiem $n$, kas dalās ar $10$.

<table>
<tr>
<th>$n$</th><td>10</td><td>20</td><td>30</td><td>40</td></tr>
</tr>
<tr>
<th>$f(n)$</th><td>2</td><td>0</td><td>2</td><td>0</td></tr>
</tr>
</table>


# <lo-sample/> EE.PK.2016.10.3

Vai var atrast tādus $n$ naturālus skaitļus, lai to summa 
būtu vienāda ar to mazāko kopīgo dalāmo, ja 
a) $n = 2$?  
b) $n = 3$?

<small>

* [div.alg](#)
* [div.common.lcm.frac](#)

</small>

<!--
ru=
Можно ли подобрать такие $n$ положительных целых чисел, 
чтобы их сумма равнялась их же наименьшему общему кратному, если
а) $n = 2$?  
б) $n = 3$?
-->

<!--
questionType=ProveDisprove.Exists
-->



## Pārtulkojam apgalvojumu algebriski

**Gadījums n=2:**

* Apzīmējam abu skaitļu $a,b$ mazāko kopīgo dalāmo ar $m$. 
* Tad $m = xa$ un $m = yb$. Ja nu $m=a+b$, tad $m = m/x+m/y$ jeb
$$1 = \frac{1}{x} + \frac{1}{y}.$$

Šim vienādojumam nav atrisinājumu veselos skaitļos $x,y$, 
jo nevar izvēlēties $x=y=2$ (šādā gadījumā $a=b$ un to 
MKD nebūs divreiz lielāks).

## Gadījums n=3

* Līdzīgi kā iepriekš apzīmējam $m=\mbox{MKD}(a,b,c)$. 
* Apzīmējam $m=xa$, $m=yb$, $m=zc$.
* Tad $m=a+b+c$ ir ekvivalents vienādojumam:

$$1 = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}.$$

* Var izvēlēties $x=2$, $y=3$ un $z=6$. Ja $m=30$, tad
$(a,b,c)=(15,10,5)$.  
* Šis piemērs der, jo $\mbox{MKD}(15,10,5)=30$ un $15+10+5=30$.


# <lo-sample/> EE.PK.2016.10.4

Vai eksistē tāds vienādojuma 
$x^2 + y^2 + z^2 + w^2 = 3 + xy + yz + zw$,
atrisinājums, kuram $x$, $y$, $z$ un $w$ ir dažādi veseli skaitļi?

<small>

* [alg.ineq.fullsquare](#)
* [alg.ineq.equations](#)

</small>

<!--
ru=
Существует ли такое решение уравнения
$x^2 + y^2 + z^2 + w^2 = 3 + xy + y z + zw$,
при котором $x$, $y$, $z$ и $w$ различные целые числа?
-->

<!--
questionType=ProveDisprove.Exists
-->



## Algebriski pārveidojumi nevienādībai

$$2x^2 + 2y^2 + 2z^2 + 2w^2 = 6 + 2xy + 2yz + 2zw$$
$$x^2+(x^2 - 2xy + y^2) + \ldots + (z^2 - 2zw + w^2) + w^2 = 6.$$
$$x^2 + (x - y)^2 + (y-z)^2 + (z-w)^2 + w^2 = 6.$$

Četru vai piecu nenulles pilnu kvadrātu summa nevar būt $6$, jo 
neviens no šiem kvadrātiem nevar būt $2^2$ vai lielāks. 





# <lo-sample/> EE.PK.2017.10.2

Atrast visus veselu skaitļu pārus $(x,y)$, kuriem 
$324^{x+y} = 2^{x−y} \cdot 3^{x−3} \cdot 4^{y−4}$.

<small>

* [div.pfactor.algorithm](#)
* [alg.powers.prod](#)
* [div.pfactor.expsystem](#)
* [alg.linear](#)

</small>

<!--
ru=
Найти все пары целых чисел $(x,y)$, при которых
$324^{x+y} = 2^{x−y} \cdot 3^{x−3} \cdot 4^{y−4}$.
-->

<!--
questionType=Find.All
-->




## Dalām pirmreizinātājos

Abās vienādojuma pusēs ir daži salikti skaitļi - 
$324$ un $4$. 

1. Sadalām skaitli $324$ pirmreizinātājos:  
$324=18 \cdot 18=(2 \cdot 3^2)^2 = 2^2 \cdot 3^4.$
2. Sadalām arī $4$ pirmereizinātājos:  
$4 = 2^2$. 


## Pielīdzinām pirmskaitļu kāpinātājus

Pārrakstām uzdevuma vienādojumu: 
$$(2^2 \cdot 3^4)^{x+y} = 2^{x−y} \cdot 3^{x−3} \cdot (2^2)^{y−4}$$
$$2^{2(x+y)} \cdot 3^{4(x+y)} = 2^{x−y} \cdot 3^{x−3} \cdot 2^{2(y−4)}$$

Pielīdzinām pirmskaitļu pakāpes:

$$\left\{ \begin{array}{l}
2(x+y) = (x-y) + 2(y-4) \\
4(x+y) = x-3
\end{array}
\right.$$

## Risinām lineāru sistēmu

$$\left\{ \begin{array}{l}
x+y = -8 \\
3x+4y = -3
\end{array}
\right.$$

No pirmā vienādojuma izsaka $y=-8-x$ un ievieto otrajā:

$3x + 4(-8-x) = -32-x = -3$. Tad $(x,y)=(-29,21)$.


# <lo-sample/> EE.PK.2017.10.3

Pierādīt, ka atradīsies bezgalīgi daudz četrinieku, ko veido 
dažādi naturāli skaitļi, kuriem
$$\frac{1}{a} - \frac{1}{b} =\frac{1}{b} - \frac{1}{c} =\frac{1}{c} - \frac{1}{d}.$$

<small>

* [misc.symmetry](#)
* [misc.experiment](#)
* [seq.arithm.expr](#)
* [alg.sums.linear](#)

</small>

<!--
ru=
Доказать, что найдётся бесконечно много четвёрок различных 
целых положительных чисел $(a, b, c, d)$, при которых
$$\frac{1}{a} - \frac{1}{b} =\frac{1}{b} - \frac{1}{c} =\frac{1}{c} - \frac{1}{d}.$$
-->

<!--
questionType=Find.InfinitelyMany
-->


## Papildu pieņēmumi (simetrija)

Tā kā visi skaitļi ir dažādi, tad varam ieviest apzīmējumus tā, 
ka $\frac{1}{a} > \frac{1}{b} > \frac{1}{c} > \frac{1}{d}$ un 
visas starpības ir pozitīvas. 

Ja starpības patiesībā ir negatīvas, tad aizstājam $(a,b,c,d)$ ar
pretējā secībā pārrakstītu skaitļu četrinieku $(d,c,b,a)$. 

Varam tātad pieņemt, ka $a < b < c < d$ un tad tiem 
apgrieztie skaitļi veido dilstošu aritmētisku progresiju. 

## Sākam ievietot vērtības skaitlim a

* Ja $a=2$, tad nesanāk, jo pat tuvākā starpība: $\frac{1}{2}-\frac{1}{3}$
jeb aritmētiskās progresijas diference ir $1/6$ un no $\frac{1}{2}$ to 
nevar atņemt trīsreiz, lai rezultāts joprojām būtu pozitīvs.
* Ja $a=3$, tad sanāk progresija: 
$$\frac{1}{3},\frac{1}{4},\frac{1}{6},\frac{1}{12}$$

## Izmantojam linearitāti

Eksistējošu atrisinājumu var piereizināt
ar vienu un to pašu skaitli $m$: 

No 
$$\frac{1}{a} - \frac{1}{b} =\frac{1}{b} - \frac{1}{c} =\frac{1}{c} - \frac{1}{d}.$$
izriet, ka arī
$$\frac{1}{ma} - \frac{1}{mb} =\frac{1}{mb} - \frac{1}{mc} =\frac{1}{mc} - \frac{1}{md}.$$

## Atbildes

Tātad bez $(a,b,c,d)=(3,4,6,12)$ var ņemt arī 
$(a,b,c,d)=(6,8,12,24)$, utt.

Eksistē arī citādas atbildes, kuras uz $(3,4,6,12)$ vai tā 
daudzkārtņiem reducēt nevar. 


# <lo-sample/> EE.PK.2018.10.3

Mari iedomājās naturālu skaitli. Pareizinot šo skaitli ar $4$, 
viņa ieguva kādu trīsciparu skaitli. Bet, pareizinot sākotnējo 
skaitli ar $3$ un pārceļot rezultāta pēdējo ciparu uz sākumu, 
negaidīti ieguva tādu pašu trīsciparu skaitli. 
Atrast visas iespējamās vērtības Mari iedomātajam skaitlim. 

<small>

* [alg.equation](#)
* [notation.dec.combine.poly](#)
* [misc.exhaustive](#)

</small>

<!--
Маша задумала одно натуральное число. Умножив это число на 4, 
она получила какое-то трёхзначное число. А когда она умножила первоначальное 
число на 3 и переставила последнюю цифру результата в его начало,
то неожиданно получила то же самое трёхзначное число. 
Найти все возможные значения задуманного Машей числа.
-->

<!--
questionType=Find.All
-->


## Vienādojuma sastādīšana

* $x$ ... tāds bija Mari iedomātais skaitlis. 
* Tad $3x=\overline{abc}$ un $4x=\overline{cab}$. 
* No desmitkāršota $4x=\overline{cab}$ atņemsim 
 $3x=\overline{abc}$ (lai $a$ un $b$ noīsinātos). 

$$40x - 3x = \overline{cab0}-\overline{abc}=\overline{c000} - c = 999\cdot{}c.$$

Iegūstam, ka $37x = 999c$ jeb $x = 27c$, kur $c$ ir cipars. 

## Gadījumu pārlase

* Cipars $c \neq 0$, jo citādi 
$\overline{cab}$ nebūtu trīsciparu. 
* Cipars $c \neq 1$, jo $3 \cdot 27 = 81$ nav trīsciparu.
* Astoņas citas vērtības $c=2,3,4,5,6,7,8,9$ der. 

Apkopojam tabulā $x=27c$, $3x$ un $4x$:

<table>
<tr>
<th>$x$</th><td>54</td><td>81</td><td>108</td><td>135</td><td>162</td><td>189</td><td>216</td><td>243</td>
</tr>
<tr>
<th>$3x$</th><td>162</td><td>243</td><td>324</td><td>405</td><td>486</td><td>567</td><td>648</td><td>729</td>
</tr>
<tr>
<th>$4x$</th><td>216</td><td>324</td><td>432</td><td>540</td><td>648</td><td>756</td><td>864</td><td>972</td>
</tr>
</table>

Pēdējā rindiņā skaitļi iegūstami, pārceļot priekšpēdējās rindiņas skaitlim 
pēdējo ciparu uz sākumu.


# <lo-sample/> EE.PK.2019.10.3

Cik ir tādu veselu negatīvu skaitļu pāru $(a,b)$, 
kas apmierina vienādību $22a + 15b = 2019$?

<small>

* [misc.extreme.param](#)
* [mod.expr.sum](#)
* [misc.experiment](#)
* [seq.arithm.mod.gaps](#)

</small>

<!--
ru=
Сколько найдётся пар неотрицательных целых чисел $(a, b)$, 
удовлетворяющих равенству $22a + 15b = 2019$?
-->

<!--
questionType=Find.Count
-->


## Lielākā iespējamā a vērtība

Iedomāsimies, ka vispirms vēlamies atrast lielāko 
iespējamo $a$ un mazāko $b$. T.i. cik reizes saskaitāmo 
$22$ var iekļaut garajā summā, kas ir $2019$. 

$$2019:22\;=\;91,\,\mbox{Atl.}17$$

* Acīmredzot, $17$ nedalās ar $15$, t.i. pie $a=91$ vienādojumu 
atrisināt nevar. 
* Pakāpeniski samazinām $a$ par $k=1,2,\ldots$.
* Gaidām brīdi, kad $17+22k$ jeb $17+7k$ dalās ar $15$. 
* Pie $k=4$ izteiksme $17 + 7\cdot{}4=17+28=45$ dalās ar $15$.
* Tātad, $a=91$ jāsamazina par $4$, t.i. der $a=87$. 

## 2 pretējas aritmētiskas progresijas

Pirmais atrisinājums ir $(a,b)=(87,7)$, jo 
$$87\cdot{}22+7\cdot{}15=2019$$. 

* Aritmētiskajā progresijā $c_k=2019-15k$ katrs $22$-tais loceklis
dalās ar $22$, jo diference $-15$ ir savstarpējs pirmskaitlis ar $22$. 
* Tātad, der $b=7,29,51,\ldots$ savukārt $a$ vērtībai (ja $b$ pieaug
par $22$) ir jāsamazinās par $15$, lai summa nemainītos. 
* Iegūstam atrisinājumus $(a;b)$:
$$(87;7),\;(72;29),\;(57;51),\;(42;73),\;(27;95),\;(12;117).$$



