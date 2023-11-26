# cria classe "nodo" para a palavra
class TrieTreeNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        self.jogos = []


# cria uma classe para a arvore
class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode("")  # indica que o nodo "root" é vazio

    # inserção
    def insert(self, word, jogo):
        node = self.root
        word_upperCase = word.upper()
        for char in word_upperCase:
            # se um caracter já existe na arvore como "child", move para aquela child
            if char in node.children:
                node = node.children[char]
            else:  # do contrario cria uma nova
                new_node = TrieTreeNode(char)
                node.children[char] = new_node
                node = new_node
        node.jogos.append(jogo)  # adiciona na lista os valores do Jogo
        node.is_end = True

    def depth_first_search(self, node):
        lista_jogos = []
        # se o nodo atual marcar o final de uma palavra, adiciona na lista
        if node.is_end:
            lista_jogos.extend(node.jogos)
        #vai adicionando as as childs dentro da lista recursivamente
        for child in node.children.values():
            lista_jogos.extend(self.depth_first_search(child))

        return lista_jogos

    def words_from_prefix(self, x):
        node = self.root
        word_upperCase = x.upper()
        #percorre os caracteres da palavra
        for char in word_upperCase:
            #se o caracter ja existir dentro da arvore, move para aquele prefixo
            if char in node.children:
                node = node.children[char]
            else: #se não existir retorna lista vazia
                return []
        return self.depth_first_search(node) #aciona a função recursiva para verificar letra por letra da palavra
