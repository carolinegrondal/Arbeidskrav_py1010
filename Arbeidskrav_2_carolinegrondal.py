"""
Arbeidskrav 2. jeg legger inn alle oppgavene nedover med løsning på oppgavene, 

Caroline Grondal (cagro1245@usn.no)

"""

"""
Oppgave 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst.
"""


   # Svar Oppgave 1) 

alder = int(input("Hvilket år er du født?"))

alder_i_2024 = 2024 - alder
print("I løpet av 2024 blir du", alder_i_2024, "år gammel.")


""" 

Oppgave 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza.
Lag et program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:'))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og
skrive svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken
(man må da kjøpe 5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: 'Det må handles inn 6.0 pizzaer til festen'.
Hvordan kan sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?
""" 

   # Svar oppgave 2)
import numpy as np

antall_elever = int(input("Skriv inn antall elever:"))

   # fant np.ceil med hjelp av KI som runder opp til nærmeste heltall. 
   
antall_pizzaer = int(np.ceil(antall_elever /4))
print ("Det må handles inn", antall_pizzaer, "pizzaer til festen.")

"""
Oppgave 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:'))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....
"""

   # Svar Oppgave 3)
   
import numpy as np

v_grad = float(input("Skriv inn gradtallet:"))
def grader_til_radianer (grader): 
 radianer = grader *np.pi / 180
 return radianer

v_rad = grader_til_radianer (v_grad)
print(v_grad, "grader er", v_rad, "radianer.")

""" 
Oppgave 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.
b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London
c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm.
"""

   #Svar Oppgave 4a)

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

    #Svar oppgave 4b)
land = input("Skriv inn et land: ")
hovedstad = data[land][0]
innbyggere = data[land][1]

print(hovedstad, "er hovedstaden i", land, "og det er", innbyggere, "mill. innbyggere i", hovedstad)


   #Svar Oppgave 4c)

nytt_land = input("Skriv inn et nytt land: ")
ny_hovedstad = input("Skriv inn hovedstaden: ")
nye_innbyggere = float(input("Skriv inn antall innbyggere i hovedstaden (mill. ): "))

data[nytt_land] = [ny_hovedstad, nye_innbyggere]
print(data)

"""
Oppgave 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant
og en halvsirkel, se figuren. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med
passende tekst.
"""

   # Svar oppgave 5)
   # # Fikk hjelp av KI til å sette opp formlene
   
def areal_og_omkrets(a, b):
    r = a / 2 
    areal = a * b / 2 + np.pi * r**2 /2   #trekant + halvsirkel
    omkrets = np.pi * r + b + np.sqrt(a**2 + b**2) # halvsirkelbue + b + hypotenus
    return areal, omkrets

a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))

areal, omkrets = areal_og_omkrets(a, b)
print("Arealet er", areal)
print("Den ytre omkrets er", omkrets)

""" 
Oppgave 6) Skriv en kode som plotter funksjonen f(x) = -x^2 - 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet [-10,10].
"""
    # Svar oppgave 6)
    
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 - 5 

plt.plot (x, y)
plt.title("f(x) = -x**2 - 5")
plt.xlabel ("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()




    