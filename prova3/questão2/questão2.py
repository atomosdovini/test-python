def lista_ordenada(nums):
    lista_ordenada = 0
    i = 1
    while i < len(nums):
        if(nums[i] < nums[i - 1]):
            lista_ordenada = 1
        i += 1
    if lista_ordenada > 0:
        return False
    else:
        return True

def lista_par(nums):
    Pares = []
    for i in range(len(nums)):
        if (nums[i] % 2 == 0):
            Pares.append(nums[i])
    return Pares


def position(input):
    x = int(input)
    nums = []
    while x != 0:
        x, d = divmod(x, 10)
        nums.append(int(d))
    nums.reverse()
    return nums

def same(input):
    resultado = position(input)
    j = 0
    pos = 0
    for i in resultado:
        if int(i) == int(j):
            pos = pos+1
        j = j+1
    return pos

input = '3456'
if input.isdigit() == False:
    print(f'A entrada {input} não está do formato solicitado')   
else:
    pos = same(input)
    if pos > 0:
        print(f'Na entrada {input} há {pos} elementos com valor igual sua posição')
    if pos == 0:    
        print(f'Na entrada {input} não há elementos com valor igual sua posição')
    resultado = position(input)
    if lista_ordenada(resultado) == True:
        print (f'A entrada {input} está ordenada')
        lista_par = lista_par(resultado)
        print(f'A lista dos elementos pares de {input} em ordem de aparição é {lista_par}')
    if lista_ordenada(resultado) == False:
        print (f'A entrada {input} não está ordenada')
