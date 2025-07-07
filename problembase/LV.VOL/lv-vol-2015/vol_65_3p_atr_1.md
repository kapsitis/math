# Latvijas 65. matemātikas olimpiādes 3. posma uzdevumi un atrisinājumi 

9.1. Atrast visus tādus naturālus skaitļus $n$ un $m$, kuriem $\frac{2015}{n^{4}-m^{4}}$ arī ir naturāàs skaitlis!

## Atrisinājums

Ievērojam, ka $n^{4}-m^{4}=(n-m)(n+m)\left(n^{2}+m^{2}\right)$. Tā kā $n$ un $m$ ir naturāli skaitli, tad $\frac{2015}{(n-m)(n+m)\left(n^{2}+m^{2}\right)}$ var būt naturāls skaitlis tikai tad, ja $n>m \geq 1$. Līdz ar to $1 \leq n-m<n+m<n^{2}+m^{2}$. Tas nozīmē, ka $n-m, n+m$ un $n^{2}+m^{2}$ ir trīs dažādi skaitlaa 2015 dalītāji. Sadalām skaitli 2015 pirmreizinātājos: $2015=5 \cdot 13 \cdot 31$. Uzrakstām augošā secībā visus skaitlaa 2015 dalītājus: $1,5,13,31,65,155,403,2015$.

Novērtējam saucēja izteiksmi:

$$
n^{4}-m^{4} \geq n^{4}-(n-1)^{4}=4 n^{3}-6 n^{2}+4 n-1=4 n(n-1)^{2}+2 n^{2}-1>4(n-1)^{3}-1
$$

Tā kā $n^{4}-m^{4} \leq 2015$, tad arī $4(n-1)^{3}-1<2015$. No kurienes iegūstam, ka $(n-1)^{3}<504<512=8^{3}$, tātad $n-1<8$ jeb $n<9$. Līdz ar to esam ieguvuši, ka lielākā iespējamā $n$ vērtība ir 8 un $n+m \leq 8+7=15$. Apskatām visus iespējamos gadījumus.

| $n-m$ | $n+m$ | $n$ | $m$ | $n^{2}+m^{2}$ |  |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 5 | $\mathbf{3}$ | $\mathbf{2}$ | 13 | Der, jo 2015: $(1 \cdot 5 \cdot 13)=31$. |
| 1 | 13 | 7 | 6 | 85 | Neder, jo nav 2015 dalītājs. |
| 5 | 13 | 9 | 4 | 97 | Neder, jo nav 2015 dalītājs. |

Tātad vienīgās iespējamās vērtības ir $n=3$ un $m=2$.

Piezīme. Var iegūt arī vājāku summas $n+m$ novērtējumu. Ievērojam: ja $n^{2}+m^{2}=2015$, tad $n-m=n+m=1$, kas nav dažādi skaitli. Tātad $n^{2}+m^{2} \leq 403<441=21^{2}$. Līdz ar to ne $n$, ne $m$ nevar pārsniegt 21 , tātad $n+m \leq 42$. Šajā gadījumā papildus jāpārbauda vēl arī tās vērtības, kurām $n+m=31$.

9.2. Pierādīt, ka, izmantojot

a) visas septinas dotās figūras (skat 1. att.), katru tieši vienu reizi, nav iespējams salikt taisnstūri;

b) sešas no dotajām figūrām, katru tieši vienu reizi, var salikt taisnstūri.

Visas figūras sastāv no vienādiem kvadrātiem. Figūras drīkst pagriezt, bet nedrīkst apmest otrādi. Taisnstūrī nedrīkst būt caurumi, un figūras nedrīkst pārklāties.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-01.jpg?height=106&width=1083&top_left_y=1963&top_left_x=492)

1. att.

## Atrisinājums

a) Visas septiņas dotās figūras kopā satur 28 rūtiņas, tātad taisnstūra laukumam arī jābūt 28 rūtinām. Vienīgie iespējamie taisnstūra izmēri ir $1 \times 28$ (neder), $2 \times 14,4 \times 7$. Izkrāsojot taisnstūrus kā šaha galdinu, katrā no tiem melno un balto rūtinuu skaits ir vienāds. Ja visas dotās figūras izkrāsotu kā šaha galdinu, tad tās visas, izṇemot trešo, saturēu tieši divas katras krāsas rūtinas. Trešā figūra saturētu trīs vienas krāsas un vienu otras krāsas rūtinu (skat. A1. att.). Tātad, saskaitot balto un melno rūtinu skaitu pa visām septiņām figūrām, iegūtu, ka vienas krāsas rūtinu ir par divām vairāk nekā otras krāsas rūtiņu. Līdz ar to, izmantojot visas septiņas dotās figūras, taisnstūri izveidot nav iespējams.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-01.jpg?height=112&width=304&top_left_y=2491&top_left_x=882)

A1. att.
b) Ja neizmanto trešo figūru, tad taisnstūri ir iespējams izveidot (skat., piemēram, A2. att.).

A2. att.

9.3. Aija izvēlas naturālu skaitli $n \leq 100$ un veido skaitļu virkni, kur katru nākamo virknes locekli iegūst pēc šāda likuma:

- ja $2 n \leq 100$, tad virknes nākamais loceklis ir $2 n$;
- ja $2 n>100$, tad virknes nākamais loceklis ir $2 n-100$.

Ja virknē vēl kādreiz parādās skaitlis $n$, tad skaitli $n$ sauksim par patīkamu. Cik pavisam ir patīkamu skaitḷu, kas nepārsniedz 100?

Piemēram, skaitlis 40 ir patīkams, jo $40 ; 80 ; 60 ; 20 ; 40 ; \ldots$, bet 25 - nav, jo $25 ; 50 ; 100 ; 100 ; \ldots$ (tālāk virknē nav skaitḷu, kas atškirī̄gi no 100).

## Atrisinājums

1. risinājums. Ir 25 skaitli, kas nepārsniedz 100 un dalās ar 4. Parādīsim, ka visi šie skaitļi ir patīkami. Katrs no tiem pieder vienam no trim cikliem:

$100 \rightarrow 100$;

$20 \rightarrow 40 \rightarrow 80 \rightarrow 60 \rightarrow 20$;

$4 \rightarrow 8 \rightarrow 16 \rightarrow 32 \rightarrow 64 \rightarrow 28 \rightarrow 56 \rightarrow 12 \rightarrow 24 \rightarrow 48 \rightarrow 96 \rightarrow 92 \rightarrow 84 \rightarrow 68 \rightarrow 36 \rightarrow 72 \rightarrow 44 \rightarrow 88 \rightarrow 76 \rightarrow 52 \rightarrow 4$

Pierādīsim, ka tie skaitļi, kas nedalās ar 4 , nevar būt patīkami. Škiirojam divus gadījums.

- Nepāra skaitḷi nevar būt patīkami, jo visi nākamie virknes locekḷi būs tikai pāra skaitḷi un, tātad, sākotnējā $n$ vērtība tajā atkārtoti parādīies nevar.
- Pāra skaitli, kas nedalās ar 4 , var pierakstīt formā $n=4 k+2$. Šajā gadījumā otrais virknes loceklis būs vai nu $2 \cdot(4 k+2)=4 \cdot(2 k+1)$, vai $2 \cdot(4 k+2)-100=4 \cdot(2 k-24)$. Abos gadījumos virknes otrais loceklis dalās ar 4 un tas ir uzrakstāms formā 4 m . Visi nākamie virknes loceklị arī dalīsies ar 4 , jo vai nu $2 \cdot 4 m=8 m$, vai $2 \cdot 4 m-100=4 \cdot(2 m-25)$. Līdz ar to virknē nevar atkārtoti parādīties skaitlis, kas nedalās ar 4 , un skaitlis $n=4 k+2$ nav patīkams.

Tātad pavisam ir 25 patīkami skaitli.

2. risinājums. Ir 25 skaitḷi, kas nepārsniedz 100 un dalās ar 4. Parādīsim, ka visi šie skaitlii ir patīkami. Ja skaitlis $x$ dalās ar 4 , tad gan $2 x$, gan $2 x-100$ arī dalīsies ar 4. Aplūkosim virkni, sākot ar patvalīgu skaitli $x_{1}$, kas dalās ar 4: $x_{1}, x_{2}, x_{3}, \ldots$ Tā kā ir tikai 25 skaitlli, kas tajā var parādīties, tad skaidrs, ka kādā brīdī virknes locekḷi sāks atkārtoties. Aplūkosim pirmo skaitli virknē, kas atkārtojas, tas ir, tādu $x_{j+1}$, ka visi iepriekšējie $x_{1}, x_{2}, \ldots, x_{j}$ ir dažādi, bet $x_{j+1}$ ir vienāds ar kādu no tiem. Pierādīsim, ka $x_{j+1}=x_{1}$, ar to arī būs pierādīts, ka skaitlis $x_{1}$ ir patīkams. Pieņemsim pretējo, ka $x_{j+1}=x_{k+1}$ un aplūkosim, kādi varēja būt iepriekšējie skaitḷi $x_{j}$ un $x_{k}$. Tā kā tiem jābūt dažādiem, tad skaidrs, ka $x_{j+1}$ un $x_{k+1}$ tika iegūti ar dažāām darbībām, tas ir, $x_{j+1}=2 x_{j}$ un $x_{k+1}=2 x_{k}-100$ (vai otrādi), kas nozīmē, ka $2 x_{j}=2 x_{k}-100$ jeb $x_{k}-x_{j}=50$ un tā ir pretruna, jo gan $x_{j}$, gan $x_{k}$ dalās ar 4 , bet 50 nedalās ar 4 .

Vēl jāpierāda, ka pārējie skaitļi nav patīkami. Skaidrs, ka nepāra skaitḷi nav patīkami, jo, ja $x$ ir nepāra skaitlis, tad gan $2 x$, gan $2 x-100$ ir pāra skaitli un tālāk virknē visi skaitli būs pāra.

Ja skaitlis $x$ dalās ar 2 , bet nedalās ar 4 , tad x nav patīkams, jo, gan $2 x$, gan $2 x-100$ dalās ar 4 un tālāk virknē visi skaitļi dalīsies ar 4 .

9.4. Trijstūrī $A B C$ novilkta bisektrise $B L$ ( $L$ atrodas uz malas $A C$ ), tā krusto taisni, kas no $A$ vilkta paralēli $B C$, punktā $K$. Zināms, ka $L K=A B$. Pierādīt, ka $A B>B C$ !

## Atrisinājums

Tā kā $\angle L B C=\angle L B A$ pēc bisektrises definīcijas un $\angle L B C=\angle A K B$ kā iekšējie šķērsleņki pie paralēlām taisnēm $B C$ un $A K$, tad $\angle L B A=\angle A K B$ un trijstūris $A K B$ ir vienādsānu, pie kam $A B=A K$ (skat. A3. att.). Arī trijstūris $A K L$ ir vienādsānu, jo pēc dotā un iepriekš iegūtā $L K=A B=A K$. Vienādsānu trijstūrim lenki pie pamata ir vienādi, tāpēc $\angle A L K=\angle L A K$.

Tā kā $\angle A L K=\angle B L C$ kā krustleņki un $\angle L A K=\angle A C B$ kā iekšējie šķērsleņki pie paralēlām taisnēm $B C$ un $A K$, tad $\angle B L C=\angle B C L$ un trijstūris $L B C$ ir vienādsānu, pie kam $B L=B C$.

No trijstūra nevienādības $A B+A K>B K=B L+L K=B C+A K$ un no tā seko, ka $A B>B C$.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-03.jpg?height=343&width=692&top_left_y=685&top_left_x=708)

9.5. Kāda ir izteiksmes $a^{20}+a^{4}+\frac{1}{a^{4}+1}$ mazākā iespējamā vērtība, ja $a$ ir reāls skaitlis?

## Atrisinājums

1. risinājums. Dotās izteiksmes mazākā iespējamā vērtība ir 1 , to iegūst, ja $a=0$. Pamatosim, ka mazāku vērtību nevar iegūt.

Ekvivalenti pārveidojam doto izteiksmi: $a^{20}+a^{4}+\frac{1}{a^{4}+1}=a^{20}+\frac{a^{8}+a^{4}+1}{a^{4}+1}=a^{20}+\frac{a^{8}}{a^{4}+1}+1$.

Pirmie divi saskaitāmie ir nenegatīvi, tātad šīs izteiksmes vērtība ir vismaz 1.

2. risinājums. Dotās izteiksmes mazākā iespējamā vērtība ir 1, to iegūst, ja $a=0$. Pamatosim, ka mazāku vētību nevar iegūt.

Ekvivalenti pārveidojam doto izteiksmi: $a^{20}+a^{4}+\frac{1}{a^{4}+1}=a^{20}-1+\left(a^{4}+1\right)+\frac{1}{a^{4}+1}$.

No sakarības starp vidējo aritmētisko un vidējo ġeometrisko izriet, ka

$$
\left(a^{4}+1\right)+\frac{1}{a^{4}+1} \geq 2 \cdot \sqrt{\left(a^{4}+1\right) \cdot \frac{1}{a^{4}+1}}=2
$$

Tā kā $a^{20} \geq 0$, tad iegūstam $a^{20}+a^{4}+\frac{1}{a^{4}+1} \geq 0-1+2=1$. Tātad dotās izteiksmes vērtiba ir vismaz 1 .

10.1. Kvadrātvienādojuma

$$
(1+\sqrt{5}) x^{2}-\sqrt[4]{\frac{7}{3+\sqrt{5}}} \cdot(1+\sqrt{5})^{2} x+\sqrt[4]{\frac{7}{3+\sqrt{5}}}=0
$$

saknes ir skaitli $a$ un $b$. Pierādīt, ka izteiksmes $a^{4} b+a b^{4}+3 a^{3} b^{2}+3 a^{2} b^{3}$ vērtība ir vesels skaitlis!

## Atrisinājums

No Vjeta teorēmas izriet, ka

$$
\left\{\begin{array}{l}
a+b=\sqrt[4]{\frac{7}{3+\sqrt{5}}} \cdot(1+\sqrt{5}) \\
a b=\sqrt[4]{\frac{7}{3+\sqrt{5}}} \cdot \frac{1}{1+\sqrt{5}}
\end{array}\right.
$$

Pārveidojam doto izteiksmi:

$a^{4} b+a b^{4}+3 a^{3} b^{2}+3 a^{2} b^{3}=a b\left(a^{3}+b^{3}+3 a^{2} b+3 a b^{2}\right)=a b(a+b)^{3}=$

$=\sqrt[4]{\frac{7}{3+\sqrt{5}}} \cdot \frac{1}{1+\sqrt{5}} \cdot \sqrt[4]{\left(\frac{7}{3+\sqrt{5}}\right)^{3}} \cdot(1+\sqrt{5})^{3}=\frac{7}{3+\sqrt{5}} \cdot(1+\sqrt{5})^{2}=$

$=\frac{7 \cdot(1+2 \sqrt{5}+5)}{3+\sqrt{5}}=\frac{7 \cdot 2 \cdot(3+\sqrt{5})}{3+\sqrt{5}}=14$.

Tā kā skaitlis 14 ir vesels skaitlis, tad prasītais ir pierādīts.

10.2. Pierādīt, ka katram naturālam $n$ izteiksme $3 n^{5}+5 n^{4}-8 n$ dalās ar 10 .

## Atrisinājums

1. risinājums. Izmantosim matemātiskās indukcijas principu.

Indukcijas bāze. Ja $n=1$, tad $3+5-8=0$ dalās ar 10 .

Induktīvā pieņēmums. Pieņemsim, ja $n=k, \operatorname{tad} 3 k^{5}+5 k^{4}-8 k$ dalās ar 10 .

Induktūvā pāreja. Pierādīsim, ja $n=k+1$, tad $3(k+1)^{5}+5(k+1)^{4}-8(k+1)$ dalās ar 10 .

Ekvivalenti pārveidojam izteiksmi $3(k+1)^{5}+5(k+1)^{4}-8(k+1)$ :

$$
\begin{aligned}
& 3\left(k^{5}+5 k^{4}+10 k^{3}+10 k^{2}+5 k+1\right)+5\left(k^{4}+4 k^{3}+6 k^{2}+4 k+1\right)-8(k+1)= \\
& =3 k^{5}+20 k^{4}+50 k^{3}+60 k^{2}+27 k=3 k^{5}+5 k^{4}-8 k+15 k^{4}+50 k^{3}+60 k^{2}+35 k= \\
& =3 k^{5}+5 k^{4}-8 k+5 k \cdot\left(3 k^{3}+10 k^{2}+12 k+7\right)
\end{aligned}
$$

Saskaitāmais $3 k^{5}+5 k^{4}-8 k$ dalās ar 10 pēc induktīvā pieņēmuma.

Saskaitāmais $5 k \cdot\left(3 k^{3}+10 k^{2}+12 k+7\right)$ dalās ar 5 , jo satur reizinātāju 5 , un dalās ar 2 , jo

- ja $k$ ir pāra skaitlis, tad reizināāājs $k$ dalās ar 2;
- ja $k$ ir nepāra skaitlis, tad reizināāās $3 k^{3}+10 k^{2}+12 k+7$ ir pāra skaitlis un tas dalās ar 2 .

Tā kā izteiksme $3(k+1)^{5}+5(k+1)^{4}-8(k+1)$ dalās gan ar 2, gan ar 5 , tad tā dalās arī ar 10 un līdz ar to esam pierādījuši, ka $3(k+1)^{5}+5(k+1)^{4}-8(k+1)$ dalās ar 10 .

No matemātiskās indukcijas principa izriet, ka katram naturālam $n$ izteiksme $3 n^{5}+5 n^{4}-8 n$ dalās ar 10 , kas arī bija jāpierāda.

2. risinājums. Pārveidojam doto izteiksmi:

$$
\begin{aligned}
& 3 n^{5}+5 n^{4}-8 n=n\left(3 n^{4}-3 n^{3}+8 n^{3}-8\right)=n\left(3 n^{3}(n-1)+8\left(n^{3}-1\right)\right)= \\
& =n\left(3 n^{3}(n-1)+8(n-1)\left(n^{2}+n+1\right)\right)=n(n-1)\left(3 n^{3}+8\left(n^{2}+n+1\right)\right)
\end{aligned}
$$

Viens no reizinātājiem $n$ vai $n-1$ ir pāra skaitlis, tāpēc noteikti dotā izteiksme dalās ar 2. Vēl jāpierāda, ka dotā izteiksme dalās ar 5 .

Skaitli $n$ dalot ar 5, iespējamas piecas dažādas atlikumu vērtības: $0,1,2,3,4$. Apskatām visus gadījumus:

- $n=5 k$, tad reizināāās $n$ dalās ar 5 ;
- $n=5 k+1$, tad reizinātājs $n-1$ dalās ar 5 ;
- $n=5 k+2$ jeb $n \equiv 2(\bmod 5), \operatorname{tad}$

$$
3 n^{3}+8 \cdot\left(n^{2}+n+1\right) \equiv 3 \cdot 8+8 \cdot(4+2+1) \equiv 4+1 \equiv 0(\bmod 5)
$$

- $n=5 k+3$ jeb $n \equiv 3(\bmod 5)$, tad

$$
3 n^{3}+8 \cdot\left(n^{2}+n+1\right) \equiv 3 \cdot 27+8 \cdot(9+3+1) \equiv 1+4 \equiv 0(\bmod 5)
$$

- $n=5 k+4$ jeb $n \equiv 4(\bmod 5)$, tad

$$
3 n^{3}+8 \cdot\left(n^{2}+n+1\right) \equiv 3 \cdot 64+8 \cdot(16+4+1) \equiv 2+3 \equiv 0(\bmod 5)
$$

Esam ieguvuši, ka visos gadījumos dotā izteiksme dalās gan ar 2, gan ar 5, tātad tā dalās ar 10 .

10.3. Pozitīviem skaitlliem $a, b, c, d, e, f$ ir spēkā sakarības $a^{2}+b^{2}=c^{2}$ un $d^{2}+e^{2}=f^{2}$. Pierādīt, ka $(a+d)^{2}+(b+e)^{2} \leq(c+f)^{2}$.

## Atrisinājums

1. risinājums. Tā kā visi dotie skaitḷi ir pozitīvi, varam tos uztvert kā nogriežñu garumus.

Apskatām taisnleņka trijstūri $K L M$ ar katešu garumiem $K L=a+d$ un $K M=e+b$ (skat. A4. att.). Novelkam nogriežņus $N O \| K M$ un $O P \| K L$ tā, ka $K N=O P=a$ un $K P=N O=e$. No dotajām sakarībām un Pitagora teorēmas trijstūros $O P M$ un $L N O$, iegūstam, ka $O M=c$ un $L O=f$.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-05.jpg?height=338&width=506&top_left_y=588&top_left_x=838)

A4. att.

Aprēķinām trijstūra $K L M$ hipotenūzas garumu: $L M=\sqrt{(a+d)^{2}+(b+e)^{2}}$. No trijstūra nevienādības trijstūrī $L M O$ izriet, ka $\sqrt{(a+d)^{2}+(b+e)^{2}} \leq c+f$. Tā kā abas nevienādības puses ir pozitīvas, tad, kāpinot kvadrātā, iegūst $(a+d)^{2}+(b+e)^{2} \leq(c+f)^{2}$, kas arī bija jāpierāda.

2. risinājums. Aplūkojam vektorus $\vec{x}=(a ; b)$ un $\vec{y}=(d ; e)$, tad

$$
\begin{aligned}
& |\vec{x}|=\sqrt{a^{2}+b^{2}}=\sqrt{c^{2}}=c \text { un }|\vec{y}|=\sqrt{d^{2}+e^{2}}=\sqrt{f^{2}}=f \\
& \vec{x}+\vec{y}=(a+d ; b+e) \text { un }|\vec{x}+\vec{y}|=\sqrt{(a+d)^{2}+(b+e)^{2}}
\end{aligned}
$$

Tad izteiksmi $(a+d)^{2}+(b+e)^{2} \leq(c+f)^{2}$ var pārrakstīt $|\vec{x}+\vec{y}|^{2} \leq(|\vec{x}|+|\vec{y}|)^{2}$, kas ir patiesa, jo jebkuriem diviem vektoriem $|\vec{x}+\vec{y}| \leq|\vec{x}|+|\vec{y}|$.

10.4. Pierād̄̄t, ka regulāram desmitstūrim $A_{1} A_{2} \ldots A_{10}$ ir spēkā sakarība $A_{1} A_{2}+R=A_{1} A_{4}$, kur $R$ ir tam apvilktās rinķa līijijas rādiuss!

## Atrisinājums

1. risinājums. Regulāram desmitstūrim $A_{1} A_{2} \ldots A_{10}$ apvilktās rinka līnijas centru apzīmēsim ar $O$ (skat. A5. att.). Regulāra desmitstūra katra mala savelk $360^{\circ}: 10=36^{\circ}$ lielu loku. Tad $\angle A_{1} A_{2} A_{7}=\frac{1}{2} \cup A_{1} A_{9} A_{7}=72^{\circ} \quad$ un $\quad \angle A_{2} A_{1} A_{4}=\frac{1}{2} \cup A_{2} A_{3} A_{4}=36^{\circ} \quad$ ka $\quad$ ievilktie leņi i un $\angle A_{2} O A_{4}=\cup A_{2} A_{3} A_{4}=72^{\circ} \quad$ kā centra lenkis. No $\triangle A_{1} A_{2} B$ iegūstam, ka $\angle A_{1} B A_{2}=180^{\circ}-36^{\circ}-72^{\circ}=72^{\circ}$.

Ievērojam, ka $\angle O B A_{4}=\angle A_{1} B A_{2}=72^{\circ}$ kā krustleņi̧i. Tātad $\triangle A_{1} A_{2} B$ un $\triangle O A_{4} B$ ir vienādsānu, jo leņki pie pamata ir vienādi, līdz ar to $A_{1} A_{2}=A_{1} B$ un $B A_{4}=O A_{4}=R$. Tad $A_{1} A_{2}+R=A_{1} B+B A_{4}=A_{1} A_{4}$, kas arī bija jāpierāda.

2. risinājums. Regulāram desmitstūrim $A_{1} A_{2} \ldots A_{10}$ apvilktās rinka līijas centru apzīmēsim ar $O$ (skat. A6. att.). Regulāra desmitstūra visas malas savelk vienāda lieluma lokus. Diagonāles $A_{1} A_{2}$, $A_{3} A_{10}$ un $A_{4} A_{9}$ ir savā starpā paralēlas, jo starp paralēlām hordām ir vienādi loki. Līdzīgi paralēlas ir arī diagonāles $A_{2} A_{3}, A_{1} A_{4}$ un $A_{5} A_{10}$, pie kam $A_{3} A_{10}=A_{1} A_{4}$, jo vienādus lokus savelk vienādas hordas.

Nogriežņi $A_{4} A_{9}$ un $A_{5} A_{10}$ ir diametri. Nogriežņu $A_{1} A_{4}$ un $A_{3} A_{10}$ krustpunktu apzīmējam ar $X$. Četrstūri $A_{1} A_{2} A_{3} X$ un $A_{10} X A_{4} O$ ir paralelogrami, jo to pretējās malas ir pa pāriem paralēlas. Tātad
$A_{1} A_{2}=X A_{3}$ un $O A_{4}=X A_{10}=R$. Tātad $A_{1} A_{2}+O A_{4}=A_{3} A_{10}$ jeb $A_{1} A_{2}+R=A_{1} A_{4}$, kas arī bija jāpierāda.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-06.jpg?height=669&width=735&top_left_y=311&top_left_x=269)

A5. att.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-06.jpg?height=669&width=721&top_left_y=314&top_left_x=1176)

A6. att.

10.5. a) Pierādīt, ka, izmantojot visas piecas dotās figūras (skat. 2. att.), katru tieši vienu reizi, nav iespējams salikt taisnstūri!

b) Vai, izmantojot četras no dotajām figūrām, katru tieši vienu reizi, var salikt taisnstūri?

Visas figūras sastāv no vienādiem kvadrātiem. Figūras drīkst pagriezt vai apmest otrādi. Taisnstūrī nedrīkst būt caurumi, un figūras nedrīkst pārklāties.

## Atrisinājums

a) Visas piecas dotās figūras kopā satur 20 rūtinas, tātad taisnstūra laukumam arī jābūt 20 rūtināam. Vienīgie iespējamie taisnstūra izmēri ir $1 \times 20$ (neder), $2 \times 10,4 \times 5$. Izkrāsojot taisnstūrus kā šaha galdinu, katrā no tiem melno un balto rūtiṇu skaits ir vienāds. Ja visas dotās figūras izkrāsotu kā šaha galdiṇu, tad tās visas, izṇemot trešo, saturētu tieši divas katras krāsas rūtinas. Trešā figūra saturētu trīs vienas krāsas un vienu otras krāsas rūtinuu (skat. A7. att.). Tātad, saskaitot balto un melno rūtinu skaitu pa visām piecām figūrām, iegūtu, ka vienas krāsas rūtiṇu ir par divām vairāk kā otras krāsas rūtinuu. Līdz ar to, izmantojot visas piecas dotās figūras, taisnstūri izveidot nav iespējams.

A7. att.

b) Četras no dotajām figūrām kopā satur 16 rūtinas, tātad taisnstūra laukumam arī jābūt 16 rūtinām. Vienīgie iespējamie taisnstūra izmēri ir $1 \times 16$ (neder), $2 \times 8,4 \times 4$. Spriežot līdzīgi kā a) gadījumā, secinām, ka nevar izmantot A7. att. redzamo figūru. Apskatīsim atlikušās četras figūras.

Izkrāsosim taisnstūrus joslās (skat. A8. att.).

A8. att.

Ievērojam, ka katrā taisnstūrī melno un balto rūtiņu skaits ir vienāds. Ja arī figūras izkrāsotu joslās, tad tās visas, izṇemot otro, saturētu tieši divas katras krāsas rūtinas. Otrā figūra saturētu trīs vienas krāsas un vienu otras krāsas rūtinu (skat. A9. att.). Tātad, saskaitot balto un melno rūtinu skaitu pa
visām četrām figūrām, iegūtu, ka vienas krāsas rūtinu ir par divām vairāk kā otras krāsas rūtiṇu. Līdz ar to, izmantojot četras no dotajām figūrām, taisnstūri izveidot nav iespējams.

A9. att.

11.1. Kvadrātvienādojuma

$$
(1+\sqrt{5}) x^{2}-\sqrt[4]{7} \cdot(1+\sqrt{5})^{2} x+\sqrt[4]{7}=0
$$

saknes ir skaitḷi $a$ un $b$. Pierādīt, ka izteiksmes $a^{4} b+a b^{4}+3 a^{3} b^{2}+3 a^{2} b^{3}+16 a^{4} b^{3}+16 a^{3} b^{4}$ vērtība ir vesels skaitlis!

## Atrisinājums

No Vjeta teorēmas izriet, ka

$$
\left\{\begin{array}{l}
a+b=\sqrt[4]{7} \cdot(1+\sqrt{5}) \\
a b=\frac{\sqrt[4]{7}}{1+\sqrt{5}}
\end{array}\right.
$$

Pārveidojam doto izteiksmi:

$a^{4} b+a b^{4}+3 a^{3} b^{2}+3 a^{2} b^{3}+16 a^{4} b^{3}+16 a^{3} b^{4}=a b\left(a^{3}+b^{3}+3 a^{2} b+3 a b^{2}+16 a^{3} b^{2}+16 a^{2} b^{3}\right)=$ $=a b\left((a+b)^{3}+16 a^{2} b^{2}(a+b)\right)=\frac{\sqrt[4]{7}}{1+\sqrt{5}} \cdot\left(\sqrt[4]{7^{3}} \cdot(1+\sqrt{5})^{3}+16 \cdot \frac{\sqrt[4]{7^{2}} \cdot \sqrt[4]{7} \cdot(1+\sqrt{5})}{(1+\sqrt{5})^{2}}\right)=$

$=7 \cdot(1+\sqrt{5})^{2}+\frac{16 \cdot 7}{(1+\sqrt{5})^{2}}=7 \cdot\left((6+2 \sqrt{5})+\frac{16}{6+2 \sqrt{5}}\right)=$

$=7 \cdot \frac{36+24 \sqrt{5}+20+16}{6+2 \sqrt{5}}=7 \cdot 12 \cdot \frac{6+2 \sqrt{5}}{6+2 \sqrt{5}}=84$.

Tā kā skaitlis 84 ir vesels skaitlis, tad prasītais ir pierādīts.

11.2. Vai uz rūtinu lapas var uzzīmēt 1612-stūri, kura laukums ir 2015 rūtinas un kura malas iet pa rūtinu līnijām?

## Atrisinājums

Jā, šādu daudzstūri var uzzīmēt (skat., piemēram, A10. att.).

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-07.jpg?height=292&width=593&top_left_y=1853&top_left_x=366)

A10. att.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-07.jpg?height=258&width=629&top_left_y=1884&top_left_x=1156)

A11. att.

Figūras būvēšanai izmantoti 403 taisnstūri ar izmēriem $1 \times 5$ rūtinas. Tātad iegūtā daudzstūra laukums ir $5 \cdot 403=2015$ rūtinas. Tā kā katrs taisnstūris satur tieši četras iegūtā daudzstūra malas, tad uzzīmēts ir $4 \cdot 403=1612$-stūris.

Piezīme. Daudzstūri var uzzīmēt arī, piemēram, kā A11. att.

11.3. Pirātam Džonam Silveram kajītē ir 38 papagailii un 39 papagaiḷu krātini. Katram papagailim ir savs krātiņš un vēl viens krātiṇš stāv tukšs. Kādu dienu vētras laikā tie visi izmuka, tika noķerti un uz ātru roku salikti atpakaḷ krātiņos (katrā krātinā ne vairāk kā viens), bet ne obligāti savos. Vienā gājienā Džons Silvers var paṇemt vienu papagaili un pārlikt uz to krātiṇu, kurš dotajā brīdī ir tukšs. Kāds ir mazākais gājienu skaits, ar kuru vinam noteikti pietiek, lai panāktu, ka visi papagaili atrodas savos sākotnējos krātinos?

## Atrisinājums

Apzīmēsim papagailịus ar numuriem no 1 līdz 38 un krātinus ar numuriem no 1 līdz 39 tā, ka sākotnēji papagaiḷa numurs sakrīt ar krātina numuru. Vienkāršības dēḷ tukšajā vietā sākumā ieliksim iedomātu papagaili ar numuru 39. N̦emsim patvaḹigu papagaili $a_{1}$, kas neatrodas savā krātiñā, pieņemsim, ka tas atrodas krātiṇā $a_{2}$. Tad $a_{2}$ arī neatrodas savā vietā un atrodas kādā vietā $a_{3}$, utt, līdz papagailis $a_{n}$ atrodas vietā $a_{1}(2 \leq n \leq 39)$. Tādā veidā visi papagaili sadalās ciklos. Ja ciklā ir $n$ papagaili, tad šī cikla sakārtošanai nepieciešams tieši

a) n-1 gājiens, ja tajā ietilpst tukšais krātiņš. Tad tur ir $n-1$ papagailis un ar katru gājienu ne vairāk kā vienu var ielikt savā krātinā, tātad mazāk gājienu nevar būt. Ar n-1 gājienu pietiek, jo vienmēr būs kāds papagailis, kuru ielikt savā vietā;
b) $n+1$ gājiens, ja tajā neietilpst tukšais krātinš. Ar pirmo gājienu nevienu papagaili nevar ielikt savā vietā un ar katru nākamo gājienu ne vairāk kā vienu papagaili var ielikt savā vietā, tāpēc mazāk būt nevar. Pirmajā gājienā jebkuru papagaili pārceļ uz tukšo krātinu, atlikušos $n-1$ sakārto kā a) gadījumā ar $n-1$ gājienu un pēdējā gājienā ieceḷ savā vietā to, kuru pārcēla pirmo.

Tātad kopējais nepieciešamais gājienu skaits ir

- papagaiļu skaits + ciklu skaits, ja nevienā ciklā neietilpst tukšais krātiņš
- papagaiḷu skaits + ciklu skaits - 1, ja kādā ciklā ietilpst tukšais krātiņš.

Redzams, ka maksimālais gājienu skaits būs nepieciešams tad, kad ciklu skaits ir maksimālais un nevienā ciklā neietilpst tukšais krātiņš. Minimālais papagaiḷu skaits ciklā ir 2, tāpēc maksimālais ciklu skaits ir $38: 2=19$, tātad maksimālais gājienu skaits, kāds var būt nepieciešams, ir $38+19=57$ gājieni. Redzam: ja papagaiḷus samaina vietām pa pāriem, tad tieši tik daudz gājieni arī ir vajadzīgi.

11.4. Naturāli skaitļi $a, b$ un $c$ ir savstarpēji pirmskaitli un visi ir lielāki nekā 50. Zināms, ka $a+b$ dalās ar $c$ un $b+c$ dalās ar $a$. Atrast mazāko iespējamo $b$ vērtību!

Atrisinājums

Mazākā iespējamā $b$ vērtība ir 2549. Pierādīsim, ka mazāku $b$ vērtību nav iespējams atrast.

Skaitlis $a+b+c$ dalās gan ar $a$ gan ar $c$, tātad $a+b+c$ dalās ar $a c$ (jo tie ir savstarpēji pirmskaitli). Tātad $a+b+c \geq a c$ jeb $b \geq a c-a-c=a c-a-c+1-1=(a-1)(c-1)-1$. Līdz ar to mazākā $b$ vērtība ir gadījumā, ja $a=51$ un $c=52$ (vai otrādi), t. i., $b=50 \cdot 51-1=2549$. Skaitli, $51,2549,52$ apmierina dotos nosacíjumus.

11.5. Pierādīt, ka regulāram četrpadsmitstūrim $A_{1} A_{2} \ldots A_{14}$ ir spēkā sakarība $A_{1} A_{2}+A_{1} A_{6}=A_{1} A_{4}+R$, kur $R$ ir tam apvilktās ringka līnijas rādiuss!

## Atrisinājums

1. risinājums. Regulāram četrpadsmitstūrim $A_{1} A_{2} \ldots A_{14}$ apvilktās riṇka līijas centru apzīmēsim ar $O$ (skat. A12. att.). Regulāra četrpadsmitstūra katras malas savilkto loku apzīmējam ar $\alpha=360^{\circ}: 14$.

Tad $\angle A_{2} A_{1} A_{4}=\angle A_{4} A_{3} A_{6}=\angle A_{6} A_{1} A_{8}=\alpha$ un $\angle A_{1} A_{2} A_{9}=\angle A_{3} A_{4} A_{11}=3 \alpha$ kā ievilktie leņki un $\angle A_{1} O A_{4}=3 \alpha$ kā centra leṇkis.

Ievērojam, ka $180^{\circ}=7 \alpha$. No $\triangle A_{1} A_{2} B$ iegūstam, ka $\angle A_{1} B A_{2}=7 \alpha-\alpha-3 \alpha=3 \alpha$, līdzīgi no $\triangle A_{3} A_{4} C$ iegūst $\angle A_{3} C A_{4}=3 \alpha$ un no $\triangle A_{1} O D$ iegūst $\angle A_{1} D O=3 \alpha$. Ievērojam, ka $\angle A_{1} D O=\angle A_{6} D C=3 \alpha$ un $\angle A_{3} C A_{4}=\angle D C A_{6}=3 \alpha$ kā krustleņi. Tātad $\triangle A_{1} A_{2} B, \triangle A_{3} A_{4} C$, $\triangle O A_{1} D$ un $\triangle A_{6} C D$ ir vienādsānu, jo lenki pie pamata ir vienādi. Līdz ar to $A_{1} B=A_{1} A_{2}=A_{3} A_{4}=A_{3} C$ un $A_{1} O=A_{1} D=R$, un $A_{6} D=A_{6} C$.

Tad $\quad A_{1} A_{2}+A_{1} A_{6}=A_{1} B+A_{1} D+D A_{6}=A_{3} C+R+C A_{6}=A_{3} A_{6}+R=A_{1} A_{4}+R, \quad$ kas arī bija jāpierāda.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-09.jpg?height=835&width=858&top_left_y=188&top_left_x=242)

A12. att.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-09.jpg?height=769&width=789&top_left_y=255&top_left_x=1133)

A13. att.

2. risinājums. Regulāram četrpadsmitstūrim $A_{1} A_{2} \ldots A_{14}$ apvilktās riņka līnijas centru apzīmēsim ar $O$ (skat. A13. att.). Regulāra četrpadsmitstūra visas malas savelk vienāda lieluma lokus. Diagonāles $A_{1} A_{2}, A_{3} A_{14}, A_{4} A_{13}$ un $A_{5} A_{12}$ ir savā starpā paralēlas, jo starp paralēlām hordām ir vienādi loki. Līdz̄̄gi paralēlas ir arī diagonāles $A_{2} A_{3}, A_{1} A_{4}, A_{5} A_{14}$ un $A_{6} A_{13}$, pie kam $A_{3} A_{14}=A_{1} A_{4}$ un $A_{4} A_{13}=A_{5} A_{14}$, jo vienādus lokus savelk vienādas hordas.

Nogriežnii $A_{5} A_{12}$ un $A_{6} A_{13}$ ir diametri. Nogriežņu $A_{1} A_{4}$ un $A_{5} A_{14}$ krustpunktu apzīmēsim ar $Y$. Četrstūris $X A_{4} Y A_{14}$ ir paralelograms, jo tā pretējās malas ir pa pāriem paralēlas. Tātad $A_{1} A_{2}=X A_{3}$ un $X A_{14}=A_{3} A_{14}-A_{1} A_{2}=A_{1} A_{4}-A_{1} A_{2}$.

Nogriežņu $A_{4} A_{13}$ un $A_{3} A_{14}$ krustpunktu apzīmēsim ar $X$. Četrstūris $A_{1} A_{2} A_{3} X$ ir paralelograms, jo tā pretējās malas ir pa pāriem paralēlas. Tātad $A_{4} Y=A_{14} X$ un $Y A_{13}=A_{4} A_{13}-X A_{14}=A_{1} A_{6}-A_{1} A_{4}+A_{1} A_{2}$.

Četrstūris $A_{13} Y A_{5} O$ arī ir paralelograms un $O A_{5}=Y A_{13}=R$. Tātad $A_{1} A_{6}-A_{1} A_{4}+A_{1} A_{2}=R$ jeb $A_{1} A_{2}+A_{1} A_{6}=A_{1} A_{4}+R$, kas arī bija jāpierāda.

12.1. Zināms, ka $\frac{\cos 3 x}{\cos x}=\frac{1}{2015}$. Aprēkināt $\frac{\sin 3 x}{\sin x}$ vērtību!

## Atrisinājums

1. risinājums. Aplūkosim starpību

$$
\frac{\sin 3 x}{\sin x}-\frac{\cos 3 x}{\cos x}=\frac{\sin 3 x \cos x-\cos 3 x \sin x}{\sin x \cdot \cos x}=\frac{\sin (3 x-x)}{\sin x \cdot \cos x}=\frac{\sin 2 x}{\sin x \cdot \cos x}=\frac{2 \sin x \cdot \cos x}{\sin x \cdot \cos x}=2
$$

Tātad $\frac{\sin 3 x}{\sin x}=2+\frac{1}{2015}=\frac{4031}{2015}$.

2. risinājums. Pārveidojam doto sakarību:

$$
\begin{aligned}
& \frac{\cos 3 x}{\cos x}=\frac{\cos (2 x+x)}{\cos x}=\frac{\cos 2 x \cos x-\sin 2 x \sin x}{\cos x}=\frac{\cos 2 x \cos x-2 \sin ^{2} x \cos x}{\cos x}= \\
& =\cos 2 x-2 \sin ^{2} x=1-2 \sin ^{2} x-2 \sin ^{2} x=1-4 \sin ^{2} x=\frac{1}{2015}
\end{aligned}
$$

Izsakot, iegūstam $4 \sin ^{2} x=\frac{2014}{2015}$. Aprēkināsim $\frac{\sin 3 x}{\sin x}$ vētību:

$\frac{\sin 3 x}{\sin x}=\frac{\sin (2 x+x)}{\sin x}=\frac{\sin 2 x \cos x+\cos 2 x \sin x}{\sin x}=\frac{2 \sin x \cos ^{2} x+\cos 2 x \sin x}{\sin x}=$

$=2 \cos ^{2} x+\cos 2 x=2\left(1-\sin ^{2} x\right)+\left(1-2 \sin ^{2} x\right)=3-4 \sin ^{2} x=3-\frac{2014}{2015}=\frac{4031}{2015}$.

12.2. Paralelograma $A B C D$ iekšpusē atzīmēts punkts $P$ tā, ka $\angle P A B=\angle P C B$. Pierādīt, ka $\angle P B C=\angle P D C$ !

## Atrisinājums

Apzīmējam $\angle P A B=\angle P C B=\alpha$. No virsotnes $D$ velk nogriezni $D Q$, kas paralēls $A P$, bet no $C-$ nogriezni $C Q$, kas paralēls $B P$ (skat. A14. att.). Trijstūri $A B P$ un $D C Q$ ir vienādi pēc pazīmes $\ell m \ell$ un to attiecīgie elementi ir vienādi, t. i., $P B=Q C$ un $\angle P A B=\angle Q D C=\alpha$. Tad $P B C Q$ ir paralelograms, jo $P B=Q C$ un $P B \| Q C$. Līdz ar to $\angle C P Q=\angle P C B=\alpha$ kā iekšējie šķērsleñki pie paralēlām taisnēm $P Q$ un $B C$. Ap četrstūri $D P C Q$ var apvilkt rinka līniju, jo vienādi leņki $\angle C P Q$ un $\angle C D Q$ balstās uz $C Q$. Tātad $\angle P D C=\angle P Q C$, jo abi ir ievilkti leņki, kas balstās uz hordas $P C$. Paralelograma $P B C Q$ pretējie leñki ir vienādi: $\angle P B C=\angle P Q C$. Tātad $\angle P B C=\angle P D C$.

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-10.jpg?height=398&width=738&top_left_y=1052&top_left_x=662)

A14. att.

12.3. Pierādīt, ka jebkuram naturālam nepāra skaitlim $n$ izteiksme $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalās ar 2015.

## Atrisinājums

1. risinājums. Ievērojam, ka $2015=5 \cdot 13 \cdot 31$. Tā kā visi pirmreizinātāji ir dažādi, nepieciešams pierādīt, ka dotā izteiksme vienlaikus dalās gan ar 5 , gan ar 13, gan 31 .

Izmantosim teorēmu: ja veseli skaitli $A$ un $B$, dalot ar $n$, dod attiecīgi atlikumus $a$ un $b$, tad dalot ar $n$ skaitḷus $A+B, A-B, A \cdot B$ rodas tādi paši atlikumi, kādus dod $a+b, a-b, a \cdot b$ dalot ar $n$.

Apskatām dotās izteiksmes dalāmību ar katru pirmreizinātāju.

- Atlikums, kāds rodas, izteiksmi $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalot ar 5 , ir $4^{n}+1^{n}+4^{n}-4^{n}$ jeb $4^{n}+1$. Tā kā $n$ ir nepāra skaitlis, tad $4^{n}+1=4^{2 k+1}+1=4 \cdot 16^{k}+1$. No tā, ka 16 , dalot ar 5 dod atlikumu 1, iegūst, ka $4 \cdot 16^{k}+1$ dalot ar 5 , dod atlikumu $4 \cdot 1^{k}+1=5$ jeb dalās ar 5 . Tātad arī izteiksme $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalās ar 5 .
- Atlikums, kāds rodas, izteiksmi $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalot ar 13 , ir $7^{n}+6^{n}+11^{n}-11^{n}$ jeb $7^{n}+6^{n}=7^{2 k+1}+6^{2 k+1}=7 \cdot 49^{k}+6 \cdot 36^{k}$. No tā, ka 49 un 36 , dalot ar 13, abi dod atlikumu 10, iegūst, ka $7 \cdot 49^{k}+6 \cdot 36^{k}$, dalot ar 13 , dod atlikumu $7 \cdot 10^{k}+6 \cdot 10^{k}=13 \cdot 10^{k}$ jeb dalās ar 13 . Tātad arī izteiksme $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalās ar 13 .
- Atlikums, kāds rodas, izteiksmi $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalot ar 31, ir $6^{n}+12^{n}+25^{n}-12^{n}$ jeb $6^{n}+25^{n}=6^{2 k+1}+25^{2 k+1}=6 \cdot 36^{k}+25 \cdot 625^{k}$. No tā, ka 36 un 625 , dalot ar 31, abi dod atlikumu 5, iegūst, ka $6 \cdot 36^{k}+25 \cdot 625^{k}$, dalot ar 31, dod atlikumu $6 \cdot 5^{k}+25 \cdot 5^{k}=31 \cdot 5^{k}$ jeb dalās ar 31. Tātad arī izteiksme $2269^{n}+2151^{n}+1389^{n}-1779^{n}$ dalās ar 31 .

Līdz ar to esam pierādījuši, ka dotā izteiksme vienlaikus dalās ar 5, 13 un 31, tātad tā dalās ar 2015.

2. risinājums. Ievērojam, ka $2015=5 \cdot 13 \cdot 31$. Tā kā visi pirmreizinātāji ir dažādi, nepieciešams pierādīt, ka dotā izteiksme vienlaikus dalās gan ar 5, gan ar 13, gan 31 .

Apskatām dotās izteiksmes dalāmību ar katru pirmreizinātāju:

- $2269^{n}+2151^{n}+1389^{n}-1779^{n} \equiv 4^{n}+1^{n}+4^{n}-4^{n} \equiv 4^{n}+1^{n} \equiv(-1)^{2 k+1}+1 \equiv-1+1 \equiv 0(\bmod 5) ;$
- $2269^{n}+2151^{n}+1389^{n}-1779^{n} \equiv 7^{n}+6^{n}+11^{n}-11^{n} \equiv 7^{n}+6^{n} \equiv(-6)^{2 k+1}+6^{2 k+1} \equiv 0(\bmod 13) ;$
- $2269^{n}+2151^{n}+1389^{n}-1779^{n} \equiv 6^{n}+12^{n}+25^{n}-12^{n} \equiv 6^{n}+25^{n} \equiv 6^{2 k+1}+(-6)^{2 k+1} \equiv 0(\bmod 31)$

Līdz ar to esam pierādījuši, ka dotā izteiksme vienlaikus dalās ar 5, 13 un 31, tātad tā dalās ar 2015.

12.4. Katrs no skaitḷu ass punktiem ar veselu koordinātu ir nokrāsots vai nu baltā, vai melnā krāsā. Nekādi divi balti punkti neatrodas viens no otra attālumā 1 un nekādi divi melni punkti neatrodas viens no otra attālumā $d$. Noteikt, kādām naturālām $d$ vērtībām šāds krāsojums ir iespējams!

## Atrisinājums

Šāds krāsojums iespējams tikai tad, ja $d$ - nepāra skaitlis. Tad der krāsojums, kur punkti nokrāsoti pamīšus baltā un melnā krāsā (skat. A15. att.).

![](https://cdn.mathpix.com/cropped/2024_07_28_2bb86a39358def63a951g-11.jpg?height=55&width=807&top_left_y=932&top_left_x=673)

A15. att.

Skaidrs, ka divi baltie punkti nevar atrasties blakus. Ja divi melnie punkti atrodas blakus (piemēram, pozīcijās 1 un 2), tad $d$ vienības tālāk (pozīcijās $d+1$ un $d+2$ ) atrodas divi baltie punkti, kas nav iespējams pēc uzdevuma nosacījumiem. Tātad punktiem jābūt izkrāsotiem pamīšus. Redzams, ka pamīšus izvietojot punktus, uzdevuma nosacījumi tiek apmierināti, ja $d$ ir nepāra skaitlis, bet, ja $d$ ir pāra skaitlis, tad ne.

12.5. Votivapu valodā visi vārdi sastāv tikai no diviem burtiem $a$ un $b$. Jebkuru vārdu var iegūt no vārda " $a$ ", atkārtoti lietojot šādus trīs likumus:

1) pierakstot vārdam galā burtu $b$;
2) pierakstot vārdam galā sevi pašu;
3) aizstājot vārdā trīs pēc kārtas esošus burtus $a$ ar vienu burtu $b$.
4) 

Vai votivapu valodā ir vārdi a) abbababab; b) baabaabaa?

## Atrisinājums

a) Vārdu “abbababab" var iegūt šādi:

```
    2) 2) 2) 2) 3) 3)
$a \rightarrow a a \rightarrow a a a a \rightarrow a a a a a a a a \rightarrow a a a a a a a a \llbracket a a a a a \rightarrow a b a a a a a a a \approx a a a \rightarrow$
3) 3) 3) 1)
$\rightarrow a b b a a a a a a \llbracket a \rightarrow a b b a b a a a a a \rightarrow a b b a b a b a \mapsto a b b a b a b a b$
```

b) Vārdu "baabaabaa" nevar iegūt. Burtu $a$ aizstājam ar ciparu 1, bet burtu $b$ - ar ciparu 3. Tad visi vārdi votivapu valodā tiek aizstāti ar naturāliem skaitliem, kuru pierakstā izmantoti tikai cipari 1 un 3.

Ievērojam, ka sākotnējais vārds " $a$ " jeb skaitlis 1 nedalās ar 3 .

Pierādīsim, ja kāds skaitlis nedalās ar 3, tad skaitlis, kas no tā tiek iegūts ar uzdevumā dotajām darbībām, arī nedalās ar 3 :

1) ja skaitlis nedalās ar 3, tad, pierakstot tam galā 3 , arī iegūtais skaitlis nedalās ar 3 , jo ciparu summas atlikums, dalot ar 3 , nemainās;
2) ja skaitḷa ciparu summa, dalot ar 3, dod atlikumu 1, tad iegūtā skaitḷa ciparu summa, dalot ar 3, dod atlikumu 2; ja skaitḷa ciparu summa, dalot ar 3, dod atlikumu 2, tad iegūtā skaitḷa ciparu summa, dalot ar 3, dod atlikumu 1; abos gadījumos iegūtais skaitlis nedalās ar 3;
3) skaitḷa ciparu summa nemainās, aizstājot 111 ar 3, tātad iegūtais skaitlis nedalās ar 3 .

Aizstājot vārda "baabaabaa" burtus ar cipariem, iegūst skaitli 311311311, kas dalās ar 3, jo tā ciparu summa ir 15. Tātad, vairākkārt izmantojot dotos likumus, šo vārdu nav iespējams iegūt.

