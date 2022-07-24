#write a program to check whether a number is prime number or not

def check_prime():
    num = int(input("Enter any number: "))
    if(num>1):
        for i in range(2,num):
            if(num%i == 0):
                print("Number is not a Prime number.")
                break
        else:
            print("Number is a Prime number")

    else:
        print(num,"Is not a Prime Number.")


check_prime()