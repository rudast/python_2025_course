class RedButton:
    def __init__(self):
        self.counts = 0
        
    def click(self) -> None:
        self.counts += 1
        print('Тревога!')
        
    def count(self) -> int:
        return self.counts
    
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
