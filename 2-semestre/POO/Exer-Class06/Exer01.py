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

class Aluno:
    def __init__(self,nome,matricula,data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        