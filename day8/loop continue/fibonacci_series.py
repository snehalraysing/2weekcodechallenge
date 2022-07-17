#Write a Program to Display Fibonacci Series upto nth term (n is entered by user)

def fibonacci():
    n = int(input("Enter a number to display nth fibonacci series: "))
    n1, n2 = 0, 1
    sum = 0
    for i in range(0,n):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1 + n2

fibonacci()


