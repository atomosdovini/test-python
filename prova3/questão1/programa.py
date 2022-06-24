from math import sqrt

try:
    with open("cordenadas.txt") as f:
        cordenadas = f.readlines()
    pontos = [tuple(map(int, cordenada.split(" "))) for cordenada in cordenadas]
    tamanho = len(pontos)
    primeirox, firsty = pontos[0]
    x1, y1 = primeirox, firsty
    perimetro = 0
    def raiz(x1, y1, x2, y2):
        return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    for i in range(1, tamanho):
        x2, y2 = pontos[i]
        perimetro = perimetro + raiz(x1,y1,x2,y2)
        x1 = x2
        y1 = y2
    perimetro = perimetro + raiz(x1,y1,primeirox,firsty)
    cordenada=0
    while cordenada < len(cordenadas):
        print(cordenadas[cordenada])
        cordenada = cordenada +1
    print(f'\n\nPerímetro do polígono de pontos contidos no arquivo: {perimetro:.2f}')
except:
    print("Arquivo de pontos está vazio!!!")


