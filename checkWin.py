def checkWin(xval,oval):
    flag = 0
    #diagonal
    if((xval[0] !=9 and xval[4]!=9 and xval[8]!=9)or (xval[2] !=9 and xval[4]!=9 and xval[6]!=9)):
        flag = 1
        
    if((oval[0] !=9 and oval[4]!=9 and oval[8]!=9)or (oval[2] !=9 and oval[4]!=9 and oval[6]!=9)):
        flag = 2
    #horizontal 
    for i in range(0,9,3):
        if((xval[i] !=9 and xval[i+1]!=9 and xval[i+2]!=9)):
            flag = 1
        elif((oval[i] !=9 and oval[i+1]!=9 and oval[i+2]!=9)):
            flag = 2
        else:
            pass
    #vertical
    for i in range(0,3):
        if((xval[i] !=9 and xval[i+3]!=9 and xval[i+6]!=9)):
            flag = 1
        elif((oval[i] !=9 and oval[i+3]!=9 and oval[i+6]!=9)):
            flag = 2
        else:
            pass
    return flag