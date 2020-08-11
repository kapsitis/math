(** #<a href="../../discrete/coq.html">Back to Coq Main Page</a>#  *)

(** * LV.NO.2020.9.2 *)

(** See #<a href='https://bit.ly/2VLBCH8'>LV Regional 
Olympiad Problems</a>#. *)

(** #<b>Problem:</b># Show that 1/(1*3) + 1/(3*5) + 1/(5*7) + ... + 
1/(2019*2021) = 1010/2021.
*)


Require Import Field.
Require Import QArith.
Require Import Qcanon.
Require Import Znumtheory.
Require Import Eqdep_dec.

Require Setoid.


Require Import ZArith.
Require Import Znumtheory.
Require Import BinInt.
Require Import Arith Psatz.
Require Import Znat.



Open Scope Q_scope.



Fixpoint SeqA (k:nat):Q :=
  match k with 
  | 0%nat => 0
  | S k' => (SeqA k') + 
    (1#((Pos.of_nat (2*k-1))*(Pos.of_nat (2*k+1))))
  end.



Open Scope nat_scope.

Lemma helper1: forall n:nat, 2 * S n - 1 = 2*n + 1.
Proof. 
  intros n.
  simpl.
  rewrite <- (plus_n_O n).
  rewrite (Nat.sub_0_r (n + S n)).
  rewrite <- (Nat.add_1_r n).
  rewrite (Nat.add_assoc n n 1).
  reflexivity.
Qed.


Lemma helper2: forall n:nat, 2 * S n + 1 = 2*n + 3.
  intros n.
  simpl.
  rewrite <- (plus_n_O n).
  rewrite <- (Nat.add_1_r n).
  rewrite <- (Nat.add_1_r (n + (n + 1) + 1)).
  rewrite (Nat.add_assoc n n 1).
  rewrite <- (Nat.add_assoc (n + n + 1) 1 1).
  assert (1 + 1 = 2) as H1. reflexivity. rewrite H1.
  rewrite <- (Nat.add_assoc (n + n) 1 2).
  assert (1 + 2 = 3) as H2. reflexivity. rewrite H2.
  reflexivity.
Qed.


Close Scope nat_scope.


(* 0 < 1 as rational numbers *)
Lemma Q_lt_0_1: 0 < 1. 
Proof. 
  unfold Qlt. simpl.
  apply Z.lt_0_1.
Qed.


(* 0 < 2 as rational numbers *)
Lemma Q_lt_0_2: 0 < 2. 
Proof. 
  unfold Qlt. simpl.
  apply Z.lt_0_2.
Qed.

(* 0 < 3 as rational numbers *)
Lemma Q_lt_0_3: 0 < 3. 
Proof. 
  pose Z.lt_0_1 as H1.
  pose Z.lt_0_2 as H2.
  apply (Zplus_lt_compat_r 0 2 1) in H2.
  rewrite (Zplus_0_l 1) in H2.
  assert (2 + 1 = 3)%Z as H3. ring. 
  rewrite H3 in H2.
  apply (Z.lt_trans 0 1 3 H1 H2).
Qed.




Lemma helper3: forall k a b:Q, 0 <= k -> 0 < a -> 0 < b -> a*k + b > 0.
Proof.
  intros k a b.
  intros H1 H2 H3.
  assert (0 <= a*k) as H4.
  pose (Qmult_le_compat_r 0 k a) as H5.
  apply H5 in H1.
  assert (0*a == 0) as H6. ring.
  rewrite H6 in H1.
  rewrite (Qmult_comm a k).
  exact H1.
  pose (Qlt_le_weak 0 a) as H7.
  apply H7 in H2. 
  exact H2.
  pose (Qplus_lt_le_compat 0 b (a*k) (a*k))  as H8.
  apply H8 in H3 as H9.
  rewrite (Qplus_0_l (a*k)) in H9.
  rewrite (Qplus_comm b (a*k)) in H9.
  pose (Qle_lt_trans 0 (a*k) (a*k + b)) as H10.
  apply H10 in H4.
  exact H4.
  exact H9.
  apply (Qle_refl (a*k)).
Qed.




Lemma helper4: forall k:Q, 0 <= k -> 2*(1/((2*k+1)*(2*k+3))) == 1/(2*k+1) - 1/(2*k+3).
Proof.
  intros k.
  intros H1.
  field.
  split.
  pose (helper3 k 2 3) as H2.
  pose Q_lt_0_2 as H3.
  pose Q_lt_0_3 as H4.
  pose (H2 H1 H3 H4) as H10.
  unfold not. intros H11.
  rewrite H11 in H10.
  pose (Qlt_irrefl 0) as H12.
  apply (H12 H10).
  pose (helper3 k 2 1) as H13.
  pose (H13 H1 Z.lt_0_1 Z.lt_0_2) as H14.
  apply (Qlt_not_eq 0 (2*k+1)) in H14 as H15.
  unfold not. intros H16.
  rewrite H16 in H15.
  assert (0 == 0) as H17. reflexivity.
  apply (H15 H17).
Qed.


(*
TODO: Rewrite with (inject_Z (Z.of_nat n)) - instead of (Z.of_nat n # 1)
*)

Lemma helper5z: forall (n:nat), 0 <= Z.of_nat n # 1.
Proof.
  intros n.
  unfold Qle.
  simpl.
  rewrite <- (Zred_factor0 (Z.of_nat n)).
  apply (Zle_0_nat n).
Qed.





Lemma add_numerators: forall (a:Z) (b:Z) (p:positive),
  (a + b) # p == (a#p) + (b#p).
Proof. 
  intros a b p.
  unfold Qplus.
  simpl.
  unfold Qeq.
  simpl.
  pose (Pos2Z.inj_mul p p) as H1.
  rewrite H1.
  rewrite (Z.mul_assoc (a + b) (Z.pos p) (Z.pos p) ).
  rewrite (Z.mul_add_distr_r  a  b (Z.pos p)).
  reflexivity.
Qed.




Lemma helper6c: forall a b:Z,
  a = b -> a#1 == b#1.
Proof.
  intros a b.
  intros H1.
  rewrite H1.
  reflexivity.
Qed.





Lemma helper6aaa: forall (n:nat),
  (2 * (Z.of_nat n # 1) + 1 == Z.of_nat (2*n + 1) #1).
Proof.
  intros n.
  unfold Qmult, Qnum, Qden.
  assert (1*1 = 1)%positive as H1.
  simpl. reflexivity. rewrite H1.
  pose (add_numerators (2* (Z.of_nat n)) 1 1) as H2.
  rewrite <- H2.
  apply (helper6c (2 * Z.of_nat n + 1) (Z.of_nat (2 * n + 1) )).
  rewrite (Nat2Z.inj_add (2 * n) 1).
  assert (Z.of_nat 1 = 1)%Z as H3.
  simpl. reflexivity. rewrite H3.
  rewrite (Nat2Z.inj_mul 2 n).
  assert (Z.of_nat 2 = 2)%Z as H4.
  simpl. reflexivity. rewrite H4.
  reflexivity.
Qed.




Lemma helper6aab: forall (n:nat),
  (2 * (Z.of_nat n # 1) + 3 == Z.of_nat (2*n + 3) #1).
Proof.
  intros n.
  unfold Qmult, Qnum, Qden.
  assert (1*1 = 1)%positive as H1.
  simpl. reflexivity. rewrite H1.
  pose (add_numerators (2* (Z.of_nat n)) 3 1) as H2.
  rewrite <- H2.
  apply (helper6c (2 * Z.of_nat n + 3) (Z.of_nat (2 * n + 3) )).
  rewrite (Nat2Z.inj_add (2 * n) 3).
  assert (Z.of_nat 3 = 3)%Z as H3.
  simpl. reflexivity. rewrite H3.
  rewrite (Nat2Z.inj_mul 2 n).
  assert (Z.of_nat 2 = 2)%Z as H4.
  simpl. reflexivity. rewrite H4.
  reflexivity.
Qed.


Compute ((Pos.of_nat 17)).

Print  SuccNat2Pos.inv.


(*
forall (n : nat) (p : positive), Pos.to_nat p = S n -> Pos.of_succ_nat n = p
*)

(* nat -> pos -> Z  ... nat -> Z *)

(*
Pos2Z.id: forall p : positive, Z.to_pos (Z.pos p) = p
*)



Lemma helperNatsArePositive: forall n, n <> 0%nat -> (Z.of_nat n > 0)%Z.
Proof.
  intros n.
  intros H1.
  pose (inj_gt n 0) as H2.
  pose (gt_0_eq n) as H3.
  unfold not in H1.
  destruct H3.
  pose (H2 H) as H4.
  assert (Z.of_nat 0 = 0)%Z as H5.
  simpl. reflexivity.
  rewrite H5 in H4.
  exact H4.
  rewrite H in H1.
  assert (n = n). reflexivity.
  contradiction (H1 H0).
Qed.



Lemma helperNatPNat: forall n, n <> 0%nat -> Pos.to_nat (Pos.of_nat n) = n.
Proof. 
  intros n. 
  intros H1.
  apply (Nat2Pos.id n H1).
Qed.




Lemma helperPNatP: forall p:positive, Pos.of_nat (Pos.to_nat p) = p.
Proof. 
  intros p.
  pose (Nat2Pos.id (Pos.to_nat p)) as H1.
  apply (Pos2Nat.inj (Pos.of_nat (Pos.to_nat p)) p).
  apply H1.
  pose (Pos2Nat.is_pos p) as H2.
  unfold not.
  intros H3.
  rewrite H3 in H2.
  contradiction (Nat.lt_irrefl 0).
Qed.




(* positive_nat_Z *)
Lemma helperPNatZ: forall p:positive, Z.of_nat (Pos.to_nat p) = Z.pos p.
Proof.
  intros p.
  destruct (Pos2Nat.is_succ p) as (n,H).
  rewrite H. simpl. f_equal. now apply SuccNat2Pos.inv.
Qed.


Lemma helperPZNat: forall p:positive, Z.to_nat (Z.pos p) = Pos.to_nat p.
Proof.
  intros p.
  apply (Z2Nat.inj_pos p).
Qed.



Lemma helperPZP: forall p:positive, (Z.to_pos (Z.pos p)) = p.
Proof.
  intros p.
  apply (Pos2Z.id p).
Qed.



(*
Lemma helperZNatZ: forall z:Z, (z>0)%Z -> (Z.of_nat (Z.to_nat z)) = z.
Proof.
  intros z. 
  intros H1.
  Admitted.
*)


Lemma helperZPZ: forall z:Z, (z>0)%Z -> (Z.pos (Z.to_pos z)) = z.
Proof.
  intros z. 
  intros H1.
  pose (Pos2Z.id (Z.to_pos z)) as H2.
  pose (Z2Pos.inj (Z.pos (Z.to_pos z)) z) as H4.
  pose (Zgt_pos_0 (Z.to_pos z)) as H5.
  pose (Z.gt_lt (Z.pos (Z.to_pos z)) 0 H5) as H6.
  pose (Z.gt_lt z 0 H1) as H7.

  pose (H4 H6 H7) as H8.
  pose (helperPZP (Z.to_pos z)) as H9.
  exact (H8 H9).
Qed.




Lemma helperNatZP: forall n:nat, n<>0%nat -> Z.to_pos (Z.of_nat n) = Pos.of_nat n.
Proof.
  intros n.
  intros H1.
  pose (helperNatsArePositive n H1) as H2.
  pose (helperPNatZ (Pos.of_nat n)) as H3.
  pose (helperNatPNat n H1) as H4.
  rewrite H4 in H3.
  assert (Z.to_pos (Z.of_nat n) = Z.to_pos (Z.of_nat n)) as H5.
  reflexivity.
  rewrite H3 in H5 at 2.
  pose (helperPZP (Pos.of_nat n)) as H6.
  rewrite H6 in H5.
  exact H5.
Qed.









Lemma helperNatPZ: forall n:nat, n<>0%nat -> (Z.pos (Pos.of_nat n)) = Z.of_nat n.
Proof.
  intros n.
  intros H1.
  pose (helperPZP (Pos.of_nat n)) as H2.
  pose (helperNatZP n H1) as H3.
  rewrite <- H3 in H2.
  assert (Z.to_pos (Z.of_nat n) = Pos.of_nat n) as H4.
  rewrite H3.
  reflexivity.
  assert (Z.pos (Pos.of_nat n) = Z.pos (Pos.of_nat n)) as H5.
  reflexivity.
  rewrite  <- H4 in H5.
  pose (helperZPZ (Z.of_nat n)) as H6.
  pose (helperNatsArePositive n H1) as H7.
  pose (H6 H7) as H8.
  rewrite <- H8.
  pose (helperNatZP n H1) as H9.
  rewrite H9. 
  reflexivity.
Qed.



Lemma helper6e: forall n:nat, ((2 * n + 1)<>0)%nat.
Proof. 
  intros n.
  assert ((S (2*n)) = 2*n+1)%nat as H1.
  lia. 
  pose (Nat.neq_succ_0 (2*n)) as H2.
  rewrite H1 in H2.
  exact H2.
Qed.

Lemma helper6f: forall n:nat, ((2 * n + 3)<>0)%nat.
Proof. 
  intros n.
  assert ((S (2*n+2)) = 2*n+3)%nat as H1.
  lia. 
  pose (Nat.neq_succ_0 (2*n+2)) as H2.
  rewrite H1 in H2.
  exact H2.
Qed.





Lemma helper5y: forall (n:nat) (k:Q), 
   (k == (Z.of_nat n) #1) -> (Z.pos (Pos.of_nat (2 * n + 1)) # 1) == 2 * k + 1. 
Proof.
  intros n k. 
  intros H1.
  rewrite H1.
  pose (helper6aaa n) as H2.
  rewrite H2.
  pose (helperNatPZ (2 * n + 1)) as H3.
  pose (helper6e n) as H4.
  apply (helper6c (Z.pos (Pos.of_nat (2 * n + 1)))  (Z.of_nat (2 * n + 1))).
  pose (helper6e n) as H5.
  apply (helperNatPZ (2 * n + 1) H5).
Qed.




Lemma helper5x: forall (n:nat) (k:Q), 
   (k == (Z.of_nat n) #1) -> (Z.pos (Pos.of_nat (2 * n + 3)) # 1) == 2 * k + 3. 
Proof.
  intros n k. 
  intros H1.
  rewrite H1.
  pose (helper6aab n) as H2.
  rewrite H2.
  pose (helperNatPZ (2 * n + 3)) as H3.
  apply (helper6c (Z.pos (Pos.of_nat (2 * n + 3)))  (Z.of_nat (2 * n + 3))).
  pose (helper6f n) as H5.
  apply (helperNatPZ (2 * n + 3) H5).
Qed.






Lemma helper5a: forall (n:nat) (k:Q), 
  (k == (Z.of_nat n) #1) -> 1 /(2*k +1) == (1 # Pos.of_nat (2 * n + 1)).
Proof.
  intros n k. 
  intros H1.
  pose (Qmake_Qdiv 1 (Pos.of_nat (2 * n + 1))) as H2.
  unfold inject_Z in H2.
  pose (helper5y n k H1) as H3.
  rewrite H3 in H2.
  rewrite H2.
  reflexivity.
Qed.



Lemma helper5b: forall (n:nat) (k:Q), 
  (k == (Z.of_nat n) #1) -> 1 /(2*k +3) == (1 # Pos.of_nat (2 * n + 3)).
Proof.
  intros n k. 
  intros H1.
  pose (Qmake_Qdiv 1 (Pos.of_nat (2 * n + 3))) as H2.
  unfold inject_Z in H2.
  pose (helper5x n k H1) as H3.
  rewrite H3 in H2.
  rewrite H2.
  reflexivity.
Qed.


(*
Lemma helper5b: forall (n:nat) (a:nat) (b:nat) (k:Q), 
  (k == (Z.of_nat n) #1) -> 
  1 /( (inject_Z ( Z.of_nat a )) * k + (inject_Z ( Z.of_nat b ))) == (1 # Pos.of_nat (a*n+b)).
Proof.
  intros n a b k. 
  intros H1.
  pose (Qmake_Qdiv 1 (Pos.of_nat (a * n + b))) as H2.
Admitted.
*)


(*
Consider simplifying this:
Lemma Qinv_mult_distr : forall p q, / (p * q) == /p * /q.
*)

Lemma helper5c: forall (n:nat) (k:Q), (k == (Z.of_nat n) #1) ->
  1/((2*k+1)*(2*k+3)) == (1 # Pos.of_nat (2 * n + 1) * Pos.of_nat (2 * n + 3)).
Proof.
  intros n k.
  intros H1.
  pose (helper5a n k H1) as H2.
  pose (helper5b n k H1) as H3. 
  assert ( (1 / (2 * k + 1)) * (1 / (2 * k + 3)) == 1 / ((2 * k + 1) * (2 * k + 3))) as H4.
  field.
  split.
  pose (helper5z n) as H5.
  rewrite <- H1 in H5.
  pose Q_lt_0_2 as H6.
  pose Q_lt_0_3 as H7.
  pose (helper3 k 2 3 H5 H6 H7) as H8.
  unfold not. intros H9.
  rewrite H9 in H8.
  contradiction (Qlt_irrefl 0).
  pose (helper5z n) as H10.
  rewrite <- H1 in H10.
  pose Q_lt_0_2 as H11.
  pose Q_lt_0_1 as H12.
  pose (helper3 k 2 1 H10 H11 H12) as H13.
  unfold not. intros H14.
  rewrite H14 in H13.
  contradiction (Qlt_irrefl 0).
  rewrite <- H4.
  rewrite H2.
  rewrite H3.
  unfold Qeq.
  simpl. reflexivity.
Qed.


Theorem lv_no_2020_9_2_gen: forall n:nat, 2*(SeqA n) == 1 - (1#(Pos.of_nat (2*n+1))).
Proof. 
  intros n.
  induction n.
  simpl.
  reflexivity.
  assert (SeqA (S n) == ((SeqA n) + 
    (1#((Pos.of_nat (2*(S n)-1))*(Pos.of_nat (2*(S n)+1)))))) as H1.
  simpl. reflexivity.
  assert (2* SeqA (S n) == 2 * SeqA (S n)) as H2.
  reflexivity.
  rewrite H1 in H2 at 2.
  rewrite H2.
  pose (Qmult_plus_distr_r 2 (SeqA n) (1 # Pos.of_nat (2 * S n - 1) * Pos.of_nat (2 * S n + 1))) as H3.
  rewrite H3.
  rewrite IHn.
  pose (helper1 n) as H4.
  rewrite H4.
  pose (helper2 n) as H5.
  rewrite H5.
  assert (Z.of_nat n # 1 == Z.of_nat n # 1) as H6. reflexivity.
  pose (helper5a n ((Z.of_nat n)#1) H6) as H7.
  rewrite <- H7.
  pose (helper5b n ((Z.of_nat n)#1) H6) as H8.
  rewrite <- H8.
  pose (helper5c n ((Z.of_nat n)#1) H6) as H9.
  rewrite <- H9.
  pose (helper5z n) as H10.
  pose (helper4  ((Z.of_nat n)#1) H10) as H11.
  rewrite H11.
  ring.
Qed.


Lemma halve_both: forall a b:Q, 2*a == b -> a == (1#2)*b.
Proof.
  intros a b.
  intros H1.
  rewrite <- H1.
  field.
Qed.


Theorem lv_no_2020_9_2: SeqA 1010 == 1010#2021.
Proof. 
  pose (lv_no_2020_9_2_gen 1010) as H1.
  pose (halve_both (SeqA 1010) (1 - (1 # Pos.of_nat (2*1010 + 1)))) as H2.
  apply H2 in H1.
  rewrite H1.
  assert (1 - (1 # (Pos.of_nat (2 * 1010 + 1))) == 2020 # 2021) as H3.
  simpl.
  reflexivity.
  rewrite H3.
  field.
Qed.


Close Scope Q_scope.

