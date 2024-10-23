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

Joueur_X = "X"
Joueur_O = "O"

#def condition_X():
#       if MaListe[0] == Joueur_X and MaListe[1] == MaListe[0] == MaListe[2]:
#            print("Le gagnant est le joueur ", Joueur_X)
#           return Fin == True
#       
#       elif MaListe[0] == Joueur_X and MaListe[3] == MaListe[0] == MaListe[6]:
#           print("Le gagnant est le joueur ", Joueur_X)
#            return Fin == True
#        
#        elif MaListe[0] == Joueur_X and MaListe[4] == MaListe[0] == MaListe[8]:
#            print("Le gagnant est le joueur ", Joueur_X)
#            return Fin == True
#        
#        elif MaListe[8] == Joueur_X and MaListe[5] == MaListe[8] == MaListe[2]:
#            print("Le gagnant est le joueur ", Joueur_X)
#            return Fin == True
#        
#        elif MaListe[8] == Joueur_X and MaListe[7] == MaListe[8] == MaListe[6]:
#            print("Le gagnant est le joueur ", Joueur_X)
#            return Fin == True
#        
#        elif MaListe[6] == Joueur_X and MaListe[4] == MaListe[6] == MaListe[2]:
#            print("Le gagnant est le joueur ", Joueur_X)
#            return Fin == True
           

Grille()

Fin = False

while Fin == False:

    chiffre = int(input("Choisir une case : ")) -1
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
    elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
        print("Aucun gagnant")
        Fin = True
        break
    
        
    chiffre = int(input("Choisir une case : ")) -1
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
    elif MaListe[0] != ' ' and MaListe[1] != ' ' and MaListe[2] != ' ' and MaListe[3] != ' ' and MaListe[4] != ' ' and MaListe[5] != ' ' and MaListe[6] != ' ' and MaListe[7] != ' ' and MaListe[8] != ' ':
        print("Aucun gagnant")
        Fin = True
        break
    