# READ ME

$x_1$

## Atrisinājums

$x_2, \ldots$

$\sin x, \mbox{tg}\, x$

<<<<<<< HEAD
$z^2 \equiv 1 \pmod {10}$
=======
$x^2 \equiv 1 \pmod {10}$

 

# <lo-sample/> LV.AMO.2018.12.4.

Naturāls skaitlis $B$ ir iegūts no naturāla skaitļa $A$, samainot vietām tā 
ciparus. Zināms, ka $A+B=10^{45}$. Pierādīt, ka gan $A$, gan $B$ dalās ar $5$.

<small>

* questionType:
* domain:

</small>

## Atrisinājums

Apzīmējam $A=\overline{a_{45}a_{44} \ldots a_{2}a_{1}}$ un 
$B=\overline{b_{45}b_{44} \ldots b_{2}b_{1}}$.

Desmitnieka pakāpes visi cipari, izņemot pirmo, ir $0$. Apskatām abus 
iespējamos gadījumus: $a_{1}+b_{1}=0$ vai $a_{1}+b_{1}=10$

Ja $a_{1}+b_{1}=0$, tad $a_{1}=b_{1}=0$. Līdz ar to $A$ un $B$ dalās ar $5$.

Ja $a_{1}+b_{1}=10$, tad derīgie ciparu komplekti (neņemot vērā $a_{1}$ un 
$b_{1}$ secību) ir $(1; 9),\ (2; 8),\ (3; 7),\ (4 ; 6),\ (5 ; 5)$ un veidojas 
pārnesums. Tas nozīmē, ka 
$\overline{a_{45}a_{44} \ldots a_{2}}+\overline{b_{45}b_{44} \ldots b_{2}}=\underbrace{9999 \ldots 9}_{45}$

Līdz ar to katram $i(2 \leq i \leq 45) i$-tajā pozīcijā $a_{i}+b_{i}=9$, jo 
divu viencipara skaitļu summa nevar būt $19$. Katrā pozīcijā zinot vienu no 
skaitļiem, viennozīmīgi ir noteikts arī otrs. Tātad pa visām šīm pozīcijām kopā
sakrīt ciparu $0$ un $9$ skaits, $1$ un $8$ skaits, $2$ un $7$ skaits, $3$ un 
$6$ skaits, $4$ un $5$ skaits. Līdz ar to pa visām šīm pozīcijām kopā ir $45$ 
pāra un $45$ nepāra cipari, bet pēdējā pozīcijā abi cipari ir vai nu pāra, vai 
nepāra.

- Ja pēdējā pozīcijā abi ir nepāra cipari, tad visi pāra cipari, kas ietilpst 
  $A$ un $B$ pierakstā, atrodas pozīcijās no pirmās līdz priekšpēdējai. Tā kā 
  $A$ un $B$ ir veidoti no viena ciparu komplekta, tad pāra ciparu komplekts 
  skaitlī $A$ sakrīt ar pāra ciparu komplektu skaitlī $B$. Tā kā katrs pāra 
  cipars vienā skaitlī viennozīmīgi nosaka nepāra ciparu otrā skaitlī, tad abu 
  skaitļu pierakstā, bez pēdējā cipara, izmantoti arī vieni un tie paši nepāra 
  cipari. Lai viss ciparu komplekts abiem skaitļiem būtu vienāds, nepieciešams,
  lai $a_{1}=b_{1}$. Bet tas ir iespējams tikai tad, ja $a_{1}=b_{1}=5$. Tas 
  nozīmē, ka $A$ un $B$ dalās ar $5$.
- Ja pēdējā pozīcijā abi ir pāra cipari, tad izmantojot līdzīgus spriedumus, 
  iegūstam, ka $a_{1}=b_{1}$, bet tas nav iespējams, jo skaitli $10$ nav 
  iespējams iegūt kā divu vienādu pāra ciparu summu.

Tātad esam pierādījuši, ka gan $A$, gan $B$ dalās ar $5$.



# <lo-sample/> LV.AMO.2018.12.5.

Katras divas regulāra sešstūra virsotnes savieno vai nu ar sarkanu, vai zilu 
nogriezni. Aplūkosim visus trijstūrus, kuru virsotnes ir dotā sešstūra 
virsotnes. **a)** Pierādīt, ka starp tiem ir vismaz viens vienkrāsas 
trijstūris! **b)** Vai var gadīties, ka starp tiem ir tieši viens vienkrāsas 
trijstūris?

Trijstūri sauc par vienkrāsas, ja tam visas malas ir nokrāsotas vienā krāsā.

<small>

* questionType:
* domain:

</small>

## Atrisinājums

Regulārā sešstūra virsotnes apzīmējam ar $A, B, C, D, E, F$.

**a)** Pierādīsim, ka vienmēr būs vismaz viens vienkrāsas trijstūris. 
Pieņemsim, ka nav neviena vienkrāsas trijstūra. Aplūkojam patvaļīgu sešstūra 
virsotni $A$. Tā kā no tās iziet $5$ nogriežņi, tad vismaz trīs no tiem ir 
vienā krāsā (Dirihlē princips). Nezaudējot vispārīgumu, uzskatīsim, ka 
nogriežņi $\textcolor{red}{AB}, \textcolor{red}{AC}, \textcolor{red}{AD}$ ir 
sarkanā krasā. Tad $\textcolor{blue}{BC}$ un $\textcolor{blue}{CD}$ jābūt zilā 
krāsā un viens no trijstūriem $ABD$ vai $BCD$ ir vienkrāsas trijstūris (skat. 
36.att.). legūta pretruna ar pieņēmumu.

![](LV.AMO.2018.12.5A.png)

**b)** Nē, nevar. Pierādīsim, ka vienmēr būs vismaz divi vienkrāsas trijstūri. 
Pieņemsim, ka ir tikai viens vienkrāsas trijstūris. Nezaudējot vispārīgumu, 
varam uzskatīt, ka tas ir sarkans trijstūris $\textcolor{red}{ACE}$ (skat. 
37.att.). Vismaz viena no trijstūra $FBD$ malām $FB,\ BD$ vai $DF$ ir zilā 
krāsā, pretējā gadījumā uzreiz būtu divi vienkrāsas trijstūri. Nezaudējot 
vispārīgumu, varam uzskatīt, ka $FB$ ir zila. Viens no nogriežņiem $AF$ vai 
$AB$ ir sarkans, jo pretējā gadījumā būtu divi vienkrāsas trijstūri. Simetrijas
dēļ varam uzskatīt, ka $\textcolor{red}{AF}$ ir sarkans. Tad 
$\textcolor{blue}{FE}$ un $\textcolor{blue}{FC}$ ir zilā krāsā, bet 
$\textcolor{red}{BC}$ ir sarkanā krāsā. Tagad vai nu $FEB$, vai $BEC$ ir 
vienkrāsas trijstūris. legūta pretruna ar pieņēmumu.

![](LV.AMO.2018.12.5B.png)
