import itertools
from copy import deepcopy

pessoas = 4

def slice_by_lengths(lengths, the_list):
    for length in lengths:
        new = []
        for i in range(length):
            new.append(the_list.pop(0))
        yield new

def partition(number):
    return {(x,) + y for x in range(1, number) for y in partition(number-x)} | {(number,)}

def subgrups(my_list):
    partitions = partition(len(my_list))
    permed = []
    for each_partition in partitions:
        permed.append(set(itertools.permutations(each_partition, len(each_partition))))
    for each_tuple in itertools.chain(*permed):
        yield list(slice_by_lengths(each_tuple, deepcopy(my_list)))


def return_partition(my_list,num_groups):
    filtered=[]
    for perm in itertools.permutations(my_list,len(my_list)):
        # print(itertools.permutations(my_list,len(my_list)))
        for sub_group_perm in subgrups(list(perm)):
            if len(sub_group_perm)==num_groups:
                #sort  within each partition
                sort1=[sorted(i) for i in sub_group_perm]
                #sort by first element of each partition
                sort2=sorted(sort1, key=lambda t:t[0])
                #sort by the number of elements in each partition
                sort3=sorted(sort2, key=lambda t:len(t))
                #if this new sorted set of partitions has not been added, add it
                if sort3 not in filtered:
                    filtered.append(sort3)
    return filtered
#     # lista.append(pessoas[i])

lista = []
i = 0
while i < pessoas:
    i  = i + 1
    lista.append(i)



countj = 0
for j in return_partition(lista,1):
    countj = countj + 1
    print(j)


count = 0
for n in return_partition(lista,2):
    print(n)
    count = count + 1

print('iterativamente temos', count+countj)


