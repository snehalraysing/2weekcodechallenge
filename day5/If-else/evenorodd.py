#Write a Program to Check Whether Number is Even or Odd

def check():
    num = int(input("Enter any number:  "))
    if(num % 2 == 0):
        print(num , "is an even number.")
    else:
        print(num, "is an odd number.")

check()