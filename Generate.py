import random

lowerCase = "qwertyuiopasdfghjklzxcvbnm"
upperCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"

all = lowerCase + upperCase + numbers
length = 10

password = "".join(random.sample(all, length))

print(password)