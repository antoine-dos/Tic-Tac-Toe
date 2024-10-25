def victory(symbol):
    if symbol == TicTacToe[0] and symbol == TicTacToe[1] and symbol == TicTacToe[2]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol == TicTacToe[3] and symbol == TicTacToe[4] and symbol == TicTacToe[5]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[6] and symbol == TicTacToe[7] and symbol == TicTacToe[8]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[0] and symbol == TicTacToe[3] and symbol == TicTacToe[6]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[0] and symbol == TicTacToe[4] and symbol == TicTacToe[8]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[1] and symbol == TicTacToe[4] and symbol == TicTacToe[7]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[2] and symbol == TicTacToe[5] and symbol == TicTacToe[8]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[0] and symbol == TicTacToe[4] and symbol == TicTacToe[8]:
        print("Le joueur X est victorieux")
        fin = True
    elif symbol== TicTacToe[2] and symbol == TicTacToe[4] and symbol == TicTacToe[6]:
        print("Le joueur X est victorieux")
        fin = True
    elif " " not in TicTacToe:
        print("Match nul !")
        fin = True

      


print("Que le sort vous soit favorable :")
TicTacToe = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def plateau () : 
    print("|", TicTacToe[0], "|", TicTacToe[1], "|", TicTacToe[2], "|\n"
          "-------------\n"
          "|", TicTacToe[3], "|", TicTacToe[4], "|", TicTacToe[5], "|\n"
          "-------------\n"
          "|", TicTacToe[6], "|", TicTacToe[7], "|", TicTacToe[8], "|\n")
    return plateau
plateau ()

# Joueur1 = "X"
# Joueur2 = "O"

symbol = "X"

fin = False
while fin == False :
    chiffre = int(input("Quelle case veux tu Joueur X ? ")) -1
    if TicTacToe[chiffre] != " " :
        chiffre = int(input("Choisis une nouvelle case :"))
        TicTacToe[chiffre] = symbol
    else :
        TicTacToe[chiffre] = symbol
    plateau ()
    

    # // ici 


    # chiffre = int(input("Quelles case veux tu Joueur 0 ? ")) -1
    # if TicTacToe[chiffre] != " " :
    #     chiffre = int(input("Choisis une nouvelle case :"))
    #     TicTacToe[chiffre] = symbol
    # else :
    #     TicTacToe[chiffre] = symbol

    plateau ()
    victory(symbol,)
    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"
  
   
    