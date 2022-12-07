# geirHostOppgave

RAPPORT OPPGAVE HØST

1. Formål, bruksområde og ansvarlige

1.1 Hva systemet skal brukes til.
Systemet er brukt til å spille et spill som ligner "Flappy Bird"

1.2 Hvordan det fungerer.
Systemet fungerer med å ta imot input fra spiller som forandrer posisjon på spillfiguren, samtidig som spillfiguren må unngå hindringer som blir tegnet til spillet med tilfeldig høyde

1.3 Hvem som er ansvarlig for å oppdatere systemdokumentasjon
meg

1.4	Hvem som er Systemansvarlig. 
meg

1.5	Hvem som er Systemeier. 
meg

1.6	Hvem som er ansvarlig for drift og vedlikehold av systemet. 
meg

1.7	Hvem som skal bruke systemet. 
meg

1.8	Hvilke andre systemer løsningen jobber med. Inndata og utdata 
Programmet jobber med python og mysql
 


 
2.	Rammer 
2.1	Hvilke lover og forskrifter løsningen skal forholde seg til. 
Systemet lagrer ikke personlig informasjon og trenger derfor ikke å forholde seg til lover



 
3.	Systembeskrivelse 
3.1	Versjon.
Commit: f5df54cf20eb7f4e003cba48ec41ee385afa6173

3.2	En beskrivelse av grensesnitt mot andre IT-systemer, manuelle eller maskinelle, som angir type, format og på import- og eksportdata. 
systemet sender ut en string verdi og en int verdi til databasen

3.3	En beskrivelse av IT-systemets oppbygging med programmer, registre, tabeller, database, inndata og utdata, metadata, samt avhengigheter og dataflyt mellom disse. Dersom det er en database, bør både den fysiske og logiske strukturen beskrives. 
Python-programmet sender informasjon om spillerens poengsum ved hjelp av en int og en string verdi, databasen får denne informasjon inn i en tabell som inneholder 3 kolonner: id, player, score

3.4	En beskrivelse av IT-systemets funksjoner med angivelse av hensikt/bruksområde, inndata, behandlingsregler, innebygd ”arbeidsflyt”, feilmeldinger og utdata. Beskrivelsen omfatter også oppdatering av registre/tabeller. 
Informasjon blir lagret til databasen og den blir oppdatert dersom poengsummen til spiller er over 0

3.5	Programmeringsspråk og versjon. 
Python 3.11



 
 
4.	Kontroller i og rundt IT-systemet 
4.1	Enkel risikovurdering av IT-systemets konfidensialitet, integritet og tilgjengelighet.
Systemet lagrer ikke personlig informasjon om spiller




 
 
5.	Driftsmessige krav og ressurser. 
5.1	Maskinvare. 
Minumum krav: Raspberry Pi 1.

 
 
6.	Systembenyttede standarder 
6.1	Verktøystandarder (en beskrivelse av regler for hvilke og hvordan verktøy skal brukes når løsning lages) 

6.2	Spesifikasjonsstandarder. (En beskrivelse av regler for hvordan funksjoner, programmer, data og dokumenter skal beskrives.) 

6.3	Programmeringsstandarder. (En beskrivelse av regler for hvordan programmeringen skal utføres.) 

6.4	Brukergrensesnitt. (En beskrivelse av regler for oppbygging av skjermbilde og meny, hva en kommando utfører, standard betydning av tastene på tastaturet, fellestrekk ved dialogene etc.) 

6.5	Navnestandarder variabler. (En beskrivelse av hvordan navn er bygget opp. Dette er standarder som skal sikre at navn er entydige og at alle forekomster bare har ett navn. I tillegg er det regler for generering av navn, som skal sikre at navn er logiske.) 

6.7	Avvik, begrunnelse for avvik fra gjeldende standard(er). 

 
 
7.	Systemforvaltning (vedlikehold og videreutvikling) 
7.1	Rutiner for systemforvaltning. 

7.2	Rutiner for konfigurasjonsstyring av kode. 

7.3	Rutiner for melding, registrering og oppfølging av endringsforslag. 

7.4	Rutiner for konsekvensvurdering og prioritering av endringsforslag og bestilling av endringer. 

7.5	Plan og miljø for testing, testgruppesammensetting, testdata og forventede testresultater. 

7.6	Rutine for godkjenning og driftssetting av endringer og oppdatering av system-, bruker- og driftsdokumentasjon. 

7.7	Rutine for informering av berørte om implementerte endringer. 

7.8	Bibliotekrutiner. 

 
 
8.	Programdokumentasjon 
8.1	Det er viktig med flittig bruk av kommentarer i programkoden for å gjøre denne lettere å forstå. Et minimum er å forklare programmets funksjon, variabler, behandlingsregler og avhengighet av/ påvirkning på andre programmer. 

8.2	Hvem som har programmert (både opprinnelig og eventuelle endringer), dato og versjon. 
meg


 
 
9.	Kjente feil og mangler 
9.1	Oversikt over FAQ og kjente feil og mangler med beskrivelse av mulige løsninger – primært for brukere/brukerstøttefunksjon og driftspersonell.

 


