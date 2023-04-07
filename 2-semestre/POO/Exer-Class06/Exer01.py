# Crie uma classe Aluno com os seguintes
# atributos de instância:
# - nome
# - matricula
# - data_nascimento
#
# Crie uma lista com instâncias desta classe
#   - crie uma função para adicionar alunos na lista
#   - crie uma função para verificar se um aluno existe
#       ou não na lista. Esta função deve retornar os
#       dados de aluno, mas caso o aluno não conste na
#       lista, retorne a mensagem "ALUNO NÃO MATRICULADO"
#       > consulte pela matrícula ou nome
#   - crie uma função para mostrar todos os alunos da
#       lista, com nome e matrícula.

class Aluno(object):
    def __init__(self, nome, matricula, data_nascimento):
        self.__nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento

    def get_nome(self):
        return self.__nome

    def __str__(self):
        return f"Nome: {aluno.nome} Matricula: {aluno.matricula} Data de Nascimento: {aluno.data_nascimento}"

    # Classe gera vários objetos


lista_alunos = []


def adicionar_aluno(aluno):
    lista_alunos.append(aluno)


def verifica_aluno(dado_consulta):
    for aluno in lista_alunos:
        if type(dado_consulta) == int:
            if aluno.matricula == dado_consulta:
                return f"Nome: {aluno.nome} Matricula: {aluno.matricula} Data de Nascimento: {aluno.data_nascimento}"
        else:
            if aluno.nome == dado_consulta:
                return f"Nome: {aluno.__nome} Matricula: {aluno.matricula} Data de Nascimento: {aluno.data_nascimento}"

    return "Aluno não encontrado"


def imprimir_dados_lista():
    print("\n", "=" * 40)
    for aluno in lista_alunos:
        print(f"Nome: {aluno.get_nome()} Matricula: {aluno.matricula} Data de Nascimento: {aluno.data_nascimento}")

# objeto aluno é apenas a referência de memória

aluno = Aluno("Ivonei", 1111, "25/10/64")
aluno2 = Aluno("Maria", 2222, "22/08/66")
aluno3 = Aluno("Carlos", 3333, "02/10/80")

adicionar_aluno(aluno)
adicionar_aluno(aluno2)
adicionar_aluno(aluno3)

# Atributo é
aluno.nome = "Bundão"

imprimir_dados_lista()
