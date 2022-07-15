#Write a Program to Check whether a year entered by user is Leap Year or not

def leap_year():
    leap = int(input("Enter any year: "))

    if(leap%400 == 0 and leap%100 == 0):
        print(leap , " is a leap year.")

    elif(leap%4 == 0 and leap%10 !=0 ):
        print(leap, " is a leap year.")

    else:
        print(leap, " is not a leap year.")


leap_year()
