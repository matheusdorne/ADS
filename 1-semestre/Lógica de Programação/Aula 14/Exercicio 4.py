"""
Faça uma função que receba como parâmetro uma lista com elementos
de diferentes tipos.
Separe os elementos em 3 listas diferentes:
lista_int, lista_str, lista_outros
Esta função deverá Retornar essas 3 listas.
Imprima as listas e a quantidade de elementos de cada lista.
"""

def verifica3Elementos(lista):

    lista_int = []
    lista_str = []
    lista_outros = []

    for a in lista:
        if isinstance(a,int):
            lista_int.append(a)
        elif isinstance(a,str):
            lista_str.append(a)
        else:
            lista_outros.append(a)

    print(lista_int, "Possui",len(lista_int),"elemento(s)")
    print(lista_str, "Possui", len(lista_str), "elemento(s)")
    print(lista_outros, "Possui", len(lista_outros), "elemento(s)")

    return lista_int,lista_str,lista_outros

verifica3Elementos([1,2,3,456,3,6,34,4.0,2.8,5.7,3.7,"teste","amor"])