# nodo
class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.height = 1


# arvore AVL
class AVLtree:
    def __init__(self):
        self.base = None

    # função que obtém altura do nó
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    # calcula o nivel de balanceamento do nó
    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # rotação simples para a direita
    def _rightSimpleRotation(self, y):  # recebe um nó e armazena no y
        x = y.left  # atribui o filho esquerdo de y ao x
        Temp = x.right  # armazena o filho direito de x na variavel temp
        # faz a atualização
        x.right = y  # y se torna o filho direito de x
        y.left = Temp  # filho esquerdo de y se torna temp

        y.height = 1 + max(
            self._height(y.left), self._height(y.right)
        )  # atualiza a altura do nó/ faz o calculo da altura com base na altura maxima dos filhos esquerdo e direito e adiciona 1
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x  # retorna x que é a nova raiz da subarvore

    # rotação simples para a esquerda
    def _leftSimpleRotation(self, y):
        x = y.right  # atribui o filho direito de y ao x
        temp = x.left  # atribui o filho esquerdo de x ao temp
        # atualização
        x.left = y  # y se torna filho esquerdo de x
        y.right = temp  # filho direito de y se torna temp

        y.height = 1 + max(
            self._height(y.left), self._height(y.right)
        )  # atualiza a altura do nó/ faz o calculo da altura com base na altura maxima dos filhos esquerdo e direito e adiciona 1
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x  # retorna x que é a nova raiz da subarvore

    # inserir
    def insertOnAVL(self, base, key):
        if base is None:
            return Node(key) 

        if key < base.key:
            base.left = self.insertOnAVL(
                base.left, key
            )  # inserido na esquerda se for menor
        else:
            base.right = self.insertOnAVL(base.right, key)  # na direita se for maior
        base.height = 1 + max(self._height(base.left), self._height(base.right))

        balance = self._balance(base)

        # caso 1 - rotação simples a esquerda
        if (
            balance < -1 and key > base.right.key
        ):  # se a balance estiver -1 e a chave for maior que o nodo na direita, faz uma rotação simples à esquerda
            return self._leftSimpleRotation(base)
        # caso 2 - rotação simples à direita
        if (
            balance > 1 and key < base.left.key
        ):  # se a balance estiver 1 e a chave for menor que o nodo na esquerda, faz uma rotação simples à direita
            return self._rightSimpleRotation(base)
        # caso 3 - rotação dupla à esquerda-direita
        if balance > 1 and key > base.left.key:
            base.left = self._leftSimpleRotation(base.left)
            return self._rightSimpleRotation(base)
        # caso 4 - rotação dupla à direita-esquerda
        if balance < -1 and key < base.right.key:
            base.right = self._rightSimpleRotation(base.right)
            return self._leftSimpleRotation(base)

        return base

    ################
    # Função auxiliar para encontrar o nó mínimo na árvore
    def _minimalValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Função para remover um nó da árvore AVL
    def deleteOnAVL(self, base, key):
        if base is None:
            return base

        if key < base.key:
            base.left = self.deleteOnAVL(base.left, key)
        elif key > base.key:
            base.right = self.deleteOnAVL(base.right, key)
        else:
            if base.left is None or base.right is None:
                if base.left:
                    temp = base.left
                else:
                    temp = base.right
                if temp is None:
                    temp = base
                    base = None
                else:
                    base = temp
                temp = None
            else:
                temp = self._minimalValueNode(base.right)
                base.key = temp.key
                base.right = self.deleteOnAVL(base.right, temp.key)

        if base is None:
            return base

        base.height = 1 + max(self._height(base.left), self._height(base.right))
        balance = self._balance(base)

        # caso 1 - rotação simples a esquerda
        if (
            balance < -1 and key > base.right.key
        ):  # se a balance estiver -1 e a chave for maior que o nodo na direita, faz uma rotação simples à esquerda
            return self._leftSimpleRotation(base)
        # caso 2 - rotação simples à direita
        if (
            balance > 1 and key < base.left.key
        ):  # se a balance estiver 1 e a chave for menor que o nodo na esquerda, faz uma rotação simples à direita
            return self._rightSimpleRotation(base)
        # caso 3 - rotação dupla à esquerda-direita
        if balance > 1 and key > base.left.key:
            base.left = self._leftSimpleRotation(base.left)
            return self._rightSimpleRotation(base)
        # caso 4 - rotação dupla à direita-esquerda
        if balance < -1 and key < base.right.key:
            base.right = self._rightSimpleRotation(base.right)
            return self._leftSimpleRotation(base)

        return base

    # Função para inserir um novo nó na árvore
    def insertNode(self, key):
        self.base = self.insertOnAVL(self.base, key)

    # Função para remover um nó da árvore
    def deleteNode(self, key):
        self.base = self.deleteOnAVL(
            self.base, key
        )  # esconder do usuario funções recursivas

    # Função para realizar uma travessia em ordem na árvore AVL
    def inOrderTraversal(self, node):  # vendo onde termina o nodo
        if node:  # checagem se não é nulo
            self.inOrderTraversal(node.left)  #
            print(
                node.key, end=" "
            )  # "end" por padrão o print poe nova linha end substitui por espaço
            self.inOrderTraversal(node.right)

    # Função para realizar uma travessia em ordem na árvore AVL
    def inOrder(self):
        self.inOrderTraversal(
            self.base
        )  # inOrderTraversal recebe node, usuario nao precisa saber quem é node

    # Função de busca por valor especifico
    def searchForItemTraversal(self, node, price):  # função recursiva
        if node:
            if node.key == price:
                return node.key  
            if price <= node.key:
                return self.searchForItemTraversal(node.left, price)
            elif price >= node.key:
                return self.searchForItemTraversal(node.right, price)
            else:
                return -1  # preço impossivel

    def searchForItem(self, price):
        return self.searchForItemTraversal(self.base, price)
    

    def searchRangeTraversal(self, node, min, max, prices):
        if node:
            if prices != None:
                self.searchRangeTraversal(node.left, min, max, prices)
                prices.append(node.key)
                self.searchRangeTraversal(node.right, min, max, prices)
            else:
                if min <= node.key and node.left != None:
                    newList = self.searchRangeTraversal(node.left, min, max, prices)
                    if newList != None:
                        newList.append(node.key)
                        newList.extend(self.searchRangeTraversal(node.right, min, max, newList) or [])
                    return newList
                elif min >= node.key:
                    return self.searchRangeTraversal(node.right, min, max, prices)
                else:
                    return [node.key] # cria lista sem nome com o menor valor
        else:
            return prices

    def searchRange(self, min, max):
        return self.searchRangeTraversal(self.base, min, max, None)
    
    def printTree(self, node=None, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:
                if node.left:
                    self.printTree(node.left, level + 1, "L--- ")
                if node.right:
                    self.printTree(node.right, level + 1, "R--- ")


avltree = AVLtree()
keys = [10, 40, 60, 20, 30, 100, 10, 20, 30, 6 , 12, 24, 45, 6, 6, 6, 6, 6, 102]
for key in keys:
    avltree.insertNode(key)

# print("arvore inicial ")
# avltree.inOrder()
# print()

# avltree.deleteNode(100)

# print("arvore ")

# avltree.inOrder()
# print()
# print(avltree.searchRange(5, 100))
