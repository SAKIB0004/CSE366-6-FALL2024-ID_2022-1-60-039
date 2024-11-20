# environment.py
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def limit_position(self, rect):
        """Ensure the agent stays within the environment boundaries."""
        if rect.left < 0:
            rect.left = 0
        if rect.right > self.width:
            rect.right = self.width
        if rect.top < 0:
            rect.top = 0
        if rect.bottom > self.height:
            rect.bottom = self.height
