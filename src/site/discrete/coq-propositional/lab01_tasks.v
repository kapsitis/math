(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a>#  *)

(** * Lab01: Proving Propositional Statements in Coq *)

(** In all the exercises replace #<b>Admitted.</b># 
with a proof. Enclose it between #<b>Proof.</b># and #<b>Qed.</b># 
#<b>Note:</b> If you can prove them without assuming extra axioms 
(such as "classic") such proofs would preferable, but
you can import and use any statements you need.

Some of the tautologies mentioned in the examples are in 
the Rosen2019 textbook, at the end of Subsection 1.3. 
*)

(** ** Do not modify this line: sample1_1 *)

Lemma sample1_1: forall a: Prop, ~(~a /\ a). 
Proof.
  intros a.
  unfold not.
  intros.
  destruct H as [H1 H2].
  apply H1.
  exact H2.
Qed.


(** ** Do not modify this line: sample1_2 *)

Lemma sample1_2: forall a: Prop, a -> ~~a.
Proof. 
  intros a. 
  unfold not.
  intros H1.
  intros H2.
  apply H2.
  exact H1.
Qed.

Require Import  ClassicalFacts.
Require Import Classical_Prop.

(*
Print ClassicalFacts.
*)
Print excluded_middle.
Check excluded_middle.

Variable xx: Prop.

Check (classic xx).
Check classic.


Lemma NNPeirce : forall A B: Prop, ~~(((A -> B) -> A) -> A).
Proof. 
  tauto.
Qed. 



Axiom ExcludedMiddle: forall A:Prop, A \/ ~ A.


(** ** Do not modify this line: sample1_3 *)

Lemma sample1_3: forall a:Prop, ~~a -> a.
Proof. 
  intros a. 
  unfold not.
  intros.
  elim (ExcludedMiddle a).
  intros aTrue.
  exact aTrue.
  intros aFalse.
  pose (H aFalse) as CONTRA.
  contradiction CONTRA.
Qed.


Axiom NegNeg: forall A:Prop, ~~A -> A.


Require Import Classical.


Lemma sample1_4: forall a:Prop, ~~(~~a -> a).
Proof.
  intros a.
  assert (~~(~~a -> a) -> (~~a -> a)).
  elim (NegNeg a).


  elim (sample1_3 a).

 








(*
~~(~~a -> a)
~~~a -> ~a
a -> (b -> a).
a /\ b -> a.
~b -> (b -> c)
a -> (a \/ b).
~a -> (a -> b)
a -> (~a -> b)
(~a -> a) -> a
(~b -> ~a) -> (a -> b)
(a -> b) -> (~b -> ~a)
a -> (~b -> ~(a -> b))
((a -> b) -> a) -> a
a -> (b -> (a /\ b)).
~b -> (~c -> ~(b \/ c))
~(a /\ b) -> (b -> ~a)
(~b -> ~a) -> ((~b -> a) -> b)
(a -> b) -> ((~a -> b) -> b)
(a -> b) -> ((a -> ~b) -> ~a)
(~b -> a) -> ((b -> a) -> a)
(a -> (b -> c)) -> ((a -> b) -> (a -> c)).
(a -> (b -> c)) <-> ((a /\ b) -> c)
(a -> c) -> ((b -> c) -> ((a \/ b) -> c)).
(a -> b) -> ((c -> a) -> (c -> b))
a \/ (b \/ c) -> ((b \/ (a \/ c)) \/ a)
(a -> (b -> c)) -> (b -> (a -> c))
(c -> a) -> ((a -> b) -> (c -> b)).
((a /\ b) -> c) -> (a -> (b -> c))
*)
 





