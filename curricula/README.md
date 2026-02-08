# Matemātikas uzdevumu lasītprasme un kļūdas pamatojumos

## Uzdevuma lasīšana un matemātiskais modelis

*Kopsavilkums:* Kā iegūt autora iecerēto matemātisko situāciju. 

### Sasniedzamie redzultāti

Uzdevumu lasīšana; valodiskie pārpratumi un pazaudēti nosacījumi. 

Teach a repeatable routine for reading and unpacking problems.
Recognize common linguistic traps and constraint-loss.
Practice converting contexts into models (equations, graphs, cases, diagrams).


Give 2 short olympiad-ish word problems where the most common error is misreading (e.g., “how many solutions” vs “find a solution”, “integer” omitted, “distinct” omitted).
Ask participants: What wrong answers would Grade 8–9 students give and why?
10–25 min — Mini-lecture: “4R routine”
A practical routine to train students:

4R = Read, Restate, Represent, Roadmap

* Read (slowly) and mark constraints.
* Restate in your own words (one sentence).
* Represent (choose model: table/graph/diagram/equations).
* Roadmap (what needs to be shown/calculated).


Handout: A one-page checklist teachers can reuse.

25–55 min — Activity: constraint hunting + rephrasing

In small groups, give 3 tasks (mix of competition + textbook style). For each: (a) underline constraints, (b) rewrite the problem in “math language”, (c) list what is being asked (“output type”: number? set? proof? construction?).
55–70 min — Modelling patterns (mini-lecture + quick examples)
Show 4–5 modelling “moves” frequently needed in olympiad problems:

“People/cities/roads” → graph (vertices/edges; degrees; connectivity).
“Each affects neighbors / parity changes” → invariant / parity.
“Choose/arrange” → counting / bijection.
“Geometric condition” → use named theorems not appearance.
70–110 min — Workshop: same story, different model
Give one situation-based problem and ask groups to propose two different models (e.g., graph vs. parity; equation vs. casework).
Discussion focuses on: Which model makes proof easiest?

110–120 min — Takeaway + classroom transfer
Participants produce: one concrete “reading routine” poster and one modelling exercise they can use next week.

Suggested materials

Handout: “4R routine + constraint checklist”
A set of 6–8 short tasks (Latvian olympiad/AMC-style length but not multiple-choice)






## Kas ir pierādījums? Pretpiemērs, kvantori, zīmējumi

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
Part 3 (2h): Pamatojuma struktūra un vērtēšana (minimālais, algoritmi, stratēģijas)
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