def vider_fichier (
    chemin : "str"
) -> None :
    with open(chemin, 'w', encoding='utf-8') as fichier:
        pass
       
def nouvelle_ligne (
    chemin : "str",
    ligne : "str"
) -> None :
    with open(chemin, 'a', encoding='utf-8') as fichier:
        fichier.write(ligne + '\n')

def nouvelle_ligne_liste (
    chemin : "str",
    liste : "list"
) -> None :
    nouvelle_ligne(chemin, ';'.join(liste))