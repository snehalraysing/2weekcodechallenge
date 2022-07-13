#Write a Program to Swap Two Numbers

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
print("Numbers before swapping: ", n1," ", n2)

#4 <--- #4
temp = n1

#3 <--#3
n1=n2

#4 <---#4
n2 = temp

print("Numbers after swapping: ",n1," ",n2)