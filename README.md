# Arbeidskrav_1_py1010
Her vil jeg legge inn arbeidskrav i py1010

Arbeidskrav 1: oppgaven er : Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.

Lag et Python-program som beregner og presenterer (viser) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

#Arbeidskrav_2_py1010 

Arbeidskrav 2 PY1010
Oppg 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst.

Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....

Oppg 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.
b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London
c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm.

Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.

Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥
2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10].
