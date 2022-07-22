romano_arabe = {
    "I" : 1,
    "II" : 2,
    "III" : 3,
    "IV" : 4,
    "V" : "5",
    "VI" : 6,
    "VII" : 7,
    "VIII" : 8,
    "IX" : 9,
    "X" : 10,
    "XI" : 11
}

numero = input("Introduz um numero romano: ")
texto = "O seu numero em árabe é: "
if numero not in romano_arabe:
    print("Simbolo errado. ")

else:
    arabe = romano_arabe.get(numero)
    print(f"({texto} {arabe}")
    