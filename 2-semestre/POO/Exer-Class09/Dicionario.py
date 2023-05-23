menu = """
    MENU
    ======================
    1- Adicionar pessoa
    2- Mostrar agenda
    Escolha:  """

# menu2 = f"""
#     -----SUB-MENU {""}
#     ======================
#     1- Adicionar novo número
#     2- Excluir número
#     3- Excluir nome
#     4- Retorna Menu anterior
#     Escolha:  """

def menu2(nome):
    return f"""
    >>> {nome} já existe:
    -----SUB-MENU ->{nome}
    ==============================
    1- Adicionar novo número
    2- Excluir número
    3- Excluir nome
    4- Retorna Menu anterior
    Escolha:  """


agenda ={}


def popula_agenda():
    global agenda
    agenda = {
    "ana" : { "endereco" : "rua A",
               "telefone" : ['1111'] ,
               "email" : "ana@email.com"
               },
    "pedro" : { "endereco" : "rua B",
               "telefone" : ['2222'] ,
               "email" : "pedro@email.com"
               }
    }
    print("=== Agenda Populada...")

def get_numeros(lst_fones):
    fones = ""
    for telefone in lst_fones:
       fones += " -"+telefone
    return fones

def novo_numero(nome):
    print(f"Nome: {nome} - {get_numeros(agenda[nome]['telefone'])}")
    agenda[nome]['telefone'].append(input("Novo número: "))

def excluir_numero(nome):
    numero_excluir = input("Número para excluir: ")
    agenda[nome]['telefone'].remove(numero_excluir)

def excluir_nome(nome):
    if input("Confirma Exclusão s/n? ").lower() == "s":
        del(agenda[nome])

def isAgenda():
    if not agenda :
        input("Agenda Vazia!  Enter")
        return False
    return True

def mostrar_agenda():
    if isAgenda():
        for nome, numeros in agenda.items():
            print(f"""
            Nome: {nome}
                Fones: {numeros}
            """)

def continua():
    while True:
        op = input("\nAdicionar/Localizar alguém? s/n: ").lower()
        if op == 's': return True
        if op == 'n': return False

        input("Resposta incorreta. Enter. ")

def visualizar_agenda():
    global agenda
    if isAgenda() :
        print("---------Agenda:")
        for pessoa in agenda:
            print(pessoa)

def adicionar_agenda():
    visualizar_agenda()

    while True:
        if not continua():
            break
        nome = input("\nNome: ")

        if nome not in agenda:
            endereco = input("Endereço: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            agenda[nome]= { "endereco": endereco,
                            "email": email ,
                            "telefone": [telefone]
                            }
            print(agenda)
            continue

        escolha = input(menu2(nome))
        if escolha == '1': novo_numero(nome)
        if escolha == '2': excluir_numero(nome)
        if escolha == '3': excluir_nome(nome)
        if escolha == '4': break

#===============================
def main():
    popula_agenda() # função para teste
    while True:
        escolha = input(menu)
        if escolha == '1': adicionar_agenda()
        if escolha == '2': mostrar_agenda()


if __name__ == '__main__':
    main()
