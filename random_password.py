import random
from os import system

system("cls")

print("Random Password")
print("Length of password")
length = int(input(">"))

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

password = lower + upper + numbers


random_password = random.choices(password , weights=None , cum_weights= None , k=length)

new_password=""

for i in range(len(random_password)):
    new_password += random_password[i]


print(f'Random generated password: "{new_password}"')


