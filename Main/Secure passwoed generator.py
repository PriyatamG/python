import random
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'r', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@',
              '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '?']
password = ''
for i in range(11):
    password += random.choice(characters)
print(password)
