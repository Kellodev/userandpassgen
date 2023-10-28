import random, time

chars = "abcdefghijklmnopgrstuvwxyz1234567890!.?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwordlenght = input("How many characters do you want the password to be?")
usernamelenght = input("How many characters do you want the username to be?")

password = ""
username = ""

for i in range(int(passwordlenght)):
    password += random.choice(chars)

for i in range(int(usernamelenght)):
    username += random.choice(chars)

print("PASS: " + password + " - USERNAME: " + username)
