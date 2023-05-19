# Dicionários em python
# dicionario = {} # ou dict()
# estrutura
# { key: value, key: value, key: value,...}

agenda = {"ivonei": "123456", "maria": "2222"}
print(agenda)
agenda = {"nome" : {"endereco" : "endereco",
                    "telefone": [1111],
                    "email": "ana@email.com"}}

agenda["pedro"] = "3333"

for pessoa in agenda:
    print(pessoa)

for pessoa, items in agenda.items():
    print(pessoa, items)


while True:
    nome = input("Nome: ")
    ende = input("Endereço: ")
    
