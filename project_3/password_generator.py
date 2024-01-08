import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator")

password_list =[]

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)


password = "".join(password_list)

print(f"Your password is: {password}")