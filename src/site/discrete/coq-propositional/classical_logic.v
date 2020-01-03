(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a># 

#<h2>What is Intuitionistic logic</h2># 

Propositional logic expressions that are 
straightforward to prove using Coq tactics
are part of so called Intuitionistic logic 
(#<i>lv:intuicionisma loģika</i>#). They 
do not use the Law of Excluded Middle 
(#<i>lv:trešā izslēgtā likumu</i>#, #<i>la:Tertium non datur</i>#).
*)

(*
Require Import Logic.
Require Import  ClassicalFacts.
Require Import Classical_Prop.
*)



Lemma sample1: forall A, ~ ~ A /\ ~ A -> A.
Proof.
  unfold not.
  intros A H.
  destruct H as [H1 H2].
  pose (H1 H2) as H3.
  contradiction H3.
Qed.

Lemma sample2: forall A: Prop, A -> ~~A.
Proof.
  unfold not. 
  intros A H1 H2.
  pose (H2 H1) as H3.
  exact H3.
Qed.

(** This sample is not yet proven in Coq, but
it could also be part of intuitionist logic, 
even though it has many negations. If you do not want
to complete the proof, write #<tt>Admitted.</tt>#
instead of full proof ended by #<tt>Qed.</tt>#. 
*)

Lemma sample3: forall A, ~ ~ (~ ~ A -> A).
Proof. 
  Admitted.


(** #<h2>What is Classical Logic</h2># 

Classical logic 
Šis likums nozīmē, ka "A \/ ~A" - tātad vienmēr 
ir patiess vai nu izteikums "A" vai arī "~A". 
Lai ar to varētu spēlēties, ir jāimportē Coq 
interaktīvajā vidē aksiomas un galvenie apgalvojumi, 
kas saistīti ar klasisko loģiku.
*) 

Require Import Classical_Prop.

(** Svarīgas "Trešā izslēgtā likuma" sekas ir 
iespēja nomest divkāršas negācijas. 
Šāds pierādījums no pretējā ļoti stipri atšķiras
no agrāk iegūtā #<tt>sample2</tt>#, kurš bija 
intuicionisma piemērs.
*) 

Lemma sample4: forall p: Prop, ~~p -> p. 
Proof.
  intros p. (*r 1nd part: ~~p -> p *)
  unfold not.
  intros H.
  elim (classic p).
  intros PTrue; exact PTrue. 
  intro PFalse.
  pose (H PFalse) as CONTRA.
  contradiction CONTRA.
Qed.


(** #<h2>Intuicionisma loģikas priekšrocības</h2>#

#<b>Apgalvojums:</b># Intuicionisma loģikas 
pasaulē visas funkcijas no reāliem skaitļiem uz reāliem 
skaitļiem ir nepārtrauktas. 
#<br/>#
Pierādījums iziet ārpus mūsu kursa ietvariem, bet
skaidrojums ir aptuveni šāds: Klasiskās loģikas ietvaros katrs skaitlis
ir vai nu mazāks par 0 (#<tt>x&lt;0</tt>#), vai arī ir 
lielāks vai vienāds par 0 (#<tt>x&gt;=0</tt>#). Nekādas 
trešās iespējas nav, jo neviens nepazīst tādus reālus skaitļus, 
kuri nebūtu ne mazāki, ne vienādi, ne lielāki par 0. 
Tiklīdz kā mēs katram #<tt>x</tt># varam pateikt, vai tas ir 
negatīvs vai arī lielāks/vienāds par 0, tad varam uztaisīt
funkciju ar pārtraukumu: Piemēram, funkciju, kura ir -1 negatīviem 
argumentiem, bet +1 pozitīviem argumentiem vai 0. 
#<br/>#
Intuicionisma loģikas pasaulē mums skaitlis #<tt>x</tt>#
nav iedots uzreiz, bet gan tas atklājas pakāpeniski, 
darbinot kaut kādu aprēķina procedūru - jo ilgāk rēķina, jo precīzāku 
vērtību iegūst. Var gadīties, ka ļoti ilgi mēs 
saņemam vērtības, kuras nav atšķiramas no 0. Tātad skaitlis 
var būt 0. No otras puses, turpinot šo aprēķinu vēl tālāk, varētu 
atklāties, ka x patiesībā ir negatīvs. 
#<br/>#
Intuicionisma pasaulē nav grūti definēt izrēķināmas, nepārtrauktas
funkcijas, teiksim, kāpināt kvadrātā. Ja gribam precīzāku funkcijas vērtību, 
sagaidām pietiekami precīzu argumenta vērtību. 
Bet nekādus pārtraukumus/lēcienus izveidot neizdodas
kaut vai tāpēc, ka reālus skaitļus (ne šajā loģikā, ne 
arī datoru pasaulē) nevar allaž salīdzināt ar 0, cerot gūt 
rezultātu galīgā skaitā soļu.
#<br/>#
#<b>Piezīme:</b># Veselu skaitļu funkcijas, protams, var 
taisīt lēcienus, jo veselam skaitlim (arī intuicionisma pasaulē) 
ir pilnīgi skaidrs, vai tas ir mazāks par 0, vai arī vienāds/lielāks
par 0. 
*)


(** #<h2>Kura loģika darbojas rīkā Coq?</h2>#

Rīkam Coq ir vienalga, ar kādām aksiomām lietotājs strādā. 
Pats rīks uzspiež pierādījuma soļus jeb "taktikas", kuras
ļauj no aksiomām izvest lemmas un teorēmas, bet 
sākotnējās aksiomas katrs var definēt pats. To var izmantot, ja 
vajag definēt pavisam jaunus spēles noteikumus,
piemēram, sākt uzreiz ar polinomu algebru vai "parastu" skaitļu 
matemātikas vietā izdarīt apgalvojumus par Rubika kuba stāvokļiem.

Pamatojot apgalvojumus izteikumu loģikā (#<i>propositional logic</i>#) 
klasiskā no intuicioniskās loģikas atšķiras, bet šī atšķirība 
nav principiāla, jo visi pierādījumi šīs
loģikas ietvaros nozīmē darbošanos ar (iespējams, ļoti lielām, bet
tomēr galīgām) patiesuma tabulām (#<i>truth tables</i>#). 
Tas nozīmē, ka ikviens pierādījums
ir konstruktīvs un pārbaudāms ar algoritmu. 
Tas gan nenozīmē, ka arī galīgiem/kombinatoriskiem
uzdevumiem reizēm nevarētu 
izmantot nekonstruktīvus "pierādījumus no pretējā".
Tiklīdz kā apgalvojumi ir par bezgalīgām kopām (piemēram, 
naturālo skaitļu kopu), tad atšķirības kļūst pavisam ievērojamas.
*)



