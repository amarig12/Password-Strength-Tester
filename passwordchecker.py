import string
import os

password= input("Enter a password:")

upperCase = any([1 if c in string.ascii_uppercase else 0 for c in password])
lowerCase = any([1 if c in string.ascii_lowercase else 0 for c in password])
specialCharac = any([1 if c in string.punctuation else 0 for c in password])
numbers = any([1 if c in string.digits else 0 for c in password])

characters = [upperCase, lowerCase, specialCharac, numbers]

length = len(password)

current_folder = os.path.dirname(__file__)  # Get the current script's directory
input_file_path = os.path.join(current_folder, 'commonpasswords.txt')

with open(input_file_path, 'r') as file:
    commonPassword = file.read().splitlines() #splitlines as a password cannot have a blankspace

#if password is found in list of common passwords it prints that it is found and exits 
if password in commonPassword:
    print("Password is found in a common list!")
    exit() #exits code 

passwordScore = 0

#checks length and adds appropiate score
if length > 8:
    passwordScore += 1
if length > 12:
    passwordScore += 1
if length > 16:
    passwordScore += 1
print(f"Your password has {str(length)} number of characters.")

#checks characters and adds appropiate score
if sum(characters) > 1:
    passwordScore += 1
if sum(characters) > 2:
    passwordScore += 1
if sum(characters) > 3:
    passwordScore +=1
print(f"Your password has {str(sum(characters))} different character types.")  

#print scores of password entered
if passwordScore < 3:
    print(f"Your password is weak! Score:{str(passwordScore)}/6")
elif 2 < passwordScore < 5:
    print(f"Your password is okay! Score:{str(passwordScore)}/6")
elif passwordScore > 4:
    print(f"Your password is strong! Score:{str(passwordScore)}/6")