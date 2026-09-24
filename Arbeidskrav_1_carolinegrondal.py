"""


Arbeidskrav 1 innlevering. Oppgave: Lag et Python-program som 
beregner og presenterer (viser) de årlige totalkostnadene for elbil og 
for bensinbil samt årlig kostnadsdifferanse basert på informasjonen 
gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader 
som renter på billån og verditap (du har da egentlig antatt at slike kostnadene 
er like for elbil og bensinbil).

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. 
(hvis du ikke har bil) kan du anta 10.000 km.

Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.

Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.

Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. 
Bensinbil: 1,0 kr/km.

Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

Caroline Grondal (cagro1245@usn.no)

"""

   # Antall km kjørt per år
km_per_aar = 10000

   # Forsikring
forsikring_elbil = 5000
forsikring_bensinbil = 7500

   # Trafikkforsikringsavgift
trafikkavgift_per_dag = 8.38
trafikkavgift = trafikkavgift_per_dag * 365

   # Elbil
stromforbruk_elbil = 0.2
strompris = 2.00
bomavgift_elbil = 0.1
stromkostnad = km_per_aar * stromforbruk_elbil * strompris
bomkostnad_elbil = km_per_aar * bomavgift_elbil

totalkostnad_elbil = forsikring_elbil + trafikkavgift + stromkostnad + bomkostnad_elbil

   # Bensinbil
drivstoffkostnad_bensinbil = 1.0
bomavgift_bensinbil =0.3
drivstoffkostnad = km_per_aar * drivstoffkostnad_bensinbil
bomkostnad_bensinbil = km_per_aar * bomavgift_bensinbil

totalkostnad_bensinbil = forsikring_bensinbil + trafikkavgift + drivstoffkostnad + bomkostnad_bensinbil

   # Kostnadsdifferanse
kostnadsdifferanse = totalkostnad_bensinbil - totalkostnad_elbil

   # Resultat
print("Årlig kostnader:")
print("Bensinbil:", totalkostnad_bensinbil, "kr")
print("Elbil:", totalkostnad_elbil, "kr")
print("kostnadsforskjell:", kostnadsdifferanse, "kr")








