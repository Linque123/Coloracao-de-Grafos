# ============================================================
# COLORAÇÃO DE GRAFOS - ORGANIZAÇÃO DE HORÁRIOS DE PROVAS
# ============================================================
# Vértice = uma prova
# Aresta  = duas provas têm pelo menos um aluno em comum
#           (por isso não podem acontecer no mesmo horário)
# Cor     = um horário
# Objetivo: usar o MENOR número de horários sem nenhum conflito.
# ============================================================


# ------------------------------------------------------------
# DADOS DO PROBLEMA: quais provas cada aluno vai fazer
# ------------------------------------------------------------
alunos = {
    "Ana":   ["Matemática", "Programação", "Física"],
    "Bruno": ["Matemática", "Física", "Cálculo"],
    "Carla": ["Programação", "Estruturas de Dados", "Redes"],
    "Diego": ["Cálculo", "Estruturas de Dados"],
    "Eva":   ["Programação", "Redes"],
}


# ------------------------------------------------------------
# 1) MODELAGEM: transforma a tabela de alunos em um grafo
#    (lista de adjacência: prova -> lista de provas em conflito)
# ------------------------------------------------------------
def montar_grafo(alunos):
    grafo = {}

    for aluno in alunos:
        provas_do_aluno = alunos[aluno]

        # Toda prova vira um vértice do grafo
        for prova in provas_do_aluno:
            if prova not in grafo:
                grafo[prova] = []

        # Provas do mesmo aluno ficam ligadas por uma aresta
        for prova1 in provas_do_aluno:
            for prova2 in provas_do_aluno:
                if prova1 != prova2 and prova2 not in grafo[prova1]:
                    grafo[prova1].append(prova2)

    return grafo


# ------------------------------------------------------------
# Mostra o grafo modelado: cada prova, seu grau e seus conflitos
# ------------------------------------------------------------
def mostrar_grafo(grafo):
    soma_dos_graus = 0

    for prova in grafo:
        print(prova, "| grau", len(grafo[prova]), "| conflita com:", grafo[prova])
        soma_dos_graus = soma_dos_graus + len(grafo[prova])

    print("Total de provas (vértices):", len(grafo))
    print("Total de conflitos (arestas):", soma_dos_graus // 2)


# ------------------------------------------------------------
# Define a ordem de coloração: provas com MAIOR grau primeiro
# (as mais "difíceis" são resolvidas antes)
# ------------------------------------------------------------
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


# ------------------------------------------------------------
# Verifica se a prova pode receber essa cor (horário):
# nenhum vizinho pode estar usando a mesma cor
# ------------------------------------------------------------
def pode_usar_cor(grafo, cor_de, prova, cor):
    for vizinho in grafo[prova]:
        if cor_de[vizinho] == cor:
            return False
    return True


# ------------------------------------------------------------
# 2) BACKTRACKING: tenta colorir as provas, uma por vez,
#    usando no máximo k cores. Se travar, volta e troca.
# ------------------------------------------------------------
def colorir(grafo, ordem, cor_de, k, posicao):
    # Caso base: todas as provas já receberam um horário
    if posicao == len(ordem):
        return True

    prova = ordem[posicao]

    for cor in range(1, k + 1):
        if pode_usar_cor(grafo, cor_de, prova, cor):
            cor_de[prova] = cor
            print("  ", prova, "-> horário", cor)

            # Tenta colorir a próxima prova da ordem
            if colorir(grafo, ordem, cor_de, k, posicao + 1):
                return True

            # Não deu certo mais à frente: desfaz e tenta outra cor
            cor_de[prova] = None
            print("  ", prova, "desfaz horário", cor)

    print("  ", prova, "-> nenhum horário funcionou, VOLTANDO")
    return False


# ------------------------------------------------------------
# Procura o MENOR k: tenta com 1 horário, depois 2, depois 3...
# A primeira tentativa que funcionar é a coloração mínima.
# ------------------------------------------------------------
def coloracao_minima(grafo):
    ordem = ordenar_por_grau(grafo)
    print("Ordem de coloração (maior grau primeiro):", ordem)

    for k in range(1, len(grafo) + 1):
        print()
        print("Tentando com", k, "horário(s):")

        # Começa com todas as provas sem cor
        cor_de = {}
        for prova in grafo:
            cor_de[prova] = None

        if colorir(grafo, ordem, cor_de, k, 0):
            return cor_de, k


# ------------------------------------------------------------
# 3) PROVA REAL: confere se nenhuma aresta liga provas
#    que ficaram com a mesma cor
# ------------------------------------------------------------
def validar_coloracao(grafo, cor_de):
    for prova in grafo:
        for vizinho in grafo[prova]:
            if cor_de[prova] == cor_de[vizinho]:
                return False
    return True


# ------------------------------------------------------------
# Mostra a grade final: quais provas ficam em cada horário
# ------------------------------------------------------------
def mostrar_grade(cor_de, k):
    for horario in range(1, k + 1):
        print("Horário", horario)
        for prova in cor_de:
            if cor_de[prova] == horario:
                print("   -", prova)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
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
