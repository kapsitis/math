(* 
This file contains all the tautologies taken from the 
SUNY Buffalo CSE 191 Course (by Knepley):
https://cse.buffalo.edu/~knepley/classes/cse191/ClassNotes.pdf
Start with Page 12. 

See also - for more guidance how to prove tautologies.
https://coq.inria.fr/tutorial/1-basic-predicate-calculus
*)

Section Logic_Examples.
Variables P Q R S : Prop.

(* Using the assumption to prove the goal. *)
Lemma id_P : P->P.
Proof.
intros H.
assumption.
Qed.

Print id_P.

(* Applying Modus Ponens multiple times. *)
Lemma imp_trans : (P->Q)->(Q->R)->P->R.
Proof. 
  intros H1.
  intros H2.
  intros hyp_PTrue.
  apply H2.
  apply H1.
  assumption.
Qed.

(* Destruct the hypothesis and split the goal. *)
Lemma and_comm: (P /\ Q) -> (Q /\ P).
Proof. 
  intros H.
  destruct H as [HLeft HRight].
  split.
  assumption. 
  assumption.
Qed.


(* Strategy: Proof by cases.  *)
Lemma or_comm : (P \/ Q) -> (Q \/ P).
Proof. 
  intros H.
  destruct H as [HLeft|HRight].
  right. assumption.
  left. assumption.
Qed.


Locate  "~".
Locate  "<->".
Locate  "/\".
Locate  "\/".
Locate  "->".


(* 'Law of noncontradiction' *)
Lemma noncon : ~(P /\ ~P).
Proof.
  unfold not.
  intros H.
  destruct H as [hyp_PTrue hyp_PFalse].
  apply hyp_PFalse.
  exact hyp_PTrue.
Qed.




