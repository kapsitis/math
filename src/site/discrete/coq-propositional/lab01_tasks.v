(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a>#  *)

(** * Lab01: Proving Propositional Statements in Coq *)

(** #<b>Description:</b># We expect to have 5 Coq-related 
exercises and 2 Scala programming exercises. This 

(* DO NOT MODIFY THIS COMMENT: EXERCISE 1.1 *)

(** #<h2>Exercise 1.1</h2># 
#<tt>fun1_1</tt># is defined below. It is a 
function with 3 "bool" arguments. It is equal to 
this expression: 
#<br/>#
#<tt>(p \/ ~ (q /\ ~r)) -> (~~r)</tt>#
#<br/>#
Assume that the Boolean variables (p,q,r) take all 8 possible 
value combinations: (true,true,true), (true,true,false), ...,
(false,false,false). Compute the truth table and assign it
to a list variable 
*) 

Require Import Bool.
Require Import List.

(** This definition is fine, no need to edit this *)
Definition fun_1_1 (p:bool) (q:bool) (r:bool) : bool :=
  implb (p || negb (q && (negb p))) (negb (negb r)).

(** The truth table is probably wrong. Make sure that you 
write the actual 8 values. The first value in the list should 
be "fun_1_1 true true true" and so on. *)

Definition truthTable_1_1 := 
  true::false::false::false::false::false::false::false::nil.


(** DO NOT MODIFY THIS COMMENT - LABEL 1.2 *)

(** #<h2>Exercise 1.2</h2># 

*)

Require Import Arith.


Check 2+2.


(*
Lemma sample1: forall p:Prop, p -> p.
Proof.
  intros p.
  intros pTrue.
  exact pTrue.
Qed.

Lemma sample2: forall p:Prop, False -> p.
Proof.
  intros p.
  intros FF.
  contradict FF.
Qed.

Show Script.
*)


(*
More things to check with Coq.

Check types in Coq, including atomic types, tuples, function types.
Use and build truth tables for Boolean operators.
Use precedence and associativity to parse Boolean expressions.
Fill in truth tables.
Check, if a Boolean expression is a tautology.
Check, if a Boolean expression is satisfiable.
Find equivalent Boolean expressions.
Rewrite expressions as CNF (conjunctive normal form).
*)

