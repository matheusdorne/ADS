"""
============================================
Criar uma classe Porta com os atributos:
        altura = 210
        largura = 80
        material = material
        cor = None
        aberta = None
        instalada = None
    Obs. O material deve ser um parâmetro de instância.
        Todos os atributos devem ser privados.


============================================
Criar os métodos:
- abrir
- fechar
- instalar
- pintar

Obs. Só posso abrir ou fechar a porta se estiver
    instalada.
    O método pintar recebe a cor como parâmetro.


============================================
Criar um método para visualizar os dados.
    Obs. Caso a porta não esteja instalada,
        imprimir a mensagem: "Porta não instalada."


============================================
-> Declare uma lista de larguras de portas
aceitaveis. lst_larguras_portas = [60, 70, 80, 90, 100]

-> Crie uma função - escolher_largura_porta - que receba
a lista de larguras de portas como parâmetro e retorne
uma das opções da lista.

-> Altere seu código para que receba também a largura
como parâmetro para a instância de uma nova porta.


============================================
-> Declara uma lista de Materiais para as portas
    - lst_materiais - ['Madeira', 'Ferro', 'Alumínio', 'PVC']

- Crie uma função - escolher_material_porta - que
    receba lst_materiais e retorne o material escolhido


============================================
Declare uma uma lista de portas - lst_portas -
para armazenar as portas.


============================================
Crie uma classe Fechadura com os atributos:
        segredo = segredo
        trancada = False
    Obs. O segredo deve ser um parâmetro de instância.
        Todos atributos devem ser privados.


============================================
Crie os métodos:
    chavear
    deschavear

    Obs. Só posso chavear ou deschavear se a chave (segredo)
        estiver correta.


============================================
Altere a classe Porta o seguinte:
 - Adicione um atributo privado chamado fechadura.
 - Crie um método instalar_fechadura que receba
    como parâmetro uma instância de fechadura.

 - Crie os métodos chavear_porta e deschavear_porta


"""


class Porta:

    def __int__(self, material):
        self.__altura = 210
        self.__largura = 80
        self.__material = material
        self.__cor = None
        self.__aberta = None
        self.__instalada = None
        self.__fechadura = None

    def __str__(self):
        valorPorta = self.__aberta
        if self.__aberta == False or None:
            valorPorta = "Fechada"
        else:
            valorPorta = "Aberta"

        return f'[Altura:{self.__altura}, Largura:{self.__largura}, Material:{self.__material}, Cor:{self.__cor}, Aberta:{valorPorta}, Instalada:{self.__instalada}]'

    def instalar_fechadura(self, fechadura):
        self.__fechadura = fechadura

    def chavear_porta(self):
        if self.__fechadura == None:
            print("Porta não possui fechadura")
        else:
            self.__fechadura.chavear

    def deschavear_porta(self):
        if self.__fechadura == None:
            print("Porta não possui fechadura")
        else:
            self.__fechadura.deschavear

    def abrir(self):
        if self.__instalada == True:
            self.__aberta = True
        else:
            print("A porta não foi instalada")

    def fechar(self):
        if self.__instalada == True:
            self.__aberta = False
        else:
            print("A porta não foi instalada")

    def instalar(self):
        self.__instalada = True

    def pintar(self, cor):
        self.__cor = cor


class Fechadura():

    def __int__(self, segredo):
        self.__segredo = segredo
        self.__trancado = False

    def chavear(self, segredo):
        if segredo == self.__segredo:
            self.__trancado = True
        else:
            print("Chave Incorreta!")

    def deschavear(self, segredo):
        if segredo == self.__segredo:
            self.__trancado = False
        else:
            print("Chave Incorreta!")


lst_larguras_portas = [60, 70, 80, 90, 100]

lst_materiais = ['Madeira', 'Ferro', 'Alumínio', 'PVC']

lst_portas = []


def escolher_info_lista(lista):
    index = 1
    for i in lista:
        print(index, " - ", i)
        index += 1
    escolha = int(input("Escolha uma opção: "))
    if escolha > len(lista):
        print("Digite um opção valida!")
    else:
        return lista[escolha]


escolher_info_lista(lst_materiais)


