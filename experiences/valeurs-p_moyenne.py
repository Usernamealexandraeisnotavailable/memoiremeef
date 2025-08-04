import modules.inferences
import statistics
import scipy
import math

print("\x1b[1;37;40mFichiers étudiés\x1b[0m")
print(modules.inferences.fichiers)

print("\x1b[3;37;40m-=-=-=-\x1b[0m")

prevalences = modules.inferences.calculer_prevalences_inferences()

print("\x1b[3;37;40m-=-=-=-\x1b[0m")

modeles = []
for modele_prev in prevalences[0][1] :
        modeles.append([modele_prev[0],[]])
for inference in prevalences :
        for indice_modele, modele_prev in enumerate(inference[1]) :
                modeles[indice_modele][1].append(modele_prev[1])
print(" ; ".join([
    "Modèle",
    "Moyenne empirique",
    "Écart-type empirique",
    "Statistique z",
    "Valeur p"
]))
for modele in modeles :
        moyenne = statistics.mean(modele[1])/100
        devst = statistics.stdev(modele[1])/100
        statistique_z = 8*moyenne-4
        valeur_p = 2*scipy.stats.norm.cdf(-abs(statistique_z))
        if valeur_p != 0 :
                print(" ; ".join([
                    f"{modele[0]}".replace('.',','),
                    f"{round(moyenne,2)}".replace('.',','),
                    f"{round(devst,2)}".replace('.',','),
                    f"{round(statistique_z,2)}".replace('.',','),
                    f"{round(valeur_p*(10**-int(math.log(valeur_p,10)-1)),2)}E{round(int(math.log(valeur_p,10)-1))}".replace('.',',')
                ]))
        else :
                print(" ; ".join([
                    f"{modele[0]}".replace('.',','),
                    f"{round(moyenne,2)}".replace('.',','),
                    f"{round(devst,2)}".replace('.',','),
                    f"{round(statistique_z,2)}".replace('.',','),
                    f"{0.0} ; (trop petite pour les virgules flottantes)".replace('.',',')
                ]))
