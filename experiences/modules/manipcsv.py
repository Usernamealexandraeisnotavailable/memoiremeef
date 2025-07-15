import csv

def liste_csv (
    chemin_csv : "str"
) -> "list" :

    donnees = []
    with open (
        chemin_csv,
        mode='r',
        newline='',
        encoding='utf-8'
    ) as fichier :
        lecteur = csv.reader (
            fichier,
            delimiter=';'
        )
        for ligne in lecteur :
            donnees.append(ligne)
    return donnees

def filtre_lignes (
    chemin_csv      : "str",
    filtres_contenu : "list[int*(int->bool)]",
    filtre_lignes   : "int->bool"
) -> "list[ligne:list]" :

    liste = liste_csv(chemin_csv)
    lignes_filtrees = []

    for indice, ligne in enumerate(liste) :
        if not filtre_lignes(indice) :
            continue
        if all(
            filtre(ligne[colonne])
            for colonne, filtre
            in filtres_contenu
        ) :
            lignes_filtrees.append(ligne)

    return lignes_filtrees

"""
# exemple d'utilisation
print (
    filtre_lignes (
        "tests/llama@0.csv",
        [
            [0, lambda indice_eleve : indice_eleve == "20"],
            [1, lambda indice_exercice : indice_exercice == "2"]
        ],
        lambda ligne : ligne & 1
    )
)
"""
