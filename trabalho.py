from arvoreAVL import *
import random
class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def get_hash(self):
        pass

    def adicionar_jogo(self, jogo):
        pass
    def obter_jogos(self, genero):
        pass

class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos 
class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class MotorBuscaJogos: ## verificar se é necessario
    def __init__(self):
        pass
        #self.catalogo_jogos = ArvoreJogos()
        # self.generos = HashGeneros()
    # ... Outros més para adicionar jogos, busca, etc



def gerar_jogos(num_jogos):
        jogos = {}
        for i in range(num_jogos):
            jogo_id = i + 1  
            titulo = f"Jogo {jogo_id}"
            desenvolvedor = f"Desenvolvedor {jogo_id}"
            preco = round(random.uniform(10, 60))  # Preço aleatório entre 10 e 60
            generos = random.sample(["Ação", "Aventura", "RPG", "Esportes", "Corrida", "Tiro", "Moba"], random.randint(1, 3))

            jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
            jogos[jogo_id] = jogo
        return jogos
        
avltree = AVLtree()
keys = [] 

num_jogos = int(input("quantos jogos terão na lista? "))
jogos_aleatorios = gerar_jogos(num_jogos)

for jogo_id, jogo in jogos_aleatorios.items():
    avltree.insertNode(jogo.preco, jogo.titulo)
    print(f"Jogo ID: {jogo.jogo_id}, Título: {jogo.titulo}, Desenvolvedor: {jogo.desenvolvedor}, Preço: {jogo.preco}, Gêneros: {jogo.generos}")

userInput = 0
while(userInput < 6):
    print(""" 
        
        ##########PESQUISA DE JOGOS##########
        1- fazer pesquisa por preço
        2- fazer pesquisa por range de preço
        3- fazer pesquisa por categoria
        4- fazer pesquisa por nome
        5- printar arvore
        """)
    userInput = int(input(" "))
    if(userInput == 1):
        price = int(input("insira o preço: "))
        print(avltree.searchForItem(price))
    elif(userInput == 2):
        rangeDown = int(input("insira o preço mínimo: "))
        rangeUp = int(input("insira o preço máximo: "))
        print(avltree.searchRange(rangeDown, rangeUp))
    elif(userInput == 3):
        print("Nao implementado")
    elif(userInput == 4):
        print("nao implementado")
    elif(userInput == 5):
        avltree.printTree(avltree.base)
    else:
        print("invalido")