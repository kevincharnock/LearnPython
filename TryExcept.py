#Erros
    #Excelente para testes
    #Mensagens customizadas


try:
    letras = ['a','b','c']
    print(letras[3])
except IndexError:
    print('Index não existe')

    #Try with input
try:  
    valor = int(input('Digite o valor do seu produto'))
    print(valor)     
except ValueError:
    print('Somente numerais')
    #Else Finally
else:
    print('Valor correto')
    resultado = valor * 2
    print(resultado)    

