(** #<a href="../../discrete/assignments.html">Back to Discrete Assignments</a># 

#<h2>What is Coq</h2># 

Here we introduce the
#<a href="https://coq.inria.fr/">Proof assistant tool Coq</a># (it 
means "rooster" in French)
YouTube has multiple tutorials (see 
#<a href="https://youtu.be/7sk8hPWAMSw">typical example</a>#) 
showing how to use Coq interactively. 
In Coq user has to write a proof in a special
syntax that can be verified by a computer. Coq checks, 
if the proof has all the steps covered and if they are done correctly
in order to achieve the goal. 
Coq is useful, since not all users see their own mistakes in 
proofs, and not all proofs can be verified by humans.
Correct logical reasoning is important, if we want to build 
correct IT solutions or configure
rule-based reasoning for artificial intelligence or similar
applications.
*)


(** #<h2>Check types in Coq</h2>#
*)
Require Import Bool.
Search bool.
(** These are "bool" datatypes - lowercase "true" and
"false" used just to manipulate Boolean values. 
*)

Check true.
Check false.

Eval compute in andb true false.
Eval compute in true && false.
Eval compute in orb true false.  (*r "orb" - boolean OR *)
Eval compute in true || false.
Eval compute in negb false.
Eval compute in if true then 3 else 4.
Eval compute in (3=4).


(** #<b>Warning!</b># The following expression is 
wrong, because "if" expression needs "bool" type, 
but "1=2" evaluates to "Prop" type. 
In short, "false" and "False" are two very different things.
#<br/>#
#<tt>Eval compute in if 1 = 2 then 3 else 4.</tt>#
#<br/>#
If you want to write such conditionals, compare two 
numbers so that it returns "bool".
*)

Require Import Coq.Arith.EqNat.
Eval compute in if beq_nat 1 2 then 3 else 4.
(** This function takes two natural numbers and returns "bool" *)
Check beq_nat.


(** These are propositions of type "Prop". 
In this case "True" embodies statement that is always true. 
And "False" is a statement that is a falsehood.
*)

Check True.
Check False.

(** You can check types of other expressions; 
and you can also evaluate them.  *)

(** These are simply natural numbers. *)

Check 3.
Check (3+4).

(** This is a pair of natural numbers of type #<tt>(nat*nat)</tt>#. *)

Check (3,4).

(** Function #<tt>mult</tt># takes two natural arguments.
#<br/>#
Expression #<tt>mult 3</tt># has got one argument already it wants one more.
#<br/>#
Finally, expression #<tt>mult 3 5</tt># has got both arguments,
it can be computed.
*)

Check mult.
Check mult 3.
Check mult 3 5.

(** Unlike "mult" which should precede
both arguments, some operators are infix operators:
they are written in the middle.
*)
Locate "*".
Locate "/\".
Locate "->".
Locate "_ <= _".


(** These are propositions (you can ask, if they are True
or not). They are not "bool" datatype! They are "Prop" datatype.
Notation #<tt>3&lt;&gt;6</tt># stands for "not equal".
*)

Check (3=5).
Check ((3=5)/\True).
Check (3 <= 6).
Check (3 <> 6).

(** This is a function type. Not a value, just a 
type notation. 
*)

Check nat -> Prop.

Definition g (x: nat): (nat*nat) :=
  (x*x, x).
Check g.

Eval compute in 
  let f := fun x => (x * x, x) in f 4.

(** #<h2>Use and build truth tables</h2>#
These examples are adopted from this source: 
#<a href="https://softwarefoundations.cis.upenn.edu/lf-current/Basics.html">Software #
#Foundations by Benjamin C. Pierce et al. - Basics</a>#
*)
Example test_orb1: (orb true false) = true.
Proof.
  simpl.
  reflexivity.
Qed.

(** 
This definition is of Peirce's arrow or 
the logical NOR operator (see also 
#<a href="">Problem 3 in HW1</a>#). 
It has two Boolean arguments
and produces a Boolean value.
It is true when both b1 and b2 are false,
and it is false otherwise.
*)
Definition norb (b1:bool) (b2:bool) : bool :=
  match b1 with
  | true => false
  | false => negb b2
  end.

Example test_norb1: (norb false false) = true.
Proof. simpl. reflexivity. Qed. 
Example test_norb2: (norb false true) = false.
Proof. simpl. reflexivity. Qed. 
Example test_norb3: (norb true false) = false.
Proof. simpl. reflexivity. Qed. 
Example test_norb4: (norb true true) = false.
Proof. simpl. reflexivity. Qed. 


(** #<h2>Use precedence and associativity</h2>#
*)
Eval compute in 3+4.
Eval compute in Nat.add 3 4.

Eval compute in 3*4.
Eval compute in Nat.mul 3 4.

Eval compute in 2+3*5.
Eval compute in (Nat.add 2 (Nat.mul 3 5)).





