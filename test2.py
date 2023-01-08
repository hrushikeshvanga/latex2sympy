
from latex2sympy2 import latex2sympyStr


def main():
    testList = [
        # r"x^1",
        # r"x^2",
        # r"x^3",
        # r"x^4",
        # r"x^{-1}",
        # r"x^{-2}",
        # r"e^1",
        # r"e^2",
        # r"e^3",
        # r"e^4",
        # r"e^{-1}",
        # r"e^{-2}",

        "---",

        r"\frac{\partial f(x,y)}{\partial x} ",
        r"\frac{df(x)}{dx} ",
        r"\frac{\partial}{\partial x} f(x,y) ",
        r"\frac{d}{dx} f(x)",

        # r"f(x)",
        # r"f(x+1)",
        # r"f(x^2)",
        # r"\sqrt{\frac{1}{x}}",
        # r"\sum_{n = 0}^{\infty} \frac{1}{n!}",
        # r"\prod^c_{a = b} x^{a!}",
        # r"\log{e^{2*x!}}"

        r"2x2y",
        r"2x2",
        r"2 4 2y",
        r"24 y",
        r"2 4 y",
        r"2 4 y",


    ]


    for tex in testList:
        if tex == '---':
            print("\n")
        else:
            math = latex2sympyStr(tex)
            print(tex, "-->", math)

main()