class Avatar:

    def __init__(self, nome, vida): #dinheiro
      
        self.nome = nome
        self.vida = vida 
        """da maneira que eu fiz em cima, signifca que todos os meus "selfs"
        vão ou podem ter um nome/vida diferente...
        Se eu quiser que tenha alguma caracteristica igual, é so fazer(ex dinheiro):"""
        self.dinheiro = 100

    def move_direita(self):
        self.vida -= 5
        print("move direita...")

    def move_esquerda(self):
        self.vida -= 5
        print("move esquerda...")

    def alimenta(self):
        self.vida += 5
        self.dinheiro -= 10
        print("alimentando...")

    def mostra_status(self):
        print("nome: ", self.nome)
        print("vida: ", self.vida)
        print("dinheiro: ", self.dinheiro)
