RED = 0
BLACK = 1

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
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
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def insert_fixup(self, z):
        while z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:
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
                if y.color == RED:
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
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
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