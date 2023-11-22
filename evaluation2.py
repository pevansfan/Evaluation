#Exercice 1
def op_sum(a, b):
    return a + b #somme de deux nombres

def op_substract(a, b):
    return a - b #différence de deux nombres

def op_multiplication(a, b):
    return a * b #produit de deux nombres

def op_division(a, b):
    if b != 0: #en effet, on ne peut diviser par 0, le dénominateur doit donc être non nul
        return a / b 
    else:
        print("Vous ne pouvez pas diviser par 0")


def sum1(*args):
    result = 0
    for n in args:
        result += n #somme de nombres (dont on ne connait le nombre)
    
    return result

def substract2(*args):
    result = 0
    for n in args:
        result -= n #somme de nombres (dont on ne connait le nombre)
    
    return result

def multiplication2(*args):
    result = 0
    for n in args:
        result *= n #somme de nombres (dont on ne connait le nombre)

    return result

def division2(*args):
    result = 0
    for n in args:
        if n == 0:
            print("Vous ne pouvez pas diviser par 0")
        else:
            first_number = args[0] #on prend le premier nombre pour éviter d'avoir un résultat nul au début
            result = first_number / n #division de nombres (dont on ne connait le nombre)

    return result



def demande():
    operation = input("Quel type d'opération souhaitez-vous appliquer ? (addition, soustraction, multiplication, division) : ")

    while True:
        nombre = input("Entrer un nombre : " )

        if nombre.lower() == "stop":
            break

        nombre = int(nombre)
        
        if operation.lower() == "addition":
            print(sum1(*nombre))
            

        if operation.lower() == "soustraction":
            #L_nombres += nombre  
            print(substract2()) 

        if operation.lower() == "multiplication":
            #L_nombres += nombre
            print(multiplication2())
        
        if operation.lower() == "division":
            #L_nombres += nombre
            print(division2())

demande()

'''
#Exercice 2
import json

def information():
    survey = []
    while len(survey) < 2:
        
        nom = input("Entrer votre nom  de famille : ")
        if nom == "stop":
            break
        
        prenom = input("Entrer votre prénom : ")
        if prenom == "stop":
            break
        jour = input("Entrer le jour de votre naissance (en chiffres) :  ")
        mois = input("Entrer le mois de naissance (en chiffres) : ")
        annee = input("Entrer l'année de naissance : ")
        date_de_naissance = f'{jour}/{mois}/{annee}'
        if jour == "stop" or mois == "stop" or annee == "stop":
            break
        
        couleur = input("Quelle est votre couleur préférée ? ")
        if couleur == "stop":
            break

        utilisateur = {}
        utilisateur["Nom"] = nom
        utilisateur["Prénom"] = prenom
        utilisateur["Date de naissance"] = date_de_naissance
        utilisateur["Couleur préférée"] = couleur

        survey.append(utilisateur)
        print("")

    if len(survey) == 2:
        for dict in survey:
            demande_nom = input("Entrer votre nom : ")
            demande_prenom = input("Entrer votre prénom : ")
            if demande_nom == dict["Nom"] and demande_prenom == dict["Prénom"]:
                question = int(input("Combien d'animaux possédez-vous ? : "))
                dict["Nombres d'animaux"] = question
                
            else:
                print("Vous n'êtes pas répertorié dans la liste des personnes.")
    

    with open("survey.json", "w") as json_file:
        json.dump(survey, json_file, indent=4)
    
    mon_fichier = open("survey.json", "r")
    data = json.load(mon_fichier)
    print(data)

    



information()

'''   