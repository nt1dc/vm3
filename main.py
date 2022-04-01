import functions
from calculations import *
from io_functions import *



if __name__ == "__main__":
    print("опять уникальная возможность ввести свою функцию ^_^ "
          "введи 1 если хочешь  ) ")
    if int(input()) == 1:
        create_own_function()
    func = functions_name[ask_function()][1]
    a, b = ask_a_b()
    epsilon = ask_error()
    # случай, если а оказывается больше b: интеграл будет равен интегралу с противоположным знаком
    mul = 1
    if a > b:
        mul = -1
        a, b = b, a

    method = functions.methods[ask_method()][1]

    ans, partition, err = calc_integral(func, method, a, b, epsilon, 2)
    print(f"Получен ответ {ans * mul}, {partition} разбиений")
