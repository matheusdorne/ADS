import json
import datetime


class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def __str__(self):
        return f'Nome: {self.__nome}, Especialidade: {self.__especialidade}, Sala: {self.__sala}'

    def getNome(self):
        return self.__nome

    def getEspecialidade(self):
        return self.__especialidade

    def getSala(self):
        return self.__sala


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def getNome(self):
        return self.__nome

    def getDocumento(self):
        return self.__documento


class Visita:
    def __init__(self, visitante, profissional, data_entrada):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = data_entrada

    def getVisitante(self):
        return self.__visitante

    def getProfissional(self):
        return self.__profissional

    def getDataEntrada(self):
        return self.__data_entrada


def menu():
    while True:
        escolha = int(input('''
        ====================== 
MENU 
====================== 
1- Cadastrar Profissional 
2- Cadastrar Visitante 
3- Localizar Profissional 
4- Registrar Visita 
5- Relatório de Conferência 
6- Gerar arquivo de Registros do dia 
7- Ler arquivos profissionais / visitantes  
8- Teste print
Escolha: '''))
        if escolha == 1:
            cadastrar_profissional()
        elif escolha == 2:
            cadastrar_visitante()
        elif escolha == 3:
            localizar_profissional()
        elif escolha == 4:
            registrar_visita()
        elif escolha == 5:
            relatorio_conferencia()
        elif escolha == 6:
            gerar_arquivo()
        elif escolha == 7:
            ler_arquivo()
        elif escolha == 8:
            for i in l_profissionais:
                print(i)
        else:
            print("Opção inválida")


def verificaSala():
    while True:
        sala = input("Sala: ")
        if converteParaInt(sala):
            break
    return sala


def converteParaInt(variavel):
    try:
        valor = int(variavel)
        return True
    except ValueError:
        print("\nDigite uma valor válido!\n")
        return False


def cadastrar_profissional():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    sala = verificaSala()
    profissional = Profissional(nome.upper(), especialidade.upper(), sala.upper())
    l_profissionais.append(profissional)


def cadastrar_visitante():
    nome = input("Nome: ")
    documento = input("Documento: ")
    visitante = Visitante(nome.upper(), documento)
    l_visitantes.append(visitante)


def localizar_profissional():
    escolha = int(input('\nPesquisa por: '
                        '\n1 - Nome'
                        '\n2 - Profissão'
                        '\nEscolha: '))
    if escolha == 1:
        nome = input("Nome: ")
        for i in l_profissionais:

            if i.getNome == nome.upper():
                print(i)
    elif escolha == 2:
        especialidade = input("Especialidade: ")
        for i in l_profissionais:
            if i.getEspecialidade == especialidade:
                print(i.getNome, i.getEspecialidade, i.getSala)

    else:
        print("Opção inválida")


def listar_profissionais():
    contador = 0
    for i in l_profissionais:
        print(contador, "-", i.getNome, i.getEspecialidade, i.getSala)
        contador += 1
    while True:
        escolha = input("Escolha: ")
        if converteParaInt(escolha) and 0 <= escolha <= contador:
            return l_profissionais[escolha]
        else:
            print("Opção inválida")

def listar_visitantes():
    contador = 0
    for i in l_visitantes:
        print(contador, "-", i.getNome, i.getDocumento)
        contador += 1
    while True:
        escolha = input("Escolha: ")
        if converteParaInt(escolha) and 0 <= escolha <= contador:
            return l_visitantes[escolha]
        else:
            print("Opção inválida")


def registrar_visita():
    profissional = listar_profissionais()
    visitante = listar_visitantes()
    data_entrada = datetime.datetime.now()



def relatorio_conferencia():
    pass


def gerar_arquivo():
    pass


def ler_arquivo():
    pass


l_profissionais = []
l_visitantes = []
dict_visitas = {}
menu()
