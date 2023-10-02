from manim import *

config.background_color = WHITE

class ArrayScene(ThreeDScene):
    def construct(self):

        # Starting address
        base_address = 0xA0
        
        # Array values
        array_values = [1, 2, 3, 4, 5, 6, 7, 8]
        
        # Create array rectangles and text
        rects = VGroup(*[Square(side_length=0.8, color=BLACK) for _ in range(8)])
        rects.arrange_submobjects(RIGHT, buff=0.4)
        
        # Create array value texts and address texts
        value_texts = VGroup(*[Text(str(value), font_size=24, color=BLACK) for value in array_values])
        address_texts = VGroup(*[Text(hex(base_address + i * 4), font_size=24, color=BLACK) for i in range(8)])
        
        # Position the texts
        for i in range(8):
            value_texts[i].move_to(rects[i].get_center())
            address_texts[i].next_to(rects[i], DOWN)
        
        # Group everything together
        array_group = VGroup(rects, value_texts, address_texts)
        
        # Center the array group
        array_group.move_to(ORIGIN)
        
        # Display the array
        self.play(Write(array_group))
        self.wait()
