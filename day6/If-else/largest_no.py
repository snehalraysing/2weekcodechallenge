#Write a Program to Find Largest Number Among ThreeNumbers entered by users

def find_largest():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))

    if(n1>=n2 and n1>=n3 ):
        print("Largest number is: ", n1)

    elif(n2>=n1 and n2>=n3):
        print("Largest number is: ", n2)

    elif(n3>=n1 and n3>=n2):
        print("Largest number is: ", n3)

    else:
        print("Bye")

find_largest()