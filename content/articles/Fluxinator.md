Title: Python harjoittelua 1, Fluxinator
Date: 2026-03-07 14:30
Category: Tietotekniikka
Tags: Python, Ohjelmointi
Image: images/pythonlogo.png
Slug: Fluxinator
Summary: Pythonin harjoittelua. CSV-data:n luku → muokkaus → kirjoitus-ohjelman tekeminen.


<div class="card-body text-lext">
  <img src="{static}/images/pythonlogo.png" 
       class="img-fluid"
       style="max-width: 250px;"
       alt="Python">
</div>
  <div class="card-body">
    <a href="https://github.com/Callun4/Fluxinator-dataconverter" class="card-link" target="_blank" rel="noopener"
       >GitHub
       </a>
</div>

Pythonia oppiakseni koitin miettiä miten sitä olisi parasta harjoitella. Tavoitteena oli kuitenkin tehdä jotain hyödyllistä samalla, niin päädyin ohjelman tekoon. Mahdollista aihetta miettiessä pohdin mitä yksitoikkoista ja usein tehtävää aihetta voisi helpottaa. Eräs tällainen aihe on kaasuvuon mittausdatan käsittely. 

Kaasuvuon mittaukset ovat hyvin ollenainen osa biogeokemian tutkimusta. Kaasuvuon mittauksissa mittauskohteita on yleensä lukuisia, joten dataa on paljon. Datan käsittelyä varten on olemassa valmis koodi, jonka avulla saadaan laskettua mittaushetken aikana ollut kaasuvuo yksikössä µmol m⁻² s⁻¹. Kaasuvuota tarkastellaan kuitenkin yleensä jossakin massayksikössä ja pidemmällä ajalla, mikä edellyttää datan muuntamista muotoon: massa (esim. g) m⁻² aika(esim. 1-24h). Tässä kohtaa tekemäni ohjelma astuu kuvaan. 

Ohjelmani tarkoituksena on lukea useampi mittausdata CSV samanaikaisesti, muuntaa niissä olevan kaasunvuo oikeaan, valittuun massayksikköön ja yhdistää annettujen CSV-tiedostojen data yhteen tiedostoon. Helppokäyttöisyyttä edistääkseni tein ohjelmaa varten oman käyttöliittymän tkinter ja messagebox moduulien avulla. 
<figure style="float: left; margin: 0 20px 20px 0; max-width: 60%;">
  <img src="{static}/images/Fluxi.png" class="img-fluid" alt="Kuva">
  <figcaption style="font-size: 0.85em; color: #6b3a1f; font-style: italic; text-align: center; margin-top: 5px;">
    Ohjelman ulkoasu
  </figcaption>
</figure>

Ohjelman käyttö alkaa valitsemalla CSV tiedostot joita halutaan muokata. Näiden tiedostojen sisältämä kaasu (CO2, N2O tai CH4) valitaan pudotusvalikosta. Tämän jälkeen valitaan, halutaanko data myös muuntaa vai ainoastaan yhdistää, jonka jälkeen valitaan halutut yksiköt pudotusvalikoista. Valinnan jälkeen merkataan tallennussijanti ja nimetään tiedosto. Tämän jälkeen painetaan Muuta-painiketta, mikä lukee CSV:stä kolumnit HM.flux ja LM.flux sekä suorittaa niille määrätyt toimenpiteet; yhdistäen useamman asiakirjan yhteisten otsikoiden alle (Näyte, HM.flux, LM.flux ja kaasu). 

Projekti oli mielestäni hyvin opettavainen. Erityisesti tkinter moduulin käyttö tuli tutuksi ja tulevaisuudessa koitan pyrkiä nätimpien käyttöliittymien tekemiseen. Hankalinta mielestäni oli komentojen ja niiden logiikkaketjujen rakentaminen, esimerkiksi missä järjestyksessä datan muuntaminen suoritetaan ja kuinka ohjelman pitäisi toimia käyttäjän tehdessä virheen käyttöliittymässä. Aiempi Python-kokemukseni ei ole myöskään edellyttänyt useamman eri tiedoston muokkausta samanaikaisesti ja niiden koostamista yhteen tiedostoon. Kokonaisuudessa sanoisin kuitenkin oppineeni hyvin ohjelman-teon perusteita. Parannettavaa minulla olisi kielen eri lauseiden muistamisessa, mutta tämä varmaan tulee ajan kanssa.
