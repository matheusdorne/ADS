import json
import datetime


class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def __str__(self):
        return f'\nNome: {self.__nome}, Especialidade: {self.__especialidade}, Sala: {self.__sala}'

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

    def retornaNome(self):
        return self.__nome

    def getDocumento(self):
        return self.__documento


class Visita:
    def __init__(self, visitante, profissional, data_entrada):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = data_entrada

    def __str__(self):
        return f'Visitante: {self.__visitante}, Profissional: {self.__profissional}, Data Entrada: {self.__data_entrada}'

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
            gerar_arquivo_json()
        elif escolha == 7:
            ler_arquivo()

        else:
            print("Opção inválida")


def verificaSala():
    while True:
        sala = input("Sala: ")
        if testaInt(sala):
            break
    return sala


def testaInt(variavel):
    try:
        valor = int(variavel)
        return True
    except ValueError:
        print("\nDigite uma valor válido!\n")
        return False


def converteParaInt(variavel):
    try:
        valor = int(variavel)
        return valor, True
    except ValueError:
        print("\nDigite uma valor válido!\n")
        return 0, False


def cadastrar_profissional():
    print("\nCadastro de Profissional\n")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    sala = verificaSala()
    profissional = Profissional(nome.upper(), especialidade.upper(), sala.upper())
    l_profissionais.append(profissional)
    print("Profissional cadastrado com sucesso!")


def cadastrar_visitante():
    print("\nCadastro de Visitante\n")
    nome = input("Nome: ")
    documento = input("Documento: ")
    visitante = Visitante(nome.upper(), documento)
    l_visitantes.append(visitante)
    print("Visitante cadastrado com sucesso!")


def localizar_profissional():
    print("\nLocalizar Profissional\n")
    escolha = int(input('\nPesquisa por: '
                        '\n1 - Nome'
                        '\n2 - Especialidade'
                        '\nEscolha: '))
    if escolha == 1:
        nome = input("Nome: ")
        for i in l_profissionais:

            if i.getNome() == nome.upper():
                print(i)
    elif escolha == 2:
        especialidade = input("Especialidade: ")
        for i in l_profissionais:
            if i.getEspecialidade() == especialidade.upper():
                print(i)

    else:
        print("Opção inválida")


def listar_profissionais():
    print("\nLista de Profissionais\n")
    contador = 0
    for i in l_profissionais:
        print(contador, "-", i.getNome(), i.getEspecialidade(), i.getSala())
        contador += 1
    while True:
        escolha = input("Escolha: ")
        escolhaint, boolean = converteParaInt(escolha)
        if boolean:
            if 0 <= escolhaint <= contador:
                return l_profissionais[escolhaint]
            else:
                print("Opção inválida")
        else:
            print("Digite um valor de 0 a ", contador, "")


def listar_visitantes():
    print("\nLista de Visitantes\n")
    contador = 0
    for i in l_visitantes:
        print(contador, "-", i.retornaNome(), i.getDocumento())
        contador += 1
    while True:
        escolha = input("Escolha: ")
        escolhaint, boolean = converteParaInt(escolha)
        if boolean:
            if 0 <= escolhaint <= contador:
                return l_visitantes[escolhaint]
            else:
                print("Opção inválida")
        else:
            print("Digite um valor de 0 a ", contador, "")


def registrar_visita():
    print("\nRegistrar Visita\n")
    profissional = listar_profissionais()
    visitante = listar_visitantes()
    data_entrada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if visitante in dict_visitas:
        dict_visitas[visitante].append({"nome_profissional": profissional.getNome(), "data_entrada": data_entrada,
                                        "Sala:": profissional.getSala()})
    else:
        dict_visitas[visitante] = []
        dict_visitas[visitante].append({"nome_profissional": profissional.getNome(), "data_entrada": data_entrada,
                                        "Sala:": profissional.getSala()})
    print("Visita registrada com sucesso!")

def quantidade_visitas():
    print("\nQuantidade de Visitas\n")
    visitante = listar_visitantes()
    contador = 0
    for i in dict_visitas[visitante]:
        contador += 1
    print("O visitante", visitante.retornaNome(), "fez", contador, "visitas")
def relatorio_conferencia():
    print("\nRelatório de Conferência\n")
    profissional = listar_profissionais()
    for i in dict_visitas:
        for j in dict_visitas[i]:
            if j["nome_profissional"] == profissional.getNome():
                print(i.retornaNome(), j["data_entrada"], j["Sala:"])


def gerar_arquivo_json():
    registros = {}
    for visitante, visitas in dict_visitas.items():
        registros[visitante.getDocumento()] = []
        for visita in visitas:
            registro = {
                "nome_profissional": visita["nome_profissional"],
                "hora_entrada": visita["data_entrada"],
                "sala": visita["Sala:"]
            }
            registros[visitante.getDocumento()].append(registro)

    with open("registros_do_dia.json", "w") as arquivo:
        json.dump(registros, arquivo, indent=4)

    print("Arquivo gerado com sucesso!")


def ler_arquivo():
    try:
        with open("profissionais.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            nome, especialidade, sala = linha.strip().split(":")
            profissional = Profissional(nome, especialidade, sala)
            l_profissionais.append(profissional)

        print("Arquivo 'profissionais.txt' lido com sucesso!")

        with open("visitantes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            nome, documento = linha.strip().split(":")
            visitante = Visitante(nome, documento)
            l_visitantes.append(visitante)

        print("Arquivo 'visitantes.txt' lido com sucesso!")

    except FileNotFoundError:
        print("Arquivos de dados não encontrados.")


l_profissionais = []
l_visitantes = []
dict_visitas = {}
dict_visitas_txt = {}

menu()
