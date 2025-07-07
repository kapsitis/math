| NACIONĀLAIS |
| :--- | :--- |
| ATTITSTĪBAS |
| PLĀNS 2020 |

I E G U L D İ J U M S T A V Ā N Ā K O T N E

# Latvijas 67. matemātikas olimpiādes 3. posma uzdevumi un atrisinājumi 

9.1. Doti 63 dažādi naturāli skaitli, kuru summa ir 2017. Atrodiet šos skaitlus un pamatojiet, ka citu nav! Atrisinājums. Der skaitli 1, 2, 3, ..., 61, 62, 64. Pierādīsim, ka citu nav. Aplūkosim 63 mazākos naturālos skaitlus. To summa ir $1+2+\cdots+63=\frac{(1+63) \cdot 63}{2}=2016$. Meklēto skaitlu summa ir tikai par 1 lielāka vienīgais veids, kā to iegūt, ir skaitli 63 aizstāt ar 64.

9.2. Uz taisnes atlikti punkti $P, Q, R$ un $S$ tā, ka $P Q=R S$ (skat. 1. att.). Nogriežṇi $P Q, R S, P S, Q R$ ir rinkuu diametri. Nogrieznis $M N$ ir iekrāsotās figūras simetrijas ass. Pierādīt, ka iekrāsotās figūras laukums ir vienāds ar laukumu rinkim, kura diametrs ir $M N$.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-1.jpg?height=529&width=532&top_left_y=1066&top_left_x=753)

Atrisinājums. Nogriežṇu $M N$ un $Q R$ krustpunktu apzīmējam ar $O, O Q=O N=O R=x$ (kā rādiusi) un $P Q=R S=y$. Simetrijas dē! $O P=O S=O M=x+y$. Aprēḳinām laukumus:

$S_{M N}=\left(\frac{M N}{2}\right)^{2} \pi=\frac{(2 x+y)^{2}}{4} \pi=\frac{\pi}{4}\left(4 x^{2}+4 x y+y^{2}\right)=\pi\left(x^{2}+x y+\frac{1}{4} y^{2}\right)$

$S_{\text {iekrāsotais }}=\frac{1}{2} S_{Q R}+\frac{1}{2} S_{P S}-S_{P Q}=\frac{1}{2} O R^{2} \pi+\frac{1}{2} O S^{2} \pi-\left(\frac{P Q}{2}\right)^{2} \pi=\pi\left(\frac{1}{2} x^{2}+\frac{1}{2}(x+y)^{2}-\left(\frac{y}{2}\right)^{2}\right)=$ $=\pi\left(\frac{1}{2} x^{2}+\frac{1}{2} x^{2}+x y+\frac{1}{2} y^{2}-\frac{1}{4} y^{2}\right)=\pi\left(x^{2}+x y+\frac{1}{4} y^{2}\right)$.

Tātad esam pierādījuši, ka iekrāsotās figūras laukums ir vienāds ar laukumu rinkim, kura diametrs ir $M N$.

9.3. Naturālā piecciparu skaitlī vienādus ciparus aizstāja ar vienādiem burtiem, bet dažādus ciparus - ar dažādiem burtiem, un ieguva pierakstu GANGA. Zināms, ka GANGA, dalot ar 7, dod atlikumu $A, G A N G A$, dalot ar 11, dod atlikumu $N$, bet $G A N G A$, dalot ar 13, dod atlikumu $G$, turklāt $G>A>N$. Kāds varēja būt sākotnējais skaitlis?

Atrisinājums. No tā, ka GANGA, dalot ar 7, dod atlikumu $A, G A N G A$, dalot ar 11, dod atlikumu $N$, bet GANGA, dalot ar 13, dod atlikumu $G$, izriet, ka $(\overline{G A N G \bar{A}}-A)$ dalās ar $7,(\overline{G A N G \bar{A}}-N)$ dalās ar 11 un $(\overline{G A N G} \bar{A}-G)$ dalās ar 13 .

Pārveidojam doto skaitli

$$
\overline{G A N G A}=\overline{G A} \cdot 1000+N \cdot 100+\overline{G A}=1001 \cdot \overline{G A}+100 N=13 \cdot 11 \cdot 7 \cdot \overline{G A}+100 N
$$

Pirmais saskaitāmais dalās gan ar 13, gan ar 11, gan ar 7 .

Lai $(\overline{G A N G A}-G)$ dalītos ar $13,(100 N-G)$ ir jādalās ar 13. levērojot, ka

$$
100 N-G=91 N+9 N-G=13 \cdot 7 N+9 N-G
$$

iegūstam, ka $(9 N-G)$ jādalās ar 13.

Līdzīgi, ar 7 ir jādalās $(100 N-A)$. Pārveidojot

$$
100 N-A=98 N+2 N-A=7 \cdot 14 N+2 N-A
$$

iegūstam, ka $(2 N-A)$ jādalās ar 7.

Visbeidzot ar 11 ir jādalās $100 N-N=99 N$, kas vienmēr izpildās.

Tā kā $A$ ir atlikums, kas rodas, skaitli dalot ar 7 , tad $A \leq 6$, un tā kā $A>N$, tad lielākā iespējamā $N$ vērtība ir 5. Apskatīsim visus gadījumus.

| $\boldsymbol{N}$ | $\mathbf{9 N}-\boldsymbol{G}$ | $\boldsymbol{G}$, lai $(\mathbf{9 N}-\boldsymbol{G}) \mathbf{1 3}$ | $\mathbf{2 N}-\boldsymbol{A}$ | $\boldsymbol{A}$, lai $(\mathbf{2 N}-\boldsymbol{A}) \vdots \mathbf{7}$ | $\overline{\mathbf{G A N G A}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\mathbf{0}$ | $-G$ | 0 (neder, jo $N=0$ ) |  |  |  |
| $\mathbf{1}$ | $9-G$ | 9 | $2-A$ | 2 <br> 9 (neder, jo $G=9)$ | 92192 |
| $\mathbf{2}$ | $18-G$ | 5 | $4-A$ | 4 | 54254 |
| $\mathbf{3}$ | $27-G$ | 1 (neder, jo $G<N)$ |  |  |  |
| $\mathbf{4}$ | $36-G$ | nav |  |  |  |
| $\mathbf{5}$ | $45-G$ | 6 | $10-A$ | 3 (neder, jo $A<N$ ) |  |

Tātad sākotnējais skaitlis varēja būt 54254 vai 92192.

9.4. Pierādīt, ka $x^{4}-x^{2}-3 x+4>0$ visiem reāliem $x$.

Atrisinājums. Veicam ekvivalentus pārveidojumus:

$$
\begin{gathered}
\left(x^{2}\right)^{2}-2 x^{2}+1+x^{2}-2 \cdot x \cdot \frac{3}{2}+\frac{9}{4}+\frac{3}{4}>0 \\
\left(x^{2}-1\right)^{2}+\left(x-\frac{3}{2}\right)^{2}+\frac{3}{4}>0
\end{gathered}
$$

Tā kā skaitla kvadrāts ir nenegatīvs un $\frac{3}{4}$ ir pozitīvs skaitlis, tad pēdējā nevienādība ir patiesa. Tā kā tika veikti ekvivalenti pārveidojumi, tad arī dotā nevienādība ir patiesa visiem reāliem skaitlliem $x$.

9.5. Katra no bumbinaām, kas atrodas kastē, nokrāsota vienā no $N$ krāsām, un uz katras uzrakstīts naturāls skaitlis, kas nepārsniedz $N$. Zināms, ka katra no $N$ krāsām izmantota vismaz vienu reizi, tāpat arī katrs skaitlis, kas nepārsniedz $N$, izmantots vismaz vienu reizi. Kādām $N$ vērtībām kastē noteikti varēs atrast $N$ dažādu krāsu bumbiṇas, uz kurām būs rakstīti $N$ dažādi skaitḷi?

Atrisinājums. Ja $N=1$, tad kastē ir vismaz viena bumbiṇa, kas nokrāsota vienīgajā iespējamajā krāsā un uz tās uzrakstīts skaitlis 1. Tātad vērtība $N=1$ der.

Parādīsim, ja $N=2$, tad vienmēr var atrast divas bumbiṇas, kam izpildās prasītās īpašības. Izvēlamies patvalīgu bumbiṇu. Tās krāsu apzīmējam ar $k_{1}$, bet skaitli, kas uz tās uzrakstīts - ar $s_{1}$. Ja kastē atrodas bumbina, kuras krāsa ir $k_{2}$ un uz kuras uzrakstīts skaitlis $s_{2}$, tad esam atraduši nepieciešamo bumbinuu pāri. Apskatīsim gadījumu, kad kastē nav bumbina, kuras krāsa ir $k_{2}$ un uz kuras uzrakstīts skaitlis $s_{2}$. Tā kā kastē ir divu dažādu krāsu bumbiṇas, tad kastē ir jābūt bumbinai, kuras krāsa ir $k_{2}$ un uz kuras uzrakstīts skaitlis $s_{1}$.Tā kā kastē ir bumbiṇa, uz kuras uzrakstīts skaitlis $s_{2}$, tad kastē ir jābūt bumbinai, kuras krāsa ir $k_{1}$ un uz kuras uzrakstīts skaitlis $s_{2}$. Tātad, kastē ir divas bumbiṇas, kuru krāsas ir $k_{2}$ un $k_{1}$ un uz tām uzrakstītie skaitḷi ir attiecīgi $s_{1}$ un $s_{2}$, kas veido nepieciešamo bumbinu pāri.

Pamatosim, ka $N$ nevar būt lielāks kā 2. Tabulā parādīts piemērs, kurā visas uzdevumā minētās īpašības izpildās, bet nevar atrast $N$ dažādu krāsu bumbiṇas, uz kurām uzrakstīti visi skaitli no 1 līdz $N$.

| Skaitlis | $s_{1}$ | $s_{2}$ | $s_{3}$ | $\cdots$ | $s_{N}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Krāsa |  |  |  |  |  |
| $k_{1}$ |  | + | + | $\cdots$ | + |
| $k_{2}$ | + |  |  |  |  |
| $k_{3}$ | + |  |  |  |  |
| $\ldots$ | $\cdots$ |  |  |  |  |
| $k_{N}$ | + |  |  |  |  |

10.1. Dots, ka $b$ un $c$ ir naturāli skaiți un kvadrātvienādojuma $x^{2}-b x+c=0$ reālās saknes ir $x_{1}$ un $x_{2}$. Pierādīt, ka a) $x_{1}^{2}+x_{2}^{2}+2017$; b) $x_{1}^{3}+x_{2}^{3}$ ir naturāls skaitlis!

Atrisinājums. No Vjeta teorēmas izriet, ka $x_{1}+x_{2}=b$ un $x_{1} x_{2}=c$. Tātad gan sakṇu summa, gan sakṇu reizinājums ir naturāls skaitlis un abas saknes ir pozitīvas.

a) Pārveidojam doto izteiksmi:

$$
\begin{gathered}
x_{1}^{2}+x_{2}^{2}+2017=x_{1}^{2}+2 x_{1} x_{2}+x_{2}^{2}-2 x_{1} x_{2}+2017=\left(x_{1}+x_{2}\right)^{2}-2 x_{1} x_{2}+2017= \\
=b^{2}-2 c+2017
\end{gathered}
$$

Tā kā naturāla skait|a kvadrāts ir naturāls skaitlis un naturālu skait|u summa vai starpība ir vesels skaitlis, $\operatorname{tad} b^{2}-2 c+2017$ ir vesels skaitlis, līdz ar to $x_{1}^{2}+x_{2}^{2}+2017$ arī ir vesels skaitlis. Nemot vērā, ka $x_{1}^{2}+$ $x_{2}^{2}+2017>0$, secinām, ka $x_{1}^{2}+x_{2}^{2}+2017$ ir naturāls skaitlis.

b) Pārveidojam doto izteiksmi:

$$
\begin{gathered}
x_{1}^{3}+x_{2}^{3}=\left(x_{1}+x_{2}\right)\left(x_{1}^{2}+x_{2}^{2}\right)-x_{1} x_{2}^{2}-x_{1}^{2} x_{2}=b\left(b^{2}-2 c\right)-x_{1} x_{2}\left(x_{2}+x_{1}\right)= \\
=b\left(b^{2}-2 c\right)-c b=b^{3}-3 b c
\end{gathered}
$$

Tā kā naturāla skaitla kubs ir naturāls skaitlis un naturālu skaitlu starpība ir vesels skaitlis, tad $b^{3}-3 b c$ ir vesels skaitlis. Tā kā $x_{1}^{3}+x_{2}^{3}>0$, tad $x_{1}^{3}+x_{2}^{3}$ ir naturāls skaitlis.

Piezīme. b) gadīumā var izmantot formulu $a^{3}+b^{3}=(a+b)\left(a^{2}-a b+b^{2}\right)$.

10.2. Dots pirmskaitlis, kas satur vismaz 4 dažādus ciparus. Pierādīt, ka tā ciparus var pārkārtot citā secībā tā, lai jauniegūtais skaitlis nebūtu pirmskaitlis!

Atrisinājums. Ja pirmskaitlis satur kādu no cipariem $0,2,4,5,6$ vai 8 , tad, izveidojot skaitli, kur šis cipars ir pēdējais, būsim ieguvuši skaitli, kas dalās ar 2 vai 5, tātad nav pirmskaitlis. Atliek aplūkot gadījumu, kad pirmskaitlis satur tikai ciparus $1,3,7$ un 9 .

Aplūkojam septinus skait|us $x \cdot 10^{4}+1379, x \cdot 10^{4}+1397, x \cdot 10^{4}+1739, x \cdot 10^{4}+1793$, $x \cdot 10^{4}+1937, x \cdot 10^{4}+1973, x \cdot 10^{4}+3719$, kur $x$ ir skaitlis, kura pieraksts veidots no atlikušajiem dotā pirmskait|a cipariem, kas paliek, ja pa vienai reizei izmanto ciparus $1,3,7$ un 9 ( $x=0$, ja dotais bija četrciparu skaitlis).

Aplūkojam atlikumus, kas rodas dalot šos skait|us ar 7 , turklāt uzskatīsim, ka, skaitli $x \cdot 10^{4}$ dalot ar 7 , atlikumā iegūst $y$, kur $y \in\{0 ; 1 ; 2 ; 3 ; 4 ; 5 ; 6\}$.

| Skaitlis | Atlikums, dalot ar 7 |
| :---: | :---: |
| $x \cdot 10^{4}+1379$ | $y$ |
| $x \cdot 10^{4}+1397$ | $y+4$ |
| $x \cdot 10^{4}+1739$ | $y+3$ |
| $x \cdot 10^{4}+1793$ | $y+1$ |
| $x \cdot 10^{4}+1937$ | $y+5$ |
| $x \cdot 10^{4}+1973$ | $y+6$ |
| $x \cdot 10^{4}+3719$ | $y+2$ |

Ievērojam, ka, neatkarīgi no y vērtības, kāds no skaitḷiem dalīsies ar 7, tātad nebūs pirmskaitlis.

Līdz ar to esam pierādījuši vajadzīgo.

10.3. Četrstūris $A B C D$ ir ievilkts rinka līnijā $\omega_{1}$, bet $A B C D$ malu viduspunkti atrodas uz rinka līnijas $\omega_{2}$. Pierādīt, ka $\Varangle A B D+\Varangle B D C=90^{\circ}$.

Atrisinājums. Apzīmēsim malu $A B, B C, C D$ un $D A$ malu viduspunktus attiecīgi ar $E, F, G$ un $H$ (skat. 2. att.). Nogrieznis $E F$ ir trijstūra $A B C$ viduslīnija, tāpēc $E F \| A C$ un $E F=\frac{1}{2} A C$. Līdzīgi, $H G$ ir $\triangle A C D$ viduslīnija, tāpēc $H G \| A C$ un $H G=\frac{1}{2} A C$.

No $\triangle A B D$ un $\triangle B C D$ līdzīgi iegūst, ka $E H=F G=\frac{1}{2} B D$ un $E H \| F \mathrm{G}$.

Tātad četrstūris $E F G H$ ir paralelograms, jo tā pretējās malas ir vienādas. Tā kā visas četrstūra $E F G H$ virsotnes atrodas uz rinka līnijas $\omega_{2}$, tad $E F G H$ ir taisnstūris, no kurienes izriet, ka $B D \perp A C$. Tātad $\triangle D O C$
(punkts $O$ ir $A C$ un $B D$ krustpunkts) ir taisnlenka un $\Varangle O D C+\Varangle O C D=90^{\circ}$ jeb $\Varangle B D C+\Varangle A C D=90^{\circ}$. Tā kā $\Varangle A B D=\Varangle A C D$ kā ievilktie leṇki, kas balstās uz viena un tā paša loka $A D$, tad $\Varangle B D C+\Varangle A B D=90^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-4.jpg?height=526&width=577&top_left_y=345&top_left_x=748)

10.4. Dotas 40 kartītes, uz divām no tām uzrakstīts skaitlis 1, uz divām - skaitlis 2, ..., uz divām - skaitlis 20 . Kāds ir lielākais iespējamais komplektu skaits, ko vienlaicīgi var izveidot no šīm 40 kartītēm tā, lai katrā komplektā būtu trīs kartītes, uz kurām uzrakstīto skait|u summa ir 21 ?

Atrisinājums. Lielākais komplektu skaits ir astonii, piemēram, (6, 7, 8); (5, 7, 9); (4, 5, 12); (3, 4, 14); $(3,6,12) ;(2,8,11) ;(2,9,10) ;(1,1,19)$.

Pierādīsim, ka vairāk kā astoṇus komplektus izveidot nevar. Ja varētu izveidot devinus komplektus, tad būtu izmantotas 27 kartītes un uz tām uzrakstīto skait|u summa būtu $9 \cdot 21=189$, bet pati mazākā skait|u summa, ko var iegūt no 27 kartītēm, ir

$$
2 \cdot 1+2 \cdot 2+2 \cdot 3+\cdots+2 \cdot 13+14=2 \cdot(1+2+\cdots+13)+14=2 \cdot \frac{(1+13) \cdot 13}{2}+14=196
$$

kas jau ir lielāka nekā 189. Tātad devinus komplektus izveidot nevar.

10.5. Seši tūristi bija devušies vairākos ceḷojumos uz sešām valstīm, katrā cellojumā viens tūrists apceloja tieši vienu valsti. Ja izvēlamies jebkuras trīs valstis un jebkurus trīs tūristus, tad vismaz viens no viniem ir bijis celojumā uz kādu no šīm valstīm. Kāds ir mazākais iespējamais kopējais celojumu skaits?

Atrisinājums. Mazākais iespējamais kopējais ceḷojumu skaits ir 10 . Rakstīsim ceḷojumus $6 \times 6$ tabulā, rindinas atbildīs tūristiem, kolonnas - valstīm, ja tūrists ir bijis celojumā uz kādu valsti, tad šajā rūtiṇā liksim krustinu. Pamatosim, ka der tabulā parādītais piemērs. Viegli redzēt, ka jebkuri 3 tūristi ir kopumā apmeklējuši vismaz 4 valstis, tātad, izvēloties jebkuras 3 valstis, vismaz vienu no tām kāds no šiem tūristiem būs apmeklējis.

| Valsts | 1. | 2. | 3. | 4. | 5. | 6. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Tūrists | 1. |  |  |  |  |  |
| 1. |  |  |  |  | $\mathbf{X}$ | $\mathbf{X}$ |
| 2. |  |  |  | $\mathbf{X}$ |  | $\mathbf{X}$ |
| 3. |  |  | $\mathbf{X}$ |  | $\mathbf{X}$ |  |
| 4. |  |  | $\mathbf{X}$ | $\mathbf{X}$ |  |  |
| 5. |  | $\mathbf{X}$ |  |  |  |  |
| 6. | $\mathbf{X}$ |  |  |  |  |  |

Pierādīsim, ka ar deviṇiem celojumiem nepietiek. Aplūkosim 3 tūristus, kuri ir devušies vismazāk ceḷojumos. Vispirms pamatosim, ka tie kopā ir devušies ne vairāk kā 3 ceḷojumos. Ja tie būtu devušies četros celojumos, tad vismaz kāds no tiem būtu devies divos celojumos, tātad arī atlikušie 3 tūristi katrs būtu devušies vismaz divos ceḷojumos (jo mēs aplūkojam tūristus, kas ir ceḷojuši vismazāk). Tātad kopējais ceḷojumu skaits ir vismaz $4+2 \cdot 3=10$ un iegūta pretruna. Līdz ar to ir 3 tūristi, kas kopā ir devušies ne vairāk kā 3 ceḷojumos, tātad tie kopā apmeklējuši ne vairāk kā 3 valstis. Tāpēc ir vismaz 3 valstis, ko neviens no šiem trim tūristiem nav apmeklējis, kas ir pretrunā ar uzdevuma nosacījumiem.

11.1. Cik ir tādu piecciparu skait|u, kam katrs nākamais cipars ir lielāks par iepriekšējo?

Atrisinājums. Katru šādu piecciparu skaitli var iegūt izsvītrojot 4 ciparus no skaitḷa 123456789. Tā kā četrus ciparus var izvēlēties $C_{9}^{4}=\frac{9 \cdot 8 \cdot 7 \cdot 6}{4 \cdot 3 \cdot 2 \cdot 1}=126$ veidos, tad ir tieši 126 šādi piecciparu skaitli.

11.2. Kurš no skaitliem $(\sqrt{7})^{\sqrt{5}}$ un $(\sqrt{5})^{\sqrt{7}}$ ir lielāks?

Atrisinājums. Lielāks ir skaitlis $(\sqrt{7})^{\sqrt{5}}$. Kāpināsim abus skaitlus pakāpē $2 \sqrt{5}$ un pierādīsim, ka $(\sqrt{5})^{\sqrt{7} \cdot 2 \sqrt{5}}<(\sqrt{7})^{\sqrt{5} \cdot 2 \sqrt{5}}$. Tas savukārt izriet no tā, ka $(\sqrt{7})^{\sqrt{5} \cdot 2 \sqrt{5}}=7^{5}=16087$, bet $(\sqrt{5})^{\sqrt{7} \cdot 2 \sqrt{5}}=5^{\sqrt{35}}<5^{6}=15625$.

11.3. Trīs rinka līnijas $\omega_{1}, \omega_{2}$ un $\omega_{3}$ krustojas punktā $O$. Riṇka līnijas pa pāriem krustojas arī punktos $P\left(\omega_{1}\right.$ un $\left.\omega_{2}\right), R\left(\omega_{2}\right.$ un $\left.\omega_{3}\right)$ un $S\left(\omega_{1}\right.$ un $\left.\omega_{3}\right)$. Uz $\omega_{1}$ loka $P S$, kas nesatur $O$, izvēlēts punkts $A$, taisne $A P$ vēlreiz krusto $\omega_{2}$ punktā $B$, un taisne $A S$ vēlreiz krusto $\omega_{3}$ punktā $C$. Pierādīt, ka punkti $B, R$ un $C$ atrodas uz vienas taisnes!

Atrisinājums. Savienojam punktu $R$ ar $B$ un $C$ (skat. 3. att.), pietiek pierādīt, ka $\Varangle B R C=180^{\circ}$. Tā kā ievilkta četrstūra pretējo leṇku summa ir $180^{\circ}$ un blakusleṇku summa ir $180^{\circ}$, tad $\Varangle B R O=180^{\circ}-\Varangle B P O=\Varangle A P O$. Līdzīgi iegūst $\quad \Varangle C R O=180^{\circ}-\Varangle C S O=\Varangle A S O$. Tātad $\Varangle B R C=\Varangle B R O+\Varangle C R O=\Varangle A P O+\Varangle A S O=180^{\circ}$ kā ievilktā četrstūra pretējo leṇku summa.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-5.jpg?height=429&width=464&top_left_y=1062&top_left_x=799)

3. att.

11.4. Pierādīt, ka no jebkuriem 17 naturāliem skaitlliem var izvēlēties 9 skait|us tā, lai to summa dalītos ar 9 .

Atrisinājums. Pierādīsim, ka no jebkuriem pieciem naturāliem skaitliem var izvēlēties trīs skaitḷus tā, ka to summa dalās ar 3 . Skaitli, dalot ar 3, var iegūt atlikumu 0; 1 vai 2 .

- Ja starp pieciem dotajiem skaitliem ir trīs skaitli, kas dod vienādu atlikumu, dalot ar 3 , tad to summa dalās ar 3 , jo $0+0+0 \equiv 0(\bmod 3) ; 1+1+1 \equiv 0(\bmod 3) ; 2+2+2 \equiv 0(\bmod 3)$.
- Ja nav trīs skaitlu, kas dod vienādu atlikumu, dalot ar 3, tad ir vismaz viens skaitlis no katra atlikuma veida. Šo trīs skaitlu summa dalās ar 3 , jo $0+1+2 \equiv 0(\bmod 3)$.

Izmantojot iepriekš pierādīto, no sākotnējiem 17 skaitlliem varam izveidot piecas grupas pa trīs skaitliem tā, lai tajās esošo skaitlu summa dalās ar 3 . Apzīmējam

$$
\left\{a_{1}, a_{2}, a_{3}\right\} ;\left\{b_{1}, b_{2}, b_{3}\right\} ;\left\{c_{1}, c_{2}, c_{3}\right\} ;\left\{d_{1}, d_{2}, d_{3}\right\} ;\left\{e_{1}, e_{2}, e_{3}\right\}
$$

Skait|us, kurus iegūst katras grupas skait|u summu dalot ar 3 , apzīmējam attiecīgi ar $A, B, C, D$ un $E$. No iepriekš pierādītā izriet, ka no šiem pieciem iegūtajiem skaitliem var izvēlēties trīs tā, ka to summa dalās ar 3. Nezaudējot vispārīgumu, pieṇemsim, ka $A+B+C$ dalās ar 3 jeb

$$
A+B+C=3 n
$$

kur $n$ - naturāls skaitlis. Tā kā $A=\frac{a_{1}+a_{2}+a_{3}}{3} ; B=\frac{b_{1}+b_{2}+b_{3}}{3} ; C=\frac{c_{1}+c_{2}+c_{3}}{3}$, tad iegūstam

$$
\frac{a_{1}+a_{2}+a_{3}}{3}+\frac{b_{1}+b_{2}+b_{3}}{3}+\frac{c_{1}+c_{2}+c_{3}}{3}=3 n
$$

Reizinot abas vienādības puses ar 3 , iegūstam

$$
a_{1}+a_{2}+a_{3}+b_{1}+b_{2}+b_{3}+c_{1}+c_{2}+c_{3}=9 n
$$

Tātad esam ieguvuši, ka $a_{1}+a_{2}+a_{3}+b_{1}+b_{2}+b_{3}+c_{1}+c_{2}+c_{3}$ dalās ar 9 un prasītais ir pierādīts.

11.5. Uz riṇka līnijas atzīmēti $N$ punkti tā, ka šie punkti ir regulāra $N$-stūra virsotnes. Spēlētāji $A$ un $B$ spēlē šādu spēli: Vini pārmaiṇus novelk pa vienai hordai, kas savieno divus atzīmētos punktus uz rinka līnijas tā, lai novilktā horda nekrustotos ar agrāk novilktajām hordām. Uzvar tas spēlētājs, pēc kura gājiena no novilktajām hordām izveidojas trijstūris. Kurš spēēētājs noteikti var uzvarēt, ja $A$ izdara pirmo gājienu un a) $N=14$; b) $N=15$ ?

Atrisinājums. a) Ja $N=14$, tad noteikti var uzvarēt spēlētājs $A$. Pirmajā gājienā spēlētājam $A$ jānovelk diametrs. Pēc katra spēlētāja $B$ gājiena spēlētājs $A$ pārbauda, vai ir iespējams novilkt hordu tā, lai veidotos trijstūris. Ja tādu hordu var novilkt, tad spēlētājs $A$ to novelk un līdz ar to uzvar. Ja tādu hordu nav iespējams novilkt, tad spēlētājs $A$ velk hordu, kas ir simetriska spēlētāja $B$ tikko novilktajai hordai attiecībā pret pirmajā gājienā novilkto diametru (piemēram, skat. 4. att.). Kamēr spēlētājs $B$ var novilkt hordu, arī spēlētājs $A$ simetriski attiecībā pret novilkto diametru var novilkt hordu. Tā kā iespējas novilkt hordu ar katru gājienu samazinās, tad pienāks brīdis, kad $B$ novilks hordu tā, ka spēlētājs $A$ savā nākamajā gājienā varēs izveidot trijstūri un būs uzvarējis.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-6.jpg?height=347&width=307&top_left_y=843&top_left_x=880)

b) Ja $N=15$, tad noteikti var uzvarēt spēlētājs $B$. Tā kā pēdējā gājienā tiek novilkta trijstūra trešā mala (to izdara uzvarētājs) un pirmspēdējā gājienā tiek novilkta trijstūra otrā mala (to izdara zaudētājs), tad, lai uzvarētu, spēlētāji visā spēles gaitā izvairās vilkt tās hordas, kurām kāda virsotne sakrīt ar jau novilktu hordu. Tāpēc varam analizēt šādu spēli: spēlētāji velk hordas tā, lai tās nekrustotos un lai neizmantotu ar novilktajām hordām kopīgus galapunktus, tādā gadījumā uzvarētājs ir tas, kurš novelk pēdējo šādu hordu. Neizmantotos punktus jau novilktās hordas sadala vairākās grupās - vienā grupā nonāk tie punkti, kurus joprojām var savienot ar hordu. Katrā gājienā spēlētājs var izvēlēties vienu no esošajām grupām un tajās esošos punktus ar hordu sadalīt divās grupās. Tās grupas, kurās ir 0 vai 1 punkts, atmetam, jo tās neiespaido turpmāko spēles gaitu.

Piemēram, pirms tiek novilkta horda $C E$ (skat. 5. att.), brīvie punkti sadalās grupās: $\{A, B, H, I\} ;\{C, E, F, G\}$ (tā kā punkts $D$ ir viens pats, tad to vienojāmies atmest). Šo pozīciju, kad ir divas grupas katrā pa 4 neizmantotiem punktiem, apzīmēsim $(4,4)$. Tad, kad tiek novilkta horda $C E$, iegūstam grupas : $\{A, B, H, I\}$ un $\{F, G\}$. Tātad tiek izdarīts gājiens no pozīcijas $(4,4)$ uz pozīciju $(4,2)$, apzīmēsim $(4,4) \rightarrow(4,2)$.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-6.jpg?height=464&width=392&top_left_y=1887&top_left_x=838)

Lai pierādītu, ka spēlētājs $B$ noteikti var uzvarēt, aplūkosim visus iespējamos spēlētāja $A$ gājienus no sākuma pozīcijas (15) un katram no šiem gājieniem atradīsim atbilstošu spēlētāja $B$ gājienu, kas viṇam nodrošinās uzvaru. Starp 15 punktiem spēlētājs $A$ var novilkt hordu septiṇos dažādos veidos, katrā no šiem gadījumiem spēlētājs $B$ var turpināt šādi:

$$
15 \rightarrow\left\{\begin{aligned}
(13) & \rightarrow(\mathbf{8}, \mathbf{3}) \\
(12) & \rightarrow(5,5) \\
(11,2) & \rightarrow(\mathbf{8}, \mathbf{2}) \\
(10,3) & \rightarrow(\mathbf{8}, \mathbf{3}) \\
(9,4) & \rightarrow(\mathbf{9}) \\
(8,5) & \rightarrow(\mathbf{5}, \mathbf{5}) \\
(7,6) & \rightarrow(7,3)
\end{aligned}\right.
$$

Pamatosim, ka treknrakstā izceltās pozīcijas ir "uzvarošās", tas ir, ja šādā pozīcijā spēlētājs nonāk, tad viṇš sev var nodrošināt uzvaru.

levērosim, ja pēc spē̄ētāja $B$ gājiena ir pozīcija $(\boldsymbol{m}, \boldsymbol{m})$, tad spēlētājs $B$ var uzvarēt, turpmāk izdarot pretinieka gājieniem simetriskus gājienus otrā punktu grupā.

Spēēētājs $A$ no pozīcijas $(\mathbf{8}, \mathbf{3})$ un no pozīcijas $(\mathbf{8}, \mathbf{2})$ hordu var novilkt piecos dažādos veidos, katrā no šiem gadijumiem spēlētājs $B$ var turpināt šādi:

$$
(\mathbf{8}, \mathbf{3}) \rightarrow\left\{\begin{array} { l } 
{ ( 8 ) \rightarrow ( \mathbf { 3 , 3 } ) } \\
{ ( 6 , 3 ) \rightarrow ( \mathbf { 3 , 3 } ) } \\
{ ( 5 , 3 ) \rightarrow ( \mathbf { 3 , 3 } ) } \\
{ ( 4 , 2 , 3 ) \rightarrow ( \mathbf { 2 , 3 } } \\
{ ( 3 , 3 , 3 ) \rightarrow ( \mathbf { 3 , 3 } }
\end{array} \quad ( \mathbf { 8 } , \mathbf { 2 } ) \rightarrow \left\{\begin{array}{c}
(8) \rightarrow(3,3) \\
(6,2) \rightarrow(2,3) \\
(5,2) \rightarrow(2,3) \\
(4,2,2) \rightarrow(\mathbf{2 , 2}) \\
(3,3,2) \rightarrow(3,3)
\end{array}\right.\right.
$$

Pozīcija $(2,3)$ ir uzvarošā spēlētājam $B$, jo no tās var izdarīt tieši divus gājienus.

Spēēēājs $A$ no pozīcijas $(9)$ un no pozīcijas $(7,3)$ hordu var novilkt četros dažādos veidos, katrā no šiem gadijumiem spēēētājs $B$ var turpināt šādi:

$$
(9) \rightarrow\left\{\begin{array} { l } 
{ ( 7 ) \rightarrow ( 2 , 3 ) } \\
{ ( 6 ) \rightarrow ( 2 , 2 ) } \\
{ ( 5 , 2 ) \rightarrow ( 2 , 2 ) } \\
{ ( 4 , 3 ) \rightarrow ( 2 , 3 ) }
\end{array} \quad ( 7 , 3 ) \rightarrow \left\{\begin{array}{l}
(7) \rightarrow(2,3) \\
(6) \rightarrow(2,2) \\
(5,2) \rightarrow(2,2) \\
(4,3) \rightarrow(2,3)
\end{array}\right.\right.
$$

Līdz ar to esam ieguvuši uzvarošu stratēġiju spēlētājam $B$ : katrā savā gājienā viṇš novelk hordu tā, lai nonāktu "uzvarošajā" pozīcijā, kas izcelta treknrakstā. Visos gadījumos spēlētājs $B$ nonāks pozīcijā $(2,3)$ vai $(\boldsymbol{m}, \boldsymbol{m})$ un vēl pēc pāra skaita gājieniem būs tas, kurš novelk pēdējo hordu, kurai ar jau novilktajām hordām nav kopīgu galapunktu.

12.1. Doti tādi skaitlli $a, b$ un $c$, ka $a+c=\frac{b}{3^{3}}$, turklāt neviens no skaitlliem $a, b, c$ nav 0 . Pierādit, ka $f(x)=a x^{2}+b x+c$ grafiks noteikti krusto $x$ asi kādā intervāla $[-1 ; 1]$ punktā!

Atrisinājums. levērojam, ka funkcijas vērtībām $f(-1)$ un $f(1)$ ir dažādas zīmes:

$f(-1)=a-b+c=\frac{b}{3}-b=-\frac{2 b}{3}$;

$f(1)=a+b+c=\frac{b}{3}+b=\frac{4 b}{3}$.

Tādā gadījumā skaidrs, ka šajā intervālā $[-1,1]$ funkcijas grafikam ir jākrusto $x$ ass.

12.2. Pierādī, ka $\sqrt{x^{2}+y^{2}}+(2-\sqrt{2}) \sqrt{x y} \geq x+y$, ja $x$ un $y$ ir reāli pozitīvi skaitl|i!

Atrisinājums. Tā kā abas nevienādības puses ir pozitīvas, tad, kāpinot kvadrātā, iegūstam

$$
\begin{gathered}
x^{2}+y^{2}+2 \cdot \sqrt{x^{2}+y^{2}} \cdot(2-\sqrt{2}) \sqrt{x y}+(4-4 \sqrt{2}+2) x y \geq x^{2}+2 x y+y^{2} \\
2 \cdot \sqrt{x^{2}+y^{2}} \cdot(2-\sqrt{2}) \sqrt{x y} \geq 4(\sqrt{2}-1) x y
\end{gathered}
$$

Izdalot abas nevienādības puses ar $2 \sqrt{x y}>0$ un pēc tam kāpinot abas nevienādības puses kvadrātā (abas puses ir pozitīvas), pakāpeniski iegūstam

$$
\begin{aligned}
& \sqrt{x^{2}+y^{2}} \cdot(2-\sqrt{2}) \geq 2(\sqrt{2}-1) \sqrt{x y} \\
& \left(x^{2}+y^{2}\right) \cdot(6-4 \sqrt{2}) \geq 4(3-2 \sqrt{2}) x y
\end{aligned}
$$

Izdalot abas nevienādības puses ar $(6-4 \sqrt{2})>0$, iegūstam $x^{2}+y^{2} \geq 2 x y$ jeb $(x-y)^{2} \geq 0$.

Tā kā skaitla kvadrāts ir nenegatīvs, tad pēdējā nevienādība ir patiesa. Tā kā tika veikti ekvivalenti pārveidojumi, tad arī dotā nevienādība ir patiesa visiem reāliem skaitliem $x$.

12.3. Dots taisnstūris $A B C D$. Uz taisnes $B D$ atlikts punkts $E$, tā ka $D$ atrodas starp $B$ un $E$. Uz taisnes $E C$ atlikts punkts $F$ tā, ka $B F$ ir paralēls $A C$. Pierādīt, ka trijstūra $B E F$ laukums ir lielāks nekā taisnstūra $A B C D$ laukums!

1. atrisinājums. No punkta $F$ velkam perpendikulu pret taisni $B C$, šī perpendikula krustpunktu ar $B D$ apzīmējam ar $F^{\prime}$ (skat. 6. att.). levērojam, ka $\Varangle C A D=\Varangle F B C$ kā leṇḳi, kuru malas atrodas uz paralēlām taisnēm, un $\Varangle C A D=\Varangle C B F^{\prime}$ (taisnstūra īpašība), tātad $\Varangle F B C=C B F^{\prime}$ un trijstūris $F B F^{\prime}$ ir vienādsānu, no kā izriet, ka punkti $F$ un $F^{\prime}$ ir simetriski attiecībā pret taisni $B C$.

Simetrijas dē! $S(B F C)=S\left(B F^{\prime} C\right)$ un $S(A B C D)=2 \cdot S(B F C)+2 \cdot S\left(C D F^{\prime}\right)$, līdz ar to pietiek pierādīt, ka $S(C D E)>S\left(C D F^{\prime}\right)$.

Apzīmējam $\quad \Varangle F^{\prime} C D=\alpha$, tad simetrijas dē! $\quad \Varangle F C B=\Varangle B C F^{\prime}=90^{\circ}-\alpha \quad$ un $\Varangle E C D=180^{\circ}-\Varangle F C B-\Varangle B C F^{\prime}-\Varangle F^{\prime} C D=180^{\circ}-2 \cdot\left(90^{\circ}-\alpha\right)-\alpha=\alpha . \quad$ Līdz ar to $S(C D E)=\frac{1}{2} C E \cdot C D \cdot \sin \alpha$ un $S\left(C D F^{\prime}\right)=\frac{1}{2} C F^{\prime} \cdot C D \cdot \sin \alpha$, tātad atliek pamatot, ka $C E>C F^{\prime}$ jeb $C E>C F$. Tā kā $B E>B F^{\prime}=B F$ un nogrieznis $B C$ ir trijstūra $E B F$ bisektrise, tad no bisektrises īpašības izriet, ka $C E>C F$.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-8.jpg?height=415&width=443&top_left_y=912&top_left_x=835)

6. att.
7. atrisinājums. Apzīmējam $A B=C D=a, D E=p, O A=O B=O C=O D=y$ (kur punkts $O$ ir diagonālu krustpunkts), $B F=x$ un $\Varangle D B C=\Varangle D A C=\Varangle C B F=\alpha$ (skat. 7. att.). Trijstūra $B E C$ augstums pret $B C$ ir $h_{1}$, bet trijstūra $B F C$ augstums pret $B C$ ir $h_{2}$.

Tad $S(A B C D)=B C \cdot a$ un $S(B E F)=S(B E C)+S(B C F)=\frac{1}{2} B C \cdot h_{1}+\frac{1}{2} B C \cdot h_{2}=B C \cdot \frac{h_{1}+h_{2}}{2}$.

Tātad nepieciešams pierādīt, ka $h_{1}+h_{2}>2 a$.

Tā kā $\triangle O E C \sim \triangle B E F$, jo leṇki $B E F$ krusto divas paralēlas taisnes $O C$ un $B F$, tad $\frac{O E}{B E}=\frac{O C}{B F}$ jeb $\frac{p+y}{p+2 y}=\frac{y}{x}$. Izsakām $x=y \cdot \frac{p+2 y}{p+y}$.

No $\triangle B C D$ iegūstam, ka $\sin \alpha=\frac{C D}{B D}=\frac{a}{2 y}$.

Apskatām summu $h_{1}+h_{2}$ :

$$
h_{1}+h_{2}=(2 y+p) \sin \alpha+x \sin \alpha=(2 y+p+x) \sin \alpha=\left(2 y+p+y \frac{p+2 y}{p+y}\right) \frac{a}{2 y}=a \frac{p^{2}+4 p y+4 y^{2}}{2 p y+2 y^{2}}
$$

Tā kā $p>0$, tad $p^{2}>0$ un $a \frac{p^{2}+4 p y+4 y^{2}}{2 p y+2 y^{2}}>a \frac{p^{2}+4 p y+4 y^{2}}{\frac{p^{2}}{2}+2 p y+2 y^{2}}=2 a$, kas arī bija jāpierāda.

![](https://cdn.mathpix.com/cropped/2024_07_25_d0d1c92d3a2f1445677ag-8.jpg?height=543&width=581&top_left_y=2130&top_left_x=743)

12.4. Naturālu skaitli sauksim par skaistu, ja tā visu naturālo dalītāju summa (ieskaitot 1 un pašu skaitli) ir nepāra skaitlis. Atrast mazāko naturālo skaiti $k$ ar īpašību: starp jebkuriem patvalīgi izvēlētiem $k$ skaistiem skaitḷiem var izvēlēties divus dažādus skait|lus tā, lai to reizinājums būtu naturāla skait|a kvadrāts!

Atrisinājums. Mazākā $k$ vērtība ir 3.

levērojam, ka $k=2$ neder, jo, piemēram, izvēloties skaistus skaitlus 2 un 9 (dalītāju summa ir attiecīgi $1+2=3$ un $1+3+9=13$ ), to reizinājums $2 \cdot 9=18$ nav naturāla skait!̣a kvadrāts.

Pierādīsim, ka ar $k=3$ pietiek. Jebkuru naturālu skaitli $n$ var izteikt formā $n=2^{u} \cdot v$, kur $v$ ir nepāra skaitlis. Skaidrs, ja $n$ ir skaists, tad arī $v$ ir skaists, jo visi $n$ nepāra dalītāji ir visi $v$ dalītāji, bet pāra dalītāji nemaina dalītāju summas paritāti. Visi $v$ dalītāji ir nepāra skaitḷi, sadalām tos pāros tā, ka vienā pārī ietilpst $v$ dalītāji, kuru reizinājums ir $v$. lespējami divi gadījumi.

- Ja $v$ nav naturāla skait!̣a kvadrāts, tad visus dalītājus šādi var sadalīt pāros, tātad to summa ir pāra skaitlis, tātad $v$ šādā gadījumā nav skaists.
- Ja $v$ ir naturāla skaitla kvadrāts, tas ir, $v=k^{2}$, tad visi dalītāji, izṇemot $k$, sadalās pāros. Tātad šādā gadījumā dalītāju skaits ir nepāra skaitlis un to summa arī ir nepāra, tātad $v$ ir skaists.

No tā secinām, ka $n$ ir skaists, ja $v$ ir kvadrāts.

Ja doti trīs skaisti skait!i $n_{1}=2^{u_{1}} \cdot v_{1}, n_{2}=2^{u_{2}} \cdot v_{2}$ un $n_{3}=2^{u_{3}} \cdot v_{3}$, tad divi no skaitliem $u_{1}, u_{2}$, $u_{3}$ būs ar vienādu paritāti, ja sareizina attiecīgos skaistos skait!us (pienemsim, ka tie ir $n_{1}$ un $n_{2}$ ), tad redzams, ka reizinājums $n_{1} \cdot n_{2}=2^{u 1+u 2} v_{1} v_{2}$ ir naturāla skait|a kvadrāts.

12.5. Kādā valstī no parlamenta deputātiem ir izveidotas 100 komisijas. Katram deputātam ir pienākums strādāt vismaz vienā komisijā, taču deputāti drīkst strādāt arī vairākās komisijās. Deputāti par darbu komisijās katru mēnesi saṇem atalgojumu pēc šāda principa:

- par darbu pirmajā komisijā netiek maksāts atalgojums;
- par darbu katrā nākamajā komisijā tiek maksāts par 10 eiro vairāk nekā par darbu iepriekšējā komisijā (tas ir, par darbu otrajā komisijā tiek maksāti 10 eiro, par darbu trešajā komisijā tiek maksāti 20 eiro utt.).

Zināms, ka jebkurām divām dažādām komisijām ir tieši viens kopīgs deputāts, kas darbojas tajās abās. Cik liels ir visu deputātu kopējais mēneša atalgojums par darbu komisijās?

Atrisinājums. Sanumurējam deputātus ar numuriem 1, 2, 3, .., n. Ar $k(d)$ apzīmējam visu komisiju skaitu, kurās strādā deputāts $d$. No dotā izriet, ka deputāts $d$ par darbu komisijās mēnesī saṇem $10 \cdot(0+1+2+\cdots+k(d)-1)=10 \cdot \frac{k(d)(k(d)-1)}{2}=10 \cdot C_{k(d)}^{2}$ eiro. Līdz ar to visi deputāti kopā par darbu komisijās mēnesī saṇem $10 \cdot\left(C_{k(1)}^{2}+C_{k(2)}^{2}+\cdots+C_{k(n)}^{2}\right)$ eiro.

Saskaitīsim, cik ir tādu pāru $\{A ; B\}$, ka $A$ un $B$ ir dažādas komisijas:

- Tā kā pavisam ir 100 komisijas, tad dažādo komisiju pāru skaits ir $C_{100}^{2}=\frac{100 \cdot 99}{2}=4950$.
- Katram šādam pārim atbilst tieši viens deputāts $d$, kas strādā gan $A$, gan $B$, tātad visus komisiju pārus var sadalīt $n$ grupās tā, ka katram komisiju pārim $\{A ; B\}$ no $d$-tās grupas, $d=1,2, \ldots, n$, ir kopīgs deputāts. Tādā gadījumā $d$-tajā grupā ir tieši $C_{k(d)}^{2}$ komisiju pāri (jo no deputāta $d$ apmeklētajām komisijām var izveidot $C_{k(d)}^{2}$ komisiju pārus). Tā kā katrs komisiju pāris $\{A ; B\}$ pieder tieši vienai no šīm $n$ grupām, tad no summas likuma izriet, ka pāru $\{A ; B\}$ skaits ir $C_{k(1)}^{2}+C_{k(2)}^{2}+\cdots+C_{k(n)}^{2}$

Vienu un to pašu lielumu esam saskaitījuši divos dažādos veidos, tātad abos gadījumos iegūtie skaitḷi ir vienādi:

$$
C_{k(1)}^{2}+C_{k(2)}^{2}+\cdots+C_{k(n)}^{2}=4950
$$

Līdz ar to esam ieguvuši, ka visi parlamenta deputāti kopā par darbu komisijās mēnesī saṇem

$$
10 \cdot\left(C_{k(1)}^{2}+C_{k(2)}^{2}+\cdots+C_{k(n)}^{2}\right)=49500 \text { eiro. }
$$

