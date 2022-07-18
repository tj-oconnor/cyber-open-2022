import time

flag = open('flag.txt', 'r').readline().strip('\n').lower()
print("[+] Guess the flag >>> ")

user_guess = input().lower()

for i in range(0, len(flag)):
    if i+1 > len(user_guess):
        print("\n[!] Incorrect")
        exit(-1)
    elif (user_guess[i] != flag[i]):
        print("\n[!] Incorrect")
        exit(-1)
    else:
        time.sleep(0.25)

print("\n[+] Access Granted. Your Flag is: %s" %flag)
