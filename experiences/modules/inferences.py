import modules.etapes
import modules.etapescsv
import modules.analysedossier
from statistics import mean, stdev

nombre_eleves = len(modules.etapes.a_posteriori)

inferences = [
    [
        [0],
        [0,1,2,3,4],
        [3,4],
        [5],
        [6,7]
    ],
    [
        [0,1],
        [2],
        [3],
        [4]
    ],
    [
        [0,1,2],
        [3],
        [4]
    ],
    [
        [0,1],
        [0],
        [0],
        [2]
    ]
]

fichiers = modules.analysedossier.fichiers_dans_dossier("tests")

def calculer_prevalences_inferences (
    # procédure
) -> "list" :

    resultat = []

    for indice_exercice, exercice in enumerate(inferences) :
        for indice_inference, inference in enumerate(exercice) :

            print(f"Pour inférence {indice_exercice+1}.{indice_inference+1}")
            resultat.append([f"{indice_exercice+1}.{indice_inference+1}"])
            prevalences_etapes = []

            for indice_etape in inference :
                etape = modules.etapes.a_priori[indice_exercice][indice_etape]
                print(f" * Étape {etape} testée")
                prevalence_etape = modules.etapescsv.prevalence_etape (
                    liste_chemins   = fichiers,
                    indice_exercice = indice_exercice,
                    etape           = etape,
                    nb_eleves       = nombre_eleves
                )
                prevalences_etapes.append(prevalence_etape)

            regroupement_modeles = []
            for indice_fichier, fichier in enumerate(fichiers) :
                regroupement_dans_fichier = []
                for prevalences_etape in prevalences_etapes :
                    regroupement_dans_fichier.append (
                        prevalences_etape[indice_fichier][1]
                    )
                regroupement_modeles.append([
                    fichier,
                    round(mean(regroupement_dans_fichier),2)
                ])

            resultat[-1].append(regroupement_modeles)

    return resultat

def calculer_ecarts_types_prevalences_entre_modeles (
    prevalences_inferences : "str"
) -> float :

    ecarts_types = []

    for inference in prevalences_inferences :
        nom_inference = inference[0]
        prevalences_inference = []

        for couple_modele_prevalence in inference[1] :
            prevalences_inference.append(couple_modele_prevalence[1])

        ecarts_types.append([
            nom_inference,
            round(.01*stdev(prevalences_inference),4)
        ])

    return ecarts_types
