lista = [1,2,3,4,5,5,4,3,2,1]
sem_duplicados =[]

for num in lista:
    if num not in sem_duplicados:
        sem_duplicados.append(num)
print(sem_duplicados)