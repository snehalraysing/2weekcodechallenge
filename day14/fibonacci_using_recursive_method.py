#write a program to print fibonacci series using recursive method

n1, n2 = 0, 1
num = int(input("please give a number for fibonacci series : "))

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print("fibonacci series are : ")

for i in range(0,num):
    print(fibonacci(i), end=" ")