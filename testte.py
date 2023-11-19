import random

class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos

def gerar_jogos(num_jogos):
    jogos = {}

    for i in range(num_jogos):
        jogo_id = i + 1  # IDs começando em 1
        titulo = f"Jogo {jogo_id}"
        desenvolvedor = f"Desenvolvedor {jogo_id}"
        preco = round(random.uniform(10, 200), 2)  # Preço aleatório entre 10 e 60
        generos = random.sample(["Ação", "Aventura", "RPG", "Esportes"], random.randint(1, 3))

        jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
        jogos[jogo_id] = jogo

    return jogos

# Exemplo de uso
num_jogos = 100
jogos_aleatorios = gerar_jogos(num_jogos)

# Imprimir os jogos gerados
for jogo_id, jogo in jogos_aleatorios.items():
    print(f"Jogo ID: {jogo.jogo_id}, Título: {jogo.titulo}, Desenvolvedor: {jogo.desenvolvedor}, Preço: {jogo.preco}, Gêneros: {jogo.generos}")
