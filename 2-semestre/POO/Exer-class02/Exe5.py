"""
Crie uma função que receba uma lista com vários números e
retorne a soma de todos os números desta lista, o menor número,
o maior número e a média dos valores da lista.
"""


def listTools(list):
    sumlist = sum(list)
    minlist = min(list)
    maxlist = max(list)
    averagelist = sum(list) / len(list)

    return sumlist, minlist, maxlist, averagelist

a = [2,36,83,4,55,2,3,8]

print(listTools(a))