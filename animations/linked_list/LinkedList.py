from manim import *

class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedListAnimation(Scene):
    def construct(self):
        nodes = [LinkedListNode(f"Node {i}") for i in range(1, 6)]
        node_mobjects = [Text(node.value) for node in nodes]

        for i in range(4):
            arrow = Arrow(node_mobjects[i].get_right(), node_mobjects[i + 1].get_left(), buff=0.25)
            self.play(Create(node_mobjects[i]), Create(arrow))

        self.play(Create(node_mobjects[4]))  # Create the last node
