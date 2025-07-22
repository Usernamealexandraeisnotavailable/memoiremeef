import csv
import modules.inferences
import scipy
import math

print("\x1b[1;37;40mFichiers étudiés\x1b[0m")
print(modules.inferences.fichiers)

print("\x1b[3;37;40m-=-=-=-\x1b[0m")

prevalences_inferences = modules.inferences.calculer_prevalences_inferences()

print("\x1b[3;37;40m-=-=-=-\x1b[0m")

ecarts_types = modules.inferences.calculer_ecarts_types_prevalences_entre_modeles (
    prevalences_inferences
)

print(
    "Inférence ;",
    "Écart-type ;",
    "Statistique ;",
    "Valeur p"
)
for inference_et_ecart_type in ecarts_types :
    statistique = inference_et_ecart_type[1]*math.sqrt(len(modules.inferences.fichiers)-1)/0.12
    valeur_p = scipy.stats.chi.cdf(statistique, len(modules.inferences.fichiers)-1)
    if valeur_p > .5 :
        valeur_p = 1-valeur_p
    print(
        inference_et_ecart_type[0],
        ";",
        f"{round(inference_et_ecart_type[1],2)}".replace('.',','),
        ";",
        f"{round(statistique,2)}".replace('.',','),
        ";",
        f"{round(valeur_p*(10**-int(math.log(valeur_p,10))),2)}E{round(int(math.log(valeur_p,10)))}".replace('.',',')
    )