# Functions 
    #DRY - Don't repeat yourself

    #USE DEF TO CREATE A NEW FUNCTION (method)


def twoNumbers():
    num1 = 10
    num2 = 5
    result = num1+num2
    print ('test')
    print(result)

twoNumbers() 


def welcome(name='kevin', quantity=0): #Parametros
    print(f'hello, {name}.')
    print(f'We have {str(quantity)} of ice cream')

welcome('Tiberio',2) #argumentos
welcome('Yume',4) #argumentos
welcome('Rog',1) #argumentos



#Realiza tarefa
def doTask(secondName):
    print(f'Your second name is: {secondName}')
doTask('Charnock')    

#Calcula e retorna valor
def doTaskTwo(age):
    return f'Your age: {age}'

print(doTaskTwo('25'))



#Many arguments(xargs)
def soma(*numeros):
    result = 0
    for num in numeros:
        result +=num
    return result    
x = soma(2,3,4,8)
print(x)
