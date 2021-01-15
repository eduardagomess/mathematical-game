from random import randint


class Calculate:

    def __init__(self, game_difficulty):
        self.__game_difficulty = game_difficulty
        self.__value_one = self.generateValue
        self.__value_two = self.generateValue
        self.__mathematical_operation = randint(1, 3)
        self.__result = self.generateResult

    @property
    def gameDifficulty(self):
        return self.__game_difficulty

    @property
    def valueOne(self):
        return self.__value_one

    @property
    def valueTwo(self):
        return self.__value_two

    @property
    def mathematicalOperation(self):
        return self.__mathematical_operation

    @property
    def result(self):
        return self.__result

    def __str__(self):
        operation = ''
        operations = {1: 'Addition', 2: 'Subtraction', 3: 'Multiplication', 4: 'Division'}
        for num in operations:
            if num == self.__mathematical_operation:
                operation = operations[num]

        return f' Value one: {self.__value_one} \n Value two: {self.__value_two} \n Game Difficulty: {self.__game_difficulty} \n' \
               f' Mathematical Operation: {operation}'

    @property
    def generateValue(self):
        if self.__game_difficulty == 1:
            return randint(1, 10)
        elif self.__game_difficulty == 2:
            return randint(1, 100)
        return randint(1, 1000)

    @property
    def symbolOfTheOperation(self):
        if self.mathematicalOperation == 1:
            return '+'
        elif self.mathematicalOperation == 2:
            return '-'
        elif self.mathematicalOperation == 3:
            return '*'
        return '/'

    @property
    def generateResult(self):
        if 1 == self.mathematicalOperation:
            return self.__value_one + self.__value_two
        elif 2 == self.mathematicalOperation:
            return self.__value_one - self.__value_two
        elif 3 == self.mathematicalOperation:
            return self.__value_one * self.__value_two
        return self.__value_one / self.__value_two

    def verifyResult(self, player_answer):
        if player_answer == self.generateResult:
            print("Right answer!")
            return True
        else:
            print("Wrong answer!")
            print(f'{self.__value_one} {self.symbolOfTheOperation} {self.__value_two} = {self.__result}')
            return False

    def operation(self):
        print(f'{self.__value_one} {self.symbolOfTheOperation} {self.__value_two} = ?')
