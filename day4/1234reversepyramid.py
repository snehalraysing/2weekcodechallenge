#1234
#123
#12
#1

def func():
    for i in range(4,0,-1):
        for j in range(0,i):
            print(j+1, end=" ")
        print()

func()