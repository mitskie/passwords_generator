import argparse

from generator.generate_password import *


def parser():
    parser_args = argparse.ArgumentParser(description='Простой генератор паролей')
    parser_args.add_argument('difficulty', type=int, help='Сложность пароля: '
                                                          '1 - пароль только из маленьких букв | '
                                                          '2 - пароль содержит большие и маленькие буквы | '
                                                          '3 - пароль содержит большие и маленькие буквы, и цифры | '
                                                          '4 - пароль содержит все возможные символы(кроме пробелов '
                                                          'и табов)')
    parser_args.add_argument('length', type=int, help='Длина пароля')
    parser_args.add_argument('count', type=int, help='Колличество паролей')

    return parser_args


if __name__ == '__main__':
    parser = parser()
    args = parser.parse_args()

    difficulty = args.difficulty
    length = args.length
    count = args.count

    passwords = []
    if difficulty == 1:
        passwords = [Generate.light_password(length) for i in range(count)]

    elif difficulty == 2:
        passwords = [Generate.easy_password(length) for i in range(count)]

    elif difficulty == 3:
        passwords = [Generate.medium_password(length) for i in range(count)]

    elif difficulty == 4:
        passwords = [Generate.hard_password(length) for i in range(count)]

    else:
        parser.print_help()

    for password in passwords:
        print(password)
