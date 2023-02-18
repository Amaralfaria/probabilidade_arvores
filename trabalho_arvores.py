class Tree:
    def __init__(self,raiz=None):
        self.raiz = raiz
        self.filhos = []
    
    def insert_node(self,node):
        self.filhos.append(Tree(node))

 
def gametree(tree,i=0):
    print(f'{i*"__"}{tree.raiz[0]}')
    for filho in tree.filhos:
        gametree(filho,i=i+1)


def probtree(arvore,i=0):
    def probabilidade(arvore):
        nonlocal vitorias,derrotas,empates
        if arvore.raiz[0] == 'V':
            vitorias += 1
        elif arvore.raiz[0] == 'D':
            derrotas += 1
        elif arvore.raiz[0] == 'E':
            empates += 1
        for filho in arvore.filhos:
            probabilidade(filho)


    vitorias = 0
    derrotas = 0
    empates = 0

    probabilidade(arvore)
    total = vitorias+derrotas+empates
    print(f'{".."*i}{arvore.raiz[0]} ({(vitorias/total)*100:.2f}%)')

    for filho in arvore.filhos:
        probtree(filho,i=i+1)
            


def monta_arvore(fila):
    while len(fila)>0:
        arvore = fila.pop(0)
        info = list(arvore.raiz.split())
        comando = info[0]
        qtd = int(info[1])

        for i in range(qtd):
            node = input()
            arvore.insert_node(node)
            fila.append(arvore.filhos[i])
            


arvore = Tree(input())
fila = []
fila.append(arvore)

monta_arvore(fila)
comando = input()

if comando == 'gametree':
    gametree(arvore)

if comando == 'probtree':
    probtree(arvore)

    
    