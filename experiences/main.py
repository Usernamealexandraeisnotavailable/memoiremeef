""" Modules """
import random
import time
import sys
import modules.decimales
import modules.manipfichiers
import modules.etapes
import modules.analyse

""" Données manipulables """
modele                                 : "str"    = "glm4:9b"
temperature                            : "float"  = float(0.0)
seuil_max_tokens_generables            : "int"    = 50
taille_echantillon_par_comparaison     : "int"    = 1
seuil_max_etapes_observees_a_analyser  : "int"    = sys.maxsize
chemin_sortie                          : "str"    = "resultat.csv"


""" Création de l'entête du fichier résultat """
modules.manipfichiers.vider_fichier(chemin_sortie)
modules.manipfichiers.nouvelle_ligne_liste(chemin_sortie, [
    "Modèle",
    "Température"
])
modules.manipfichiers.nouvelle_ligne_liste(chemin_sortie, [
    f"{modele}",
    f"{temperature}"
])
modules.manipfichiers.nouvelle_ligne_liste(chemin_sortie, [
    "Numéro étudiant",
    "Numéro exercice",
    "Proposition étudiant",
    "Proposition inférence",
    "Concordance générée (en %)"
])

""" Analyse selon le modèle """
if seuil_max_etapes_observees_a_analyser < sys.maxsize :
    random.shuffle(modules.etapes.a_posteriori)
nombre_etapes_observees_analysees = 0
for indice_eleve, eleve in enumerate(modules.etapes.a_posteriori) :

    for indice_exercice, etapes_hypothetiques in enumerate(modules.etapes.a_priori) :
        etapes_observees = eleve[indice_exercice]

        for etape_observee in etapes_observees :
            if nombre_etapes_observees_analysees > seuil_max_etapes_observees_a_analyser :
                break
            nombre_etapes_observees_analysees += 1

            for etape_hypothetique in etapes_hypothetiques :
                modules.analyse.analyse_etape (
                    etape_observee,
                    etape_hypothetique,
                    indice_eleve,
                    indice_exercice,
                    modele,
                    temperature,
                    seuil_max_tokens_generables,
                    taille_echantillon_par_comparaison,
                    chemin_sortie,
                    modules.decimales.valeur_decimale,
                    modules.manipfichiers.nouvelle_ligne_liste
                )
