from turtle import *
from random import *

"""
NOM1NOM2 , Fonction Hasard
"""
from RAHMYDEBE import *


#MODIFICATION 1/4 : INDIQUER LE NOM DES JOUEURS
Joueur1="Alea 1"
Joueur2="Alea 2"

#Creation de la grille
speed(0)
title("Morpion")
Taille=600
Marge =30
setup(Taille,Taille+100)
Case=(Taille-2*Marge)//3
up()
goto(Marge-Taille//2,30-Taille//2)
down()
color('red')
write("Joueur Rouge : "+Joueur1,font=("Arial",13))
up()
goto(0,30-Taille//2)
down()
color('blue')
write("Joueur Bleu : "+Joueur2,font=("Arial",13))
up()
color('black')
goto(Marge-Taille//2,Taille//2-Marge+50)
width(3)
for i in range(4):
    down()
    forward(3*Case)
    up()
    backward(3*Case)
    right(90)
    forward(Case)
    left(90)
left(90)
forward(Case)
for i in range(4):
    down()
    forward(3*Case)
    up()
    backward(3*Case)
    right(90)
    forward(Case)
    left(90)
left(90)
forward(4*Case-30)
right(90)
forward(2*Case)


#Imprimer dans une case

def Imprimer_Case(Numero,Caractere):
    up()
    rangee=(Numero-1)//3
    colonne=Numero-1-3*rangee
    right(90)
    forward(colonne*Case)
    left(90)
    backward(rangee*Case)
    if Caractere=='X':
        color('red')
    elif Caractere=='O':
        color('blue')
    write(Caractere,font=("Arial",120))
    forward(rangee*Case)
    left(90)
    forward(colonne*Case)
    right(90)
    color('black')


#Test de victoire

def Tester_Victoire(L):
    if (set([1,2,3])<=set(L)) or (set([4,5,6])<=set(L)) or(set([7,8,9])<=set(L)) or(set([1,4,7])<=set(L)) or(set([2,5,8])<=set(L)) or(set([3,6,9])<=set(L)) or(set([1,5,9])<=set(L)) or(set([3,5,7])<=set(L)):
        return True
    else:
        return False

#Deroulement d'une partie
speed(3)
Case_1=[]
Case_2=[]
Case_Libre=[1,2,3,4,5,6,7,8,9]

#MODIFICATION 2/4 : INDIQUER LEJOUEUR QUI COMMENCE
Joueur=randint(1,2)

Fin=False
while Case_Libre!=[] and Fin==False:
    if Joueur==1:

#MODIFICATION 3/4 : REMPLACER LE NOM DE L ALGORITHME DU JOUEUR 1
        Coup=Hasard(Case_1,Case_2)

        Imprimer_Case(Coup,'X')
        if Coup in Case_Libre:
            Case_1.append(Coup)
            Case_Libre.remove(Coup)
            if Tester_Victoire(Case_1)==True:
                Fin =1
            Joueur=2
        else:
            Fin=2
    else:

#MODIFICATION 4/4 : REMPLACER LE NOM DE L ALGORITHME DU JOUEUR 2
        Coup=Hasard(Case_2,Case_1)

        Imprimer_Case(Coup,'O')
        if Coup in Case_Libre:
            Case_2.append(Coup)
            Case_Libre.remove(Coup)
            if Tester_Victoire(Case_2)==True:
                Fin =2
            Joueur=1
        else:
            Fin=1
up()
goto(Marge-Taille//4,10-Taille//2)
if Fin==False:
    color('black')
    write('Egalite',font=("Arial",13))
elif Fin==1:
    color('red')
    write(Joueur1+" a gagne",font=("Arial",13))
elif Fin==2:
    color('blue')
    write(Joueur2+" a gagne",font=("Arial",13))
exitonclick()



