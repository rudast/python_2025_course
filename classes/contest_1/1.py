class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x 
        self.y = y
        
if __name__ == '__main__':
    point = Point(1, 2)
    print(point.x, point.y)