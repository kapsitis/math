# <lo-sample/> PL.OMJ.2015TEST.7_8.1

Dane są takie dodatnie liczby $a$ i $b$, że $30\%$ liczby $a$ jest równe $60\%$ liczby $b$. Wynika z tego, że

**(a)** $a=2b$;

**(b)** $b=2a$;

**(c)** liczba $a$ jest o $100\%$ większa od liczby $b$.

<small>

* answer:T,N,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

Warunki zadania można zapisać następująco
$$
30\%\cdot a=60\%\cdot b,
$$
$$
\frac{30}{100}a=\frac{60}{100}b,
$$
$$
a=2b.
$$
W szczególności wynika z tego, że $a=b+b=b+100\%\cdot b$.


# <lo-sample/> PL.OMJ.2015TEST.7_8.2

Dwa z boków trójkąta prostokątnego mają długości $3$ oraz $4$. Wynika z tego, że trzeci bok tego trójkąta ma długość

**(a)** nie mniejszą od $5$;

**(b)** nie większą od $5$;

**(c)** równą $5$.

<small>

* answer:N,T,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

Ponieważ przeciwprostokątna trójkąta prostokątnego jest jednocześnie najdłuższym bokiem tego trójkąta, więc bok o długości $3$ musi być jedną z przyprostokątnych. Stąd wniosek, że bok o długości $4$ jest albo drugą przyprostokątną, albo przeciwprostokątną danego trójkąta.

W pierwszym przypadku, w myśl twierdzenia Pitagorasa, przeciwprostokątna tego trójkąta ma długość
$$
\sqrt{3^2+4^2}=5.
$$
Z kolei w drugim przypadku długość drugiej przyprostokątnej jest równa
$$
\sqrt{4^2-3^2}=\sqrt{7}.
$$
Pozostaje zauważyć, że $\sqrt{7}<\sqrt{25}=5$, skąd wynika, że w obu przypadkach trzeci bok rozważanego trójkąta ma długość nie większą od $5$.


# <lo-sample/> PL.OMJ.2015TEST.7_8.3

Liczba $9^{16}-16^9$ jest podzielna przez

**(a)** $4$;

**(b)** $5$;

**(c)** $3^{16}-4^9$.

<small>

* answer:N,T,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

a) Liczba $9^{16}$ jest nieparzysta, a liczba $16^9$ jest parzysta. Wobec tego różnica $9^{16}-16^9$ jest liczbą nieparzystą, więc nie jest podzielna przez $4$.

b) Ostatnią cyfrą liczby $9^{16}=81^8$ jest $1$, gdyż wszystkie potęgi liczb zakończonych cyfrą $1$ są zakończone cyfrą $1$. Podobnie, ostatnią cyfrą liczby $16^9$ jest $6$, gdyż wszystkie potęgi liczb zakończonych cyfrą $6$ są zakończone cyfrą $6$. W związku z tym ostatnią cyfrą różnicy $9^{16}-16^9$ jest $5$, więc różnica ta jest podzielna przez $5$.

c) Zauważmy, że dana liczba jest różnicą kwadratów dwóch liczb całkowitych dodatnich, wobec czego możemy ją przedstawić następująco
$$
9^{16}-16^9=(3^{16})^2-(4^9)^2=(3^{16}-4^9)(3^{16}+4^9).
$$
W takim razie omawiana różnica jest liczbą podzielną przez $3^{16}-4^9$.


# <lo-sample/> PL.OMJ.2015TEST.7_8.4

Każde dwie spośród trzech dodatnich liczb całkowitych $a$, $b$, $c$ są różne. Ponadto liczby te spełniają zależności $\operatorname{NWD}(a,b)=1$ oraz $\operatorname{NWD}(a,c)=1$. Wynika z tego, że

**(a)** $\operatorname{NWD}(b,c)=1$;

**(b)** $\operatorname{NWD}(a,b+c)=1$;

**(c)** $\operatorname{NWD}(a,bc)=1$.

<small>

* answer:N,N,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

a), b) Jeżeli $a=2$, $b=3$, $c=9$, to $\operatorname{NWD}(a,b)=1$ oraz $\operatorname{NWD}(a,c)=1$, a przy tym
$$
\operatorname{NWD}(b,c)=\operatorname{NWD}(3,9)=3\neq 1
$$
oraz
$$
\operatorname{NWD}(a,b+c)=\operatorname{NWD}(2,12)=2\neq 1.
$$

c) Przypuśćmy, że $\operatorname{NWD}(a,bc)>1$. Oznacza to, że liczby $a$ oraz $bc$ mają wspólny dzielnik większy od $1$. Wobec tego istnieje pewien wspólny dzielnik pierwszy $p$ liczb $a$ oraz $bc$. Skoro $p$ dzieli iloczyn $bc$, to dzieli co najmniej jeden z czynników $b$, $c$. Jedna z par $(a,b)$, $(a,c)$ ma więc wspólny dzielnik większy od $1$, czyli $\operatorname{NWD}(a,b)\neq 1$ lub $\operatorname{NWD}(a,c)\neq 1$. Uzyskana sprzeczność dowodzi, że $\operatorname{NWD}(a,bc)=1$.


# <lo-sample/> PL.OMJ.2015TEST.7_8.5

Punkt $I$ jest środkiem okręgu wpisanego w trójkąt $ABC$, w którym $\angle ACB=50^\circ$. Wynika z tego, że

**(a)** $\angle AIB=100^\circ$;

**(b)** $\angle AIB>110^\circ$;

**(c)** $\angle AIB<120^\circ$.

<small>

* answer:N,T,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

Punkt $I$, jako środek okręgu wpisanego w trójkąt $ABC$, jest punktem przecięcia dwusiecznych kątów wewnętrznych $BAC$ oraz $ABC$ trójkąta $ABC$ (rys. 1). Stąd wniosek, że
$$
\angle BAI=\frac{\angle BAC}{2}
\quad\text{oraz}\quad
\angle ABI=\frac{\angle ABC}{2}.
$$
Suma kątów wewnętrznych w trójkącie jest równa $180^\circ$, skąd
$$
\angle BAC+\angle ABC=180^\circ-\angle ACB=130^\circ.
$$
Łącząc uzyskane równości, otrzymujemy
$$
\angle AIB=180^\circ-\angle BAI-\angle ABI
=180^\circ-\frac{\angle BAC+\angle ABC}{2}
=180^\circ-\frac{130^\circ}{2}=115^\circ.
$$

![](PL.OMJ.2015TEST.7_8.5.png)
rys. 1


# <lo-sample/> PL.OMJ.2015TEST.7_8.6

Trójkąt $T$ rozcięto wzdłuż odcinka na dwa trójkąty $T_1$ i $T_2$, a trójkąt $S$ — na trójkąty $S_1$ i $S_2$. Okazało się, że trójkąt $T_1$ jest przystający do trójkąta $S_1$, a trójkąt $T_2$ jest przystający do trójkąta $S_2$. Wynika z tego, że trójkąty $T$ i $S$

**(a)** mają równe pola;

**(b)** mają równe obwody;

**(c)** są przystające.

<small>

* answer:T,N,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

a) Pole trójkąta $T$ jest równe sumie pól trójkątów $T_1$ i $T_2$, a pole trójkąta $S$ jest równe sumie pól trójkątów $S_1$ i $S_2$. Figury przystające mają równe pola, więc pola trójkątów $T_1$ i $S_1$ są równe oraz pola trójkątów $T_2$ i $S_2$ są równe. Wobec tego również pola trójkątów $T$ i $S$ są równe.

b), c) Niech $ABCD$ będzie dowolnym równoległobokiem, w którym kąt $ABC$ jest rozwarty. Niech ponadto $P$ będzie punktem przecięcia przekątnych $AC$ i $BD$ (rys. 2). Oznaczmy trójkąty $ABC$, $ABP$, $BCP$ odpowiednio przez $T$, $T_1$, $T_2$, a trójkąty $ABD$, $ABP$, $DAP$ odpowiednio przez $S$, $S_1$, $S_2$. Zauważmy, że wówczas trójkąty $T_1$ i $S_1$ są przystające (jest to ten sam trójkąt), a także trójkąty $T_2$ i $S_2$ są przystające (jeden jest obrazem drugiego w symetrii względem punktu $P$). Jednak
$$
AB+BC+CA>AB+AD+DB,
$$
co oznacza, że obwód trójkąta $T$ jest większy od obwodu trójkąta $S$. Stąd wynika także, że trójkąty $T$ i $S$ nie są przystające.

![](PL.OMJ.2015TEST.7_8.6.png)
rys. 2


# <lo-sample/> PL.OMJ.2015TEST.7_8.7

Liczby rzeczywiste $x$, $y$ spełniają nierówność $x(x+2)<y(y+2)$. Wynika z tego, że

**(a)** $x<y$;

**(b)** $x+y\neq -2$;

**(c)** $|x+1|<|y+1|$.

<small>

* answer:N,T,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

b) Przypuśćmy, że $x+y=-2$. Wówczas $x+2=-y$ oraz $y+2=-x$ i wobec tego
$$
x(x+2)=x\cdot(-y)=-xy
\quad\text{oraz}\quad
y(y+2)=y\cdot(-x)=-xy.
$$
Stąd wynika, że liczby $x(x+2)$ i $y(y+2)$ są równe. Uzyskana sprzeczność dowodzi, że $x+y\neq 2$.

c) Daną w treści zadania nierówność możemy przekształcić równoważnie
$$
x(x+2)<y(y+2),
$$
$$
x^2+2x<y^2+2y,
$$
$$
x^2+2x+1<y^2+2y+1,
$$
$$
(x+1)^2<(y+1)^2,
$$
$$
|x+1|<|y+1|.
$$

a) Przyjmując $x=0$, $y=-3$, otrzymujemy $x(x+2)=0$ oraz $y(y+2)=3$. Dla tak dobranych liczb zachodzi więc dana nierówność $x(x+2)<y(y+2)$, ale $x>y$.


# <lo-sample/> PL.OMJ.2015TEST.7_8.8

Każdy z wierzchołków sześcianu pomalowano jednym z dwóch kolorów. Wynika z tego, że

**(a)** pewna krawędź tego sześcianu ma końce jednakowego koloru;

**(b)** pewna przekątna pewnej ściany tego sześcianu ma końce jednakowego koloru;

**(c)** pewna przekątna tego sześcianu ma końce jednakowego koloru.

<small>

* answer:N,T,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

Oznaczmy dwie przeciwległe ściany sześcianu przez $ABCD$ oraz $A'B'C'D'$ w taki sposób, aby odcinki $AA'$, $BB'$, $CC'$, $DD'$ były krawędziami sześcianu.

a), c) Jeżeli pomalujemy wierzchołki $A$, $B'$, $C$, $D'$ na czarno, a wierzchołki $A'$, $B$, $C'$, $D$ na biało (rys. 3), to każda krawędź i każda przekątna sześcianu będzie miała wierzchołki różnych kolorów.

![](PL.OMJ.2015TEST.7_8.8.png)
rys. 3

b) Ponieważ wierzchołki pomalowano dwoma kolorami, więc pewne dwa wierzchołki trójkąta $A'BC'$ zostały pomalowane tym samym kolorem. To oznacza, że pewien bok tego trójkąta ma końce tego samego koloru (rys. 4).

![](PL.OMJ.2015TEST.7_8.8A.png)
rys. 4


# <lo-sample/> PL.OMJ.2015TEST.7_8.9

Antek, biegnąc z prędkością $x$ km/h, jeden kilometr pokonuje w ciągu $x$ minut, gdzie $x$ jest pewną dodatnią liczbą rzeczywistą. Wynika z tego, że

**(a)** $x$ jest liczbą wymierną;

**(b)** Antek biegnie z prędkością większą niż $8$ km/h;

**(c)** gdyby Antek szedł z prędkością $\frac12 x$ km/h, to jeden kilometr pokonywałby w ciągu $2x$ minut.

<small>

* answer:N,N,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

Skoro Antek pokonuje jeden kilometr w ciągu $x$ minut, to biegnie z prędkością $\frac{1}{x}$ kilometrów na minutę, czyli $\frac{60}{x}$ kilometrów na godzinę. Wobec tego
$$
\frac{60}{x}=x,
$$
skąd obliczamy $x=\sqrt{60}$.

a) Liczba $\sqrt{60}=2\sqrt{15}$ jest niewymierna.

b) Zachodzi nierówność $\sqrt{60}<\sqrt{64}=8$, więc Antek biegnie z prędkością mniejszą od $8$ km/h.

c) Gdyby Antek szedł dwa razy wolniej, przebycie tej samej trasy zajęłoby mu dwukrotnie więcej czasu.


# <lo-sample/> PL.OMJ.2015TEST.7_8.10

Wielokąt $A$ ma co najmniej osiem wierzchołków oraz dwa razy więcej boków niż wielokąt $B$. Wynika z tego, że wielokąt $A$ ma

**(a)** dwa razy więcej wierzchołków niż wielokąt $B$;

**(b)** dwa razy więcej przekątnych niż wielokąt $B$;

**(c)** parzystą liczbę przekątnych.

<small>

* answer:T,N,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

a) Każdy wielokąt ma tyle samo boków co wierzchołków. Wobec tego, skoro wielokąt $A$ ma dwa razy więcej boków niż wielokąt $B$, to ma on również dwa razy więcej wierzchołków.

b) Zauważmy, że liczba przekątnych każdego $n$-kąta jest równa $\frac12 n(n-3)$. Rzeczywiście, każdy z wierzchołków $n$-kąta jest końcem dokładnie $n-3$ przekątnych tego wielokąta. Stąd wniosek, że wszystkie przekątne mają łącznie dokładnie $n(n-3)$ końców. Skoro każda przekątna ma dwa końce, to przekątnych jest $\frac12 n(n-3)$. W szczególności wynika stąd, że czworokąt ma dwie przekątne, a mający dwa razy więcej boków ośmiokąt ma $20$, czyli $10$ razy więcej, przekątnych.

c) Korzystając ze wzoru na liczbę przekątnych w $n$-kącie wypukłym, wyprowadzonego w poprzednim podpunkcie, stwierdzamy, że każdy dziesięciokąt wypukły ma dokładnie
$$
\frac12\cdot 10\cdot(10-3)=35,
$$
czyli nieparzystą liczbę, przekątnych.


# <lo-sample/> PL.OMJ.2015TEST.7_8.11

Każdy punkt okręgu $\omega$ o promieniu $1$ pomalowano na czarno lub biało w taki sposób, że każda cięciwa tego okręgu o długości $1$ ma końce różnych kolorów. Wynika z tego, że

**(a)** każda średnica okręgu $\omega$ ma końce różnych kolorów;

**(b)** każdy trójkąt równoboczny wpisany w okrąg $\omega$ ma wszystkie trzy wierzchołki tego samego koloru;

**(c)** każdy kwadrat wpisany w okrąg $\omega$ ma dwa wierzchołki czarne i dwa białe.

<small>

* answer:T,T,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

Oznaczmy przez $O$ środek okręgu $\omega$. Niech $A$ będzie dowolnym punktem okręgu $\omega$ oraz niech $ABCDEF$ będzie sześciokątem foremnym wpisanym w ten okrąg (rys. 5). Wówczas $\angle AOB=60^\circ$, gdyż jest to kąt środkowy oparty na łuku będącym $\frac16$ okręgu. Stąd wniosek, że trójkąt $ABO$ jest równoboczny, więc $AB=OA=1$. To oznacza, że każdy z boków sześciokąta $ABCDEF$ jest cięciwą okręgu $\omega$ o długości $1$.

![](PL.OMJ.2015TEST.7_8.11.png)
rys. 5

![](PL.OMJ.2015TEST.7_8.11A.png)
rys. 6

a) Bez straty ogólności przypuśćmy, że punkt $A$ został pomalowany na biało (rozumowanie w przypadku gdy punkt $A$ jest czarny jest w pełni analogiczne). Wówczas z warunków zadania wynika kolejno, że punkty $B$ i $F$ zostały pomalowane na czarno, punkty $C$ i $E$ na biało i w końcu punkt $D$ na czarno (rys. 6). Odcinek $AD$ jest średnicą okręgu $\omega$, która ma końce różnych kolorów, a punkt $A$ został wybrany dowolnie. Stąd wniosek, że każda średnica okręgu $\omega$ ma końce różnych kolorów.

b) Trójkąt $ACE$ o wierzchołkach tego samego koloru jest równoboczny i wpisany w okrąg $\omega$. Punkt $A$ został wybrany dowolnie. Stąd wynika, że każdy trójkąt równoboczny wpisany w dany okrąg ma wierzchołki tego samego koloru.

c) Zauważmy, że przekątne kwadratu wpisanego w okrąg $\omega$ są średnicami tego okręgu. Z punktu a) wiemy, że każda taka średnica ma jeden wierzchołek czarny i jeden biały. Stąd wniosek, że wśród wierzchołków kwadratu zawsze będą dwa wierzchołki czarne i dwa białe.


# <lo-sample/> PL.OMJ.2015TEST.7_8.12

Liczba $\sqrt{2}\cdot\sqrt[3]{2}\cdot\sqrt[6]{2}$ jest

**(a)** niewymierna;

**(b)** mniejsza od $2$;

**(c)** równa $\sqrt[n]{2}$ dla pewnej liczby całkowitej $n>1$.

<small>

* answer:N,N,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

Zauważmy, że
$$
\sqrt{2}\cdot\sqrt[3]{2}\cdot\sqrt[6]{2}
=\sqrt[6]{2^3}\cdot\sqrt[6]{2^2}\cdot\sqrt[6]{2}
=\sqrt[6]{2^3\cdot 2^2\cdot 2}
=\sqrt[6]{2^6}=2.
$$


# <lo-sample/> PL.OMJ.2015TEST.7_8.13

Iloczyn cyfr dodatniej liczby całkowitej $n$ jest równy $4^{100}$. Wynika z tego, że

**(a)** liczba $n$ jest parzysta;

**(b)** liczba $n$ ma co najmniej $100$ cyfr;

**(c)** suma cyfr liczby $n$ jest nie mniejsza od $400$.

<small>

* answer:N,N,T
* questionType:ShortAnswer

</small>

## Rozwiązanie

a) Liczba $n=\underbrace{444\ldots 4}_{100\ \text{cyfr }4}1$ jest nieparzysta, a jej iloczyn cyfr jest równy $4^{100}$.

b) Liczba $n=\underbrace{888\ldots 8}_{66\ \text{cyfr }8}4$ ma $67$ cyfr, a jej iloczyn cyfr jest równy
$$
8^{66}\cdot 4=2^{3\cdot 66}\cdot 2^2=2^{198+2}=2^{200}=4^{100}.
$$

c) Zauważmy, że jedynymi możliwymi cyframi liczby $n$ są cyfry $1$, $2$, $4$ i $8$. Oznaczmy przez $m_d$ liczbę wystąpień cyfry $d$ w zapisie dziesiętnym liczby $n$. Z warunków zadania wynika wówczas, że
$$
\underbrace{1\cdot 1\cdot\ldots\cdot 1}_{m_1\ \text{cyfr }1}\cdot
\underbrace{2\cdot 2\cdot\ldots\cdot 2}_{m_2\ \text{cyfr }2}\cdot
\underbrace{4\cdot 4\cdot\ldots\cdot 4}_{m_4\ \text{cyfr }4}\cdot
\underbrace{8\cdot 8\cdot\ldots\cdot 8}_{m_8\ \text{cyfr }8}
=4^{100},
$$
czyli równoważnie
$$
1^{m_1}\cdot 2^{m_2}\cdot 4^{m_4}\cdot 8^{m_8}=4^{100},
$$
$$
2^{m_2}\cdot 2^{2m_4}\cdot 2^{3m_8}=2^{200},
$$
$$
2^{m_2+2m_4+3m_8}=2^{200},
$$
$$
m_2+2m_4+3m_8=200.
$$
Suma cyfr liczby $n$ jest równa
$$
\underbrace{1+1+\ldots+1}_{m_1\ \text{cyfr }1}+
\underbrace{2+2+\ldots+2}_{m_2\ \text{cyfr }2}+
\underbrace{4+4+\ldots+4}_{m_4\ \text{cyfr }4}+
\underbrace{8+8+\ldots+8}_{m_8\ \text{cyfr }8}
=m_1+2m_2+4m_4+8m_8.
$$
Możemy teraz zauważyć, że
$$
m_1+2m_2+4m_4+8m_8
=m_1+2m_8+2\cdot(m_2+2m_4+3m_8)
=m_1+2m_8+2\cdot 200\geq 400,
$$
gdyż $m_1\geq 0$ oraz $m_8\geq 0$.


# <lo-sample/> PL.OMJ.2015TEST.7_8.14

Każdy bok pewnego czworokąta ma długość mniejszą od $1$. Wynika z tego, że

**(a)** pole tego czworokąta jest mniejsze od $1$;

**(b)** istnieje kwadrat o boku $1$, w którym ten czworokąt jest zawarty;

**(c)** długość każdej przekątnej tego czworokąta jest mniejsza od $\sqrt{2}$.

<small>

* answer:T,N,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

Udowodnimy najpierw następujący fakt: jeżeli co najmniej dwa z boków trójkąta mają długość mniejszą od $1$, to pole tego trójkąta jest mniejsze od $\frac12$.

Niech $XYZ$ będzie trójkątem, w którym $XY<1$ oraz $XZ<1$ (rys. 7). Oznaczmy przez $T$ rzut prostokątny punktu $Z$ na prostą $XY$ (punkt $T$ może leżeć poza odcinkiem $XY$ lub pokrywać się z jednym z punktów $X$, $Y$). W trójkącie prostokątnym $XZT$ (być może zdegenerowanym do odcinka) przeciwprostokątna $XZ$ jest nie krótsza od przyprostokątnej $ZT$, czyli $ZT\leq XZ$. Uzyskujemy więc nierówność
$$
[XYZ]=\frac{XY\cdot ZT}{2}\leq \frac{XY\cdot XZ}{2}<\frac{1\cdot 1}{2}=\frac12,
$$
gdzie $[\mathcal{F}]$ oznacza pole figury $\mathcal{F}$. To kończy dowód.

![](PL.OMJ.2015TEST.7_8.14.png)
rys. 7

a) Niech $ABCD$ będzie czworokątem, którego każdy bok ma długość mniejszą od $1$. Korzystając z udowodnionego na początku faktu, otrzymujemy
$$
[ABC]<\frac12
\quad\text{oraz}\quad
[ADC]<\frac12.
$$
Dodając stronami dwie powyższe nierówności, uzyskujemy $[ABCD]<1$.

c) Rozważmy prostopadłe odcinki $AC$, $BD$ o długościach odpowiednio $1{,}8$, $0{,}6$, które dzielą się na połowy (rys. 8). Wówczas czworokąt $ABCD$ jest rombem, którego każdy bok ma długość
$$
\sqrt{0{,}9^2+0{,}3^2}=\sqrt{0{,}81+0{,}09}=\sqrt{0{,}9}<1.
$$
Z kolei przekątna $AC$ ma długość większą od $\sqrt{2}$, gdyż $(1{,}8)^2=3{,}24>2=(\sqrt{2})^2$.

![](PL.OMJ.2015TEST.7_8.14A.png)
rys. 8

b) Każdy odcinek zawarty w kwadracie o boku $1$ ma długość co najwyżej $\sqrt{2}$. Stąd wniosek, że czworokąta $ABCD$ skonstruowanego w punkcie c) nie można umieścić wewnątrz takiego kwadratu.


# <lo-sample/> PL.OMJ.2015TEST.7_8.15

Graniastosłup prawidłowy trójkątny rozcięto płaszczyzną na dwa wielościany, uzyskując w przekroju trójkąt. Wynika z tego, że

**(a)** każdy z otrzymanych wielościanów ma dokładnie dwie ściany trójkątne;

**(b)** w każdym wierzchołku każdego z otrzymanych wielościanów schodzą się dokładnie trzy krawędzie;

**(c)** każda ściana każdego z otrzymanych wielościanów jest trójkątem lub czworokątem.

<small>

* answer:N,N,N
* questionType:ShortAnswer

</small>

## Rozwiązanie

Rozważmy graniastosłup prawidłowy trójkątny o podstawach $ABC$, $A'B'C'$ oznaczonych w taki sposób, że $AA'$, $BB'$, $CC'$ są krawędziami bocznymi graniastosłupa. Niech punkty $M$ i $N$ będą odpowiednio środkami krawędzi $AC$ i $CC'$.

Przetnijmy graniastosłup płaszczyzną $BMN$, uzyskując w przekroju trójkąt (rys. 9). Wówczas jedna z otrzymanych brył ma trzy ściany trójkątne $ABM$, $BMN$, $A'B'C'$, w jej wierzchołku $B$ schodzą się dokładnie cztery krawędzie oraz posiada ona ścianę pięciokątną $AMNC'A'$.

![](PL.OMJ.2015TEST.7_8.15.png)
rys. 9
