import random
import hashlib

all_char = "1234567890abcdefghijklmnopqrstuvwxyz!"

user_password = "aaaaaaaaaa".lower()
user_password = user_password.strip()
user_password = user_password.lower()

random_password = ""
while random_password != user_password:
    random_password = random.choices(all_char, k=len(user_password))
    print(random_password)

    if random_password == list(user_password):
        print("password is", random_password)
        break