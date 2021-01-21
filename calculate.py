from random import randint


class Calculate:

    def __init__(self, game_difficulty):
        self.__game_difficulty = game_difficulty
        self.__value_one = self.generateValue()
        self.__value_two = self.generateValue()
        self.__mathematical_operation = randint(1, 3)
        self.__result = self.generateResult()
        self.__math_operations = {1: ['Addition', '+'], 2: ['Subtraction', '-'], 3: ['Multiplication', '*'], 4: ['Division', '/']}

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
        for num in self.__math_operations:
            if num == self.__mathematical_operation:
                operation = self.__math_operations[num][0]

        return f' Value one: {self.__value_one} \n Value two: {self.__value_two} \n Game Difficulty: {self.__game_difficulty} \n' \
               f' Mathematical Operation: {operation}'

    def generateValue(self):
        if self.__game_difficulty == 1:
            return randint(1, 10)
        elif self.__game_difficulty == 2:
            return randint(1, 100)
        return randint(1, 1000)

    def symbolOfTheOperation(self):
        return self.__math_operations[self.mathematicalOperation][1]

    def generateResult(self):
        operations = {1: self.__value_one + self.__value_two, 2: self.__value_one - self.__value_two,
                           3: self.__value_one * self.__value_two, 4: self.__value_one / self.__value_two}

        return operations[self.mathematicalOperation]

    def verifyResult(self, player_answer):
        if player_answer == self.generateResult():
            print("Right answer!")
            return True
        else:
            print("Wrong answer!")
            print(f'{self.__value_one} {self.__math_operations[self.mathematicalOperation][1]} {self.__value_two} = {self.result}')
            return False

    def operation(self):
        print(f'{self.__value_one} {self.__math_operations[self.mathematicalOperation][1]} {self.__value_two} = ?')
