#    * * *   * * *
#   *      *      *
#    *           *
#      *       *
#        *   *
#          *


def func():
    #r = int(input("Enter the no. of rows: "))
    #c = int(input("Enter the no. of columns: "))
    r = 6
    c = 9
    for i in range(0,r):
        for j in range(0,c):
            if(i==r-1 and j==c-4):
                print("*" , end=" ")
            else:
                print(" ", end=" ")
        print()

func()