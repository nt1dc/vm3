from functions import *


def ask_a_b():
    a = 0
    b = 0
    while True:
        try:
            a = float(input("Введите точку а: "))
            b = float(input("Введите точку b: "))
            if a == b:
                print("введите разные числа")
                continue
            break
        except Exception:
            print("Введите число")
    return a, b


def ask_error():
    err = -1
    while True:
        try:
            err = float(input("Введите точность: "))
            if err <= 0:
                print("число должно быть больше нуля")
                continue
            break
        except Exception:
            print("\n")
    return err


def ask_function():
    num = -1
    while num not in functions_name.keys():
        for i in range(len(functions_name)):
            print(f"{i} : {functions_name[i][0]}")
        num = int(input("Выберите функцию: "))
    return num


def ask_method():
    method = -1
    while method not in methods.keys():
        try:
            for i in range(len(methods)):
                print(f"{i} : {methods[i][0]}")
            method = int(input("Выберите метод: "))
        except Exception:
            print("\n")
    return method
