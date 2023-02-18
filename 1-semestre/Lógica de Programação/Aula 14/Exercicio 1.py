
"""
Faça uma função que receba uma string como parâmetro e
retorne a quantidade de palavras existente nesta string.
"""


import re
def qntPalavras(texto):
     
    res = len(re.findall(r'\w+', texto))
    print(texto)
    print ("O texto possui " +  str(res) + " palavra(s)")