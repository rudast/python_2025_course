import math


class Rectangle:
    def __init__(self, p1: tuple[float], p2: tuple[float]):
        (x1, y1), (x2, y2) = p1, p2
        self.x1, self.x2 = sorted((x1, x2))
        self.y1, self.y2 = sorted((y1, y2))
        self.width, self.height = self.x2 - self.x1, self.y2 - self.y1
    
    def perimeter(self) -> float:
        return round((self.width + self.height) * 2, 2)
    
    def area(self) -> float:
        return round(self.width * self.height, 2)
    
    def get_pos(self) -> tuple[float]:
        return (round(self.x1, 2), round(self.y2, 2))
    
    def get_size(self) -> tuple[float]:
        return (round(self.width, 2), round(self.height, 2))
    
    def move(self, dx: float, dy: float) -> None:
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
        
    def resize(self, width: float, height: float) -> None:
        self.x2 = self.x1 + width
        self.y1 = self.y2 - height
        self.width, self.height = self.x2 - self.x1, self.y2 - self.y1



rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())

    
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
