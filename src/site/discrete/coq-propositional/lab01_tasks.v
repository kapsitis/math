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

Lemma sample1_1: forall a b: Prop, 

(** ** Do not modify this line: sample1_2 *)

Lemma sample1_2: forall a b c: Prop









~(~a /\ a)
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

 




(** DO NOT MODIFY THIS: LABEL 1.2 *)




~~a -> a


