#1            #1                #1234(just for j in range(0,4)
#11           #12               #1234
#111          #123              #1234
#1111         #1234             #1234
def func():
    for i in range(0,4):
        #for j in range(0,i+1):
        #for j in range(0,4):
        for j in range(0,i+1):
            print(j+1 , end=" ")
        print()
func()
