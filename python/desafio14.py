from desafio14def import perguntas


pergunta1 = perguntas
pergunta2 = perguntas
pergunta3 = perguntas
pergunta4 = perguntas


primeiro_ministro = print("Quem é o primeiro ministro de PT? : ")
Opcao_A = "A" or "a"
Opcao_B = "B" or "b"
Opcao_C = "C" or "c"
Opcao_D = "D" or "d"
pergunta1.respostas1()
pergunta = input("Qual destas opções está correta? : ")
if len(pergunta) > 1:
    print("Resposta inválida.")

print("=" * 20)

capital_pt = print("Qual é a capital de PT? : ")
Opcao_A2 = "A" or "a"
Opcao_B2 = "B" or "b"
Opcao_C2 = "C" or "c"
Opcao_D2 = "D" or "d"
pergunta2.respostas2()
pergunta2 = input("Qual destas opções está correta? : ")
if len(pergunta2) > 1:
    print("Resposta inválida.")

print("=" * 20)

presidente_pt = print("Quem é o presidente de PT? : ")
Opcao_A = "A" or "a"
Opcao_B = "B" or "b"
Opcao_C = "C" or "c"
Opcao_D = "D" or "d"
pergunta3.respostas3()
pergunta3 = input("Qual destas opções está correta? : ")
if len(pergunta3) > 1:
    print("Resposta inválida.")

print("=" * 20)

capital_fr = print("Qual é a capital de FR? : ")
Opcao_A = "A" or "a"
Opcao_B = "B" or "b"
Opcao_C = "C" or "c"
Opcao_D = "D" or "d"
pergunta4.respostas4()
pergunta4 = input("Qual destas opções está correta? : ")
if len(pergunta4) > 1:
    print("Resposta inválida.")


if pergunta == Opcao_A:
    certa = 1
else:
    certa = 0

if pergunta2 == Opcao_B2:
    certa2 = 1
else:
    certa2 = 0
if pergunta3 == Opcao_C:
    if len(pergunta3) > 1:
        print("Resposta inválida.")
    certa3 = 1
else:
    certa3 = 0
if pergunta4 == Opcao_D:
    if len(pergunta4) > 1:
        print("Resposta inválida.")    
    certa4 = 1
else:
    certa4 = 0

all = certa + certa2 + certa3 + certa4
print(f"Acertaste {all} respostas!")