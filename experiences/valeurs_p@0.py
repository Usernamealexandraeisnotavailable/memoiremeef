import csv
import modules.inferences

print("\x1b[1;37;40mFichiers étudiés\x1b[0m")
print(modules.inferences.fichiers)

print("\x1b[3;37;40m-=-=-=-\x1b[0m")

prevalences_inferences = modules.inferences.calculer_prevalences_inferences()

print("\x1b[3;37;40m-=-=-=-\x1b[0m")
moyennes = modules.inferences.calculer_moyennes_prevalences_entre_modeles (
    prevalences_inferences
)
medianes = modules.inferences.calculer_medianes_prevalences_entre_modeles (
    prevalences_inferences
)
ecarts_types = modules.inferences.calculer_ecarts_types_prevalences_entre_modeles (
    prevalences_inferences
)
print(
    "Inférence ;",
    "Moyennes ;",
    "Médianes ;",
    "Écarts-types"
)
for indice in range(len(moyennes)) :
    print(
        moyennes[indice][0],
        ";",
        f"{moyennes[indice][1]}".replace('.',','),
        ";",
        f"{medianes[indice][1]}".replace('.',','),
        ";",
        f"{ecarts_types[indice][1]}".replace('.',',')
    )
