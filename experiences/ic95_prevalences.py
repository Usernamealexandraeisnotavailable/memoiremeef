import modules.inferences

prevalences = modules.inferences.calculer_prevalences_inferences()

from statistics import mean
from math import sqrt

print("\x1b[3;37;40m-=-=-=-\x1b[0m")

print('Inférence ; Moyenne ; CI- ; CI+')
for liste_inference in prevalences :
    moyenne = mean([
        liste_inference[1][_][1]
        for _ in range(len(liste_inference[1]))
    ])
    intervalle_de_confiance__plus_ou_moins = 196*sqrt((.01*moyenne)*(1-.01*moyenne)/len(prevalences[0][1]))
    print(
        liste_inference[0],
        ';',
        f"{round(moyenne,2)}".replace('.',','),
        ';',
        f"{round(moyenne-intervalle_de_confiance__plus_ou_moins,2)}".replace('.',','),
        ';',
        f"{round(moyenne+intervalle_de_confiance__plus_ou_moins,2)}".replace('.',',')
    )