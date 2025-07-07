![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-1.jpg?height=233&width=1700&top_left_y=133&top_left_x=210)

I E G LD I J U M TAVĀ N A K O T N EE

# Latvijas 71. matemātikas olimpiādes 3. posma uzdevumi un atrisinājumi 

## 9.-12. klase

9.1. Dots, ka $a$ un $b$ ir kaut kādi reāli skaitḷi. Pierādīt, ka vismaz vienam no vienādojumiem

$$
\begin{aligned}
& x^{2}+2 a x+b=0 \\
& a x^{2}+2 b x+1=0 \\
& b x^{2}+2 x+a=0
\end{aligned}
$$

ir atrisinājums.

Atrisinājums. Pieṇemsim pretējo. Tad visiem diskriminantiem jābūt negatīviem, tas ir,

$$
a^{2}<b, \quad b^{2}<a, \quad 1<a b
$$

No pirmajām divām nevienādībām izriet, ka $a>0$ un $b>0$. Sareizinot pirmās divas nevienādības (to drīkst darīt, jo visas izteiksmes ir pozitīvas), iegūstam $a^{2} b^{2}<a b$. Izdalot abas nevienādības puses ar $a b>0$, iegūstam $a b<1$, kas ir pretrunā ar trešo nevienādību. Tātad pieṇēmums bija aplams, līdz ar to vismaz vienam vienādojumam ir atrisinājums.

9.2. Dots naturāls skaitlis $n$. Pierādīt, ka $4 n \times 4 n$ rūtiṇu tabulā var aizkrāsot $4 n^{2}$ rūtiṇas tā, ka katrā rindā un katrā kolonnā ir aizkrāsotas tieši $n$ rūtinas un nekādām divām aizkrāsotām rūtinām nav kopīgu punktu (tas ir, iekrāsotās rūtinas neatrodas blakus un nesaskaras pat ar stūriem).

Atrisinājums. Vispirms aplūkosim gadījumu, ja $n=1$. Tad $4 \times 4$ rūtiṇu tabulā rūtinas var aizkrāsot, kā parādīts 1. att. šis tabulas krāsojums atbilst visām prasībām.
![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-1.jpg?height=214&width=544&top_left_y=1774&top_left_x=298)

1. att.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-1.jpg?height=282&width=271&top_left_y=1710&top_left_x=965)

2. att.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-1.jpg?height=412&width=418&top_left_y=1577&top_left_x=1428)

3. att.

Ievērosim, ka, sadalot aizpildīto tabulu $2 \times 2$ rūtiṇas lielos kvadrātos, iegūsim vienādi aizpildītus $2 \times 2$ rūtiṇu kvadrātus, kas pagriezti attiecībā viens pret otru. Izmantojot šo ideju, veidosim tabulas aizpildījumu patvalīgai $n$ vērtībai.

Vispirms izveidosim $2 n \times 2 n$ rūtinu tabulu, kurā īpaši izdalīsim $(2 n-1) \times(2 n-1)$ kvadrātu, kam papildus ir viena tukša rinda un viena tukša kolonna. Šajā $(2 n-1) \times(2 n-1)$ kvadrātā aizkrāsosim $n$ rūtinas katrā otrajā rindā un kolonnā, katrā virzienā atstājot pa tukšai rūtiṇai starp iekrāsotajām (skat. 2. att., kur parādīts gadījums $n=3$ ).

Pagriežot šo kvadrātu un sakombinējot tā, kā $2 \times 2$ kvadrāti tika sakombinēti $4 \times 4$ tabulā, iegūstam nepieciešamo tabulas aizpildijumu (skat. 3. att.).

9.3. Atrast visus naturālu skait|u pārus $(m ; n)$, kuriem ir spēkā vienādība $m^{5}+5 n^{4}=81 m$.

Atrisinājums. Pārveidojam doto vienādību:

$$
\begin{gathered}
5 n^{4}=81 m-m^{5} \\
5 n^{4}=m\left(9+m^{2}\right)(3+m)(3-m)
\end{gathered}
$$

Tā kā $m$ un $n$ ir naturāli skaitli un iegūtās vienādības kreisās puses izteiksme ir pozitīva, tad $m=1$ vai $m=2$. Apskatām abus gadijumus:

- ja $m=1$, tad $5 n^{4}=1 \cdot 10 \cdot 4 \cdot 2$ jeb $n^{4}=16$, no kā iegūstam, ka $n=2$ (vērtība $n=-2$ neder, jo nav naturāls skaitlis);
- ja $m=2$, tad $5 n^{4}=2 \cdot 13 \cdot 5 \cdot 1$ jeb $n^{4}=26$, no kā iegūstam, ka naturālu atrisinājumu nav.

Līdz ar to esam ieguvuši, ka vienīgais derīgais skaitlu pāris ir $(1 ; 2)$.

9.4. Trijstūrī $A B C$ ievilktā rinka līnija pieskaras tā malām $A B, B C$ un $A C$ attiecīgi punktos $C_{1}, A_{1}$ un $B_{1}$. Taisne, kas vilkta caur punktu $A$ paralēli $B C$, un taisne $A_{1} C_{1}$ krustojas punktā $K$. Pierādīt, ka $\Varangle K B_{1} A_{1}=90^{\circ}$.

Atrisinājums. Trijstūris $C_{1} B A_{1}$ ir vienādsānu trijstūris (jo $B C_{1}=B A_{1}$ kā pieskaru nogriežṇi, kas vilkti no viena punkta), tāpēc $\Varangle B A_{1} C_{1}=\Varangle B C_{1} A_{1}$ (kā pamata pielenkị pie vienādajām malām). Līdz ar to

$$
\Varangle A K C_{1}=\Varangle B A_{1} C_{1}=\Varangle B C_{1} A_{1}=\Varangle A C_{1} K
$$

(pirmajā vienādībā ir iekšējie škērsleṇki, trešajā - krustleṇki, skat. 4. att.).

Tātad $\triangle K A C_{1}$ ir vienādsānu trijstūris (jo pamata pielenki ir vienādi) un $K A=A C_{1}$.

Tā kā $A C_{1}=A B_{1}$ kā pieskaru nogriežṇi, kas vilkti no viena punkta, tad arī $K A=A B_{1}$. Tātad $\triangle K A B_{1}$ ir vienādsānu trijstūris un $\Varangle K B_{1} A=\frac{180^{\circ}-\Varangle K A B_{1}}{2}$. Tā kā $A_{1} C=C B_{1}$, tad arī $\Varangle C B_{1} A_{1}=\frac{180^{\circ}-\Varangle B_{1} C A_{1}}{2}$. Tātad

$$
\Varangle K B_{1} A+\Varangle C B_{1} A_{1}=\frac{180^{\circ}-\Varangle K A B_{1}}{2}+\frac{180^{\circ}-\Varangle B_{1} C A_{1}}{2}=180^{\circ}-\frac{\Varangle K A B_{1}+\Varangle B_{1} C A_{1}}{2}=90^{\circ}
$$

jo $\Varangle K A B_{1}+\Varangle B_{1} C A_{1}=180^{\circ}$ kā iekšējie vienpusleṇki. Līdz ar to

$$
\Varangle K B_{1} A_{1}=180^{\circ}-\Varangle K B_{1} A-\Varangle C B_{1} A_{1}=180^{\circ}-90^{\circ}=90^{\circ}
$$

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-2.jpg?height=607&width=916&top_left_y=1567&top_left_x=648)
4. $a t t$.

9.5. Dotas 8 kastes, sākumā tās visas ir tukšas. Divi spēlētāji spēlē sekojošu spēli, pirmais spēētājs sāk. Vienā gājienā var izvēēēties jebkuras 7 kastes un katrā no tām ielikt vienu ābolu (āboli ir pieejami pietiekamā daudzumā). Uzvar tas spēlētājs, pēc kura gājiena kādā no kastēm ir tieši 15 āboli. Kurš spēlētājs - pirmais vai otrais - uzvarēs, pareizi spēlējot?

Atrisinājums. Pierādīsim, ka otrais spēlētājs vienmēr var uzvarēt.

Sanumurēsim kastes ar skaitliem no 1 līdz 8 un apzīmēsim gājienu ar tās kastes numuru, kurā ābols netiek ielikts. Piemēram, gājiens " 3 ", nozīmē, ka āboli tiek ielikti kastēs ar numuriem 1, 2, 4, 5, 6, 7, 8 .

Simetrijas dē! pieṇemsim, ka savā pirmajā gājienā pirmais spēlētājs veic gājienu " 1 ". Tad otrais spēlētājs savos pirmajos 7 gājienos neatkarīgi no tālākajiem pirmā spēēētāja gājieniem, var paiet gājienus " 2 ", " 3 ", " 4 ", “ 5 ", “ 6 ", " 7 ", " 8 ". Aplūkosim situāciju pirms otrā spēlētāja astotā gājiena.

Pirmā spēlētāja pirmais gājiens kopā ar otrā spēlētāja pirmajiem 7 gājieniem dod tieši 7 ābolus katrā kastē. Pirmais spēlētājs vēl ir pagājis 7 gājienus, tātad nevienā kastē nav vairāk kā 14 āboli, bet noteikti ir vismaz viena kaste, kurā ir tieši 14 āboli. Tajā tad savā 8. gājienā 2. spēlētājs var ielikt ābolu (kur likt pārējos 6 ābolus nav svarīgi) un uzvarēt.

10.1. Naturāls skaitlis $S$ ir izsakāms formā $S=9 n^{2}+42 n$, kur $n$ ir kāds naturāls skaitlis. Pierādīt, ka, ja $S$ pēdējais cipars ir 6, tad tā priekšpēdējais cipars ir 7 .

Atrisinājums. Aplūkosim skaitli $S+49=9 n^{2}+42 n+49=(3 n+7)^{2}$.

Ja $S$ beidzas ar 6 , tad $S+49$ beidzas ar 5 . Vesela skait|a, kas beidzas ar 5, kvadrāts beidzas ar 25 .

Tātad $S+49=\cdots 25$ un tas nozīmē, ka $S$ decimālais pieraksts beidzas ar 76 .

10.2. Dota ǵeometriskā progresija $x_{1} ; x_{2} ; x_{3} ; x_{4} ; x_{5} ; x_{6}$, kuras locekḷi ir pozitīvi skaitḷ. Zināms, ka $x_{4}+x_{3}-x_{2}-x_{1}=3$. Pierādīt, ka $x_{5}+x_{6} \geq 12$.

Piezīme. G eometriskā progresija ir skait|u virkne, kuras pirmais loceklis ir $x_{1}$ un katru nākamo virknes locekli iegūst, iepriekšēo reizinot ar kādu fiksētu skaitli $q$, tas ir, $x_{2}=q x_{1}, x_{3}=q x_{2}$ utt.

Atrisinājums. Apzīmēsim ǵeometriskās progresijas kvocientu ar $q$. levērojam, ka $q$ ir pozitīvs skaitlis un nav vienāds ar 1 (citādi progresija būtu konstanta un nevarētu izpildīties $x_{4}+x_{3}-x_{2}-x_{1}=3$ ).

No dotā izriet, ka

$$
\begin{gather*}
x_{1} q^{3}+x_{1} q^{2}-x_{1} q-x_{1}=3 \\
x_{1} \cdot\left(q^{3}+q^{2}-q-1\right)=3 \\
x_{1}\left(q^{2}(q+1)-(q+1)\right)=3 \\
x_{1}(q+1)\left(q^{2}-1\right)=3 \\
x_{1} \cdot(q+1)=\frac{3}{q^{2}-1} \tag{1}
\end{gather*}
$$

Mums jāpierāda, ka $x_{5}+x_{6}=x_{1}\left(q^{5}+q^{4}\right)=x_{1}(q+1) q^{4} \geq 12$ jeb $q^{4} \geq \frac{12}{x_{1} \cdot(q+1)}$. levietojot šajā nevienādībā (1), iegūstam, ka $q^{4} \geq 4 \cdot\left(q^{2}-1\right)$, kas ir patiesa nevienādība, jo $q^{4}-4 q^{2}+4=\left(q^{2}-2\right)^{2} \geq 0$.

10.3. Dota taisnleṇka trapece $A B C D$, tās pamati ir $A D$ un $B C$ un $A B \perp A D$. Uz malas $A B$ izvēlēts punkts $P$ tā, ka $\Varangle C P D=90^{\circ}$. Pierādīt, ka $B P=B C$ vai $B P=A D$, ja zināms, ka $A B=A D+B C$.

Atrisinājums. Aplūkosim divus punktus $P_{1}$ un $P_{2}$ uz malas $A B$ tā, ka $B P_{1}=B C$ un $B P_{2}=A D$ (skat. 5. att.). Tā kā trapeces pamati pēc definīcijas ir dažāda garuma, tad $P_{1}$ un $P_{2}$ ir atškirīgi punkti.

Tad $\Varangle C P_{1} D=90^{\circ}$, jo $\triangle B C P_{1}$ un $\triangle A D P_{1}$ ir vienādsānu taisnlenka trijstūri.

$\triangle B C P_{2}=\triangle A D P_{2}$, pēc pazīmes mlm , jo $\Varangle C B P_{2}=\Varangle P_{2} A D=90^{\circ}, B P_{2}=A D$ un $B C=A P_{2}$. Tātad arī $\Varangle C P_{2} D=90^{\circ}$ un ap četrstūri $P_{1} C D P_{2}$ var apvilkt riṇka līiju, kuras diametrs ir $C D$.

Bet riṇka līnija nogriezni var škērsot ne vairāk kā divos punktos, tāpēc uz malas $A B$ nav citu punktu, kam nogriežṇi uz $C$ un $D$ veido taisnu leṇki, līdz ar to $P$ sakrīt vai nu ar $P_{1}$, vai $P_{2}$. Tātad $B P=B C$ vai $B P=A D$.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-4.jpg?height=694&width=620&top_left_y=564&top_left_x=796)

10.4. Uz tāfeles sākumā uzrakstīts vienādojums $2019 x^{2}+2020 x+2021=0$. Divi spēlētāji pēc kārtas izdara gājienus, pirmais spēlētājs sāk. Vienā gājienā var izvēlēties jebkuru no trim koeficientiem vienādojuma kreisajā pusē (pie $x^{2}$, pie $x$ vai brīvo locekli) un no tā atṇemt vieninieku. Zaudē tas spēlētājs, pēc kura gājiena uz tāfeles uzrakstītajam vienādojumam ir kāda vesela sakne. Kurš spēlētājs - pirmais vai otrais - uzvarēs, pareizi spēlējot?

Atrisinājums. Pirmais spēlētājs vienmēr var uzvarēt. Pierādīsim to.

Vispirms parādīsim, kā pirmais spēēētājs var noteikti nezaudēt. Lai to izdarītu, vinam jānodrošina, ka koeficienti pie $x^{2}$ un $x$ ir ar vienādu paritāti, bet brīvais loceklis ir nepāra skaitlis. Tādā gadījumā izteiksmes vērtība vienādojuma kreisajā pusē būs nepāra skaitlis pie jebkādas $x$ vērtības, tātad tā nevarēs būt nulle. Savā pirmajā gājienā pirmais spēlētājs var koeficientu pie $x$ samazināt no 2020 uz 2019 un visos tālākajos gājienos rīkoties šādi: ja otrais spēlētājs samazina koeficientu pie brīvā locek!̣, tad to pašu dara arī pirmais spēlētājs, bet, ja otrais samazina koeficientu pie $x^{2}$ vai $x$, tad pirmais - attiecīgi pie $x$ vai $x^{2}$.

Atliek ievērot, ka spēle nevar turpināties bezgalīgi, jo noteikti pienāks brīdis, kad visu koeficientu summa būs vienāda $\operatorname{ar} 0$, un tātad $x=1$ būs vienādojuma sakne.

10.5. Taisnstūrveida tabulā, kurā ir 19 rindas un 14 kolonnas, ierakstīti kaut kādi reāli skait|li. Zināms, ka skait|u summa katrā 6. att. dotajā figūrā ir 1, turklāt šī figūra var būt pagriezta vai apmesta otrādi. Aprēkināt skaitlu summu pirmajā rindā!

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-5.jpg?height=133&width=307&top_left_y=270&top_left_x=909)

6. att.

Atrisinājums. levērosim, ka no divām 6. att. figūrām var salikt $2 \times 7$ rūtinu taisnstūri, skait|u summa šajā taisnstūrī ir 2. Visu tabulu $19 \times 14$ var noklāt ar šādiem 19 šādiem taisnstūriem (pirmās 7 rindas noklāj, liekot tos vertikāli, pārējās 12 rindas noklāj pa pāriem, liekot tos blakus horizontāli, skat. 7. att.), tātad skait|u summa visā tabulā ir 38 . Bet visu tabulu bez pirmās rindas var noklāt ar 18 šādiem taisnstūriem, liekot tos horizontāli (skat. 7. att.), tātad skaitlu summa šajā tabulas daḷā ir 36 . Tātad pirmās rindas skaitlu summa ir $38-36=2$.
![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-5.jpg?height=452&width=696&top_left_y=703&top_left_x=758)

7. att.

11.1. Pierādìt, ka $\sqrt[3]{6 \sqrt{3}+10}-\sqrt[3]{6 \sqrt{3}-10}=2$.

Atrisinājums. levērosim, $\mathrm{ka}(\sqrt{3}+1)^{3}=6 \sqrt{3}+10$ un $(\sqrt{3}-1)^{3}=6 \sqrt{3}-10$. Līdz ar to

$$
\sqrt[3]{6 \sqrt{3}+10}-\sqrt[3]{6 \sqrt{3}-10}=(\sqrt{3}+1)-(\sqrt{3}-1)=2
$$

11.2. Dota ǵeometriskā progresija $y_{1} ; y_{2} ; y_{3} ; y_{4} ; y_{5} ; y_{6}$, kuras locekḷi ir pozitīvi skaitli. Zināms, ka $y_{4}+y_{3}-y_{2}-y_{1}=15$. Kāda ir $y_{5}+y_{6}$ mazākā iespējamā vērtība?

Atrisinājums. Pierādīsim, ka $y_{5}+y_{6}$ mazākā iespējamā vērtība ir 60 .

Vispirms parādīsim, ka $y_{5}+y_{6} \geq 60$.

Apzīmēsim geometriskās progresijas kvocientu ar $q>1$. No dotā izriet, ka $y_{1} \cdot\left(q^{3}+q^{2}-q-1\right)=15$ jeb

$$
\begin{equation*}
y_{1} \cdot(q+1)=\frac{15}{q^{2}-1} \tag{1}
\end{equation*}
$$

Mums jāpierāda, ka $y_{1}\left(q^{5}+q^{4}\right) \geq 60$ jeb ka $q^{4} \geq \frac{60}{x_{1} \cdot(q+1)}$. levietojot šajā nevienādībā (1), regūstam, ka $q^{4} \geq 4 \cdot\left(q^{2}-1\right)$, kas ir patiesa nevienādība, jo $q^{4}-4 q^{2}+4=\left(q^{2}-2\right)^{2} \geq 0$.

Atliek parādīt, ka vērtība $y_{5}+y_{6}=60$ ir iegūstama. Lai tas tā būtu, visām nevienādībām ir jāklūst par vienādībām, tātad $q=\sqrt{2}$ un $y_{1} \cdot\left(\sqrt{2}^{3}+\sqrt{2}^{2}-\sqrt{2}-1\right)=15$ jeb $y_{1}=15(\sqrt{2}-1)$. Redzams, ka šajā gadījumā tik tiešām $y_{5}+y_{6}=y_{1}\left(q^{5}+q^{4}\right)=15(\sqrt{2}-1)(4 \sqrt{2}+4)=60$.

11.3. Naturālu skaitli sauksim par elegantu, ja tā decimālajā pierakstā nav nevienas nulles un šis skaitlis dalās ar savu ciparu summu. (Eleganti ir visi viencipara skaitli, kā arī, piemēram, skaitli 36 un 322.) Pierādīt, ka ir bezgalīgi daudz elegantu skait|u!

Atrisinājums. Apzīmēsim skaitla $x$ ciparu summu ar $S(x)$. Pierādīsim, ka, ja $A$ ir elegants, tad arī $\overline{A A A}$ (skaitlis, kas sastāv no trim pēc kārtas uzrakstītiem skaitliem $A$ ) ir elegants.

levērosim, ka, ja $A$ ir $n$-ciparu skaitlis, tad $\overline{A A A}=A \cdot\left(1+10^{n}+10^{2 n}\right)$ un $S(\overline{A A A})=3 S(A)$. Tā kā $A$ dalās ar $S(A)$ pēc pienēmuma, ka $A$ ir elegants, tad atliek pamatot, ka $1+10^{n}+10^{2 n}$ dalās ar 3, bet tas ir acīmredzami, jo tā ciparu summa ir 3 .

Šādā veid̄̄, sākot ar jebkuru elegantu skaitli (piemēram, 36), mēs varam iegūt bezgalīgu elegantu skaitlu virkni (36; 363636; 363636363636363636 utt.).

11.4. Izliektā četrstūrī $A B C D$ ir spēkā $\Varangle C B D=\Varangle C A B$ un $\Varangle A C D=\Varangle A D B$. Pierādīt, ka no nogriežniem $B C, A D, A C$ var salikt taisnlenka trijstūri!

Atrisinājums. Apzīmēsim $A C$ un $B D$ krustpunktu ar $O$ (skat. 8. att.).

Trijstūri $C B O$ un $C A B$ ir līdzīgi pēc pazīmes $\ell \ell$ ( $\Varangle B C A$ ir kopīgs un $\Varangle C A B=\Varangle C B O$ pēc dotā), tāpēc $\frac{C O}{B C}=\frac{B C}{A C}$ jeb $B C^{2}=C O \cdot A C$.

Tieši tāpat arī $\triangle A D O \sim \triangle A C B$ pēc pazīmes $\ell \ell$ ( $\Varangle C A D$ ir kopīgs un $\Varangle A D O=\Varangle A C D$ pēc dotā), tāpēc $\frac{A O}{A D}=\frac{A D}{A C}$ jeb $A D^{2}=A O \cdot A C$. Tāpēc

$$
B C^{2}+A D^{2}=C O \cdot A C+A O \cdot A C=A C \cdot(A O+C O)=A C^{2}
$$

un pēc apgrieztās Pitagora teorēmas izriet, ka no malām $B C$ un $A D$ kā katetēm un $A C$ kā hipotenūzas var salikt taisnleṇka trijstūri.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-6.jpg?height=347&width=434&top_left_y=1268&top_left_x=889)

8. att.

11.5. Dotam naturālam skaitlim $k>1$ torni būvē šādi: simetriski attiecībā pret vertikālu simetrijas asi pirmajā rindā blakus saliek $k$ kvadrātus, otrajā rindā saliek $(k-1)$ kvadrātu, trešajā rindā saliek $(k-2)$ kvadrātus utt. līdz $k$-ajā rindā liek vienu kvadrātu (skat. 9. att., kur parādīts tornis, ja $k=4$ ). No torṇa pirmās rindas kreisā malējā kvadrāta kreisās apakšējās virsotnes O novelk staru, kas torni sadala divās vienlielās figūrās. Pierādīt, ka bezgalīgi daudzām $k$ vērtībām šis stars iet caur kādas rindas labā malējā kvadrāta labo augšējo virsotni!

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-6.jpg?height=445&width=460&top_left_y=2011&top_left_x=838)

Atrisinājums. Pierādīsim, ka prasītais izpildās visām nepāra $k$ vērtīām $k=2 n-1$. Pievērsīsim uzmanību $n$-tajai kvadrātu rindai pēc kārtas un tās pēdējā kvadrāta labējai augšējai virsotnei.

Pieṇemsim, ka kvadrāta malas garums ir viena vienība. Aprēkināsim figūras laukuma dalu, kas atrodas zem stara $O P$ (skat. 10. att.). To veido trijstūra $O P R$ laukums un kvadrātu rindu galu "trepīte" (figūras daḷa pa labi no $P R$ ):

$$
\begin{gathered}
S_{O P R}=\frac{R O \cdot P R}{2}=\frac{\left(2 n-1-\frac{1}{2}(n-1)\right) \cdot n}{2}=\frac{(3 n-1) \cdot n}{4} \\
S_{\text {trepite }}=\frac{1}{2}\left(\frac{n(n-1)}{2}\right)=\frac{n(n-1)}{4} \\
S_{\text {ZemoP }}=\frac{(3 n-1) n}{4}+\frac{n(n-1)}{4}=\frac{n(2 n-1)}{2}
\end{gathered}
$$

Kopējais visas figūras laukums ir

$$
S_{v i s a}=1+2+\cdots+(2 n-1)=\frac{2 n(2 n-1)}{2}=n(2 n-1)
$$

Puse no $S_{\text {visa }}$ ir $\frac{n(2 n-1)}{2}$, kas sakrīt ar aprēkināto $S_{\text {zemoP }}$. Tātad, ja $k$ ir nepāra skaitlis, tad figūras laukumu vienlielās daḷās sadalošais stars iet caur kvadrāta virsotni.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-7.jpg?height=523&width=526&top_left_y=926&top_left_x=843)

10. att.

12.1. Pierādīt, ka kvadrātu var sagriezt sešos taisnstūros, kuriem visiem īsākās malas attiecība pret garāko ir $2-\sqrt{2}$.

Atrisinājums. Zīmējumā (skat. 11. att.) attēlots, kā var sagriezt kvadrātu, kura malas garums ir 4. Lielākajiem taisnstūriem īsākās malas attiecība pret garāko ir $\frac{2}{2+\sqrt{2}}=2-\sqrt{2}$, mazākajiem - arī tāda pati.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-7.jpg?height=482&width=567&top_left_y=1765&top_left_x=844)

11. att.

12.2. Doti reāli pozitīvi skait!i $x, y, z$. Pierādīt, ka

$$
\frac{x^{2}+y^{2}}{x+y}+\frac{y^{2}+z^{2}}{y+z}+\frac{z^{2}+x^{2}}{z+x} \geq x+y+z
$$

Atrisinājums. Vispirms pamatosim, ka patvalīgiem $x$ un $y$ ir spēkā $x^{2}+y^{2} \geq \frac{(x+y)^{2}}{2}$. Atverot iekavas un pārnest visu uz kreiso pusi, iegūstam

$$
x^{2}+y^{2}-\frac{(x+y)^{2}}{2}=x^{2}+y^{2}-\frac{1}{2}\left(x^{2}+2 x y+y^{2}\right)=\frac{1}{2}\left(x^{2}-2 x y+y^{2}\right)=\frac{(x-y)^{2}}{2} \geq 0
$$

Pielietojot šo visiem trim dalu skaitīājiem, iegūstam

$$
\frac{x^{2}+y^{2}}{x+y}+\frac{y^{2}+z^{2}}{y+z}+\frac{z^{2}+x^{2}}{z+x} \geq \frac{(x+y)^{2}}{2(x+y)}+\frac{(y+z)^{2}}{2(y+z)}+\frac{(z+x)^{2}}{2(z+x)}=x+y+z
$$

12.3. Agita ir iedomājusies naturālu skaitli $x$, kura ciparu summa ir 2021, un Konstantīns cenšas skaitli uzminēt. Vienā gājienā Konstantīns nosauc patvalīgu naturālu skaitli $a$, un Agita viṇam pasaka skait!a $|x-a|$ ciparu summu. Kāds ir mazākais gājienu skaits, ar kuru Konstantīnam noteikti pietiek, lai uzzinātu Agitas iedomāto skaitli?

Atrisinājums. Mazākais gājienu skaits ir 2021. Vispirms parādīsim, kā Konstantīns var atrast Agitas skaitli 2021 gājienā.

Pirmajā gājienā Konstantīns nosauc skaitli $a_{1}=1$. Ja Agitas skaitlis $x$ beidzas ar $k$ nullēm, tad vina Konstantīnam nosauc skaitli $2020+9 k$. Tādā veidā Konstantīns noskaidro, ar cik nullēm beidzas Agitas skaitlis. Apzīmēsim šo skaitu ar $k_{1}$ un tālāk aplūkosim skaitli $x_{1}=x-10^{k_{1}}$, kura ciparu summa ir 2020 .

Otrajā gājienā Konstantīns piemeklē skaitli $a_{2}$ tā, lai $x-a_{2}=x_{1}-1$ un līdzīgā veidā noskaidro, ar cik nullēm beidzas skaitlis $x_{1}$. Apzīmēsim šo skaitu ar $k_{2}$ un tālāk aplūkosim skaitli $x_{2}=x_{1}-10^{k_{2}}$, kura ciparu summa ir 2019 . Trešajā gājienā Konstantīns piemeklē skaitli $a_{3}$ tā, lai $x-a_{3}=x_{2}-1$ un līdz̄̄gā veidā noskaidro, ar cik nullēm beidzas skaitlis $x_{2}$. Apzīmēsim šo skaitu ar $k_{3}$ un tālāk aplūkosim skaitli $x_{3}=x_{2}-10^{k_{3}}$, kura ciparu summa ir 2018. Šādi Konstantīns turpina, līdz pēdējā solī tas iegūst, ka skaitlis $x_{2020}$, kura ciparu summa ir 1, beidzas ar $k_{2021}$ nullēm (tātad tas ir $x_{2020}=10^{k_{2021}}$ ).

Tātad Agitas iedomātais skaitlis ir $x=10^{k_{1}}+10^{k_{2}}+10^{k_{3}}+\cdots+10^{k_{2021}}$.

Atliek pamatot, ka ar mazāk gājieniem Konstantīns to izdarīt nevar. Pienemsim, ka Agita ir atzinusies Konstantīnam, ka vinas iedomātais skaitlis sastāv tikai no vieniniekiem un nullēm. Konstantīnam ir jānoskaidro tikai, kurās pozīcijās atrodas vieninieki. Tas ir, Agitas skaitlis ir izteikts formā $x=10^{k_{1}}+10^{k_{2}}+10^{k_{3}}+\cdots+10^{k_{2021}}$, kur $k_{1}<k_{2}<k_{3}<\cdots<k_{2021}$, un Konstantīnam ir jānoskaidro visas vērtības $k_{i}$. Bet, ja izrādās, ka $10^{k_{1}}>a_{1}$, tad ar savu pirmo minējumu Konstantīns neko nenoskaidro par pārējiem skaitliem $k_{2}, \ldots, k_{2021}$. Līdzīgi, ja $10^{k_{2}}>a_{2}$, tad ar savu otro minējumu Konstantīns neko nenoskaidro par atlikušajiem skaitlliem $k_{3}, \ldots, k_{2021}$. Līdzīgi turpinot, redzams, ka pat pēc 2020-ā minējuma Konstantīns vēl neko nevarēs pateikt par skaitli $k_{1}$, tas var atrasties jebkurā pozīcijā.

12.4. Vienādmalu trijstūra $A B C$ malas garums ir 15 . Uz malas $A B$ atlikts punkts $D$ tā, ka $A D=5$, bet uz malas $A C$ - punkts $E$ tā, ka $A E=3$. Pierādīt, ka nogriežṇi $B E$ un $C D$ ir perpendikulāri!

Atrisinājums. Caur $B E$ un $C D$ krustpunktu $O$ novelk nogriezni $A F$, kur $F$ atrodas uz $B C$ (skat. 12. att.). Pēc Čevas teorēmas $\frac{C F}{B F}=\frac{C E}{A E} \cdot \frac{A D}{D B}=2$ jeb $C F=10$ un $B F=5$. Tātad $\triangle B C D=\triangle A C F$ pēc pazīmes mlm. Attiecīgi $\Varangle B D C=\Varangle A F C$ un $\Varangle B D C+\Varangle A F B=180^{\circ}$, no kurienes izriet, ka četrstūrim $B D O F$ var apvilkt rinka līiju.

Aplūkosim trijstūri $B D F$. Tā malu garumi $B D=10, B F=5$ un $\Varangle D B F=60^{\circ}$. Tātad $B D F$ ir taisnlenka un ap $B D F$ apvilktās rinka līnijas rādiusi $B G=G D=G F=5$.

Ap $\triangle B D F$ apvilktā riṇka līnija vienlaikus ir arī ap $B D O F$ apvilktā ring̣a līnija.

Tā kā $\Varangle B O D$ balstās uz diametra, tad $\Varangle B O D=90^{\circ}$. Tātad $B E \perp C D$.

![](https://cdn.mathpix.com/cropped/2024_07_12_ac6caabe337027663316g-9.jpg?height=692&width=813&top_left_y=581&top_left_x=645)

12.5. Atrast visus veselu skaitlu pārus $(a ; b)$, kuriem

$$
(19 a+b)^{18}+(a+b)^{18}+(a+19 b)^{18}
$$

ir kāda vesela skait!a kvadrāts.

Atrisinājums. Vienīgais šāds pāris ir $(0 ; 0)$, kurš der, jo $0^{18}+0^{18}+0^{18}=0$. Pierādīsim, ka neviens cits pāris neder. Pieṇemsim, ka kāds skaitlu pāris $(a ; b)$ atbilst uzdevuma nosacijumiem. Ja gan $a$, gan $b$ dalās ar $19^{k}$, tad arī skaitlu pāris $\left(\frac{a}{19^{k}} ; \frac{b}{19^{k}}\right)$ atbilst uzdevuma nosacīumiem. Tādā veidā mēs varam iegūt jaunu skaitlu pāri $(a ; b)$, kurš atbilst uzdevuma nosacijumiem un kurā vismaz viens no skaitliem nedalās ar 19.

levērosim, ka pēc mazās Fermā teorēmas, ja $x$ nedalās ar $19, \operatorname{tad} x^{18}=1(\bmod 19)$. Tātad katrs no trim summas locekliem pēc modula 19 ir vai nu 0 , vai 1 . levērosim arī, ka, ja vismaz viens no skaitlliem $(a ; b)$ nedalās ar 19 , tad vismaz divi no trim skaitliem $19 a+b ; a+b ; a+19 b$ nedalās ar 19. Līdz ar to šīs summas vērtība pēc moduḷa 19 ir vai nu 2 , vai 3 .

Bet ne 2, ne 3 pēc moduḷa 19 nevar būt naturāla skaitla kvadrāts (pārbaude ar tabulu) - pretruna.

| $n(\bmod 19)$ | 0 | $\pm 1$ | $\pm 2$ | $\pm 3$ | $\pm 4$ | $\pm 5$ | $\pm 6$ | $\pm 7$ | $\pm 8$ | $\pm 9$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $n^{2}(\bmod 19)$ | 0 | 1 | 4 | 9 | 16 | 6 | 17 | 11 | 7 | 5 |

