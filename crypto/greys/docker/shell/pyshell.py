#!/usr/bin/env python3

import random


MAX_TRUST = 1000
CODES = 15

flag = open('flag.txt','r').readline() 

print("Welcome to the Seattle Grace Hospital EMR Terminal Access Program")
print("Please enter your credentials to access patient records.")

print("Username: ")
user = input()
print("Password: ")
passwd = input()

if f"{user}/{passwd}" != "mgrey/1515":
    print("Incorrect Credentials!")
    exit()

print("Due to increased security concerns around patient health records, we have recently implemented two-factor authentication.")
print(f"Please enter the series of {CODES} 3-digit codes found on your 2 factor enabled device.")
print('UPDATE: Due to complaints, we have implemented a custom "trust" meter which will allow you to re-enter a code if you mistype.')
print("Your trust goes down more if it looks like you are randomly guessing.")

def get_code():
    print(f"Enter Code #{correct_codes+1} (Trust: {trust}): ")
    inp = input()
    if len(inp) != 3 or not inp.isdigit():
        print("Invalid Code Format!")
        exit()
    else:
        return int(inp)

def cost(a, b):
    return bin(a^b).count('1')

correct_codes = 0
while correct_codes < CODES:
    code = random.randint(0,999)
    trust = MAX_TRUST
    last_guess = None
    while trust > 0:
        guess = get_code()
        if guess == code:
            print("Correct Code")
            correct_codes += 1
            break
        else:
            print("Incorrect Code, please re-enter")
        
        if last_guess is None:  # For first guess, set last_guess = guess, cost = 0
            last_guess = guess
        
        trust -= cost(last_guess, guess)

        last_guess = guess

    if trust <= 0:
        print("Too many incorrect attempts!")
        exit()


print("You have successfully authenticated!")
print(f"FLAG: {flag}")
