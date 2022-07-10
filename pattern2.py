#1111
#111
#11
#1

def pattern2():
    r = int(input("Enter the no. of rows: "))
    for i in range(r,0,-1):
        for j in range(0,i):
            print(1, end=" ")
        print("\n")

pattern2()

