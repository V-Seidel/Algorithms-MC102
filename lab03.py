N = int(input())  
while N!=0:
    name, x, y = input().split()
    literal_position = (x+y)
    x = int((ord(x)-ord('a')+1)) #Transformando o char em inteiro
    y = int(y)
        
    def check_position(i,j,name): #Verficiar se é a origem
        if i==x and j==int(y):
            casa = 'o'
        else:
            casa = check_piece(i,j,name)
        return casa

    def check_piece(i,j,name): #Verificar a lógica de cada peça 
        if name=='Torre':
            if (abs(i-x)==0 or abs(j-y)==0):
                casa = 'x'
            else:
                casa = '-'
        
        elif name=='Peao':
            if i==x:
                if y<=2:
                    if j<=(y+2) and j>y:
                        casa = 'x'
                    else: 
                        casa = '-'
                else:
                    if j<=(y+1) and j>y:
                        casa = 'x'
                    else:
                        casa= '-'
            else:
                casa = '-'

        elif name=='Cavalo':
            if (abs(i-x)==2 and abs(j-y)==1) or (abs(i-x)==1 and abs(j-y)==2):
                casa = 'x'
            else:
                casa = '-'
        
        elif name=='Bispo':
            if (abs(i-x)==abs(j-y)):
                casa = 'x'
            else:
                casa = '-'
        
        elif name=='Rei':
            if (abs(i-x)<=1 and abs(j-y)<=1):
                casa = 'x'
            else:
                casa = '-'

        elif name=='Dama':
            if (abs(i-x)<=1 and abs(j-y)<=1) or (abs(i-x)==abs(j-y)) or (abs(i-x)==0 or abs(j-y)==0):
                casa = 'x'
            else:
                casa = '-'

        return casa

    print("Movimentos para a peca",name,"a partir da casa",literal_position+".")
    for j in range(N,-1,-1):
        for i in range(N+1):     
            if j==(0):
                if i==0:
                    casa = " " 
                    print(casa, end=' ')
                else:
                    casa = (chr(ord('a')+(i-1)))
                    print(casa, end=' ')
            else:
                casa = check_position(i,j,name)
                if i==0:
                    casa = j
                    print(casa, end=' ')
                elif i==N:
                    print(casa, end='\n')
                else:
                    print(casa, end=' ')
        
    print()
    print()
    N = int(input())  
