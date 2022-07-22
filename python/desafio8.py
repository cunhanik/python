dicionario = {
    "1" : "um",
    "2" : "dois",
    "3" : "três",
    "4" : "quatro",
    "5" : "cinco"
}
numeros_utilizador = input("Escreve os numeros : ")
texto = ""
for num in numeros_utilizador:
    texto = texto + dicionario.get(num) + " "
print(texto)