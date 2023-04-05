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
#       lista, com nome e matricula.

class Aluno(object):
    def __init__(self, nome, matricula, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento

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
                return f"Nome: {aluno.nome} Matricula: {aluno.matricula} Data de Nascimento: {aluno.data_nascimento}"

    return "Aluno não encontrado"

def imprimir_dados_lista():
    print("\n","="*40)
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome} Matricula: {aluno.matricula} Data de Nascimento: {aluno.data_nascimento}")


aluno = Aluno("Ivonei", 1111, "25/10/64")
# objeto aluno é apenas a referencia de memoria
aluno2 = Aluno("Maria", 2222, "22/08/66")

adicionar_aluno(aluno)
adicionar_aluno(aluno2)

print(lista_alunos)

# Atributo é
print(aluno.nome)

verifica_aluno("Ivonei")
print(verifica_aluno(2222))

imprimir_dados_lista()