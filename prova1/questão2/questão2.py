myVariable = input('enter a number\n')

x = myVariable.isdigit()

if x == False:
    print(f'A entrada {myVariable} não está do formato solicitado')    
else:
    x = int(myVariable)
    result = []
    while x != 0:
        x, d = divmod(x, 10)
        result.append(int(d))
    result.reverse()

    j = 0
    k = 0
    for i in result:
        if i == j:
            k = k+1
        j = j+1
    if k > 0:
        if k > 1:
            s = 'elementos'
        else:    
            s = 'elemento'
        print(f'na entrada {myVariable} há {k} {s} com valor igual sua posição')
    if k == 0:    
        print(f'na entrada {myVariable} não há elementos com valor igual sua posição')

    flag = 0
    i = 1
    while i < len(result):
        if(result[i] < result[i - 1]):
            flag = 1
        i += 1

        
    Pares = []
    for i in range(len(result)):
        if (result[i] % 2 == 0):
            Pares.append(result[i])
 
    # printing result
    if (not flag) :
        print (f'A entrada {myVariable} está ordenada')
        print(f'A lista dos elementos pares de {myVariable} em ordem de aparição é {Pares}')

        
    else :
        print (f'A entrada {myVariable} não está ordenada')
        # if i < result[j]:
        #     print(print(f'a entrada {myVariable} nao está ordenada') )
