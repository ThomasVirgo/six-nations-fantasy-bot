class Player:
    def __init__(self, name, position, cost, country=None) -> None:
        self.name = name
        self.position = position
        self.country = country
        self.cost = cost
    
    def __str__(self) -> str:
        return f'{self.name} -- {self.position} -- {self.cost}'

class Squad:
    def __init__(self) -> None:
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.seven = None
        self.eight = None
        self.nine = None
        self.ten = None
        self.eleven = None
        self.twelve = None
        self.thirteen = None
        self.fourteen = None
        self.fifteen = None
        self.bench1 = None
        self.bench2 = None
        self.bench3 = None