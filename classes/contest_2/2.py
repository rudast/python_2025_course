class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x 
        self.y = y
        
    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y
        
    def length(self, point: 'Point') -> float:
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)
        
        
class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(args[0], args[1])
            
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return 'PatchedPoint' + self.__str__()
            

point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))


