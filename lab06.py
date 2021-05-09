# Tarefa de Laboratório 06 - Classes (Torneios de Cyberluta)

# H = Habilidade do medalutador ÚNICA em todo o torneio.
# Medapeças: Torso (Defesa), Braços esquerdo e direito (Ataque), Pernas (Defesa)
# Medalha: Bônus para o ataque e defesa.
# Ficha final: Atk + Def + Bonus

class Medalutador:
    """Classe Medalutador"""

    def __init__(self, ID, Hi, Ki, Ba, Bd, melhores_pecas):
        self.ID = ID
        self.melhores_pecas = melhores_pecas
        self.habilidade_maxima = int(Hi)
        self.habilidade_atual, self.recuperacao_atual = int(Hi), int(Ki)
        self.ponto_do_braco_e, self.ponto_do_braco_d, self.bonus_de_ataque = int(
            max(self.melhores_pecas['E'])), int(max(self.melhores_pecas['D'])), Ba
        self.pontos_do_torso, self.pontos_das_pernas, self.bonus_de_defesa = int(
            max(self.melhores_pecas['T'])), int(max(self.melhores_pecas['P'])), Bd
        self.pontos_de_ataque = self.ponto_do_braco_d + \
            self.ponto_do_braco_e + int(Ba)
        self.pontos_de_defesa = self.pontos_do_torso + \
            self.pontos_das_pernas + int(Bd)

    def update(self, melhores_pecas):
        """Função update para atualizar os pontos após cada batalha"""
        for tipo in ['E', 'D', 'T', 'P']:  # Verifica se o robô possui nenhuma peça em algum tipo
            if len(self.melhores_pecas[tipo]) == 0:
                self.melhores_pecas[tipo].append(0)

        self.ponto_do_braco_e = int(max(self.melhores_pecas['E']))
        self.ponto_do_braco_d = int(max(self.melhores_pecas['D']))
        self.pontos_do_torso = int(max(self.melhores_pecas['T']))
        self.pontos_das_pernas = int(max(self.melhores_pecas['P']))
        self.pontos_de_ataque = self.ponto_do_braco_d + \
            self.ponto_do_braco_e + int(self.bonus_de_ataque)
        self.pontos_de_defesa = self.pontos_do_torso + \
            self.pontos_das_pernas + int(self.bonus_de_defesa)

    def obter_ID(self):
        return self.ID

    def __repr__(self):
        return str(self.ID)

# ---------------------------------------------------------------------------------------


def imprimir_ficha_tecnica(i, j):
    """Função Imprimir ficha técnica com parâmetros i e j e retorno nulo"""
    print(f'\tA{i.ID} = E{i.ponto_do_braco_e} + D{i.ponto_do_braco_d} + {i.bonus_de_ataque} = {i.pontos_de_ataque}')
    print(f'\tD{i.ID} = T{i.pontos_do_torso} + P{i.pontos_das_pernas} + {i.bonus_de_defesa} = {i.pontos_de_defesa}')
    print(f'\tH{i.ID} = {i.habilidade_atual}')
    print(f'\tA{j.ID} = E{j.ponto_do_braco_e} + D{j.ponto_do_braco_d} + {j.bonus_de_ataque} = {j.pontos_de_ataque}')
    print(f'\tD{j.ID} = T{j.pontos_do_torso} + P{j.pontos_das_pernas} + {j.bonus_de_defesa} = {j.pontos_de_defesa}')
    print(f'\tH{j.ID} = {j.habilidade_atual}')


# ---------------------------------------------------------------------------------------


def batalhar(i, j):
    """Função para batalhar com parâmetros i e j e retorno do ganhador"""
    if (i.pontos_de_ataque > j.pontos_de_defesa or j.pontos_de_ataque > i.pontos_de_defesa) and i.pontos_de_ataque+i.pontos_de_defesa != j.pontos_de_ataque + j.pontos_de_defesa:
        if i.pontos_de_ataque+i.pontos_de_defesa > j.pontos_de_ataque + j.pontos_de_defesa:
            k, p = i, j
        else:
            k, p = j, i
    else:
        if i.habilidade_atual != j.habilidade_atual:
            if i.habilidade_atual > j.habilidade_atual:
                k, p = i, j
            else:
                k, p = j, i
        else:
            if i.ID < j.ID:
                k, p = i, j
            else:
                k, p = j, i

    medapecas = {'T': p.pontos_do_torso - k.pontos_do_torso, 'E': p.ponto_do_braco_e-k.ponto_do_braco_e,
                 'D': p.ponto_do_braco_d-k.ponto_do_braco_d, 'P': p.pontos_das_pernas-k.pontos_das_pernas}
    # Vê o tipo de medapeça ganha e qual o ponto
    global tipo_da_medapeca_ganha
    global pontos_da_medapeca_ganha
    tipo_da_medapeca_ganha = max(medapecas, key=medapecas.get)
    pontos_da_medapeca_ganha = max(p.melhores_pecas[tipo_da_medapeca_ganha])
    # Adiciona a peça ao robô vencedor (k) e retira do perdedor (p)
    k.melhores_pecas[tipo_da_medapeca_ganha].append(pontos_da_medapeca_ganha)
    p.melhores_pecas[tipo_da_medapeca_ganha].remove(pontos_da_medapeca_ganha)
    k.update(melhores_pecas)
    p.update(melhores_pecas)
    # Verifica a lógica das habilidades propostas no problema
    k.habilidade_atual = k.habilidade_atual-p.habilidade_atual
    if k.habilidade_atual < 0:
        k.habilidade_atual = 0
    p.habilidade_atual = p.habilidade_atual//2 + p.recuperacao_atual
    if p.habilidade_atual >= p.habilidade_maxima:
        p.habilidade_atual = p.habilidade_maxima
    k.habilidade_atual = k.habilidade_atual + k.recuperacao_atual
    if k.habilidade_atual >= k.habilidade_maxima:
        k.habilidade_atual = k.habilidade_maxima
    return k

# ----------------------------------------------------------------------------------


def imprimir_resultado_da_batalha(k):
    """Função que imprime o resultado da matalha com retorno nulo"""
    print(
        f'Medalutador {k} venceu e recebeu a {tipo_da_medapeca_ganha}{pontos_da_medapeca_ganha}\n')

# ---------------------------------Função Simulação torneio-------------------------------------------------


def simular_torneios_de_cyberlutas(lista_de_medalutadores):
    lista_torneio_principal = []
    lista_de_repescagem = []
    for medalutador in lista_de_medalutadores:
        lista_torneio_principal.append(medalutador)
    while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
        lista_torneio_principal = aplicar_rodada_de_batalhas(
            lista_torneio_principal, lista_de_repescagem)
        lista_de_repescagem = aplicar_rodada_de_batalhas(
            lista_de_repescagem, None)
    i = lista_torneio_principal.pop(0)
    j = lista_de_repescagem.pop(0)
    print('Cyberluta Final')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    print(f'Campeao: medalutador {k}')

# ---------------------------------Função para aplicar uma rodada-------------------------------------------------


def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
    if len(lista_de_medalutadores) < 2:
        return lista_de_medalutadores
    lista_de_vencedores = []
    while len(lista_de_medalutadores) >= 2:
        i = lista_de_medalutadores.pop(0)
        j = lista_de_medalutadores.pop(0)
        if i.obter_ID() > j.obter_ID():
            i, j = j, i
        if lista_de_repescagem != None:
            print('Cyberluta do Torneio Principal')
        else:
            print('Cyberluta da Repescagem')
        print(f'Medalutadores: {i} vs {j}')
        imprimir_ficha_tecnica(i, j)
        k = batalhar(i, j)
        imprimir_resultado_da_batalha(k)
        if lista_de_repescagem != None:
            if i == k:
                lista_de_repescagem.append(j)
            else:
                lista_de_repescagem.append(i)
        lista_de_vencedores.append(k)
    lista_de_vencedores.extend(lista_de_medalutadores)
    return lista_de_vencedores

# --------------------------------------------------------------------------------------------------------


lista_de_medalutadores = []

N = int(input())  # Número de robôs que terão no campeonato

for i in range(0, N):
    # Hi = Habilidade do robô; Ki = Recuperação do robô; Mi=Número de peças;
    Hi, Ki, Mi = input().split()
    # Bi = Bônus de ataque; Bd = Bônus de defesa;
    Ba, Bd = input().split()
    # Braço Esquerdo, Braço Direito, Torso, Pernas (Dicionário para armazenar os valores das peças)
    melhores_pecas = {'T': [], 'D': [], 'E': [], 'P': []}

    for j in range(0, int(Mi)):
        tipoMedapeca, pontos_medapeca = input().split()
        melhores_pecas[tipoMedapeca].append(pontos_medapeca)
    lista_de_medalutadores.append(
        Medalutador(i+1, Hi, Ki, Ba, Bd, melhores_pecas))

simular_torneios_de_cyberlutas(lista_de_medalutadores)
