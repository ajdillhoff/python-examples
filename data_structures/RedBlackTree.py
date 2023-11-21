import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

RED = 0
BLACK = 1

class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = None

    def __str__(self):
        return str([self.key, self.color])

class RedBlackTree:
    def __init__(self):
        self.root = None

    def create_treeviz(self):
        G = nx.DiGraph()
        queue = [self.root]
        node_colors = ["black"]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
                G.add_edge(node.key, node.left.key)
                node_colors.append("red" if node.left.color == RED else "black")
            if node.right != None:
                queue.append(node.right)
                G.add_edge(node.key, node.right.key)
                node_colors.append("red" if node.right.color == RED else "black")
        return G, node_colors

    def print_inorder(self, x):
        if x != None:
            self.print_inorder(x.left)
            print(x)
            self.print_inorder(x.right)

    def print_ascii_tree(self, node, prefix=""):
        if node != None:
            print(prefix + "└── " + str(node.key) + " " + str(node.color))
            self.print_ascii_tree(node.left, prefix + "    ")
            self.print_ascii_tree(node.right, prefix + "    ")

    def repr_ascii_tree(self, node, prefix=""):
        s = ""
        if node != None:
            s = prefix + "└── " + str(node.key) + " " + str(node.color)
            s += self.repr_ascii_tree(node.left, prefix + "    ")
            s += self.repr_ascii_tree(node.right, prefix + "    ")
        
        return s

    def print_tree(self):
        """Prints an ASCII version of the tree."""
        self.print_ascii_tree(self.root)

    def print_bfs(self):
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.p = x
        y.p = x.p
        if x.p == None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != None:
            x.right.p = y
        x.p = y.p
        if y.p == None:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        if v != None:
            v.p = u.p

    def search(self, x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def insert_fixup(self, z):
        while z.p is not None and z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y is not None and y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y is not None and y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)
        self.root.color = BLACK

    def insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
        z.color = RED
        self.insert_fixup(z)

    def delete(self, z):
        y = z
        y_original_color = y.color

        if z.left == None:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == None:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y != z.right: # y is farther down the tree
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            else:
                x.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.p)
                    x = self.root
        x.color = BLACK

    def __str__(self):
        return self.repr_ascii_tree(self.root)
    
    def __repr__(self):
        return self.repr_ascii_tree(self.root)


if __name__ == "__main__":
    tree = RedBlackTree()

    rng = np.random.default_rng(0)
    values = rng.choice(20, size=15, replace=False)

    for i in values:
        tree.insert(Node(i))

    n = tree.search(tree.root, 15)
    tree.delete(n)

    tree.insert(Node(21))

    G, node_colors = tree.create_treeviz()

    # Visualize as a tree
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

    # Set font color to white
    options = {
        "font_color": "white",
        "font_size": 18,
        "node_size": 1000,
        "edgecolors": "black",
        "linewidths": 3,
        "width": 3,
    }

    nx.draw_networkx(G, pos, with_labels=True, arrows=True, node_color=node_colors, **options)
    plt.show()
