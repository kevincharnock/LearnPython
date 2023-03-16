#Set (Listas)
    #Quando converte de lista pra set perde a indexição


list1 =[10,20,30]
list2 = [10,40,63]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union
print(num1 - num2) #Difference
print(num1 ^ num2) #Symetric Difference
print(num1 & num2) # And


