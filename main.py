import random
import hashlib
import json
import string


cara = [False, False, False, False, False]
longueur=12


def menu():
    choose=input("""
                 Veuillez choisir une option parmi celles-ci :

                 1/ Générer un mot de passe aléatoire
                 2/ Definir un mot de passe
                 3/ Quitter
                 """)
    
    if choose == '1':
        aleatoire(longueur)
        print(mdp_aleatoire)

    if choose == '2':
        verification(create())

    if choose == '3':
        print("Aurevoir")


def aleatoire(longueur):
    caracteres = string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    pwd = ''.join(random.choice(caracteres) for _ in range(longueur))
    return pwd
mdp_aleatoire = aleatoire(12)


def create():
    mdp=input("""
          Veuillez entrer un mot de passe qui contient ceci :
            ➔ Au moins huit caractères.
            ➔ Au moins une lettre majuscule.
            ➔ Au moins une lettre minuscule.
            ➔ Au moins un chiffre.
            ➔ Au moins un caractère spécial !, @, #, $, %, ^, &, *.
          """)
    return mdp


def hash(x):
    hashage = hashlib.sha256()
    hashage.update(x.encode('utf-8'))
    hashage_data = hashage.hexdigest()
    return hashage_data


def verification(s):
    if len(s) >= 8:
        cara[0] = True

    for i in s:
        if i in "abcdefghijklmnopqrstuvwxyz":
            cara[1] = True
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cara[2] = True
        if i in string.digits:
            cara[3] = True
        if i in "!, @, #, $, %, ^, &, *":
            cara[4] = True

    if sum(cara) == 5:
        print("Mot de passe validé")
        h = hash(s)
        with open('data.json', 'r') as json_file: 
            variable=json.load(json_file)
        num = len(variable)
        data = {num : h}
        variable.update(data)
        with open('data.json', 'w') as json_file:
            json.dump(variable, json_file, indent=2)
    else:
        print("Mot de passe invalide, veuillez choisir un nouveau mot de passe valide")
        verification(create())

menu()

