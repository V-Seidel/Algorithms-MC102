password, number_of_attempts = input().split() 
number_of_attempts = int(number_of_attempts)

password_list = list(map(int, str(password))) #Transforma um int em uma lista str

def check_similarity(attempts_list,password_list): #Função para determinar a similaridade entre as senhas
    similarity=0
    
    for i in range(0,len(password_list)): #Percorre a lista comparando os números entre as senhas
        if attempt_list[i]==password_list[i]: 
            similarity=similarity+1
    
    return similarity

while number_of_attempts>0:
    attempt = input()
    attempt_list = list(map(int, str(attempt)))
    
    if len(password_list)!=len(attempt_list): #Checa se a tentativa tem o mesmo número de dígitos que a senha
        number_of_attempts=number_of_attempts-1
        print("Senha incorreta")
        print("Semelhanca: Erro: quantidade de digitos incongruente")
        print("Tentativas restantes:",number_of_attempts)
        print("")
    
    else:
        similarity = check_similarity(attempt_list,password_list)
        
        if similarity==len(password_list):
            print("Senha reconhecida. Desativando defesas...")
            break
            
        else:
            number_of_attempts=number_of_attempts-1
            print("Senha incorreta")
            print("Semelhanca:",similarity)
            print("Tentativas restantes:",number_of_attempts)
            print("")

if number_of_attempts==0:
    print("Tentativas esgotadas. Acionando defesas...")


