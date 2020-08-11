# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span style="color:darkgreen">**(1) Ievads**</span>  
<span>(2) [Elipsoīda algoritms](#section-1)</span>  
<span>(3) [Sarežģītības novērtējums](#section-2)</span>  
<span>(4) [Kopsavilkums](#section-3)</span>

</hgroup>



-----

# <lo-why/> why

<div class="bigWhy">

Kāpēc ar simpleksalgoritmu nepietiek?

</div>

<div class="smallWhy">

* Polinomiāla laika algoritms ir standarts visam, ko lieto praksē.

</div>



--
 
## <lo-theory/> Sasniedzamie rezultāti

1. Formulēt Elipsoīda algoritmu (Khachiyan). 
2. LP lietojumi plūsmu maksimizēšanā un 
"operāciju pētīšanā". 



-----

# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section-0)</span>   
<span style="color:darkgreen">**(2) Elipsoīda algoritms**</span>  
<span>(3) [Sarežģītības novērtējums](#section-2)</span>  
<span>(4) [Kopsavilkums](#section-3)</span>

</hgroup>



-----

# <lo-summary/> Elipsoīda algoritma ievads

Šo algoritmu izgudroja Hačijans (Khachiyan) 1979. gadā.  
Elipsoīda algoritms pazīstams kā pirmais lineārās programmēšanas algoritms, 
kuram tika pierādīts, ka tas atrod atrisinājumu polinomiālā laikā ($O(n^4L)$),
kur $n$ - dimensiju skaits, $L$ – ar cik bitu precizitāti jāatrod atrisinājums. 

Lai gan teorētiski darbības laiks ir polinomiāls, praksē algoritms ir 
lēns un netiek lietots. Tāpēc šajā kursā mēs ierobežosimies ar īsu šī algoritma aprakstu.


--

## <lo-summary/> Elipsoīda algoritma pārskats

<div style="font-size:70%">

Dualitātes teorēmas (un redukcijas uz primāro+duālo) dēļ 
pietiek ar algoritmu, kas atrod punktu, kur izpildās visi nosacījumi. To meklē šādi:

Sāk ar elipsoīdu $E_0$, kas noteikti ietver LP pieļaujamo apgabalu.  
Pilda sekojošus soļus līdzkamēr sasniegta vajadzīgā precizitāte:

1. Ņem iepriekšējā elipsoīda $E_i$ centru $c_i$.
2. Ja $c_i$ neapmierina visus LP nosacījumus, tad atrod nosacījumu 
$a_k$, kas tiek pārkāpts visvairāk.
3. Ar plakni, kas sastāv no visiem punktiem, kur nosacījuma $a_k$ 
izteiksmei ir vienāda vērtība $c$ (kur $c$ ir pa vidu starp vērtību punktā 
$c_i$ un pieļaujamajām izteiksmes vērtībām) pārdala telpu divās daļās. 
Ar $R_1$ apzīmējam daļu, kur nonāk $c_i$ un ar $R_2$ apzīmējam daļu, 
kur nonāk pieļaujamais apgabals.
4. Uzkonstruē jaunu elipsoīdu $E_{i+1}$, tā lai izpildītos
$$E_i \cap R_2 \subseteq E_{i+1}.$$

</div>


--

## <lo-summary/> Apgalvojums par elipsoīdu

<hgroup>

![Elipsoid Algorithm](elipsoid-algorithm.png)

</hgroup>
<hgroup>

Hačjana konstrukcijā (*barycentric coordinate descent*) elipsoīdi ir tādi, ka 
$$\frac{\text{Volume}(E_{k+1})}{\text{Volume}(E_{k})} = \frac{1}{2^{\frac{1}{2n+1}}}$$
veido konstantu attiecību, kas atkarīga no dimensiju skaita $n$. 


</hgroup>


-----

# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section-0)</span>  
<span>(2) [Elipsoīda algoritms](#section-1)</span>  
<span style="color:darkgreen">**(3) Sarežģītības novērtējums**</span>  
<span>(4) [Kopsavilkums](#section-3)</span>

</hgroup>



-----

# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Lineārā optimizācija - 2</blue>

</hgroup><hgroup style="font-size:90%">

<span>(1) [Ievads](#section-0)</span>   
<span>(2) [Elipsoīda algoritms](#section-1)</span>  
<span>(3) [Sarežģītības novērtējums](#section-2)</span>  
<span style="color:darkgreen">**(4) Kopsavilkums**</span>

</hgroup>


-----

# <lo-theory/> Ko darījām šajā nodarbībā

1. Minējām metodi sākotnējā tuvinājuma atrašanai (un pārbaudei, vai LP uzdevums
ir atrisināms un nav pretrunīgs). 
2. Aprakstījām elipsoīda algoritmu. 



