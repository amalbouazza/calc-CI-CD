"""
Un script python prenant 3 arguments dont le premier est l'opération voulue et les deux suivants 
les deux entiers.
"""

import calc
import sys

print("Bienvenue dans cette petite calculatrice sous Python pour entier.\n")


def run_calc():
    op = input("Choisissez une opération entre +, -, x , /, %, et racine : \n")
    
    if op == "racine":
        term_1 = input("Entrer l'entier pour calculer sa racine carrée : \n")
        res = calc.ope(op, term_1)
        if res is not None:
            print(f"La racine carrée de {term_1} est {res:.2f}")
    else:
        term_1 = input("Entrer votre premier entier : \n")
        term_2 = input("Entrer votre second entier : \n")
        res = calc.ope(op, term_1, term_2)

        if res is not None:
            print(f"{term_1} {op} {term_2} = {res}")

    keep_going = input("Voulez-vous stopper le programme ? Écrivez Oui pour arrêter.\n").strip()
    if keep_going.lower() == "oui":
        print("Merci d'avoir utilisé la calculatrice. À bientôt !")
        sys.exit(0)
    
    # Recommencer le programme si l'utilisateur ne veut pas arrêter
    print("Nous allons recommencer le programme\n")
    run_calc()


run_calc()