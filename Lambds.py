#Lambda Function
    #Muito utilizada dentro de outras funções
    #codigo mais clean
    #pode ter varios argumentos mas somente 1 expressão

                #Args   
somar10 = lambda  x: x+10       
print(somar10(2))


somar20 = lambda x,y: x+y+10
print(somar20(4,6))


def multi():
    multi = lambda x: x*10
    return multi(2)