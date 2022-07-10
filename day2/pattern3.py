#  * * *
#  *   *
#  * * *


def func():
    for i in range(0,3):
        for j in range(0,4):
            if(i==0 or i==2 or j==0 or j==3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

func()

