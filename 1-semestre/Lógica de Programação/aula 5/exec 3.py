
linhas = int(input("Digite a quantidade de linhas: ")) 
msg = ""
for a in range(linhas): 
    if a != 0:  
        msg = (str(a))
        if a != 1: 
            msg += str("0"*(a-1)) 
            
    print(msg)     