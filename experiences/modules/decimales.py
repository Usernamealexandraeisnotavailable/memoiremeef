def valeur_decimale(chaine: str) -> str:
    """
    Extrait le premier nombre (avec séparateurs de milliers éventuels) d'une chaîne.
    Accepte les séparateurs décimaux ',' ou '.'.
    Retourne 'nan' si aucun nombre n'est trouvé.
    """
    import re
    try:
        if '%' in chaine:
            match = re.search(r'(\d{1,3}(?:[\s ]\d{3})*(?:[.,]\d+)?)[\s ]*%', chaine)
            if match:
                nombre = match.group(1)
                nombre = nombre.replace(' ', '').replace(' ', '')  # retire espaces et espaces insécables
                return nombre.replace('.', ',')
    except Exception:
        pass

    match = re.search(r'(\d{1,3}(?:[\s ]\d{3})*(?:[.,]\d+)?)', chaine)
    if match:
        nombre = match.group(1)
        nombre = nombre.replace(' ', '').replace(' ', '')  # nettoie les séparateurs de milliers
        return nombre.replace('.', ',')

    return 'nan'