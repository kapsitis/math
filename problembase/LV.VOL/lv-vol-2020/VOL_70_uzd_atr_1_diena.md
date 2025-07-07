NACIONĀLAIS
ATTISSTÏBAS
PLĀNS 2020

# Latvijas 70. matemātikas olimpiādes 3. posma uzdevumi un atrisinājumi 9.-12. klase 

9.1. Kādām naturālām $n$ vērtībām izteiksmes $\frac{(3 n-1)(n+4)}{n+2}$ vērtība ir vesels skaitlis?

Atrisinājums. Ekvivalenti pārveidojam doto izteiksmi:

$$
\frac{(3 n-1)(n+4)}{n+2}=\frac{3 n^{2}+11 n-4}{n+2}=\frac{3 n(n+2)+5 n-4}{n+2}=\frac{3 n(n+2)}{n+2}+\frac{5(n+2)-14}{n+2}=3 n+5-\frac{14}{n+2}
$$

Tā kā $3 n+5$ ir naturāls skaitlis, tad dotās izteiksmes vērtība būs vesels skaitlis tikai tad, ja $\frac{-14}{n+2}$ ir vesels skaitlis, bet tas iespējams, ja $(n+2)$ ir skaitla 14 dalītājs. levērojot, ka $n$ ir naturāls, iegūstam, ka $n+2=7$ vai $n+2=14$, no kā iegūstam, ka $n=5$ vai $n=12$.

9.2. Atrast visus naturālos skait|us $B$ intervālā $1<B<99$, kuriem izpildās šāda īpašība: jebkuram naturālam skaitlim $C$, kuram $B<C<100$ ir spēkā $B \leq V \leq C$, kur $V=\frac{1+B+C+100}{4}$ ir skait!u $1, B, C, 100$ vidējais aritmētiskais.

Atrisinājums. Pēc dotā $1<B<C<100$. Tā kā $B<C$, tad var pieṇemt, ka $C=B+x$, kur $1 \leq x \leq 99-B$. Līdz ar to iegūstam, ka četru doto skait|u vidējais aritmētiskais ir

$$
V=\frac{1+B+B+x+100}{4}=\frac{2 B+x+101}{4}
$$

Nemot vērā, ka jāizpildās nevienādībām $B \leq V \leq C$, iegūstam

$$
\begin{gathered}
B \leq \frac{2 B+x+101}{4} \leq B+x \\
4 B \leq 2 B+x+101 \leq 4 B+4 x
\end{gathered}
$$

Pārrakstot iegūto divkāršo nevienādību kā nevienādību sistēmu, iegūstam

$$
\left\{\begin{array} { l } 
{ 4 B \leq 2 B + x + 1 0 1 } \\
{ 2 B + x + 1 0 1 \leq 4 B + 4 x }
\end{array} \quad \text { jeb } \quad \left\{\begin{array}{l}
2 B \leq 101+x \\
2 B \geq 101-3 x
\end{array}\right.\right.
$$

Ievērojam, ja nevienādība izpildās pie $x=1$, tad tā izpildās arī pie lielākiem $x$. Tāpēc tas, ka šī nevienādība izpildās visiem $x \geq 1$ ir ekvivalents apgalvojumam, ka tā izpildās pie $x=1$. Tātad

$$
\left\{\begin{array} { l } 
{ 2 B \leq 1 0 2 } \\
{ 2 B \geq 9 8 }
\end{array} \text { jeb } \quad \left\{\begin{array}{l}
B \leq 51 \\
B \geq 49
\end{array}\right.\right.
$$

Līdz ar to esam ieguvuši, ka jebkurai derīgai $C$ vērtībai ir spēkā sakarība $B \leq V \leq C$, ja $B$ ir 49, 50 vai 51 .

9.3. Punkts $R$ atrodas uz stara $O B$ un punkti $P$ un $Q$ atrodas uz stara $O A$ tā, ka $O P<O Q$ un $\Varangle O R P=\Varangle B R Q$. Leṇka $R P A$ bisektrise krusto staru $O B$ punktā $T$. Pierādīt, ka $Q T$ ir $\Varangle R Q A$ bisektrise!

Atrisinājums. Pagarinām nogriezni $P R$, tad $\Varangle O R P=\Varangle N R B$ kā krustleṇki (skat. 1. att.) un līdz ar to arī $B R Q=\Varangle N R B$. Izmantojot bisektrises īpašību, iegūstam, ka punkts $T$ atrodas vienādā attālumā no

- leṇk.a $N R Q$ malām $N R$ un $R Q$, tas ir, $T C=T D$;
- leṇka $Q P R$ malām $P R$ un $P Q$, tas ir, $T C=T E$.

Tātad $T D=T E$ un esam ieguvuši, ka punkts $T$ atrodas vienādā attālumā no leṇka $R Q A$ malām. Līdz ar to pēc bisektrises pazīmes esam ieguvuši, ka punkts $T$ atrodas uz $\Varangle R Q A$ bisektrises jeb $Q T$ ir $\Varangle R Q A$ bisektrise.

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-02.jpg?height=555&width=713&top_left_y=105&top_left_x=706)

9.4. Vai eksistē tādi četri dažādi a) naturāli skaiți, b) pirmskaitḷi $a, b, c, d$, ka vienlaicīgi izpildās šādi nosacījumi:

○ $b+c+d$ dalās ar $a$,

- $c+d+a$ dalās ar $b$,
- $d+a+b$ dalās ar $c$,
- $a+b+c$ dalās ar $d$ ?

Atrisinājums. a) Jā, eksistē. Skaitliem 1, 2, 3, 6 izpildās visi uzdevuma nosacijumi:

- $2+3+6$ dalās ar 1 ,
- $1+3+6$ dalās ar 2 ,
- $1+2+6$ dalās ar 3 ,
- $1+2+3$ dalās ar 6 .

b) Nē, neeksistē. levērojam, ka

- $a+(b+c+d)$ dalās ar $a$ (jo abi saskaitāmie dalās ar $a$ ),
- $b+(c+d+a)$ dalās ar $b$,
- $c+(d+a+b)$ dalās ar $c$,

○ $d+(a+b+c)$ dalās ar $d$.

Tā kā $a, b, c, d$ ir pirmskaitḷi, tad $a+b+c+d$ dalās ar $a b c d$, no kā izriet, ka $a+b+c+d \geq a b c d$. Nezaudējot vispārīgumu varam pienemt, ka $a \leq b \leq c \leq d$. Tādā gadījumā $a+b+c+d \leq 4 d<a b c d$, jo pat trīs mazāko atškirīgo pirmskaitlu reizinājums $2 \cdot 3 \cdot 5>4$. Esam ieguvuši pretrunu, tātad neeksistē tādi četri dažādi pirmskaitli, kuriem izpildās visi uzdevuma nosacijumi.

9.5. Vai kubu ar izmēriem $12 \times 12 \times 12$ iespējams salikt no kieǵeliem, kuru izmēri ir $1 \times 1 \times 8$ ?

Atrisinājums. Pamatosim, ka prasīto nevar izdarīt. Sadalām kubu 9 mazākos kubos, kuru izmēri ir $4 \times 4 \times 4$, un iekrāsojam tos kā šaha galdinuu (skat. 2. att.). Pavisam ir $64 \cdot 14=896$ melni un $64 \cdot 13=832$ balti kubiṇi ar izmēriem $1 \times 1 \times 1$. Tā kā katrs kieǵelis pārklāj 4 melnus un 4 baltus kubinuus ar izmēriem $1 \times 1 \times 1$ (skat. 3. att.), tad, ja no šiem kiegeliem būtu salikts kubs, tas saturētu vienāda skaita melnos un baltos kubinus ar izmēriem $1 \times 1 \times 1$, bet $896 \neq 832$.

2. att.
3. att.

10.1. Pierādīt, ka skaitlim $2019^{3}+2020^{3}+2021^{3}$ ir vismaz 20 dažādi pozitīvi dalītāji!

Atrisinājums. Apzīmējam $n=2020$ un pārveidojam doto skaitli:

$$
\begin{aligned}
(n-1)^{3} & +n^{3}+(n+1)^{3}=n^{3}-3 \cdot n^{2}+3 \cdot n-1+n^{3}+n^{3}+3 \cdot n^{2}+3 \cdot n+1= \\
& =n \cdot\left(3 n^{2}+6\right)=n \cdot 3 \cdot\left(n^{2}+2\right)=2^{2} \cdot 5 \cdot 101 \cdot 3 \cdot\left(2020^{2}+2\right)
\end{aligned}
$$

Tā kā naturālam skaitlim $x=p_{1}^{k_{1}} \cdot p_{2}^{k_{2}} \cdot \ldots \cdot p_{m}^{k_{m}}$, kur $p_{i}$ ir dažādi pirmskaitli, pavisam ir $\left(k_{1}+1\right)\left(k_{2}+1\right) \ldots\left(k_{m}+1\right)$ dažādi naturālie dalītāji, tad dotajam skaitlim ir vismaz $(2+1)(1+1)(1+1)(1+1)=24$ dažādi dalītāji, pat neṇemot vērā reizinātāju $2020^{2}+2$. Patiesībā dotajam skaitlim ir 640 dažādi dalītāji.

10.2. Zināms, ka $x^{2}+y^{2}+x y=3$. Kāda var būt $x+y$ vērtība?

1. atrisinājums. Pamatosim, ka $x^{2}+y^{2}+x y \geq \frac{3}{4}(x+y)^{2}$. Veicam ekvivalentus pārveidojumus:

$$
\begin{gathered}
x^{2}+y^{2}+x y \geq \frac{3}{4} x^{2}+\frac{3}{2} x y+\frac{3}{4} y^{2} \\
\frac{1}{4} x^{2}+\frac{1}{4} y^{2}-\frac{1}{2} x y \geq 0 \\
x^{2}+y^{2}-2 x y \geq 0 \\
(x-y)^{2} \geq 0 .
\end{gathered}
$$

Tā kā iegūta patiesa nevienādība, tad arī dotā nevienādība ir patiesa. Līdz ar to esam ieguvuši, ka $3 \geq \frac{3}{4}(x+y)^{2}$ jeb $4 \geq(x+y)^{2}$, tātad $-2 \leq x+y \leq 2$.

Vēl jāparāda, ka visām vērtībām šajā intervālā ir atbilstošas $x$ un $y$ vērtības. Apzīmējam $x+y=t(-2 \leq t \leq 2)$. No dotās vienādības iegūstam

$$
x^{2}+2 x y+y^{2}-x y=3 \quad \Rightarrow \quad x y=(x+y)^{2}-3 \quad \Rightarrow \quad x y=t^{2}-3
$$

Sastādām kvadrātvienādojumu $a^{2}-t a+t^{2}-3=0$, kura sakṇu summa ir $a_{1}+a_{2}=t$ un sakṇu reizinājums ir $a_{1} a_{2}=t^{2}-3$. Ja šim vienādojumam ir atrisinājums dotai $t$ vērtībai, tad tā saknes ir meklētās $x$ un $y$ vērtības. Aprēkinām diskriminantu $D=(-t)^{2}-4 \cdot 1 \cdot\left(t^{2}-3\right)=12-3 t^{2}$, tā kā $-2 \leq t \leq 2$, tad $t^{2} \leq 4$, tātad visām pielaujamajām $t$ vērtībām $D \geq 0$. Tātad $-2 \leq x+y \leq 2$.

2. atrisinājums. Apzīmējam $x=u+v$ un $y=u-v$. levietojot apzīmējumus dotajā vienādībā, jegūstam

$$
\begin{gathered}
(u+v)^{2}+(u-v)^{2}+(u+v)(u-v)=3 \\
u^{2}+2 u v+v^{2}+u^{2}-2 u v+v^{2}+u^{2}-v^{2}=3 \\
3 u^{2}+v^{2}=3
\end{gathered}
$$

Lai pēdējā vienādība būtu patiesa, tad $-1 \leq u \leq 1$. Tā kā $x+y=(u+v)+(u-v)=2 u$, tad $-2 \leq x+y \leq 2$.

10.3. Taisnlenka trijstūrī $A B C$, kurā $\Varangle A B C=90^{\circ}$, novilkts augstums $B D$, nogriežṇa $B D$ viduspunkts ir $E$. Punkti $F$ un $G$ ir attiecīgi nogriežṇu $A D$ un $C D$ viduspunkti. Pierādīt, ka $\Varangle A E C+\Varangle F B G=180^{\circ}$.

Atrisinājums. levērojam, ka $\triangle A B D \sim \triangle B D C$ pēc pazīmes $\ell \ell$, jo $\Varangle A D B=\Varangle B D C=90^{\circ}$ un $\Varangle B A D=90^{\circ}-\Varangle A B D=\Varangle D B C$ (skat. 4. att.). Tātad trijstūru malas ir proporcionālas, tas ir, $\frac{B D}{C D}=\frac{A D}{B D}$. Tā kā

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-03.jpg?height=80&width=1830&top_left_y=2009&top_left_x=169)
$\Varangle F B D=\Varangle D C E=90^{\circ}-\Varangle D E C$ jeb $\Varangle F B D+\Varangle D E C=90^{\circ}$.

Līdzīgi pierāda, ka $\Varangle G B D+\Varangle A E D=90^{\circ}$.

Tātad $\Varangle A E C+\Varangle F B G=(\Varangle A E D+\Varangle D E C)+(\Varangle F B D+\Varangle G B D)=90^{\circ}+90^{\circ}=180^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-03.jpg?height=285&width=527&top_left_y=2221&top_left_x=823)

4. att.

10.4. Aplūkojam skaitlu virkni $7 ; 737 ; 73737 ; 7373737 ; \ldots$, kuras pirmais loceklis ir 7 un katru nākamo iegūst, iepriekšējam pierakstot galā 37. Pierādīt, ka neviens šīs virknes loceklis nedalās ar 17.

Atrisinājums. Apzīmējam virknes loceklus ar $s_{0}=7, s_{1}=737, s_{2}=73737, \ldots$

Redzams, ka virknē ir spēkā sakarība $s_{k+1}=100 s_{k}+37$. Patiešām, skaitli pareizinot ar 100 tam tiek galā pierakstītas divas nulles, bet pieskaitot 37 šīs nulles pārvēršas par 37, tātad šī operācija pieraksta skaitla galā 37. Apzīmēsim ar $a_{k}$ atlikumu virkni, kas rodas $s_{k}$ dalot ar 17, $a_{k}=s_{k}$ mod 17. Mums jāpierāda, ka virknē ( $a_{k}$ ) nav nevienas nulles.

Arī virknes $a_{k}$ katrs loceklis (tāpat kā virknei $s_{k}$ ) ir atkarīgs tikai no iepriekšējā

$$
a_{k+1}=s_{k+1} \bmod 17=100 s_{k}+37 \bmod 17=15 a_{k}+3 \bmod 17
$$

Izmantojot šo formulu un to, ka $a_{0}=7 \bmod 17=7$, aprēkināsim virknes $a_{k}$ pirmos loceklus.

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $a_{k}(\bmod 17)$ | 7 | 6 | 8 | 4 | 12 | 13 | 11 | 15 | 7 |

Esam ieguvušì, ka $a_{0}=a_{8}=7$. Tā kā šajā virknē katrs loceklis ir atkarīgs tikai no iepriekšējā, tad šī virkne būs periodiska ar periodu 8: no tā, ka $a_{0}=a_{8}$, secinām, ka $a_{1}=a_{9}$, tad $a_{2}=a_{10}$ utt.

Tā kā starp pirmajiem 8 locekliem šajā virknē nav nevienas nulles, tad, tā kā tā ir periodiska, tad arī tālāk tajā nebūs nevienas nulles.

10.5. Dotas četras pēc ārējā izskata vienādas monētas, katras monētas masa ir 20 g vai 21 g . Kā noteikt katras monētas masu ar trīs svēršanām uz elektroniskajiem svariem, kas rāda uz svariem uzlikto monētu kopējo masu?

Atrisinājums. Apzīmējam monētas ar $A, B, C, D$. Pirmajā svēršanā uz svariem liekam $A$ un $B$.

- Ja $A+B=40$ vai $A+B=42$, tad $A$ un $B$ masas jau zināmas, tās attiecīgi ir 20 g un 20 g vai 21 g un 21 g . Pēc tam ar divām svēřǎanām atrodam $C$ un $D$ masu.
- Ja $A+B=41$, tad otrajā svēršanā uz svariem liekam $A$ un $C$.
- Ja $A+C=40$ un $A+C=42$, tad zinām $A$ un $C$ masu, tātad arī $B$ masu. Trešajā svēršanā uz svariem liekam $D$ un nosakām tās masu.
- Ja $A+C=41$, tad no tā, ka $A+B=A+C$, secinām, ka $B=C$. Trešajā reizē uz svariem liekam $B, C$ un D. levērojam, ka $B+C$ ir pāra skaitlis (40 vai 42). Apskatot visus iespējamos svēršanas iznākumus, iegūstam katras monētas masu, skat. 5. att.

| $\boldsymbol{B}+\boldsymbol{C}$ | $\boldsymbol{B}+\boldsymbol{C}+\boldsymbol{D}$ | $\boldsymbol{D}$ | $\boldsymbol{B}$ | $\boldsymbol{C}$ | $\boldsymbol{A}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 40 | 60 | 20 | 20 | 20 | 21 |
| 40 | 61 | 21 | 20 | 20 | 21 |
| 42 | 62 | 20 | 21 | 21 | 20 |
| 42 | 63 | 21 | 21 | 21 | 20 |
| 5. att. |  |  |  |  |  |

11.1. Dota funkcija $f(x)=m x^{2}+(m-1) x+\frac{2020}{m-2019}$. Ar kādām parametra $m$ vērtībām funkcija ir augoša intervālā $(1 ; 2)$ ?

1. atrisinājums. levērojam, ka $m \neq$ 2019. Lai funkcija būtu augoša, jāizpildās nevienādībai $f(1)<f(2)$. Atrisinām šo nevienādību:

$$
\begin{aligned}
m+(m-1)+\frac{2020}{m-2019} & <4 m+(m-1) \cdot 2+\frac{2020}{m-2019} \\
2 m-1 & <6 m-2 \\
m & >\frac{1}{4}
\end{aligned}
$$

Vēl jāgarantē, ka parabolas virsotne neatrodas intervālā $(1 ; 2)$. Tā kā $m$ vērtības ir pozitīvas, tad parabolas zari ir vērsti uz augšu un, lai dotajā intervālā funkcija būtu augoša, jāizpildās nevienādībai $x_{v} \leq 1$ jeb $\frac{1-m}{2 m} \leq 1$. Reizinot nevienādību ar $2 m>0$, iegūstam $1-m \leq 2 m$ jeb $m \geq \frac{1}{3}$. Līdz ar to funkcija ir augoša intervālā $(1 ; 2)$, ja $m \in\left[\frac{1}{3} ; 2019\right) \cup$ $\cup(2019 ;+\infty)$.

2. atrisinājums. levērojam, ka $m \neq 2019$. Ja $m<0$, tad parabolas virsotnes abscisa $\frac{1-m}{2 m}<0$, kas nozīmē, ka funkcija nav augoša dotajā intervālā. Ja $m=0$, tad iegūstam $f(x)=-x-\frac{2020}{2019}$ un tā ir dilstoša funkcija. Ja $m>0$, tad parabolas zari ir vērsti uz augšu un, lai dotajā intervālā funkcija būtu augoša, jāizpildās nevienādībai $\frac{1-m}{2 m} \leq 1$. Reizinot nevienādību ar $2 m>0$, iegūstam $1-m \leq 2 m$ jeb $m \geq \frac{1}{3}$. Līdz ar to funkcija ir augoša intervālā $(1 ; 2)$, ja $m \in\left[\frac{1}{3} ; 2019\right) \cup(2019 ;+\infty)$.

11.2. Aplūkojam virkni $1 ; 2 ; 2 ; 3 ; 3 ; 3 ; 4 ; 4 ; 4 ; 4 ; 5 ; 5 ; 5 ; 5 ; 5 ; 6 ; 6 ; 6 ; 6 ; 6 ; 6 ; \ldots$, kurā katrs naturālais skaitlis $k$ tiek atkārtots $k$ reizes. Pierādīt, ka šīs virknes $n$-to locekli var aprēkināt pēc formulas $\left[\sqrt{2 n}+\frac{1}{2}\right]$.

$\operatorname{Ar}[x]$ apzīmējam skaitḷa veselo daḷu, tas ir, lielāko veselo skaitli, kas nepārsniedz $x$. Piemēram, $[3,1]=3,[17]=17$, $[6,99]=6$.

Atrisinājums. Katrs naturāls skaitlis $k$ dotajā virknē atkārtojas $k$ reizes, noskaidrosim, ar kādiem indeksiem (kurās pozīcijās) tas tajā parādās.

Pirms pirmā skaitla $k$ ir viens vieninieks, divi divnieki, trīs trijnieki, ..., $(k-1)$ skaitlis $(k-1)$, tātad kopā

$$
1+2+\ldots+(k-1)=\frac{k^{2}-k}{2}
$$

skaitli. Tātad skaitlim $k$ indeksi šajā virnē būs

$$
\frac{k^{2}-k}{2}+1 ; \frac{k^{2}-k}{2}+2 ; \ldots ; \frac{k^{2}-k}{2}+k
$$

jeb, citiem vārdiem sakot, jebkurš skaitlis $k$ šajā virknē parādās ar indeksu $\frac{k^{2}-k}{2}+i$, kur $1 \leq i \leq k$. Lai pierādītu formulu, jāpierāda, ka visiem naturāliem $k$ un visiem naturāliem $1 \leq i \leq k$ izpildās

$$
\left[\sqrt{2\left(\frac{k^{2}-k}{2}+i\right)}+\frac{1}{2}\right]=k \quad \text { jeb } \quad\left[\sqrt{k^{2}-k+2 i}+\frac{1}{2}\right]=k
$$

Vienādība $[x]=y$, kur $y$ ir naturāls skaitlis izpildās tad un tikai tad, ja $y \leq x<y+1$, tāpēc vienādība pārvēršas par divkāršo nevienādību

$$
k \leq \sqrt{k^{2}-k+2 i}+\frac{1}{2}<k+1
$$

Atṇemot $\frac{1}{2}$ un kāpinot kvadrātā, iegūstam

$$
\begin{gathered}
\left(k-\frac{1}{2}\right)^{2} \leq k^{2}-k+2 i<\left(k+\frac{1}{2}\right)^{2} \\
\frac{1}{4} \leq 2 i<2 k+\frac{1}{4}
\end{gathered}
$$

Redzams, ka pēdējā nevienādība ir patiesa visiem $1 \leq i \leq k$. Tā kā visi pārveidojumi bija ekvivalenti (kvadrātā tika kāpinātas pozitīvas izteiksmes), tad sākotnējā izteiksme arī ir spēkā.

11.3. Četrstūris $A B C D$ ievilkts riṇka līnijā. Pierādīt, ka trijstūros $A B C, B C D, C D A, D A B$ ievilkto riṇka līniju centri ir taisnstūra virsotnes!

Atrisinājums. Ja $X$ un $Y$ ir attiecīgi $\triangle A B D$ un $\triangle A B C$ ievilkto rinka līniju centri (skat. 6. att.), tad $A Y$ un $B Y$ ir attiecīgi $\Varangle B A C$ un $\Varangle A B C$ bisektrises. Tātad

$$
\begin{gathered}
\Varangle A Y B=180^{\circ}-(\Varangle B A Y+\Varangle A B Y)=180^{\circ}-\frac{1}{2}(\Varangle B A C+\Varangle A B C)= \\
=\Varangle B A C+\Varangle A B C+\Varangle A C B-\frac{1}{2}(\Varangle B A C+\Varangle A B C)= \\
=\frac{1}{2}(\Varangle B A C+\Varangle A B C+\Varangle A C B)+\frac{1}{2} \Varangle A C B=90^{\circ}+\frac{1}{2} \Varangle A C B .
\end{gathered}
$$

Līdzīgi $\Varangle A X B=90^{\circ}+\frac{1}{2} \Varangle A D B$.

Tā kā $\Varangle A C B=\Varangle A D B$ kā ievilktie lenki, kas balstās uz vienu un to pašu loku, tad $\Varangle A Y B=\Varangle A X B$. Tātad punkti $A, X, Y, B$ atrodas uz vienas rinka līnijas. Līdz ar to $\Varangle X Y B=180^{\circ}-\Varangle X A B=180^{\circ}-\frac{1}{2} \Varangle D A B$.

Ja $Z$ ir $\triangle B C D$ ievilktās riṇka līnijas centrs, tad līdzīgi iegūstam, ka $\Varangle Z Y B=180^{\circ}-\frac{1}{2} \Varangle D C B$.

Izmantojot šīs divas vienādības, iegūstam

$$
\begin{gathered}
\Varangle X Y Z=360^{\circ}-\Varangle X Y B-\Varangle Z Y B=360^{\circ}-\left(180^{\circ}-\frac{1}{2} \Varangle D A B\right)-\left(180^{\circ}-\frac{1}{2} \Varangle D C B\right)= \\
=\frac{1}{2}(\Varangle D A B+\Varangle D C B)=\frac{1}{2} \cdot 180^{\circ}=90^{\circ} .
\end{gathered}
$$

Līdzīgi pierāda, ka arī pārējie četrstūra leṇki ir taisni, tātad tas ir taisnstūris.

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-06.jpg?height=454&width=462&top_left_y=586&top_left_x=823)

6. att.

11.4. Zināms, ka trīsciparu skaitlis $\overline{a b c}$ ir pirmskaitlis un ka vienādojumam $a x^{2}+b x+c=0$ ir divas reālas saknes. Vai var gadīties, ka šīs saknes ir a) veseli skaitli, b) racionāli skaitlii?

Atrisinājums. a) Nē, saknes nevar būt veseli skaitḷi. levērojam, ka $c \neq 0$, jo pretējā gadījumā $\overline{a b c}$ nav pirmskaitlis. Tas nozīmē, ka 0 nav vienādojuma sakne. Ja $x \geq 0$, tad $a x^{2}+b x+c \geq c>0$. Tātad vienādojumam var būt tikai negatīvas saknes. Apzīmējot saknes ar $-x_{1},-x_{2}$ un sadalot kreisās puses izteiksmi reizinātājos, iegūstam

$$
a x^{2}+b x+c=a\left(x+x_{1}\right)\left(x+x_{2}\right)
$$

Pieṇemsim, ka šīs saknes ir veseli skaitḷi. Ja $x=10$, tad iegūstam

$$
a\left(10+x_{1}\right)\left(10+x_{2}\right)=100 a+10 b+c=\overline{a b c}
$$

Tātad esam ieguvuši, ka $\overline{a b c}$ ir salikts skaitlis, kas ir pretrunā ar doto. Līdz ar to vienādojumam nav veselu sakṇu.

b) Nē, saknes nevar būt racionāli skaitḷi. Pienemsim pretējo, ka saknes vienādojumam ir racionālas, tas ir, $-\frac{p_{1}}{q_{1}}$ un $-\frac{p_{2}}{q_{2}}$, kur $p_{1}, q_{1}$ ir savstarpēji pirmskaitli un arī $p_{2}, q_{2}$ ir savstarpēji pirmskaitli. Sadalām vienādojuma kreiso pusi reizinātājos:

$$
a x^{2}+b x+c=a\left(x+\frac{p_{1}}{q_{1}}\right)\left(x+\frac{p_{2}}{q_{2}}\right)=\frac{a}{q_{1} q_{2}}\left(q_{1} x+p_{1}\right)\left(q_{2} x+p_{2}\right)
$$

Ievietojot $x=10$, iegūstam

$$
\begin{gathered}
\frac{a}{q_{1} q_{2}}\left(10 q_{1}+p_{1}\right)\left(10 q_{2}+p_{2}\right)=100 a+10\left(\frac{p_{1}}{q_{1}}+\frac{p_{2}}{q_{2}}\right)+\frac{p_{1} p_{2}}{q_{1} q_{2}}=100 a+10 b+c=\overline{a b c} \\
a\left(10 q_{1}+p_{1}\right)\left(10 q_{2}+p_{2}\right)=\overline{a b c} \cdot q_{1} q_{2}
\end{gathered}
$$

Pamatosim, ja kvadrātvienādojuma $a x^{2}+b x+c=0$ sakne ir $\frac{p}{q}$ (nesaīsināma daḷa), tad $a$ dalās ar $q$. levietojam vienādojumā $a x^{2}+b x+c=0$ tā sakni $x=\frac{p}{q}$ un pārveidojam iegūto identitāti:

$$
\begin{gathered}
a\left(\frac{p}{q}\right)^{2}+b\left(\frac{p}{q}\right)+c=0 \\
a p^{2}+b p q+c q^{2}=0 \\
q(c q+b p)=-a p^{2}
\end{gathered}
$$

Tā kā pēdējās vienādības kreisā puse dalās ar $q$, tad arī labās puses izteiksmei jādalās ar $q$. Nemot vērā, ka pēc pieṇēmuma $p$ un $q$ ir savstarpēji pirmskaitli, secinām, ka $a$ ir jādalās ar $q$.

Līdz ar to secinām, ka $q_{i}$ ir viencipara skaitlis, jo $a$ ir cipars.

Analogi iegūst, ka $c$ dalās ar $p_{i}$. Tas nozīmē, ka $10 q_{i}+p_{i}$ ir divciparu skaitlis.

Tātad vienādība $q_{1} q_{2} \cdot \overline{a b c}=a\left(10 q_{1}+p_{1}\right)\left(10 q_{2}+p_{2}\right)$ nevar pastāvēt, jo kreisajā pusē ir reizinātājs $\overline{a b c}$ (trīsciparu pirmskaitlis), bet labajā pusē $a$ ir viencipara skaitlis un pārējie reizinātāji - divciparu. Līdz ar to dotā vienādojuma saknes nav racionāli skaitli.

11.5. Atrast lielāko naturālo skaitli $N$, kuram ir spēkā īpašība: lai kuras $N$ rūtinas būtu aizkrāsotas $4 \times 4$ rūtinu tabulā, vienmēr varēs izvēlēties divas rindas un divas kolonnas tā, ka katra aizkrāsotā rūtina atrodas vai nu izvēlētajā rindā, vai izvēlētajā kolonnā (vai abās).

Atrisinājums. Lielākā $N$ vērtība ir 6. Pamatosim, ja iekrāsotas 6 rūtinas, tad jebkuram krāsojumam izpildās uzdevuma nosacījumi. Ja kādā rindā ir vairāk nekā divas iekrāsotas rūtinas, tad izvēlamies šo rindu un vēl kādu rindu, kurā ir kāda iekrāsota rūtina. Tātad izvēlētajās divās rindās jau ir vismaz četras iekrāsotas rūtinas. Tā kā ir palikušas divas iekrāsotas rūtinas, tad pietiek izvēlēties divas kolonnas, lai iekrāsotās rūtiṇas atrastos šajās kolonnās.

Ja nevienā rindā nav vairāk kā divas iekrāsotas rūtiṇas, tad pēc Dirihlē principa divas iekrāsotas rūtinas ir vismaz divās rindās. Izvēlamies šīs divas (vai divas no trim, ja trīs rindās ir pa divām iekrāsotām rūtiṇām) rindas. Tad izvēlētajās divās rindās jau ir tieši četras iekrāsotas rūtinas. Tā kā ir palikušas divas iekrāsotas rūtinas, tad pietiek izvēēeties divas kolonnas, lai iekrāsotās rūtiṇas atrastos šajās kolonnās.

Pamatosim, ka lielākām $N$ vētībām īpašība nav spēkā visām tabulām. Ja $N=7$, tad īpašība nav spēkā, piemēram, 7. att. dotajam rūtinuu izvietojumam. levērojam, ka, izvēloties jebkuras divas rindas, paliek trīs kolonnas, kurās atrodas iekrāsotās rūtiṇas.

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-07.jpg?height=237&width=215&top_left_y=1193&top_left_x=955)

7. att.

12.1. G̣eometriskās progresijas pirmais, desmitais un 2020 -ais loceklis ir naturāls skaitlis. Vai noteikti arī tās 2019 -ais loceklis ir naturāls skaitlis?

Atrisinājums. Nē, 2019-ais loceklis var nebūt naturāls skaitlis, piemēram, ja $b_{1}=1 \in \mathbb{N}$ un $q=\sqrt[3]{2}$, tad

- $b_{10}=b_{1} \cdot q^{9}=(\sqrt[3]{2})^{9}=2^{3}=8 \in \mathbb{N}$,
- $b_{2020}=b_{1} \cdot q^{2019}=(\sqrt[3]{2})^{2019}=2^{673} \in \mathbb{N}$,
- $b_{2019}=b_{1} \cdot q^{2018}=(\sqrt[3]{2})^{2016} \cdot(\sqrt[3]{2})^{2}=2^{672} \cdot \sqrt[3]{4}$, kas nav naturāls skaitlis.

12.2. Noteikt izteiksmes $(x+y+z)\left(\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\right)$ vislielāko un vismazāko vēttību, ja $1 \leq x, y, z \leq 2020$.

Atrisinājums. Pārveidojam doto izteiksmi un lietojam nevienādību $\frac{a}{b}+\frac{b}{a} \geq 2$ :

$$
(x+y+z)\left(\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\right)=3+\frac{x}{y}+\frac{y}{x}+\frac{x}{z}+\frac{z}{x}+\frac{y}{z}+\frac{z}{y} \geq 3+2+2+2=9
$$

Tātad dotās izteiksmes mazākā vērtība ir 9 un to var iegūt, ja $x=y=z$.

Lai atrastu izteiksmes $F$ maksimālo vērtību, vispirms pierādīsim lemmu.

Lemma. Funkcija $f(x)=x+\frac{k}{x}, k>0$, dilst pa kreisi no tās minimuma punkta $x=\sqrt{k}$ un aug pa labi no tā, tas ir,

$$
0<u<v \leq \sqrt{k} \Rightarrow f(u)>f(v) \text { un } \sqrt{k} \leq u<v \Rightarrow f(u)<f(v)
$$

Pierādīums. Apskatām abus gadijumus.

$$
\begin{aligned}
& f(u)>f(v) \quad \Leftrightarrow \quad \frac{k}{u}-\frac{k}{v}>v-u \Leftrightarrow \frac{k}{u v}>1 \quad \Leftrightarrow \quad k>u v \\
& f(u)<f(v) \Leftrightarrow \frac{k}{u}-\frac{k}{v}<v-u \Leftrightarrow \frac{k}{u v}<1 \quad \Leftrightarrow \quad k<u v
\end{aligned}
$$

Saskaṇā ar Lemmu fiksētiem $y, z \in[1 ; 2020]$, funkcija

$$
F(x)=x\left(\frac{1}{y}+\frac{1}{z}\right)+\frac{1}{x}(y+z)+\frac{y}{z}+\frac{z}{y}+3
$$

maksimālo vērtību sasniedz intervāla galapunktā, tas ir, kad $x=1$ vai $x=2020$. Simetrijas dē las pats attiecas uz gadījumiem, kad fiksējam $x, y$ un $x, z$. Tātad izteiksme $F$ maksimālo vērtību sasniedz tad, kad $x, y, z \in\{1 ; 2020\}$. Apskatām izteiksmes $F$ vērtību, ja $x, y, z \in\{1 ; 2020\}$ :

$$
\begin{aligned}
& \quad x=y=z=1 \text { vai } x=y=z=2020, \operatorname{tad} F(x ; x ; x)=9 \\
& \quad x=y=1 \text { un } z=2020, \operatorname{tad} F(1 ; 1 ; 2020)=2022 \cdot 2 \frac{1}{2020}=\frac{2022 \cdot 4041}{2020} \\
& \quad x=y=2020 \text { un } z=1, \operatorname{tad} F(2020 ; 2020 ; 1)=4041 \cdot 1 \frac{2}{2020}=\frac{4041 \cdot 2022}{2020}
\end{aligned}
$$

Līdz ar to dotās izteiksmes vislielākā vērtība ir $\frac{4041 \cdot 2022}{2020}$.

12.3. Riṇka līnijā $\omega$ ievilkta vienādsānu trapece $A B C D$, punkts $H$ ir garākā pamata $A B$ viduspunkts. Punkts $M$ ir viduspunkts tam lokam $A B$, kas nesatur punktus $C$ un $D$. Taisnes $C D$ un $A M$ krustojas punktā $X$. Zināms, ka nogriežņi $H X, D M$ un $A C$ krustojas vienā punktā $Y$ un $D M=A C$. Pierādīt, ka $A B^{2}=2 C D^{2}$.

Atrisinājums. Pierādīsim, ka $H$ ir rinka līnijas $\omega$ centrs. Tā kā $A C=D M$, tad $\overline{C D A}=\overline{D A M}$ un $\overline{A k M}=\overline{D A M}-\overline{D A}=$ $=\overline{C D A}-\overline{D A}=\overline{C m D}$ (skat. 8. att.). Tā kā uz vienādiem lokiem balstās vienādas hordas, tad $A M=C D$. levērojam, ka $\Varangle M A C=\Varangle C D M$ un $\Varangle A M D=\Varangle D C A$ kā ievilktie leṇki, kas balstās attiecīgi uz viena un tā paša loka. Tad $\triangle A Y M=\triangle D Y C$ pēc pazīmes $\ell m \ell$ un $M Y=Y C$ kā atbilstošās malas. Esam ieguvuši, ka punkts $Y$ atrodas vienādā attālumā no nogriežṇa $M C$ galapunktiem. Trijstūris $M X C$ ir vienādsānu, jo $\Varangle D C M=\Varangle A M C$ kā leṇki, kas balstās uz vienādiem lokiem $D A M$ un $A D C$, tātad punkts $X$ atrodas vienādā attālumā no nogriežṇa $M C$ galapunktiem. Līdz ar to $X Y$ (jeb $X H$ ) ir nogriežṇa $M C$ vidusperpendikuls. levērojam, ka simetrijas dē! $M H$ ir malu $A B$ un $C D$ vidusperpendikuls. Tā kā četrstūris $D A M C$ ir ievilkts četrstūris, tad tam apvilktās rinka līnijas centrs atrodas malu vidusperpendikulu krustpunktā, līdz ar to punkts $H$ ir rinka līnijas $\omega$ centrs.

Tā kā punkts $M$ ir mazākā loka $A B$ viduspunkts, tad $A M=M B$. Trijstūris $A M B$ ir vienādsānu taisnleṇka trijstūris, jo balstās uz diametra $A B$, tad pēc Pitagora teorēmas $A B^{2}=A M^{2}+M B^{2}=C D^{2}+C D^{2}=2 C D^{2}$.

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-08.jpg?height=500&width=638&top_left_y=1555&top_left_x=771)

8. att.

12.4. Zināms, ka četrciparu skaitlis $\overline{a b c d}$ ir pirmskaitlis un ka vienādojumam $a x^{3}+b x^{2}+c x+d=0$ ir trīs reālas saknes. Vai var gadīties, ka visas šīs saknes ir a) veseli skaitli, b) racionāli skaitlli?

Atrisinājums. a) Nē, saknes nevar būt veseli skaitli. levērojam, ka $d \neq 0$, jo pretējā gadījumā $\overline{a b c d}$ nav pirmskaitlis. Tas nozīmē, ka 0 nav vienādojuma sakne. Ja $x \geq 0$, tad $a x^{3}+b x^{2}+c x+d \geq d>0$. Tātad vienādojumam var būt tikai negatīvas saknes. Apzīmējot saknes ar $-x_{1},-x_{2},-x_{3}$ un sadalot kreisās puses izteiksmi reizinātājos, iegūstam

$$
a x^{3}+b x^{2}+c x+d=a\left(x+x_{1}\right)\left(x+x_{2}\right)\left(x+x_{3}\right)
$$

Pieṇemsim, ka vienādojuma saknes ir veseli skaitli. Ja $x=10$, tad iegūstam

$$
a\left(10+x_{1}\right)\left(10+x_{2}\right)\left(10+x_{3}\right)=1000 a+100 b+10 c+d=\overline{a b c d}
$$

Tātad esam ieguvuši, ka $\overline{a b c} d$ ir salikts skaitlis, kas ir pretrunā ar doto. Līdz ar to vienādojumam nav veselu sakṇu.

b) Nē, saknes nevar būt racionāli skaitli. Pieṇemsim, ka saknes vienādojumam ir racionālas, tas ir, $-\frac{p_{1}}{q_{1}},-\frac{p_{2}}{q_{2}}$ un $-\frac{p_{3}}{q_{3}}$, pie kam daḷas ir nesaīsināmas jeb $p_{i}$ un $q_{i}$ ir savstarpēji pirmskaitḷi. Pārveidojam vienādojuma kreisās puses izteiksmi:

$$
a x^{3}+b x^{2}+c x+d=a\left(x+\frac{p_{1}}{q_{1}}\right)\left(x+\frac{p_{2}}{q_{2}}\right)\left(x+\frac{p_{3}}{q_{3}}\right)=\frac{a}{q_{1} q_{2} q_{3}}\left(q_{1} x+p_{1}\right)\left(q_{2} x+p_{2}\right)\left(q_{3} x+p_{3}\right)
$$

levietojot $x=10$, iegūstam

$$
\begin{gathered}
\frac{a}{q_{1} q_{2} q_{3}}\left(10 q_{1}+p_{1}\right)\left(10 q_{2}+p_{2}\right)\left(10 q_{3}+p_{3}\right)= \\
=1000 a+100\left(\frac{p_{1}}{q_{1}}+\frac{p_{2}}{q_{2}}+\frac{p_{3}}{q_{3}}\right)+10\left(\frac{p_{1}}{q_{1}} \cdot \frac{p_{2}}{q_{2}}+\frac{p_{1}}{q_{1}} \cdot \frac{p_{3}}{q_{3}}+\frac{p_{2}}{q_{2}} \cdot \frac{p_{3}}{q_{3}}\right)+\frac{p_{1}}{q_{1}} \cdot \frac{p_{2}}{q_{2}} \cdot \frac{p_{3}}{q_{3}}= \\
=1000 a+100 b+10 c+d=\overline{a b c d} .
\end{gathered}
$$

Reizinot abas puses ar $q_{1} q_{2} q_{3} \neq 0$, iegūstam

$$
q_{1} q_{2} q_{3} \cdot \overline{a b c d}=a\left(10 q_{1}+p_{1}\right)\left(10 q_{2}+p_{2}\right)\left(10 q_{3}+p_{3}\right)
$$

Pamatosim, ja vienādojuma $a x^{3}+b x^{2}+c x+d=0$ sakne ir $\frac{p}{q}$ (nesaīsināma dala), tad $a$ dalās ar $q$. levietojam vienādojumā $a x^{3}+b x^{2}+c x+d=0$ tā sakni $x=\frac{p}{q}$ un pārveidojam iegūto identitāti:

$$
\begin{gathered}
a\left(\frac{p}{p}\right)^{3}+b\left(\frac{p}{q}\right)^{2}+c\left(\frac{p}{q}\right)+d=0 \\
a p^{3}+b p^{2} q+c q^{2} p+d q^{3}=0 \\
q\left(b p^{2}+c q p+d q^{2}\right)=-a p^{3}
\end{gathered}
$$

Tā kā pēdējās vienādības kreisā puse dalās ar $q$, tad arī labās puses izteiksmei jādalās ar $q$. Nemot vērā, ka pēc pieṇēmuma $p$ un $q$ ir savstarpēji pirmskaitli, secinām, ka $a$ ir jādalās ar $q$.

Līdz ar to secinām, ka $q_{i}$ ir viencipara skaitlis, jo $a$ ir cipars.

Analogi iegūst, ka $c$ dalās ar $p_{i}$. Tas nozīmē, ka $10 q_{i}+p_{i}$ ir divciparu skaitlis.

Tātad vienādība $q_{1} q_{2} q_{3} \cdot \overline{a b c d}=a\left(10 q_{1}+p_{1}\right)\left(10 q_{2}+p_{2}\right)\left(10 q_{3}+p_{3}\right)$ nevar pastāvēt, jo kreisajā pusē ir reizinātājs $\overline{a b c d}$ (četrciparu pirmskaitlis), bet labajā pusē $a$ ir viencipara skaitlis un pārējie reizinātāji - divciparu. Līdz ar to dotā vienādojuma saknes nav racionāli skaitli.

12.5. Kādā valstī ir 2020 pilsētas, katra ar katru ir savienota ar ceḷu, celi ārpus pilsētām nekrustojas (izmantoti viadukti). Biznesmenis ar ceḷu pārvaldi spēlē šādu spēli: katru dienu biznesmenis privatizē vienu celu, bet celu pārvalde nojauc desmit neprivatizētus celus. Pierādīt, ka biznesmenis var panākt, ka pēc kāda laika viṇam pieder ciklisks celu maršruts kas iet caur tieši 70 pilsētām, katrā iegriežoties tieši vienu reizi!

Atrisinājums. Vispirms biznesmenis sev var izveidot celu virkni no 67 celiem caur kādām pilsētām $A_{1}-A_{2}-A_{3}-\ldots-A_{67}-A_{68}$. To noteikti var izdarī, jo pat pēc pēdējā gājiena ceḷu pārvalde ir nojaukusi tikai $67 \cdot 10=670$ celus, bet no katras pilsētas iziet 2019 ceḷi. Nosauksim pilsētas $A_{1}, A_{2}, \ldots, A_{68}$ par zalām.

Nākamajā etapā biznesmenis var sev privatizēt 40 celus, kas iziet no pilsētas $A_{1}$ un iet uz pilsētām $S_{1}, S_{2}, \ldots, S_{40}$ (skat. 9. att.), kas nav zalas. To noteikti var izdarī, jo no pilsētas $A_{1}$ iziet $2019-68=1951$ celš uz pilsētām, kas nav zaḷas, bet ceḷu pārvalde pat pēdējā gājienā kopā ir nojaukusi tikai $(67+40) \cdot 10=1070$ celus. Nosauksim pilsētas $S_{1}, \ldots, S_{40}$ par sarkanām.

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-10.jpg?height=262&width=1418&top_left_y=658&top_left_x=381)

9. att.

Nākamajā etapā biznesmenis var sev privatizēt 40 celus, kas iziet no pilsētas $A_{68}$ un iet uz pilsētām $D_{1}, D_{2}, \ldots, D_{40}$, kas nav ne zalas, ne sarkanas. To noteikti var izdarīt, jo no pilsētas $A_{68}$ iziet $2019-68-40=1911$ ceḷi uz pilsētām, kas nav ne zaḷas, ne sarkanas, bet ceḷu pārvalde pat pēdējā gājienā kopā ir nojaukusi tikai $(67+40+40) \cdot 10=1470$ celus.

Uz doto brīdi ceḷu pārvalde ir nojaukusi 1470 celus, bet 40 sarkanās ar 40 zalajām pilsētām kopā savieno $40 \cdot 40=1600$ ceḷi, tātad vismaz 130 no tiem vēl nav nojaukti. Pienemsim, ka nav nojaukts celšs, starp pilsētām $S_{i}$ un $D_{j}$. Tad pēdējā gājienā biznesmenis var privatizēt šo celu un viṇš būs ieguvis ciklisku maršrutu caur 70 pilsētām (skat. 10. att.).

![](https://cdn.mathpix.com/cropped/2024_07_24_55494e53b52a18028c6bg-10.jpg?height=399&width=335&top_left_y=1389&top_left_x=922)

