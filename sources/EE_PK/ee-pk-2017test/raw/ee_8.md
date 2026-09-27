# <lo-sample/> EE.PK.2017TEST.8.1

Kui palju on selliseid neljakohalisi paarisarve, mis koosnevad erinevatest numbritest 2, 0, 1 ja 7 ning ei jagu arvuga 4?

<small>

* answer:6
* questionType:ShortAnswer

</small>

## Lahendus

Paarisarvu lõpus saab olla 0 või 2. Kui arvu lõpus on 0, peab kümneliste number olema 1 või 7, et arv ei jaguks 4-ga (2 võimalust). Kaks esimest numbrit võivad olla ükskõik kummas järjestuses (2 võimalust). Seega 0-ga lõppevaid nõutud omadusega arve on $2 \cdot 2$ ehk 4. Kui arvu lõpus on 2, peab kümneliste number olema 0, et arv ei jaguks 4-ga (1 võimalus). Kaks esimest numbrit võivad olla ükskõik kummas järjestuses (2 võimalust). Seega 2-ga lõppevaid nõutud omadusega arve on $1 \cdot 2$ ehk 2. Kokku on nõutud arve $4 + 2$ ehk 6.


# <lo-sample/> EE.PK.2017TEST.8.2

Leia avaldise $2017-(2016-(2015-(2014-(2013-2017))))$ väärtus.

<small>

* answer:$-2$
* questionType:ShortAnswer

</small>

## Lahendus

Saame
$$
\begin{aligned}
2017-(2016-(2015-(2014-(2013-2017)))) & = \\
& = 2017-(2016-(2015-(2014-(-4)))) = \\
& = 2017-(2016-(2015-2018)) = \\
& = 2017-(2016-(-3)) = \\
& = 2017-2019 = \\
& = -2.
\end{aligned}
$$


# <lo-sample/> EE.PK.2017TEST.8.3

Leia kuuekohaline naturaalarv, mille kõik numbrid on erinevad, kui on teada, et selle arvu kolme numbri vähendamisel 1 võrra ja kolme ülejäänud numbri suurendamisel 1 võrra on võimalik saada arv 742809.

<small>

* answer:653718
* questionType:ShortAnswer

</small>

## Lahendus

Numbrit 0 on võimalik saada ainult vähendamisega numbrist 1. Numbrit 2 pole seega võimalik saada suurendamisega numbrist 1, vaid ainult vähendamisega numbrist 3. Sarnaselt pole numbrit 4 võimalik saada suurendamisega numbrist 3, vaid ainult vähendamisega numbrist 5. Numbrid 7, 8 ja 9 peavad järelikult olema saadud suurendamisega vastavalt numbritest 6, 7 ja 8.


# <lo-sample/> EE.PK.2017TEST.8.4

Papist on välja lõigatud hulk kolmnurki ja ruute. Ruute on 8 võrra rohkem kui kolmnurki ning kõigil neil kujunditel on kokku 88 nurka. Mitu kujundit on papist välja lõigatud?

<small>

* answer:24
* questionType:ShortAnswer

</small>

## Lahendus

*Lahendus 1.* Olgu kolmnurkade arv $x$, siis ruute on $x+8$. Kolmnurkadel on kokku $3x$ tippu, ruutudel aga $4(x+8)$ ehk $4x+32$ tippu. Seega $3x+4x+32=88$, kust $x=8$. Järelikult on kolmnurki 8 ja ruute 16, kokku 24 kujundit.

*Lahendus 2.* Olgu kolmnurkade arv $x$ ja ruutude arv $y$. Ülesande tingimuste põhjal saame võrrandisüsteemi
$$
\begin{cases}
y-x=8,\\
4y+3x=88.
\end{cases}
$$
Korrutades teise võrrandi pooled 2-ga ja lahutades esimese võrrandi, saame $7y+7x=168$, kust $7(x+y)=168$ ja $x+y=24$.


# <lo-sample/> EE.PK.2017TEST.8.5

Leia vähim naturaalarv $n$, mille korral arv $n^2$ jagub arvuga 5 ja arv $(n+2)^2$ jagub arvuga 8.

<small>

* answer:10
* questionType:ShortAnswer

</small>

## Lahendus

Arvu ruut jagub algarvuga 5 parajasti siis, kui arv ise jagub arvuga 5. Seega tuleb leida vähim 5-ga jaguv naturaalarv $n$, mille korral $(n+2)^2$ jagub 8-ga. Juhul $n=0$ ja $n=5$ saame vastavalt $(n+2)^2=4$ ja $(n+2)^2=49$, mis ei jagu 8-ga. Juhul $n=10$ aga $(n+2)^2=144=8 \cdot 18$.


# <lo-sample/> EE.PK.2017TEST.8.6

Täisnurkse kolmnurga $ABC$ täisnurga tipust $C$ on tõmmatud kõrgus $CD$, mis lõikub tipust $B$ tõmmatud nurgapoolitajaga punktis $L$. Nurk $BLC$ on suurusega $110^\circ$. Leia nurga $ACD$ suurus.

![](EE.PK.2017TEST.8.6.png)

<small>

* answer:$40^\circ$
* questionType:ShortAnswer

</small>

## Lahendus

![](EE.PK.2017TEST.8.6A.png)

Et $\angle BLD = 180^\circ - 110^\circ = 70^\circ$, siis kolmnurgast $DBL$ saame võrduse $\angle DBL = 180^\circ - 90^\circ - 70^\circ = 20^\circ$ (joonis 5). Seega $\angle CBA = 2 \cdot 20^\circ = 40^\circ$. Kuna kolmnurgad $ACD$ ja $ABC$ on sarnased tunnuse NN põhjal, siis ka $\angle ACD = 40^\circ$.


# <lo-sample/> EE.PK.2017TEST.8.7

Joonisel on kolm ruutu, neist suurim on küljepikkusega 3 cm ja kumbki väiksematest on küljepikkusega 1 cm. Punktid $A$, $B$ ja $C$ on nende ruutude tipud. Leia kolmnurga $ABC$ pindala.

![](EE.PK.2017TEST.8.7.png)

<small>

* answer:$2{,}5\ \mathrm{cm}^2$
* questionType:ShortAnswer

</small>

## Lahendus

Tähistame punktid $D$, $E$, $K$, $L$, $M$ nagu näidatud joonisel 6.

![](EE.PK.2017TEST.8.7A.png)

Tähistagu $S_{\mathcal{K}}$ kujundi $\mathcal{K}$ pindala. Saame
$$
S_{AKMD}=3\ \mathrm{cm}\cdot 3\ \mathrm{cm}=9\ \mathrm{cm}^2,
$$
$$
S_{ELMD}=1\ \mathrm{cm}\cdot 3\ \mathrm{cm}=3\ \mathrm{cm}^2,
$$
$$
S_{ABE}=\frac{2\ \mathrm{cm}\cdot 1\ \mathrm{cm}}{2}=1\ \mathrm{cm}^2,
$$
$$
S_{AKC}=\frac{1\ \mathrm{cm}\cdot 3\ \mathrm{cm}}{2}=1{,}5\ \mathrm{cm}^2,
$$
$$
S_{BLC}=\frac{2\ \mathrm{cm}\cdot 1\ \mathrm{cm}}{2}=1\ \mathrm{cm}^2.
$$
Järelikult
$$
S_{ABC}=S_{AKMD}-(S_{ELMD}+S_{ABE}+S_{AKC}+S_{BLC})=2{,}5\ \mathrm{cm}^2.
$$


# <lo-sample/> EE.PK.2017TEST.8.8

Lõigul on märgitud kolm punkti $A$, $B$ ja $C$ nii, et $|AB|=|BC|=1$ cm. Lõiku pööratakse algul ümber punkti $B$ ja siis ümber punkti $C$ iga kord päripäeva täpselt täisnurga võrra. Kui pika tee läbib punkt $A$ nende pööramiste jooksul?

![](EE.PK.2017TEST.8.8.png)

<small>

* answer:$1{,}5\pi\ \mathrm{cm}$
* questionType:ShortAnswer

</small>

## Lahendus

![](EE.PK.2017TEST.8.8A.png)

Esimese pööramise jooksul ümber punkti $B$ läbib punkt $A$ veerandi ringjoonest, mille raadius on 1 cm. Läbitud tee pikkus on $\frac{1}{4}\cdot 2\pi \cdot 1\ \mathrm{cm}$ ehk $\frac{1}{2}\pi\ \mathrm{cm}$. Teise pööramise jooksul ümber punkti $C$ läbib punkt $A$ veerandi ringjoonest, mille raadius on 2 cm. Läbitud tee pikkus on nüüd $\frac{1}{4}\cdot 2\pi \cdot 2\ \mathrm{cm}$ ehk $\pi\ \mathrm{cm}$. Järelikult läbib punkt $A$ kokku tee pikkusega $\frac{3}{2}\pi\ \mathrm{cm}$. Joonisel 7 on punktide $A$, $B$, $C$ asukohad pärast esimest pööramist tähistatud vastavalt $A'$, $B'$, $C'$ ja pärast teist pööramist vastavalt $A''$, $B''$, $C''$.


# <lo-sample/> EE.PK.2017TEST.8.9

Nelinurga $ABCD$ külgede pikkused on $|AB|=8$ cm, $|BC|=6$ cm, $|CD|=4$ cm ja $|DA|=16$ cm. Leia diagonaali $AC$ pikkus, kui on teada, et see on täisarv sentimeetreid.

![](EE.PK.2017TEST.8.9.png)

<small>

* answer:$13\ \mathrm{cm}$
* questionType:ShortAnswer

</small>

## Lahendus

Kolmnurgas $ABC$ on küljed $AB$ ja $BC$ vastavalt pikkustega 8 cm ja 6 cm, mistõttu külje $AC$ pikkus peab olema väiksem kui 14 cm. Teisalt on kolmnurgas $ADC$ küljed $AD$ ja $DC$ vastavalt pikkustega 16 cm ja 4 cm, mistõttu külje $AC$ pikkus peab olema suurem kui 12 cm. Ainus täisarv 12 ja 14 vahel on 13.


# <lo-sample/> EE.PK.2017TEST.8.10

Kuubiku igasse tippu kirjutatakse üks numbritest 1 kuni 8. Igasse tippu kirjutatakse erinev number. Viie tahu tippudes olevad numbrid suuruse järjestuses on järgmised:

![](EE.PK.2017TEST.8.10.png)

1, 2, 4, 5;

3, 6, 7, 8;

2, 5, 7, 8;

1, 3, 4, 6;

2, 3, 4, 7.

Milline number on tipus, mis asub tipust numbriga 8 kõige kaugemal?

<small>

* answer:4
* questionType:ShortAnswer

</small>

## Lahendus

![](EE.PK.2017TEST.8.10A.png)

*Lahendus 1.* Iga tipp kuulub kolmele tahule. Viie tahu tippude loeteludes esinevad numbrid 1, 5, 6, 8 kaks korda ja ülejäänud numbrid kolm korda. Seega puuduva tahu tippudes on numbrid 1, 5, 6, 8. Kaks kuubi tippu on kuubi diagonaali otspunktid parajasti siis, kui nad ei asu ühel ja samal tahul. Tahkudel olevate numbrite loeteludest näeme, et 8 ei asu samal tahul numbriga 4.

*Lahendus 2.* Kahel tahul võib olla kaks ühist tippu või mitte ühtegi. Ühised tipud on kuubi serva otspunktid.

* Esimesest ja kolmandast tahust tuleneb serv otspunktidega 2 ja 5, esimesest ja viiendast tahust aga serv otspunktidega 2 ja 4. Seega esimese tahu tippude järjestus mööda servi on 1, 4, 2, 5.
* Et leidub serv otspunktidega 2 ja 5, siis selle serva vastasserv kolmandal tahul on otspunktidega 7 ja 8. Viienda tahu tähtede põhjal peavad olema ühendatud 2 ja 7. Seega kolmanda tahu tippude järjestus mööda servi on 2, 5, 8, 7.
* Et leidub serv otspunktidega 1 ja 4, siis selle serva vastasserv neljandal tahul on otspunktidega 3 ja 6. Viienda tahu tähtede põhjal peavad olema ühendatud 4 ja 3. Seega neljanda tahu tippude järjestus mööda servi on 1, 4, 3, 6.

Eelnevast tulenevalt on viiendal tahul tippude järjestus mööda servi 2, 7, 3, 4 teisel tahul 3, 6, 7, 8 (joonis 8). Üle jääb tahk tippudega 1, 5, 8, 6. Kuubi diagonaal, mis algab tipust numbriga 8, lõpeb tipus numbriga 4.