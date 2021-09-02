num = 4
text = ['code', 'aaagmnrs', 'anagrams', 'doce'] 
test = ''
vet = []
aux = text
for i in range(num):
    
    print(aux)
    
    for word in text:
        print(f"Aux: {aux[i]} e Sorted: {sorted(word)}")
        if sorted(aux[i]) == sorted(word):
            test += aux[i] + ' '
    aux[i] = '{i}'
print(f"Teste = {test}")