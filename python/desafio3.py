nota = int(input("Qual foi a tua nota? : "))
if nota < 50:
    print("Insuficiente.")
elif nota < 70:
    print("Suficiente.")
elif nota < 90:
    print("Bom.")
elif nota > 100:
    print("Nota inválida")
else:
    print("Parabens, muito bom!") 