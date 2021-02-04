Section Predicate_Logic_Examples.

(* A is a nonempty set (containing element 'something' *)
Variables A : Set.
Variables something: A.
(* Assume that P,Q are 1-argument predicates defined on A *)
Variables P Q : A->Prop. 


(* Can distribute 'exists' quantifier over a disjunction *)
Lemma distribute_exists: 
    (exists (y:A), (P y)) \/ (exists (y:A), (Q y)) <-> 
    exists (x:A), (P x) \/ (Q x).
Proof. 
  split. 
  intros H.
  destruct H as [H1 | H2].
  destruct H1 as [y H3].
  exists y. left. exact H3.
  destruct H2 as [y H3].
  exists y. right. exact H3.
  intros H.
  destruct H as [x H1].
  destruct H1 as [H2 | H3].
  left. exists x. exact H2.
  right. exists x. exact H3.
Qed.



Lemma sample5_1: 
    (forall (x:A), (P x) /\ (Q x)) <-> (forall (x:A),(P x)) /\ (forall (x:A), (Q x)).
Proof. 
  split.
  intros H.
  split. 
  intros x0.
  apply (H x0). 
  intros x1.
  apply (H x1).
  intros H.
  destruct H as [H1 H2].
  intros x2.
  split.
  apply (H1 x2).
  apply (H2 x2).
Qed.


Require Import Classical_Prop.



(* One variant of De Morgans law *)
Lemma sample5_2: (exists (x:A), ~~(P x)) <-> ~(forall (y:A), ~(P y)).
Proof. 
  split. 
  intros H.
  destruct H as [x H1].
  intros H2.
  pose (H2 x) as H3.
  contradiction (H1 H3).
  intros H.
  apply NNPP.
  intros H2.
  apply H.
  intros y. 
  intros H3.
  apply H2.
  exists y.
  intros H4.
  contradiction (H4 H3).
Qed.



(* If (P x) always implies (Q x), then the existence 
   of some (P x0) leads to existence of some (Q x1) *)
Lemma sample5_3: (forall (x:A), P x -> Q x) -> ((exists (x:A), (P x)) -> exists (x:A), (Q x)).
Proof. 
  intros H1. 
  intros H2.
  destruct H2 as [x1 H3].
  exists x1. 
  apply (H1 x1).
  exact H3.
Qed.


(*
Lemma L2: (exists (x:A), (P(x) -> Q(x))) <-> ((exists (x:A), (P x)) -> (exists (x:A), (Q x))).
Proof. 
  split.
  intros H.
  destruct H as [x H2].
  intros H3.
  destruct H3 as [x1 H4].
  exists x1.
  Admitted.
*)


(* If P being true sometimes implies that also Q is true sometimes, 
   then there is some x0 for which (P x) implies (Q x) *)
Lemma sample5_4: ((exists (x:A), (P x)) -> (exists (x:A), (Q x))) -> (exists (x:A), ((P x) -> (Q x))).
Proof.
  intros H.
  pose (classic (exists x : A, P x)) as H2.
  destruct H2 as [H3 | H4].
  pose (H H3) as H5.
  destruct H5 as [x0 H6].
  exists x0.
  intros H7.
  exact H6.
  exists something.
  intros H5.
  assert (exists x : A, P x).
  exists something.
  exact H5.
  contradiction (H4 H0).
Qed.


(* If P(x) always implies Q(x), and P(x) is always true, then Q(x) is always true. *)
Lemma sample5_5: (forall (x:A), ((P x) -> (Q x))) -> ((forall (x:A), (P x)) -> forall (x:A), (Q x)).
Proof. 
  intros H.
  intros H2.
  intros x.
  pose (H x) as Hx.
  pose (H2 x) as H2x.
  apply (Hx H2x).
Qed.



Lemma L4: ((forall (x:A), (P x)) -> (forall (x:A), (Q x))) -> (exists (x:A), (P x) -> (Q x)).
Proof. 
  intros H.
  destruct (classic (forall x : A, P x)) as [AllP | NotAllP].
  pose (H AllP) as H2.
  exists something.
  intros H3.
  apply H2.
  unfold not in NotAllP.

  assert (exists y, ~(P y)). 
  apply NNPP.
  intros H3.
  apply NotAllP.
  intros x.
Admitted.


  










  












End Predicate_Logic_Examples.