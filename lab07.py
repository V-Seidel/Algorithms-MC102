# Lab07 - Listas e Strings
# Cliando um plano infalível e indescoblível

def codificar(i, frase, E):
    """Função que dado o número da linha i e a palavra é atribuido um valor codificado"""

    if i % 2 == 0:
        frase_invertida = frase[::-1]
        frase_final = ""
        for c in frase_invertida:
            c = str(ord(c)).zfill(E)
            c = oct(int(c))
            c = c[2:].zfill(E)
            frase_final = frase_final + str(c)
        return frase_final.upper()
    else:
        frase_final = ""
        for c in frase:
            c = str(ord(c)).zfill(E)
            c = hex(int(c))
            c = c[2:].zfill(E)
            frase_final = frase_final + str(c)
        return frase_final.upper()


def decodificar(i, frase, E):
    """Função que dado o número da linha i e a palavra é atribuido um valor decodificado"""

    if i % 2 == 0:
        frase_final = ""
        start, final = 0, E
        for c in frase[::E]:
            c = frase[int(start):int(final)].lower()
            c = int(c, 8)
            c = chr(c)
            frase_final = frase_final + str(c)
            start, final = start + E, final + E
        return frase_final[::-1]
    else:
        frase_final = ""
        start, final = 0, E
        for c in frase[::E]:
            c = frase[int(start):int(final)].lower()
            c = int(c, 16)
            c = chr(c)
            frase_final = frase_final + str(c)
            start, final = start + E, final + E
        return frase_final


M, E, L = input().split()
M, E, L = int(M), int(E), int(L)
# M=Modo do programa operar (1=Codificar, 2=Decodificar)
# E=Enxerto (Número de quantos caracteres decodificados devem representar o original)
# L=Número de linhas a mensagem codificada possui
i = 1
while i <= L:
    frase = str(input())

    if M == 1:
        print(codificar(i, frase, E))
    else:
        print(decodificar(i, frase, E))
    i = i+1
