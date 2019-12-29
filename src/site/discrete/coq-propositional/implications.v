(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a># 

#<h2>Implications</h2># 
If one proposition logically implies another
it is called #<i>implication</i>#. For example:
#<blockquote><u>Direct implication:</u> <b>if</b> x=2,#
#<b>then</b> x<sup>2</sup>=4.</blockquote>#
In this example the first proposition (p) is "x=2", 
the second proposition (q) is "x squared is 4".
The combined statement is #<tt>p -&gt; q</tt># 
and it is read #"<b>if</b> <tt>p</tt> <b>then</b> <tt>q</tt>"#.
#<br/>#
Note that in implication the order is relevant. For example, 
"x squared equals 4" does not necessarily imply "x=2", 
since x can also be negative 2. Nevertheless, there is 
one way to rewrite implication, and it is always equivalent
to the original implication. It is named 
#<i>contrapositive</i>#. 
#<br/>#
In our above example it would look like this: 
#<blockquote><u>Contrapositive implication:</u>#
#<b>if</b> x<sup>2</sup> is <b>not</b> 4,#
#<b>then</b> x is <b>not</b> equal to 2.</blockquote>#
*)


(** #<h2>Implication is equivalent to its Contrapositive (Proof in Coq)</h2># 
Using Coq, we show a Lemma that #<tt>p-&gt;q</tt># is
equivalent to #<tt>~q -&gt; ~p</tt>#. This means that
every direct implication always means its contrapositive implication 
and vice versa. 
To see the proof in Coq, click on the link
#<b>Proof.</b># right under the theorem.
*)

Require Import Classical_Prop.  

Lemma contrapos : forall p q: Prop, (p -> q) <-> (~q -> ~p).
Proof. 
  split.
  intros. (*r Part 1: (~ q -> ~ p) -> (p -> q) *)
  intro.
  apply H0.
  apply H.
  exact H1.
  unfold not. (*r Part 2: (~ q -> ~ p) -> (p -> q) *)
  intros.
  assert (q \/ ~q).  (*r Law of Excluded Middle *)
  unfold not.
  apply classic with (P := q). 
  destruct H1 as [H2 | H3].
  exact H2.
  pose (H H3).
  pose (f H0).
  contradiction f0.
Qed.



Lemma id_p : forall p: Prop, p -> p.
Proof.
  intros p H.
  exact H.
Qed.

Lemma imp_trans : forall p q r: Prop, (p->q)->(q->r)->p->r.
Proof.
  intros p q r.
  intros H1.
  intros H2.
  intros H3.
  apply H2.
  apply H1.
  exact H3.
Qed.


(*
https://coq.inria.fr/tutorial/1-basic-predicate-calculus
*)

Lemma or_commutative : forall a b: Prop, a \/ b -> b \/ a.
Proof. 
  intros A B H.
  elim H.
  intro HA.
  clear H.
  right.
  exact HA.
  intro HB.
  left.
  exact HB.
Qed.

Lemma or_commutative1 : forall a b: Prop, a \/ b -> b \/ a.
Proof. 
  intros a b H.
  destruct H as [HA | HB].
  right.
  exact HA.
  left.
  exact HB.
Qed.



(*
Theorem zero_not_one : 0 <> 1.
Proof.
  unfold not.
  intros contra.
  discriminate contra.
Qed. 

Theorem False_cannot_be_proven : ~False.
Proof.
  unfold not.
  intros proof_of_False.
  contradiction.
Qed.

Theorem False_implies_nonsense : False -> 2 + 2 = 5.
Proof.
  intros contra.
  contradiction.
Qed.
*)

(*
Require Import Logic.
Require Import  ClassicalFacts.
Require Import Classical_Prop.
*)




