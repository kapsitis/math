# <lo-sample/> EE.PK.2012TEST.9.1

Arvul $2012$ on järgmine omadus: kui kirjutada välja tema iga kahe kõrvutioleva numbri summa, siis need summad $2$, $1$ ja $3$ on kolm järjestikust täisarvu mingis järjekorras. Leia vähim selline viiekohaline naturaalarv, millel on sarnane omadus, st tema kahe kõrvutioleva numbri summad on neli järjestikust täisarvu mingis järjekorras.

<small>

* answer:10021
* questionType:ShortAnswer

</small>

## Lahendus

Leiame ühekaupa selle viiekohalise arvu numbrid vasakult paremale, valides igal sammul vähima võimaliku numbri. Et arv ei alga 0-ga, on vähim võimalik esimene number 1. Teine ja kolmas number saavad olla 0 – arvu esimese kahe numbri summa on siis 1 ning teise ja kolmanda numbri summa 0. Arvu neljas number ei saa olla 0 ega 1, sest siis summad korduksid, kuid saab olla 2, siis kolmanda ja neljanda numbri summa on 2. Kahe viimase numbri summa peab seega olema 3, st arvu viimaseks numbriks tuleb valida 1.


# <lo-sample/> EE.PK.2012TEST.9.2

*Palindroomiks* nimetatakse arvu, mis tagant ettepoole lugedes annab sama arvu. Näiteks arvud $353$ ja $5445$ on palindroomid. Leia vähim selline naturaalarv $k$, mille korral arv $k + 2573$ on palindroom.

<small>

* answer:89
* questionType:ShortAnswer

</small>

## Lahendus

Vähim palindroom, mis on suurem arvust 2573, on 2662. Siit leiame, et $k = 2662 - 2573 = 89$.


# <lo-sample/> EE.PK.2012TEST.9.3

Kolme erineva täisarvu korrutis on $12$ ja summa $3$. Leia neist kolmest vähima arvu vähim võimalik väärtus.

<small>

* answer:-2
* questionType:ShortAnswer

</small>

## Lahendus

Arvu 12 esitamisel kolme täisarvulise teguri korrutisena on tegurite absoluutväärtuste jaoks neli võimalust: $(1, 1, 12)$, $(1, 2, 6)$, $(1, 3, 4)$ ja $(2, 2, 3)$. Et tegurite summa 3 on paaritu, peab tegurite seas olema kas 1 või 3 paaritut arvu – nii jäävad järele absoluutväärtuste kolmikud $(1, 2, 6)$ ja $(2, 2, 3)$. Esimesest kolmikust saame summa 3 ainult siis, kui need tegurid on $-1$, $-2$ ja 6. Teisest kolmikust saame summa 3 ainult siis, kui tegurid on 2, $-2$ ja 3, ent nende korrutis on siis $-12$. Seega ongi ainus sobiv võimalus $12 = (-1) \cdot (-2) \cdot 6$ ning vähim tegur on siis $-2$.


# <lo-sample/> EE.PK.2012TEST.9.4

Olgu $a$ ja $b$ positiivsed arvud. On teada, et arv $a$ moodustab $b$ protsenti arvust $b$ ning arv $b$ moodustab $a$ protsenti arvust $a$. Leia arvude $a$ ja $b$ summa.

<small>

* answer:200
* questionType:ShortAnswer

</small>

## Lahendus

Oletame, et $b > a$, siis $b$ protsenti arvust $b$ on suurem kui $a$ protsenti arvust $a$, st $a > b$ – vastuolu. Samamoodi saame vastuolu oletusest, et $b < a$. Järelikult $b = a$ ning arv $a$ moodustab $a$ protsenti iseendast, st $a = b = 100$ ja $a + b = 200$.


# <lo-sample/> EE.PK.2012TEST.9.5

Ruudustiku ülemisele reale kirjutatakse korduvalt järjest sõna MATEMAATIKA, alumisele reale aga kirjutatakse korduvalt järjest sõna FÜÜSIKA. Igas ruudus on üks täht ja tühje ruute ei ole. Mitmendas veerus on tähed K esimest korda kohakuti?

![](EE.PK.2012TEST.9.5.png)

<small>

* answer:76. veerus
* questionType:ShortAnswer

</small>

## Lahendus

*Lahendus 1.* Ülemises reas esineb täht K esimest korda 10. veerus ja edasi iga 11 veeru järel, st veergudes numbritega $10 + 11k$, kus $k = 0, 1, \ldots$ . Alumises reas esineb täht K esimest korda 6. veerus ja edasi iga 7 veeru järel, st veergudes numbritega $6 + 7m$, kus $m = 0, 1, \ldots$ . Tähed K on mõlemas reas kohakuti, kui $10 + 11k = 6 + 7m$, ehk $11k + 4 = 7m$. Vaadates järjest läbi arve kujul $11k + 4$ leiame, et esimesena jagub neist 7-ga arv $70 = 11 \cdot 6 + 4$, st $k = 6$. Otsitava veeru number on niisiis $10 + 11 \cdot 6 = 76$.

*Lahendus 2.* Ülemises reas kordub täht K iga 11 veeru järel ja alumises reas iga 7 veeru järel. Täiendame ruudustikku vasakule kahe veeru võrra, olgu need numbritega 0 ja $-1$. Siis veerus numbriga $-1$ on mõlemas reas K ning sama olukord kordub iga $m$ veeru järel, kus $m = \mathrm{VÜK}(11, 7)$. Et arvud 11 ja 7 on ühistegurita, siis nende vähim ühiskordne on $11 \cdot 7 = 77$, st järgmist korda on tähed K kohakuti veerus numbriga $-1 + 77 = 76$.


# <lo-sample/> EE.PK.2012TEST.9.6

Arvus $324$ on kõik numbrid erinevad ning ta jagub iga oma numbriga. Leia vähim sellise omadusega kolmekohaline arv.

<small>

* answer:124
* questionType:ShortAnswer

</small>

## Lahendus

Leiame ühekaupa selle kolmekohalise arvu numbrid vasakult paremale, valides igal sammul vähima võimaliku numbri. Et 0-ga ei saa jagada, on vähim võimalik sajaliste number 1; vähim võimalik kümneliste number on siis 2 ning üheliste number peab olema paaris, et saadav arv jaguks 2-ga. Seega on vähim võimalik üheliste number 4 ning saadav arv 124 on ka nõutava omadusega.


# <lo-sample/> EE.PK.2012TEST.9.7

Ristküliku lühem külg on poolringjoone diameetriks ning võrdhaarse kolmnurga aluseks. Võrdhaarse kolmnurga aluse vastastipp asub sellel poolringjoonel. Leia kolmnurga ühe haara pikenduse ja ristküliku pikema külje vahelise nürinurga $\alpha$ suurus.

![](EE.PK.2012TEST.9.7.png)

<small>

* answer:$135^\circ$
* questionType:ShortAnswer

</small>

## Lahendus

Et võrdhaarse kolmnurga aluseks on poolringjoone diameeter ja vastastipp asub poolringjoonel, siis tipunurga suurus on $90^\circ$ (diameetrile toetuv piirdenurk). Võrdhaarse kolmnurga alusnurk on seega $45^\circ$ ning nurga $\alpha$ kõrvunurk on $180^\circ - 90^\circ - 45^\circ = 45^\circ$ (vt joonist 5), kust $\alpha = 180^\circ - 45^\circ = 135^\circ$.

![](EE.PK.2012TEST.9.7A.png)


# <lo-sample/> EE.PK.2012TEST.9.8

Joonisel näidatud kujund koosneb kuuest võrdsest võrdhaarsest kolmnurgast. Mitu korda on kujundi valge osa pindala suurem tumedaks värvitud osa pindalast?

![](EE.PK.2012TEST.9.8.png)

<small>

* answer:2
* questionType:ShortAnswer

</small>

## Lahendus

![](EE.PK.2012TEST.9.8A.png)

Olgu iga võrdhaarse kolmnurga aluse pikkus $a$ ja kõrgus $h$ (vt joonist 6). Kogu kujundi pindala on siis $6 \cdot \frac{ah}{2} = 3ah$. Valge osa koosneb kahest kolmnurgast alusega $2a$ ja kõrgusega $h$, st selle pindala on $2 \cdot \frac{2ah}{2} = 2ah$, mis moodustab kaks kolmandikku kogu kujundi pindalast. Tumedaks värvitud osa moodustab niisiis ühe kolmandiku kogu kujundi pindalast, ehk valge osa on tumedaks värvitud osast 2 korda suurem.


# <lo-sample/> EE.PK.2012TEST.9.9

Kolmnurga kõik nurgad on erineva suurusega ja iga nurga suurus on mingi täisarv kraade. Kolmnurga suurim ja vähim nurk erinevad suuruselt keskmisest nurgast täpselt sama arvu kraadide võrra. Mitu erinevat võimalikku suurust on selle kolmnurga vähimal nurgal?

<small>

* answer:59
* questionType:ShortAnswer

</small>

## Lahendus

Olgu suuruselt keskmine nurk $n$ kraadi, siis vähim ja suurim nurk on vastavalt $n - k$ ja $n + k$ kraadi, kus $k$ on mingi positiivne täisarv. Niisiis $180 = n + (n - k) + n + k = 3n$, kust $n = 60$. Vähima nurga suurus saab seega olla 1 kuni 59 kraadi, ning need kõik on ka ilmselt võimalikud.


# <lo-sample/> EE.PK.2012TEST.9.10

Pöörlevale lauale asetatakse neli täringut, nagu joonisel näidatud. Iga täringu tahkudele on kirjutatud naturaalarvud $1$ kuni $6$ nii, et vastastahkudel olevate arvude summa on $7$. Leia täringute $14$ nähtaval tahul olevate arvude suurim võimalik summa.

![](EE.PK.2012TEST.9.10.png)

<small>

* answer:62
* questionType:ShortAnswer

</small>

## Lahendus

Ühe täringu tahkudel olevate arvude summa on $1 + 2 + 3 + 4 + 5 + 6 = 21$, neljal täringul kokku 84. Kahel alumisel täringul ei ole kummalgi nähtavad üks paar vastastahke, millel olevate arvude summa on 7, ning lisaks üks tahk, millel olev arv on vähemalt 1. Kahel ülemisel täringul on kummalgi kaks mittenähtavat tahku, mis ei ole teineteise vastastahud, neil olevate arvude summa on vähemalt $1 + 2 = 3$. Seega on täringute nähtavatel tahkudel olevate arvude summa ülimalt $84 - 2 \cdot (7 + 1) - 2 \cdot (1 + 2) = 84 - 16 - 6 = 62$.