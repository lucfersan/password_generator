from io import TextIOWrapper
import random

passwords_file = open('password_generator_file.txt', 'a')

lowercase = []
for x in range(97, 123):
  lowercase.append(chr(x))

uppercase = []
for x in range(65, 91):
  uppercase.append(chr(x))

numbers = []
for x in range(48, 58):
  numbers.append(chr(x))

special = []
for x in range(33, 48):
  special.append(chr(x))
for x in range(58, 65):
  special.append(chr(x))
for x in range(91, 97):
  special.append(chr(x))
for x in range(123, 127):
  special.append(chr(x))

app = str(input('Type the application name: '))
password = ''
for x in range(10):
  password += random.choice(lowercase)
  password += random.choice(uppercase)
  password += random.choice(special)
  password += random.choice(numbers)

def write_file(file: TextIOWrapper, text: str):
  file.write(text)
  file.write('\n')

text = app + ': ' + password
write_file(passwords_file, text)

print('This is your ' + app + ' password: ' + password)

passwords_file.close()