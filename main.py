MaListe = [" ", " ", " ", " ", " ", " "," ", " ", " "]
Joueur_X = "X"
Joueur_O = "O"
Nom_Joueur_N = ""

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
    
    Nom_Joueur_X = input("Choisir le nom du joueur 'X' : ")
    Nom_Joueur_O = input("Choisir le nom du joueur 'O' : ")
    def Condition():
        Fin = False
        Joueur_N = input("Quel joueur commence (X/O) : ")

        while Joueur_N != "X" or Joueur_N != "x" or Joueur_N != "O" or Joueur_N != "o":
            
            Joueur_N = input("Choisir entre (X/O) : ")
            if Joueur_N == "X" or Joueur_N == "x" or Joueur_N == "O" or Joueur_N == "o":
                break
        
        if Joueur_N == "X" or Joueur_N == "x":
            Joueur_N = "X"
            Nom_Joueur_N = Nom_Joueur_X
        elif Joueur_N == "O" or Joueur_N == "o":
            Joueur_N = "O"
            Nom_Joueur_N = Nom_Joueur_O
        
        print("Que le sort vous soit favorable : ")
        while Fin == False:    

            Grille()

            chiffre = int(input("Choisir une case : ")) -1

            if MaListe[chiffre] != ' ':
                chiffre = int(input("Choisir une autre case : ")) -1
                MaListe[chiffre] = Joueur_N
            else:
                MaListe[chiffre] = Joueur_N

            Grille()

            if MaListe[0] == Joueur_N and MaListe[1] == MaListe[0] == MaListe[2]:
                
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[0] == Joueur_N and MaListe[3] == MaListe[0] == MaListe[6]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[0] == Joueur_N and MaListe[4] == MaListe[0] == MaListe[8]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[8] == Joueur_N and MaListe[5] == MaListe[8] == MaListe[2]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[8] == Joueur_N and MaListe[7] == MaListe[8] == MaListe[6]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[6] == Joueur_N and MaListe[4] == MaListe[6] == MaListe[2]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[7] == Joueur_N and MaListe[4] == MaListe[7] == MaListe[1]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[3] == Joueur_N and MaListe[4] == MaListe[3] == MaListe[5]:
                print("Le gagnant est le joueur : ", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
                print("Aucun gagnant")
                Fin = True
                break
            elif Joueur_N == Joueur_X:
                Joueur_N = Joueur_O
            elif Joueur_N == Joueur_O:
                Joueur_N = Joueur_X

    Condition()

Choix_Jeux = input('Jouer contre un "Joueur" ou contre un "Robot" : ')

if Choix_Jeux == "Joueur" or Choix_Jeux == "joueur":
    Joueur_contre_Joueur()
elif Choix_Jeux == "Robot" or Choix_Jeux == "robot":
    print("En cour de développment")

