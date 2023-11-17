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

class MotorBuscaJogos:
    def __init__(self):
        pass
        #self.catalogo_jogos = ArvoreJogos()
        # self.generos = HashGeneros()
    # ... Outros més para adicionar jogos, busca, etc
    
avltree = AVLtree()
keys = [10, 40, 60, 20, 30, 100, 10, 20, 30, 6 , 12, 24, 45, 74, 70, 6, 80, 6, 102, 130, 250, 1000]
for key in keys:
    avltree.insertNode(key, "value")    
    
    
print(""" 
      
      ##########PESQUISA DE JOGOS##########
      1- ver jogos
      2- fazer pesquisa por item
      3- fazer pesquisa por range
      """)
userInput = int(input(" "))
if(userInput == 1):
    avltree.inOrder()
    print()
elif(userInput == 2):
    price = int(input("insira o preço: "))
    print(avltree.searchForItem(price))
elif(userInput == 3):
    rangeDown = int(input("insira o preço mínimo: "))
    rangeUp = int(input("insira o preço máximo: "))
    print(avltree.searchRange(rangeDown, rangeUp))