from arvoreAVL import *
# class HashGeneros:
#     def __init__(self):
#         self.genero_para_jogos = {}
#     def adicionar_jogo(self, jogo):
#         pass
#     # Adicionar jogos na hash table de acordo com seu(s) gênero(s)
#     def obter_jogos(self, genero):
#         pass
#     # Buscar jogos de um determinado gênero
# ''''''

######criar menu fdisk#######
class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos # Lista, pois um jogo pode pertencer a múltiplos gêneros
class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None
class ArvoreJogos:
    def __init__(self):
        self.raiz = None
    def inserir(self, jogo):
        pass
    # : Inserir jogo na BST com base no preço
    def buscar_por_preco(self, preco):
        pass
    # : Buscar jogos por preço simple
    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        pass
    # : Recuperar jogos dentro de uma faixa de preço

class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        # self.generos = HashGeneros()
    # ... Outros més para adicionar jogos, busca, etc