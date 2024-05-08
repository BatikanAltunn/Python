import random
a = random.randrange(1,12)
characters = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!+%&/=?*$#:;"
number = "1234567890"
alltogether = characters + upper + special + number
b = []
b.append(random.choice(characters))
b.append(random.choice(upper))
b.append(random.choice(special))
b.append(random.choice(number))

for i in range(a-len(b)) :
  b.append(random.choice(alltogether))
random.shuffle(b)
password = "".join(b)
print("Your Password Is:" , password)


