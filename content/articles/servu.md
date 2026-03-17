Title: Kotipalvelimen käyttöönotto
Date: 2026-03-08 10:20
Category: Tietotekniikka
Image: images/serveri.jpg
Tags: Serveri, Linux, Kotipalvelin
Slug: Serveri1
Summary: Kotipalvelimen asennus ja käyttö, aloittelijan yritykset. 


<div class="card-body text-lext">
  <img src="{static}/images/serveri.jpg" 
       class="img-fluid"
       style="max-width: 250px;"
       alt="Serveri">
</div>

Käyttämieni pilvipalvelujen tallennustilan täyttyessä aloin pohtimaan että onko tilan ostaminen näiltä sivuilta kannattavaa. Enemmistö näillä sivuilla olevista tiedostoistani ovat siellä pitkäaikaissäilytyksessä ja niihin harvemmin tarvitsee päästä käsiksi poissa kotoa. 

Pilvipalvelujen myymät lisämuistit ovat mielestäni melko kalliita verrattuna niiden tarjoamaan muistin määrään, vaikka palvelun käytännöllisyys on todennäköisesti myös huomioitu hinnassa. Itse satuin kuitenkin myös omistamaan valmiiksi tyhjiä kovalevyjä, jotka olin hankkinut vanhoista kannettavista. Täten päädyin että oman palvelimen hankkiminen olisi minulle todennäköisesti edullisin, opettavaisin ja kätevin vaihtoehto. 

Palvelin projekti alkoi oikeanlaisen koneen hankkimisella. Tavoitteenani oli hankkia pienemmän kokoluokan pöytäkone alhaisemman energiankulutuksen saavuttamiseksi. Kone ei kuitenkaan saanut olla ihan minimalli sillä olen aikaisemmin huomannut niiden tuulettimien pitävän melkoista ääntä altistuessa kovemmalle kuormitukselle. Koneelta vaadin myös vähintään 8 GB Ramia ja prosessorin jossa olisi vähintään 4-ydintä. Tällaista lähdin etsimään huutokauppasivuilta, missä myydään käytettyjä työkoneita.

Oikeanlaisen ja hintaisen koneen löytymisessä kesti n. 1 kk. Sellainen kuitenkin lopulta löytyi kun vastaan tuli pienehkö Lenovon työasema. Koneen ominaisuudet löytyy alta. Kuvassa näkyvästä luukusta huolimatta koneessa ei ole CD-asemaa. Loppujen lopuksi koneelle tuli hintaa toimituksineen hieman yli 120 €. 

Koneen saavuttua latasin Ubuntun palvelinjärjestelmän ja käytin pääkoneessani valmiiksi löytyvää USB-levykuvan kirjoitusohjelmaa tehdäkseni bootattavan USB:n. Asennus sujui nopeasti ja mutkitta internetin tarjoamien ohjeiden ansiosta. Erityisesti <a href="https://www.youtube.com/watch?v=2Btkx9toufg" class="card-link" target="_blank" rel="noopener">tästä</a> videosta oli paljon apua. Käyttöliittymän jätin asentamatta eli palvelin toimii ns. päättömästi. Yhteyden siihen saa helposti pääkoneelta ssh:n avulla. Asennuksen jälkeen asensin vielä Cockpitin huoltotyökaluksi ja Nextcloudin omaa pilvipalvelua varten. 

Vielä jää tehtäväksi omien kovalevyjeni asennus tietokoneeseen ja jos paikat eivät riitä niin alan pohtimaan NAS:in hankkimista. Näistä jäljellä olevista askeleista huolimatta projekti on edennyt odotettua jouhevammin. Kaiken kaikkiaan mielestäni palvelinjärjestelmän asennus ohjelmineen oli äärimmäisen helppoa, minunkin Linux-kokemuksella. Useampaa ohjelmaa varten löytyy jo niiden nettisivuilta riittävät asennusohjeet ja jos tämä ei riitä vanhoja foorumikeskusteluita on myös runsaasti.

<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" data-toggle="tab" href="#Faktoja">Tietokone</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" data-toggle="tab" href="#Kasvatus">Järjestelmä</a>
  </li>
</ul>
<div class="tab-content">
  <div class="tab-pane fade show active" id="Faktoja">
    <div class="card border-primary mb-3" style="max-width: 20rem;">
      <div class="card-header">Koneen malli:</div>
      <div class="card-body">
        <h4 class="card-title">•Lenovo V530s SSF</h4>
        <p class="card-text">•Intel i5-8400 2.8 GHz, 6-ydintä</p>
        <p class="card-text">•8 GB DDR4</p>
        <p class="card-text">•300 GB SSD</p>
        <p class="card-text">•UHD Graphics 630</p>
      </div>
    </div>
  </div>  
  <div class="tab-pane fade" id="Kasvatus">
      <div class="card-header">Järjestelmä ja asennukset:</div>
        <p class="card-text">•Ubuntu 24.04.4 LTS</p>
        <p class="card-text">•Nextcloud</p>
  </div>
</div>
