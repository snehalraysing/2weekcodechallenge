def calculator():
    def add(n1,n2):
        return n1+n2

    def sub(n1,n2):
        return n1-n2

    def mul(n1,n2):
        return n1*n2

    def div(n1,n2):
        return n1/n2

    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    while(True):
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1','2','3','4'):
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number: "))

            if(choice == '1'):
                print(add(n1,n2))

            elif(choice == '2'):
                print(sub(n1,n2))

            elif(choice == '3'):
                print(mul(n1,n2))

            elif(choice == '4'):
                print(div(n1,n2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                 break

        else:
            print("Invalid Input")

print(calculator())

