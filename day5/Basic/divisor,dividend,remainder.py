#formula
#dividend = divivsor * quotient + remainder

#Write a program where the user is asked to enter twointegers (divisor and dividend)
#and the quotient and theremainder of their division is computed.
#(Both divisor anddividend should be integers.)

def division():
    dividend = int(input("Enter the divisor: "))
    divisor = int(input("Enter the dividend: "))

    quotient = dividend/divisor

    #print(quotient)

    remainder = dividend % divisor
    print("Quotient is: ", quotient)
    print("Remainder is: ", remainder)

division()

