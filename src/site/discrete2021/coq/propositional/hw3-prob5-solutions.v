Section A6toA1.

Axiom ContraPos: forall p q: Prop, (p -> q) <-> (~q -> ~p).  (* (6) *)

(*
Lemma ExcludedMiddle: forall p: Prop, (p \/ ~p). 
Proof.
  intros p. 
*)

Require Import Classical_Prop.

Lemma ImplToDisjClassic: forall a b: Prop, (a -> b) -> (~a \/ b).
Proof.
  intros a b.
  intros H.
  pose (classic a) as H2.
  destruct H2 as [aTrue|aFalse].
  right. 
  apply H.
  exact aTrue.
  left. 
  exact aFalse.
Qed.


Require Import Classical_Prop.

Lemma PeirceLaw1: 
    forall a b: Prop, ((a -> b) -> a) -> a.
Proof. 
  intros a b.
  intros H.
  pose (classic a) as H4.
  destruct H4 as [aTrue|aFalse].
  exact aTrue.
  unfold not in aFalse.
  apply H.
  intros H5.
  contradiction (aFalse H5).
Qed.

Lemma Peirce_Law2: 
    forall a b: Prop, ((a -> b) -> a) -> a.
Proof.
  intros a b.
  intros H1.
  apply NNPP.
  unfold not.
  intros aFalse.
  apply aFalse.
  apply H1.
  intros aTrue.
  contradiction (aFalse aTrue).
Qed.


Lemma NNPPUsingClassic:
    forall a: Prop, ~~a -> a.
Proof.
  intros a. 
  intros H.
  unfold not in H.
  pose (classic a) as H2.
  destruct H2 as [aTrue|aFalse].
  exact aTrue.
  pose (H aFalse) as H3.
  contradiction H3.
Qed.



(*
Lemma ImplToDisj: forall a b: Prop, (a -> b) -> (~a \/ b).
Proof.
  intros a b.
  intros H.
  pose (ContraPos a b) as H2.
  unfold iff in H2.
  destruct H2 as [H3 H4].
  pose (H3 H) as H5.
  unfold not.
*)






Lemma Peirce_Law: forall a b: Prop, ((a -> b) -> a) -> a. (* (1) *)
Proof.
  intros a b.
  intros H1.
  pose (ContraPos (a -> b) (a)) as H2.
  destruct H2 as [H3 _].
  pose (H3 H1) as H4.
  unfold not in H4.

