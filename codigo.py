disciplinas_ids = [
    'icc', 'calculoI', 'gaal', 'empreendedorismo',
    'algProgramacao', 'calculoVV', 'algLinearComputacional', 'sistemasDigitais', 'matDiscreta',
    'aeds', 'gerenciaProjetos', 'metodologiaCient', 'arquiteturaI', 'introducaoTeoriaGrafos',
    'tecnicasBuscaOrdenacao', 'uceI', 'probEstatistica', 'arquiteturaII', 'poo',
    'organizacaoSistemasArquivos', 'pesquisaOperacional', 'engenhariaSoftware', 'sistemasOperacionais', 'desenvolvimentoWeb', 'projetoAnaliseAlg',
    'bancoDados', 'uceII', 'paradigmasProgramacao', 'algoritmosGrafos', 'complexidadeProblemasAproximacao',
    'gerenciamentoAplicacoesBD', 'computacaoGrafica', 'sistemasDistribuidos', 'redesComputadores', 'linguagensFormaisAutomatos',
    'introducaoIA', 'informaticaEticaSociedade', 'compiladores', 'optativaI',
    'projetoEstagioConclusaoCurso', 'optativaII', 'uceIII',
    'administracao', 'optativaIII',
]

# regras: cada item = {'requisitos': [índices], 'libera': índice}
regras = [
    {'requisitos': [0], 'libera': 4},
    {'requisitos': [1], 'libera': 5},
    {'requisitos': [2], 'libera': 6},
    {'requisitos': [4], 'libera': 9},
    {'requisitos': [4], 'libera': 20},
    {'requisitos': [5], 'libera': 16},
    {'requisitos': [6, 9], 'libera': 31},
    {'requisitos': [7], 'libera': 12},
    {'requisitos': [8], 'libera': 13},
    {'requisitos': [8, 14], 'libera': 24},
    {'requisitos': [8], 'libera': 34},
    {'requisitos': [9], 'libera': 14},
    {'requisitos': [9], 'libera': 25},
    {'requisitos': [9], 'libera': 27},
    {'requisitos': [9], 'libera': 35},
    {'requisitos': [9, 17, 34], 'libera': 37},
    {'requisitos': [9], 'libera': 18},
    {'requisitos': [9], 'libera': 19},
    {'requisitos': [12], 'libera': 17},
    {'requisitos': [12], 'libera': 22},
    {'requisitos': [13, 24], 'libera': 28},
    {'requisitos': [18], 'libera': 21},
    {'requisitos': [18], 'libera': 23},
    {'requisitos': [19, 25], 'libera': 30},
    {'requisitos': [21, 23], 'libera': 26},
    {'requisitos': [22], 'libera': 32},
    {'requisitos': [24], 'libera': 29},
]

sem_requisitos = [0, 1, 2, 3, 7, 8, 10, 11, 15, 33, 36, 38, 39, 40, 41, 42, 43]

selecionadas = set()

def atualiza_liberadas():
    liberadas = set()
    for idx in sem_requisitos:
        if idx not in selecionadas:
            liberadas.add(idx)
    for regra in regras:
        if all(pr in selecionadas for pr in regra['requisitos']):
            if regra['libera'] not in selecionadas:
                liberadas.add(regra['libera'])
    return liberadas

def mostra_estado():
    print("\nDisciplinas já concluídas:")
    for idx in selecionadas:
        print(f"  - {disciplinas_ids[idx]}")
    liberadas = atualiza_liberadas()
    print("\nDisciplinas disponíveis para matrícula:")
    for idx in liberadas:
        print(f"  - {disciplinas_ids[idx]}")
    print()

def main():
    global selecionadas
    print("Simulador de fluxo de disciplinas: Digite o nome da disciplina concluída ou ENTER para sair.")
    while True:
        mostra_estado()
        entrada = input("Digite disciplina concluída: ").strip()
        if not entrada:
            print("Encerrando.")
            break
        try:
            idx = disciplinas_ids.index(entrada)
            selecionadas.add(idx)
        except ValueError:
            print("Disciplina não reconhecida.")

if __name__ == "__main__":
    main()
