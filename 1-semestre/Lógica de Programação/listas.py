
"""
Faça um algoritmo que leia (teclado) infinitos números inteiros.
Esses números irão preencher a lista "lista_geral" com, no máximo, 10 números (elementos).
Quando lista_geral estiver com os 10 números e o próximo for adicionado,
    deverás retirar o número que ocupa a posição 0 (zero) de lista_geral
    e, se este número for par deverá ser inserido em lista_pares e, se for ímpar,
    deverá ser inserido em lista_impares.
Quando lista_pares ou lista_impares estiverem completarem 5 elementos, a lista deverá ser iniciada
    novamente (retirado todos elementos).
Exemplo: se lista_impares completar 5 elementos, lista_impares = [], e inicia tudo novamente.
"""
lista_geral = []
lista_pares = []
lista_impar = []

while True:

    print("Geral:",lista_geral)
    print("Pares: ",lista_pares)
    print("Impar: ",lista_impar)

    lista_geral.append(int(input("Digite um número inteiro: ")))

    if len(lista_geral) == 10:
        if lista_geral[0] % 2 == 0:
            lista_pares.append(lista_geral[0])
            if len(lista_pares) == 5:
                lista_pares = []
        else:
            lista_impar.append(lista_geral[0])
            if len(lista_impar) == 5:
                lista_impar = []
                """ .pop tem função de remover um index especifico da lista """
        lista_geral.pop(0)




