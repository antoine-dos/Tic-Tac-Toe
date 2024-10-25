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

        # a corriger
        if Joueur_N == 'X':
            Joueur_N = Joueur_X
        elif Joueur_N == 'O':
            Joueur_N = Joueur_O
        else:
            while Joueur_N != 'X':
                Joueur_N = input("Choisir qui commence entre (X/O) : ")
         
        if Joueur_N == 'X' or Joueur_N == 'x':
            Joueur_N = 'X'
        elif Joueur_N == 'O' or Joueur_N == 'o':
            Joueur_N = 'O'

        print("Que le sort vous soit favorable")
        while Fin == False:    

            Grille()

            chiffre = int(input("Choisir une case : ")) -1

            if MaListe[chiffre] != ' ':
                while MaListe[chiffre] != ' ':
                    chiffre = int(input("Choisir une autre case : ")) -1
                MaListe[chiffre] = Joueur_N
            else:
                MaListe[chiffre] = Joueur_N

            if MaListe[0] == Joueur_N and MaListe[1] == MaListe[0] == MaListe[2]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[0] == Joueur_N and MaListe[3] == MaListe[0] == MaListe[6]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[0] == Joueur_N and MaListe[4] == MaListe[0] == MaListe[8]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[8] == Joueur_N and MaListe[5] == MaListe[8] == MaListe[2]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[8] == Joueur_N and MaListe[7] == MaListe[8] == MaListe[6]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[6] == Joueur_N and MaListe[4] == MaListe[6] == MaListe[2]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[7] == Joueur_N and MaListe[4] == MaListe[7] == MaListe[1]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[3] == Joueur_N and MaListe[4] == MaListe[3] == MaListe[5]:
                Grille()
                print("Le gagnant est le joueur :", Nom_Joueur_N)
                Fin = True
                break
            elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
                Grille()
                print("Aucun gagnant")
                Fin = True
                break
            elif Joueur_N == Joueur_X:
                Joueur_N = Joueur_O
                Nom_Joueur_N = Nom_Joueur_O
            elif Joueur_N == Joueur_O:
                Joueur_N = Joueur_X
                Nom_Joueur_N = Nom_Joueur_X

    Condition()

Joueur = "X"

def ia(board, signe):

    if signe not in ('X', 'O'):
        return False

    #Contre X
    if board[6] == Joueur and board[7] == Joueur and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[8] == Joueur and board[7] == Joueur and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[6] == Joueur and board[3] == Joueur and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[0] == Joueur and board[3] == Joueur and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[0] == Joueur and board[1] == Joueur and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[2] == Joueur and board[1] == Joueur and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[2] == Joueur and board[5] == Joueur and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[8] == Joueur and board[5] == Joueur and board[2] == ' ':
        board[1] = signe
        return 1
    elif board[6] == Joueur and board[4] == Joueur and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[2] == Joueur and board[4] == Joueur and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[8] == Joueur and board[4] == Joueur and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[0] == Joueur and board[4] == Joueur and board[8] == ' ':
        board[8] = signe 
        return 8
    elif board[3] == Joueur and board[4] == Joueur and board[5] == ' ':
        board[5] = signe 
        return 5
    elif board[5] == Joueur and board[4] == Joueur and board[3] == ' ':
        board[3] = signe
        return 3
    elif board[7] == Joueur and board[4] == Joueur and board[1] == ' ':
        board[1] = signe 
        return 1
    elif board[1] == Joueur and board[4] == Joueur and board[7] == ' ':
        board[7] = signe 
        return 7
    elif board[6] == Joueur and board[8] == Joueur and board[7] == ' ':
        board[7] = signe
        return 7
    elif board[6] == Joueur and board[0] == Joueur and board[3] == ' ':
        board[3] = signe
        return 3
    elif board[0] == Joueur and board[2] == Joueur and board[1] == ' ':
        board[1] = signe
        return 1
    elif board[2] == Joueur and board[8] == Joueur and board[5] == ' ':
        board[5] = signe 
        return 5
    elif board[3] == Joueur and board[5] == Joueur and board[4] == ' ':
        board[4] = signe
        return 4
    elif board[7] == Joueur and board[1] == Joueur and board[4] == ' ':
        board[4] = signe 
        return 4
    elif board[6] == Joueur and board[2] == Joueur and board[4] == ' ':
        board[4] = signe
        return 4
    elif board[8] == Joueur and board[0] == Joueur and board[4] == ' ':
        board[4] = signe 
        return 4

    #Centre      
    elif board[4] == ' ':
        board[4] = signe
        return 4

    elif board[6] == Joueur and board[2] == Joueur and board[1] == ' ' and board[7] == ' ':
        board[7] = signe
        return 7
    elif board[6] == Joueur and board[2] == Joueur and board[3] == ' ' and board[5] == ' ':
        board[5] = signe 
        return 5
    elif board[8] == Joueur and board[0] == Joueur and board[1] == ' ' and board[7] == ' ':
        board[7] = signe
        return 7
    elif board[8] == Joueur and board[0] == Joueur and board[3] == ' ' and board[5] == ' ':
        board[5] = signe
        return 5
    
    #Haut gauche
    elif board[6] == ' ':
        board[6] = signe
        return 6
    elif board[6] == signe and board[7] == ' ' and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[6] == signe and board[7] == signe and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[6] == signe and board[3] == ' ' and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[6] == signe and board[3] == signe and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[6] == signe and board[4] == ' ' and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[6] == signe and board[4] == signe and board[2] == ' ':
        board[2] = signe
        return 2

    #Haut droit
    elif board[8] == ' ':
        board[8] = signe
        return 8
    elif board[8] == signe and board[7] == ' ' and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[8] == signe and board[7] == signe and board[6] == ' ':
        board[6] = signe 
        return 6
    elif board[8] == signe and board[5] == ' ' and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[8] == signe and board[5] == signe and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[8] == signe and board[4] == ' ' and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[8] == signe and board[4] == signe and board[0] == ' ':
        board[0] = signe
        return 0
    
    #Bas gauche
    elif board[0] == ' ':
        board[0] = signe
        return 0
    elif board[0] == signe and board[1] == ' ' and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[0] == signe and board[1] == signe and board[2] == ' ':
        board[2] = signe
        return 2
    elif board[0] == signe and board[3] == ' ' and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[0] == signe and board[3] == signe and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[0] == signe and board[4] == ' ' and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[0] == signe and board[4] == signe and board[8] == ' ':
        board[8] = signe 
        return 8

    #Bas droit
    elif board[2] == ' ':
        board[2] = signe
        return 2
    elif board[2] == signe and board[1] == ' ' and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[2] == signe and board[1] == signe and board[0] == ' ':
        board[0] = signe
        return 0
    elif board[2] == signe and board[5] == ' ' and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[2] == signe and board[5] == signe and board[8] == ' ':
        board[8] = signe
        return 8
    elif board[2] == signe and board[4] == ' ' and board[6] == ' ':
        board[6] = signe
        return 6
    elif board[2] == signe and board[4] == signe and board[6] == ' ':
        board[6] = signe 
        return 6

def Joueur_contre_Robot():
    Fin = False

    print("Que le sort vous soit favorable")
        
    while Fin == False:
        Grille()
        chiffre = int(input("Choisir une case : ")) -1

        if MaListe[chiffre] != ' ':
            while MaListe[chiffre] != ' ':
                chiffre = int(input("Choisir une autre case : ")) -1
            MaListe[chiffre] = Joueur
        else:
            MaListe[chiffre] = Joueur

        if MaListe[0] == 'X' and MaListe[1] == MaListe[0] == MaListe[2]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[0] == 'X' and MaListe[3] == MaListe[0] == MaListe[6]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[0] == 'X' and MaListe[4] == MaListe[0] == MaListe[8]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[8] == 'X' and MaListe[5] == MaListe[8] == MaListe[2]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[8] == 'X' and MaListe[7] == MaListe[8] == MaListe[6]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[6] == 'X' and MaListe[4] == MaListe[6] == MaListe[2]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[7] == 'X' and MaListe[4] == MaListe[7] == MaListe[1]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[3] == 'X' and MaListe[4] == MaListe[3] == MaListe[5]:
                Grille()
                print("Vous avez gagner")
                Fin = True
                break
        elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
                Grille()
                print("Aucun gagnant")
                Fin = True
                break
        
        ia(MaListe, 'O')

        if MaListe[0] == 'O' and MaListe[1] == MaListe[0] == MaListe[2]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[0] == 'O' and MaListe[3] == MaListe[0] == MaListe[6]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[0] == 'O' and MaListe[4] == MaListe[0] == MaListe[8]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[8] == 'O' and MaListe[5] == MaListe[8] == MaListe[2]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[8] == 'O' and MaListe[7] == MaListe[8] == MaListe[6]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[6] == 'O' and MaListe[4] == MaListe[6] == MaListe[2]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[7] == 'O' and MaListe[4] == MaListe[7] == MaListe[1]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[3] == 'O' and MaListe[4] == MaListe[3] == MaListe[5]:
                Grille()
                print("Vous avez perdu")
                Fin = True
                break
        elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
                Grille()
                print("Aucun gagnant")
                Fin = True
                break
        
Choix_Jeux = input('Jouer contre un "Joueur" ou contre un "Robot" : ')

if Choix_Jeux == "Joueur" or Choix_Jeux == "joueur":
    Joueur_contre_Joueur()
elif Choix_Jeux == "Robot" or Choix_Jeux == "robot":
    Joueur_contre_Robot()