#Map Function
    #Muito utilizado com listas
    #Aplicar função a um iterable, por item.

lista1 = [1,2,3,4]

def multi(x):
    return x*2

lista2 = map(multi,lista1)
print(list(lista2))


#Map com lambda
#lista2 = map(lambda x: x*2 ,lista1)
print(list(map(lambda x: x*2 ,lista1)))

