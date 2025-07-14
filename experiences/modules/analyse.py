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
        print(f"Sortie brute : \"{chaine}\"")

        pourcentage = valeur_decimale(chaine)
        donnees = [
            f"{indice_eleve}",
            f"{indice_exercice}",
            f"\"{etape_observee}\"",
            f"\"{etape_hypothetique}\"",
            f"\"{pourcentage}\""
        ]
        
        print(f"Nouvelle ligne : {';'.join(donnees)}")
        nouvelle_ligne_liste(chemin_sortie, donnees)
        
        epoch_fin = time.time()
        
        print(f"Temps d'exécution : {
            round(epoch_fin - epoch_debut, 2)
        } secondes", end="\n\n")
