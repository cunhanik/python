try:
    idade = int(input("idade: "))
    print(idade)
except ValueError:
    print("A idade introduzida não é válida!")
print("FIM.")