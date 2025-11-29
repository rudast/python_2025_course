class Cell:
    def __init__(self, state: str = '*'):
        self.state = state
        
    def status(self) -> str:
        return self.state

    def __str__(self) -> str:
        return self.state
    
    
class Checkers:
    def __init__(self):
        self.cells = [[Cell() for _ in range(8)] for _ in range(8)]
        
        for row in '87654321':
            for col in 'ABCDEFGH':
                self.cells[int(row) - 1][ord(col) - ord('A')] = Cell('X')
                
        for row in '8642':
            for col in 'FH':
                self.cells[ord(col) - ord('A')][int(row) - 1] = Cell('B')
                
        for row in '7531':
            for col in 'G':
                self.cells[ord(col) - ord('A')][int(row) - 1] = Cell('B')
                
        for row in '8642':
            for col in 'B':
                self.cells[ord(col) - ord('A')][int(row) - 1] = Cell('W')
                
        for row in '7531':
            for col in 'AC':
                self.cells[ord(col) - ord('A')][int(row) - 1] = Cell('W')
                
    def get_cell(self, pos: str) -> Cell:
        return self.cells[int(pos[1]) - 1][ord(pos[0]) - ord('A')]
    
    def move(self, start_pos: str, finish_pos: str) -> None:
        self.cells[int(start_pos[1]) - 1][ord(start_pos[0]) - ord('A')], \
            self.cells[int(finish_pos[1]) - 1][ord(finish_pos[0]) - ord('A')] = \
            self.cells[int(finish_pos[1]) - 1][ord(finish_pos[0]) - ord('A')], \
            self.cells[int(start_pos[1]) - 1][ord(start_pos[0]) - ord('A')]
