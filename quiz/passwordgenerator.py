# Task: Password Generator
# Create a Python program that generates a secure password based on these conditions:

# The password should be 12-16 characters long.
# It must include:
# At least 2 uppercase letters.
# At least 2 digits.
# At least 2 special characters (e.g., @, #, $, %).
# The remaining characters can be random letters, numbers, or symbols.
# Ensure no character repeats consecutively (e.g., "aa" is invalid).
# The program should allow the user to specify the desired password length within the given range.
# Bonus Challenge: Implement logic that retries the generation process if the rules aren’t satisfied (edge case prevention).


import random


def generate():
    while True:
        user_desire = input("ENTER YOUR PASSWORD LENGTH: ")
        print("YOUR Length: ",user_desire)
        length = int(user_desire)
        if 12 <= length <=16:
            break
        else:
            print("WRONG length the range is 12 - 16")


    print('length is: ',length)
    password = []
    count = 0

    for numbers in range(length):
        
        if count == 0 or count % 5 == 0:
            password.append(random.choice('!@#$%&*'))
        elif count % 2 == 0:
            password.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        else:
            password.append(random.randint(0,9))
        count +=1

        
       
    return password




def validation():
    password = generate()
    capital = 0
    digits = 0
    lower = 0
    special = ['!', '@', '#', '$', '%', '&', '*']
    special_count = 0;

    
    for numbers in password:
        if isinstance(numbers,str):
            if numbers.isupper():
                capital+=1  
            if numbers in special:
                special_count+=1
        else:
            digits+=1

            
    if (capital>=2 and digits>=2 and special_count >= 2):
        print("PASSWORD GENERATED SUCCESSFULLY")
        final_password = ' '.join(map(str,password))
        print('YOUR PASSWORD: ',final_password)
    else:
        validation()

    


validation()