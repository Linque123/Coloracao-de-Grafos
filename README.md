# Coloração de Grafos em Python

Seminário AV2 — Grafos. Tema: **Coloração de grafos**.

## Equipe

| Nome | Matrícula |
|---|---|
| Carlos Henrique Almeida | 2320315 |
| Caio Alves | 2322593 |

## Problema

Organizar os horários das provas de uma universidade usando o **menor número de horários possível**, sem que nenhum aluno tenha duas provas ao mesmo tempo.

## Modelagem

| Elemento do grafo | Significado no problema |
|---|---|
| Vértice | Uma prova |
| Aresta | As duas provas têm pelo menos um aluno em comum |
| Cor | Um horário |
| Número cromático χ(G) | Menor número de horários sem conflito |

O grafo **não é digitado à mão**: ele é gerado a partir da tabela `alunos`, que diz quais provas cada aluno faz. Todas as provas de um mesmo aluno ficam ligadas entre si.

## Algoritmo

O programa usa **backtracking** (busca com retrocesso):

1. Ordena as provas pelo grau, da maior para a menor.
2. Tenta colorir o grafo com 1 cor, depois com 2, depois com 3, e assim por diante.
3. Em cada tentativa, dá a cada prova a primeira cor que nenhum vizinho está usando.
4. Se uma prova não tiver nenhuma cor possível, o algoritmo **volta**, desfaz a escolha anterior e tenta outra cor.
5. O primeiro número de cores que funcionar é o mínimo.

O método é **exato**: sempre encontra o menor número de horários. O custo no pior caso é exponencial, por isso ele é indicado para grafos pequenos e médios.

## Requisitos

- Python 3 (qualquer versão recente)
- Nenhuma biblioteca externa

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python coloracao_grafos.py
```

Em alguns sistemas, o comando é `python3 coloracao_grafos.py`.

## O que o programa mostra

1. **Grafo modelado:** cada prova com seu grau e a lista de provas com que conflita, além do total de vértices e arestas.
2. **Busca passo a passo:** cada cor atribuída, cada escolha desfeita e cada volta do backtracking, para 1, 2, 3… horários.
3. **Resultado:** o menor número de horários, a grade final e a verificação de que nenhuma prova em conflito ficou no mesmo horário.

Para o exemplo incluído, o resultado é **3 horários**. Duas cores não bastam porque Matemática, Programação e Física formam um triângulo: cada uma conflita com as outras duas.

## Como adaptar para outro cenário

Edite o dicionário `alunos` no início do arquivo:

```python
alunos = {
    "Ana": ["Matemática", "Programação", "Física"],
    "Novo aluno": ["Prova X", "Prova Y"],
}
```

O nome de cada prova precisa ser escrito sempre do mesmo jeito, com os mesmos acentos e maiúsculas. Nada mais precisa ser alterado.
