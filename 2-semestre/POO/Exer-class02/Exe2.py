"""
Crie uma função que receba um número inteiro como parâmentro e
retorne quantos dígitos há neste número
"""


def countIntDigits(number):
    digits = len(str(number))
    return digits


print(countIntDigits(457845))

