
#Armazenar Mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável.

citys = ['Hell de Janeiro', 'Cidade da Garoa', 'Oz']
print(citys)

#remove
citys.remove('Oz')
print(citys)

#Append adiciona final da lista
#Insert inicio da lista


#Manipulando listas positivos
numerais = [2,3,6,25]
print(numerais[0])


#Manipulando listas Negativas
Others = [2,3,6,'peixe',22]
print(Others[-2])

#Concatenando Listas
final = numerais+Others
print(final)

numerais.extend(citys)
print(numerais)

#Lista sobre Lista
itens = [[1,2,3,],[4,5]]
print(itens)
print(itens[0])
print(itens[0][2])


#Unpacking Lists
produto = ['Arroz', 'feijão', 'laranja', 'banana']

item0, item1, item2, *outros = produto

print(item0)
print(item1)
print(item2)
print(outros)

#forLoops
valores = [0,50,24,31]

for x in valores:
    print(x)


#Listas condicionais
corCliente = input('Qual cor?')
cores = ['amarelo','vermelho','azul','magenta']

if corCliente.lower in cores:
    print('sim')
else:
    print('não temos esta cor no momento')    


var = list('comprar')
print(var)


food = ['dog', 'banana', 'burg']
drinks = ['soda','refri']

twoLists = zip(food, drinks)
print(list(twoLists))