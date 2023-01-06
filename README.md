# geirHostOppgave

RAPPORT OPPGAVE HØST

1. Formål, bruksområde og ansvarlige


1.1 Hva systemet skal brukes til.

Systemet er brukt til å spille et spill som ligner "Flappy Bird"

1.2 Hvordan det fungerer.

Systemet fungerer med å ta imot input fra spiller som forandrer posisjon på spillfiguren, samtidig som spillfiguren må unngå hindringer som blir tegnet til spillet med tilfeldig høyde

1.3	Hvilke andre systemer løsningen jobber med. Inndata og utdata 

Programmet jobber med python og mysql
 


 
2. Rammer 


2.1	Hvilke lover og forskrifter løsningen skal forholde seg til. 

Systemet lagrer ikke personlig informasjon og trenger derfor ikke å forholde seg til lover



 
3. Systembeskrivelse 


3.1	Versjon.

Commit: 4a6a8ec

3.2	En beskrivelse av grensesnitt mot andre IT-systemer, manuelle eller maskinelle, som angir type, format og på import- og eksportdata. 

systemet sender ut en string verdi og en int verdi til databasen

3.3	En beskrivelse av IT-systemets oppbygging med programmer, registre, tabeller, database, inndata og utdata, metadata, samt avhengigheter og dataflyt mellom disse. Dersom det er en database, bør både den fysiske og logiske strukturen beskrives. 

Python-programmet sender informasjon om spillerens poengsum ved hjelp av en int og en string verdi, databasen får denne informasjon inn i en tabell som inneholder 3 kolonner: id, player, score

3.4	En beskrivelse av IT-systemets funksjoner med angivelse av hensikt/bruksområde, inndata, behandlingsregler, innebygd ”arbeidsflyt”, feilmeldinger og utdata. Beskrivelsen omfatter også oppdatering av registre/tabeller. 

Informasjon blir lagret til databasen og den blir oppdatert dersom poengsummen til spiller er over 0

3.5	Programmeringsspråk og versjon. 

Python 3.11
MySQL 8.0.31


 
 
4. Kontroller i og rundt IT-systemet 


4.1	Enkel risikovurdering av IT-systemets konfidensialitet, integritet og tilgjengelighet.

Systemet lagrer ikke personlig informasjon om spiller




 
5. Driftsmessige krav og ressurser. 


5.1	Maskinvare. 

Minumum krav: Raspberry Pi 1.

 

6. Systembenyttede standarder 


6.1	Verktøystandarder 

Python 3.11

6.4	Brukergrensesnitt. (En beskrivelse av regler for oppbygging av skjermbilde og meny, hva en kommando utfører, standard betydning av tastene på tastaturet, fellestrekk ved dialogene etc.) 

bruker tar i bruk en pygame UI, knapper som kan bli brukt er ESC, ENTER, KEYUP, SPACE og MOUSEBUTTONDOWN

6.5	Navnestandarder variabler.

Variabler er beskrivende og er skrevet i ett ord uten understrek

6.7	Avvik, begrunnelse for avvik fra gjeldende standard(er). 

Variabler for velocity av spillfigur inneholder understrek, dersom navnet ble langt og ulesbart.
 

 
 
7. Programdokumentasjon 


8.1	Det er viktig med flittig bruk av kommentarer i programkoden for å gjøre denne lettere å forstå. Et minimum er å forklare programmets funksjon, variabler, behandlingsregler og avhengighet av/ påvirkning på andre programmer. 



 
8. Kjente feil og mangler 

9.1	Oversikt over FAQ og kjente feil og mangler med beskrivelse av mulige løsninger – primært for brukere/brukerstøttefunksjon og driftspersonell.
For å hente navn av spiller brukte jeg først en input funksjon, men dette fikk pygame til å fryse opp. 
Jeg fant en erstatning for det, som var TKinter. TKinter sendte ut en dialogboks istedenfor, som fikk pygame til å fortsette å kjøre


ER Diagram

https://cdn.discordapp.com/attachments/800718989805748226/1060252366630301818/image.png


Forklaring av SQL kobling

1. last ned mysql og mysql connector for python
2. lag en table i databasen som skal har verdiene du vil lagre fra spillet
3. importer mysql.connector i python
4. lag en connection med databasen din ved hjelp av mysql.connector.connect funskjonen (spesifiser host, user, passord og database). lagre dette i en variabel
5. bruk cursor funksjonen til å navigere rundt databasen
