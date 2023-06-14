"""
Você deverá realizar o controle de um estacionamento.
O estacionamento possui 40 vagas não fixas.
Para isso utilize o menu abaixo:
=== Estacionamento do Tio Ivo ===
1- Estacionar
2- Saída
3- Resumo de ocupação
9- Fim
Escolha:

Na opção1, ao estacionar o veículo você deverá
        informar a placa, o sistema deverá informar
        a primeira vaga livre para estacionar.

Na opção2, você deverá informar a placa do veículo
        e o sistema deverá infomar a vaga onde o
        veículo está estacionado, atualizando o
        horário de saída e liberando esta vaga.

Na opção3, o sistema deverá imprimir todas as vagas
        mostrando os veículos que ocuparam essas
        vagas, horário de entrada e de saída.

Utilizar:
-classe Veiculo
    atributos:
        placa
        hora_entrada
        hora_saida

-classe Estacionamento
    atributo:
        vagas (será um dicionário com 40 vagas)

-estacionamento = {box : [veiculo, veiculo,...]}

OBS. Ao finalizar o programa,
    pergunte ao usuário se ele quer armazenar
    os dados em um arquivo TXT ou JSON.

    Ao iniciar o programa, verifique se o arquivo
    TXT e JSON já existem. Caso exista,
    pergunte ao usuário qual arquivo ele quer
    utilizar.
"""