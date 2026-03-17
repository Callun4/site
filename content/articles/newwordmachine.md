Title: Python harjoittelua 2, Sanakone
Date: 2026-03-14 18:30
Category: Tietotekniikka
Tags: Python, Ohjelmointi
Image: images/pythonlogo.png
Slug: New-word-machine
Summary: Pythonin harjoittelua. Kielien harjoittelu ohjelma. Tiedoston luku ja datan haku netistä → haetun datan muokkaus 


<div class="card-body text-lext">
  <img src="{static}/images/pythonlogo.png" 
       class="img-fluid"
       style="max-width: 250px;"
       alt="Python">
</div>
  <div class="card-body">
    <a href="https://github.com/Callun4/New-words-machine" class="card-link" target="_blank" rel="noopener"
       >GitHub
       </a>
</div>


Toista Python harjoitteluprojektia varten sain ideaksi suunnitella kieltenopettelusovelluksen. Suurimpana ongelmana vieraissa kielissä minulla on mielestäni sanojen, ei kieliopin puute, joten halusin jonkun työkalun jossa saisi nappia painamalla listan sanoja opiskeltavaksi. Sovellus toimii mielestäni hyvin. Ainoa ongelma on mielestäni käännösohjelman hitaus. Tähän en ainakaan nyt keksi mitään ratkaisua, mutta ehkä tulevaisuudessa tämäkin korjaantuu.

Halusin sovelluksen sisältävän sekä tiettyä aihekohtaista sanastoa että täysin satunnaisia sanoja, missä mikään ei toistu kahdesti. Tämän takia valmistin ohjelmani toimimaan joko valmiin sanalistan avulla tai satunnaisilla <a href="https://random-word-api.herokuapp.com/word" target="_blank" rel="noopener">netistä</a> haetuilla sanoilla. Sanojen valinta tapahtuu simppelillä radio-napilla, minkä lisäksi on mahdollista valita sanojen lukumäärä. Valinnan jälkeen sovellus kääntää halutun sanamäärän valittuja sanoja käyttäen deep_translator pakettia. 

Käännökset tapahtuvat sovelluksessa englannista muihin kieliin. Lisäksi sovellus kääntää aina kahdelle kielelle kerralla. Tämän ominaisuuden laitoin ohjelmaan koska en luota täysin nettikääntäjiin ja halusin jonkin menetelmän jonka avulla tämän voi tarkastaa. Käännös tapahtuu englannista muihin kieliin koska olen huomannut sen olevan luotettavin käännös. Lisäksi mikäli sanalistoja etsii netistä ohjelmaa varten, on niiden löytäminen englanniksi huomattavasti helpompaa 

Projektia tehdessä huomasi jo että Python taitoni ovat hieman kehittyneet. Ohjelman kirjoittaminen oli huomattavasti nopeampaa ja komentoketjujen rakennekkin selvisi minulle nopeasti. Koodista sain ainakin tehtyä siistimpää kuin viimeksi, mutta ulkoasussa olisi edelleen parannettavaa.

<div style="display: flex; gap: 15px; margin-bottom: 20px; width: 100%;">
  <figure style="flex: 1; margin: 0; min-width: 0; max-width: none !important;">
    <img src="{static}/images/newword.png"
         style="width: 100% !important; max-width: none !important; height: 520px; object-fit: contain; border-radius: 6px;">
    <figcaption style="font-size: 0.85em; color: #6b3a1f; font-style: italic; text-align: center; margin-top: 5px;">
      Ohjelman ulkoasu
    </figcaption>
  </figure>
</div>


