from array import array

#Arrays (Matriz)
    #Similar a listas
    #Melhor performance


letras = ['a','b','c','d']
numerosI = [10,20,30,40] 
numerosF = [1.2, 2.5, 3.1]

print(letras)
print(numerosF)
print(numerosI)

letras = array('u', ['a','b','c','d'])
numerosI = array('i',[10,20,30,40])
numerosF = array('f',[1.2, 2.5, 3.1])


print(letras)
print(numerosF)
print(numerosI)