from turtle import *
from random import *

def Hasard(Mes_Cases,Ses_Cases):
    Cases_Restantes=[]
    for i in range(1,10):
        if (i not in Mes_Cases) and (i not in Ses_Cases):
            Cases_Restantes.append(i)
    return choice(Cases_Restantes)

Joueur1="Alea 1"
Joueur2="Alea 2"

speed(0)
title("Morpion NSI - Ambre & Arthur")
Taille=600
setup(Taille,Taille+100)
Case=(Taille-2*Marge)//3
up()
goto(Marge-Taille//2,30-Taille//2)
down()
color('red')
write("Joueur rouge : "+Joueur1,font=("Arial",13))
up()
goto(0,30-Taille//2)
down()
color('blue')
write("Joueur Bleu :" +Joueur2,font=("Arial",13))
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