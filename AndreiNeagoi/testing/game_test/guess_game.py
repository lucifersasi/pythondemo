import random


def guess_run(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print(f"you are damn lucky !! it's {answer}")
            return True
        else:
            print(f"Oops it was {answer}")
            return False

    else:
        print('Hey!!, I said 1~10')
        return False


if __name__ == '__main__':

    while True:
        answer = random.randint(1, 10)
        try:
            guess = int(input('guess a number 1~10 '))
            if (guess_run(guess, answer)):
                break

        except ValueError:
            print('please enter a number')
            continue
