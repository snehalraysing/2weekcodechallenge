#Write a Program to Find Factorial of a given number N(N is entered by user)

def fun():
    num = int(input("Enter number to obtain its factorial: "))
    mul = 1
    while(num>0):
        mul = mul * num
        num = num - 1
    print(f'Fatorial is: ', mul)


fun()