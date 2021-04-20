material = str(input())
pontoFusao = float(input())
pontoEbulicao = float(input())
tempAtual_fahrenheit = float(input())
tempAtual_celsius = round((tempAtual_fahrenheit-32)*(5/9), 2)


while (pontoEbulicao<=pontoFusao):
    pontoEbulicao = float(input("Insira um ponto de ebulicao valido:"))

if (tempAtual_celsius<pontoFusao) and (tempAtual_celsius>-273.15):
    estado = "Solido"

elif (tempAtual_celsius>=pontoFusao) and (tempAtual_celsius<pontoEbulicao):
    estado = "Liquido"

elif (tempAtual_celsius>=pontoEbulicao):
    estado = "Gasoso"

else:
    estado = "Abaixo do 0 absoluto"

print("Material:",material)
print("Ponto de fusao (Celsius):",format(pontoFusao,'.2f'))
print("Ponto de ebulicao (Celsius):",format(pontoEbulicao,'.2f'))
print("Temperatura atual (Celsius):",format(tempAtual_celsius,'.2f'))
print("Estado fisico do material:",estado)