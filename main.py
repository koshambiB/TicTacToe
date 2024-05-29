from board import board  # Import board function (likely for displaying the game board)
from checkWin import checkWin  # Import checkWin function (likely for checking win conditions)


def Oturn(xval,oval):
    Ovalue = int(input("ENTER THE VALUE FOR O: "))
    while(
        Ovalue<0 or Ovalue >8
        or xval[Ovalue] != 9
        or oval[Ovalue] != 9
    ):  # Check for valid input (between 0-8, empty space)
        print("WRONG INPUT")
        Ovalue = int(input("Enter Again : "))
    
    oval[Ovalue] = Ovalue


def Xturn(xval,oval):
    Xvalue = int(input("ENTER THE VALUE FOR X : "))
    while (
        Xvalue<0 or Xvalue >8
        or xval[Xvalue] != 9
        or oval[Xvalue] != 9
    ):  # Check for valid input (between 0-8, empty space)
        print("WRONG INPUT")
        Xvalue = int(input("Enter Again : "))
    xval[Xvalue] = Xvalue


owin = 0
xwin = 0
matches = 1



def game(matches,owin,xwin):
    turn = 1
    xval = [9, 9, 9, 9, 9, 9, 9, 9, 9]  # Initialize board with empty spaces (9)
    oval = [9, 9, 9, 9, 9, 9, 9, 9, 9]  # Initialize board with empty spaces (9)
    while True:
        if turn >= 10:
            print("The match is draw")
            break
        elif turn % 2 == 0:
            Xturn(xval,oval)
            turn+=1
        elif turn % 2 != 0:
            Oturn(xval,oval)
            turn += 1

        board(xval, oval)  # Displays the updated game board

        f = checkWin(xval, oval)  # Check for winner using the checkWin function

        if f == 1:
            print("X wins")
            xwin += 1
            break
        elif f == 2:
            print("O wins")
            owin += 1
            break
        else:
            pass

    st = str(input("Re-match? Y/N" ))
    if st == 'Y':
        game( matches+1,owin,xwin)  # Restart the game
    else:
        print("Times O won : ", owin)
        print("Times X won : ", xwin)
        draw = matches - (owin+xwin)
        print("Draws : ", draw)
            


game(matches,owin,xwin)  # Start the game
