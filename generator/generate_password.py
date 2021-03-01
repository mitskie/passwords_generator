import secrets
import string
from enum import auto


class Difficulty(auto):
    LIGHT = string.ascii_lowercase
    EASY = string.ascii_letters
    MEDIUM = EASY + string.digits
    HARD = MEDIUM + string.punctuation


class Generate:
    @staticmethod
    def light_password(length):
        password = ''.join(secrets.choice(Difficulty.LIGHT) for i in range(length))
        return password

    @staticmethod
    def easy_password(length):
        password = ''.join(secrets.choice(Difficulty.EASY) for i in range(length))
        return password

    @staticmethod
    def medium_password(length):
        password = ''.join(secrets.choice(Difficulty.MEDIUM) for i in range(length))
        return password

    @staticmethod
    def hard_password(length):
        password = ''.join(secrets.choice(Difficulty.HARD) for i in range(length))
        return password
