# probabilidade_arvores
Algoritmo que calcula a probabilidade de vitória em um jogo a partir de arvores

probtree:
calculo da probabilidade de vitoria a partir de escolhas(que serão tratadas como nós).
inputs validos exemplos:
1-	? 2
2-	E 0
3-	? 2
4-	V 0
5-	E 0
probtree
explicaçao: 
1- o primeiro nó - possui dois fihos que serão lidos logo em seguida(E 0 e ? 2)
2 - resulta em derrota logo não possui filhos
3 - outro nó com filhos(2: V 0 e D 0)
4 - resulta em vitoria 
5 - resulta em empate

gametree: mostra as possibilidades de maneira um pouco mais visual
input: mesmo do probtree porem ultima linha devera ser gametree.
