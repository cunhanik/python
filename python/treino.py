class JogoMarado:

    def __init__(self,nome,vida,poder,stamina):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.stamina = stamina
    
    def morte(self):
        self.vida <= 0
        print("****FODEU-SE DE VEZ****")

    def descansar(self):
        print("A descansar...")
        self.vida += 20
        self.stamina += 10

    def atacar(self):
        print("A atacar...")
        self.stamina -= 20

    def recebe(self):
        print("-A ser fodido/a-")
        self.vida -= 30

    def move_esquerda(self):
        print("movendo para a esquerda...")

    def move_direita(self):
        print("movendo para a direita...")

    def move_baixo(self):
        print("movendo para baixo...")

    def move_cima(self):
        print("movendo para cima")