"""
Crie uma função que receba um número inteiro como parâmetro e
retorne esse número invertido
"""


def reverseInt(number):
    inv = []
    invstr = ""

    for a in str(number):
        inv.insert(0, a)

    for b in inv:
        invstr += str(b)

    print(invstr)


reverseInt(123456587)
