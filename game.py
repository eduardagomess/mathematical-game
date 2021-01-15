from calculate import Calculate


def main():
    score = 0
    startTheGame(score)


def startTheGame(score):
    difficulty = int(input('Enter the difficulty of the game (1-3): '))

    calculate = Calculate(difficulty)

    print('Show the result of the operation below')
    calculate.operation()

    result = int(input('Enter the result: '))

    if calculate.verifyResult(result):
        score += 1

    if input('Continue the game (yes or no): ') == 'yes':
        startTheGame(score)
    else:
        print(f'You finished the game with {score} scores')


if __name__ == '__main__':
    main()
