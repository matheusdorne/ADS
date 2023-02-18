# Função

def subtrai(n1 , n2):
    return n1 - n2

def multiplica(n1, n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

def soma(n1 , n2):
    return n1 + n2

def ler_inteiro(mensagem):
    while True:
        try:
            numero = int(input("Digite"+mensagem))
            return numero
        except:
            input("Erro. Não é um inteiro. Enter")

def escolha_operacao():
    while True:
        escolha = input("""
        Menu
        1- Soma
        2- Subtrai
        3- multiplica
        4- divide
        escolha: """)

        if escolha in ['1','2','3','4']:
            op = ["", "+","-","*", "/"]
            return op[int(escolha)]
        input("Erro. Escolha 1,2,3,4. Enter")

def calculo(num1, num2, operacao):
    if operacao == '+':
        return soma(num1, num2)
    if operacao == '-':
        return subtrai(num1, num2)
    if operacao == '*':
        return multiplica(num1, num2)
    if operacao == '/':
        if num2 == 0:
            return "Erro. Divisao por Zero."
        return divide(num1, num2)

############################
# Programa principal
while True:
    num1 = ler_inteiro(" um número: ")
    num2 = ler_inteiro(" um segundo número: ")

    operacao = escolha_operacao()

    resultado = calculo(num1, num2, operacao)

    print(f" Resultado de {num1} {operacao} {num2} = {resultado}")



# funções

def soma(n1 , n2):
    return n1 + n2


def entrada_inteira(mensagem):
    numero = int(input(f"Digite o {mensagem} número: "))
    return numero

#######################################
# programa principal

print(
    f"Resultado: "
    f"{ soma( entrada_inteira('primeiro'),entrada_inteira('segundo') ) }"
    f"")


