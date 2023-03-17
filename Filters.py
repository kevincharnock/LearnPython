#Filter Function
    

valores = [2,5,3,12]

def remover20(x):
    return x>20
print(list(filter(remover20,valores)))

print(list(filter(lambda x: x<20,valores)))