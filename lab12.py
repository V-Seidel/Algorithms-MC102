# Tarefa de Laboratório 12 - Recursão - Parte 1
# Artista digital
# Ajudar Smeargle a pintar coisas :)
# Método Iteração Recursiva

def distance(center_row, center_column, size, atual_position_x, atual_position_y, type, painting):
    """Função dado os parâmetros geométricos e o tipo da forma verifica se atende à lei geométrica"""
    if type == 'S':
        # Lei cartesiana para o quadrado (Square)
        if abs(atual_position_x-center_column) <= (size-1)/2 and abs(atual_position_y-center_row) <= (size-1)/2:
            painting[atual_position_y][atual_position_x] = 'x'
            return painting
    if type == 'C':
        # Lei cartesiana para o cículo (Circle)
        if (atual_position_x-center_column)**2 + (atual_position_y-center_row)**2 <= size**2:
            painting[atual_position_y][atual_position_x] = 'x'
        return painting
    return painting


def draw_circle(center_row, center_column, size, painting, atual_position_x, atual_position_y):
    """Função que dado o caso base chama a si mesma verificando cada item da matriz"""
    # Se a matriz chegou ao final retorna a pintura
    if atual_position_x == (len(painting[0])-1) and atual_position_y == (len(painting)-1):
        painting = distance(center_row, center_column, size,
                            atual_position_x, atual_position_y, 'C', painting)
        return painting
    # Se a matriz terminou a primeira linha reseta o x e chama novamente com y+1
    if atual_position_x == (len(painting[0])-1):
        painting = distance(center_row, center_column, size,
                            atual_position_x, atual_position_y, 'C', painting)
        return draw_circle(center_row, center_column, size, painting, 0, atual_position_y+1)
    else:
        painting = distance(center_row, center_column, size,
                            atual_position_x, atual_position_y, 'C', painting)
        return draw_circle(center_row, center_column, size, painting, atual_position_x + 1, atual_position_y)


def draw_square(center_row, center_column, size, painting, atual_position_x, atual_position_y):
    """Função que dado o caso base chama a si mesma verificando cada item da matriz"""
    # Se a matriz chegou ao final retorna a pintura
    if atual_position_x == (len(painting[0])-1) and atual_position_y == (len(painting)-1):
        painting = distance(center_row, center_column, size,
                            atual_position_x, atual_position_y, 'S', painting)
        return painting

    # Se a matriz terminou a primeira linha reseta o x e chama novamente com y+1
    if atual_position_x == (len(painting[0])-1):
        painting = distance(center_row, center_column, size,
                            atual_position_x, atual_position_y, 'S', painting)
        return draw_square(center_row, center_column, size, painting, 0, atual_position_y+1)

    else:
        painting = distance(center_row, center_column, size,
                            atual_position_x, atual_position_y, 'S', painting)
        return draw_square(center_row, center_column, size, painting, atual_position_x + 1, atual_position_y)


rows, columns = input().split()
rows, columns = int(rows), int(columns)

number_of_geometric_shapes = int(input())

# Criação da pintura em branco
painting = [['-' for x in range(columns)] for y in range(rows)]

for geometric_shape in range(number_of_geometric_shapes):
    shape, center_row, center_column, size = input().split()
    center_row, center_column, size = int(
        center_row), int(center_column), int(size)

    if shape == 'quadrado':
        painting = draw_square(center_row, center_column,
                               size, painting, 0, 0)
    if shape == 'circulo':
        painting = draw_circle(center_row, center_column,
                               size, painting, 0, 0)

# Apresentação da pintura final
for line in painting:
    for place in line:
        print(place, end=' ')
    print()
