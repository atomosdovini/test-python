entrada = '1234'

if entrada.isdigit() == False:
    print(f'A entrada {entrada} não está do formato solicitado')   
else:

    def check_position(entrada):
        x = int(entrada)
        valores = []
        while x != 0:
            x, d = divmod(x, 10)
            valores.append(int(d))
        valores.reverse()
        return valores

    def equal_position(entrada):
        resultado = check_position(entrada)
        j = 0
        posicao_igual = 0
        for i in resultado:
            if int(i) == int(j):
                posicao_igual = posicao_igual+1
            j = j+1
        return posicao_igual

    def ordenada(valores):
        ordenada = 0
        i = 1
        while i < len(valores):
            if(valores[i] < valores[i - 1]):
                ordenada = 1
            i += 1
        if ordenada > 0:
            return False
        else:
            return True

    def lista_par(valores):
        Pares = []
        for i in range(len(valores)):
            if (valores[i] % 2 == 0):
                Pares.append(valores[i])
        return Pares

     
    resultado = check_position(entrada)
    if ordenada(resultado) == True:
        print (f'A entrada {entrada} está ordenada')
        lista_par = lista_par(resultado)
        print(f'A lista dos elementos pares de {entrada} em ordem de aparição é {lista_par}')

    if ordenada(resultado) == False:
        print (f'A entrada {entrada} não está ordenada')

    posicao_igual = equal_position(entrada)
    if posicao_igual > 0:
        print(f'na entrada {entrada} há {posicao_igual} elementos com valor igual sua posição')
    if posicao_igual == 0:    
        print(f'na entrada {entrada} não há elementos com valor igual sua posição')

