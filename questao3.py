from itertools import combinations

Entrada = 3
npos_it = 0
npos_rec = 0
narray = []

#funçoes iterativas
def partitionsIt(elements, size):
    elements = set(elements)
    assert(len(elements) % size == 0)
    if len(elements) == 0:
        yield ()
        return
    first = next(iter(elements))
    rest = elements.difference((first,))
    for c in combinations(rest, size - 1):
        first_subset = (first,) + c
        for p in partitionsIt(rest.difference(c), size):
            firstsub = (first_subset,) + p
            yield firstsub

def partitions_iter(elements, size): 
    elements = set(elements)
    for n in range(len(elements), -1, -size):
        if n == 0:
            for p in partitionsIt(elements, size):
                yield p
        elif n != size:
            for remainder in combinations(elements, n):
                for p in partitionsIt(elements.difference(remainder), size):
                    group = p + (remainder,)
                    yield group   
#funçoes recursivas
def partitions(elements, size):
    elements = set(elements)
    assert(len(elements) % size == 0)
    if len(elements) == 0:
        yield ()
        return
    first = next(iter(elements))
    rest = elements.difference((first,))
    for c in combinations(rest, size - 1):
        first_subset = (first,) + c
        for p in partitions(rest.difference(c), size):
            yield (first_subset,) + p

def partitions_rec(elements, size): 
    elements = set(elements)
    for n in range(len(elements), -1, -size):
        if n == 0:
            for p in partitions(elements, size):
                yield p
        elif n != size:
            for remainder in combinations(elements, n):
                for p in partitions(elements.difference(remainder), size):
                    yield p + (remainder)
def possibilities(groups):
    npos = 0
    while npos < len(groups):
        npos +=1
    return npos

def entrada():
    for n in range(Entrada):
        n = n +1
        narray.append(n)
    return narray   

narray = entrada()
groups= (list(partitions_iter(narray, 2)))
groupsrec= (list(partitions_rec(narray, 2)))
npos_rec = possibilities(groupsrec)
while npos_it < len(groups):
    npos_it +=1
#prints
print(f'iterativamente, temos {npos_it} possibilidades de jogos')
print(f'Recursivamente, temos {npos_rec} possibilidades de jogos')
