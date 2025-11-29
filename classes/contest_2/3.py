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
            
    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self
    

point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)



