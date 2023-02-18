'''
Competências:
- Atividade é individual. :)
- Saber interpretar o que foi solicitado;
- Desenvolver uma solução viável para o problema proposto;
- Utilizar os comandos de forma adequada para a solução;

Tarefa:
-------
Perguntar a 4 alunos a resposta de 10 questoes de uma prova de múltipla escolha.
Comparar essas respostas com o gabarito da prova.
Calcular o total de acertos de cada aluno.

No final informar:
Aluno(s) com Maior acerto(s)
Aluno(s) com Menor acerto(s)
A média das notas da turma


lista_gabarito = ["A","B","C","D","E","E","D","C","B","A"]
Aceitar como respostas apenas A,B,C,D,E.
'''

list_1 = []
list_2 = []
list_3 = []
list_4 = []

acert_1 = 0
acert_2 = 0
acert_3 = 0
acert_4 = 0

lista_gabarito = ["A","B","C","D","E","E","D","C","B","A"]

def verficaABCD(resp):
    while True:
        if resp == "A" or resp == "B" or resp == "C" or resp == "D" or resp == "E":
            return resp
        else:
            print("Digite uma resposta válida!")
            return 1

def perguntas(x,list):

    while True:
                resp = input("Resposta Questão "+str(x+1)+": ")
                teste = verficaABCD(resp)
                if teste != 1 and list == 1:
                    list_1.append(teste)
                    break
                elif teste != 1 and list == 2:
                    list_2.append(teste)
                    break
                elif teste != 1 and list == 3:
                    list_3.append(teste)
                    break
                elif teste != 1 and list == 4:
                    list_4.append(teste)
                    break

def media(x,y,z,c):
    m = (x + y + z + c)/4
    print("A média dos alunos foi de",m,"acertos")

for i in range(4):
    print("Aluno", i+1)
    if i == 0:
        for x in range(10):
            perguntas(x,1)

    elif i == 1:
        for x in range(10):
           perguntas(x,2)

    elif i == 2:
        for x in range(10):
           perguntas(x,3)
    else:
        for x in range(10):
           perguntas(x,4)

print(list_1,list_2,list_3,list_4)

for x in range(len(list_1)):
        if list_1[x] == lista_gabarito[x]:
            acert_1 += 1
for x in range(len(list_2)):
        if list_2[x] == lista_gabarito[x]:
            acert_2 += 1
for x in range(len(list_3)):
        if list_3[x] == lista_gabarito[x]:
            acert_3 += 1
for x in range(len(list_4)):
        if list_4[x] == lista_gabarito[x]:
            acert_4 += 1

acert_list = [acert_1,acert_2,acert_3,acert_4]

media(acert_1,acert_2,acert_3,acert_4)

print(acert_1,acert_2,acert_3,acert_4)

maxAcert = (max(acert_1,acert_2,acert_3,acert_4))
minAcert = (min(acert_1,acert_2,acert_3,acert_4))

maxAlunoAcert = 0
minAlunoAcert = 0

for x in acert_list:
    if x == maxAcert:
        maxAlunoAcert += 1
for x in acert_list:
    if x == minAcert:
        minAlunoAcert += 1

print("Aluno(s) com maior nota:", maxAlunoAcert)

print("Aluno(s) com menor nota:", minAlunoAcert)






