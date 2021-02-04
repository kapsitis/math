(* ***************************** *)


(* If 'a' is both True and False, it implies any 'b' *)
Lemma sample1: forall a b: Prop, ~a -> a -> b.
Proof.
  intros a b.
  unfold not.
  intros aFalse.
  intros aTrue.
  pose (aFalse aTrue) as H2.
  contradiction H2.
Qed.

(* One can write this a bit shorter *)
Lemma sample1_VAR: forall a b: Prop, ~a -> a -> b.
Proof.
  intros a b.
  unfold not.
  intros aFalse aTrue.
  contradiction (aFalse aTrue).
Qed.

(* NOTE: You cannot switch places  for 'aFalse aTrue' in the last line. 
One cannot 'plug in' '(a -> False)' into expression 'a'. 
But one can 'plug in' 'a' into 'a -> False' and get 'False', a contradiction. *)



(* If a=True, but b=False, then implication (a ->b) is always False. *)
Lemma sample2: forall a b: Prop, a -> (~b -> ~(a -> b)).
Proof.
  intros a b.
  unfold not.
  intros aTrue bFalse.
  intros H.
  apply bFalse.
  apply H.
  apply aTrue.
Qed. 

(* NOTE: In this example we reasoned 'backwards' with three 'apply' tactics.
(1) replaced the goal False  by 'b', 
(2) replaced the goal 'b' by 'a',
(3) finally, we know that 'a' is true. 
*)

(* One can write this a bit shorter *)
Lemma sample2_VAR: forall a b: Prop, a -> (~b -> ~(a -> b)).
Proof.
  unfold not.
  intros a b aTrue bFalse H.
  apply (bFalse (H aTrue)).
Qed.

(* The last line works just like a 'function composition': 
Normal people would write this like this: 
bFalse(H(aTrue))
The inner expression is H(aTrue)=b.
The expression bFalse(b)=False. (this is our goal).
*)

(* The last goal is False; so it is also a contradiction *)
Lemma sample2_VARVAR: forall a b: Prop, a -> (~b -> ~(a -> b)).
Proof.
  unfold not.
  intros a b aTrue bFalse H.
  contradiction (bFalse (H aTrue)).
Qed.


(* *********************************** *)
(* Import some axioms; Prepare to do   *)
(* some classic/non-constructive stuff *)
(* *********************************** *)
Require Import Classical_Prop.

(* If implication (a -> b) is False, then 'a' must be True *)
Lemma sample3: forall a b: Prop, ~(a -> b) -> a.
Proof.
  intros a b H1.
  apply NNPP.
  unfold not.
  intro H2.
  apply H1.
  intro aTrue.
  contradiction (H2 aTrue).
Qed.

(* 'apply NNPP' simply added two negations to the goal. 
The axiom NNPP means '~~a -> a', so you can reason backwards.
This step gave some additional possibilities, when we were stuck. *)


(* Type this to display meaning of this symbol *)
Print NNPP.
(* Note that this lemma NNPP (just like the lemmas that
we are doing is, in fact, a function. 
It eats one parameter: 
fun (p : Prop) 
(....SOME BODY - It can execute some proof inside...)
And finally the 'usable stuff': ~ ~ p -> p *)





(* If both 'a' and 'b' are False, then the disjunction 'a \/ b' is False *)
Lemma sample4: forall a b: Prop, ~a -> ~b -> ~(a \/ b).
Proof.
  intros a b.
  unfold not.
  intros aFalse bFalse.
  intros aORb.
  destruct aORb as [aTrue | bTrue].
  contradiction (aFalse aTrue).
  contradiction (bFalse bTrue).
Qed.

(* NOTE: This shows a standard way to 'destruct' disjunctions in hypotheses: 
Sort two cases: Left side of aORb (in our case it is aTrue). 
The right side of aORb (in our case it is bTrue). 
In both cases we get a contradiction. *)


Lemma sample5: forall a b: Prop, ~(a /\ b) -> (b -> ~a).
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


(* NOTE: This shows a standard way to 'split' conjunction in the goal.
Split into two subgoals. 
First prove the left part of the conjunction, then prove the right part. *)


(* Non-constructive stuff: 
If ~b implies ~a, and ~b also implies a, 
then b must be true *)
Lemma sample6: forall a b: Prop, (~b -> ~a) -> (~b -> a) -> b.
Proof.
  intros a b.
  unfold not.
  intros H1.
  intros H2.
  pose (classic b) as H3.
  destruct H3 as [bTrue | bFalse].
  exact bTrue.
  pose (H1 bFalse) as aFalse.
  pose (H2 bFalse) as aTrue.
  contradiction (aFalse aTrue).
Qed.

(* NOTE: Here is one new trick: First introduce 'classic' axiom; 
then immediately destruct it into two subcases: 
(1) b=True. (Really easy case)
(2) b=False. In this situation we get contradictions with our earlier hypotheses.
*)


(* Similar to the previous result: 
If ~b implies ~a, and ~b also implies a, 
then b must be true *)
Lemma sample7: forall a b: Prop, (a -> b) -> (~a -> b) -> b.
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

(* NOTE: Very similar to the previous case; 
but it shows that you should pay attention to what 
'classic' axiom you need. In this case we wanted to sort two cases:
(1) a = True
(b) b = False
*)


(* Similar to sample6, but not exactly the same *)
Lemma sample8: forall a b: Prop, (a -> b) -> (a -> ~b) -> ~a.
Proof.
  intros a b.
  intros H1.
  intros H2.
  pose (classic a) as H3.
  destruct H3 as [aTrue | aFalse].
  contradiction ((H2 aTrue) (H1 aTrue)).
  exact aFalse.
Qed.

(* NOTE the strange expression that gives contradiction. 
If this seems too fast, 
you can rewrite this into several lines:

THIS:
=====
contradiction ((H2 aTrue) (H1 aTrue)).

IS THE SAME AS THIS:
====================
pose (H1 aTrue) as bTrue.
pose (H2 aTrue) as bFalse.
contradiciton (bFalse bTrue) as CONTRA.
*)



Lemma sample9: forall a b: Prop, (~b -> a) -> (b -> a) -> a.
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

(* NOTE: In the last few proofs there is almost a pattern: 

pose (classic b) as H3.
destruct H3 as [bTrue | bFalse].

In the following proof we show that you can 
rewrite this in a single line; and (instead of sorting two hypotheses)
prove two separate goals.
*)


(* If 'a','b' are either both True or both False, then ~a OR b must be True. *)
Lemma sample10: forall a b: Prop, (a <-> b) -> (~a \/ b).
Proof.
  intros a b.
  intros H1.
  destruct H1 as [H2 H3].
  elim (classic a).
  intros aTrue.
  right. 
  apply (H2 aTrue).
  intros aFalse.
  left.
  exact aFalse.
Qed.


(* If 'a','b' both together imply 'c'; and also 'a->b', then 'a->c' *)
Lemma sample11: forall a b c: Prop, (a -> b -> c) -> (a -> b) -> (a -> c). 
Proof.
  intros a b c H1 H2 aTrue.
  apply (H1 aTrue).
  apply (H2 aTrue).
Qed.

(* NOTE: Some implications are easy, if they are constructive and
you can apply Modus Ponens - i.e. simply 'plug in' one expression into another *)


(* 'a' implies 'b -> c' iff 'a and b' together imply 'c' *)
Lemma sample12: forall a b c: Prop, (a -> b -> c) <-> ((a /\ b) -> c).
Proof.
  intros a b c.
  split.
  - intros H1.
    intros [aTrue bTrue].
    exact (H1 aTrue bTrue).
  - intros H2.
    intros aTrue bTrue.
    assert (a /\ b) as H3.
    split.
    + exact aTrue.
    + exact bTrue.
    + pose (H2 H3) as cTrue.
      exact cTrue.
Qed.

(* Tactic 'split' is useful when proving conjunctions and also equivalences. 
In this case we need to check the statement in both directions. 

THIS:
=====
intros [aTrue bTrue].

IS SAME AS THIS:
================
intros myHypothesis. 
destruct myHypothesis as [aTrue bTrue].


Preceding your subcases with '+' and '-' is sometimes 
used to split long proofs in shorter sections.
It may keep things cleaner and more focused, 
but splitting into sections is not mandatory.
*)


(* If both (a->c) and (b->c), and you know that (a \/ b) is True, then c is True *)
Lemma sample13: forall a b c: Prop, (a -> c) -> (b -> c) -> (a \/ b) -> c. 
Proof.
  intros a b c.
  intros H1.
  intros H2.
  intros [aTrue | bTrue].
  exact (H1 aTrue).
  exact (H2 bTrue).
Qed.


(*
NOTE: One more little shorthand: 

THIS:
=====
intros [aTrue | bTrue].

IS SAME AS THIS:
intros H.
destruct H as [aTrue | bTrue].
*)

(* Just a statement that if (a->b) and (c->a), then (c->b). 
Transitivity - similar to the problem in Homeowork 2, Q2.C. 
It was about the plane/railway traffic being transitive.
*)
Lemma sample14: forall a b c: Prop, (a -> b) -> (c -> a) -> (c -> b).
Proof.
  intros a b c.
  intros H1 H2 cTrue.
  exact (H1 (H2 cTrue)).
Qed.



(* Some variant to say that disjunction is associative; and one can regroup. *)
Lemma sample15: forall a b c: Prop, a \/ (b \/ c) -> (b \/ (a \/ c)) \/ a.
Proof.
  intros a b c.
  intros [H2 | H3].
  right; exact H2.
  destruct H3 as [H4 | H5].
  left; left; exact H4.
  left; right; right; exact H5.
Qed.

(*
The long expression with semicolons (;)
left; right; right; exact H5.

applies all the goals right after one another (one big jump). 

What happens? We have the following goal: 
(b \/ a \/ c) \/ a
It seems that disjunction is right-associative: 
(b \/ a \/ c) \/ a = (b \/ (a \/ c)) \/ a. 

Our hypothesis H5 says that 'c' must be True. 
We can 'drill down' to that variable: 
'left' on '(b \/ (a \/ c)) \/ a' is '(b \/ (a \/ c))' 
'right' on '(b \/ (a \/ c))' is '(a \/ c)'.
'right' on '(a \/ c)' is 'c'. 
It is exactly our hypothesis H5. 
*)



(* Realy easy lemma: If 'a' and then 'b' both imply 'c', 
then 'b' and 'a' (switched places) imply 'c'
*)
Lemma sample16: forall a b c: Prop, (a -> (b -> c)) -> (b -> (a -> c)).
Proof.
  intros a b c. 
  intros H bTrue aTrue.
  exact ((H aTrue) bTrue).
Qed.

(* NOTE:
Here we pass two arguments to the 'two-argument' hypothesis H. 

The notation:
=============
(H aTrue bTrue)
or ((H aTrue) bTrue)

is not the same as:
===================
(H (aTrue bTrue))

Function/implication application is left-associative.
*)


(* Implication is transitive'; similar to 'sample14', but switched order. *)
Lemma sample17: forall a b c: Prop, (a -> b) -> (b -> c) -> (a -> c).
Proof.
  intros a b c H1 H2 aTrue.
  exact (H2 (H1 aTrue)).
Qed. 

(* NOTE: 
In this case we need to group the function application from right to left *)


(* If (a and b) imply c, then 'a' implies that 'b' implies 'c' *)
Lemma sample18: forall a b c: Prop, ((a /\ b) -> c) -> (a -> (b -> c)).
Proof.
  intros a b c.
  intros H1 aTrue bTrue.
  assert (a /\ b) as aANDb.
  split.
  exact aTrue.
  exact bTrue.
  exact (H1 aANDb).
Qed. 


(* 'a' implies 'b and c'  iff  'a->b' and 'a->c' *)
Lemma sample19: forall a b c: Prop, (a -> b /\ c) <-> (a -> b) /\ (a -> c).
Proof.
  intros a b c.
  split.
  - intros H1.
    split.
    + intros aTrue.
      destruct (H1 aTrue) as [bTrue _].
      exact bTrue.
    + intros aTrue.
      destruct (H1 aTrue) as [_ cTrue].
      exact cTrue.
  - intros [H2 H3].
    intros aTrue.
    split.
    + exact (H2 aTrue).
    + exact (H3 aTrue).
Qed.

(* Once again a long proof structured into subsections *)



(* The final 2 lemmas are not too intuitive, but they are also tautologies *)
Lemma sample20: forall a b c d e: Prop, 
    ((((a -> b) -> (~c -> ~d)) -> c) -> e) -> ~a -> (d -> e).
Proof. 
  intros a b c d e.
  intros H1.
  intros aFalse.
  intros dTrue.
  assert (((a -> b) -> ~ c -> ~ d) -> c) as H4.
  intros H5.
  assert (a -> b) as H6.
  intros aTrue.
  contradiction (aFalse aTrue).
  pose (H5 H6) as H7.
  apply NNPP.
  unfold not.
  intros cFalse.
  contradiction ((H7 cFalse) dTrue).
  exact (H1 H4).
Qed.


Corollary longTautology: forall a b c d e: Prop, 
    ((((a -> b) -> (~c -> ~d)) -> c) -> e) -> ((e -> a) -> (d -> a)).
Proof.
  intros a b c d e.
  intros H1 H2 dTrue.
  destruct (classic a) as [aTrue | aFalse]. 
  exact aTrue.
  pose (sample20 a b c d e) as H3.
  pose (H3 H1) as H4.
  pose (H4 aFalse) as H5.
  pose (H5 dTrue) as eTrue.
  pose (H2 eTrue) as aTrue.
  exact aTrue.
Qed.




