#Write a Program to Display Fibonacci Series uptocertain number n (n is entered by user)
#Example: n=100
#Output:
#Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def fibonacci():
    n = int(input("Enter any positive number: "))          #10-->0,1,1,2,3,5,8 this should be printed
    n1, n2 = 0, 1
    sum = n1 + n2
    print(n1)
    print(n2)
    while(sum <= n): #sum <= 10
               print(sum)
               n1 = n2
               n2 = sum
               sum = n1 + n2


fibonacci()