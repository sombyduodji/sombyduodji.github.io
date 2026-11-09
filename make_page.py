#!/usr/bin/env python3
"""Tekee index.html:n neljällä kielellä (suomi, norja, pohjoissaame, englanti).

Kaikki tekstit ovat tässä tiedostossa kielittäin; sivu näyttää valitun kielen lippupainikkeista.
Käyttö: python3 make_page.py
Pohjoissaame on konekäännös, joka on tarkistettu saamen oikolukijalla (Divvun / libvoikko 'se').
"""
import html

LANGS = [  # koodi, nimi omalla kielellään, html lang
    ("fi", "Suomi", "fi"),
    ("nb", "Norsk", "nb"),
    ("se", "Sámegiella", "se"),
    ("en", "English", "en"),
]

GIEVRA_APK = "https://github.com/sombyduodji/gievra/releases/latest/download/Gievra-android-arm64.apk"

T = {
    # ---------------------------------------------------------------- suomi
    "fi": dict(
        title="Sombyduodji – sovellukset",
        desc="Maksuttomia ja avoimia sovelluksia: Gievra – Treenipäiväkirja, Sátni FST -pohjoissaamen sanakirja ja "
        "Sátnemátki-sanapeli lapsille. Ei mainoksia, ei tiliä, lähdekoodi avoimena.",
        tagline="Pieniä sovelluksia saamen kieleen ja arkeen.",
        lead="Teen maksuttomia ja avoimia sovelluksia: pohjoissaamen sanakirjan, sanapelin lapsille ja "
        "treenipäiväkirjan. Kaikki ovat ilmaisia, eikä niissä ole mainoksia, tiliä tai seurantaa.",
        chips=["Maksuton", "Avoin lähdekoodi (GPL-3.0)", "Ei mainoksia", "Ei tiliä", "Toimii ilman verkkoa"],
        note="🛠️ Sovellukset ovat kehityksessä: ominaisuudet, ulkoasu ja tiedostomuodot voivat vielä muuttua. "
        "Palaute auttaa päättämään, mihin keskitytään.",
        apps="Sovellukset",
        langs_label="Kielet",
        gievra_what="Treenipäiväkirja salille ja kuntoiluun · Android ja selain",
        gievra_status="Juuri julkaistu · päivittyy usein",
        gievra_desc="<i>Gievra</i> on pohjoissaamea ja tarkoittaa <i>vahvaa</i>. Treenit tallentuvat tavallisina "
        "Markdown-tiedostoina omaan kansioosi: <i>sinun treenisi, sinun tiedostosi</i>.",
        gievra_feats=[
            "sarjan kirjaus yhdellä napautuksella, lämmittelysarjat ja painoehdotukset valmiina",
            "valmiit treeniohjelmat: voimanosto, lihaskasvu, rasvanpoltto, yleiskunto, kahvakuula ja kehonpaino",
            "uutta: valinnainen GPS juoksuun, kävelyyn ja pyöräilyyn; reitti kartalla ja .gpx-tiedostona, korjautuu poluille; nousut, korkeusprofiili ja kilometrien vauhti (kaikki karttamaat); offline-kartat Suomeen, Pohjoismaihin, Iso-Britanniaan ja Espanjaan",
            "syke, kalorit ja askeleet kellosta Health Connectin kautta (Android, vain luku); uutta: tehty liikunta ja salitreeni kokonaisena Health Connectista, myös pelkät askeleet esim. kävelymatolta",
            "palautusajastin, tilastot (viikko–vuosi), ennätykset ja liikeohjeet animaatioineen; kehonpainon seuranta",
            "juoksulle oma kehitysnäkymä: vauhti, kilometrit, kevyiden lenkkien kehitys ja ennätykset",
            "ohjelmapohjat (<code>.gmd</code>) jaettaviksi; tuonti FitNotesista",
        ],
        gievra_langs="käyttöliittymä suomeksi, englanniksi ja kokeellisesti pohjoissaameksi (konekäännös); liikkeiden nimet "
        "suomeksi, englanniksi tai molemmilla.",
        gievra_links=["Kotisivu", "Kokeile selaimessa", "Lataa Androidille", "Lähdekoodi", "🗺️ Lataa offline-kartat"],
        satni_what="Pohjoissaame–suomi–norja-sanakirja ja taivutin · Linux, Windows, Android ja selain",
        satni_status="Julkiset julkaisut tauolla",
        satni_desc="Uudet julkiset versiot ovat tauolla, kunnes suljettu testaus on valmis. Työ jatkuu kulissien "
        "takana, ja verkkoversiota ja nykyisiä latauksia voi käyttää edelleen.",
        satni_feats=[
            "noin 80 000 pohjoissaamen sanaa, joista noin 74 000 täysin taivutustauluin",
            "haku taivutetulla muodolla (<i>dagan</i> → <i>dahkat</i>) tai suomeksi ja norjaksi",
            "astevaihtelu väreillä, ääntäminen puhesynteesillä, historia ja suosikit",
            "toimii ilman verkkoa; kielitieto GiellaLT:ltä, Divvunilta ja Giellateknolta",
        ],
        satni_langs="sanakirja pohjoissaamesta suomeen ja norjaan ja toisin päin; käyttöliittymä suomeksi ja "
        "norjaksi; osalle sanoista käännös myös englanniksi sekä inarin-, luulajan- ja eteläsaameksi; "
        "kokeellisesti koltansaamen sanoja.",
        satni_links=["Kotisivu ja verkkoversio", "Lataukset", "Lähdekoodi"],
        mat_what="Pohjoissaamen sanapeli lapsille · selaimessa",
        mat_status="Teknologiademo",
        mat_desc="<i>Sátnemátki</i> tarkoittaa sanamatkaa. Pelaaja kulkee paikasta toiseen Máhttena tai Biretinä, "
        "peli sanoo saamenkielisen sanan ja pelaaja etsii sen tarkoittaman asian. Hävitä ei voi.",
        mat_feats=[
            "koti, metsä, kauppa, rautakauppa, kirjasto, luokka, parkkipaikka ja laavu",
            "kosketus näyttää sanan saameksi ja suomeksi, joten aiempaa osaamista ei tarvita",
            "numerot sanoina ja numeroina, kaupassa ostoslista ja maksaminen",
        ],
        mat_langs="pohjoissaamen sanat suomennoksineen; käyttöliittymä suomeksi.",
        mat_links=["Pelaa selaimessa", "Lähdekoodi"],
        free_h="Maksuton ja avoin",
        free=[
            ("Ilmainen", "Kaikki sovellukset ovat ja pysyvät maksuttomina. Ei mainoksia, ei tilauksia, ei kirjautumista."),
            ("Avoin lähdekoodi", "Lähdekoodi on GitHubissa GNU GPL v3.0 -lisenssillä: saat käyttää, tutkia, muokata ja jakaa."),
            ("Tietosi pysyvät sinulla", "Sovellukset toimivat ilman verkkoa, eivätkä ne lähetä tietojasi minnekään. "
             "Poikkeuksena valinnaiset toiminnot, kuten Sátni FST:n ääntäminen (Divvunin puhesynteesi) ja kokeellinen kuvahaku."),
        ],
        fb_h="Palaute on aina tervetullutta",
        fb_intro="Virheet, ideat, käännöskorjaukset ja kaikki muu auttavat sovelluksia eteenpäin:",
        fb_gievra="Gievra: {mail} tai sovelluksessa ☰ → <i>Ilmoita ongelmasta</i>",
        fb_satni="Sátni FST ja Sátnemátki: {mail}",
        fb_github="GitHubissa: {link} (kunkin sovelluksen virheilmoitukset ja ehdotukset)",
        coffee="Jos sovelluksista on sinulle hyötyä, voit {link} ☕",
        coffee_link="tarjota kahvit",
        mt_note="",
        footer="Sombyduodji · Juha Somby",
        icon_alt=["Gievran logo: kahvakuula", "Sátni FST:n logo: saamen lipun värinen pisara",
                  "Sátnemátki: isometrinen koti, jossa perhe ja Biret"],
    ),
    # ---------------------------------------------------------------- norsk
    "nb": dict(
        title="Sombyduodji – apper",
        desc="Gratis apper med åpen kildekode: Gievra (treningsdagbok), Sátni FST (nordsamisk ordbok) og Sátnemátki "
        "(ordspill for barn). Ingen reklame, ingen konto.",
        tagline="Små apper for samisk språk og hverdag.",
        lead="Jeg lager gratis og åpne apper: en nordsamisk ordbok, et ordspill for barn og en treningsdagbok. "
        "Alle er gratis, uten reklame, konto eller sporing.",
        chips=["Gratis", "Åpen kildekode (GPL-3.0)", "Ingen reklame", "Ingen konto", "Virker uten nett"],
        note="🛠️ Appene er under utvikling: funksjoner, utseende og filformater kan fortsatt endres. "
        "Tilbakemeldinger hjelper meg å velge hva jeg skal prioritere.",
        apps="Apper",
        langs_label="Språk",
        gievra_what="Treningsdagbok for styrketrening og mosjon · Android og nettleser",
        gievra_status="Nettopp lansert · oppdateres ofte",
        gievra_desc="<i>Gievra</i> er nordsamisk og betyr <i>sterk</i>. Øktene lagres som vanlige Markdown-filer "
        "i en mappe du velger: <i>din trening, dine filer</i>.",
        gievra_feats=[
            "logg et sett med ett trykk, oppvarmingssett og vektforslag ferdig utfylt",
            "ferdige treningsprogrammer: styrkeløft, muskelvekst, fettforbrenning, allsidig form, kettlebell og kroppsvekt",
            "nytt: valgfri GPS for løping, gåing og sykling; ruten på kart og som .gpx-fil, tilpasses stiene; stigning, høydeprofil og tempo per kilometer (alle kartlandene); frakoblede kart for Norden, Storbritannia og Spania",
            "puls, kalorier og skritt fra klokka via Health Connect (Android, kun lesing); nytt: hent en fullført økt eller styrkeøkt fra Health Connect, også bare skritt, f.eks. fra tredemølle",
            "pausetimer, statistikk (uke–år), rekorder og øvelsesveiledninger med animasjoner; vektlogg",
            "egen utviklingsvisning for løping: tempo, kilometer, rolige turer over tid og rekorder",
            "programmaler (<code>.gmd</code>) til deling; import fra FitNotes",
        ],
        gievra_langs="brukergrensesnitt på finsk, engelsk og eksperimentelt på nordsamisk (maskinoversatt); navn på "
        "øvelser på finsk, engelsk eller begge.",
        gievra_links=["Hjemmeside", "Prøv i nettleseren", "Last ned for Android", "Kildekode", "🗺️ Last ned offline-kart"],
        satni_what="Nordsamisk–finsk–norsk ordbok og bøyingsverktøy · Linux, Windows, Android og nettleser",
        satni_status="Offentlige utgivelser på pause",
        satni_desc="Nye offentlige versjoner venter til den lukkede testen er ferdig. Arbeidet fortsetter i "
        "kulissene, og nettversjonen og dagens nedlastinger kan fortsatt brukes.",
        satni_feats=[
            "rundt 80 000 nordsamiske ord, rundt 74 000 av dem med fullstendige bøyingstabeller",
            "søk med en bøyd form (<i>dagan</i> → <i>dahkat</i>) eller på finsk og norsk",
            "stadieveksling i farger, uttale med talesyntese, historikk og favoritter",
            "virker uten nett; språkdata fra GiellaLT, Divvun og Giellatekno",
        ],
        satni_langs="ordbok fra nordsamisk til finsk og norsk og motsatt vei; brukergrensesnitt på finsk og norsk; "
        "for noen ord også oversettelser til engelsk, enaresamisk, lulesamisk og sørsamisk; eksperimentelt "
        "skoltesamiske ord.",
        satni_links=["Hjemmeside og nettversjon", "Nedlastinger", "Kildekode"],
        mat_what="Nordsamisk ordspill for barn · i nettleseren",
        mat_status="Teknologidemo",
        mat_desc="<i>Sátnemátki</i> betyr ordreise. Spilleren går fra sted til sted som Máhtte eller Biret, "
        "spillet sier et samisk ord, og spilleren finner tingen ordet betyr. Det går ikke an å tape.",
        mat_feats=[
            "hjemme, skogen, matbutikken, jernvarehandelen, biblioteket, klasserommet, parkeringsplassen og lavvoen",
            "trykk på noe for å se ordet på samisk og finsk, så ingen forkunnskaper trengs",
            "tall som ord og sifre, handleliste og betaling i butikken",
        ],
        mat_langs="nordsamiske ord med finsk oversettelse; brukergrensesnitt på finsk.",
        mat_links=["Spill i nettleseren", "Kildekode"],
        free_h="Gratis og åpent",
        free=[
            ("Gratis", "Alle appene er og forblir gratis. Ingen reklame, ingen abonnement, ingen innlogging."),
            ("Åpen kildekode", "Kildekoden ligger på GitHub under GNU GPL v3.0: du kan bruke, studere, endre og dele den."),
            ("Dataene dine blir hos deg", "Appene virker uten nett og sender ikke dataene dine noe sted. Unntak er "
             "valgfrie funksjoner, som uttalen i Sátni FST (Divvuns talesyntese) og det eksperimentelle bildesøket."),
        ],
        fb_h="Tilbakemeldinger er alltid velkomne",
        fb_intro="Feil, ideer, rettelser til oversettelser og alt annet hjelper appene videre:",
        fb_gievra="Gievra: {mail} eller i appen ☰ → <i>Ilmoita ongelmasta</i> (rapporter et problem)",
        fb_satni="Sátni FST og Sátnemátki: {mail}",
        fb_github="På GitHub: {link} (feilrapporter og forslag for hver app)",
        coffee="Hvis appene er nyttige for deg, kan du {link} ☕",
        coffee_link="spandere en kaffe",
        mt_note="",
        footer="Sombyduodji · Juha Somby",
        icon_alt=["Gievras logo: en kettlebell", "Sátni FSTs logo: en dråpe i det samiske flaggets farger",
                  "Sátnemátki: et isometrisk hjem med familie og Biret"],
    ),
    # ---------------------------------------------------------------- davvisámegiella
    "se": dict(
        title="Sombyduodji – prográmmat",
        desc="Nuvttá ja rabas prográmmat: Gievra (hárjehallanbeaivegirji), Sátni FST (davvisámegiel sátnegirji) ja "
        "Sátnemátki (sátnespeallu mánáide). Eai reklámat, ii kontu.",
        tagline="Unna prográmmat sámegiela ja árgabeaivvi várás.",
        lead="Ráhkadan nuvttá ja rabas prográmmaid: davvisámegiel sátnegirjji, sátnespealu mánáide ja "
        "hárjehallanbeaivegirjji. Buot leat nuvttá, eaige dain leat reklámat, kontot iige čuovvun.",
        chips=["Nuvttá", "Rabas gáldokoda (GPL-3.0)", "Eai reklámat", "Ii kontu", "Doaibmá neahta haga"],
        note="🛠️ Prográmmat leat ain ovdánahttimis: doaimmat, hápmi ja fiilahámit sáhttet vel rievdat. "
        "Máhcahat veahkeha mearridit, maid galgá vuoruhit.",
        apps="Prográmmat",
        langs_label="Gielat",
        gievra_what="Hárjehallanbeaivegirji sállii ja lihkadeapmái · Android ja neahttalohkki",
        gievra_status="Aitto almmuhuvvon · ođasmuvvá dávjá",
        gievra_desc="<i>Gievra</i> mearkkaša <i>nanu</i>. Hárjehallamat vurkejuvvojit dábálaš Markdown-fiilan "
        "du iežat máhppii: <i>du hárjehallamat, du fiillat</i>.",
        gievra_feats=[
            "ráiddu vurken ovttain deaddilemiin, liegganeami ráiddut ja deaddoevttohusat gárvvisin",
            "gárvves hárjehallanprográmmat: fápmolokten, deahkkešattolašvuohta, buoiddi boaldin, oppalaš návccat, "
            "kettlebell ja rumašdeaddu",
            "ođđa: eaktodáhtolaš GPS viehkamii, vázzimii ja sihkkelastimii; johtolat kárttas ja .gpx-fiilan, divvojuvvo bálgáide; goargŋumat ja allodatprofiila (buot kártariikkat); kárttat interneahta haga: Suopma, Ruoŧŧa, Norga, Dánmárku, Islánda, Stuorra-Británnia ja Spánja",
            "pulsa, kaloriijat ja lávkkit diimmus Health Connect bokte (Android, dušše lohkat); ođđa: lasit dahkkon lihkadeami ja sállahárjehallama Health Connect bokte, maiddái dušše lávkkiid",
            "vuoiŋŋasteami áigemihttár, statistihkka (vahkku–jahki), rekordat ja hárjehusaid rávvagat animašuvnnaiguin; rumašdeattu čuovvun",
            "viehkamii iežas ovdánanoaidnu: leaktu, kilomehterat ja rekordat",
            "prográmmavuođut (<code>.gmd</code>) juogadeapmái; hárjehallamiid viežžan FitNotes-prográmmas",
        ],
        gievra_langs="geavahanlávdi suomagillii, eŋgelasgillii ja geahččaleapmin davvisámegillii (mašiidnajorgalus); "
        "hárjehusaid namat suomagillii, eŋgelasgillii dahje goappašagain.",
        gievra_links=["Ruoktosiidu", "Geahččal neahttalohkkis", "Viečča Androidii", "Gáldokoda", "🗺️ Viečča kárttaid fierpmehis geavahussii"],
        satni_what="Davvisámegiel sátnegirji suomagillii ja dárogillii, sojahanreaidu · Linux, Windows, Android ja neahttalohkki",
        satni_status="Almmolaš veršuvnnat bottus",
        satni_desc="Ođđa almmolaš veršuvnnat vurdet dassážii go giddejuvvon geahččaleapmi lea gárvvis. Bargu "
        "joatkašuvvá duogábealde, ja neahttaveršuvnna ja dálá veršuvnnaid sáhttá ain geavahit.",
        satni_feats=[
            "sullii 80 000 davvisámegiel sáni, main sullii 74 000 sánis leat ollislaš sojahantabeallat",
            "ohcan sojahuvvon hámiin (<i>dagan</i> → <i>dahkat</i>) dahje suomagillii ja dárogillii",
            "ceahkkemolsašupmi ivnniiguin, hupman hállansyntesain, historjá ja favorihtat",
            "doaibmá neahta haga; gielladieđut GiellaLT:s, Divvunis ja Giellateknos",
        ],
        satni_langs="sátnegirji davvisámegielas suomagillii ja dárogillii ja nuppe guvlui; geavahanlávdi "
        "suomagillii ja dárogillii; muhtin sániide jorgalusat maiddái eŋgelasgillii, anárašgillii, "
        "julevsámegillii ja máttasámegillii; geahččaleapmin nuortalašgiel sánit.",
        satni_links=["Ruoktosiidu ja neahttaveršuvdna", "Veršuvnnat", "Gáldokoda"],
        mat_what="Davvisámegiel sátnespeallu mánáide · neahttalohkkis",
        mat_status="Teknologiijaovdačájeheapmi",
        mat_desc="Speallanolmmoš (Máhtte dahje Biret) vázzá báikkis báikái, speallu dadjá sámegiel sáni, ja "
        "speallanolmmoš ohcá dan, maid sátni mearkkaša. Vuoittáhallat ii sáhte.",
        mat_feats=[
            "ruoktu, vuovdi, gávpi, ruovdegávpi, girjerádju, skuvlaluokka, biilabáiki ja lávvu",
            "go guoská juoidá, oainnát sáni sámegillii ja suomagillii, nu ahte ovdamáhttu ii dárbbašuvvo",
            "logut sátnin ja nummirin, gávppis oastinlistu ja máksin",
        ],
        mat_langs="davvisámegiel sánit suomagiel jorgalusaiguin; geavahanlávdi suomagillii.",
        mat_links=["Speala neahttalohkkis", "Gáldokoda"],
        free_h="Nuvttá ja rabas",
        free=[
            ("Nuvttá", "Buot prográmmat leat ja bissot nuvttá. Eai reklámat, eai diŋgojumit, ii sisačáliheapmi."),
            ("Rabas gáldokoda", "Gáldokoda lea GitHubas GNU GPL v3.0 -liseanssain: sáhtát geavahit, dutkat, "
             "rievdadit ja juogadit dan."),
            ("Du dieđut bissot dus", "Prográmmat doibmet neahta haga, eaige sádde du dieđuid gosage. Spiehkastagat "
             "leat válljejuvvon doaimmat, nugo Sátni FST hupman (Divvuna hállansyntesa) ja geahččaleaddji govvaohcan."),
        ],
        fb_h="Máhcahat lea álo buresboahtin",
        fb_intro="Meattáhusat, jurdagat, jorgalusaid divvumat ja buot eará veahkehit prográmmaid ovddos:",
        fb_gievra="Gievra: {mail} dahje prográmmas ☰ → <i>Dieđit váttisvuođas</i>",
        fb_satni="Sátni FST ja Sátnemátki: {mail}",
        fb_github="GitHubas: {link} (juohke prográmma meattáhusdieđáhusat ja evttohusat)",
        coffee="Jus prográmmat leat dutnje ávkkálaččat, sáhtát {link} ☕",
        coffee_link="fállat káffe",
        mt_note="Sámegiel jorgalus lea mašiidnajorgalus, mii lea dárkkistuvvon sámegiel čállindárkkisteaddjiin. "
        "Divvumat leat buresboahtin: {mail}",
        footer="Sombyduodji · Juha Somby",
        icon_alt=["Gievra logo: kettlebell", "Sátni FST logo: sámi leavgga ivnnat goaikkanasas",
                  "Sátnemátki: ruoktu, gos lea bearaš ja Biret"],
    ),
    # ---------------------------------------------------------------- English
    "en": dict(
        title="Sombyduodji – apps",
        desc="Free, open-source apps: Gievra (training log), Sátni FST (North Sámi dictionary) and Sátnemátki "
        "(word game for children). No ads, no accounts.",
        tagline="Small apps for the Sámi language and everyday life.",
        lead="I make free and open apps: a North Sámi dictionary, a word game for children and a training log. "
        "They are all free, with no ads, accounts or tracking.",
        chips=["Free", "Open source (GPL-3.0)", "No ads", "No account", "Works offline"],
        note="🛠️ The apps are under development: features, look and file formats may still change. "
        "Feedback helps decide what to focus on.",
        apps="Apps",
        langs_label="Languages",
        gievra_what="Training log for the gym and fitness · Android and browser",
        gievra_status="Just released · updated often",
        gievra_desc="<i>Gievra</i> is North Sámi for <i>strong</i>. Workouts are saved as plain Markdown files "
        "in a folder you choose: <i>your training, your files</i>.",
        gievra_feats=[
            "log a set with one tap, with warm-up sets and weight suggestions filled in",
            "ready-made programs: powerlifting, muscle growth, fat loss, general fitness, kettlebell and bodyweight",
            "new: optional GPS for running, walking and cycling; the route on a map and as a .gpx file, snapped to paths; climb, elevation profile and pace per kilometre (all map countries); offline maps for Finland, the Nordic countries, the UK and Spain",
            "heart rate, calories and steps from your watch via Health Connect (Android, read only); new: add a completed workout or gym session from Health Connect, even steps only, e.g. from a walking pad",
            "rest timer, statistics (week to year), records and exercise guides with animations; body weight tracking",
            "a separate progress view for running: pace, distance, easy-run progress and records",
            "program templates (<code>.gmd</code>) to share; import from FitNotes",
        ],
        gievra_langs="user interface in Finnish, English and, experimentally, North Sámi (machine translated); exercise "
        "names in Finnish, English or both.",
        gievra_links=["Home page", "Try in your browser", "Download for Android", "Source code", "🗺️ Download offline maps"],
        satni_what="North Sámi–Finnish–Norwegian dictionary and inflection tool · Linux, Windows, Android and browser",
        satni_status="Public releases on hold",
        satni_desc="New public releases are on hold until closed testing is finished. Work continues behind the "
        "scenes, and the web version and current downloads can still be used.",
        satni_feats=[
            "about 80,000 North Sámi words, about 74,000 of them with full inflection tables",
            "search with an inflected form (<i>dagan</i> → <i>dahkat</i>) or in Finnish and Norwegian",
            "consonant gradation in colour, pronunciation with speech synthesis, history and favourites",
            "works offline; language data from GiellaLT, Divvun and Giellatekno",
        ],
        satni_langs="dictionary from North Sámi to Finnish and Norwegian and the other way round; user interface "
        "in Finnish and Norwegian; for some words also translations into English, Inari, Lule and Southern "
        "Sámi; experimentally Skolt Sámi words.",
        satni_links=["Home page and web version", "Downloads", "Source code"],
        mat_what="North Sámi word game for children · in your browser",
        mat_status="Technology demo",
        mat_desc="<i>Sátnemátki</i> means <i>word journey</i>. The player walks from place to place as Máhtte or "
        "Biret, the game says a Sámi word, and the player finds the thing it means. You can't lose.",
        mat_feats=[
            "home, forest, grocery store, hardware store, library, classroom, car park and lávvu",
            "touching anything shows its word in Sámi and Finnish, so no prior knowledge is needed",
            "numbers as words and digits, a shopping list and paying in the store",
        ],
        mat_langs="North Sámi words with Finnish translations; user interface in Finnish.",
        mat_links=["Play in your browser", "Source code"],
        free_h="Free and open",
        free=[
            ("Free", "All the apps are and will stay free. No ads, no subscriptions, no sign-in."),
            ("Open source", "The source code is on GitHub under the GNU GPL v3.0: you may use, study, change and share it."),
            ("Your data stays with you", "The apps work offline and don't send your data anywhere. The exceptions "
             "are optional features, such as Sátni FST's pronunciation (Divvun's speech synthesis) and its "
             "experimental photo search."),
        ],
        fb_h="Feedback is always welcome",
        fb_intro="Bugs, ideas, translation fixes and anything else help the apps along:",
        fb_gievra="Gievra: {mail} or in the app ☰ → <i>Report a problem</i>",
        fb_satni="Sátni FST and Sátnemátki: {mail}",
        fb_github="On GitHub: {link} (bug reports and suggestions for each app)",
        coffee="If the apps are useful to you, you can {link} ☕",
        coffee_link="buy me a coffee",
        mt_note="",
        footer="Sombyduodji · Juha Somby",
        icon_alt=["Gievra logo: a kettlebell", "Sátni FST logo: a drop in the colours of the Sámi flag",
                  "Sátnemátki: an isometric home with a family and Biret"],
    ),
}

# Liput: 27×18 px; saamen lippu omissa mittasuhteissaan (808:600), ettei ympyrä veny.
FLAGS = {
    "fi": '<svg viewBox="0 0 36 24" aria-hidden="true"><rect width="36" height="24" fill="#fff"/>'
    '<rect x="10" width="6" height="24" fill="#002f6c"/><rect y="9" width="36" height="6" fill="#002f6c"/></svg>',
    "nb": '<svg viewBox="0 0 36 24" aria-hidden="true"><rect width="36" height="24" fill="#ba0c2f"/>'
    '<rect x="9" width="7" height="24" fill="#fff"/><rect y="8.5" width="36" height="7" fill="#fff"/>'
    '<rect x="10.75" width="3.5" height="24" fill="#00205b"/><rect y="10.25" width="36" height="3.5" fill="#00205b"/></svg>',
    # Saamen lippu Wikimedia Commonsista (File:Sami_flag.svg, public domain; mitat ja värit Saamelaiskäräjiltä):
    # ympyrän keskipiste vihreän ja keltaisen raidan rajalla, punaisella puolella sininen, sinisellä punainen.
    "se": '<svg class="se" viewBox="0 0 808 600" aria-hidden="true"><path fill="#0035ad" d="M0 0h808v600H0z"/>'
    '<path fill="#ffce00" d="M0 0h370v600H0z"/><path fill="#007229" d="M0 0h314v600H0z"/>'
    '<path fill="#dc241f" d="M0 0h258v600H0z"/>'
    '<path fill="#0035ad" d="M314 108a192 192 0 0 0 0 384l16-16-16-16a160 160 0 0 1 0-320l16-16-16-16z"/>'
    '<path fill="none" stroke="#dc241f" stroke-width="32" d="M314 124a176 176 0 0 1 0 352"/></svg>',
    "en": '<svg viewBox="0 0 60 40" aria-hidden="true"><clipPath id="uk"><path d="M30,20 h30 v20 z v20 h-30 z h-30 v-20 z v-20 h30 z"/></clipPath>'
    '<rect width="60" height="40" fill="#012169"/><path d="M0,0 L60,40 M60,0 L0,40" stroke="#fff" stroke-width="8"/>'
    '<path d="M0,0 L60,40 M60,0 L0,40" clip-path="url(#uk)" stroke="#c8102e" stroke-width="5"/>'
    '<path d="M30,0 v40 M0,20 h60" stroke="#fff" stroke-width="13"/><path d="M30,0 v40 M0,20 h60" stroke="#c8102e" stroke-width="8"/></svg>',
}


def mail(a):
    return f'<a href="mailto:{a}">{a}</a>'


def link(href, text, cls):
    return f'<a class="btn {cls}" href="{href}">{text}</a>'


def app(t, key, icon, alt, status_cls, links):
    feats = "\n".join(f"          <li>{f}</li>" for f in t[key + "_feats"])
    btns = "\n          ".join(link(h, txt, "primary" if i == 0 else "secondary")
                              for i, (h, txt) in enumerate(zip(links, t[key + "_links"])))
    names = {"gievra": "Gievra – Treenipäiväkirja", "satni": "Sátni FST", "mat": "Sátnemátki"}
    return f"""    <article class="app">
      <img class="icon" src="{icon}" alt="{html.escape(alt)}">
      <div>
        <h3>{names[key]}</h3>
        <p class="what">{t[key + '_what']}</p>
        <span class="status {status_cls}">{t[key + '_status']}</span>
        <p>{t[key + '_desc']}</p>
        <ul>
{feats}
        </ul>
        <p class="langs"><b>{t['langs_label']}:</b> {t[key + '_langs']}</p>
        <div class="links">
          {btns}
        </div>
      </div>
    </article>"""


def block(code, t):
    chips = "".join(f"<li>{c}</li>" for c in t["chips"])
    free = "\n".join(f'    <div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["free"])
    mt = f'\n  <p class="mt">{t["mt_note"].format(mail=mail("satni@somby.fi"))}</p>' if t["mt_note"] else ""
    return f"""<main data-lang="{code}" lang="{dict((c, h) for c, _, h in LANGS)[code]}"{'' if code == 'fi' else ' hidden'}>
<header>
  <h1>Sombyduodji</h1>
  <p><span class="bures">Bures!</span> {t['tagline']}</p>
  <p class="lead">{t['lead']}</p>
  <ul class="chips">{chips}</ul>
  <p class="note">{t['note']}</p>{mt}
</header>

<section>
  <h2>{t['apps']}</h2>
  <div class="apps">
{app(t, 'gievra', 'img/gievra.png', t['icon_alt'][0], 'new', [
        'https://sombyduodji.github.io/gievra/' + ('en/' if code == 'en' else ''),
        'https://sombyduodji.github.io/gievra/app/' + ('?lang=en' if code == 'en' else ''), GIEVRA_APK,
        'https://github.com/sombyduodji/gievra',
        'https://sombyduodji.github.io/gievra/' + ('en/' if code == 'en' else '') + '#maphaku'])}
{app(t, 'satni', 'img/satni-fst.svg', t['icon_alt'][1], 'hold', [
        'https://sombyduodji.github.io/satni-fst/', 'https://github.com/sombyduodji/satni-fst/releases/latest',
        'https://github.com/sombyduodji/satni-fst'])}
{app(t, 'mat', 'img/satnematki.png', t['icon_alt'][2], 'demo', [
        'https://sombyduodji.github.io/satnematki/', 'https://github.com/sombyduodji/satnematki'])}
  </div>
</section>

<section>
  <h2>{t['free_h']}</h2>
  <div class="grid">
{free}
  </div>
</section>

<section>
  <h2>{t['fb_h']}</h2>
  <p>{t['fb_intro']}</p>
  <ul>
    <li>{t['fb_gievra'].format(mail=mail('treeni@somby.fi'))}</li>
    <li>{t['fb_satni'].format(mail=mail('satni@somby.fi'))}</li>
    <li>{t['fb_github'].format(link='<a href="https://github.com/sombyduodji">github.com/sombyduodji</a>')}</li>
  </ul>
  <p>{t['coffee'].format(link='<a href="https://buymeacoffee.com/sombyduodji">' + t['coffee_link'] + '</a>')}</p>
</section>
</main>"""


CSS = """
:root{--bg:#f6f4ef;--surface:#fff;--text:#17191d;--muted:#5d636d;--line:#e4e1da;
  --red:#d52b1e;--green:#007229;--yellow:#ffce00;--blue:#0035ad;--dark:#262a30;--link:#b5241a}
@media (prefers-color-scheme:dark){:root{--bg:#121417;--surface:#1c1f24;--text:#eceae5;--muted:#a3a8b0;--line:#2c3037;--link:#ff7a6f}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",sans-serif}
a{color:var(--link)}
[hidden]{display:none!important}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px}
.band{height:8px;background:linear-gradient(90deg,var(--red) 0 25%,var(--green) 25% 50%,var(--yellow) 50% 75%,var(--blue) 75%)}
nav.langs{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;padding:16px 0 0}
nav.langs button{display:flex;align-items:center;gap:8px;font:inherit;font-size:14px;font-weight:600;color:var(--text);
  background:var(--surface);border:2px solid var(--line);border-radius:99px;padding:6px 12px 6px 8px;cursor:pointer}
nav.langs button[aria-pressed="true"]{border-color:var(--red)}
nav.langs svg.se{width:24.24px}
nav.langs svg{width:27px;height:18px;border-radius:3px;box-shadow:0 0 0 1px rgba(0,0,0,.15);flex:none}
header{padding:28px 0 18px;text-align:center}
h1{font-size:clamp(30px,6vw,46px);margin:0 0 6px;letter-spacing:-.5px}
.bures{color:#b07d00;font-weight:700}
@media (prefers-color-scheme:dark){.bures{color:var(--yellow)}}
.lead{font-size:19px;max-width:700px;margin:10px auto 0}
.chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:18px 0 0;padding:0;list-style:none}
.chips li{background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:5px 12px;font-size:14px}
.note{border-left:5px solid var(--yellow);background:var(--surface);border-radius:12px;padding:14px 16px;margin:22px 0 0;text-align:left}
.mt{color:var(--muted);font-size:13px;margin:10px 0 0}
section{padding:24px 0}
h2{font-size:26px;margin:0 0 14px}
.apps{display:grid;gap:18px}
.app{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:20px;display:grid;grid-template-columns:96px 1fr;gap:18px}
@media (max-width:620px){.app{grid-template-columns:1fr}}
.app .icon{width:96px;height:96px;border-radius:22px;object-fit:cover;background:var(--dark)}
.app h3{margin:0;font-size:22px}
.app .what{margin:2px 0 8px;color:var(--muted)}
.status{display:inline-block;font-size:13px;font-weight:700;border-radius:99px;padding:3px 10px;margin:0 0 10px}
.status.new{background:rgba(0,114,41,.14);color:var(--green)}
.status.hold{background:rgba(255,206,0,.22);color:#7a5a00}
.status.demo{background:rgba(0,53,173,.12);color:var(--blue)}
@media (prefers-color-scheme:dark){.status.new{color:#5fd38a}.status.hold{color:var(--yellow)}.status.demo{color:#8fb0ff}}
.app ul{margin:6px 0 10px;padding-left:20px}
.app li{margin:3px 0}
.app .langs{margin:0 0 12px;font-size:15px}
.links{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:10px 16px;border-radius:12px;text-decoration:none;font-weight:700;font-size:15px}
.btn.primary{background:var(--red);color:#fff}
.btn.secondary{border:2px solid var(--line);color:var(--text)}
code{background:var(--line);padding:1px 6px;border-radius:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px}
.card h3{margin:0 0 6px;font-size:18px}
.card p{margin:0}
footer{padding:30px 0 40px;color:var(--muted);text-align:center;font-size:14px}
"""

JS = """
(function () {
  var meta = %s;
  var codes = Object.keys(meta);
  function pick() {
    var q = new URLSearchParams(location.search).get('lang');
    if (q && meta[q]) return q;
    try { var s = localStorage.getItem('lang'); if (s && meta[s]) return s; } catch (e) {}
    var prefs = navigator.languages || [navigator.language || 'fi'];
    for (var i = 0; i < prefs.length; i++) {
      var p = (prefs[i] || '').toLowerCase().split('-')[0];
      if (p === 'fi') return 'fi';
      if (p === 'nb' || p === 'nn' || p === 'no') return 'nb';
      if (p === 'se' || p === 'sme' || p === 'smn' || p === 'sms' || p === 'smj' || p === 'sma') return 'se';
      if (p === 'en') return 'en';
    }
    return 'fi';
  }
  function show(code, save) {
    document.querySelectorAll('main[data-lang]').forEach(function (m) { m.hidden = m.dataset.lang !== code; });
    document.querySelectorAll('nav.langs button').forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.lang === code ? 'true' : 'false');
    });
    document.documentElement.lang = meta[code].lang;
    document.title = meta[code].title;
    var d = document.querySelector('meta[name=description]'); if (d) d.content = meta[code].desc;
    if (save) {
      try { localStorage.setItem('lang', code); } catch (e) {}
      var u = new URL(location.href); u.searchParams.set('lang', code); history.replaceState(null, '', u);
    }
  }
  document.querySelectorAll('nav.langs button').forEach(function (b) {
    b.addEventListener('click', function () { show(b.dataset.lang, true); });
  });
  show(pick(), false);
})();
"""


def main():
    import json
    meta = {c: {"lang": h, "title": T[c]["title"], "desc": T[c]["desc"]} for c, _, h in LANGS}
    nav = "\n".join(
        f'  <button type="button" data-lang="{c}" aria-pressed="{"true" if c == "fi" else "false"}" lang="{h}">'
        f'{FLAGS[c]}<span>{n}</span></button>'
        for c, n, h in LANGS
    )
    page = f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T['fi']['title']}</title>
<meta name="description" content="{html.escape(T['fi']['desc'])}">
<link rel="icon" href="img/satni-fst.svg" type="image/svg+xml">
<!-- Tehty make_page.py:llä: muokkaa tekstejä siellä, älä tässä tiedostossa. -->
<style>{CSS}</style>
</head>
<body>
<div class="band"></div>
<div class="wrap">
<nav class="langs" aria-label="Kieli · Språk · Giella · Language">
{nav}
</nav>
{chr(10).join(block(c, T[c]) for c, _, _ in LANGS)}
</div>
<footer>{T['fi']['footer']} · <a href="https://github.com/sombyduodji">GitHub</a></footer>
<div class="band"></div>
<script>{JS % json.dumps(meta, ensure_ascii=False)}</script>
</body>
</html>
"""
    open("index.html", "w", encoding="utf-8").write(page)
    print("index.html:", len(page), "merkkiä")


if __name__ == "__main__":
    main()
