class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x 
        self.y = y
        
    
    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y
        
        
    def length(self, point: Point) -> float:
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)
        
        
if __name__ == '__main__':
    point = Point(3, 5)
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)
    
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))

