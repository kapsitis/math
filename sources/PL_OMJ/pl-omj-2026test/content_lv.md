# <lo-sample/> PL.OMJ.2026TEST.7_8.1

Trīs kastēs sadalīja 7 bumbiņas, neatstājot nevienu kasti tukšu. No tā izriet, ka

**(a)** kādā kastē ir tieši viena bumbiņa;

**(b)** kādā kastē ir pāra skaits bumbiņu;

**(c)** kādās divās kastēs ir vienāds skaits bumbiņu.

<small>

* answer:N,N,N
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Ja bumbiņu skaiti kastēs ir 2, 2, 3, tad nevienā kastē nav tieši vienas bumbiņas.

b) Ja bumbiņu skaiti kastēs ir 1, 3, 3, tad katrā kastē ir nepāra skaits bumbiņu.

c) Ja bumbiņu skaiti kastēs ir 1, 2, 4, tad katrā kastē ir atšķirīgs skaits bumbiņu.

**Piezīme.**

Ir tikai četri iespējamie bumbiņu skaitu sadalījumi kastēs, kas apmierina uzdevuma nosacījumus. Bez iepriekš minētajiem ir vēl sadalījums 1, 1, 5.


# <lo-sample/> PL.OMJ.2026TEST.7_8.2

Eksistē tādi divdesmit divi veseli skaitļi, ka visu šo skaitļu reizinājums ir $-1$, bet to summa ir

**(a)** $-20$;

**(b)** $-21$;

**(c)** $-22$.

<small>

* answer:T,N,N
* questionType:ShortAnswer

</small>

## Atrisinājums

Veselu skaitļu reizinājums ir $-1$ tad un tikai tad, ja katrs no šiem skaitļiem ir 1 vai $-1$ un turklāt reizinātāju, kas vienādi ar $-1$, skaits ir nepāra.

a) Ja viens no dotajiem skaitļiem ir 1, bet pārējie ir $-1$, tad šo skaitļu reizinājums ir $-1$, bet to summa ir $1+21\cdot(-1)=-20$.

b) 22 nepāra skaitļu summa vienmēr ir pāra skaitlis, tātad atšķirīga no $-21$.

c) Ja 22 skaitļu, kas vienādi ar 1 vai $-1$, summa ir $-22$, tad visi šie skaitļi ir $-1$. Taču tad to reizinājums ir 1. Tas nozīmē, ka 22 veselu skaitļu ar reizinājumu $-1$ summa nevar būt $-22$.

**Piezīme.**

Var pamatot, ka, ja kādi 22 skaitļi apmierina uzdevuma nosacījumus, tad to summa ir skaitlis, kas dalās ar 4, un tā ir cita metode, kā izslēgt summu $-21$ vai $-22$. Ja apzīmēsim ar $k$ reizinātāju, kas vienādi ar $-1$, skaitu, tad $k$ ir nepāra skaitlis, bet $22-k$ ir reizinātāju, kas vienādi ar 1, skaits. Tātad visu 22 skaitļu summa ir

$$
k\cdot(-1)+(22-k)\cdot1=22-2k=2\cdot(11-k).
$$

Tā kā $k$ ir nepāra skaitlis, tad skaitlis $11-k$ ir pāra, un līdz ar to skaitlis $2\cdot(11-k)$ dalās ar 4.


# <lo-sample/> PL.OMJ.2026TEST.7_8.3

Eksistē vesels skaitlis $n$ ar īpašību, ka skaitļa $n$ ciparu summa un skaitļa $n+1$ ciparu summa abas dalās ar

**(a)** 2;

**(b)** 3;

**(c)** 5.

<small>

* answer:T,N,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Ja $n=19$, tad $n+1=20$, un šo skaitļu ciparu summas ir 10 un 2 — abas dalās ar 2.

b) Starp skaitļiem $n$, $n+1$ vismaz viens nedalās ar 3, tāpēc saskaņā ar dalāmības ar 3 pazīmi tā ciparu summa nedalās ar 3.

c) Ja $n=49999$, tad $n+1=50000$, un šo skaitļu ciparu summas ir 40 un 5 — abas dalās ar 5.

**Piezīme.**

Ievērosim, ka, ja skaitļa $n$ decimālais pieraksts beidzas ar tieši $k$ deviņniekiem, tad $s(n+1)=s(n)+1-9k$, kur $s(m)$ apzīmē skaitļa $m$ ciparu summu.

Ja gan $s(n)$, gan $s(n+1)$ dalās ar 5, tad arī to starpība $9k-1$ dalās ar 5. Mazākais iespējamais $k$ ir 4, tāpēc skaitlim $n$ jābeidzas ar vismaz četriem deviņniekiem. Viegli tieši pārbaudīt, ka 49999 ir mazākais iespējamais piemērs c) punktā.


# <lo-sample/> PL.OMJ.2026TEST.7_8.4

Katru $4\times4$ laukuma rūtiņu nokrāsoja baltā vai melnā krāsā tā, ka nekādām divām melnām rūtiņām nav kopīgas malas un katrai baltai rūtiņai ir kopīga mala ar vismaz vienu melnu rūtiņu. No tā izriet, ka šajā laukumā

**(a)** ir vismaz 8 baltas rūtiņas;

**(b)** ir vismaz 6 melnas rūtiņas;

**(c)** vismaz viena stūra rūtiņa ir balta.

<small>

* answer:T,N,N
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Sadalīsim laukumu 8 taisnstūros $1\times2$. Neviens no šiem taisnstūriem nevar sastāvēt no divām melnām rūtiņām, tāpēc katrā no tiem ir vismaz viena balta rūtiņa. Tātad kopā laukumā ir vismaz 8 baltas rūtiņas.

b) Ja melnā krāsā nokrāsosim 1. zīmējumā parādītās 4 rūtiņas, tad uzdevuma nosacījumi būs izpildīti.

c) Ja melnā krāsā nokrāsosim 2. zīmējumā parādītās 6 rūtiņas, tad uzdevuma nosacījumi būs izpildīti.

![](PL.OMJ.2026TEST.7_8.4.png)

1. zīm.

![](PL.OMJ.2026TEST.7_8.4A.png)

2. zīm.

**Piezīme.**

Var pierādīt, ka mazākais iespējamais melno rūtiņu skaits ir 4 (1. zīmējums parāda, ka to var sasniegt). Ja būtu ne vairāk kā 3 melnas rūtiņas, tad tām kopā būtu kopīgas malas ar ne vairāk kā 12 baltām rūtiņām, turpretī balto rūtiņu būtu vismaz 13 — tātad kādai baltai rūtiņai nebūtu kopīgas malas ne ar vienu melnu.


# <lo-sample/> PL.OMJ.2026TEST.7_8.5

Eksistē taisnleņķa trijstūris, kurā divu malu garumi ir veseli skaitļi, bet trešās malas garums ir

**(a)** $\sqrt{20}$;

**(b)** $\sqrt{21}$;

**(c)** $\sqrt{22}$.

<small>

* answer:T,T,N
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Taisnleņķa trijstūrim ar katešu garumiem 4 un 2 hipotenūzas garums ir $\sqrt{4^2+2^2}=\sqrt{20}$.

b) Taisnleņķa trijstūrim ar katešu garumiem 2 un $\sqrt{21}$ hipotenūzas garums ir $\sqrt{2^2+21}=5$.

c) Ja taisnleņķa trijstūrim ar katešu garumiem $a$ un $b$ hipotenūzas garums ir $\sqrt{22}$, tad $a^2+b^2=22$. Tieši pārbaudām, ka skaitli 22 nevar izteikt kā divu (ne obligāti dažādu) saskaitāmo no saraksta 1, 4, 9, 16 summu, tāpēc nav iespējams, ka abi skaitļi $a$, $b$ būtu veseli.

Savukārt, ja taisnleņķa trijstūrim ar katešu garumiem $a$ un $\sqrt{22}$ hipotenūzas garums ir $c$, tad $c^2-a^2=22$, t.i., $(c-a)(c+a)=22$. Ja skaitļi $a$ un $c$ būtu veseli, tad skaitļi $c-a$ un $c+a$ būtu vai nu abi nepāra, vai abi pāra (jo tie atšķiras par pāra skaitli $2a$). Pirmajā gadījumā to reizinājums būtu nepāra skaitlis, bet otrajā — skaitlis, kas dalās ar 4; tātad nav iespējams, ka tas būtu vienāds ar 22.

**Piezīme.**

Nav grūti pārbaudīt, ka pāra vesela skaitļa kvadrāts, dalot ar 8, dod atlikumu 0 vai 4, bet nepāra vesela skaitļa kvadrāts, dalot ar 8, dod atlikumu 1.

Izmantojot šo faktu, konstatējam, ka skaitlis, kas ir divu veselu skaitļu kvadrātu summa, dalot ar 8, var dot tikai atlikumu 0, 1, 2, 4 vai 5, tāpēc tas nevar būt vienāds ar 22. Līdzīgi skaitlis, kas ir divu veselu skaitļu kvadrātu starpība, dalot ar 8, nevar dot atlikumu 2 vai 6 (tātad atkal nevar būt vienāds ar 22). Tādā veidā var alternatīvi atrisināt c) punktu.


# <lo-sample/> PL.OMJ.2026TEST.7_8.6

Eksistē tādi no nulles atšķirīgi skaitļi $x$ un $y$, ka skaitlis $(x+y)^2$ ir vienāds ar

**(a)** $x^2-y^2$;

**(b)** $x^2$;

**(c)** $x^2+y^2$.

<small>

* answer:T,T,N
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Ja $x=1$ un $y=-1$, tad $(x+y)^2=0=x^2-y^2$.

b) Ja $x=1$ un $y=-2$, tad $(x+y)^2=1=x^2$.

c) Tā kā $(x+y)^2=x^2+2xy+y^2$, tad vienādība $(x+y)^2=x^2+y^2$ nozīmē, ka $2xy=0$, un līdz ar to $x=0$ vai $y=0$. Tātad neeksistē no nulles atšķirīgi skaitļi $x$ un $y$, kas apmierina šo vienādību.

**Piezīme.**

Vienādību $(x+y)^2=x^2-y^2$ var pārveidot formā $2y(x+y)=0$, kas nozīmē, ka tā izpildās, ja $y=0$ vai $y=-x$. Savukārt $(x+y)^2=x^2$ var pārveidot formā $y(2x+y)=0$, kas nozīmē, ka tā izpildās, ja $y=0$ vai $y=-2x$.


# <lo-sample/> PL.OMJ.2026TEST.7_8.7

Kvadrātveida papīra lapu var sagriezt $n$ daļās, no kurām katra ir vienādsānu taisnleņķa trijstūris ar katetes garumu 2. No tā izriet, ka

**(a)** šīs lapas laukums ir $2n$;

**(b)** skaitlis $2n$ ir vesela skaitļa kvadrāts;

**(c)** to pašu lapu var sagriezt $2n$ daļās, no kurām katra ir taisnleņķa trijstūris ar hipotenūzas garumu 2.

<small>

* answer:T,N,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Vienādsānu taisnleņķa trijstūra ar katetes garumu 2 laukums ir $\frac12\cdot2\cdot2=2$. Tātad $n$ šādu trijstūru kopējais laukums ir $2n$.

b) Kvadrātu ar diagonāles garumu 4 var ar abām diagonālēm sagriezt četros vienādsānu taisnleņķa trijstūros ar katešu garumu 2. Tad iegūto daļu skaita divkāršotā vērtība ir 8 — tātad tā nav vesela skaitļa kvadrāts.

c) Vienādsānu taisnleņķa trijstūri ar katetes garumu 2 var pa augstumu, kas novilkts no taisnā leņķa virsotnes, sagriezt divos vienādsānu taisnleņķa trijstūros ar hipotenūzas garumu 2. Ja šādi sadalīsim katru uzdevumā aprakstītā sadalījuma daļu, iegūsim sagriezumu $2n$ daļās, no kurām katra ir vienādsānu taisnleņķa trijstūris ar hipotenūzas garumu 2.


# <lo-sample/> PL.OMJ.2026TEST.7_8.8

Eksistē divciparu naturāls skaitlis ar nenulles cipariem, kas, samainot vietām tā ciparus, palielinās

**(a)** par 20%;

**(b)** par 25%;

**(c)** par 75%.

<small>

* answer:T,N,T
* questionType:ShortAnswer

</small>

## Atrisinājums

b) Divciparu skaitlis ar desmitu ciparu $a$ un vienu ciparu $b$ ir vienāds ar $10a+b$, bet skaitlis, kas iegūts, samainot vietām tā ciparus, ir $10b+a$. Ja $a$ un $b$ nav nulles, tad nosacījumu $10b+a=\frac{125}{100}\cdot(10a+b)$ var ekvivalenti pārveidot pēc kārtas par

$$
10b+a=\frac54\cdot(10a+b),\qquad 40b+4a=50a+5b,\qquad 35b=46a,\qquad \frac{a}{b}=\frac{35}{46}.
$$

Iegūtā daļa ir nesaīsināma, tāpēc tā nav vienāda ar viencipara skaitļu dalījumu.

a) Skaitlis 45 apmierina uzdevuma nosacījumus, jo $54=45+9=45+\frac{20}{100}\cdot45$.

c) Skaitlis 12 apmierina uzdevuma nosacījumus, jo $21=12+9=12+\frac{75}{100}\cdot12$.

**Piezīme.**

a) punktā parādītais piemērs ir vienīgais, bet c) punktā meklētā īpašība piemīt arī skaitļiem 24, 36, 48. Lai atrastu šos piemērus, var pārveidot vienādības, kas analoģiskas b) punkta atrisinājumā uzrakstītajai.

Var arī balstīt spriedumu uz novērojumu, ka starpība starp skaitļiem $10b+a$ un $10a+b$ ir $9(b-a)$, tātad dalās ar 9.

a) punktā, ja eksistē skaitlis, kas apmierina uzdevuma nosacījumus, tad 20% no šī skaitļa dalās ar 9. Tātad pats skaitlis dalās ar 45. Ņemot vērā nosacījumu $a<b$ (kas nozīmē, ka skaitlis, samainot vietām ciparus, palielinājās) un to, ka cipari nav nulles, paliek tikai viens kandidāts: 45, kas patiešām apmierina uzdevuma nosacījumus.

Līdzīgi b) punktā 25% no meklētā skaitļa būtu jādalās ar 9, tāpēc pašam skaitlim būtu jādalās ar 36. Ņemot vērā nosacījumu $a<b$, paliek tikai skaitlis 36, kas tomēr neapmierina uzdevuma nosacījumus, jo skaitlis 63 ir par to lielāks par 75%, nevis par 25%.


# <lo-sample/> PL.OMJ.2026TEST.7_8.9

Eksistē tāds piecstūris, kurā

**(a)** kādas malas garums ir vienāds ar pārējo četru malu garumu summu;

**(b)** kādu divu blakus esošu malu garumu summa ir vienāda ar pārējo trīs malu garumu summu;

**(c)** kāda iekšējā leņķa lielums ir vienāds ar pārējo četru iekšējo leņķu lielumu summu.

<small>

* answer:N,T,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Lauztās līnijas, kas savieno divus punktus un neatrodas uz nogriežņa, kas savieno šos punktus, garums ir lielāks nekā šī nogriežņa garums.

![](PL.OMJ.2026TEST.7_8.9.png)

3. zīm.

![](PL.OMJ.2026TEST.7_8.9A.png)

4. zīm.

b) Aplūkosim kvadrātu $ABCD$ ar malas garumu 2 un tādu punktu $E$ ārpus šī kvadrāta, ka $AE=DE=3$ (3. zīm.). Tad

$$
AE+DE=3+3=2+2+2=AB+BC+CD.
$$

c) Aplūkosim kvadrātu $ABCD$ un punktu $S$, kas ir šī kvadrāta centrs (4. zīm.). Tad ieliektajā piecstūrī $ABCDS$ iekšējā leņķa pie virsotnes $S$ lielums ir $270^\circ$ un ir vienāds ar iekšējo leņķu lielumu summu pie pārējām četrām virsotnēm:

$$
\angle SAB+\angle ABC+\angle BCD+\angle CDS=45^\circ+90^\circ+90^\circ+45^\circ=270^\circ.
$$

**Piezīme.**

Jebkura piecstūra iekšējo leņķu lielumu summa ir $540^\circ$. Tātad c) punktā atbilstošs piemērs ir jebkurš piecstūris, kura viena iekšējā leņķa lielums ir $270^\circ$.


# <lo-sample/> PL.OMJ.2026TEST.7_8.10

Reālie skaitļi $a$, $b$ apmierina nevienādības $a^2>b^2$ un $a+b<0$. No tā izriet, ka

**(a)** $a>b$;

**(b)** $ab>0$;

**(c)** $a^3<b^3$.

<small>

* answer:N,N,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a), b) Ja $a=-2$, $b=1$, tad uzdevuma nosacījumi ir izpildīti, turklāt $a\leqslant b$ un $ab=-2\leqslant0$.

c) Pirmo nosacījumu varam pārveidot formā $a^2-b^2>0$, t.i., $(a-b)(a+b)>0$. Ja reizinātājs $a+b$ ir negatīvs skaitlis, tad reizinājums $(a-b)(a+b)$ ir pozitīvs tikai tad, ja reizinātājs $a-b$ ir negatīvs. Tas nozīmē, ka $a-b<0$, t.i., $a<b$.

Tā kā $a+b<0$, tad vismaz viens no skaitļiem $a$, $b$ ir negatīvs. Ja skaitlis $a$ ir negatīvs, bet skaitlis $b$ ir nenegatīvs, tad $a^3<0\leqslant b^3$. Savukārt, ja abi skaitļi $a$ un $b$ ir negatīvi, tad no nevienādības $a<b$ izriet, ka $|a|>|b|$. Līdz ar to $-a^3=|a|^3>|b|^3=-b^3$, t.i., $a^3<b^3$.

**Piezīme.**

Parādītais arguments, atsevišķi aplūkojot nesarežģīto gadījumu $0\leqslant a<b$, parāda arī, ka jebkuriem reāliem skaitļiem $a<b$ izpildās $a^3<b^3$. Kvadrātiem analoģisks fakts ir patiess, ja papildus pieņemam, ka skaitļi $a$, $b$ ir nenegatīvi.


# <lo-sample/> PL.OMJ.2026TEST.7_8.11

Katrā $3\times3$ tabulas rūtiņā ierakstīja veselu skaitli tā, ka skaitļu summa katrā rindā ir pāra skaitlis. No tā izriet, ka:

**(a)** eksistē vismaz trīs dažādas rūtiņas, kurās ierakstīts pāra skaitlis;

**(b)** eksistē kolonna, kurā ir trīs skaitļi ar pāra summu;

**(c)** eksistē divas rindas, kurās ir seši skaitļi ar summu, kas dalās ar 4.

<small>

* answer:T,T,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Katrā tabulas rindā ir trīs skaitļi ar pāra summu, tāpēc vismaz viens no šiem skaitļiem ir pāra — ja visi trīs būtu nepāra, to summa būtu nepāra. Tas nozīmē, ka eksistē vismaz trīs dažādas rūtiņas, kurās ierakstīti pāra skaitļi.

b) Visu tabulas skaitļu summa $S$ ir pāra skaitlis, jo tā ir trīs pāra skaitļu (rindu summu) summa. Ja skaitļu summa katrā kolonnā būtu nepāra, tad $S$ kā trīs nepāra skaitļu summa būtu nepāra. Tas nozīmē, ka vismaz vienā kolonnā ir trīs skaitļi ar pāra summu.

c) Katrā rindā skaitļu summa ir pāra skaitlis, tāpēc, dalot ar 4, tā dod atlikumu 0 vai 2. Ja kādu divu rindu summas dalās ar 4, tad arī sešu skaitļu summa šajās divās rindās dalās ar 4. Savukārt, ja ir ne vairāk kā viena rinda ar summu, kas dalās ar 4, tad ir vismaz divas rindas ar summu, kas, dalot ar 4, dod atlikumu 2. Sešu skaitļu summa šādās divās rindās ir skaitlis, kas dalās ar 4.


# <lo-sample/> PL.OMJ.2026TEST.7_8.12

Dota trapece $ABCD$ ar pamatiem $AB$ un $CD$, kurā $AB=AC=BD$. No tā izriet, ka

**(a)** $\angle BAD>60^\circ$;

**(b)** $BC\leqslant CD$;

**(c)** trijstūra $ABD$ laukums ir lielāks nekā trijstūra $BCD$ laukums.

<small>

* answer:T,N,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Ieviesīsim apzīmējumu $\angle BAD=\alpha$ (5. zīm.). Tā kā trapecei $ABCD$ ir vienāda garuma diagonāles, tad tā ir vienādsānu trapece, tāpēc $\angle ABC=\alpha$. Tā kā $AB=BD$, tad $\angle ADB=\alpha$ un $\angle ABD=180^\circ-2\alpha$. Tātad nevienādība $\angle ABC>\angle ABD$ iegūst formu

$$
\alpha>180^\circ-2\alpha,\qquad \text{t.i.,}\qquad \alpha>60^\circ.
$$

![](PL.OMJ.2026TEST.7_8.12.png)

5. zīm.

![](PL.OMJ.2026TEST.7_8.12A.png)

6. zīm.

b) Nevienādība $BC\leqslant CD$ ir ekvivalenta nevienādībai $\angle BDC\leqslant\angle CBD$, jo trijstūrī $BCD$ pret lielāko leņķi atrodas garākā mala. Izmantojot iepriekš ieviestos apzīmējumus, iegūstam

$$
\angle BDC=\angle ABD=180^\circ-2\alpha\qquad \text{un}\qquad \angle CBD=\alpha-(180^\circ-2\alpha)=3\alpha-180^\circ.
$$

Tātad iepriekšējā nevienādība izpildās tieši tad, ja

$$
180^\circ-2\alpha\leqslant3\alpha-180^\circ,\qquad \text{t.i.,}\qquad \alpha\geqslant72^\circ.
$$

Piemēru, kurā nevienādība $BC\leqslant CD$ neizpildās, iegūsim, ja $60^\circ<\alpha<72^\circ$.

Piemēram, pieņemsim, ka $ABD$ ir trijstūris, kurā $\angle BAD=\angle ADB=70^\circ$, un $C$ ir punktam $D$ simetrisks punkts attiecībā pret nogriežņa $AB$ vidusperpendikulu (6. zīm.). Trapece $ABCD$ apmierina uzdevuma nosacījumus, bet $\angle CDB=40^\circ>30^\circ=\angle CBD$, tāpēc $BC>CD$.

c) Vienādsānu trijstūrī $ABD$ leņķis starp pamatu un sānu malu ir šaurs, no kurienes $\angle BAD<90^\circ$. Līdz ar to vienādsānu trapeces $ABCD$ leņķi pie pamata $AB$ ir šauri, tātad pamats $AB$ ir garāks par pamatu $CD$. Trijstūra $ABD$ augstums, kas novilkts pret pamatu $AB$, ir vienāds ar trijstūra $BCD$ augstumu, kas novilkts pret pamatu $CD$ (tas ir attālums starp taisnēm $AB$ un $CD$), tāpēc lielāks laukums ir tam no šiem diviem trijstūriem, kuram ir garāks pamats. Tas nozīmē, ka trijstūra $ABD$ laukums ir lielāks nekā trijstūra $BCD$ laukums.

**Piezīme.**

Uzdevuma nosacījumus var ilustrēt arī ar šādu konstrukciju. Uzzīmēsim nogriezni $AB$ un taisnes $AB$ vienā pusē divus riņķa līniju lokus ar centriem $A$, $B$ un rādiusu $AB$. Pieņemsim, ka $E$ ir šo loku kopīgais punkts (7. zīm.).

![](PL.OMJ.2026TEST.7_8.12B.png)

7. zīm.

Ja šķelsim šo figūru ar taisni, kas ir paralēla $AB$ un krusto lokus attiecīgi punktos $D$ un $C$, tad iegūsim trapeci $ABCD$. No konstrukcijas $BD=AB=AC$. Šādā veidā var iegūt jebkuru trapeci, kas apmierina uzdevuma nosacījumus.

Šī konstrukcija sniedz intuīciju, kas slēpjas aiz b) punktā konstruētā piemēra. Ja taisni $CD$ novilksim pietiekami tuvu punktam $E$, tad nogrieznis $CD$ būs ļoti īss, turpretī nogrieznis $BC$ paliks ievērojami garāks. Tātad iegūsim trapeci, kurai $BC>CD$.


# <lo-sample/> PL.OMJ.2026TEST.7_8.13

Pozitīvi veseli skaitļi $a$, $b$ ir tādi, ka $\frac1a+\frac1b=\frac1{12}+\frac1{24}$. No tā izriet, ka

**(a)** skaitļi $a$ un $b$ ir dažādi;

**(b)** skaitlis $a+b$ ir pāra;

**(c)** skaitlis $a\cdot b$ nedalās ar 5.

<small>

* answer:N,N,N
* questionType:ShortAnswer

</small>

## Atrisinājums

Ievērosim, ka $\frac1{12}+\frac1{24}=\frac3{24}=\frac18$.

a) Ja $a=b=16$, tad $\frac1{16}+\frac1{16}=\frac18$, un skaitļi $a$ un $b$ ir vienādi.

b) Ja $a=9$ un $b=72$, tad $\frac19+\frac1{72}=\frac18$, un skaitlis $a+b=81$ ir nepāra.

c) Ja $a=10$ un $b=40$, tad $\frac1{10}+\frac1{40}=\frac18$, un skaitlis $a\cdot b=400$ dalās ar 5.

**Piezīme.**

Lai atrastu visus vienādojuma $\frac1a+\frac1b=\frac18$ atrisinājumus, var rīkoties šādi. Vispirms ievērojam, ka, ja $a$, $b$ apmierina šo vienādojumu, tad $\frac1a<\frac18$ un $\frac1b<\frac18$, no kurienes $a>8$ un $b>8$. Ekvivalenti pārveidojam vienādojumu pēc kārtas formās

$$
8a+8b=ab,\qquad 0=ab-8a-8b,\qquad 64=ab-8a-8b+64,\qquad 64=(a-8)(b-8).
$$

Tā kā $a>8$, $b>8$, tad reizinātāji $a-8$ un $b-8$ ir pozitīvi veseli skaitļi. Skaitli 64 (līdz pat secībai) var izteikt kā divu šādu skaitļu reizinājumu šādos veidos: $1\cdot64$, $2\cdot32$, $4\cdot16$ un $8\cdot8$. Tas nozīmē, ka visi pāri $(a,b)$, kas apmierina uzdevuma nosacījumus un kuros $a\leqslant b$, ir: $(9,72)$, $(10,40)$, $(12,24)$, $(16,16)$.


# <lo-sample/> PL.OMJ.2026TEST.7_8.14

Pjotrs atzīmēja uz lapas četrus dažādus punktus, no kuriem nekādi trīs neatrodas uz vienas taisnes. Pēc tam katrus divus no šiem punktiem viņš savienoja ar nogriezni. Izrādījās, ka starp šo nogriežņu garumiem ir tikai divi dažādi skaitļi. No tā izriet, ka

**(a)** kādi divi no uzzīmētajiem nogriežņiem ir perpendikulāri;

**(b)** kādiem diviem no uzzīmētajiem nogriežņiem ir kopīgs punkts, kas nav neviena no tiem galapunkts;

**(c)** kādi trīs no atzīmētajiem punktiem ir vienādmalu trijstūra virsotnes.

<small>

* answer:N,N,N
* questionType:ShortAnswer

</small>

## Atrisinājums

a), c) Ja Pjotrs atzīmēja četras no piecām regulāra piecstūra virsotnēm, tad starp uzzīmētajiem nogriežņiem ir tikai divi garumi: piecstūra malas garums un diagonāles garums. Nekādi divi no uzzīmētajiem nogriežņiem nav perpendikulāri, un nekādi trīs no atzīmētajiem punktiem nav vienādmalu trijstūra virsotnes.

b) Ja Pjotrs atzīmēja kāda vienādmalu trijstūra virsotnes un centru, tad starp uzzīmētajiem nogriežņiem ir tikai divi garumi: trijstūra malas garums un tā centra attālums līdz virsotnei. Nekādiem diviem no uzzīmētajiem nogriežņiem nav kopīgu punktu, izņemot galapunktus.

**Piezīme.**

8. zīmējumā parādītas visas (līdz pat līdzībai) 4 plaknes punktu konfigurācijas, starp kuriem ir tikai divi dažādi attālumi. Viens no garumiem ir atzīmēts ar treknu līniju, bet otrs — ar raustītu. Pirmās divas konfigurācijas ir minētas parādītajos atrisinājumos.

![](PL.OMJ.2026TEST.7_8.14.png)

8. zīm.


# <lo-sample/> PL.OMJ.2026TEST.7_8.15

Uz kuba ar šķautni 2 virsmas atzīmēja 20 punktus: visas virsotnes un visu šķautņu viduspunktus. Starp nogriežņiem, kuru abi galapunkti ir atzīmētajos punktos, ir tieši 24 nogriežņi ar garumu

**(a)** 1;

**(b)** 2;

**(c)** 3.

<small>

* answer:T,T,T
* questionType:ShortAnswer

</small>

## Atrisinājums

a) Attālums starp atzīmētajiem punktiem ir 1 tieši tad, ja viens no tiem ir kādas kuba šķautnes viduspunkts, bet otrs — šīs šķautnes galapunkts. Katrai no 12 kuba šķautnēm ir divi galapunkti, tāpēc kopējais visu nogriežņu ar garumu 1 skaits ir $12\cdot2=24$.

b) Attālums starp atzīmētajiem punktiem ir 2, ja tie ir vienas kuba šķautnes galapunkti (šādu pāru ir 12) vai ja tie ir kādas kuba skaldnes pretējo malu viduspunkti (katrā skaldnē ir divi šādi pāri, tāpēc kopā šādu pāru ir $6\cdot2=12$). Tātad kopējais nogriežņu ar garumu 2 skaits ir 24.

c) Attālums starp atzīmētajiem punktiem ir 3 tikai tad, ja viens no šiem punktiem ir kuba virsotne, bet otrs — vienas no trim šķautnēm, kas iziet no tai pretējās virsotnes, viduspunkts. Kopējais šādu pāru skaits ir $8\cdot3=24$.

**Piezīme.**

Lai izsmeļoši pamatotu, ka nogriežņi ar garumiem 1, 2, 3 neparādās citās situācijās, kā vien atrisinājumā aprakstītajās, aplūkosim visus iespējamos nogriežņu veidus atkarībā no tā, kāda veida ir to galapunkti. Ja abi nogriežņa galapunkti ir kuba virsotnes (9. zīm.), tad šī nogriežņa garums ir:

* 2, ja tas ir kuba šķautne;

* $2\sqrt2$, ja tas ir kādas skaldnes diagonāle;

* $2\sqrt3$, ja tas ir kuba diagonāle.

Ja abi nogriežņa galapunkti ir kuba šķautņu viduspunkti (10. zīm.), tad šī nogriežņa garums ir:

* $\sqrt2$, ja tie ir kādas skaldnes blakus esošo malu viduspunkti;

* 2, ja tie ir kādas skaldnes pretējo malu viduspunkti;

* $\sqrt6$, ja tie ir kāda šķērsu šķautņu pāra viduspunkti;

* $2\sqrt2$, ja tie ir kāda pretējo šķautņu pāra viduspunkti.

Ja viens nogriežņa galapunkts ir kuba virsotne, bet otrs — šķautnes viduspunkts (11. zīm.), tad šī nogriežņa garums ir:

* 1, ja tas ir tādas šķautnes viduspunkts, kuras galapunkts ir dotā virsotne;

* $\sqrt5$, ja tas ir tādas šķautnes viduspunkts, kas atrodas tajā pašā skaldnē, kurā dotā virsotne, bet nebeidzas tajā;

* 3, ja tas ir tādas šķautnes viduspunkts, kas iziet no pretējās virsotnes.

![](PL.OMJ.2026TEST.7_8.15.png)

9. zīm.

![](PL.OMJ.2026TEST.7_8.15A.png)

10. zīm.

![](PL.OMJ.2026TEST.7_8.15B.png)

11. zīm.

Turpmākajā tabulā parādīts kopējais nogriežņu skaits ar katru no garumiem.

| garums | 1 | $\sqrt2$ | 2 | $\sqrt5$ | $\sqrt6$ | $2\sqrt2$ | 3 | $2\sqrt3$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| nogriežņu skaits | 24 | 24 | 24 | 48 | 24 | 18 | 24 | 4 |
