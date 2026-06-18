import random

rock = "✊"
paper = "✋"
scissors = "✌️"

mains_possible = [rock, paper, scissors]

main_du_joueur = input("rock (1) paper (2) scissors (3) : ")
main_de_l_ia = random.choice(mains_possible)

if main_du_joueur == "1" and main_de_l_ia == rock:
    print(f"Le joueur a choisis: {rock}")
    print(f"L'ia a choisis: {rock}")
    print("ÉGALITÉ")

if main_du_joueur == "2" and main_de_l_ia == paper:
    print(f"Le joueur a choisis: {paper}")
    print(f"L'ia a choisis: {paper}")
    print("ÉGALITÉ")

if main_du_joueur == "3" and main_de_l_ia == scissors:
    print(f"Le joueur a choisis: {scissors}")
    print(f"L'ia a choisis: {scissors}")
    print("ÉGALITÉ")

if main_du_joueur == "1" and main_de_l_ia == scissors:
    print(f"Le joueur a choisis: {rock}")
    print(f"L'ia a choisis: {scissors}")
    print("C'est le joueur qui gagne !")

if main_du_joueur == "1" and main_de_l_ia == paper:
    print(f"Le joueur a choisis: {rock}")
    print(f"L'ia a choisis: {paper}")
    print("C'est l'ia qui gagne !")

if main_du_joueur == "2" and main_de_l_ia == rock:
    print(f"Le joueur a choisis: {paper}")
    print(f"L'ia a choisis: {rock}")
    print("C'est le joueur qui gagne !")

if main_du_joueur == "2" and main_de_l_ia == scissors:
    print(f"Le joueur a choisis: {paper}")
    print(f"L'ia a choisis: {scissors}")
    print("C'est l'ia qui gagne !")

if main_du_joueur == "3" and main_de_l_ia == paper:
    print(f"Le joueur a choisis: {scissors}")
    print(f"L'ia a choisis: {paper}")
    print("C'est le joueur qui gagne !")

if main_du_joueur == "3" and main_de_l_ia == rock:
    print(f"Le joueur a choisis: {scissors}")
    print(f"L'ia a choisis: {rock}")
    print("C'est l'ia qui gagne !")



