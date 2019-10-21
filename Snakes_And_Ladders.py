from PIL import Image
import random

end = 100


def show_board():
    img = Image.open('slb.jpg')
    img.show()


def check_ladder(points):
    if points == 8:
        print('Ladder')
        return 26
    elif points == 21:
        print('Ladder')
        return 82
    elif points == 43:
        print('Ladder')
        return 77
    elif points == 50:
        print('Ladder')
        return 91
    elif points == 54:
        print('Ladder')
        return 93
    elif points == 62:
        print('Ladder')
        return 96
    elif points == 66:
        print('Ladder')
        return 87
    elif points == 80:
        print('Ladder')
        return 100
    else:
        return points


def check_snake(points):
    if points == 44:
        print('Snake')
        return 22
    elif points == 46:
        print('Snake')
        return 5
    elif points == 48:
        print('Snake')
        return 9
    elif points == 52:
        print('Snake')
        return 11
    elif points == 55:
        print('Snake')
        return 7
    elif points == 59:
        print('Snake')
        return 17
    elif points == 64:
        print('Snake')
        return 36
    elif points == 69:
        print('Snake')
        return 33
    elif points == 73:
        print('Snake')
        return 1
    elif points == 83:
        print('Snake')
        return 19
    elif points == 92:
        print('Snake')
        return 51
    elif points == 95:
        print('Snake')
        return 24
    elif points == 98:
        print('Snake')
        return 28
    else:
        return points


def reached_end(points):
    if points == end:
        return True
    else:
        return False


def play():
    p1_name = input('Enter name of Player 1: ')
    p2_name = input('Enter name of Player 2: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    while 1:
        if turn % 2 == 0:
            print(p1_name, 'your turn.')
            c = input('Press 1 to continue, 0 to quit: ')
            if c == 0:
                print(p1_name, 'scored:', pp1)
                print(p2_name, 'scored:', pp2)
                print('Quitting the game! Thank you for playing.')
                break
            dice = random.randint(1, 6)
            print('Dice showed:', dice)
            pp1 = pp1+dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            if pp1 > end:
                pp1 = end
            print(p1_name, 'your score:', pp1)
            if reached_end(pp1):
                print(p1_name, 'has won!')
                break
        else:
            print(p2_name, 'your turn.')
            c = input('Press 1 to continue, 0 to quit: ')
            if c == 0:
                print(p1_name, 'scored:', pp1)
                print(p2_name, 'scored:', pp2)
                print('Quitting the game! Thank you for playing.')
                break
            dice = random.randint(1, 6)
            print('Dice showed:', dice)
            pp2 = pp2 + dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            if pp2 > end:
                pp2 = end
            print(p2_name, 'your score:', pp2)
            if reached_end(pp2):
                print(p2_name, 'has won!')
                break
        turn = turn+1


show_board()
play()
