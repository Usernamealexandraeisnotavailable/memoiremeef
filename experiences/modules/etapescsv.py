import modules.manipcsv
from statistics import mean

def trouver_etape (
    liste_chemins   : "list",
    indice_exercice : "int",
    etape           : "str",
    nb_eleves       : "int",
) -> "list" :

    """
    1er indice   : indice du modèle
    2ème indice  : 0 pour nom du modèle
                   1 pour liste élèves
    3ème indice  : indice de l'élève
    4ème indice  : indice étape élève comparée
    5ème indice  : colonne
    """

    return [
        [
            chemin,
            [
                modules.manipcsv.filtre_lignes (
                    chemin,
                    [
                        [0, lambda indice_eleve_donne : f"{indice_eleve_donne}" == f"{indice_eleve}"],
                        [1, lambda indice_exercice_donne : f"{indice_exercice_donne}" == f"{indice_exercice}"],
                        [3, lambda etape_donnee : f"{etape_donnee}" == f"{etape}"],
                        [4, lambda pourcentage : str(pourcentage).strip().lower() != "nan"]
                    ],
                    lambda ligne : ligne >= 3
                )
                for indice_eleve in range(nb_eleves)
            ]
        ]
        for chemin in liste_chemins
    ]

def prevalence_etape (
    liste_chemins   : "list",
    indice_exercice : "int",
    etape           : "str",
    nb_eleves       : "int"
) -> "float" :

    liste_trouves = trouver_etape (
        liste_chemins,
        indice_exercice,
        etape,
        nb_eleves
    )

    prevalences = []

    for modele in liste_trouves :
        nom_modele = modele[0]
        maximums_similarites = []

        for eleve in modele[1] :
            maximum_temporaire = 0.0

            for etape_eleve in eleve :
                maximum_temporaire = max (
                    float(etape_eleve[-1].replace(',', '.')),
                    maximum_temporaire
                )

            maximums_similarites.append(maximum_temporaire)

        prevalences.append([
            nom_modele,
            round(mean(maximums_similarites), 2)
        ])

    return prevalences


"""
# exemple d'utilisation
import analysedossier
fichiers = analysedossier.fichiers_dans_dossier("tests")
print(
    prevalence_etape (
        liste_chemins   = fichiers,
        indice_exercice = 0,
        etape           = "f ≥ -2 sur [0;1]",
        nb_eleves       = 31
    )
)
"""
