# Tarefa de Laboratório 13 - Recursão - Parte 2
# Magias em área
# Missão: Achar Celéstia e derrotar o Boss Garlon
global magic_list
magic_list = []


def areaMagic(biggest_side, short_side, magic_list):
    """"Função que dado o lado maior e o menor calcula a maior magia possível"""
    if short_side > biggest_side:
        short_side, biggest_side = biggest_side, short_side
    i = 0

    if short_side == 0:
        biggest_side = 0

    if biggest_side == 0 and short_side == 0:
        return 0
    else:
        while short_side >= 1 and biggest_side >= 1:
            size = 2**i
            if size == short_side:
                magic_list.append(i)
                # Chama a função novamente dividindo em dois retângulos
                return areaMagic(short_side-size, size, magic_list), areaMagic(biggest_side-size, short_side, magic_list)
            if size > short_side:
                size = 2**(i-1)
                magic_list.append(i-1)
                # Chama a função novamente dividindo em dois retângulos
                return areaMagic(short_side-size, size, magic_list), areaMagic(biggest_side-size, short_side, magic_list)
            i += 1


rows, columns = input().split()
rows, columns = int(rows), int(columns)

areaMagic(rows, columns, magic_list)
print("---")
print("Grimorio de Teraf L'are")
print("---")
# Contador de quantas magias foram utilizadas
for magic in range(0, max(magic_list)+1):
    number_of_magics = magic_list.count(magic)
    if number_of_magics > 0:
        print(number_of_magics, "submagia(s) de nivel", magic)
print("---")
print("Total de submagia(s) conjurada(s):", len(magic_list))
# Cálculo do PM gasto por todas as magias
magic_points = 0
for magic in range(0, len(magic_list)):
    magic_points = magic_points + 2**magic_list[magic]
print("Total de PM gasto:", magic_points)
print("---")
