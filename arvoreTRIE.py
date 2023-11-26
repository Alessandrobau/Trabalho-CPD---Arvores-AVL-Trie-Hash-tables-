class TrieTreeNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        self.jogos = []


class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode("")

    def insert(self, word, jogo):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieTreeNode(char)
                node.children[char] = new_node
                node = new_node
        node.jogos.append(jogo)
        node.is_end = True

    def depth_first_search(self, node):
        lista_jogos = []
        if node.is_end:
            lista_jogos.extend(node.jogos)

        for child in node.children.values():
            lista_jogos.extend(self.depth_first_search(child))

        return lista_jogos

    def words_from_prefix(self, x):
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return self.depth_first_search(node)
