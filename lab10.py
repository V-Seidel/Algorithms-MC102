# Tarefa de Laboratório 10 - Combinando e Usando Estruturas de Dados
# Descobrindo o suspeito de um crime
# Serviço prestado à MAGAMI


def collect_dossier():
    """Função para tratar as entradas e criar a lista de suspeitos
    com suas características e as evidências retornando os mesmos"""
    # Variável temporária
    suspect_information = {}
    # Variável de retorno
    suspects = []
    evidence_information = {}
    while True:
        # Lê a entrada e divide em uma tupla
        input_suspect = input().partition(': ')

        if input_suspect[0] == '-':
            suspects.append(suspect_information)
            suspect_information = {}
            continue

        if input_suspect[0] == '--':
            suspects.append(suspect_information)
            while True:
                input_evidence = input().partition(': ')

                if input_evidence[0] == '---':
                    return suspects, evidence_information

                evidence_information[input_evidence[0]] = input_evidence[2]

        # Salva a Tupla encontrada em Key e Value
        suspect_information[input_suspect[0]] = input_suspect[2]


suspects, evidence_information = collect_dossier()

final_suspects = []

for suspect in suspects:
    # Checa se o as evidências são um subconjunto do suspeito
    if evidence_information.items() <= suspect.items():
        final_suspects.append(suspect.get('Nome'))

if len(final_suspects) == 0:
    print("Nenhum suspeito(a) com essas caracteristicas foi identificado(a).")

if len(final_suspects) == 1:
    print("Suspeito(a):")
    print(final_suspects[0])

if len(final_suspects) > 1:
    print("Suspeitos(as):")
    final_suspects = sorted(final_suspects)
    for i in range(len(final_suspects)):
        print(final_suspects[i])
