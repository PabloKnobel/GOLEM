---
type: portal
title: "Contacts and collaborators"
aliases: [network, people, collaborators, contacts]
tags: [portal]
created: 2026-11-18
updated: 2026-11-18
generated: true
reviewed: false
---

**Overview.** Entry point for the people Pablo has worked with: co-authors (from his OpenAlex record), and people he shared a workshop, course, session, conference or mentoring pod with (from lists and programs he feeds in). The master record is the set of tables in `_system/network/`; person pages exist for co-authors, collaborators Pablo names, and anyone who appears in 2 or more contexts.

**Quick lookup.** Ask Claude ("have I worked with X?", "who do I know at Y?", "who did I meet at Z?"), or use Obsidian search, e.g. `path:wiki/entities/people "Columbia"`, or open a person by name with the quick switcher.

## Most frequent collaborators
```dataview
TABLE WITHOUT ID file.link AS Person, affiliation AS Affiliation, n_coauthored AS Papers, n_events AS Events, last_contact AS "Last"
FROM "wiki/entities/people"
SORT (n_coauthored + n_events) DESC, last_contact DESC
LIMIT 30
```

## Recent contacts
```dataview
TABLE WITHOUT ID file.link AS Person, affiliation AS Affiliation, roles AS Roles, last_contact AS "Last"
FROM "wiki/entities/people"
SORT last_contact DESC
LIMIT 20
```

## By expertise
```dataview
TABLE WITHOUT ID expertise AS Expertise, rows.file.link AS People
FROM "wiki/entities/people"
FLATTEN expertise
WHERE expertise
GROUP BY expertise
SORT expertise ASC
```

## Events
```dataview
TABLE WITHOUT ID file.link AS Event, kind AS Kind, date AS Date, location AS Where
FROM "wiki/events"
SORT date DESC
```

<!-- network:auto start -->
## All people with pages (200)
[[fatai-a-adewuyi|Fatai A. Adewuyi]] · [[m-akhtar|M. Akhtar]] · [[valentina-alaasam|Valentina Alaasam]] · [[ana-moreno-alcazar|Ana Moreno‐Alcázar]] · [[itziar-arrieta-aldea|Itziar Arrieta‐Aldea]] · [[melissa-d-aldridge|Melissa D. Aldridge]] · [[xavier-delclos-alio|Xavier Delclòs‐Alió]] · [[lucia-alonso|Lucía Alonso]] · [[benedikt-lorenz-amann|Benedikt Lorenz Amann]] · [[dharesh-raj-amarnath|Dharesh Raj Amarnath]] · [[adeladza-kofi-amegah|Adeladza Kofi Amegah]] · [[heresh-amini|Heresh Amini]] · [[isabelle-anguelovski|Isabelle Anguelovski]] · [[quim-zaldo-aubanell|Quim Zaldo-Aubanell]] · [[ivan-gutierrez-avila|Iván Gutiérrez-Ávila]] · [[andrea-baccarelli|Andrea Baccarelli]] · [[albert-bach|Albert Bach]] · [[xavier-bartoll|Xavier Bartoll]] · [[mariska-bauwelinck|Mariska Bauwelinck]] · [[jordina-belmonte|Jordina Belmonte]] · [[marc-g-berman|Marc G. Berman]] · [[henrik-bggild|Henrik Bøggild]] · [[marti-boada|Martí Boada]] · [[lilian-marie-boll|Lilian Marie Boll]] · [[carme-borrell|Carme Borrell]] · [[matilda-annerstedt-van-den-bosch|Matilda Annerstedt van den Bosch]] · [[gregory-n-bratman|Gregory N. Bratman]] · [[martin-f-breed|Martin F. Breed]] · [[matthew-h-e-m-browning|Matthew H. E. M. Browning]] · [[joana-bucker|Joana Bücker]] · [[thomas-astell-burt|Thomas Astell‐Burt]] · [[ceclia-canepa|Ceclia Canepa]] · [[alejandra-cantoral|Alejandra Cantoral]] · [[xavier-castells|Xavier Castells]] · [[edgar-castro|Edgar Castro]] · [[jane-ellen-clougherty|Jane Ellen Clougherty]] · [[elena-colicino|Elena Colicino]] · [[merce-comas|Mercè Comas]] · [[diana-c-soria-contreras|Diana C. Soria‐Contreras]] · [[luis-costa|Luis Costa]] · [[payam-dadvand|Payam Dadvand]] · [[pilar-diaz|Pilar Díaz]] · [[javier-dopico|Javier Dopico]] · [[angel-mario-dzhambov|Angel Mario Dzhambov]] · [[maria-espanol|Maria Español]] · [[pepus-daunis-i-estadella|Pepus Daunis‐i‐Estadella]] · [[alex-d-federman|Alex D. Federman]] · [[k-m-feeney|K.M. Feeney]] · [[xiaoqi-feng|Xiaoqi Feng]] · [[amanda-paula-fernandes|Amanda Paula Fernandes]] · [[robert-guerri-fernandez|Robert Güerri‐Fernández]] · [[olivia-ferrandez|Olivia Ferrández]] · [[t-elliott-floyd|T. Elliott Floyd]] · [[howard-frumkin|Howard Frumkin]] · [[elaine-fuertes|Elaine Fuertes]] · [[nuria-pujolar-fulquet|Nuria Pujolar Fulquet]] · [[judit-villar-garcia|Judit Villar-García]] · [[kevin-j-gaston|Kevin J. Gaston]] · [[daniela-l-gatto|Daniela L. Gatto]] · [[vincenzo-giannico|Vincenzo Giannico]] · [[cristina-de-cordoba-gil|Cristina De Córdoba Gil]] · [[priyanka-gogna|Priyanka Gogna]] · [[kimiya-gohari|Kimiya Gohari]] · [[alicia-valiente-gomez|Alicia Valiente-Gómez]] · [[cristina-ocallaghan-gordo|Cristina O’Callaghan‐Gordo]] · [[nelson-gouveia|Nélson Gouveia]] · [[santiago-grau|Santiago Grau]] · [[carme-miralles-guasch|Carme Miralles‐Guasch]] · [[ana-guelar|Ana Guelar]] · [[daniel-guinart|Daniel Guinart]] · [[michael-b-hadley|Michael B. Hadley]] · [[terry-hartig|Terry Hartig]] · [[mike-z-he|Mike Z. He]] · [[joachim-heinrich|Joachim Heinrich]] · [[marco-helbich|Marco Helbich]] · [[bridget-hogg|Bridget Hogg]] · [[louisa-w-holaday|Louisa W. Holaday]] · [[kees-de-hoogh|Kees de Hoogh]] · [[juan-pablo-horcajada|Juan Pablo Horcajada]] · [[hsiao-hsien-leon-hsu|Hsiao Hsien Leon Hsu]] · [[hsieh-hsuan|Hsieh Hsuan]] · [[jamie-l-humphrey|Jamie L. Humphrey]] · [[william-hung|William Hung]] · [[inhye-hwang|Inhye Hwang]] · [[soonmyung-a-hwang|Soonmyung A. Hwang]] · [[perry-hystad|Perry Hystad]] · [[rocio-ibanez|Rocio Ibañez]] · [[jesus-maria-ibarluzea|Jesús María Ibarluzea]] · [[aritz-irizar|Aritz Irizar]] · [[benedicte-jacquemin|Bénédicte Jacquemin]] · [[peter-james|Peter James]] · [[mahsa-jashni|Mahsa Jashni]] · [[michael-jerrett|Michael Jerrett]] · [[allan-c-just|Allan C. Just]] · [[peter-h-kahn|Peter H. Kahn]] · [[carmen-de-keijzer|Carmen de Keijzer]] · [[ellen-kinnee|Ellen Kinnee]] · [[itai-kloog|Itai Kloog]] · [[luke-d-knibbs|Luke D. Knibbs]] · [[hernando-knobel|Hernando Knobel]] · [[fred-ko|Fred Ko]] · [[manolis-kogevinas|Manolis Kogevinas]] · [[michelle-c-kondo|Michelle C. Kondo]] · [[georgios-kourounis|Georgios Kourounis]] · [[helena-krasnov|Helena Krasnov]] · [[s-m-labib|S.M. Labib]] · [[kevin-lane|Kevin Lane]] · [[l-l-van-leeuwen|L.L. van Leeuwen]] · [[c-lefebvre|C. Lefebvre]] · [[aitana-lertxundi|Aitana Lertxundi]] · [[rachel-r-litke|Rachel R Litke]] · [[alonso-fernando-lopez|Alonso Fernando Lopez]] · [[ferran-campillo-i-lopez|Ferran Campillo i López]] · [[m-ubalde-lopez|M Ubalde-López]] · [[walter-lupo|Walter Lupo]] · [[tszshan-ma|Tszshan Ma]] · [[cristina-macias|Cristina Macias]] · [[jay-e-maddock|Jay E. Maddock]] · [[rohollah-fallah-madvari|Rohollah Fallah Madvari]] · [[roser-maneja|Roser Maneja]] · [[augustin-marcos|Augustin Marcos]] · [[diana-marin|Diana Marin]] · [[iana-markevych|Iana Markevych]] · [[oriol-marquet|Oriol Marquet]] · [[margarita-triguero-mas|Margarita Triguero Mas]] · [[olivia-mcanirlin|Olivia McAnirlin]] · [[mary-ann-mclaughlin|Mary Ann McLaughlin]] · [[marta-fontana-mcnally|Marta Fontana-McNally]] · [[amir-houshang-mehrparvar|Amir Houshang Mehrparvar]] · [[alicia-gonzalez-mena|Alicia González‐Mena]] · [[vishal-midya|Vishal Midya]] · [[mohammad-miri|Mohammad Miri]] · [[richard-mitchell|Richard Mitchell]] · [[charles-v-mobbs|Charles V. Mobbs]] · [[m-montero|M. Montero]] · [[r-sean-morrison|R. Sean Morrison]] · [[kiran-p-nagdeo|Kiran P. Nagdeo]] · [[tim-s-nawrot|Tim S. Nawrot]] · [[mark-j-nieuwenhuijsen|Mark J Nieuwenhuijsen]] · [[marta-beatriz-fernandez-nunez|Marta-Beatriz Fernández Núñez]] · [[francesco-oliva|Francesco Oliva]] · [[marcela-tamayo-ortiz|Marcela Tamayo‐Ortiz]] · [[frank-padberg|Frank Padberg]] · [[krupa-ambalal-patel|Krupa Ambalal Patel]] · [[lokesh-patil|Lokesh Patil]] · [[jamie-r-pearce|Jamie R Pearce]] · [[michelle-plusquin|Michelle Plusquin]] · [[achilleas-psyllidis|Achilleas Psyllidis]] · [[minhan-qiu|Minhan Qiu]] · [[g-w-randall|G.W. Randall]] · [[martha-maria-tellez-rojo|Martha María Téllez‐Rojo]] · [[marta-roman|Marta Román]] · [[claudio-damiao-rosa|Claudio Damião Rosa]] · [[oscar-royuela|Oscar Royuela]] · [[esperanza-canas-ruano|Esperanza Cañas‐Ruano]] · [[kshitij-sachdev|Kshitij Sachdev]] · [[maayan-yitshak-sade|Maayan Yitshak‐Sade]] · [[mohammad-javad-zare-sakhvidi|Mohammad Javad Zare Sakhvidi]] · [[maria-sala|María Sala]] · [[karl-samuelsson|Karl Samuelsson]] · [[giovanni-sanesi|Giovanni Sanesi]] · [[leah-h-schinasi|Leah H. Schinasi]] · [[jasper-schipperijn|Jasper Schipperijn]] · [[joel-david-schwartz|Joel David Schwartz]] · [[consol-serra|Cònsol Serra]] · [[isabel-serra|Isabel Serra]] · [[perry-elizabeth-sheffield|Perry Elizabeth Sheffield]] · [[ali-sheidaei|Ali Sheidaei]] · [[liuhua-shi|Liuhua Shi]] · [[aditi-singhvi|Aditi Singhvi]] · [[masashi-soga|Masashi Soga]] · [[giuseppina-spano|Giuseppina Spano]] · [[s-sparrow|S. Sparrow]] · [[kyle-steenland|Kyle Steenland]] · [[jason-g-su|Jason G. Su]] · [[william-sullivan|William Sullivan]] · [[lia-campos-suzman|Lia Campos Suzman]] · [[viren-swami|Viren Swami]] · [[susan-l-teitelbaum|Susan L. Teitelbaum]] · [[hannah-thompson|Hannah Thompson]] · [[samuel-tingle|Samuel Tingle]] · [[agusti-albalat-torres|Agustí Albalat-Torres]] · [[antonia-valentin|Antònia Valentín]] · [[guillem-vich|Guillem Vich]] · [[rocio-villar|Rocío Villar]] · [[sjerp-de-vries|Sjerp de Vries]] · [[d-c-wallom|D.C. Wallom]] · [[mathew-p-white|Mathew P. White]] · [[c-wilson|C Wilson]] · [[johannes-wolf|Johannes Wolf]] · [[robert-o-wright|Robert O. Wright]] · [[jeanne-wu|Jeanne Wu]] · [[bo-yi-yang|Bo‐Yi Yang]] · [[jun-yang|Jun Yang]] · [[ray-a-yeager|Ray A. Yeager]] · [[maria-luisa-pizano-zarate|María Luisa Pizano-Zárate]] · [[jinguang-zhang|Jinguang Zhang]] · [[tianyu-zhao|Tianyu Zhao]] · [[yuzhe-zhao|Yuzhe Zhao]] · [[wilma-l-zijlema|Wilma L. Zijlema]]

## All events (2)
- [[ihen-exposome-training-school-2025]]
- [[ihen-exposome-training-school-2026]]

_Tables: 257 people, 2 events, 41 works, 409 links, 1 names held for review._
<!-- network:auto end -->

## See also
- [[Home]]
