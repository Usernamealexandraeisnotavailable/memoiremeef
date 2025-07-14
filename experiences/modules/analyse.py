def analyse_etape (
  etape_observee                     : "str",
  etape_hypothetique                 : "str",
  indice_eleve                       : "int",
  indice_exercice                    : "int",
  modele                             : "str",
  temperature                        : "float",
  seuil_max_tokens_generables        : "int",
  taille_echantillon_par_comparaison : "int",
  chemin_sortie                      : "str",
  valeur_decimale                    : "str -> str",
  nouvelle_ligne_liste               : "uncurried(str -> list -> str)"
) -> None :

    import ollama
    import time
    
    for i in range(taille_echantillon_par_comparaison):
        
        prompt = '\n'.join([
            "CONTEXTE : Un exercice de mathématiques en classe de seconde (lycée) sur les variations d'une fonction définie sur [0;2].",
            f"OBJECTIF : On attend que l'élève dise, possiblement en ses mots, que \"{etape_hypothetique}\".",
            f"RÉSULTAT : L'élève a dit \"{etape_observee}\" à la place.",
            "ATTENTES : Ne réponds qu'un pourcentage, pas de phrase ou de mot.",
            "CONCORDANCE (en %) = "
        ])

        epoch_debut = time.time()
        
        chaine = ""
        for chunk in ollama.chat(
            model     = modele,
            messages  = [{'role': 'user',
                          'content': prompt}],
            stream    = True,
            options   = {'temperature': temperature,
                         'num_predict': seuil_max_tokens_generables}
        ) :
            chaine += chunk['message']['content']

        pourcentage = valeur_decimale(chaine)
        print(f"{indice_eleve};{indice_exercice};{etape_observee};{etape_hypothetique};{pourcentage}")
        nouvelle_ligne_liste(chemin_sortie, [
            str(indice_eleve),
            str(indice_exercice),
            f"\"{etape_observee}\"",
            f"\"{etape_hypothetique}\"",
            f"\"{pourcentage}\""
        ])
        
        epoch_fin = time.time()
        
        print(f"Temps d'exécution : {round(epoch_fin - epoch_debut, 2)} secondes")
