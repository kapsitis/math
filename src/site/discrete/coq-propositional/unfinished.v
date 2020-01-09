
Require Import  ClassicalFacts.
Require Import Classical_Prop.

Theorem restricted_excluded_middle : forall (P:Prop) (b:bool),
  (P <-> b = true) -> P \/ ~P.
Proof.
  intros P [] H.
  - left. rewrite H. reflexivity.
  - right. rewrite H. intros contra. discriminate contra.
Qed.

Require Import Bool. 
Require Import Arith.

Theorem restricted_excluded_middle_eq : forall n m : nat,
  n = m \/ n <> m.
Proof.
  intros n m.
  apply (restricted_excluded_middle (n = m) (beq_nat n m)).
  symmetry.
  apply eqb_eq.
Qed.