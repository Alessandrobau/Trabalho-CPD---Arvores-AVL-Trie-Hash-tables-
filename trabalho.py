from arvoreAVL import *
from arvoreTRIE import *
import random
BUCKET_SIZE = 666

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = [None] * BUCKET_SIZE

    def get_hash(self, key):
        ASC_Value = 0
        hash = 0
        for letter in key:
            ASC_Value = ASC_Value + ord(letter)
        hash = (hash*31 + ASC_Value) % BUCKET_SIZE
        return hash

    def adicionar_jogo(self, genero, jogo):
        index = self.get_hash(genero)
        if self.genero_para_jogos[index] is None:
            self.genero_para_jogos[index] = [(genero, [jogo])]
        #colisoes
        else:
            for pair in self.genero_para_jogos[index]:
                if pair[0] == genero: #pair[0] = genero
                    pair[1].append(jogo)#adiciona jogo à lista de jogos dentro do parametro pair
                    return
                self.genero_para_jogos[index].append((genero, [jogo]))

    def obter_jogos(self, genero):
        index = self.get_hash(genero)
        if self.genero_para_jogos[index] is not None:
            for pair in self.genero_para_jogos[index]:
                if pair[0] == genero:
                    return pair[1]
        return []
class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos 

    def __str__(jogo):
        return f"Jogo ID: {jogo.jogo_id}, Título: {jogo.titulo}, Desenvolvedor: {jogo.desenvolvedor}, Preço: {jogo.preco}, Gêneros: {jogo.generos}"

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

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

def Print_List(xs):
    return '\n'.join(str(x) for x in xs)

hashes_por_genero = HashGeneros()     
avltree = AVLtree()
trietree = TrieTree()
keys = [] 


num_jogos = int(input("quantos jogos terão na lista? "))
jogos_aleatorios = gerar_jogos(num_jogos)

for jogo_id, jogo in jogos_aleatorios.items():
    avltree.insertNode(jogo.preco, jogo)
    trietree.insert(jogo.titulo, jogo)
    for item in jogo.generos:
        hashes_por_genero.adicionar_jogo(item, jogo)
    print(jogo)

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
        print(Print_List(avltree.searchRange(rangeDown, rangeUp)))
    elif(userInput == 3):
        generoInput = input("insira o gênero: ")
        print(Print_List(hashes_por_genero.obter_jogos(generoInput)))
    elif(userInput == 4):
        nomeInput = input("nome que deseja pesquisar: ")
        print(Print_List(trietree.words_from_prefix(nomeInput)))
    elif(userInput == 5):
        avltree.printTree(avltree.base)
    else:
        print("invalido")