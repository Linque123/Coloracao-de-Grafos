alunos = {
    "Ana":   ["Matemática", "Programação", "Física"],
    "Bruno": ["Matemática", "Física", "Cálculo"],
    "Carla": ["Programação", "Estruturas de Dados", "Redes"],
    "Diego": ["Cálculo", "Estruturas de Dados"],
    "Eva":   ["Programação", "Redes"],
}


def montar_grafo(alunos):
    grafo = {}

    for aluno in alunos:
        provas_do_aluno = alunos[aluno]

        for prova in provas_do_aluno:
            if prova not in grafo:
                grafo[prova] = []

        for prova1 in provas_do_aluno:
            for prova2 in provas_do_aluno:
                if prova1 != prova2 and prova2 not in grafo[prova1]:
                    grafo[prova1].append(prova2)

    return grafo


def mostrar_grafo(grafo):
    soma_dos_graus = 0

    for prova in grafo:
        print(prova, "| grau", len(grafo[prova]), "| conflita com:", grafo[prova])
        soma_dos_graus = soma_dos_graus + len(grafo[prova])

    print("Total de provas (vértices):", len(grafo))
    print("Total de conflitos (arestas):", soma_dos_graus // 2)


def ordenar_por_grau(grafo):
    restantes = []
    for prova in grafo:
        restantes.append(prova)

    ordem = []
    while len(restantes) > 0:
        maior = None
        for prova in restantes:
            if maior is None or len(grafo[prova]) > len(grafo[maior]):
                maior = prova
        ordem.append(maior)
        restantes.remove(maior)

    return ordem


def pode_usar_cor(grafo, cor_de, prova, cor):
    for vizinho in grafo[prova]:
        if cor_de[vizinho] == cor:
            return False
    return True


def colorir(grafo, ordem, cor_de, k, posicao):
    if posicao == len(ordem):
        return True

    prova = ordem[posicao]

    for cor in range(1, k + 1):
        if pode_usar_cor(grafo, cor_de, prova, cor):
            cor_de[prova] = cor
            print("  ", prova, "-> horário", cor)

            if colorir(grafo, ordem, cor_de, k, posicao + 1):
                return True

            cor_de[prova] = None
            print("  ", prova, "desfaz horário", cor)

    print("  ", prova, "-> nenhum horário funcionou, VOLTANDO")
    return False


def coloracao_minima(grafo):
    ordem = ordenar_por_grau(grafo)
    print("Ordem de coloração (maior grau primeiro):", ordem)

    for k in range(1, len(grafo) + 1):
        print()
        print("Tentando com", k, "horário(s):")

        cor_de = {}
        for prova in grafo:
            cor_de[prova] = None

        if colorir(grafo, ordem, cor_de, k, 0):
            return cor_de, k


def validar_coloracao(grafo, cor_de):
    for prova in grafo:
        for vizinho in grafo[prova]:
            if cor_de[prova] == cor_de[vizinho]:
                return False
    return True


def mostrar_grade(cor_de, k):
    for horario in range(1, k + 1):
        print("Horário", horario)
        for prova in cor_de:
            if cor_de[prova] == horario:
                print("   -", prova)


grafo = montar_grafo(alunos)

print("=== 1) GRAFO MODELADO ===")
mostrar_grafo(grafo)

print()
print("=== 2) BUSCA PELA COLORAÇÃO MÍNIMA (backtracking) ===")
cor_de, k = coloracao_minima(grafo)

print()
print("=== 3) RESULTADO ===")
print("Menor número de horários:", k)
mostrar_grade(cor_de, k)

print()
if validar_coloracao(grafo, cor_de):
    print("Verificação: nenhuma prova em conflito ficou no mesmo horário. OK!")
else:
    print("Verificação: ERRO, existem provas em conflito no mesmo horário.")
