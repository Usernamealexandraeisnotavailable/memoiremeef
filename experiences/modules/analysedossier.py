def fichiers_dans_dossier (
    chemin_dossier : "str"
) -> "list" :
    import os
    if not os.path.isdir(chemin_dossier):
        raise ValueError(f"\"{chemin_dossier}\" n'est pas un dossier.")
    fichiers = [
        f"{chemin_dossier}/{fichier}"
        for fichier
        in os.listdir(chemin_dossier)
        if os.path.isfile(os.path.join(chemin_dossier, fichier))
    ]
    return fichiers
