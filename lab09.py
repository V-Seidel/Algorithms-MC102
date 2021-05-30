# Lab09 - Matrizes
# Supermatriz Comum
# Fatores/Resultados observados:
# Num. de L/C da SuperM = Num. de L/C Matrix n + Num. de L/C Matrix m - Num.de L/C da Interseção de m e n

def number_commum_elements(matrix_number_1, matrix_number_2):
    """Função que recebe duas matrizes e retorna uma matriz de interseção entre elas"""
    intersection_matrix = []
    for i in range(len(matrix_number_1)):
        for j in range(len(matrix_number_2)):
            temp = set(matrix_number_2[j])
            intersection_row = [x for x in matrix_number_1[i] if x in temp]
            intersection_matrix.append(intersection_row)
    return intersection_matrix


def commum_supermatrix(matrix_number_1, matrix_number_2, order_number_1, order_number_2):
    """Dada duas matrizes, a ordem da supermatriz é dada pela fórmula observada e escrita na linha 4"""

    if matrix_number_2 > matrix_number_1:
        matrix_number_1, matrix_number_2 = matrix_number_2, matrix_number_1

    intersection_matrix = number_commum_elements(
        matrix_number_1, matrix_number_2)
    intersection_matrix = [x for x in intersection_matrix if x]

    intersection_rows = len(intersection_matrix)
    intersection_columns = len(intersection_matrix[0])

    supermatrix_row = order_number_1 + order_number_2 - intersection_rows
    supermatrix_column = order_number_1 + order_number_2 - intersection_columns

    return supermatrix_row, supermatrix_column


while True:
    order_number_1, order_number_2 = input().split()
    order_number_1, order_number_2 = int(order_number_1), int(order_number_2)
    if order_number_1 == 0 and order_number_2 == 0:
        break

    # Comandos para a primeira matriz
    matrix_number_1 = []
    for i in range(order_number_1):
        x = list(map(int, input().split()))
        matrix_number_1.append(x)

    # Comandos para a segunda matriz
    matrix_number_2 = []
    for i in range(order_number_2):
        x = list(map(int, input().split()))
        matrix_number_2.append(x)

    supermatrix_row, supermatrix_column = commum_supermatrix(
        matrix_number_1, matrix_number_2, order_number_1, order_number_2)
    print(supermatrix_row, "x", supermatrix_column)
