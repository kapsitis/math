# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span style="color:darkgreen">**(1) Ievads**</span>  
<span>(2) [Kļūdu detekcija un korekcija](#section-1)</span>  
<span>(3) [Kļūdu korekcijas kodi](#section-2)</span>  
<span>(4) [Heminga kodi](#section-3)</span>  
<span>(5) [Citi lineāri kodi](#section-4)</span>  
<span>(6) [Rīda-Solomona kodi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>




## <lo-theory/> Mērķi

* Definēt kļūdu detekcijas un korekcijas atšķirības
* Pamatot apgalvojumu par divu kļūdu korekcijas kodu attālumu.
* Lietot un pamatot Heminga kodus. 





# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span>(1) [Ievads](#section)</span>  
<span style="color:darkgreen">**(2) Kļūdu detekcija un korekcija**</span>  
<span>(3) [Kļūdu korekcijas kodi](#section-2)</span>  
<span>(4) [Heminga kodi](#section-3)</span>  
<span>(5) [Citi lineāri kodi](#section-4)</span>  
<span>(6) [Rīda-Solomona kodi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>


# <lo-theory/> Kļūdu detekcija

![Error detection](error-detection.png)


## <lo-summary/> Bitu paritātes metode

**Situācija:** Pārraida $n$ bitu virkni 
$x_1,x_2,\ldots,x_n \in \{ 0; 1\}$. 
Lai konstatētu iespējamu kļūdu $1$ bitā (kas var gan 
iestāties, gan neiestāties), pārraida $n+1$ bitus:  
Visus $x_1,x_2,\ldots,x_n$ un arī pēdējo bitu
$$\left( x_1 + x_2 + \ldots + x_n \left)\,\text{mod}\,2.$$

Pēdējais bits glabā visu iepriekšējo bitu paritāti. 
Tāpēc visu $n+1$ bitu paritāte ir $0$. Ja pārraidē rodas viena
kļūda, tad paritāte būs $1$, un kļūdu varēs konstatēt. 


## <lo-summary/> CRC kontrolsumma

...






# <lo-theory/> Kļūdu korekcija

![Error correction](error-correction.png)

Ideja visās metodēs - papildināt pārraidāmos datus ar 
papildinformāciju, cerot, ka papildinformācija ļaus pamanīt 
kļūdas. 


## <lo-



# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span>(1) [Ievads](#section)</span>  
<span>(2) [Kļūdu detekcija un korekcija](#section-1)</span>  
<span style="color:darkgreen">**(3) Kļūdu korekcijas kodi**</span>  
<span>(4) [Heminga kodi](#section-3)</span>  
<span>(5) [Citi lineāri kodi](#section-4)</span>  
<span>(6) [Rīda-Solomona kodi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>






# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span>(1) [Ievads](#section)</span>  
<span>(2) [Kļūdu detekcija un korekcija](#section-1)</span>  
<span>(3) [Kļūdu korekcijas kodi](#section-2)</span>  
<span style="color:darkgreen">**(4) Heminga kodi**</span>  
<span>(5) [Citi lineāri kodi](#section-4)</span>  
<span>(6) [Rīda-Solomona kodi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>






# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span>(1) [Ievads](#section)</span>  
<span>(2) [Kļūdu detekcija un korekcija](#section-1)</span>  
<span>(3) [Kļūdu korekcijas kodi](#section-2)</span>  
<span>(4) [Heminga kodi](#section-3)</span>  
<span style="color:darkgreen">**(5) Citi lineāri kodi**</span>  
<span>(6) [Rīda-Solomona kodi](#section-5)</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>






# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span>(1) [Ievads](#section)</span>  
<span>(2) [Kļūdu detekcija un korekcija](#section-1)</span>  
<span>(3) [Kļūdu korekcijas kodi](#section-2)</span>  
<span>(4) [Heminga kodi](#section-3)</span>  
<span>(5) [Citi lineāri kodi](#section-4)</span>  
<span style="color:darkgreen">**(6) Rīda-Solomona kodi**</span>  
<span>(7) [Kopsavilkums](#section-6)</span>

</hgroup>







# &nbsp;

<hgroup>

<h1 style="font-size:28pt">Lietišķie algoritmi</h1>

<blue>Kļūdu korekcija - 1</blue>

</hgroup><hgroup>

<span>(1) [Ievads](#section)</span>  
<span>(2) [Kļūdu detekcija un korekcija](#section-1)</span>  
<span>(3) [Kļūdu korekcijas kodi](#section-2)</span>  
<span>(4) [Heminga kodi](#section-3)</span>  
<span>(5) [Citi lineāri kodi](#section-4)</span>  
<span>(6) [Rīda-Solomona kodi](#section-5)</span>  
<span style="color:darkgreen">**(7) Kopsavilkums**</span>

</hgroup>


