import ollama
import math
import random
import time

llm = 'gemma:7b' # changer modèle ici
temp = 2.1 # changer température ici
maxtokens = 6 # changer seuil max de tokens générés ici
samplesize = 31 # changer taille d'échantillon ici

def frenchDecimalValue (string) :
    hasDigit = False
    returnValue = ""
    for char in string :
        if char in [f'{_}' for _ in range(10)]+[','] :
            if not char == ',' or hasDigit :
                returnValue += char
                hasDigit = True
        elif char in ['.'] and hasDigit :
            returnValue += ','
        elif hasDigit:
            return returnValue
    if hasDigit :
        return returnValue
    return 50
def clean_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        pass
def write_new_line(file_path, new_line):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(new_line + '\n')

inferencesteps = [
    ["f ≥ -2 sur [0;1]",
     "f est décroissante sur [1;2]",
     "f(1) = 1",
     "f(2) = -5",
     "-5 < -2",
     "-2 < 1",
     "f(1) = 1",
     "1 > -2"],
    ["1 est le maximum de f",
     "1 ≤ 2",
     "x ≤ 2 est toujours vraie",
     "f(x) ≤ 2 est toujours vraie",
     "2 ≤ 2"],
    ["f(2) = -5",
     "-5 < 1",
     "2 ≥ 1",
     "Le maximum de f est 1",
     "Si f(x) < 1, alors -2 ≤ x < 1"],
    ["Le maximum de f est 1",
     "Si l’antécédent est faux, l’implication est vraie",
     "Le maximum de f est 1",
     "Si f(x) > 1, on a -5 ≤ x < 1"]
]
studentsteps = [
    [
        ["2=f(-5)",
        "f(-5)=-5",
        "-5<f(2)",
        "f(2)=-2",
        "2>1"],
        ["f(x) entre [0;2[ est égal à -2 et 1",
        "f(x)[0;2[≤2"],
        ["f(-2)=0",
        "f(-2)<1",
        "0<1"],
        ["Aucune valeur est supérieure à 1 dans le tableau de variation"]
    ],
    [
        ["f(-5)=2"],
        ["2>1"],
        ["2>1"],
        ["f(x)>-5"]
    ],
    [
        ["il est inf"],
        ["ils sont égaux"],
        ["x est inf"],
        ["il est supérieur"]
    ],
    [
        ["f(0)=-2",
        "0<1"],
        ["f(0)=-2",
        "0<"],
        ["f(0)=-2",
        "1"],
        ["f(0)=-2",
        "1"]
    ],
    [
        ["la courbe va de -2 à 1"],
        ["le max de la courbe est 5"],
        ["le min de la courbe est 1"],
        []
    ],
    [
        ["f(-2)≤2",
        "0>1"],
        ["2≤2",
        "f(-5)≤2"],
        ["f(-2)<1",
        "0<1"],
        ["f(1)≥1",
        "1>1"]
    ],
    [
        ["f(2)=-5",
        "-5<-2"],
        ["le maximum de f(x) est 1"],
        ["f(0)=-2",
        "-2<1"],
        ["le maximum de f(x) est 1"]
    ],
    [
        ["0<-2"],
        ["toutes le valeurs de f(x) son inferieures à 2"],
        ["f(0)=-2"],
        ["f(2)=-5"]
    ],
    [
        ["si f(x)=-2 alors x=0"],
        [],
        [],
        []
    ],
    [
        ["x∈[0;2]",
        "x>sur 2"],
        ["f(x) depasse pas 1"],
        ["x est défini sur [0;2]",
        "x plus grand en 2"],
        ["il n'est pas plus grand mais égal que en 1"]
    ],
    [
        ["le minimum de f est 1"],
        ["f(2)=-5",
        "-5<1",
        "2>1"],
        ["le maximum de f est 1"],
        ["f(2)=-5",
        "-5<-2",
        "2>1"]
    ],
    [
        ["f(1)=1"],
        ["f"],
        ["f(0)=-2"],
        ["f(0)=-2"]
    ],
    [
        ["f(-2)=0"],
        ["f(-5)=2"],
        ["f(1)=1"],
        ["f(-2)=0"]
    ],
    [
        ["f(-2)=-5"],
        ["f≤2"],
        ["f(2)=-5"],
        ["f(x) n'est jamais supérieur à 1"]
    ],
    [
        ["si f(x)<-2 alors on a 0 à -2"],
        ["x≤2 = f(x)≤2"],
        ["f(x)<1,x<1"],
        ["f(x)<1,x<1"]
    ],
    [
        ["-5<-2",
        "2>1"],
        ["2≤2",
        "-5≤2"],
        ["[0;-2]",
        "[2;-5]"],
        ["f(x)≤1 et x≥0"]
    ],
    [
        ["f(x)<-2 entre [1;2]"],
        ["f(x) n'est pas égal mais inférieure à 2"],
        ["x est entre [0;2]",
        "f(x) est décroissant entre [1;2]"],
        []
    ],
    [
        ["f(-5)=2"],
        ["le min est -5",
        "le max 1"],
        ["f(0)=-2"],
        ["f(2)=-5"]
    ],
    [
        ["1 est la seule image supérieur à -2"],
        ["f(x) est strictement inferieur"],
        ["le référentiel de -5 est >1"],
        ["f(x) ne peut pas être supérieur à 1"]
    ],
    [
        ["f(x)≤2",
        "x≤2"],
        ["f(x)<1",
        "x<1"],
        ["f(x)<1",
        "x<1"],
        ["f(x)>-2",
        "x>0"]
    ],
    [
        ["lorsque f(x)<-2 on est sur l'intervalle [1;2]",
        "on voit bien que c'est supérieur a 1",
        "on est entre 1 et 2 et pas égal à 1",
        "la courbe passe par le centre de l'intervalle"],
        ["f(x) ne depasse 2 a aucun moment sur [0;2]"],
        ["la courbe est croissante sur l'intervalle [0;1]",
        "dans cette intervalle [0;1] on passe de 0 à 1 et f(-2) à f(1)"],
        ["la courbe est decroissante sur l'intervalle [1;2]",
        "cette intervalle [1;2] ne possède aucun f(x)>1"]
    ],
    [
        ["f(2)=-5",
        "-5<-2",
        "2>1"],
        ["la fonction est définie sur [0;2]",
        "x≤2",
        "-2≤2",
        "1≤2",
        "-5≤2"],
        ["f(2)=-5",
        "-5<1",
        "2>1"],
        ["f(x)>1 n'existe pas"]
    ],
    [
        ["il est seulement superieur à -5"],
        ["il n'y a pas de f(x)2"],
        ["il est superieur à tous"],
        ["il n'est pas superieur"]
    ],
    [
        ["il est seulement superieur à -5"],
        ["il n'y a pas de f(x)2"],
        ["il est superieur à tous"],
        ["il n'est pas superieur"]
    ]
]
clean_file("llm.csv")
write_new_line("llm.csv",f"Modèle;Température\n{llm};{temp}\nNuméro étudiant;Numéro exercice;Proposition étudiant;Proposition inférence;Concordance générée (en %)")
nbstuprops = 0
random.shuffle(studentsteps)
com = 0
for numstudent in range(len(studentsteps)) :
    student = studentsteps[numstudent]
    for numexercise in range(4) :
        infexercise = inferencesteps[numexercise]
        stuexercise = student[numexercise]
        for stuprop in stuexercise :
           if (nbstuprops < 31) :
              nbstuprops += 1
              for infprop in infexercise :
                 start = time.time()
                 for i in range(samplesize) :
                    prompt = f"CONTEXTE : Un exercice de mathématiques en classe de seconde (lycée) sur les variations d'une fonction définie sur [0;2].\nOBJECTIF : On attend que l'élève dise, possiblement en ses mots, que \"{infprop}\".\nRÉSULTAT : L'élève a dit \"{stuprop}\" à la place.\nATTENTES : Ne réponds qu'un pourcentage, pas de phrase ou de mot.\nCONCORDANCE (en %) = "
                    string = ""
                    stream = ollama.chat (model = llm, messages = [{'role' : 'user', 'content' : prompt}], stream = True, options = {'temperature' : temp, 'num_predict' : 50})
                    for chunk in stream :
                        string += (chunk['message']['content'].replace('\n','\\n').replace('\r','').replace('#','\\#'))
                    print(f"{i} {numstudent};{numexercise};\"{stuprop}\";\"{infprop}\";{frenchDecimalValue(string)}          ",end="\r")
                    write_new_line("llm.csv",f"{numstudent};{numexercise};\"{stuprop}\";\"{infprop}\";{frenchDecimalValue(string)}")
                 print(time.time()-start,"                                                 ")
