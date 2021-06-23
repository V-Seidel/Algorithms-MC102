# Tarefa de Laboratório 11 - Busca e Ordenação
# Ajudando a Yelena

# Função dado um ponto e uma lista de esconderijos calcula a maior distância
# Calcular mesma coisa para o mid+1
# Calcular o mesmo para mid-1

import math
hiding_places_coordinates_list = []
max_distance_list = []


def search_max_distance(max_distance_list, wall_coordinate):
    """Função que calcula a maior distância dado um ponto e uma lista de esconderijos"""
    max_distance = 0
    for j in range(0, len(max_distance_list)):
        distance = ((int(hiding_places_coordinates_list[j][0])) **
                    2) + ((int(hiding_places_coordinates_list[j][1])-wall_coordinate)**2)
        if distance > max_distance:
            max_distance = distance  # Pegando a maior distância
    return max_distance


def binarySearch(max_distance_list, wall_coordinate):
    """Algoritmo de busca binária que procura o valor da menor distância"""
    first = 1
    last = wall_coordinate

    while True:
        mid = (first+last)//2
        max_distance_mid = search_max_distance(max_distance_list, mid)
        max_distance_upper = search_max_distance(max_distance_list, mid+1)
        max_distance_lower = search_max_distance(max_distance_list, mid-1)

        if (max_distance_mid < max_distance_upper) and (max_distance_mid < max_distance_lower):
            return mid
        else:
            if max_distance_upper < max_distance_mid:
                first = mid
            else:
                last = mid


while True:

    # Entradas
    num_hiding_places, wall_coordinate = input().split()
    num_hiding_places, wall_coordinate = int(
        num_hiding_places), int(wall_coordinate)

    # Fim do programa
    if num_hiding_places == 0 and wall_coordinate == 0:
        break

    # Obtenção das coordenadas dos esconderijos
    for i in range(num_hiding_places):
        hiding_place_coordinate = input().split()
        hiding_places_coordinates_list.append(hiding_place_coordinate)

    print(binarySearch(hiding_places_coordinates_list, wall_coordinate))
    max_distance_list = []
    hiding_places_coordinates_list = []
