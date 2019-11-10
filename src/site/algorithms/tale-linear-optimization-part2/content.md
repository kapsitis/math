# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span style="color:darkgreen">**(1) Ievads**</span>  
<span>(2) [Vispārīgais simpleksalgoritms](#section-1)</span>  
<span>(3) [Duālā lineārā programma](#section-2)</span>  
<span>(4) [Sākotnējā stūra izvēle](#section-3)</span>  
<span>(5) [Elipsoīda algoritms](#section-4)</span>  
<span>(6) [(P) Plūsmu uzdevumi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>




# <lo-why/> why

<div class="bigWhy">

Kāpēc ar simpleksalgoritmu nepietiek?

</div>

<div class="smallWhy">

* Simpleksalgoritma varianti (sākotnējā un duālā problēma,
pirmā stūra izvēle, pārejas izvēle un randomizācija). 
* Var būt slikta sarežģītība (īpaši uzkonstruētem piemēriem). 
* Polinomiāla laika algoritms ir standarts visam, ko lieto praksē.

</div>


 
## <lo-theory/> Sasniedzamie rezultāti

1. Definēt duālo uzdevumu. 
2. Formulēt dualitātes teorēmu. 
3. Noskaidrot simpleksalgoritma izvēles.
4. Formulēt Elipsoīda algoritmu (Khachiyan). 
5. LP lietojumi plūsmu maksimizēšanā un 
"operāciju pētīšanā". 





# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section)</span>  
<span style="color:darkgreen">**(2) Vispārīgais simpleksalgoritms**</span>  
<span>(3) [Duālā lineārā programma](#section-2)</span>  
<span>(4) [Sākotnējā stūra izvēle](#section-3)</span>  
<span>(5) [Elipsoīda algoritms](#section-4)</span>  
<span>(6) [(P) Plūsmu uzdevumi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>



# <lo-theory/> Kāpēc LP ir svarīgas?

* (Reālo skaitļu) LP ir pirmais solis, lai risinātu 
veselo skaitļu problēmas (*Integer Programming, IP*) un 
jauktās LP problēmas (*Mixed Integer Linear Programs, MIP*). 
* Kā optimāli izvēlēties komplektu (izejvielas, akciju portfeļus), 
kā vislabāk sadalīt kādu resursu.
* Plūsmas maksimizēšana grafā (skatīsimies šajā lekcijā).

Veselie skaitļi kā nezināmie (*Integer Programming*) 
labāk modelē Yes/No lēmumu pieņemšanu (0 un 1 vērtības), 
bet šādus uzdevumus ir grūtāk risināt. 


## <lo-summary/> LP algoritmi 

* Simpleksalgoritmi (Kantorovičs, 1939; Dantzig, 1947).
* Elipsoīda algoritms (Khachian, 1979)
* Iekšējo punktu metodes (*Interior Point methods*).
    - Projektīvā metode (Karmarkar, 1984).
    - Afīnā metode (Dikin, 1967).
    - Log Barrier Method. 

Simpleksalgoritms parasti ir ļoti ātrs, bet īpaši uzkonstruēti
piemēri var būt sarežģīti.   
Matricām var būt ap 100 tūkstošiem rindiņu/kolonnu; ap miljons
skaitļu šajās matricās nav nulles. 





# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section)</span>  
<span>(2) [Vispārīgais simpleksalgoritms](#section-1)</span>  
<span style="color:darkgreen">**(3) Duālā lineārā programma**</span>  
<span>(4) [Sākotnējā stūra izvēle](#section-3)</span>  
<span>(5) [Elipsoīda algoritms](#section-4)</span>  
<span>(6) [(P) Plūsmu uzdevumi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>





# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section)</span>  
<span>(2) [Vispārīgais simpleksalgoritms](#section-1)</span>  
<span>(3) [Duālā lineārā programma](#section-2)</span>  
<span style="color:darkgreen">**(4) Sākotnējā stūra izvēle**</span>  
<span>(5) [Elipsoīda algoritms](#section-4)</span>  
<span>(6) [(P) Plūsmu uzdevumi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>






# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section)</span>  
<span>(2) [Vispārīgais simpleksalgoritms](#section-1)</span>  
<span>(3) [Duālā lineārā programma](#section-2)</span>  
<span>(4) [Sākotnējā stūra izvēle](#section-3)</span>  
<span style="color:darkgreen">**(5) Elipsoīda algoritms**</span>  
<span>(6) [(P) Plūsmu uzdevumi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>






# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section)</span>  
<span>(2) [Vispārīgais simpleksalgoritms](#section-1)</span>  
<span>(3) [Duālā lineārā programma](#section-2)</span>  
<span>(4) [Sākotnējā stūra izvēle](#section-3)</span>  
<span>(5) [Elipsoīda algoritms](#section-4)</span>  
<span style="color:darkgreen">**(6) (P) Plūsmu uzdevumi**</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>



# <lo-sample/> Maksimālās plūsmas atrašana grafā

![Max Flow Graph](max-flow-graph.png)




# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section)</span>  
<span>(2) [Vispārīgais simpleksalgoritms](#section-1)</span>  
<span>(3) [Duālā lineārā programma](#section-2)</span>  
<span>(4) [Sākotnējā stūra izvēle](#section-3)</span>  
<span>(5) [Elipsoīda algoritms](#section-4)</span>  
<span>(6) [(P) Plūsmu uzdevumi](#section-5)</span>  
<span style="color:darkgreen">**(7) Kopsavilkums**</span>

</hgroup>


