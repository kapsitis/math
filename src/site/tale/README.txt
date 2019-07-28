An unknown number is divisible by just four numbers from the set {6, 15, 20, 21, 70}. Determine which ones.
https://www.hackmath.net/en/problem/7137?tag_id=149,161



5. [Help Post](https://artofproblemsolving.com/community/c6t487922f6h1782126_help_post)  
Dots naturāls skaitlis $a$. Vai vienmēr ir spēkā sakarība: 
$\mbox{LKD}(a^{m}-1,a^{n} -1) = a^{\mbox{LKD}(m,n)} - 1$?




# <lo-theory/> LKD saglabājas

**Apgalvojums:** Ja $\mbox{LKD}(a_1,d) = k$, 
tad arī $\mbox{LKD}(a_1+d,d)=k$ un 
$\mbox{LKD}(a_1 - d, d) = k$. 

Šis ir apgalvojums par invariantu: 
lielākais kopīgais dalītājs progresijas loceklim 
un diferencei saglabājas. 

## <lo-summary/> Piemērs: Kalendārs

TODO: Tabulkalendārs, kur nemainās atlikumi


TODO: Attēls, kur $9k$ un $15k$ uzzīmētas tā, lai $\mbox{LKD}(9,15) =3$ ir
sasniegta kā starpība.



## <lo-sample/> BBK2012.P1.104

Skaitļu virkne $(a_i)$ tiek definēta šādi: 
$$a_1=19,\;a_2=90,\;a_{n+2}=a_n+a_{n+1},\;\mbox{ja}\;n=1,2,3,\ldots.$$
Atrast skaitļu $a_{1989}$ un $a_{1990}$ lielāko kopīgo dalītāju.


## <lo-hints/> BBK2012.P1.104

* Kādi ir daži pirmie locekļi virknē? 
* Vai tā ir aritmētiska progresija?
* Kāda ir 

## <lo-soln/> BBK2012.P1.104

* Ievērojam, ka $\mbox{LKD}(a_1,a_2)=\mbox{LKD}(19,90)=1$. 
* Pamatojam ar indukciju, ka $\mbox{LKD}(a_n,a_{n+1})=1$ katram $n=1,2,\ldots$. 

Jāpamato tikai indukcijas pāreja: 

* Ja $\mbox{LKD}(a_k,a_{k+1})=1$, tad arī $\mbox{LKD}(a_{k+1},a_{k+2})=1$, 
jo $a_{k+2} = a_{k} + a_{k+1}$ un skaitļiem $(a_{k+1}, a_{k}+a_{k+1})$ 
lietojam Eiklīda algoritmu - atņemam mazāko no lielākā:

$$\mbox{LKD}(a_{k+1},a_{k+2}) = \mbox{LKD}(a_k,a_{k+1})=1.$$


