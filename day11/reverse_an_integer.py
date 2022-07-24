#write a program to reverse an integer number

def reverse_integer():
    num = int(input("Enter an positive interger: "))
    #print(num)   #4758
    n = len(str(num))
    #print(n)   #4
    temp = num
    rev = 0
    if(num <= 0):
       print("Please enter a positive integer.")
    else:
        while(num > 0):
           rev = rev*10 + num%10
           num = num//10

    print("Original integer is: ",temp)
    print("Reverse integer is: " , rev)




reverse_integer()