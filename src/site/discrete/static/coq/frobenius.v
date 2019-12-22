(* Kaut kaads pieraadiijums *)
Theorem frobenius (A: Set) (p: A -> Prop) (q : Prop) :
  (exists x: A, q /\ p x) <-> (q /\ exists x: A, p x).
Proof.
  split.
  intros.
  destruct H as [y [H1 H2]].
  split.
  assumption.
  exists y.
  assumption.
  intros.
  destruct H as [H1 [y H2]].
  exists y.
  split.
  assumption.
  assumption.
Qed.

(*  *)


Lemma example2 : forall a b:Prop, a /\ b -> b /\ a.
Proof. 
  intros a b H.
  split.
  destruct H as [H1 H2].
  assumption.
  destruct H as [H1 H2].
  assumption.
Qed.


(*
Inductive nat : Set :=
  | 0 : nat
  | S : nat -> nat.
*)

(*
Print nat.

Eval compute in 0.
Eval compute in (S 0).
Eval compute in (S (S (S 0))).
*)
