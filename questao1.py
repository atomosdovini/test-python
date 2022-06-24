from math import sqrt
import os
def getInfo(x1, y1, x2, y2):
   return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def solve(points):
   N = len(points)
   firstx, firsty = points[0]
   prevx, prevy = firstx, firsty
   res = 0

   for i in range(1, N):
      nextx, nexty = points[i]
      res = res + getInfo(prevx,prevy,nextx,nexty)
      prevx = nextx
      prevy = nexty
   res = res + getInfo(prevx,prevy,firstx,firsty)
   return res




filesize = os.path.getsize("Vazio.txt")

if filesize == 0:
    print("Arquivo de pontos está vazio!!!")
else:
        
    with open("Vazio.txt") as f:
        lines = f.readlines()
    coords = [tuple(map(int, line.split(" "))) for line in lines]
    x = (solve(coords))
    print('conteúdo no arquivo\n')
    for line in lines:
        print( line)
    print(f'\n\nPerímetro do polígono de pontos contidos no arquivo: {x:.2f}')


