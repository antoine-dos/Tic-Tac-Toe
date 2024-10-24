<<<<<<< HEAD
=======
MaListe = [" ", " ", " ", " ", " ", " "," ", " ", " "]

def Grille():
    print('-------------\n'
          '|', MaListe[6], '|', MaListe[7], '|', MaListe[8], '|\n'
          '-------------\n'
          '|', MaListe[3], '|', MaListe[4], '|', MaListe[5], '|\n'
          '-------------\n'
          '|', MaListe[0], '|', MaListe[1], '|', MaListe[2], '|\n'
          '-------------')
    return Grille
            
def Joueur_contre_Joueur():

    Joueur_X = "X"
    Joueur_O = "O"
    Fin = False

    input("Quel joueur commence (X/O) : ")

    while Fin == False:

        chiffre = int(input("Choisir une case : ")) -1

        if MaListe[chiffre] != ' ':
            chiffre = int(input("Choisir une autre case : ")) -1
            MaListe[chiffre] = Joueur_X
        else:
            MaListe[chiffre] = Joueur_X

        Grille()

        if MaListe[0] == Joueur_X and MaListe[1] == MaListe[0] == MaListe[2]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[0] == Joueur_X and MaListe[3] == MaListe[0] == MaListe[6]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[0] == Joueur_X and MaListe[4] == MaListe[0] == MaListe[8]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[8] == Joueur_X and MaListe[5] == MaListe[8] == MaListe[2]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[8] == Joueur_X and MaListe[7] == MaListe[8] == MaListe[6]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[6] == Joueur_X and MaListe[4] == MaListe[6] == MaListe[2]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[7] == Joueur_X and MaListe[4] == MaListe[7] == MaListe[1]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[3] == Joueur_X and MaListe[4] == MaListe[3] == MaListe[5]:
            print("Le gagnant est le joueur ", Joueur_X)
            Fin = True
            break
        elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
            print("Aucun gagnant")
            Fin = True
            break
            
        chiffre = int(input("Choisir une case : ")) -1
            
        if MaListe[chiffre] != ' ':
            chiffre = int(input("Choisir une autre case : ")) -1
            MaListe[chiffre] = Joueur_O
        else:
            MaListe[chiffre] = Joueur_O

        Grille()
            
        if MaListe[0] == Joueur_O and MaListe[1] == MaListe[0] == MaListe[2]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[0] == Joueur_O and MaListe[3] == MaListe[0] == MaListe[6]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[0] == Joueur_O and MaListe[4] == MaListe[0] == MaListe[8]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[8] == Joueur_O and MaListe[5] == MaListe[8] == MaListe[2]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[8] == Joueur_O and MaListe[7] == MaListe[8] == MaListe[6]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[6] == Joueur_O and MaListe[4] == MaListe[6] == MaListe[2]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[7] == Joueur_O and MaListe[4] == MaListe[7] == MaListe[1]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[3] == Joueur_X and MaListe[4] == MaListe[3] == MaListe[5]:
            print("Le gagnant est le joueur ", Joueur_O)
            Fin = True
            break
        elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
            print("Aucun gagnant")
            Fin = True
            break

Choix_Jeux = input('Jouer contre un "Joueur" ou contre un "Robot" : ')

if Choix_Jeux == "Joueur" or Choix_Jeux == "joueur":
    print("Que le sort vous soit favorable : ")
    Grille()
    Joueur_contre_Joueur()
elif Choix_Jeux == "Robot" or Choix_Jeux == "robot":
    print("En cour de développment")
>>>>>>> Antoine
