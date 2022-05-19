# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:05:26 2022

@author: 
"""

# Laster inn de bibliotekene jeg trenger

# Laster inn alt fra pylab. Da kan jeg gjøre matteting og jeg kan plotte grafer
from pylab import *
# Laster inn pandas som er et bibiotek som er fint å bruke til å lese inn data
# Må skrive pd. foran alt jeg bruker herfra
import pandas as pd 

# Bruker pandas-funksjonen read_csv til å lese inn fila klimagasser.csv
# delimiter = ';' forteller at det er semicolon som separerer kolonner, 
# skiprows = 2 for å hoppe over de to første radene (overskrift)
utslipp = pd.read_csv(r'C:\Users\katie\OneDrive\Dokumenter\GitHub\School\Matte\lesing av filer\klimagasser.csv', delimiter = ';', skiprows = 2)

# Ser hva som er i de forksjellige kollonene ved å skrive ut "nøklene" 
# (overskriften til hver kolonne). Når jeg jobber med pandas kan jeg bruke
# disse som referanse til hele kolonnen med data
print(utslipp.keys())

# Lagrer kolonnen med årstall som en liste 
aar = utslipp['aar'].tolist()

# Gjør tilsvarende for alle utslippskilder
alle_kilder = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 0 Alle kilder'].tolist()

olje_gass = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 1 Olje- og gassutvinning'].tolist()
industri_bergverk = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 2 Industri og bergverk'].tolist()
energiforsyning = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 3 Energiforsyning'].tolist()
oppvarming = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 4 Oppvarming i andre naeringer og husholdninger'].tolist()
veitrafikk = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 5 Veitrafikk'].tolist()
luftfart_sjofart_fiske = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 6 Luftfart, sjofart, fiske, motorredskaper m.m.'].tolist()
jordbruk = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 7 Jordbruk'].tolist()
andre_kilder = utslipp['Utslipp til luft (1 000 tonn CO2-ekvivalenter) 9 Andre kilder'].tolist()


'''
    Lager funksjoner som vi kan få bruk for til å analysere data
'''

# Derivasjon. Numerisk derivasjon av diskrete data.
def derivert(y, x):
# Funksjon som tar inn en liste med x-verdier og en liste med y-verdier 
# (begge reelle data). 
# Returnerer den numerisk deriverte av y med hensyn på x, samt en oppdatert 
# x-liste som korresponderer

    # Setter n lik lengden til x
    n = len(x)
    # Lager en tom liste hvor vi vil lagre den deriverte for hver x-verdi
    y_derivert = []
    # x-lista som vi returnerer (fjerner første element) 
    x_ut = x[1:n ]
    # Går gjennom alle korresponderende x- og y-verdier
    for i in range(0, n - 1):
        # Endring i y
        dy = y[i + 1] - y[i]
        # Endring i x
        dx = x[i + 1] - x[i]
        # Den numerisk deriverte.
        y_derivert.append(dy / dx)
    return(y_derivert, x_ut)


# Undersøker det totale utslippet fra alle kilder:

# Plotter totalt utslipp mot år
plot(aar, alle_kilder)
# Lager tittel
title('Utslipp av klimagasser i Norge mellom 1990 og 2020')
# Navn på x-aksen
xlabel('År')
# Navn på y-aksen
ylabel(r'1 000 tonn $CO_2$-ekvivalenter')
# Viser plottet
show()

# Justerer aksene og plotter på nytt
# Plotter totalt utslipp mot år
plot(aar, alle_kilder)
# Lager tittel
title('Utslipp av klimagasser i Norge mellom 1990 og 2020')
# Justerer akser
ylim([0,58000]); xlim([1989, 2031])
# Navn på x-aksen
xlabel('År')
# Navn på y-aksen
ylabel(r'1 000 tonn $CO_2$-ekvivalenter')
# Viser plottet
show()

# Videre underøker vi veksten/nedgangen til de totale utslippene

# Regner ut gjennomnittlig vekstfart siste 30 år:
gj_vekst_30_tot = (alle_kilder[-1] - alle_kilder[0]) / (aar[-1] - aar[0])
print('Gjennomsnittlig vekstfart for utslipp av klimagasser mellom 1990 og 2020:\n', gj_vekst_30_tot, r' tusen tonn $CO_2$-ekvivalenter per år')

# Regner ut gjennomnittlig vekstfart siste 30 år:
gj_vekst_10_tot = (alle_kilder[-1] - alle_kilder[19]) / (aar[-1] - aar[19])
print('Gjennomsnittlig vekstfart for  utslipp av klimagasser mellom 2010 og 2020:\n', gj_vekst_10_tot, r' tusen tonn $CO_2$-ekvivalenter per år')

# Regner ut gjennomnittlig vekstfart siste 30 år:
gj_vekst_5_tot = (alle_kilder[-1] - alle_kilder[24]) / (aar[-1] - aar[24])
print('Gjennomsnittlig vekstfart for  utslipp av klimagasser mellom 2015 og 2020:\n', gj_vekst_5_tot, r' tusen tonn $CO_2$-ekvivalenter per år')

# Vil derivere for å undersøke trenden til veksten
# Bruker funskjonen for numerisk derivasjon av dirkrete data som jeg definerte
# tidligere
alle_kilder_vekst, aar_vekst = derivert(alle_kilder, aar)

plot(aar_vekst, alle_kilder_vekst)
title('Vekst/nedgang i utslipp av klimagasser\n i Norge mellom 1990 og 2020')
xlabel('År')
ylabel(r'1 000 tonn $CO_2$-ekvivalenter per år')
show()

# Nå vil vi se på hvordan utslippene må endre seg for å nå målet fra 
# Parisavtalen. 
# Vil gjøre prediskjoner basert på gjennomsnittlig vekst 
# Siste 30, 10, 5 og 2 år (antar lineære sammenhenger)

# Lager en liten liste med årene 2020 og 2030
aar_pred = [2020, 2030]
# Prediksjon dersom veksten blir lik veksten siste 30 år 
# alle_kilder[-1] betyr at vi henter ut den siste verdien i listen
# Det siste elementet er den rette linja fra den siste verdien i alle_kilder, 
# som har stigningstall likt veksten de siste 30 år
# Ganger veksten med 10 slik at linja stopper ved 2030
pred_1 = [alle_kilder[-1], alle_kilder[-1] + gj_vekst_30_tot * 10]
# Prediksjon dersom veksten blir lik veksten siste 10 år 
pred_2 = [alle_kilder[-1], alle_kilder[-1] + gj_vekst_10_tot * 10]
# Prediksjon dersom veksten blir lik veksten siste 5 år 
pred_3 = [alle_kilder[-1], alle_kilder[-1] + gj_vekst_5_tot * 10]
# Prediksjon dersom veksten blir lik veksten siste 2 år 
pred_4 = [alle_kilder[-1], alle_kilder[-1] + alle_kilder_vekst[-1] * 10]

# Lager en liste med alle år mellom 1990 til 2039
aar_utvidet = range(1990, 2031)

# Deler utslippstallet fra 2020 (alle_kilder[-1]) på 2,
# og ganger med en liste med enere.
# ones(n) Lager en liste med n enere: [1, 1, ..., 1]
# Dermed vi f.eks. 3 * ones(n) gi en listee med n treere: [3, 3, ..., 3]
forpliktelse = alle_kilder[-1]/2 * ones(len(aar_utvidet))

# Plotter totalutslippet sammen med alle prdiksjonslinjer og Parisavtalemålet 
plot(aar, alle_kilder)
plot(aar_pred, pred_1, label = 'Samme vekst som siste 30 år')
plot(aar_pred, pred_2, label = 'Samme vekst som siste 10 år')
plot(aar_pred, pred_3, label = 'Samme vekst som siste 5 år')
plot(aar_pred, pred_4, label = 'Samme vekst som siste år')
plot(aar_utvidet, forpliktelse, linestyle = '--', label = 'Parisavtale-forpliktelse')
ylim([0,58000]); xlim([1989, 2031])
title('Utslipp av klimagasser i Norge mellom 1990 og 2020 med prediksjoner')
xlabel('År')
ylabel(r'1 000 tonn $CO_2$-ekvivalenter')
legend()
show()

# Ser videre på utslippet fra alle de forskjellige kildene:

# Plotter de forksjllige utslippene mot år
plot(aar, olje_gass, label = 'Olje og gass')
plot(aar, industri_bergverk, label = 'Industri og bergverk')
plot(aar, energiforsyning, label = 'Energiforsyning')
plot(aar, oppvarming, label = 'Oppvarming i andre naeringer og husholdninger')
plot(aar, veitrafikk, label = 'Veitrafikk')
plot(aar, luftfart_sjofart_fiske, label = 'Luftfart, sjøfart og fiske')
plot(aar, jordbruk, label = 'Jordbruk')
plot(aar, andre_kilder, label = 'Andre kilder')
title('Utslipp av klimagasser i Norge mellom 1990 og 2020 \n fordelt på utslippskilder')
xlabel('År')
ylabel(r'1 000 tonn $CO_2$-ekvivalenter')
legend(bbox_to_anchor = (1, 1))
show()




# Nå vil vi undersøke og analysere utslippene fra olje og gass spesielt
plot(aar, olje_gass)
title('Utslipp av klimagasser fra olje- og gassnæringen \n i Norge mellom 1990 og 2020')
xlabel('År')
ylabel(r'1 000 tonn $CO_2$-ekvivalenter')
show()

# Videre underøker vi veksten/nedgangen til utslippene fra olje og gass

# Regner ut gjennomnittlig vekstfart siste 30 år:
gj_vekst_30 = (olje_gass[-1] - olje_gass[0]) / (aar[-1] - aar[0])
print('Gjennomsnittlig vekstfart for  utslipp av klimagasser fra olje- og gassnæringen mellom 1990 og 2020:\n', gj_vekst_30, r' tusen tonn $CO_2$-ekvivalenter per år')

# Regner ut gjennomnittlig vekstfart siste 30 år:
gj_vekst_10 = (olje_gass[-1] - olje_gass[19]) / (aar[-1] - aar[19])
print('Gjennomsnittlig vekstfart for  utslipp av klimagasser fra olje- og gassnæringen mellom 2010 og 2020:\n', gj_vekst_10, r' tusen tonn $CO_2$-ekvivalenter per år')

# Regner ut gjennomnittlig vekstfart siste 30 år:
gj_vekst_5 = (olje_gass[-1] - olje_gass[24]) / (aar[-1] - aar[24])
print('Gjennomsnittlig vekstfart for  utslipp av klimagasser fra olje- og gassnæringen mellom 2015 og 2020:\n', gj_vekst_5, r' tusen tonn $CO_2$-ekvivalenter per år')

# Vil derivere dataene for å undersøke hvordan veksten/nedgangen har utviklet seg fra år til år
olje_gass_vekst, aar_vekst = derivert(olje_gass, aar)
plot(aar_vekst, olje_gass_vekst)
title('Vekst/nedgang i utslipp av klimagasser fra olje- og gassnæringen \n i Norge mellom 1990 og 2020')
xlabel('År')
ylabel(r'1 000 tonn $CO_2$-ekvivalenter per år')
show()


