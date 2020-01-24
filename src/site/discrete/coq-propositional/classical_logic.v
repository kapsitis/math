(** #<a href="../../discrete/coq.html">Back to Discrete Assignments</a># *)

(** * What is Intuitionistic logic *)

(** Propositional logic expressions that are 
straightforward to prove using Coq tactics
are part of so called Intuitionistic logic 
(#<i>lv:intuicionisma loģika</i>#). They 
do not use the Law of Excluded Middle 
(#<i>lv:trešā izslēgtā likumu</i>#, 
#<i>la:Tertium non datur</i>#).
*)

(*
Require Import Logic.
Require Import  ClassicalFacts.

*)


Lemma sample2: forall a: Prop, a -> ~~a.
Proof.
  unfold not. 
  intros A H1 H2.
  pose (H2 H1) as H3.
  exact H3.
Qed.


Require Import Classical_Prop.

Lemma sample3: forall a, ~ ~ (~ ~ a -> a).
Proof. 
  intros a. 
  apply sample2.
  unfold not. 
  intros H.
  destruct (classic a) as [aTrue | aFalse].
  exact aTrue.
  pose (H aFalse) as CONTRA.
  contradiction CONTRA.
Qed.


Lemma sample4: forall a: Prop, ~~a -> a. 
Proof.
  intros a. 
  unfold not.
  intros H.
  destruct (classic a) as [aTrue | aFalse].
  exact aTrue.
  pose (H aFalse) as CONTRA.
  contradiction CONTRA.
Qed.

(*
https://stackoverflow.com/questions/14644086/proving-p-q-q-p-using-coq-proof-assistant
*)
Theorem easy_contrapos: forall a b:Prop, (a->b)->(~b->~a).
Proof. 
  intros a b. 
  intros H1.
  intros bFalse.
  unfold not.
  intros aTrue.
  apply bFalse.
  apply H1.
  exact aTrue.
Qed.


Theorem hard_contrapos_with_nnpp: forall a b:Prop, (~b -> ~a) -> (a -> b).
Proof.
  intros a b. 
  intros H1.
  intros aTrue.
  apply NNPP.
  intros H2.
  apply H1 in H2.
  contradiction.
Qed.


Lemma double_negation_elimination: forall a:Prop,
  ~~a -> a.
Proof. 
  intros a.
  unfold not.
  intros H1.
  pose (classic a) as H2.
  destruct H2 as [aTrue | aFalse].
  exact aTrue.
  absurd (~a); trivial.
Qed.


Lemma double_negation_constructive: forall a:Prop,
  a -> ~~a.
Proof. 
  intros a. 
  intros aTrue.
  unfold not.
  intros aFalse.
  absurd a; trivial.
Qed.


Lemma Peirce1 : forall a:Prop, ((a -> False) -> a) -> a.
Proof.
  intros.
  apply double_negation_elimination.
  unfold not.
  intros aFalse.
  pose (H aFalse) as aTrue.
  pose (aFalse aTrue) as CONTRA.
  contradiction CONTRA.
Qed.



Lemma Peirce2 : forall a:Prop, ((a -> False) -> a) -> a.
Proof.
  intros a. 
  intros H. 
  destruct (classic a) as [aTrue | aFalse].
  exact aTrue.
  pose (H aFalse) as aTrue.
  exact aTrue.
Qed.



Lemma de_morgan_not_and_not: forall a b:Prop,
  ~(~a /\ ~b) -> a \/ b.
Proof. 
  intros a b.
  unfold not.
  intros H.
  pose (classic a) as H1.
  destruct H1 as [aTrue | aFalse]. 
  left; exact aTrue.
  pose (classic b) as H2.
  destruct H2 as [bTrue | bFalse].
  right; exact bTrue.
  assert (~a /\ ~b) as H3.
  split.
  exact aFalse.
  exact bFalse.
  pose (H H3) as CONTRA.
  contradiction CONTRA.
Qed.


Lemma implies_to_or: forall a b:Prop,
  (a -> b) -> (~a \/ b).
Proof. 
  intros a b.
  intros H1.
  pose (classic a) as H2.
  destruct H2 as [aTrue | aFalse].
  pose (H1 aTrue) as bTrue.
  right; exact bTrue.
  left; exact aFalse.
Qed.



