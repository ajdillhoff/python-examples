from manim import *
from PIL import Image
import os


class InsertionSort(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame_count = 0

    def construct(self):
        # Initial list to sort
        numbers = [5, 2, 4, 6, 1, 3]
        rectangles = self.create_rectangles(numbers)
        
        # Center the group of rectangles
        group = VGroup(*rectangles).center()
        self.play(*[Create(rect) for rect in rectangles])
        self.wait(1)

        self.take_screenshot()

        # Perform insertion sort and animate the process
        self.insertion_sort(rectangles)
    
    def create_rectangles(self, numbers):
        # Create rectangles with numbers inside them
        rectangles = []
        for i, number in enumerate(numbers):
            rect = Rectangle(height=1, width=1)
            text = Text(str(number))
            group = VGroup(rect, text)
            group.shift(RIGHT * i * 1.5)
            rectangles.append(group)
        return rectangles
    
    def insertion_sort(self, rectangles):
        n = len(rectangles)
        for i in range(1, n):
            key = rectangles[i]
            j = i - 1
            self.play(Indicate(key))
            self.wait(0.5)
            
            # Move the key above the array while comparing and shifting
            self.play(key.animate.shift(UP * 1.5))
            self.take_screenshot()
            while j >= 0 and self.get_value(rectangles[j]) > self.get_value(key):
                self.play(rectangles[j].animate.shift(RIGHT * 1.5))
                rectangles[j + 1] = rectangles[j]
                j -= 1
                self.wait(0.5)
                self.take_screenshot()
            
            rectangles[j + 1] = key
            self.play(key.animate.shift(RIGHT * 1.5 * (j + 1 - i) + DOWN * 1.5))
            self.wait(0.5)

            self.take_screenshot()
    
    def get_value(self, rectangle):
        # Extract the value from the Text inside the VGroup
        return int(rectangle[1].text)

    def take_screenshot(self):
        # Get the current frame as an image
        image_array = self.camera.get_image()
        image = Image.fromarray(np.array(image_array))
        
        # Save the image file
        file_path = os.path.join('media/images/insertion_sort', f'insertion_sort_step{self.frame_count}.png')
        image.save(file_path)
        
        self.frame_count += 1
    

# To run this script locally you would typically use the following command in your terminal or command prompt:
# manim -p -ql <script_name>.py InsertionSort
