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
            if((i==r-1 and j==c-4) or (i==r-2 and j==c-5) or
                    (i==r-2 and j==c-3) or (i==r-3 and j==c-6) or (i==r-3 and j==c-6) or
                    (i==r-3 and j==c-2) or (i==r-4 and j==c-7) or (i==r-4 and j==c-1) or
                    (i==r-5 and j==c-8) or(i==r-5 and j==c-1) or (i==r-6 and j==c-7) or
                    (i==r-6 and j==c-6) or (i==r-6 and j==c-5) or (i==r-5 and j==c-4) or
                    (i==r-6 and j==c-3) or (i==r-6 and  j==c-2) or (i==r-6 and j==c-1)):
                print("*" , end=" ")
            else:
                print(" ", end=" ")
        print()

func()

