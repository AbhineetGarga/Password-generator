
import random

print("Lets generate a Secure Password")

# Pass= random.randint(1, 10)
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910@#$%&*()'

number= int(input("How many number of Password you want: "))

length =  int(input("Length of Password: "))

print("\nHere are your Password: ")

for pwd in range(number):
    password= ''
    for c in range(length):
        password+= random.choice(chars)
    print(password)