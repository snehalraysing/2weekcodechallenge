#Write a Program to Check Whether a Character isVowel or Consonant.
#vowels = a,e,i,o,u
def check_alpha():
    while(True):
        alpha = input("Enter Any Character: ")

        if(alpha == 'a' or alpha == 'e'or alpha == 'i' or alpha == 'o' or alpha == 'u'):
            print(alpha, "is a Vowel.")

        elif(alpha == 'A' or alpha == 'E'or alpha == 'I' or alpha == 'O' or alpha == 'U'):
            print(alpha, "is a Vowel.")

        elif(alpha == '0' or alpha == '1'):
            print("Thankyou Program Exit.")
            break

        else:
            print(alpha , "is a Consonant.")



check_alpha()