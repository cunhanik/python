import random
num_random = random.randint(1,6)

print(num_random)
numero_tentativas = 0

while numero_tentativas < 3:
        tentativa = int(input("Tenta adivinhar o numero: "))
        numero_tentativas += 1
        if tentativa == num_random:
                print("Boa, conseguiste! ")
                break

print("Falhaste, tenta outra vez: ")