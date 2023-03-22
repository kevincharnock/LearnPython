#List Comprehension


frutas1 = ['abacaxi','banana','maça','kiwi']

frutas2 = [iten for iten in frutas1 if 'b' in iten]
print(frutas2)


#Numeros
valores = []

#1for x in range(6):
#    valores.append(x*10)
#print(valores)    

valores = [x * 10 for x in range(6)]
print(valores)