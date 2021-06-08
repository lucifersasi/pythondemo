import random
from sys import argv
while True:
    try:
        print('e to exit')
        pc_num = random.randint(int(argv[1]), int(argv[2]))
        # print(pc_num)
        user_num = input(f'Enter a number from {int(argv[1])} to {int(argv[2])}: ')

        if user_num == 'e':
            break
        elif 1 <= int(user_num) <= 10:
            if int(user_num) == pc_num:
                print("You're Goddamn right!")
                break
            else:
                print(f'oops its {pc_num} ')
                continue
        else:
            print('enter b/w 1 to 10')
            continue

    except ValueError:
        print('please enter a number')
        continue
