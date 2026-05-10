# Matemātikas uzdevumu lasītprasme un kļūdas pamatojumos

7.-9.klašu matemātikas saturs 

## 1. Uzdevuma lasīšana un matemātiskais modelis

*Kopsavilkums:* Pirms risināšanas jālasa uzdevums, jāpamana tajā visi nosacījumi un 
uzdevums jāpārveido par matemātisku modeli. 

### Sasniedzamie redzultāti:

* Analizēt uzdevumu tekstus, nepazaudējot nosacījumus (uzdevuma "ievade"). 
* Pazīt biežus valodiskus pārpratumus. 
* Uzdevuma kontekstu izsaka kā modeli (vienādojumu, apgalvojumu par grafiem, kombināciju saskaitīšanu vai līdzīgu). 
* Izlasīt veicamo darbību un saprast, kāds ir vēlamais rezultāts; vai "izvade" ir skaitlis, 
  skaitļu kopa, konstrukcija jeb algoritms, pierādījums. 
* Praktizēt 4R secību: *Read, Restate, Represent, Roadmap*:

    1. **Izlasīt** uzdevumu un atrast visus nosacījumus;  
    2. **Pārformulēt** īsāk un saviem vārdiem;  
    3. **Attēlot** situāciju zīmējumā, tabulā, funkciju grafikā;  
    4. **Izplānot** nepieciešamās vai sagaidāmās risinājuma darbības.


### Izmantotie līdzekļi:

1. Daži ievaduzdevumi, kuri viegli noved pie pārpratumiem (atšķirība starp "cik atrisinājumu", "atrast atrisinājumu", 
   "atrast visus atrisinājumus", pārprastas skaitļu kopas, izlaists vārds "atšķirīgs"). 
   Katram uzdevumam uzdodam precizējošus jautājumus, lai saprastu, kādos veidos to var pārprast.
   Šie uzdevumi jāizvēlas no olimpiāžu un arī matemātikas standartkursa krājumiem.
2. Uzdevumu piemēri, kuros (a) pasvītro nosacījumus, (b) formalizē, (c) noskaidro atrisinājuma struktūru.  

   Piemēri var parādīt modelēšanas paņēmienus (pārsvarā kombinatorikas vai ģeometrijas uzdevumiem):

   * Cilvēki/draudzēšanās vai pilsētas/ceļi (modelis ir grafi - virsotnes, šķautnes, virsotņu pakāpes, sakarīgums), 
   * Uzdevumi, kur elementi iespaido savus kaimiņus (modelis ir summas, invarianti, paritāte), 
   * Izvēles vai piekārtošanas uzdevumi, kombināciju saskaitīšana (modelis ir bijektīvas vai injektīvas funkcijas), 
   * Ģeometrisku uzdevumu nosacījumi (modelis ir ģeometriskas teorēmas nevis izskats diagrammā), 
   * Divu spēlētāju kombinatoriskas spēles modelis.
   * Algoritmiska uzdevuma modelis.

3. Piemēri, kuros var izveidot atšķirīgus modeļus tam pašam uzdevumam (grafi vs. paritāte, vienādojums vs. gadījumu 
   analīze). Kurš no modeļiem ir vienkāršāks risinājuma iegūšanai? 
   Arī piemēri, kas var viegli novest pie neparastiem modeļiem.


### Izmantotie līdzekļi:

* Darbību saraksts uz vienas lapas: 4R secība, pārbaudāmās lietas (*checklist*) uzdevuma nosacījumiem un vēlamajam rezultātam.
* Uzdevumi līdzīgi 5.-6.lappusei no [5.-9.klašu olimpiāžu 
  grāmatas](https://www.nms.lu.lv/fileadmin/user_upload/lu_portal/projekti/nms.lu.lv/Gramatas/Tematiskie/GRAMATA_atjaunots_matem_olimp_uzd_macibu_procesa_5-9kl.pdf), bet mazliet tuvāki reālām olimpiādēm.





## 2. Kas ir pierādījums? Pretpiemērs, kvantori, zīmējumi

*Kopsavilkums:* Kādi soļi ir atļauti, kā apgāzt apgalvojumus, kāpēc attēli un piemēri var būt maldinoši. 

### Mērķi

Theme: Building “proof culture”: what is allowed evidence, how to disprove, and why pictures/examples are dangerous.

Learning goals
Separate: example / counterexample / proof / explanation.
Handle quantifiers and negations correctly (De Morgan).
Identify diagram-based fallacies in geometry and fix them with proper reasoning.
Plan (120 min)
0–15 min — Sorting task: “What is this?”
Give 10 short student-like responses; teachers classify each as:

valid proof / partial proof / example / counterexample / irrelevant. Include classics:
“I drew it and it seems true.”
“It works for n=1,2,3 so true.”
“Assume… therefore…” but missing key justification.
15–35 min — Mini-lecture: proof vs. experiment
Key messages (teacher-friendly, not overly formal):

A proof must work for all allowed cases, not just “many”.
A diagram is a model, not evidence (unless conditions explicitly guarantee it).
Counterexample is a complete disproof for universal claims.
35–60 min — Quantifiers clinic
Use 4 statements and ask:

write the negation,
what counts as a disproof,
what counts as a proof.
Include one of each type:

∀x P(x)
∃x P(x)
∀x ∃y P(x,y)
∃x ∀y P(x,y)
Connect directly to olympiad evaluation: why “I couldn’t find” is not disproof; why to disprove ∀x∃y you must find a single bad x.

60–90 min — Geometry: “looks right” vs “is right”
Use 2–3 short geometry problems where the diagram misleads:

angle that appears 90° but isn’t given,
“seems isosceles” triangle,
collinearity that’s only visual.
Task: groups rewrite solutions replacing “it is obvious from the picture” with:

named theorem (parallel lines → alternate angles),
congruence criteria,
circle theorems,
vector/coordinate method if appropriate.
90–115 min — Micro-teaching rehearsal
Pairs practice a 3-minute explanation to students:

“Why one example isn’t proof” (with an example statement that fails at n=…).
“How to disprove a universal statement fast” (counterexample habit).
115–120 min — Takeaway
A compact “Proof & Disproof toolbox” sheet:

what to try first (counterexample search),
common negations,
forbidden phrases in solutions (“looks like”, “clearly from the drawing” without theorem).





## 3. Pamatojuma struktūra un vērtēšana (minimālais, algoritmi, stratēģijas)
Theme: Turning reasoning into a complete, checkable written solution; diagnosing typical olympiad marking issues.

Learning goals
Teach and use proof templates (especially “smallest possible”, “strategy”, “construction”).
Apply a simple rubric to check completeness.
Learn to give feedback that upgrades a student from “idea” to “solution”.
Plan (120 min)
0–15 min — Mini-lecture: solution architecture
Introduce 3 high-frequency templates:

Minimality / extremal To prove “minimum is N”:
(Existence) show a construction achieving N.
(Lower bound) prove impossible to do better than N−1 (or <N).
2. Algorithm / strategy (scales, games, processes)
A correct solution needs:

clear algorithm/strategy,
proof it always works,
proof it terminates / fits constraints (moves, weighings),
optimality if asked.
3. Casework

state cases so they cover all possibilities,
avoid overlap,
conclude explicitly.
15–55 min — Marking workshop (realistic olympiad scripts)
Provide 3 anonymized “student solutions” (half-correct typical):

one minimality missing the lower bound,
one game strategy not fully specified,
one geometry proof with diagram assumptions.
Groups grade using a rubric:

correctness,
completeness,
justification quality,
clarity.
Then discuss: what single sentence would fix the solution? (This is gold for teachers.)

55–85 min — Build-a-proof exercise
Give one problem of each type (short but nontrivial):

Minimality (e.g., covering/partition, number theory bound, graph degree bound).
Balance scale / coin ordering (focus on describing decision tree).
Game/invariant (winning strategy justification).
Groups must write a “competition-ready” solution with explicit structure headings:

Given / To show
Proof / Construction / Strategy
Correctness argument
Conclusion
85–110 min — Feedback language: how to coach proof-writing
Create a list of teacher prompts that force justification:

“Which theorem allows this step?”
“What are the cases and why do they cover all?”
“Where did you prove it can’t be smaller?”
“If your strategy fails, show the first moment it would fail and derive contradiction.”
110–120 min — Takeaway
Participants leave with:

a 1-page rubric for solutions,
3 proof templates,
a bank of “upgrade questions” for student drafts.




Crawl over all the files in problembase/LV.VOL/lv-vol-YYYY/content_lv.md (where the YYYY is between 2004 and 2025). 
Each "content_lv.md" contains some 20 olympiad problems about high-school math. Only focus on the first 5 problems in each problemset - they are meant for Grade 9 (for example, problems with titles "LV.VOL.2016.9.1", ..., "LV.VOL.2016.9.5" are all fine, but the remaining ones - such as "LV.VOL.2016.10.x" should be ignored. 

Out of these problems pick those that may be challenging for one of these 3 reasons: 
(1) Reading the problem; fully understanding its condition and building a mathematical model can be difficult; 
(2) Proof involves some overlooked nuances (and it may be tempting to omit some parts and come up with example instead of a proof). 
(3) The problem has solution that follows some intricate proof pattern or strategy (finding the optimum, casework, describing an algorithm or a game strategy etc.), where the solution involves certain established structure how to write mathematical justification. 

If problem is not challenging to understand (and its proof uses a single idea or example), then just skip it. As there are around 110 problems for Grade 9; you can skip the majority - just leave some 30 problems. 

Distribute thee 30 remaining problems (that may be challenging for reading skills, for logical understanding or for proof structure/strategy), and insert htem into "curricula/README.md". 
For each problem that you selected, quote it from H1 heading (e.g. "# <lo-sample/> LV.VOL.2004.9.xx"), and the problem text (up to <small> or "#Atrisinajums" - exclusive). 

If there are images in the problem or its solution (such as "problembase/LV.VOL/lv-vol-2004/xxxx.png"), then copy those PNG files into curricula as well. 

You will end up filling in "curricula/README.md" with problems from under "problembase/LV.VOL" and also copying some PNGs to "curricula". Do not modify other directories except curricula.