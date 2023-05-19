# MGA 802
# Auteur : Michaël Roquejofre
# Date : 15/05/2023

# Code pour jouer au jeu du pendu.
# Ce code a été créé avant la supression des mots 'fantôme' et 'relâche' de la liste.
# Il gère donc les caractères 'ô' et 'â'.

import random
import string

def importation_mots():
    # Ouverture du fichier en mode lecture
    with open("mots_pendu.txt", 'r') as f:
        # Lecture du contenu du fichier
        return f.read()

def choisir_mot(mots):
    # Choix d'un mot aléatoire dans la liste
    return random.choice(mots)

def initialisation(mot_solution):
    # Remplacement des caractères Ã¢ et Ã´ par â et ô
    if '¢' in mot_solution:
        mot_solution = mot_solution[:mot_solution.find('¢') - 1] + 'â'+ mot_solution[mot_solution.find('¢') + 1:]
    elif '´' in mot_solution:
        mot_solution = mot_solution[:mot_solution.find('´') - 1] + 'ô' + mot_solution[mot_solution.find('´') + 1:]
    # Pas de else car si pas de â ou ô on ne veut rien faire

    # Initialisation de deux variables de mémoire
    solution_actuelle = '_ ' * len(mot_solution)
    lettres_utilisees = ''

    return solution_actuelle, lettres_utilisees, mot_solution

def affichage_jeu(nombre_vie, solution_actuelle, lettres_utilisees):
    # Modification du message en fonction du nombre d'essais restant
    if nombre_vie != 1:
        print(f"Il reste {nombre_vie} essais.")
    else:
        print(f"Attention ! Il reste {nombre_vie} seul essai.")

    # Affichage du mot à trouver
    print(f"Le mot à trouver est : {solution_actuelle}")

    # Affichage des lettres déjà essayé
    if len(lettres_utilisees) > 1:
        print(f"Les lettres déjà essayé sont : {lettres_utilisees}.")
    elif len(lettres_utilisees) == 1:
        print(f"La lettre déjà essayé est : {lettres_utilisees}.")
    # Pas de else car si len(lettres_utilisees) == 0 on ne veut rien afficher

    # Renvoi de lettre à essayer
    essai_actuel = input("Entrer la lettre à essayer : ")
    return essai_actuel

def validation(mot_solution, essai_actuel, solution_actuelle):
    # Retour utilisateur
    print(f"La lettre '{essai_actuel}' est dans le mot.")
    # Remplace toutes les itérations de la lettre dans le mot
    while essai_actuel in mot_solution:
        # Cherche l'emplacement de la lettre
        emplacement = mot_solution.find(essai_actuel)
        # Retire la lettre du mot
        mot_solution = mot_solution[:emplacement] + ' ' +  mot_solution[emplacement + 1:]
        # Dévoile la lettre à l'utilisateur
        solution_actuelle = solution_actuelle[:emplacement * 2] + essai_actuel + solution_actuelle[emplacement * 2 + 1:]
    return solution_actuelle

def traitement(mot_solution, essai_actuel, solution_actuelle, lettres_utilisees, nombre_vie):
    # Saut de ligne
    print()
    # Elimine les entrées invalides
    if essai_actuel not in string.ascii_lowercase:
        print(f"Attention ! L'entrée '{essai_actuel}' est invalide.")
        return lettres_utilisees, nombre_vie, solution_actuelle
    # Evite les répétitions
    elif essai_actuel in lettres_utilisees:
        print(f"Attention ! La lettre '{essai_actuel}' a déjà été essayé.")
        return lettres_utilisees, nombre_vie, solution_actuelle
    # Traitement des cas particulier â et ô
    elif essai_actuel == 'a' and 'â' in mot_solution:
        solution_actuelle = validation(mot_solution, 'â', solution_actuelle)
    elif essai_actuel == 'o' and 'ô' in mot_solution:
        solution_actuelle = validation(mot_solution, 'ô', solution_actuelle)
    # Cas général de succès
    elif essai_actuel in mot_solution:
        solution_actuelle = validation(mot_solution, essai_actuel, solution_actuelle)
    # Cas général d'échec
    else:
        print(f"La lettre '{essai_actuel}' n'est pas dans le mot.")
        # Retrait d'une vie, ajout de la lettre utilisé à la liste
        return lettres_utilisees + essai_actuel + ' ', nombre_vie - 1, solution_actuelle

    # Ajout de la lettre utilisé à la liste
    return lettres_utilisees + essai_actuel + ' ', nombre_vie, solution_actuelle

def fin_jeu(solution_actuelle, mot_solution):
    # Saut de ligne
    print()
    # Retour utilisateur
    if '_' in solution_actuelle:
        print(f"Perdu ! Le mot derrière '{solution_actuelle}' était '{mot_solution}'.")
    else:
        print(f"Gagné ! Le mot à trouver était bien '{mot_solution}'.")

def pendu(nombre_vie):

    # Importe la liste de mots fournis
    mots = importation_mots()
    # Separe les mots pour faire une liste
    mots = mots.split('\n')
    # Selectionne un mot dans cette liste
    mot_solution = choisir_mot(mots)

    # Initialisation
    solution_actuelle, lettres_utilisees, mot_solution = initialisation(mot_solution)
    #print(mot_solution) #code pour les tests

    print('Jouons au jeu du pendu !')

    while nombre_vie != 0 and '_' in solution_actuelle:
        # Affichage des informations de jeu
        essai_actuel = affichage_jeu(nombre_vie, solution_actuelle, lettres_utilisees)
        # Traitement de l'entree du joueur
        lettres_utilisees, nombre_vie, solution_actuelle = traitement(mot_solution, essai_actuel, solution_actuelle, lettres_utilisees, nombre_vie)

    # Affichage de fin
    fin_jeu(solution_actuelle, mot_solution)

# Lancement du jeu, l'argument est le nombre de vie du joueur
pendu(6)