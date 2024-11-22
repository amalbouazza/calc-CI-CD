"""
La librairie calc permet de faire les opérations basiques de calcul entre deux entiers.
"""
import math
def add(arg1,arg2):
    try:
        return int(arg1)+int(arg2)
    except ValueError: 
        print("Vous devez entrer un entier.") 

def sous(arg1,arg2):
    try:
        return int(arg1)-int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 


def mult(arg1,arg2):
    try:
        return int(arg1)*int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 

def div(arg1,arg2):
    try:
        return int(arg1)/int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 
    except ZeroDivisionError:
        print("Vous divisez par 0.")

def modulo(arg1,arg2):
    try:
        return int(arg1)%int(arg2)
    except ValueError:
        print("Un des arguments n'est pas un entier")    
def racine(arg1):
    """Calcule la racine carrée d'un entier."""
    try:
        arg1 = int(arg1)
        if arg1 < 0:
            raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif.")
        return math.sqrt(arg1)
    except ValueError as e:
        print(e)
def ope(operateur,arg1,arg2=None):   
    if operateur=='+':
        return add(arg1,arg2)        
    elif operateur=="%":
        return modulo(arg1,arg2)
    elif operateur=="-":
        return sous(arg1,arg2)
    elif operateur=="x":
        return mult(arg1,arg2)
    elif operateur=="/":
        return div(arg1,arg2)
    elif operateur == "racine":
        return racine(arg1)
    else:
        print("L'opérateur {} n'est pas reconnu.".format(operateur))