#Write a Program to Check Whether a Number Nentered by user is Palindrome or Not

num = int(input("Enter any positive number: "))  #525
temp = num
rev = 0
while num > 0:
    rev = (rev*10) + num % 10
    num = num//10
if(temp == rev):
    print("Number is Palindrome.")
else:
    print("Number is not Palindrom.")




