from treino import JogoMarado

bot1 = JogoMarado("Cunha",100,"Cagar anões",50)
bot2 = JogoMarado("Bea",100,"discutir",50)
bot3 = JogoMarado("Jay",100,"Rouba stamina",50)
bot4 = JogoMarado("nuck",100,"Apaixonar",50)
bot5 = JogoMarado("piruças",100,"Mandar tachos",50)
bot6 = JogoMarado("bininho",100,"Falar de motas e adormecer toda a gente",50)
bot7 = JogoMarado("mvc",100,"Manda pêlo",50)
bot8 = JogoMarado("Gonçalo",100,"Duplicar-se",50)
bot9 = JogoMarado("lekas",100,"berrar",50)
bot10 = JogoMarado("Caldas",100,"Mandar polvos",50)
bot11 = JogoMarado("xico",100,"Bafo de droga",50)
bot12 = JogoMarado("tixa",100,"Caga anão com picos",50)


print("""            PRIMEIRO COMBATE:

                              bot1 VS bot2 """)
print(bot1.nome)
print("VS")    
print(bot2.nome)   
print("=" *20)                      
print("Cunha: ")
print(bot1.poder)
bot1.atacar()
print("Bea: ")
bot2.recebe()
print("=" *20)
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("=" *20)
print("Bea: ")
print(bot2.poder)
bot2.atacar()
print(bot2.poder)
bot2.atacar()
print(bot2.poder)
bot2.atacar()
print("Cunha: ")
bot1.recebe()
bot1.recebe()
bot1.recebe()
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("=" *20)
print("Cunha: ")
bot1.descansar()
bot1.descansar()
print("Bea: ")
bot2.descansar()
print("=" *20)
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("=" *20)
print("Cunha: ")
print(bot1.poder)
bot1.atacar()
print(bot1.poder)
bot1.atacar()
print("Bea: ")
bot2.recebe()
bot2.recebe()
print("=" *20)
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("=" *20)
print("Cunha: ")
bot1.descansar()
print("Bea:")
bot2.descansar()
bot2.descansar()
print("=" *20)
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("=" *20)
print("Cunha: ")
print(bot1.poder)
bot1.atacar()
print("Bea: ")
bot2.recebe()
print("Bea: ")
print(bot2.poder)
bot2.atacar()
print(bot2.poder)
bot2.atacar()
print("Cunha: ")
bot1.recebe()
bot1.recebe()
print("=" *20)
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("=" *20)
print("Cunha: ")
print(bot1.poder)
bot1.atacar()
print("Bea: ")
bot2.recebe()
print("Cunha: ")
bot1.descansar()
print("Bea: ")
bot2.atacar()
print("Cunha: ")
bot1.recebe()
print("=" *20)
print("Vida: ")
print("Cunha: ", bot1.vida)
print("Bea: ", bot2.vida)
print("       Cunha ")
bot1.morte()
print("******       Bea ganhou!!!!!!!         ******")




"""Comandos uteis:
X = nome do bot
y = numero do bot
=============================
=============================
y.atacar()
y.recebe()
y.move_esquerda()
y.move_direita()
y.move_cima()
y.move_baix()
y.descansar()
y.morte()
print("poder X:, y.poder)
print("stamina X:, y.stamina)
print("nome X: ", y.nome)
print("vida X: ", y.vida)
"""