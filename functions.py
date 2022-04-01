import calculations
import numpy as np

functions_name = {
    0: ("x^3 + 2.28x^2 - 1.934x - 3.907", lambda x: x ** 3 + 2.28 * (x ** 2) - 1.934 * x - 3.907),
    1: ("x^2 - 3x - 2", lambda x: x ** 2 - 3 * x - 2),
    2: ("sin(x) - cos(x) + 0.2x", lambda x: np.sin(x) - np.cos(x) + 0.2 * x)
}

methods = {
    0: ("метод прямоугольника левого", calculations.squad_method_left),
    1: ("метод прямоугольника правого", calculations.squad_method_right),
    2: ("метода прямоугольника среднего", calculations.squad_method_mid),
    3: ("метод трапеций", calculations.trapezoid_method)
}


def create_own_function():
    while True:
        try:
            zxc = input("Введите функцию :")
            asd = zxc
            zxc = zxc.replace("sin", "np.sin")
            zxc = zxc.replace("cos", "np.cos")
            zxc = zxc.replace("tg", "np.tg")
            zxc = zxc.replace("ctg", "np.ctg")
            temp = lambda x: eval(zxc)
            temp.__call__(1)
            functions_name[len(functions_name)] = (asd, temp)
            return
        except Exception:
            print("давай по новой, миша, все *****!\n ")
