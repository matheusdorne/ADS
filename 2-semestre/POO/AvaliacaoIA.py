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

    def avaliar(self, a, b, c, d, e):
        self.__desemprego = a
        self.__etica = b
        self.__seguranca = c
        self.__regulamentacao = d
        self.__potencial = e

    def __str__(self):
        return f'Desemprego e Desigualdade: {self.__desemprego}' \
               f'Questões Éticas e Morais: {self.__etica}' \
               f'Segurança cibernética e privacidade: {self.__seguranca}' \
               f'Controle e regulamentação: {self.__regulamentacao}' \
               f'Potencial desenvolvimento de IA superinteligente: {self.__potencial}'


UF = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ',
      'RN', 'RS', 'RO',
      'RR', 'SC', 'SP', 'SE', 'TO']
pesquisa = {}

def selecionaUF():
    while True:
        estado = input("Informe a sigla do seu estado (Ex: RS, CE, SP...): ")
        if estado in UF:
            return estado
        else:
            print("Digite uma UF válida!")


def verificaNota(nota):
    if isinstance(nota, int):
        if 0 <= nota <= 5:
            return True
        else:
            print("Digite um valor entre 1 a 5!")
            return False
    else:
        print("Digite um valor entre 1 a 5!")

def converteParaInt(variavel):
    try:
        valor = int(variavel)
        return valor, True
    except ValueError:
        print("Digite um valor entre 1 a 5!")
        return  False



def realizaAvaliacao():
    uf = selecionaUF()
    avaliacao = Relevancia()

    print("\nAvalie o nivel de preocupancia dos seguintes tópicos com notas de 1 a 5.\n")
    while True:
        a , i = converteParaInt(input("Desemprego e Desigualdade: "))
        if verificaNota(a) and i:
            break
    while True:
        b, i = converteParaInt(input("Questões Éticas e Morais: "))
        if verificaNota(b) and i:
            break
    while True:
        c, i = converteParaInt(input("Segurança cibernética e privacidade: "))
        if verificaNota(c) and i:
            break
    while True:
        d, i = converteParaInt(input("Controle e regulamentação: "))
        if verificaNota(d) and i:
            break
    while True:
        e, i = converteParaInt(input("Potencial desenvolvimento de IA superinteligente: "))
        if verificaNota(e) and i:
            break
    avaliacao.avaliar(a,b,c,d,e)

    if uf in pesquisa:
        pesquisa[uf].append(avaliacao)
    else:
        pesquisa[uf] = []
        pesquisa[uf].append(avaliacao)





def relatorio():
    pass


def menu():
    while True:
        escolha = int(input('''Menu
    0- Finalizar o Programa
    1- Realizar avaliação
    2- Relatório
    Escolha: '''))
        if escolha == 0:
            exit()
        elif escolha == 1:
            realizaAvaliacao()
        elif escolha == 2:
            print(pesquisa)
            relatorio()
        else:
            print("Selecione uma opção valida!")
menu()
