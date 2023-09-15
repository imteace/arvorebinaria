class Arvore:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionarFilho(self, child_node):
        self.filhos.append(child_node)

def procurarElemento(node, target):
    if node is None:
        return False

    if node.valor == target:
        return True

    for child in node.filhos:
        if procurarElemento(child, target):
            return True

    return False

def destruirArvore(node):
    if node is not None:
        for child in node.filhos:
            destruirArvore(child)
        node.filhos = []  # Remove as referências aos filhos
    node = None  # Remove a referência ao nó atual

# Construindo a árvore
root = Arvore("A")
b = Arvore("B")
c = Arvore("C")
d = Arvore("D")
e = Arvore("E")
f = Arvore("F")
g = Arvore("G")
h = Arvore("H")
i = Arvore("I")
j = Arvore("J")
k = Arvore("K")
l = Arvore("L")
m = Arvore("M")
n = Arvore("N")
o = Arvore("O")

root.adicionarFilho(b)
root.adicionarFilho(c)
b.adicionarFilho(d)
b.adicionarFilho(e)
c.adicionarFilho(f)
c.adicionarFilho(g)
d.adicionarFilho(h)
d.adicionarFilho(i)
e.adicionarFilho(j)
f.adicionarFilho(k)
g.adicionarFilho(l)
g.adicionarFilho(m)
j.adicionarFilho(n)
j.adicionarFilho(o)

# Exemplo de uso:
element_to_search = input("Digite o elemento que deseja buscar na árvore: ")
if procurarElemento(root, element_to_search):
    print(f"O elemento '{element_to_search}' existe na árvore.")
else:
    print(f"O elemento '{element_to_search}' não existe na árvore.")

# Destruir a árvore
destruirArvore(root)
print("A árvore foi destruída.")