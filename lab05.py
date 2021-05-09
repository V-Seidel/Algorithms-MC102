# Laboratório número 05: Ordenação alternativa

day, n = input().split()
adress_list = []
state = 0  # Criar um estado para verificar se a lista será crescente ou descrescente


def Segunda(x):  # Verifica o número de letras minúsculas da string
    y = 0
    for i in x:
        if i.islower() == 1:
            y = y+1
        else:
            continue
    return y


def Terca(x):  # Verifica o número de letras maíusculas da string
    y = 0
    for i in x:
        if i.isupper() == 1:
            y = y+1
        else:
            continue
    return y


def Quarta(x):  # Por meio da função isalpha verfica se o caractere está no alfabeto
    y = 0
    for i in x:
        if i.isalpha():
            y = y+1
        else:
            continue
    return y


def Quinta(x):  # Checa o número de espaços acrescentados em 1 para ver o num de palavras
    y = 1
    for i in x:
        if i == ' ':
            y = y+1
        else:
            continue
    return y


def Quinta(x):  # Checa o número de espaços acrescentados em 1 para ver o num de palavras
    y = 1
    for i in x:
        if i == ' ':
            y = y+1
        else:
            continue
    return y


def Sexta(x):  # Para qualquer caractere checa o valor ASCII e soma ao total
    y = 0
    for i in x:
        y = y + ord(i)
    return y


for i in range(0, int(n)):
    adress = input()
    adress_list.append(adress)

if day == 'Terca' or day == 'Sexta':
    state = 1

ordered_list = sorted(adress_list, key=eval(day), reverse=state)

for i in range(0, len(ordered_list)):
    print(ordered_list[i])
