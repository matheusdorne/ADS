'''
Problema:
Faça um algoritmo que realize uma pesquisa por região do brasil sobre quais dos 5 tópicos a cima (Desemprego e desigualdade, Questões éticas e morais, Segurança cibernética e privacidade,
Controle e regulamentação, Potencial desenvolvimento de IA superinteligente) o brasileiro considera mais preocupantes sobre a Inteligência artificial. Em seu programa, o usuário deverá informar qual estado ele reside e escolher um de grau de relevância de 1 a 5 para cada um dos tópicos.
Armazene esses dados em um dicionário ( pesquisa = {} ), onde o estado(sigla) será a chave, e o valor, será uma lista contendo o grau informado de cada usuário na forma de instância(objetos).
Os valores informados serão instâncias da classe Relevancia especificada a baixo.
class Relevancia:
     def __init__(self):
self.__desemprego = None self.__etica = None self.__seguranca = None self.__regulamentacao = None self.__potencial = None

obs. O construtor acima poderá ser modificado se você achar conveniente.
Não é necessário nenhuma identificação, ou validação do usuário. Este apenas escolhe um estado e um valor para cada atributo. Podendo realizar essas avaliações quantas vezes desejar.
Como sugestão:
Seu programa poderá utilizar o seguinte menu como guia:

Menu
0- Finalizar o Programa
1- Realizar avaliação
2- Relatório
Escolha: Obs:

- Uma pessoa avalia todos os tópicos (para facilitar ☺).
Na Opção 1: Informar o estado que reside, e informar o grau para cada um dos 5 tópicos.
Instanciar e adicionar na lista do restado informado.
Na Opção 2: Informar um estado e mostrar o percentual de importância dada a cada tópico do estado informado.
Exemplo de como pode ficar o dicionário:
pesquisa {
RS: [objRelevancia, objRelevancia, objRelevancia, objRelevancia] SC: [objRelevancia, objRelevancia, objRelevancia, objRelevancia] ...
}
Estados
 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO',
 'RR', 'SC', 'SP', 'SE', 'TO'
 '''

class Relevancia:
    def __init__(self):
        self.__desemprego = None
        self.__etica = None
        self.__seguranca = None
        self.__regulamentacao = None
        self.__potencial = None
UF = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO',
 'RR', 'SC', 'SP', 'SE', 'TO']

def selecionaUF():
    while True:
        estado = input("Informe a sigla do seu estado (Ex: RS, CE, SP...): ")
        if estado in UF:
            return  estado
        else:
            print("Digite uma UF válida!")

def realizaAvaliacao():
    uf = selecionaUF()
    avaliacao = Relevancia()



def relatorio():
    pass

def menu():
    while True:
        escolha = input('''Menu
    0- Finalizar o Programa
    1- Realizar avaliação
    2- Relatório
    Escolha: ''')
        if escolha == 0:
            exit()
        elif escolha == 1:
            realizaAvaliacao()
        elif escolha == 2:
            relatorio()
        else:
            print("Selecione uma opção valida!")

