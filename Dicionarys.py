#Dicionarios
    #Utiliza index no formato de keys e value
    #Aceita Strings, Integer, float, boolean

             #Key   #Value
aluno =     {
    'nome':'Kevin',
    'idade':25,
    'notaFinal':'A',
    'aprovacao': True
 }

print(aluno)
print(aluno['nome'])

#Alterando Dicionario Simple Form
aluno['nome'] = 'Rafaella'
aluno['idade'] = 22
print(aluno)

#Update
aluno.update({'nome': 'kevin','idade':25})
print(aluno)

aluno.update({'endereço': 'rua A'})
print(aluno)

for keys, values in aluno.items():
    print(keys, values)