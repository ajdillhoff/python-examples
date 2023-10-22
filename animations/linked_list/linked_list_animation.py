from manim import *

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.circle = Circle(radius=0.5)  # Create a circle to represent the node
        self.text = Text(value).scale(0.5).next_to(self.circle, UP)  # Create text to display the value
        self.group = VGroup(self.circle, self.text)  # Group the circle and text together

class LinkedListAnimation(Scene):
    def construct(self):
        nodes = [LinkedListNode(f"Node {i}") for i in range(1, 6)]  # Create 5 nodes
        for i in range(4):  # Position the nodes and arrows
            nodes[i].group.next_to(nodes[i - 1].group, RIGHT, buff=2) if i != 0 else nodes[i].group.to_edge(LEFT, buff=2)
            arrow = Arrow(nodes[i].group.get_right(), nodes[i + 1].group.get_left(), buff=0.25)
            self.play(Create(nodes[i].group), Create(arrow))  # Create the nodes and arrows

        self.play(Create(nodes[4].group))  # Create the last node
