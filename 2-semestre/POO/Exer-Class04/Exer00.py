"""
-Definir (instânciar) as listas:
lista_nomes = []
lista_matriculas = []


-Faça uma função que retorne o nome lido
de um aluno. Nome da função: ler_nome()
    (o nome deve ter no mínimo 3 caracteres)
    (não pode aceitar números)

— Faça uma função que retorne a matrícula
lida de um aluno. Nome da função: ler_matricula()
    (somente dígitos alfanuméricos)
    (Não precisa verificar a quantidade de dígitos)

-Faça uma função que receba como parâmetro o
nome de um aluno e adicione a lista_nomes.
Nome da função: adiciona_nome(????)

-Faça uma função que receba como parâmetro a matrícula
de um aluno e adicione a lista_matriculas.
Nome da função: adiciona_matricula(????)

-Faça uma função para imprimir as duas listas
no seguinte formato:
Aluno       Matrícula
Pedro       23998877
Maria       22987622
Carlos      21087980


-Crie uma função chamada inicio() para executar o
menu a baixo:
    while True:
        escolha = input('''
        Menu
        ====================
        1- Adicionar nome
        2- imprimir dados
        ====================
        Escolha: ''')

        if escolha == "1":
            adicionar_dados()
        if escolha == '2':
            imprimir_dados()


- Para a opção 1 do menu crie uma função chamada
adicionar_dados() que, por sua vez, vai chamar as
funções já criadas:
adiciona_nome()
adiciona_matricula()

- Para opção 2 do menu faça a chamada afunção
imprimir_dados().
"""
lista_nomes = ["Matheus", "Carlos"]
lista_matriculas = ["12235435", "4565436"]



def semnumero(value):
    for i in value:
        if type(i) == int or float:
            return False
        else:
            return True


def ler_nome():
    while True:
        nome = input("Digite um nome: ")
        if len(nome) > 3 and semnumero(nome):
            break
        else:
            print("O nome deve ter mais que 3 caracteres e não pode conter números")
    return nome


def ler_matricula():
    while True:
        matricula = input("Digite a matricula: ")
        if matricula.isalnum():
            break
        else:
            print("Matricula pode conter apenas caracteres alfanúmericos.")
    return matricula


def adiciona_nome(value):
    lista_nomes.append(value)


def adiciona_matricula(value):
    lista_matriculas.append(value)


def imprime_dados():
    contador = 0
    for i in lista_nomes:
        linha = ""
        linha += i + (" " * (15 - len(i))) + lista_matriculas[contador]
        contador += 1
        print(linha)


def adicionar_dados():
    adiciona_nome(ler_nome())
    adiciona_matricula(ler_matricula())


def inicio():
    while True:
        escolha = input('''
Menu
====================
1- Adicionar Dados
2- imprimir dados
====================
Escolha: ''')

        if escolha == "1":
            adicionar_dados()
        if escolha == '2':
            imprime_dados()

inicio()