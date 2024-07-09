import random
import string
length = int(input("Enter the length of the password: "))
print("Choose the characters:\n1. Digits\n2. Letters\n3. Special characters\n4. Exit")
character=" "
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        character+= string.ascii_letters
    elif choice == 2:
        character+= string.digits
    elif choice == 3:
        character+= string.punctuation
    elif choice == 4:
        break
    else:
        print(" Invalid option")
pw = []
for i in range(length):
    pw.append(random.choice(character))
print("Generated Password:", "".join(pw))
    