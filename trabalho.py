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
        return f"Jogo ID: {jogo.jogo_id} -- Título: {jogo.titulo} -- Desenvolvedor: {jogo.desenvolvedor} -- Preço: {jogo.preco} -- Gêneros: {jogo.generos}"

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

def gerar_jogos(num_jogos):
        jogos = {}
        lista_nome_jogos = [
    "Dark Horizon",
    "Forgotten Realms: Echoes of Destiny",
    "Quantum Shift",
    "Lunar Eclipse",
    "Nebula Quest",
    "Shadow of Serenity",
    "Mystic Legends",
    "Realm of Chaos",
    "Celestial Odyssey",
    "Galactic Dominion",
    "Enchanted Kingdoms",
    "Cybernetic Uprising",
    "Phoenix Rising",
    "Echoes of Eternity",
    "Starlight Citadel",
    "The Abyssal Rift",
    "Arcane Ascension",
    "Wandering Souls",
    "Infinite Horizons",
    "Abyssal Conquest",
    "Stellar Convergence",
    "Chronicles of Valor",
    "Runebound Chronicles",
    "Kingdoms of Kaleidoscope",
    "Frostfall Adventures",
    "Infinity's Edge",
    "Radiant Vanguard",
    "Nexus of Shadows",
    "Runeblade Reckoning",
    "Dreamweaver's Legacy",
    "Eldritch Chronicles",
    "Odyssey of the Ancients",
    "Ascendant Empires",
    "Shadowbane Requiem",
    "Aetherial Alchemy",
    "Celestial Echo",
    "Astral Ascendancy",
    "Legends of Lumina",
    "Enigma of Elysium",
    "Mythos Unbound",
    "Riftwalker Chronicles",
    "Stellaris Dominion",
    "Ethereal Enclave",
    "Lost Horizon",
    "Crimson Eclipse",
    "Elysian Uprising",
    "Emberfall Chronicles",
    "Quantum Nexus",
    "Celestial Drift",
    "Starforged Odyssey",
    "Shattered Realms",
    "Arcane Alchemy",
    "Echoes of Eldoria",
    "Astral Dominion",
    "Runebound Odyssey",
    "Crimson Convergence",
    "Infinite Realms",
    "Starlight Serenade",
    "Aetherial Awakenings",
    "Shadow's Embrace",
    "Celestial Voyager",
    "Nexus of Legends",
    "Ethereal Enigma",
    "Mythic Ascendancy",
    "Forgotten Realms: Echoes of Shadows",
    "Runeblade Chronicles",
    "Emberfall Reckoning",
    "Quantum Serenade",
    "Shattered Odyssey",
    "Astral Alchemy",
    "Celestial Chronicles",
    "The Legend of Zelda: Breath of the Wild",
    "Super Mario Odyssey",
    "Red Dead Redemption 2",
    "Fortnite",
    "Minecraft",
    "Call of Duty: Warzone",
    "Assassin's Creed Valhalla",
    "Cyberpunk 2077",
    "Among Us",
    "Genshin Impact",
    "Overwatch",
    "FIFA 22",
    "Apex Legends",
    "Destiny 2",
    "Valorant",
    "The Witcher 3: Wild Hunt",
    "Grand Theft Auto V",
    "League of Legends",
    "Dota 2",
    "Counter-Strike: Global Offensive",
    "Animal Crossing: New Horizons",
    "Super Smash Bros. Ultimate",
    "Monster Hunter: World",
    "World of Warcraft",
    "Final Fantasy XIV",
    "Rocket League",
    "Mortal Kombat 11",
    "The Last of Us Part II",
    "Marvel's Spider-Man: Miles Morales",
    "Hades",
    "Hollow Knight",
    "Stardew Valley",
    "Rainbow Six Siege",
    "Tom Clancy's The Division 2",
    "No Man's Sky",
    "Among Us",
    "Fall Guys: Ultimate Knockout",
    "Star Wars Jedi: Fallen Order",
    "God of War",
    "DOOM Eternal",
    "Control",
    "Celeste",
    "Death Stranding",
    "Subnautica",
    "Sekiro: Shadows Die Twice",
    "Bioshock Infinite",
    "The Elder Scrolls V: Skyrim",
    "Dark Souls III",
    "Ratchet & Clank: Rift Apart",
    "Demon's Souls",
    "Resident Evil Village",
    "Returnal",
    "Hitman 3",
    "F1 2021",
    "Cyber Shadow",
    "Crash Bandicoot 4: It's About Time",
    # Adicione mais jogos conforme necessário
]
        lista_nome_desenvolvedores = [
    "Ubisoft",
    "Electronic Arts",
    "Nintendo",
    "Rockstar Games",
    "Activision",
    "Square Enix",
    "Epic Games",
    "Valve Corporation",
    "Bethesda Game Studios",
    "Capcom",
    "Blizzard Entertainment",
    "CD Projekt",
    "NetherRealm Studios",
    "Naughty Dog",
    "Bioware",
    "Respawn Entertainment",
    "Bandai Namco Entertainment",
    "Konami",
    "Gearbox Software",
    "Sega",
    "Kojima Productions",
    "343 Industries",
    "Sony Interactive Entertainment",
    "Insomniac Games",
    "Riot Games",
    "Guerrilla Games",
    "Treyarch",
    "Larian Studios",
    "Bungie",
    "FromSoftware",
    "Obsidian Entertainment",
    "Remedy Entertainment",
    "Hangar 13",
    "Playdead",
    "Turn 10 Studios",
    "Crytek",
    "Io Interactive",
    "Double Fine Productions",
    "Digital Extremes",
    "Quantic Dream",
    "PlatinumGames",
    "Fatshark",
    "Square Enix Montreal",
    "Ghost Games",
    "Monolith Productions",
    "Hangar 13",
    "Mojang Studios",
    "The Coalition",
    "Ubisoft Montreal",
    "Crystal Dynamics",
    "Playtonic Games",
    "Playism",
    "Guerilla Cambridge",
    "Camouflaj",
    "Compulsion Games",
    "Hello Games",
    "Mediatonic",
    "Klei Entertainment",
    "Motion Twin",
    "Moon Studios",
    "Team Cherry",
    "Vlambeer",
    "Yacht Club Games",
    "Zaum Studio",
    "IO Interactive",
    "Night School Studio",
    "Outerminds Inc.",
    "Playdead",
    "Quest",
    "Raw Fury",
    "Snowman",
    "Team17",
    "Ubisoft Toronto",
    "Vicarious Visions",
    "Wargaming",
    "Xbox Game Studios",
    "Young Horses",
    "ZeniMax Media",
    "Zynga",
    # Continue a lista conforme necessário
]

        for i in range(num_jogos):
            jogo_id = i + 1  
            titulo = random.choice(lista_nome_jogos)
            desenvolvedor = random.choice(lista_nome_desenvolvedores)
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
        if(avltree.searchForItem(price) != None):
            print(Print_List(avltree.searchForItem(price)))
        else: 
            print("None")
    elif(userInput == 2):
        rangeDown = int(input("insira o preço mínimo: "))
        rangeUp = int(input("insira o preço máximo: "))
        print(Print_List(avltree.searchRange(rangeDown, rangeUp)))
    elif(userInput == 3):
        print("""generos disponiveis: 
              Ação
              Aventura
              Moba
              Corrida
              Tiro
              RPG
              Esportes""")
        generoInput = input("insira o gênero: ")
        print(Print_List(hashes_por_genero.obter_jogos(generoInput)))
    elif(userInput == 4):
        nomeInput = input("nome que deseja pesquisar: ")
        print(Print_List(trietree.words_from_prefix(nomeInput)))
    elif(userInput == 5):
        avltree.printTree(avltree.base)
    else:
        print("invalido")