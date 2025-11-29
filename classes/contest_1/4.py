class Programmer:
    def __init__(self, name: str, job: str):
        self.name = name
        self.job = job
        self.hours = 0
        self.increases = 0
        self.current_salary = 0
        
        self.salary = {
            'junior': 10,
            'middle': 15,
            'senior': 20
        }
        
    def work(self, time: int) -> None:
        self.hours += time
        self.current_salary += time * self.salary[self.job.lower()]
        
    def rise(self) -> None:
        if self.job.lower() == 'junior':
            self.job = 'Middle'
        elif self.job.lower() == 'middle':
            self.job = 'Senior'
        else:
            self.salary['senior'] += 1
        
        self.increases += 1
    
    def info(self) -> str:
        return f'{self.name} {self.hours}ч. {self.current_salary}тгр.'

        
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
