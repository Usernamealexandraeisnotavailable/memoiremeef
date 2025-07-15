def valeur_decimale (
    chaine : "str"
) -> "str" :
    """
    Cette fonction permet d'analyser les productions LLM pour en extraire un nombre.
    Il s'agit peu ou prou d'une version de floatval (PHP) amélioré. Il extrait le premier nombre décimal qu'il trouve, prenant également en compte que les séparateurs décimaux puissent aussi bien être :
     * des points (".", U+002E), le séparateur décimal natif de Python et principal dans le monde entier,
     * ou des virgules (",", U+002C) comme en France et tel qu'utilisé dans le Bulletin Officiel.
    S'il n'en trouve pas, le programme retourne la chaîne de caractères "nan". Sinon, il renvoie la chaîne de caractères trouvée, en prenant soin d'utiliser une virgule comme séparateur décimal.
    """
    chiffre_trouve = False
    valeur_retour = ""
    for caractere in chaine :
        if caractere in [f'{_}' for _ in range(10)]+[','] :
            if not caractere == ',' or chiffre_trouve :
                valeur_retour += caractere
                chiffre_trouve = True
        elif caractere in ['.'] and chiffre_trouve :
            valeur_retour += ','
        elif chiffre_trouve:
            return valeur_retour
    if chiffre_trouve :
        return valeur_retour
    return 'nan'