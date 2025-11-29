import math


class Rectangle:
    def __init__(self, p1: tuple[float], p2: tuple[float]):
        (x1, y1), (x2, y2) = p1, p2
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.x, self.y = x1, y1
        self.width, self.height = x2 - x1, y2 - y1
    
    def perimeter(self) -> float:
        return round((self.width + self.height) * 2, 2)
    
    def area(self) -> float:
        return round(self.width * self.height, 2)
    
