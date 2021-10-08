'''
1. Реализовать собственный класс с использованием магических методов
'''

class Human:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        s = f'Гражданин\nимя: {self.name}, возраст: {self.age}, вес: {self.weight}\n'
        return s

    def __eq__( self, other ):
        return  self.age == other.age
    def __lt__( self, other ):
        return  self.age < other.age
    def __gt__( self, other ):
        return  self.age > other.age


if __name__ == '__main__':
    human = Human( 'Павел',30,91 )
    human2 = Human('Фёдор', 35, 120)
    human3 = Human('Маша', 30, 50)

    print( human , human2, human3,sep='' )

    print(  human == human2, human == human3 )
    print(  human <  human2, human <  human3 )
    print(  human >  human2, human >  human3 )