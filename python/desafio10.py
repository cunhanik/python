try:
    preco_produto = int(input("Qual é o preço do produto? : "))
except ValueError:
    print("O preço do produto é inválido.")

try:
    desconto = int(input("Qual é o desconto do produto? : "))
except ValueError:
    print("A percentagem do desconto é inválida.")
try:
    valor_final = preco_produto - preco_produto * (desconto/100)
    print("Tem a pagar: ", valor_final , "euros.")
except NameError:
    print("O programa não tem informação para calcular o desconto.")
