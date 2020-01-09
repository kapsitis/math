(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a># 

#<h2>One Jazz Song</h2>#
Let us analyze one song from 1924 that later became  
one of the "standard songs", that has been sung by many people 
at different times. 
#<a href="https://en.wikipedia.org/wiki/Everybody_Loves_My_Baby">Everybody Loves My Baby (But My Baby Don't Love Nobody But Me)</a>#;
music by #<i>Spencer Williams</i>#, lyric by
#<i>Jack Palmer</i># (see 
#<a href="https://www.youtube.com/watch?v=U2BtteA0k8o">Video</a>#). 

This example is also analyzed in this textbook:
#<a href="https://learning.oreilly.com/library/view/logic-as-a/9781118880005/c04.xhtml">Logic# 
#as a Tool by Valentin Goranko, 2016.</a>#

Let us consider the title of the song.
#<i>"Everybody Loves My Baby (But My Baby Don't Love Nobody But Me)"</i>#.
This mentions humans #<tt>MyBaby</tt># and #<tt>Me</tt># satisfying properties:
#<ol type="A"><li>Every human loves <tt>MyBaby</tt></li>#
#<li>On the other hand <tt>MyBaby</tt> does not love anyonee except <tt>Me</tt></li># 
#</ol>#

If #<tt>L(x,y)</tt># is the predicate to denote that 
x loves y, then for every human #<tt>x</tt>#: #<tt>L(x,MyBaby)</tt>#. 
In the meantime: for every human #<tt>y</tt>#, as long as #<tt>y</tt># is
not equal to #<tt>Me</tt>#, then #<tt>~L(MyBaby,y)</tt># 
(#<tt>MyBaby</tt># does not love #<tt>y</tt>#).

Let us prove that in this case #<tt>MyBaby</tt># and #<tt>Me</tt>#
is the same human being (two names for the same real-life object). 
An informal outline of the proof is as follows:
#<ul><li>Denote the set of all humans by <tt>HUM</tt>;#
#locate elements <tt>MyBaby</tt> and <tt>Me</tt> in this set.</li>#
#<li>From the contrary, assume that they differ: <tt>MyBaby&lt;&gt;Me</tt>.</li>#
#<li>Substitute in the property (B) <tt>y = MyBaby</tt>#
#<li>From the assumption (B) <tt>MyBaby</tt> and <tt>Me</tt> should differ:#
#<tt>MyBaby</tt> cannot love itself, since <tt>MyBaby</tt> only loves <tt>Me</tt></li>#
#<li>On the other hand, by assumption (A) <b>everybody</b> must love <tt>MyBaby</tt>.#
#Certaintly, this includes <tt>MyBaby</tt> who also loves <tt>MyBaby</tt>.</li>#
#<li>This is a contradiction. Therefore <tt>MyBaby=Me</tt></li></ul>#
*)

(** Here the same proof is formalized with Coq. 
#<tt>HUM</tt># is the set of all humans. *)
Parameter HUM : Type.
(** Me and MyBaby are humans. *)
Parameter Me : HUM.  
Parameter MyBaby : HUM.

(** The predicate #<tt>L(x,y)</tt># is true if and only if
#<tt>x</tt># loves #<tt>y</tt>#. *)
Parameter L : HUM*HUM -> Prop. 

Require Import Coq.Logic.Decidable.
Print contrapositive.



Axiom contrapos : forall p q: Prop, (p -> q) <-> (~q -> ~p).


(** We prove that #<tt>MyBaby</tt># and #<tt>Me</tt># 
are equal. 
To see the proof, click on the link #<b>Proof.</b># 
right under the theorem.
*)
Theorem who_is_mybaby: (forall x: HUM, L(x,MyBaby)) /\ 
  (forall y: HUM, ~(y=Me) -> ~(L(MyBaby,y))) -> MyBaby=Me.
Proof. 
  intros [ItemA ItemB].  (* Both song facts: ItemA and ItemB. *)
  assert (MyBaby <> Me -> ~L(MyBaby,MyBaby)).  (* Let us prove that MyBaby does not love itself. *)
  apply ItemB with (y := MyBaby).  (* substitute in (B): y=MyBaby. *)
  assert (L(MyBaby,MyBaby)).  (* On the other hand MyBaby should love itself. *)
  apply ItemA with (x := MyBaby).
  clear ItemA ItemB.  (* Song facts no longer needed. *)
  elim (contrapos (L(MyBaby,MyBaby)) (MyBaby = Me)).
  intros.
  clear H1.
  pose (H2 H) as H3.
  pose (H3 H0) as H4.
  exact H4.
Qed. 












