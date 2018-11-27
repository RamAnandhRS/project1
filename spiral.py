def spiral():
    row=int(input())
    column=int(input())
    lis=[[input() for i in range(0,row)] for j in range(0,column)]
    for i in range(0,row):
        print (lis[i])
    for i in range(0,row):
        for j in range(0,column):
            if (i==0) or (j==0) or (i==row-1) or (j==column-1):
                print(lis[i][j],end=" ")
            else:
                print(" ",end=" ")


spiral()