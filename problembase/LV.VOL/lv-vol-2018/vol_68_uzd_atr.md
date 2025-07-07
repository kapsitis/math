![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-1.jpg?height=212&width=1690&top_left_y=134&top_left_x=183)

I E G U L D Ī J U M S T A V Ā N Ā K O T N Ē

# Latvijas 68. matemātikas olimpiādes 3. posma 1. kārtas uzdevumi un atrisinājumi 

## 9. klase

9.1. Zināms, ka $a$ un $b$ ir pozitīvi skaitli, un kvadrātfunkciju $y=a x^{2}+2018 x+b$ un $y=b x^{2}+2018 x+a$ minimālo vērtību summa ir nulle. Pierādīt, ka katrai no šīm kvadrātfunkcijām minimālā vērtība ir nulle!

1. atrisinājums. Abām dotajām kvadrātfunkcijām ir vienāds sakṇu skaits, jo tām ir vienāds diskrimintants $D=2018^{2}-4 a b$. Ja tām abām būtu divas saknes, tad to minimālās vērtības būtu negatīvas un to summa arī būtu negatīva. Ja tām abām nebūtu sakṇu, tad to minimālās vērtības būtu pozitīvas un summa arī pozitīva. Tātad tām abām ir tieši viena sakne, kas nozīmē, ka to minimālā vērtība ir nulle.
2. atrisinājums. Tā kā $a$ un $b$ ir pozitīvi skaitli, tad abu parabolu zari ir vērsti uz augšu un kvadrātfunkciju minimālā vērtība sakrīt ar parabolas virsotnes $y$ koordinātu. Parabolas $y=a x^{2}+2018 x+b$ virsotnes koordinātas ir

$$
x_{v_{1}}=-\frac{2018}{2 a}=-\frac{1009}{a} \quad \text { un } \quad y_{v_{1}}=a \cdot\left(-\frac{1009}{a}\right)^{2}+2018 \cdot\left(-\frac{1009}{a}\right)+b=-\frac{1009^{2}}{a}+b
$$

bet parabolas $y=b x^{2}+2018 x+a$ virsotnes koordinātas ir

$$
x_{v_{2}}=-\frac{1009}{b} \quad \text { un } \quad y_{v_{2}}=b \cdot\left(-\frac{1009}{b}\right)^{2}+2018 \cdot\left(-\frac{1009}{b}\right)+a=-\frac{1009^{2}}{b}+a
$$

Tā kā abu kvadrātfunkciju minimālo vērtību summa ir nulle, tad

$$
\begin{gathered}
-\frac{1009^{2}}{a}+b-\frac{1009^{2}}{b}+a=0 \\
a+b-\frac{1009^{2}}{a b}(a+b)=0 \\
(a+b)\left(1-\frac{1009^{2}}{a b}\right)=0
\end{gathered}
$$

Tā kā $a+b>0, \operatorname{tad}\left(1-\frac{1009^{2}}{a b}\right)=0$ jeb $a b=1009^{2}$. Tātad $b=\frac{1009^{2}}{a}$ un $y_{v_{1}}=-\frac{1009^{2}}{a}+\frac{1009^{2}}{a}=0$. Līdzīgi iegūst, ka $y_{v_{2}}=0$.

Piezīme. Kvadrātfunkcijas minimālo vērtību var atrast arī atdalot pilno kvadrātu:

$$
y=a x^{2}+2018 x+b=a\left(x^{2}+2 \cdot 1009 \cdot x \cdot \frac{1}{a}+\frac{1009^{2}}{a^{2}}\right)+b-\frac{1009^{2}}{a^{2}}=a\left(x+\frac{1009}{a}\right)^{2}+b-\frac{1009^{2}}{a^{2}}
$$

Tā kā $a\left(x+\frac{1009}{a}\right)^{2} \geq 0$, tad kvadrātfunkcijas minimālā vērtība $y_{v_{1}}=b-\frac{1009^{2}}{a^{2}}$.

9.2. Izvēlēti trīs dažādi naturāli skaitḷi un aprēkināti to reizinājumi pa pāriem, iegūstot trīs reizinājumus. Pierādīt, ka šos reizinājumus, dalot ar 4 , vismaz divi dod vienādus atlikumus!

Atrisinājums. Katru naturālu skaitli $n$ var izteikt formā $n=4 b+a$, kur $b \in \mathbb{Z}$ un $a$ ir skaitḷa $n$ atlikums, dalot ar 4. Iespējamās atlikuma $a$ vērtības ir $0,1,2$ vai 3 . Apskatām visus iespējamos gadījumus, kādus atlikumus var dot trīs izvēlētie skaitli.

1) Ja kāds no skaitliem dalās ar 4 (jeb dod atlikumu 0), tad šī skaitḷa reizinājums ar pārējiem diviem skaitḷiem arī dalās ar 4 jeb šie divi reizinājumi dod atlikumu 0.
2) Ja neviens no skaitliem nedalās ar 4, tad iespējami divi gadījumi.

a) Ja vismaz diviem skaitḷiem atlikums, dalot ar 4, ir vienāds, tas ir, skaitlus varam izteikt formā $4 k+q ; 4 m+q$ un $4 n+p$, tad reizinājumiem $(4 k+q)(4 n+p)=4(4 k n+k p+n q)+q p$ un $(4 m+q)(4 n+p)=4(4 m n+m p+n q)+q p$ atlikums ir vienāds ar $q p$ atlikumu, dalot ar 4 .

b) Ja visi atlikumi ir dažādi, tad viena skaitla atlikums, dalot ar 4, ir 1, otra - 2, trešā-3, tas ir, skaitlus varam izteikt formā $4 k+1 ; 4 m+2$ un $4 n+3$. Tad reizinājuma
$(4 k+1)(4 m+2)=4(4 k m+2 k+m)+2$ atlikums ir vienāds ar reizinājuma $(4 m+2)(4 n+3)=4(4 m n+3 m+2 n+4)+2$ atlikumu, tas ir, ir vienāds ar 2 .

Esam aplūkojuši visus gadījumus un prasītais pierādīts.

9.3. Rūtiṇu tabulas ar izmēriem $8 \times 14$ katrā rūtinā sēž tieši viena muša. Visas mušas pārlido uz citu tabulu ar izmēriem $7 \times 16$ rūtinas tā, ka katrā rūtiṇā atkal ir tieši viena muša. Vai iespējams, ka visas mušas, kas bija kaimiṇi sākotnējā izvietojumā (tas ir, atradās blakus rūtinās ar kopīgu malu), būs kaimiṇi arī jaunajā izvietojumā?

1. atrisinājums. Pamatosim, ka prasītais nav iespējams. Pieṇemsim, ka mušas ir pārlidojušas tā, ka visas, kas bija kaiminos pirms pārlidošanas, ir kaimiṇos arī pēc tās. levērojam, ka stūra rūtinā (skat. 1. att. melnās rūtiṇas) sēdošai mušai ir tieši 2 kaimiṇi, malējā rūtinā (pelēkās rūtiṇas) - tieši 3 kaimiṇi un vidējā rūtiṇā (baltās rūtiṇas) - tieši 4 kaimiṇi. Skaidrs, ka katrai mušai kaiminu skaits nemainās vai palielinās (ja tas samazinātos, tad kādu no kaimiṇiem tā būtu pazaudējusi). Tātad stūra rūtiṇās, kurās mušām ir tikai divi kaimiṇi, var ielidot tikai mušas, kas arī pirms tam bijušas stūros. Tabulā ar izmēriem $8 \times 14$ rūtinas ir 36 malējās rūtiṇas, bet tabulai ar izmēriem $7 \times 16$ ir 38 malējās rūtinas. Tā kā abās tabulās ir vienāds rūtinu skaits, tad divas malējās rūtiṇas būs jāaizṇem mušām, kuras atradās sākotnējās tabulas vidējās rūtinās, bet tad tās būtu pazaudējušas vismaz vienu kaimiṇu, kas ir pretrunā ar pienēmumu.
2. atrisinājums. Pamatosim, ka prasītais nav iespējams. Saskaitīsim, cik mušu pāri bija kaimiņi pirms un pēc pārlidošanas. Kaimiṇu katrā tabulā ir tieši tik, cik ir iekšējo līniju, katra iekšējā līnija atdala divas kaiminuu mušas. Tātad pirms pārlidošanas kaimiṇu skaits bija $7 \cdot 14+8 \cdot 13=202$, bet pēc pārlidošanas tas ir $6 \cdot 16+7 \cdot 15=201$, tātad ir vismaz viens mušu pāris, kas bija kaimiṇi pirms pārlidošanas, bet nav kaimiṇi pēc.

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-2.jpg?height=222&width=380&top_left_y=1094&top_left_x=838)

9.4. Dots vienādsānu trijstūris $A B C$, kuram $A C=6$ un $A B=B C=5$. Uz malas $A B$ atlikts tāds punkts $D$, ka $B D=2$, un uz malas $A C$ atlikts tāds punkts $E$, ka $A E=2$. Nogriežṇi $B E$ un $C D$ krustojas punktā $M$. Aprēkināt trijstūra $B M C$ laukumu!

1. atrisinājums. Novelkam trijstūrī $A B C$ augstumu $B H$ (skat. 2. att.). Tā kā $B H$ ir arī mediāna, tad $H C=\frac{1}{2} A C=3$, un pēc Pitagora teorēmas $\triangle B H C \quad$ aprēkinām $\quad B H=\sqrt{B C^{2}-H C^{2}}=4$. Tad $S_{A B C}=\frac{1}{2} B H \cdot A C=12$. Tā kā trijstūriem $B C D$ un $D C A$ ir kopīgs augstums no virsotnes $C$, tad $S_{B D C}=\frac{2}{5} S_{A B C}=\frac{24}{5}$ un $S_{A D C}=\frac{3}{5} S_{A B C}=\frac{36}{5}$. legūstam, ka $h_{A C}=\frac{2 S_{A D C}}{A C}=\frac{12}{5}$, kur $h_{A C}$ ir no virsotnes $D$ vilktais augstums. Aprēkinām $S_{D E C}=\frac{1}{2} E C \cdot h_{A C}=\frac{24}{5}$. Tātad $S_{D E C}=S_{B D C}$. Tas nozīmē, ka augstums no $B$ pret $C D$ ir vienāds ar augstumu no $E$ pret $C D$, no kā izriet, ka trijstūru $B M C$ un $E M C$ laukumi ir vienādi. Tātad $S_{B M C}=\frac{1}{2} S_{B E C}=\frac{1}{2} \cdot 4 \cdot \frac{4}{2}=4$.
![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-2.jpg?height=478&width=1676&top_left_y=1908&top_left_x=226)
2. atrisinājums. Novelkam trijstūrī $A B C$ augstumu $B H$ (skat. 3. att.). Tā kā $B H$ ir arī mediāna, tad $H C=\frac{1}{2} A C=3$, un pēc Pitagora teorēmas $\triangle B H C$ aprēkinām $B H=\sqrt{B C^{2}-H C^{2}}=4$. Tad $S_{B E C}=\frac{1}{2} E C$. $B H=\frac{1}{2} \cdot 4 \cdot 4=8$. Novelkam $E K \| A B$, kur punkts $K$ atrodas uz $C D$ (skat. 4. att.). Tad $\triangle A C D \sim \triangle E C K$, jo $E K \| A D$. Tad $\frac{E K}{A D}=\frac{E C}{A C}$ jeb $\frac{E K}{3}=\frac{4}{6}$ no kā izriet, ka $E K=2$. Tā kā $\Varangle D B M=\Varangle K E M$ un $\Varangle B D M=\Varangle E K M$ kā iekšējie škeērsleṇki pie paralēlām taisnēm un $B D=E K=2$, tad $\triangle D M B=\Delta K M E$ pēc pazīmes $\ell m \ell$. Tā kā
$B M=M E$ kā atbilstošās malas vienādos trijstūros un trijstūriem $B M C$ un $M E C$ sakrīt augstums, $\operatorname{tad} S_{B M C}=S_{M E C}=\frac{1}{2} S_{B E C}=\frac{1}{2} \cdot 8=4$.

9.5. Rindā izvietotas 2018 monētas. Vienā gājienā drīkst paṇemt vienu monētu, pārcelt to pāri tieši divām monētām un uzlikt to uz nākamās monētas. Vai 1009 gājienos visas monētas iespējams savākt kaudzītēs pa divām monētām katrā kaudzītē?
![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-3.jpg?height=194&width=892&top_left_y=417&top_left_x=590)

Atrisinājums. Pamatosim, ka prasītais ir iespējams. Ja ir 10 monētas vai 8 monētas, tad attiecīgi ar 5 vai 4 gājieniem tās var savākt kaudzītēs pa divām monētām katrā kaudzītē, skat., piemēram, 6. att. un 7. att. Tā kā $2018=201 \cdot 10+8$, tad ar $201 \cdot 5+4=1009$ gājieniem monētas iespējams savākt kaudzītēs pa divām monētām katrā kaudzītē.
![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-3.jpg?height=484&width=1396&top_left_y=820&top_left_x=316)

## 10. klase

10.1. Atrast visus tādus veselu skaitlu pārus $(x ; y)$, kas apmierina nevienādību sistēmu

$$
\left\{\begin{aligned}
& 2 x^{2}+2 y^{2}+24 x-28 y+167<0 \\
& x+2 y<\frac{15}{2}
\end{aligned}\right.
$$

Atrisinājums. Pārveidojam sistēmas pirmo nevienādību

$$
\begin{gathered}
2\left(x^{2}+12 x+36\right)+2\left(y^{2}-14 y+49\right)-3<0 \\
(x+6)^{2}+(y-7)^{2}<\frac{3}{2}
\end{gathered}
$$

Skaitḷa kvadrāts ir nenegatīvs. Ja divu nenegatīvu veselu skaitlu summa ir mazāka nekā $\frac{3}{2}$, tad šie skaitli var būt tikai $(0 ; 0),(1 ; 0)$ vai $(0 ; 1)$.

| $(\boldsymbol{x}+\mathbf{6})^{2}$ | $(\boldsymbol{y}-7)^{2}$ | $\boldsymbol{x}$ | $\boldsymbol{y}$ | $\boldsymbol{x}+\mathbf{2 y}$ |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | -6 | 7 | $-6+14=8>\frac{15}{2}$ | neder |
| 0 | 1 | -6 | 8 | $-6+16=10>\frac{15}{2}$ | neder |
| 0 | 1 | -6 | 6 | $-6+12=6<\frac{15}{2}$ |  |
| 1 | 0 | -5 | 7 | $-5+14=9>\frac{15}{2}$ | neder |
| 1 | 0 | -7 | 7 | $-7+14=7<\frac{15}{2}$ |  |

Līdz ar to dotajai sistēmai ir divi atrisinājumi $(-6 ; 6)$ un $(-7 ; 7)$.

10.2. Paralelograma $A B C D$ malu $B C$ un $C D$ viduspunkti attiecīgi ir $K$ un $M$. Aprēkināt $A D$ garumu, ja $A K=6, A M=$ 3 un $\Varangle K A M=60^{\circ}$.

Atrisinājums. Novelkam $K M, B D$ un ar $E$ apzīmējam $B D$ un $A M$ krustpunktu (skat. 8. att.). Uz stara $A M$ atliekam tādu punktu $A^{\prime}$, ka $A^{\prime} M=A M=3$, tad $A^{\prime} A K$ ir vienādmalu trijstūris, jo tas ir vienādsānu trijstūris, kura virsotnes leṇkis ir $60^{\circ}$, tātad abi pamata pielenki arī ir $60^{\circ}$. Tāpēc tā mediāna $K M$ ir arī augstums, tātad $\Varangle K M A=90^{\circ}$. Pēc Pitagora teorēmas iegūstam, ka $K M=3 \sqrt{3}$.

Nogrieznis $K M$ ir trijstūra $B C D$ viduslīijia, tāpēc $B D=2 K M=6 \sqrt{3}$ un $\Varangle M E B=90^{\circ}$.

Tā kā $\Varangle M E D=\Varangle A E B$ kā krustlenki un $\Varangle E M D=\Varangle E A B$ kā iekšējie škērslenki pie paralēlām taisnēm, tad $\triangle M E D \sim \triangle A E B$ pēc pazīmes $\ell \ell$ un $\frac{M E}{A E}=\frac{E D}{E B}=\frac{M D}{A B}=\frac{1}{2}$, no kā iegūstam $E D=\frac{1}{3} B D=2 \sqrt{3}$ un $A E=\frac{2}{3} A M=2$. Pēc Pitagora teorēmas $\triangle A E D$, iegūstam $A D=\sqrt{A E^{2}+E D^{2}}=\sqrt{4+12}=4$.

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-4.jpg?height=366&width=540&top_left_y=622&top_left_x=815)

Piezīme. Malas $K M$ garumu var aprēḳināt arī izmantojot kosinusu teorēmu trijstūrī $K A M$ :

$$
K M^{2}=A K^{2}+A M^{2}-2 \cdot A K \cdot A M \cdot \cos \Varangle K A M \quad \Rightarrow \quad K M=3 \sqrt{3}
$$

Pamatot, ka $\Varangle K M A=90^{\circ}$, var arī izmantojot Pitagora teorēmas apgriezto teorēmu, tas ir, tā kā $A K^{2}+K M^{2}=A M^{2}$, tad trijstūris $K A M$ ir taisnlenka.

10.3. Skait]us $a, b, c$ sauksim par skaistu trijnieku, ja tiem piemīt šādas īpašības:

- tie ir trīs pēc kārtas esoši naturāli skaitli;
- katrs no tiem dalās ar savu ciparu summu.

Piemēram, skaists trijnieks ir 8, 9, 10 .

a) Atrast tādu skaistu trijnieku, kurā mazākais skaitlis ir lielāks nekā 10.

b) Pierādīt, ka eksistē bezgalīgi daudz skaistu trijnieku!

Atrisinājums. a) Skaists trijnieks ir, piemēram, 110 (dalās ar 2), 111 (dalās ar 3), 112 (dalās ar 4).

b) Aplūkosim skait|us, ko iegūst no skaitliem 110, 111 un 112, aiz pirmā cipara ievietojot $n$ nul!u grupu:

$$
1 \underbrace{0 \ldots 0}_{n} 10 ; 1 \underbrace{0 \ldots 0}_{n} 11 ; 1 \underbrace{0 \ldots 0}_{n} 12
$$

legūtie skaitḷi joprojām ir secīgi. Pirmā skait|la ciparu summa ir 2, un tas dalās ar 2. Otrā skait|la ciparu summa ir 3, tātad tas dalās ar 3. Trešā skaitla ciparu summa ir 4 , un tas dalās ar 4, jo tā pēdējo divu ciparu veidotais skaitlis dalās ar 4. Tā kā $n$ var būt jebkurš naturāls skaitlis, tad skaistu trijnieku ir bezgalīgi daudz.

10.4. Desmit šahisti katrs ar katru izspēlēja vienu šaha partiju, dažas no tām beidzās neizškirti. Ir zināms, ka bija tieši viens šahists, kas neizškirti nospēlēja tieši vienu partiju, divi šahisti - kas nospēlēja divas, trīs šahisti - kas nospēlēja trīs, un četri šahisti, kas neizškirti nospēlēja tieši četras partijas. Šos pēdējos četrus šahistus (kas katrs četras partijas nospēlēja neiž̌kirti) sauksim par neizškirtu karaliem, bet par karalisku neizškirtu sauksim partiju, kurā neizškirtu izcīnija divi neizšǩirtu karali. Vai var apgalvot, ka tika izspēēts a) vismaz viens karaliskais neizšǩrts, b) vismaz divi karaliskie neiž̌kirti?

Atrisinājums. Šahistus apzīmējam ar punktiem. Ja divi šahisti spēlējuši neiž̌kirti viens ar otru, tad atbilstošos punktus savienojam ar līiju. Tad, atbilstoši uzdevuma nosacijumiem, no katra punkta iziet tik līiiju, cik parādīts 9 . att.

a) No punktiem $A, B, C$ un $D$ (skat. 9. att.) kopā iziet 16 līiju gali, bet no sešiem atlikušajiem punktiem kopā iziet 14 līniju gali. Tātad nevar būt tā, ka punkti $A, B, C$ un $D$ ir savienoti tikai ar atlikušajiem sešiem punktiem un nav savienoti savā starpā. Tātad esam ieguvuši, ka no tiem šahistiem, kas neizšķirti spēējuši tieši četras reizes, noteikti ir tādi divi, kas spēlējuši viens ar otru, tas ir, noteikti tika izspēlēts vismaz viens karaliskais neizškirts.

b) Nē, skat., piemēram, 10. att.

$$
\begin{aligned}
& \begin{array}{ccc}
A \\
\hline
\end{array} \\
& \circ \gamma \gamma \gamma \gamma \\
& \text { 9. att. }
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-4.jpg?height=174&width=351&top_left_y=2500&top_left_x=1338)

10. att.

10.5. Izvēlēti 12 dažādi naturāli skaitlli, neviens no tiem nepārsniedz 35 . Pierādīt, ka no šiem skaitlliem iespējams izvē̄ēties trīs atškirīgus skaitlu pārus tā, ka visiem trīs pāriem lielākā un mazākā skaitla starpība ir vienāda! Viens skaitlis var ietilpt arī divos pāros (vienreiz kā lielākais, otrreiz - kā mazākais).

Atrisinājums. Pienemsim pretējo, ka eksistē tāds 12 skait|u komplekts, kur visas starpības starp skaitliem atkārtojas ne vairāk kā divas reizes.

levērojam, ka 12 skaitli kopā veido $12 \cdot 11: 2=66$ starpības, tām iespējamas 34 dažādas vērtības: no 1 līdz 34. Ja kādu no vērtībām starpības vispār nepienem, tad katrai no pārējām starpībām jāparādās tieši divas reizes. Tāpat redzams, ja kādas divas vērtības tiek pienemtas tikai vienu reizi, tad visas pārējās jāpieṇem tieši divas reizes. Nav iespējams, ka trīs vērtības tiek pieṇemtas tikai vienu reizi, tāpat nav iespējams, ka kāda vērtība netiek pieṇemta un kāda cita tiek pienemta tikai vienu reizi.

levērosim, ja mēs katru no tiem (apzīmēsim ar $x$ ) aizstājam ar $36-x$, tad arī šis jauniegūtais skait|u komplekts atbilst visām prasībām: visi skaitḷi ir intervālà [1; 35] un to starpības ir tieši tās pašas. Šo simetrijas īpašību izmantosim, lai samazinātu aplūkojamo gadīumu skaitu.

levērojam, ka starpību

- 34 var iegūt tikai vienā veidā $34=35-1$;
- 33 var iegūt tikai 2 veidos $33=35-2=34-1$;
- 32 var iegūt tikai 3 veidos $32=35-3=34-2=33-1$;
- 31 var iegūt tikai 4 veidos $31=35-4=34-3=33-2=32-1$.

Pienemsim, ka šādi 12 skaitlli ir atrasti.

Starpību 34 var iegūt tikai no skaitljiem 1 un 35, starpību 33 tikai no skaitlu pāriem (2; 35) un (1; 34). Tas nozīmē, ja nav izvēlēts 1 vai 35 , tad mums nav neviena starpība 34 un ir lielākais viena starpība 33 , kas nav iespējams. Tātad noteikti ir izvēlēti abi skaitli 1 un 35 . Ja nav izvēēēts ne 2 , ne 34 , tad mums ir viena starpība 34 un neviena starpība 33 , kas nav iespējams. Tātad viens no skaitllem 2 vai 34 noteikti ir izvēlēts, augstākminētās simetrijas pēc pienemsim, ka tas ir 2. Tālāk aplūkojam iespējamos gadījumus.

1. Skaitlis 3 ir izvēlēts (kopā ar 35; 1 un 2). Tad 34 noteikti nav izvēlēts, citādi mums būtu trīs starpības 1 $(35-34=3-2=2-1=1$ ). Tad 33 noteikti ir izvēlēts, citādi mums būtu tikai viena starpība 34 , viena 33 un viena 32 (ko var iegūt tikai 3 veidos $35-3=34-2=33-1=32$ ).

Ja mums ir izvēēēti skaitḷi $1,2,3,33,35$, tad noteikti nav izvēēēti 4 un 32 , jo citādi mums būtu vairāk nekā divas starpības 1. Tas nozīmē, ka mums ir tikai viena starpība 31 (jo nav ne 2, ne 4, ne 32), kas kopā ar to, ka mums ir tikai viena starpība 33 un viena starpība 34 dod pretrunu.

2. Skaitlis 3 nav izvēlēts. Tad 34 ir izvēlēts, jo pretējā gadijumā mums būtu tikai viena starpība 32 (ja ne 3, ne 34 nav) viena 33 un viena 34. Tātad mums ir izvēlēti skaitli 1 1, 2,34, 35, kas nozīmē, ka nav ne 3, ne 33, lai nebūtu vairāk kā divas starpības 1. Tas nozīmē, ka mums jau ir tikai viena starpība 34 un tikai viena starpība 32, kas nozīmē, ka visām pārējām starpībām jābūt pieṇemtām tieši divreiz. Tātad 4 un 32 noteikti ir izvēē̄ti, lai varētu iegūt divas starpības 31. No tā, ka mums ir izvēlēti 1, 2, 4, 32, 34, 35 (un nav 3 un 33) seko, ka mums noteikti nav izvē̄ēti $5,6,30$ un 31 , lai nebūtu par daudz starpību 1 vai 2 . Bet tas savukārt nozīmè, ka mums nav nevienas starpības 29 (ko var iegūt tikai 6 veidos: kā $35-6=34-5=33-4=32-3=$ $=31-2=30-1=29$ ), kas kopā ar to, ka mums ir tikai viena starpība 34 dod pretrunu.

## 11. klase

11.1. Atrisināt nevienādību ||$|x-2|-3|-7|<5$.

1. atrisinājums. Tā kā modula vērtība ir mazāka nekā 5 , tad

$$
-5<|| x-2|-3|-7<5 \text { jeb } 2<|| x-2|-3|<12
$$

lespējami divi gadijumi:

1) $2<|x-2|-3<12$ jeb $5<|x-2|<15$ un atkal iespējami divi gadijumi
a) $5<x-2<15$ jeb $7<x<17$;
b) $-15<x-2<-5$ jeb $-13<x<-3$;
2) $-12<|x-2|-3<-2$ jeb $-9<|x-2|<1$ un tā kā modulis ir nenegatīvs, tad $-1<x-2<1$ jeb $1<x<3$.
2. atrisinājums. Doto nevienādību var atrisināt, pakāpeniski veidojot funkciju $y=|x-2|, y=|x-2|-3$, $y=|| x-2|-3|, y=|| x-2|-3|-7, y=|||x-2|-3|-7|$ grafikus, ievērojot, ka funkcijas

- $y=f(x)-a$, kur $a>0$, grafiku iegūst, funkcijas $y=f(x)$ grafiku pārbīdot paralēli $O y$ asij par $a$ vienībām uz leju;
- $y=|f(x)|$ grafiku iegūst, nemainot to grafika $y=f(x)$ daḷu, kur $f(x) \geq 0$, un to grafika dalu, kur $f(x)<0$, attēlojot simetriski attiecībā pret $O x$ asi.

Rezultāāā iegūst 11. att. doto grafiku. Atbildi nolasa no grafika, atrodot krustpunktus ar taisni $y=5$ un izvēloties tos intervālus, kur grafiks atrodas zem taisnes $y=5$. Līdz ar to $x \in(-13 ;-3) \cup(1 ; 3) \cup(7 ; 17)$.

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-6.jpg?height=477&width=1608&top_left_y=390&top_left_x=224)

11.2. Vienādsānu trijstūrī $A B C$ no pamata $B C$ viduspunkta $H$ novilkts perpendikuls $H E$ pret sānu malu $A C$, punkts $O$ ir nogriežṇa $H E$ viduspunkts. Pierādīt, ka $A O \perp B E$ !

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-6.jpg?height=431&width=552&top_left_y=1001&top_left_x=752)

Atrisinājums. Vienādsānu trijstūrī mediāna, kas vilkta no virsotnes, ir arī augstums un bisektrise. Tāpēc $A H \perp B C$ un $\Varangle B A H=\Varangle H A C$, no kā izriet, ka $\triangle B H A \sim \triangle H E A$ pēc pazīmes $\ell \ell$ (skat. 12. att.). Trijstūrī $B A H$ novelkam mediānu $A F$. No sakarībām līdzīgos trijstūros ( $A F$ un $A O$ ir atbilstošās mediānas) secinām, ka $\Varangle F A H=\Varangle O A E$ un $\frac{A F}{A H}=\frac{A O}{A E}$. Tā kā $\Varangle F A O=\Varangle F A H+\Varangle H A O=\Varangle O A E+\Varangle H A O=\Varangle H A E$, tad $\triangle F O A \sim \triangle H E A$ pēc pazīmes m \ell m . Tātad $\Varangle F O A=90^{\circ}$. Bet $B E \| O F$, jo $F O$ ir $\triangle B H E$ viduslīijia. Tāpēc $B E \perp A O$.

11.3. Skaitus $a, b, c, d, e$ sauksim par skaistu piecinieku, ja tiem piemīt šādas īpašības:

- tie ir pieci pēc kārtas esoši naturāli skaitli;
- katrs no tiem dalās ar savu ciparu summu.

Piemēram, skaists piecinieks ir $6,7,8,9,10$.

a) Atrast tādu skaistu piecinieku, kurā mazākais skaitlis ir lielāks nekā 10 .

b) Pierādīt, ka eksistē bezgalīi daudz skaistu piecinieku!

Atrisinājums. a) Skaists piecinieks ir, piemēram,

- 27027024 - ciparu summa ir 24; tā kā šis skaitlis dalās ar 3 (jo ciparu summa dalās ar 3) un 8 (jo pēdējo trīs ciparu veidotais skaitlis dalās ar 8), tad tas dalās ar 24;
- 27027025 - ciparu summa ir 25 ; tā kā pēdējo divu ciparu veidotais skaitlis dalās ar 25 , tad arī pats skaitlis dalās ar 25 ;
- 27027026 - ciparu summa ir 26 un $27027026=26 \cdot 10392501$;
- 27027027 - ciparu summa ir 27 un $27027027=27 \cdot 1001001$;
- 27027028 - ciparu summa ir 28 un $27027028=28 \cdot 965251$.

b) Aplūkosim skait|us, ko iegūst no skaitliem 27027024, 27027025, 27027026, 27027027 un 27027028, pirms pēdējiem diviem cipariem ievietojot $n$ nulllu grupu:

$$
27027 \underbrace{0 \ldots 0}_{n} 24 ; 27027 \underbrace{0 \ldots 0}_{n} 25 ; 27027 \underbrace{0 \ldots 0}_{n} 26 ; 27027 \underbrace{0 \ldots 0}_{n} 27 ; 27027 \underbrace{0 \ldots 0}_{n} 28
$$

legūtie skaitlli joprojām ir secīgi un tā kā tika pievienotas tikai nulles, tad ciparu summa nemainās, tas ir, ciparu summas attiecīgi ir $24,25,26,27$ un 28 . Katru no šiem skaitliem var uzrakstì formā $27027 \cdot 10^{n+2}+x$, kur $x=24,25,26,27,28$. Pamatosim, ka šie skaitḷi dalās ar savu ciparu summu. levērojam, ka
$27027 \cdot 10^{n+2}+x=27 \cdot 1001 \cdot 10^{3} \cdot 10^{n-1}+x=2^{3} \cdot 3^{3} \cdot 5^{3} \cdot 7 \cdot 11 \cdot 13 \cdot 10^{n-1}+x \quad$ un $\quad$ ka pirmais saskaitāmais dalās ar visām iespējamām $x$ vērtībām, tas ir, ar $24,25,26,27$ un 28 . Tā kā abi saskaitāmie dalās ar $x$, tad arī pats skaitlis dalās ar $x$.

Tā kā $n$ var būt jebkurš naturāls skaitlis, tad skaistu piecinieku ir bezgalīgi daudz.

11.4. Atrisināt vienādojumu sistēmu reālos skaitlos

$$
\left\{\begin{array}{l}
x^{3}+4 x=5 y \\
y^{3}+4 y=5 z \\
z^{3}+4 z=5 x
\end{array}\right.
$$

Atrisinājums. Dotās sistēmas atrisinājumi ir $(0 ; 0 ; 0) ;(1 ; 1 ; 1)$ un $(-1 ;-1 ;-1)$. Pierādīsim, ka citu atrisinājumu nav. Tā kā vienādojums ir simetrisks attiecībā pret mainīgo rotāciju, tad nezaudējot vispārīgumu, varam pienemt, ka $x \geq y$ un $x \geq z$. Funkcija $f(a)=a^{3}+4 a$ ir stingri augoša visā savā definícijas apgabalā, kā divu augošu funkciju summa ( $a^{3}$ un $4 a$ ), tātad, ja $x \geq y$, tad no sistēmas pirmā un otrā vienādojuma iegūst, ka $x^{3}+4 x \geq y^{3}+4 y$ jeb $5 y \geq 5 z$, no kā izriet, ka $y \geq z$. Savukārt no $y \geq z$ tieši tādā pašā veidā, izmantojot sistēmas otro un trešo vienādojumu, iegūst, ka $z \geq x$. Tātad $x \geq y \geq z \geq x$, no kā seko, ka $x=y=z$. levietojot šo sistēmas pirmajā vienādojumā, iegūst $x^{3}+4 x=5 x$ jeb $x^{3}-x=0$, tātad $x_{1}=-1, x_{2}=0$, $x_{3}=1$. Pārbaude apstiprina, ka $x=y=z=-1, x=y=z=0$ un $x=y=z=1$ patiešām der kā šīs vienādojumu sistēmas atrisinājumi.

11.5. Trīs 500 litru mucās atrodas attiecīgi 100, 107 un 113 litri ūdens. Vienā gājienā at!auts jebkurā mucā $M$ pieliet klāt no jebkuras citas mucas (kurā ir vismaz tikpat daudz ūdens kā mucā $M$ ) tik daudz ūdens, cik mucā $M$ jau atrodas. Vai, veicot šādus gājienus, iespējams iztukšot a) vienu mucu, b) divas mucas?

Atrisinājums. a) Vienu mucu ir iespējams iztukšot, skat., piemēram, tālāk dotajā tabulā

| 100 | 107 | 113 |
| :---: | :---: | :---: |
| 100 | $107+107=214$ | $113-107=6$ |
| $100+100=200$ | $214-100=114$ | 6 |
| 200 | $114-6=108$ | $6+6=12$ |
| 200 | $108-12=96$ | $12+12=24$ |
| $200-24=176$ | 96 | $24+24=48$ |
| $176-48=128$ | 96 | $48+48=96$ |
| 128 | 0 | 192 |

b) Pamatosim, ka divas mucas nav iespējams iztukšot. levērojam, ka kopējais ūdens daudzums ir 320 litru, tātad pēdējā gājiena rezultātam (ar precizitāti līdz mucu sakārtojumam), jābūt ( $320 ; 0 ; 0$ ), tātad beigās katrā mucā esošajam ūdens daudzums būtu jādalās ar 5 .

Aplūkosim patvalịgu soli, pēc kura ūdens daudzums visās mucās dalās ar 5, simetrijas pēc pieṇemsim, ka šajā solī no pirmās mucas ūdens tika pārliets otrajā, tātad tas bija $(x ; y ; z) \rightarrow(x-y ; 2 y ; z)$ un visi trīs skaitḷi $x-y, 2 y$ un $z$ dalās ar 5. No tā, ka $2 y$ dalās ar 5, izriet, ka $y$ dalās ar 5 (jo 2 un 5 ir savstarpēji pirmskaitli) un no tā, ka $x-y$ dalās ar 5 un $y$ dalās ar 5, izriet, ka $(x-y)+y=x$ dalās ar 5. Tātad gan $x$, gan $y$, gan $z$ dalās ar 5 , tātad, ja pēc kāda soḷa visās mucās ūdens daudzums dalās ar 5 , tad arī pirms šī soḷa tas ir dalījies ar 5. Tā kā sākotnējais ūdens daudzums ne visās mucās dalās ar 5, tad skaidrs, ka no tā nav iespējams iegūt situāciju, kad visās mucās ūdens daudzums dalās ar 5 .

## 12. klase

12.1. Apzīmēsim $a=2018^{\lg (\lg 2018)}, b=(\lg 2018)^{\lg 2018}$ un $c=(\lg (\lg 2018))^{2018}$. Aprēkināt izteiksmes $\frac{a-b}{c}+\frac{b-c}{a}+\frac{c-a}{b}$ vērtību!

Atrisinājums. Izmantojot logaritmu īpašību $m^{\log m}=t$, iegūstam, ka $x^{\lg y}=10^{\lg \left(y^{\lg x}\right)}=10^{\lg x \lg y}=y^{\lg x}$, tāpēc $a=2018^{\lg (\lg 2018)}=\lg 2018^{\lg 2018}=b$ (šeit $x=2018$ un $y=\lg 2018$ ). Līdz ar to

$$
\frac{a-b}{c}+\frac{b-c}{a}+\frac{c-a}{b}=0+\frac{a-c}{a}+\frac{c-a}{a}=0
$$

12.2. Uz trijstūra $A B C$ malas $A B$ atlikti punkti $D$ un $E$ tā, ka $A D=D E=E B$, uz malas $B C$ - punkti $F$ un $G$ tā, ka $B F=F G=G C$, uz malas $A C$ - punkts $H$ tā, ka $2 A H=C H$. Nogrieznis $D F$ krusto nogriežṇus $E H$ un $E G$ attiecīgi punktos $P$ un $R$. Pierādīt, ka $D P=P R=R F$.

Atrisinājums. Nogriežṇi $D F$ un $G E$ ir trijstūra $B D G$ mediānas (skat. 13. att.). Mediānas krustojoties tiek sadalítas attiecībā 2:1, skaitot no virsotnes, tāpēc $D R=2 R F$.

Novelkam $B R$, tas krusto $D G$ punktā $M$ un $A C$ punktā $J$. levērojam, ka $B M$ ir trijstūra $D B G$ mediāna (jo iet caur mediānu krustpunktu). Tā kā trijstūri $B D G$ un $B A C$ ir līdzīgi pēc pazīmes m \ell m , tad $\frac{B A}{B D}=\frac{A C}{D G}$ un $\Varangle B D G=\Varangle B A C$, tātad $D G \| A C$. Tā kā trijstūri $B D M$ un $B A J$ ir līdzīgi pēc pazīmes $\ell \ell$, tātad $\frac{A J}{D M}=\frac{B A}{B D}=\frac{A C}{G D}$, no kā varam secināt, ka $\frac{A J}{A C}=\frac{D M}{G D}=\frac{1}{2^{\prime}}$ tātad $B J$ ir trijstūra $B A C$ mediāna. Tā kā trijstūri $A E H$ un $A B J$ ir līdzīgi pēc pazīmes $m \ell m$, tad $\Varangle A E H=\Varangle A B J$ un tātad $E H \| B J$. Pēc Talesa teorēmas secinām, ka $D P=P R$.

Tā kā $D R=2 R F$ un $D P=P R$, tad $D P=P R=R F$.

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-8.jpg?height=436&width=445&top_left_y=553&top_left_x=814)

12.3. Atrisināt veselos skaitlos vienādojumu $x^{6}+3 x^{3}+1=y^{4}$.

Atrisinājums. Der skait|u pāri $(0 ; 1)$ un $(0 ;-1)$. Pierādīsim, ka citu atrisinājumu nav.

Apzīmējam $x^{3}=a, \operatorname{tad} y^{4}=a^{2}+3 a+1$.

Ja $a \geq 1$, tad $a^{2}+2 a+1<a^{2}+3 a+1<a^{2}+4 a+4$, tātad arī $(a+1)^{2}<y^{4}<(a+2)^{2}$, redzams, ka $y^{4}$ (kas ir naturāla skait|la kvadrāts) atrodas starp divu pēc kārtas esošu naturālu skait|u kvadrātiem - pretruna. Ja $a \leq-4$, tad $a^{2}+4 a+4<a^{2}+3 a+1<a^{2}+2 a+1$, tātad arī $(a+2)^{2}<y^{4}<(a+1)^{2}$ un, tieši tāpat kā iepriekš, iegūstam pretrunu, ka $y^{4}$ atrodas starp diviem pēc kārtas esošu skaitlu kvadrātiem.

Tātad $-3 \leq a \leq 0$. Tā kā $a=x^{3}$, tad $a=0$ vai $a=-1$.

Ja $a=0$, tad $x=0$, no kā izriet, ka $y= \pm 1$. Ja $a=-1$, tad $x=-1$, un iegūstam, ka $y^{4}=-1$, kam atrisinājuma nav. Tātad dotajam vienādojumam ir tikai divi atrisinājumi $(0 ; 1)$ un $(0 ;-1)$.

12.4. Taisnstūris, kura izmēri ir $n \times m$ rūtinas, griežot par rūtinuu līnijām, sagriezts $1 \times 6$ rūtinas lielos taisnstūros. Pierādīt, ka $n$ vai $m$ dalās ar 6 .

Atrisinājums. Sākotnējo rūtinu laukumu šaha veidā izkrāsosim $3 \times 3$ rūtinas lielos melnos un baltos kvadrātos (skat. 14. att.).

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-8.jpg?height=352&width=351&top_left_y=1800&top_left_x=424)

14. att.

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-8.jpg?height=363&width=728&top_left_y=1783&top_left_x=1144)

15. att.

Katrs $1 \times 6$ rūtinu taisnstūris, neatkarīgi no novietojuma laukumā, satur tieši trīs melnas un trīs baltas rūtinas. Tātad visi šādi taisnstūri kopā satur vienādu skaitu melno un balto rūtinu.

Pamatosim, ja ne $n$, ne $m$ nedalās ar 6, tad taisnstūrī $n \times m$ melno un balto rūtinu skaits nav vienāds, tas ir, šādu taisnstūri nevar sagriezt taisnstūros $1 \times 6$ rūtiṇas. Sadalām taisnstūri slejās, kuru platums ir 6 rūtiṇas (skat. 15. att.), tajās melno un balto rūtiṇu skaits ir vienāds. Labajā pusē noteikti atliek sleja, kuras platums ir mazāks nekā 6 rūtinas. Šo sleju sadalām joslās, kuru augstums ir 6 rūtiṇas, tajās melno un balto rūtinu skaits ir vienāds. Labā apakšējā stūrī paliek taisnstūris, kura augstums ir mazāks nekā 6 rūtinas. Līdz ar to nesadalīts paliek taisnstūris $a \times b$, kura malu garumi var būt no 1 līdz 5 rūtinām. Tā kā taisnstūris ir sagriezts taisnstūros $1 \times 6$, tad $a \cdot b$ dalās ar 6 un iespējami divi gadijumi $2 \times 3$ vai $4 \times 3$. Nevienā no šiem abiem taisnstūriem
melno un balto rūtinu skaits nav vienāds (skat. 16. att.). Tātad sākotnējā taisnstūrī melno un balto rūtiṇu skaits nav vienāds un to nevar sadalīt taisnstūros $1 \times 6$ rūtiṇas.

![](https://cdn.mathpix.com/cropped/2024_07_21_f9ba762c34c36a66a707g-9.jpg?height=222&width=490&top_left_y=203&top_left_x=840)

12.5. Trīs mucās attiecīgi ir $a, b$ un $c$ litri ūdens, kur $a, b, c$ ir naturāli skaitli. Katras mucas tilpums ir lielāks nekā $a+b+c$ litri. Vienā gājienā atlauts jebkurā mucā $M$ pieliet klāt no jebkuras citas mucas (kurā ir vismaz tikpat daudz ūdens kā mucā $M$ ) tik daudz ūdens, cik mucā $M$ jau atrodas. Pierādīt, ka, veicot šādus gājienus, vienmēr iespējams iztukšot vienu no mucām!

Atrisinājums. Apskatām mucu, kurā ir vismazāk ūdens. Parādīsim, kā kādā no pārējām mucām iegūt mazāk ūdens nekā šajā mucā. Tad skaidrs, ka, atkārtojot šo procesu, agrāk vai vēlāk kāda no mucām būs tukša.

Apzīmējam mucas ar $A$ (sākumā tajā ir a litri), $B$ ( $b$ litri) un $C$ (c litri) un, nezaudējot vispārīgumu, pieṇemam, ka $0<a \leq b \leq c$. Aplūkojam mucas $A$ un $B$.

Izsakām $b=a \cdot x+y$, kur $0 \leq y<a$, bet $x$ izsakām binārā formā:

$$
x=x_{0}+2 x_{1}+2^{2} x_{2}+2^{3} x_{3}+\cdots+2^{k} x_{k}
$$

kur $x_{i}$ ir vai nu 0 , vai 1 visiem $i=0,1, \ldots, k$.

Veiksim pārliešanas uz mucu $A$, izdarot $k+1$ gājienu (gājienus numurēsim no 0 līdz $k$ ):

- ja $x_{i}=1$, tad $i$-tajā gājienā pārlejam ūdeni no mucas $B$ mucā $A$;
- ja $x_{i}=0$, tad $i$-tajā gājienā pārlejam ūdeni no mucas $C$ mucā $A$.

Katrā gājienā ūdens daudzums mucā $A$ dubultojas un $i$-tajā gājienā mucā tiek ielieti $2^{i} a$ litri ūdens. Tā kā katram naturālam $m$ izpildās nevienādība $1+2+2^{2}+2^{3}+\cdots+2^{m-1}=\frac{1 \cdot\left(2^{m}-1\right)}{2-1}<2^{m}$, tad mucā $B$ pietiks ūdens, lai veiktu kārtējo gājienu neatkarīgi no tā, cik reizes veikta liešana no $C$ uz $A$.

Pat, ja no $B$ uz $A$ būs jāveic tikai viena - pēdējā liešana, no $C$ pārlietais ūdens daudzums nepārsniedz $a\left(1+2+2^{2}+2^{3}+\cdots+2^{k-1}\right)<a 2^{k} \leq b \leq c$, tātad mucā $C$ pietiks ūdens, lai veiktu nepieciešamos gājienus.

Ar aprakstītajiem gājieniem tiks panākts, ka mucā $B$ paliek $y$ litri ūdens, bet, tā kā $y<a$, tad tagad mucā $B$ ir mazāk ūdens nekā sākotnēji bija mucā $A$ (tas ir, tagad mucā $B$ ir vismazākais ūdens daudzums). Atkārtojot līdzīgas gājienu virknes, panāksim, ka kādā no mucām ūdens vairs nebūs.

