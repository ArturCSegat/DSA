class Node:

    def __init__(self, key):
        self.key = int(key)
        self.right = None
        self.left = None

def search(alvo, raiz):
    if raiz is None:
        return False

    elif alvo == raiz.key:
        return True

    elif alvo > raiz.key:
        return search(alvo, raiz.right)
    else:
        return search(alvo, raiz.left)


def insertion(node, raiz):
    if raiz is None:
        raiz = node
    else:
        if raiz.key > node.key:
            if raiz.left is None:
                raiz.left = node
            else:
                insertion(node, raiz.left)
        else:
            if raiz.right is None:
                raiz.right = node
            else:
                insertion(node, raiz.right)

    

def inOrder(raiz):
    if raiz:
        inOrder(raiz.left)
        print(raiz.key)
        inOrder(raiz.right)
def preOrder(raiz):
    if raiz:
        print(raiz.key)
        inOrder(raiz.left)
        inOrder(raiz.right)

def postOrder(raiz):
    if raiz:
        inOrder(raiz.left)
        inOrder(raiz.right)
        print(raiz.key)

root = Node(6)
insertion(Node(4), root)
insertion(Node(5), root)
insertion(Node(8), root)


print("Ordem simetrica")
inOrder(root)
print("Pre Ordem")
preOrder(root)
print("Pos Ordem")
postOrder(root)

x = search(4, root)

print(x)
