class Node:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.children = dict()
    
    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

class Trie:
    def __init__(self):
        self.head = Node()
    
    def add_word(self, word):
        current_node = self.head
        word_finished = True
        
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break
        
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1
        
        current_node.data = word
    
    def add_words(self, words):
        for word in words.split():
            self.add_word(word)
   
    def has_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word precisa de uma string valida.')

        current_node = self.head
        exists = True
        
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break
        
        if exists:
            if current_node.data == None:
                exists = False
        
        return exists

    def remove_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word precisa de uma string valida')

        current_node = self.head
        exists = True
        
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break
        
        if exists:
            current_node.data = None


if __name__ == '__main__':

    trie = Trie()
    words = 'abacate bala cão dado elefante faca giz helicóptero igreja jacaré kiwi lápis macaco nuvem ovo pássaro quarto rádio sapato tartaruga uva vela xícara zebra abajur balão caranguejo dente espelho fogueira garfo herança ilha joelho ketchup lenço martelo nariz olho pipoca queijo relógio sacola tigela urso vaso whisky xale youtuber zíper abacaxi banana cama dado eletricidade foguete gaveta helicóptero iglu jardim karaokê lâmpada melancia ninho orelha palhaço quiche rede sorvete tapete uísque veludo xerife yoga zumbido abelha bolacha computador dardo eletrônica fivela galho hambúrguer iceberg jacuzzi kimono lábio maçã narval ostra pente quadro raquete sela trovão uva-passa viking waffle xícara yttrium zepelim abajur bengala camiseta dado espada fogão giroscópio helicóptero isqueiro janela kimchi labirinto mala nuvem ovo pão quimera robô sorriso taco unicórnio vaso wok xenônio yodel zangão abacate bambu caneca dado esquilo foice girafa holograma isca jardineira kiwi lanterna malote nuvem ovo papel quinoa rato serpente tabuleiro unicornio vareta xarope yurt zumbi abóbora biscoito cadeira dado escada ferro galáxia holograma iglu jacaré kilt lança mel ninho orquídea pá quadro rabanete sereia tangerina uniforme violino xadrez yogurt zoológico açaí bolha canivete dado esmeralda fogo gato hipopotamo isopor jacuzzi kiwi lupa neblina orvalho pipa quadro rosto sorvete totem urso-pardo violão xale zíper açúcar banana chave dado escritório fada gavião hóquei ioga joaninha ketchup lança maçã nuca ovo pato quebra-nozes robalo sacola tatuagem unicórnio vareta xarope yo-yo zangado abacate balde chá dado espinha fada gengibre harpa ícone joelho kiwi laranja mola navio ouro pêssego quadro rabisco sol trampolim urtiga violino xerife yuppie zebra acordeão bambolê calça dado espelho faca gato helicóptero igreja'

    trie.add_words(words)

    userInput = input("insira uma palavra ")
    if(trie.has_word(userInput) == True):
        print("foi encontrada a palavra  ", userInput)
    else:
        print("non existent")
    # #Testes para busca
    # print("Teste para busca:\n")
    # if(trie.has_word('sol') == True):
    #     print("A palavra foi encontrada.\n")
    # else:
    #     print("A palavra nao foi encontrada.\n")      

    # if(trie.has_word('cobre') == True):
    #     print("A palavra foi encontrada.\n")
    # else:
    #     print("A palavra nao foi encontrada.\n")

    # #Testes para inserção
    # print("Teste para insercao:\n")
    # if(trie.has_word('so') == True):
    #     print("A palavra foi encontrada.\n")
    # else:
    #     print("A palavra nao foi encontrada.\n")  
    
    # trie.add_word('so')

    # if(trie.has_word('so') == True):
    #     print("A palavra foi encontrada.\n")
    # else:
    #     print("A palavra nao foi encontrada.\n")  

    # #Testes para remoção
    # print("Teste para remocao:\n")
    # trie.remove_word('sol')
    
    # if(trie.has_word('sol') == True):
    #     print("A palavra foi encontrada.\n")
    # else:
    #     print("A palavra nao foi encontrada.\n")