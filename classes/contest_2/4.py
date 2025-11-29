class Fraction:
    def __init__(self, *args):
        self.n: int = 0
        self.d: int = 1
        
        if len(args) == 1 and type(args[0]) == str:
            data = [x.strip() for x in args[0].split('/')]
            self.n = int(data[0])
            self.d = int(data[1])
        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            self.n = args[0]
            self.d = args[1]
            
        self.__update()
            
    def __update(self) -> None:
        for i in range(2, max(abs(self.n), abs(self.d))):
            while self.n % i == 0 and self.d % i == 0:
                self.n //= i
                self.d //= i
                
    def numerator(self, *args) -> int | None:
        if len(args) == 1:
            self.n = args[0]
            self.__update()
            return None
        
        return abs(self.n)
    
    def denominator(self, *args) -> int:
        if len(args) == 1:
            self.d = args[0]
            self.__update()
            return None
        
        return abs(self.d)
        
    def __str__(self):
        return f'{self.n}/{self.d}'
    
    def __repr__(self):
        return f'Fraction({self.n}, {self.d})'
    
            
fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))

fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
