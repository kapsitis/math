# <lo-sample/> BBK2012.P1.118 

Uz tāfeles uzrakstìti 1999 naturāli skaiţ̦i (starp tiem var būt arī vienādi). 
Ar vienu gājienu aţ̦auts nodzēst divus skaitlus un to vietā uzrakstīt 
nodzēsto skaitlu lielāko kopīgo dalītāju un mazāko kopīgo dalāmo.

Pierādīt, ka izdarot šādus gājienus pietiekami ilgi, uz tāfeles uzrakstītie 
skaitļi kādreiz pārstās mainīties.




## Atrisinājums

Apzīmēsim $\operatorname{LKD}(x, y)=(x, y)=u$, bet $\operatorname{MKD}(x, y)=[x, y]=v$. 
No vienādības $u \cdot v=x \cdot y$ seko, ka kopējais skaitļu reizinājums $R$ nemainās. 
Atzīmēsim, ka no šejienes seko, ka kopējā skaitļu summa nevar palielināties bezgalīgi ilgi. 
Tiešām, ja skaitļu summa palielinātos bezgalīgi ilgi, tad tā kļūtu lielāka par $1999R$. 
Tādā gadījumā kāds no skaitļiem būtu lielāks par $R$, un arī viss reizinājums būtu palielinājies.

Atliek pierādīt tikai tādu faktu:

Ja $x<y$, $u<x<y<v$, kur $u, x, y, v$ -- reāli skaitli, $xy=uv$, tad $u+v>x+y$.

Šis fakts nozīmē, ka, aizvietojot skaiţus $x, y$ ar to lielāko kopīgo dalītāju un 
mazāko kopīgo dalāmo visu skaitlu summa palielinās (izṇemot gadījumu, kad $x=u$ un $y=v$). 
Pierādījums:

$$u+v=\sqrt{(u-v)^{2}+4uv} > \sqrt{(x-y)^{2} + 4xy}=x+y.$$

Tas nozīmē, ka ar laiku iestāsies stabilizācija; no jebkuriem diviem skaitļiem 
viens būs otra dalītājs un izpildīsies vienādības $u=(x, y)$ un $v=[x, y]$; 
tātad vai nu $x$ būs skaitļa $y$ dalītājs, vai otrādi.





