# Dalīšana ar atlikumu

**Definīcija:**
Izdalīt veselu skaitli $m$ ar naturālu skaitli $n$ ar atlikumu 
nozīmē uzrakstīt skaitli formā $m=nq+r$, turklāt $q$ un $r$ 
ir veseli skaitļi, un $0 \leq r \leq n-1$.

Praktiski dalīšanu ar atlikumu izpilda kā parastu dalīšanu, 
tikai šo procesu pabeidz, tiklīdz atlikums kļūst mazāks par dalītāju.

Mēs parasti neuzdodam sev jautājumu, vai vienmēr var izdalīt ar atlikumu 
un vai atlikums nosakāms viennozīmīgi. 

**Teorēma:** 
Jebkuram veselam skaitlim $m$ un jebkuram naturālam skaitlim $n$ 
eksistē tieši viens veselu skaitļu pāris $(q,r)$, kuram izpildās nosacījumi:
$$m = q \cdot n + r,\;\;0 \leq r < n.$$


**Pierādījums.** 

* **Eksistence (Izdalīt ar atlikumu vienmēr var).**  
  Ar $q$ apzīmēsim lielāko veselo skaitli, 
  kurš nepārsniedz $\frac{m}{n}$; tad  $q \leq \frac{m}{n} < q+1$ un $qn \leq m < qn+n$. 
  Ar $r$ apzīmēsim skaitli $m-qn$; tātad $m = q \cdot n + r$. 
  No nevienādībām $qn \leq m < qn+n$ seko, ka $0 \leq r < n$.

* **Unitāte (Izdalīt ar atlikumu var tikai vienā veidā).**  
  Pieņemsim, ka to pašu skaitli $m$ var izteikt divos dažādos veidos: 
  $$\left\{ \begin{array}{ll}
  m = q_1 \cdot n + r_1, & 0 \leq r_1 < n\\
  m = q_1 \cdot n + r_1, & 0 \leq r_1 < n.\\
  \end{array} \}$$
	
  Atņemot no pirmās vienādības otro, iegūstam:

  $$0 = (q_1 - q_2) \cdot n + (r_1 - r_2)\;\;\text{jeb}\;\; (q_2 - q_1) \cdot n = (r_1 - r_2).$$

  Tātad $r_1 - r_2$ dalās ar $n$. Tā kā $|r_1 - r_2 | < n$, tad 
  $r_1 - r_2 = 0$ un tādēļ arī $r_1 = r_2$ un $q_1 = q_2$.  
  Unitāte pierādīta.
