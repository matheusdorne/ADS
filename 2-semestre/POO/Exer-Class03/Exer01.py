lista_nomes = ['Pedro',
               'Ana',
               'Guilherme',
               'Carla',
               'Julia',
               'Maria',
               'Valentina',
               'Mariana',
               'Debora',
               'Augusta',
               'Rosangela',
               'Rafaela',
               'Helena',
               'Marco',
               'Mauricio',
               'Matheus']

lista_bebidas = ['CocaCola',
                 'Guarana',
                 'CocaCola',
                 'Pepsi',
                 'Sprite',
                 'Soda Limonada',
                 'Guarana',
                 'CocaCola',
                 'Fanta Laranja',
                 'Soda Limonada',
                 'Guarana',
                 'Pepsi',
                 'Soda Limonada',
                 'Guarana',
                 'Fanta Laranja',
                 'Pepsi']


# Exercício 1
# Desenvolva uma função que receba como parâmetro o nome da bebida e
# Imprima todas pessoas que gostam desta bebida.


# Exercício 2
# Desenvolva uma função que receba como parâmetro o nome e a bebida preferida
# de uma pessoa e insira esses dados nas listas.

# Exercício 3
# desenvolva uma função que retorne o nome da bebida que é mais preferida.


def favSoda(soda):
    lista_resposta = []
    contador = 0
    for a in lista_bebidas:
        if a == soda:
            lista_resposta.append(lista_nomes[contador])
        contador += 1

    print(lista_resposta)


favSoda("Guarana")


def addFavSoda(name, soda):
    lista_nomes.append(name)
    lista_bebidas.append(soda)


def bestSoda(List):
    return max(set(List), key=List.count)


def bestSoda2():
    coca_count = 0
    guarana_count = 0
    sprite_count = 0
    pepsi_count = 0
    fanta_count = 0
    soda_count = 0

    for a in lista_bebidas:
        if a == "CocaCola":
            coca_count += 1
        elif a == "Guarana":
            guarana_count += 1
        elif a == "Sprite":
            sprite_count += 1
        elif a == "Pepsi":
            pepsi_count += 1
        elif a == "Fanta Laranja":
            fanta_count += 1
        elif a == "Soda Limonada":
            soda_count += 1

    list_contadores = [coca_count, guarana_count, sprite_count, pepsi_count, fanta_count, soda_count]

    maxSoda = max(list_contadores)

    for a in list_contadores:
        if maxSoda == list_contadores[0]:
            print("CocaCola")
            break
        elif maxSoda == list_contadores[1]:
            print("Guarana")
            break
        elif maxSoda == list_contadores[2]:
            print("Sprite")
            break
        elif maxSoda == list_contadores[3]:
            print("Pepsi")
            break
        elif maxSoda == list_contadores[4]:
            print("Fanta Laranja")
            break
        if maxSoda == list_contadores[5]:
            print("Soda Limonada")
            break


print(bestSoda(lista_bebidas))
bestSoda2()
