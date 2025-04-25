class Jogador:
    def __init__(self, vida, forca):
        self.vida = vida  
        self.forca = forca
        print(f"O jogador foi criado com sucesso")

    def atacar(self, inimigo):
        print(f"Player - Estou atacando o inimigo {inimigo.nome}.")

class Inimigo:
    def __init__(self, vida, forca, nome):
        self.vida = vida  
        self.forca = forca
        self.nome = nome
        print(f"O inimigo {self.nome} criado com sucesso")

    def atacar(self, jogador):
        print(f"{self.nome} - Estou atacando o jogador.")
        jogador.vida = jogador.vida - self.forca
        print(f"{self.nome} - O jogador ficou com {jogador.vida} de vida restante.")


class Bowser(Inimigo):
    def AtaqueEspecial(self, tipo_ataque, jogador):
        if tipo_ataque == "SoproDeFogo":
            jogador.vida = jogador.vida - 30
            print(f"{self.nome} - Ataque (Sopro de Fogo) - O jogador ficou com {jogador.vida} de vida restante.")
        elif tipo_ataque == "GiroDoCasco":
            jogador.vida = jogador.vida - 50
            print(f"{self.nome} - Ataque (Giro Do Casco) - O jogador ficou com {jogador.vida} de vida restante.")

player = Jogador(100, 100)
inimigo1 = Inimigo(800, 10, "Lorota")
inimigo2 = Bowser(2000,20, "Bowser")

inimigo1.atacar(player)
inimigo2.AtaqueEspecial("SoproDeFogo", player)
inimigo2.atacar(player)