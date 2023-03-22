"""
Crie uma função que retorne uma lista com 10 números inteiros entre
10 e 1000
"""
import random


def randomInt():
    number = random.randint(10,1000)
    return number

print(randomInt())