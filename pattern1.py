#1
#11
#111
#1111

def func():
    r =int(input("Enter the number of rows: "))
    for i in range(0,r):
        for j in range(0,i+1):
            print(1, end=" ")
        print(" ")

func()

