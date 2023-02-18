"""
Faça uma função que receba como parâmetro uma lista.
(este parâmetro pode ter tipos de dados diferentes.)
Retorne uma lista com todos os números float existentes no
parâmetro.
Caso não exista nenhum número float no parâmetro, retorne
a seguinte mensagem: 'SEM NÚMEROS REAIS' "
"""

def verificaFloat(lista):
    listFloat = []
    for a in lista:
       if isinstance(a,float):
           listFloat.append(a)
    if listFloat != []:
        print(listFloat)
        return listFloat
    else:
        print("SEM NÚMEROS REAIS")

verificaFloat([12.0,45,7.0,3,8,"amor","teste",True])