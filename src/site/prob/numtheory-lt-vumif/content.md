# &nbsp;

<h1 style="font-size:28pt">Skaitļu teorija (LT, 10.kl.)</h1>

* **LT.LKMMO** - Lietuvos komandinė mokinių matematikos 
olimpiada (Lietuvas komandveida skolēnu matemātikas olimpiāde)
* **LT.LDK** - Varžybos Lietuvos Didžiosios Kunigaikštystės garbei
(Sacensības Lietuvas Lielkņazistes godam)  
* **LT.RAJ** - Rajono/miesto etapas (Rajona/pilsētas posms)  
* **LT.LMMO** - Lietuvos mokinių matematikos olimpiada (Lietuvas skolēnu
matemātikas olimpiāde: nacionālais posms)  
* <blue>**LT.VUMIF** - **Vilniaus universiteto Matematikos ir 
informatikos fakulteto olimpiada** (Viļņas universitātes 
rīkota olimpiāde skolēniem)</blue>

[Matematikos olimpiados](http://mif.vu.lt/matematikos-olimpiados/)



# <lo-sample/> LT.VUMIF.2016.9.3

Atrodiet visas naturālas $n$ vērtības, kurām skaitlis
$\frac{n^3 + 3}{n^2 + 7}$
ir naturāls.

<!--
Raskite visas natūraliąsias $n$ reikšmes, su kuriomis skaičius
$\frac{n^3 + 3}{n^2 + 7}$
yra natūralusis.
-->

<small>

* [alg.poly.division](#)
* [alg.ineq.equations](#)
* [misc.exhaustive](#)

</small>

## Dalām divus polinomus

Ja skaitītājā polinoma pakāpe (kubs) ir vismaz tāda
pati kā saucējā (kvadrāts), tad tos var dalīt, iegūstot
atlikumu:

$$\frac{n^3 + 3}{n^2 + 7} = \frac{n(n^2 + 7) - 7n + 3}{n^2 + 7} = 
n + \frac{-7n+3}{n^2 + 7}.$$

* Skaitītājs un saucējs ir pozitīvi naturāliem $n$, t.i. dalījums
būs naturāls t.t.t. ja daļa $\frac{-7n+3}{n^2+7}$ ir vesela. 
* Ja $n \geq 7$, tad daļa nav vesela, jo
$$|n^2 + 7| \geq |7n + 7| > |-7n+3|$$

## Pilnā pārlase

$\frac{-7n+3}{n^2+7}$ ievietojam 
visas vērtības $n=1,2,3,4,5,6$. (Lielākas ievietojot, 
nav cerību iegūt naturālu skaitli, 
jo tām saucēja modulis pārsniedz skaitītāja
moduli.)

* Ja $n=2$, tad $\frac{-7n+3}{n^2 + 7} = \frac{-11}{11} = -1$. 
* Ja $n=5$, tad $\frac{-7n+3}{n^2 + 7} = \frac{-32}{32} = -1$. 
* Vērtībām $n=1,3,4,6$ sanāk daļskaitļi.



# <lo-sample/> LT.VUMIF.2016.10.3

Atrodiet mazāko naturālo skaitli $n$, kuram skaitļi 
$\sqrt[5]{5n}$, $\sqrt[6]{6n}$, $\sqrt[7]{7n}$
ir naturāli. 

<!--
Raskite mažiausią natūralųjį skaičių $n$, kuriam skaičiai
$\sqrt[5]{5n}$, $\sqrt[6]{6n}$, $\sqrt[7]{7n}$
yra natūralieji.
-->

<small>

* [div.pfactor.powers.higher](#)
* 


</small>

# <lo-sample/> LT.VUMIF.2016.11_12.1

Agne savā traukā ielēja $p$ litrus ūdens, 
bet Bens savā traukā ielēja $q$ litrus ūdens. 
Pārmaiņus veikdami gājienus, viņi spēlē sekojošu spēli. 
Gājiena laikā spēlētājs no sava trauka otra spēlētāja
traukā ielej tik daudz ūdens, 
cik ūdens jau ir otrā spēlētāja traukā.
Spēli sāk Agne. Pēc simts gājieniem Agnes traukā
bija $q$ litri ūdens, bet Bena traukā - $p$ litri ūdens. 
Atrodiet $\frac{p}{q}$.

<!--
Agnė į savo turimą indą įpylė $p$ litrų vandens, 
o Benas į savąjį indą įpylė $q$ litrų vandens.
Pakaitomis atlikdami ėjimus, jie žaidžia tokį žaidimą. 
Ėjimo metu žaidėjas iš savo indo į
kito žaidėjo indą turi įpilti tiek vandens, 
kiek jo tuo metu yra kito žaidėjo inde. Žaidimą
pradėjo Agnė. Po šimto ėjimų Agnės inde buvo $q$ 
litrų vandens, o Beno – $p$ litrų vandens.
Raskite $\frac{p}{q}$.
-->


# <lo-sample/> LT.VUMIF.2016.11_12.3

Noskaidrojiet, vai eksistē tāds naturāls skaitlis $n$, ka 
skaitlis $n \cdot 2^{2016} - 7$ ir
naturāla skaitļa kvadrāts.

<!--
Nustatykite, ar egzistuoja toks natūralusis skaičius $n$, 
kad skaičius $n \cdot 2^{2016} - 7$ yra
natūraliojo skaičiaus kvadratas.
-->

# <lo-sample/> LT.VUMIF.2017.9.2

Vai izmantojot tieši pa vienai reizei visus desmit ciparus 
$0,1,2,\ldots,9$ var uzrakstīt divus naturālus skaitļus, ka 
viens skaitlis būtu otra kvadrāts?  
*Piezīme.* Pirmais skaitļa cipars nevar būt nulle.

<!--
Ar panaudojus po lygiai vieną kartą visus dešimt skaitmenų
$0,1,2,\ldots,9$ galima užrašyti du natūraliuosius skaičius, 
kad vienas skaičius būtų kito kvadratas?  
*Pastaba.* Pirmasis skaičiaus skaitmuo negali būti nulis. 
-->

# <lo-sample/> LT.VUMIF.2017.10.1

Atrodiet visus veselu skaitļu pārus $(a,b)$, 
kuriem eksistē tādi veseli skaitļi $x$ un
$y$, ka
$$8x^4 + 8y^4 = a^4 + 6a^2b^2 + b^4.$$


<!--
Raskite visas sveikųjų skaičių poras $(a,b)$, 
kurioms egzistuoja tokie sveikieji skaičiai $x$ ir
$y$, kad
$$8x^4 + 8y^4 = a^4 + 6a^2b^2 + b^4.$$
-->

# <lo-sample/> LT.VUMIF.2017.10.2

Atrodiet visus veselo skaitļu $m$ un $n$ pārus
$(m,n)$, kas apmierina vienādību 
$$m^2 + 2m - 9 = n^2 + n.$$

<!--
Raskite visas sveikųjų skaičių $m$ ir $n$ poras 
$(m, n)$, tenkinančias lygybę
$$m^2 + 2m - 9 = n^2 + n.$$
-->

# <lo-sample/> LT.VUMIF.2017.11_12.2

Atrodiet vienādojuma
$$x^2y^2 + 208 + 4(\mbox{LKD}(x,y) + \mbox{MKD}(x,y))^2$$
visus naturālos atrisinājumus $(x,y)$. 
Šeit $\mbox{LKD}(x,y)$ un $\mbox{MKD}(x,y)$ attiecīgi apzīmē skaitļu 
$x$ un $y$ lielāko kopīgo dalītāju un mazāko kopīgo dalāmo. 

<!--
Raskite lygties
$$x^2y^2 + 208 + 4(\mbox{DBD}(x,y) + \mbox{MBK}(x,y))^2$$
visus natūraliuosius sprendinius $(x,y)$. 
Čia $\mbox{DBD}(x,y)$ ir $\mbox{MBK}(x,y)$ atitinkamai žymi
skaičių $x$ ir $y$ didžiausią bendrą daliklį ir 
mažiausią bendrą kartotinį.
-->

# <lo-sample/> LT.VUMIF.2017.11_12.4

Uz tāfeles uzrakstīts skaitlis $636363$. 
Divi spēlētāji $A$ un $B$ pārmaiņus veic gājienus, 
pirmo gājienu izdara $A$. 
Gājiena laikā ir jānodzēš uz tāfeles esošais skaitlis un 
jāuzraksta tā starpība ar jebkuru viņa naturālu dalītāju. 
Spēlētājs, kurš uzraksta $0$, zaudē. Noskaidrojiet, kuram 
spēlētājam ir uzvaras stratēģija, un parādiet to.

<!--
Lentoje užrašytas skaičius $636363$. 
Du žaidėjai $A$ ir $B$ pakaitomis atlieka ėjimus, pirmąjį
ėjimą atlieka $A$. Ėjimo metu reikia nutrinti 
lentoje esantį skaičių ir užrašyti jo ir bet kurio
jo natūraliojo daliklio skirtumą. Žaidėjas, užrašęs 
skaičių $0$, pralaimi. Nustatykite, kuris
žaidėjas turi pergalės strategiją, ir nurodykite ją.
-->

# <lo-sample/> LT.VUMIF.2018.9.4

Naturālam skaitlim $M = 3N$ 
ir tikpat ciparu, cik naturālam skaitlim $N > 10$. 
Lai iegūtu skaitli $M$, vajag palielināt
ikvienu skaitļa $N$ ciparu: vienam no cipariem 
pieskaitīt $2$, bet pie atlikušajiem cipariem 
pieskaitīt pa nepāru naturālam skaitlim (ne obligāti 
visiem to pašu). 
Atrodiet visas iespējamās skaitļa $N$ pēdējā 
cipara vērtības.

<!--
Natūralusis skaičius $M = 3N$ 
turi tiek pat skaitmenų, kaip ir
natūralusis skaičius $N > 10$. 
Norint gauti skaičių $M$, reikia padidinti 
kiekvieną iš skaičiaus $N$ skaitmenų: prie vieno skaitmens
pridėti $2$, o prie likusių skaitmenų 
pridėti po nelyginį natūralųjį
skaičių (nebūtinai po tą patį). 
Raskite visas galimas skaičiaus $N$
paskutinio skaitmens reikšmes.
-->

# <lo-sample/> LT.VUMIF.2018.10.4

Skaitļa $n>1$ visu pozitīvo dalītāju 
(ieskaitot $1$ un $n$) reizinājums vienāds ar $n^3$.
Norādiet visas iespējamās skaitļa $n$ vērtības, 
uzrakstot, kāds var būt skaitļa $n$ sadalījums pirmreizinātājos. 

<!--
Skaičiaus $n>1$ visų teigiamų daliklių 
(įskaitant $1$ ir $n$) sandauga lygi $n^3$.
Nurodykite visas galimas skaičiaus $n$ reikšmes, 
užrašydami, koks gali būti skaičiaus $n$ 
skaidinys pirminiais daugikliais.
-->


# <lo-sample/> LT.VUMIF.2018.11_12.4

Naturālie skaitļi $p$, $x$, $y$ apmierina vienādojumus:
$$p + 1 = 2x^2,\;\;p^2 + 1 = 2y^2.$$
Noskaidrojiet visas iespējamās skaitļa $p$ vērtības, ja 
zināms, ka šis skaitlis ir pirmskaitlis. 

<!--
Natūralieji skaičiai $p$, $x$, $y$ tenkina lygtis:
$p + 1 = 2x^2,\;\;p^2 + 1 = 2y^2.$$
Nustatykite visas galimas skaičiaus $p$ reikšmes, 
jei žinoma, kad šis skaičius pirminis.
-->

# <lo-sample/> LT.VUMIF.2019.9.1

Atrodiet visus veselu skaitļu trijniekus $(x,y,z)$, 
kas apmierina vienādojumu sistēmu
$$
\left\{ \begin{array}{l}
x^3 + y^3 = z^3 + 1,\\
y^2 - x^2 = x+y,\\
2x^3 - 6x = z^3 - 4x^2.
\end{array} \right.$$

<!--
Raskite visus sveikųjų skaičių trejetus $(x,y,z)$, 
tenkinančius lygčių sistemą
$$
\left\{ \begin{array}{l}
x^3 + y^3 = z^3 + 1,\\
y^2 - x^2 = x+y,\\
2x^3 - 6x = z^3 - 4x^2.
\end{array} \right.$$
-->

# <lo-sample/> LT.VUMIF.2019.9.2

Algis un Balis spēlē sekojošu spēli, 
pārmaiņus izdarīdami gājienus. Sākumā 
ir divas monētu kaudzītes: vienā kaudzītē
ir $m$ monētas, bet otrā $n$ monētas.
Gājiena laikā jāveic jebkura viena no trim 
sekojošām darbībām:
1) izmest vienu monētu no jebkuras kaudzītes;
2) izmest pa vienai monētai no abām kaudzītēm; 
3) pārcelt vienu monētu no jebkuras kaudzītes uz otru kaudzīti. 
Sāk Algis. Spēlētājs, kurš nevar veikt gājienu, zaudē. 
Noskaidrojiet visus naturālu skaitļu pārus $(m,n)$, 
kuriem Balim ir uzvaras stratēģija, t.i. kurām viņš var
nodrošināt uzvaru, lai kā spēlētu Algis. 

<!--
Algis ir Balys žaidžia tokį žaidimą, 
pakaitomis atlikdami ėjimus. Pradžioje
yra dvi monetų krūvelės: vienoje krūvelėje 
yra $m$ monetų, o kitoje yra $n$
monetų. Ėjimo metu reikia atlikti bet 
kurį vieną iš šių trijų veiksmų: 
1) išmesti vieną monetą iš bet kurios krūvelės; 
2) išmesti po vieną monetą iš abiejų krūvelių; 
3) perkelti vieną monetą iš bet kurios krūvelės į kitą. 
Pradeda Algis. Žaidėjas, negalintis atlikti ėjimo, 
pralaimi. Nustatykite visas natūraliųjų skaičių $(m,n)$ 
poras, kurioms Balys turi pergalės strategiją, t. y.
kurioms jis gali užsitikrinti pergalę, 
kad ir kaip žaistų Algis.
-->

# <lo-sample/> LT.VUMIF.2019.9.4

Jurgis uzrakstīja trīs naturālus skaitļus, 
no kuriem katrs beidzas ar to pašu ciparu, ar kuru 
beidzas pārējo divu skaitļu summa, un sareizināja tos. 
Jurgis uzrakstīja tikai reizinājuma pēdējos trīs 
ciparus. Kādu ciparu trijnieku viņš varēja iegūt? 
Atrodiet visas iespējas. 

<!--
Jurgis užrašė tris natūraliuosius skaičius, 
iš kurių kiekvienas baigiasi tuo
pačiu skaitmeniu kaip kitų dviejų skaičių 
suma, ir sudaugino juos. Jurgis
užrašė tik sandaugos paskutinius tris 
skaitmenis. Kokį skaitmenų trejetą jis
galėjo gauti? Raskite visas galimybes.
-->


# <lo-sample/> LT.VUMIF.2019.10.4

Naturālu skaitli sauksim par *septiņīgu*, 
ja tam ir tieši $70$ ciparu: $10$ vieninieku, 
$10$ divnieku, $\ldots$, $10$ septiņnkieku. 
Pierādīt, ka, ja viens septiņīgs skaitlis dalās
ar citu septiņīgu skaitli, tad tie ir vienādi. 

<!--
Natūralųjį skaičių vadinsime *septintiniu*, 
jei jis turi lygiai $70$ skaitmenų: $10$
vienetų, $10$ dvejetų, $\ldots$, $10$ septynetų. 
Įrodykite, kad jei vienas septintinis
skaičius dalijasi iš kito, tai jie lygūs.
-->

# <lo-sample/> LT.VUMIF.2019.11_12.4

Naturālu skaitli sauksim par *piecīgu*, ja
tam ir tieši $500$ ciparu: pa $100$ divnieku, 
trijnieku, četrinieku, piecinieku un sešinieku. 
Pie piecīga skaitļa $M$ labajā pusē pierakstot 
divus ciparus $81$, iegūts skaitlis 
$N = \overline{M81}$. Pierādiet, ka  
a) $M$ nedalās ne ar vienu piecīgu skaitli, izņemot sevi pašu;  
b) $N$ nedalās ne ar vienu piecīgu skaitli. 

<!--
Natūralųjį skaičių vadinsime *penktiniu*, 
jei jis turi lygiai $500$ skaitmenų: po
$100$ dvejetų, trejetų, ketvertų, penketų ir šešetų. 
Prie penktinio skaičiaus $M$
iš dešinės prirašius du skaitmenis $81$, 
gautas skaičius $N = \overline{M81}$. Įrodykite,
kad a) $M$ nesidalija iš jokio penktinio skaičiaus, 
išskyrus save patį; 
b) $N$ nesidalija iš jokio penktinio skaičiaus.
-->


