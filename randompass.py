import random

lower = 'abcdefghijklmnopqrstuvwxyz'

upper = lower.upper()

numbers = '0123456789'

symbols = "./[]{};:~`!@#$%^&*()+-_/\|,"


all = lower + upper + numbers + symbols
length = 16

pass1 = ",".join(random.sample(all, length))

print(pass1)