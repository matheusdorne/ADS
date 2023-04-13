"""
Crie uma classe chamada Pessoa com os seguintes atributos:
    -nome
    -telefone

    Os atributos são privados e do tipo string.

Utilizando o menu a baixo crie uma agenda e armazene
    os objetos de Pessoa em uma lista chamada agenda.
    agenda = []

MENU
================
1- Adicionar / Excluir
2- Visualizar agenda
 Escolha:


Descrição:
Na opção 1: Ler nome
                Caso nome não exista na agenda, ler telefone, Instanciar e
                adicionar em agenda.
            Caso o nome já exista, mostre os dados. Perguntar se quer
                adicionar outro telefone, ou se quer
                excluir o nome localizado, ou excluir um número.

Na opção 2: mostrar na tela o nome e os telefones das pessoas.

"""


class Pessoa:

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def set_nome(self, nome):
        self.__nome = nome

    def set_telefone(self, telefone):
        self.__telefone = telefone


agenda = []
teste = Pessoa("Matheus", "51")
agenda.append(teste)


def menu():
    while True:
        escolha = input('''MENU
================
1- Adicionar / Excluir
2- Visualizar agenda
Escolha: ''')
        if escolha == "1":
            adicionar_excluir()
        if escolha == "2":
            visualiza_agenda()


def adiciona_pessoa(nome):
    telefone = input("Digite telefone: ")
    contato = Pessoa(nome, telefone)
    agenda.append(contato)


def adicionar_excluir():
    valornome = input("Digite o nome: ")

    boolean, index, pessoa = verifica_nome(valornome)

    if boolean == False:
        adiciona_pessoa(valornome)
    else:
        altera_exclui_pessoa(pessoa,index)

def verifica_nome(nome):

    index = 0
    for pessoa in agenda:
        if nome == pessoa.get_nome():
            return True, index, pessoa
        index += 1
    return False

def altera_exclui_pessoa(pessoa, index):
    escolha = input('''
================
1- Adicionar outro telefone
2- Apagar nome 
3- Apagar telefone
 Escolha: ''')

    if escolha == "1":
        a = input("Digite o telefone: ")
        pessoa.set_telefone(a)
        agenda[index] = pessoa

    elif escolha == "2":
        pessoa.set_nome("")
        agenda[index] = pessoa


    else:

        pessoa.set_telefone("")
        agenda.insert(index, pessoa)


def visualiza_agenda():
    for i in agenda:
        print("Nome:",i.get_nome(),"Telefone:",i.get_telefone())


menu()
print(agenda)
