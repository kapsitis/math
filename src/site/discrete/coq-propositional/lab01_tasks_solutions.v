(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a>#  *)

(** * Lab01: Proving Propositional Statements in Coq: Solutions *)

(** ** Do not modify this line: sample1_1 *)

Lemma sample1_1: forall a b: Prop, ~a -> (a -> b).
Proof.
  intros a b.
  unfold not.
  intros aFalse.
  intros aTrue.
  pose (aFalse aTrue) as CONTRA.
  contradiction CONTRA.
Qed.

(** ** Do not modify this line: sample1_2 *)

Lemma sample1_2: forall a b: Prop, a -> (~b -> ~(a -> b)).
Proof.
  intros a b.
  unfold not.
  intros aTrue bFalse.
  intros H.
  pose (H aTrue) as bTrue.
  pose (bFalse bTrue) as CONTRA.
  contradiction CONTRA.
Qed.


(** ** Do not modify this line: sample1_3 *)

Require Import Classical_Prop.

Axiom CounterPos: forall a b: Prop, (~b -> ~a) -> (a -> b).

Axiom CounterPos2: forall a b: Prop, (a -> b) -> (~b -> ~a).


Lemma sample1_3: forall a b: Prop, ((a -> b) -> a) -> a.
Proof.
  intros a b.
  intros H.
  Admitted.

  

(** ** Do not modify this line: sample1_4 *)

Lemma sample1_4: forall a b: Prop, ~a -> (~b -> ~(a \/ b)).
Proof.
  intros a b.
  unfold not.
  intros aFalse.
  intros bFalse.
  intros aORb.
  destruct aORb as [aTrue | bTrue].
  pose (aFalse aTrue) as CONTRA1.
  exact CONTRA1.
  pose (bFalse bTrue) as CONTRA2.
  exact CONTRA2.
Qed.

(** ** Do not modify this line: sample1_5 *)

Lemma sample1_5: forall a b: Prop, ~(a /\ b) -> (b -> ~a).
Proof.
  intros a b.
  unfold not.
  intros H.
  intros bTrue.
  intros aTrue.
  apply H.
  split.
  exact aTrue.
  exact bTrue.
Qed.



(** ** Do not modify this line: sample1_6 *)

Lemma sample1_6: forall a b: Prop, (~b -> ~a) -> ((~b -> a) -> b).
Proof.
  intros a b.
  unfold not.
  intros H1.
  intros H2.
  pose (CounterPos a b) as H3.
  pose (H3 H1) as H4.
  
  Admitted.

(** ** Do not modify this line: sample1_7 *)

Lemma sample1_7: forall a b: Prop, (a -> b) -> ((~a -> b) -> b).
Proof.
  intros a b.
  intros H1.
  intros H2.
  pose (classic a) as H3.
  destruct H3 as [aTrue | aFalse].
  apply H1.
  exact aTrue.
  apply H2.
  exact aFalse.
Qed.


(** ** Do not modify this line: sample1_8 *)

Lemma sample1_8: forall a b: Prop, (a -> b) -> ((a -> ~b) -> ~a).
Proof.
  intros a b.
  intros H1.
  intros H2.
  pose (classic a) as H3.
  destruct H3 as [aTrue | aFalse].
  pose (H1 aTrue) as bTrue.
  pose (H2 aTrue) as bFalse.
  pose (bFalse bTrue) as CONTRA.
  contradiction CONTRA.
  exact aFalse.
Qed.

(** ** Do not modify this line: sample1_9 *)

Lemma sample1_9: forall a b: Prop, (~b -> a) -> ((b -> a) -> a).
Proof.
  intros a b.
  unfold not.
  intros H1.
  intros H2.
  pose (classic b) as H3.
  destruct H3 as [bTrue | bFalse].
  pose (H2 bTrue) as aTrue.
  exact aTrue.
  pose (H1 bFalse) as aTrue.
  exact aTrue.
Qed.


(** ** Do not modify this line: sample1_10 *)

Lemma sample1_10: forall a b: Prop, (a <-> b) -> (~a \/ b).
Proof.
  intros a b.
  intros H1.
  destruct H1 as [H2 H3].
  unfold not.
  split.



(** ** Do not modify this line: sample1_11 *)

Lemma sample1_11: forall a b c: Prop, (a -> (b -> c)) -> ((a -> b) -> (a -> c)).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_12 *)

Lemma sample1_12: forall a b c: Prop, (a -> (b -> c)) <-> ((a /\ b) -> c).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_13 *)

Lemma sample1_13: forall a b c: Prop, (a -> c) -> ((b -> c) -> ((a \/ b) -> c)).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_14 *)

Lemma sample1_14: forall a b c: Prop, (a -> b) -> ((c -> a) -> (c -> b)).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_15 *)

Lemma sample1_15: forall a b c: Prop, a \/ (b \/ c) -> ((b \/ (a \/ c)) \/ a).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_16 *)

Lemma sample1_16: forall a b c: Prop, (a -> (b -> c)) -> (b -> (a -> c)).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_17 *)

Lemma sample1_17: forall a b c: Prop, (c -> a) -> ((a -> b) -> (c -> b)).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_18 *)

Lemma sample1_18: forall a b c: Prop, ((a /\ b) -> c) -> (a -> (b -> c)).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_19 *)

Lemma sample1_19: forall a b c: Prop, (a -> b /\ c) <-> (a -> b) /\ (a -> c).
Proof.
  tauto.
Qed.

(** ** Do not modify this line: sample1_20 *)

Lemma sample1_20: forall a b c d e: Prop, 
    ((((a -> b) -> (~c -> ~d)) -> c) -> e) -> ((e -> a) -> (d -> a)).
Proof.
  Admitted.









