linhas = int(input("Digite a quantidade de linhas: ")) 
msg = ""
for a in range(linhas):   
    a +=1 
    if a <10:
        msg += str(a)
        print(msg,"."*(10-a),msg) 