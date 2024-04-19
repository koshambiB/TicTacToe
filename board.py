
#from TicTacToe  import Oturn,xval,oval,turn,Xturn
def board(xval,oval):
    
    print(f" {'X' if(xval[0] ==0 ) else ('O' if(oval[0] ==0) else " ")} | {'X' if(xval[1] ==1 ) else ('O' if(oval[1] ==1) else " ")} | {'X' if(xval[2] ==2 ) else ('O' if(oval[2] ==2) else " ")} ")
    print(f"---|---|---")
    print(f" {'X' if(xval[3] ==3 ) else ('O' if(oval[3] ==3) else " ")} | {'X' if(xval[4] ==4 ) else ('O' if(oval[4] ==4) else " ")} | {'X' if(xval[5] ==5 ) else ('O' if(oval[5] ==5) else " ")} ")
    print(f"---|---|---")
    print(f" {'X' if(xval[6] ==6 ) else ('O' if(oval[6] ==6) else " ")} | {'X' if(xval[7] ==7 ) else ('O' if(oval[7] ==7) else " ")} | {'X' if(xval[8] ==8 ) else ('O' if(oval[8] ==8) else " ")} ")