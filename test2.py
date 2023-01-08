
from latex2sympy2 import latex2sympyStr


def main():
    testList = [
        r"x^1",
        r"x^2",
        r"x^3",
        r"x^4",
        r"x^{-1}",
        r"x^{-2}",
        r"e^1",
        r"e^2",
        r"e^3",
        r"e^4",
        r"e^{-1}",
        r"e^{-2}",

        "---",

        # r"f(x^2)",
        # r"\sqrt{\frac{1}{x}}",
        r"\sum_{n = 0}^{\infty} \frac{1}{n!}",
        r"\prod^c_{a = b} x^{a!}",
        r"\log{e^{2*x!}}"

    ]


    for tex in testList:
        if tex == '---':
            print("\n")
        else:
            math = latex2sympyStr(tex)
            print(tex, "-->", math)

main()