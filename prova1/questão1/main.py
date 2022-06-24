from math import sqrt
import os


with open("valores.txt") as f:
    linhas = f.readlines()
    print('conteúdo no arquivo\n')

    
filesize = os.stat('valores.txt')
if filesize.st_size == 0:
    print("Arquivo de pontos está vazio!!!")
else:  
    pontos = [tuple(map(int, linha.split(" "))) for linha in linhas]
    tamanho = len(pontos)
    primeirox, firsty = pontos[0]
    anteriorx, anteriory = primeirox, firsty
    perimetro = 0
    for i in range(1, tamanho):
        proximox, proximoy = pontos[i]
        perimetro = perimetro + sqrt((anteriorx-proximox)*(anteriorx-proximox)+(anteriory-proximoy)*(anteriory-proximoy))
        anteriorx = proximox
        anteriory = proximoy
    perimetro = perimetro + sqrt((anteriorx-primeirox)*(anteriorx-primeirox)+(anteriory-firsty)*(anteriory-firsty))
    linha=0
    while linha < len(linhas):
        print(linhas[linha])
        linha = linha +1
    print(f'\n\nPerímetro do polígono de pontos contidos no arquivo: {perimetro:.2f}')


