nome_canal = input()
numero_anotacoes = int(input())

#Variáveis auxiliares
i=1
datas_list = []
views_list = []
anotacoes_trienio = 0

#Função que calcula as views totais, porcentagem e média do ano inserido
def estatistica_anual(ano):   
    views_anuais = []
    for j in range(0,len(datas_list),3):
        if int(datas_list[j])==ano:
            views_anuais.append(views_list[int(j/3)]) #Dividir o índice por 3 para achar o índice das views 
    views_anuais_totais = sum(views_anuais)
    if views_trienio==0:
        porcentagem_views = 'indeterminada'
    else:
        porcentagem_views = round(((views_anuais_totais/views_trienio)*100),2)
    media = round((views_anuais_totais/len(views_anuais)),2)
    return(views_anuais_totais,porcentagem_views,media)

while i<=numero_anotacoes:
    data = input()
    verificacao_data = data.split('-')
    views = int(input())
    if int(verificacao_data[0])>=2018 and int(verificacao_data[0])<=2020: #Verificar se o ano está dentro do range
        datas_list.extend(verificacao_data) #Inserir a lista dentro de outra
        views_list.append(views)
        anotacoes_trienio = anotacoes_trienio+1
    i=i+1

views_trienio = sum(views_list)

print("Canal:",nome_canal)
print("Total de views do trienio:",views_trienio)
print("Media de views do trienio:",format((views_trienio/anotacoes_trienio),'.2f'))

for k in range(2018,2021): #Loop chamando a funcão de 2018 a 2020
    views_anuais_totais,porcentagem_views,media = estatistica_anual(k)
    print("")
    print(k)
    print("Total:",views_anuais_totais)
    if views_trienio==0:
        print("Porcentagem das views do trienio:",porcentagem_views)
    else:
         print("Porcentagem das views do trienio:",format(porcentagem_views,'.2f'))
    print("Media:",format(media,'.2f'))
