#Write a Program to Generate Multiplication Table of anumber (entered by the user) using a for loop.

def table():
    num = int(input("Enter a number whose multiplication table you want: "))
    list = [0,1,2,3,4,5,6,7,8,9,10]
    while(num>=0):
        for i in list:
            result = num * i
            print(result)
        break


table()

