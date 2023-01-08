from latex2sympy2 import latex2sympyStr


def main():
    testList = [
        r"0",
        r"1",
        r"5-3",
        r"x^2",
        r"2x",
        r"a \cdot b",
        r"a \div b",
        r"a^2 + b^2 = c^2",
        r"\artanh(a)",
        r"\operatorname{ceil}(b)",
        r"\operatorname{arcsinh}(a)",
        r"\operatorname{arccosh}(a)",
        r"\operatorname{arctanh}(a)",
        r"\operatorname{arsinh}(a)",
        r"\operatorname{arcosh}(a)",
        r"\operatorname{artanh}(a)",
        r"\operatorname{gcd}(a, b)",
        r"\operatorname{lcm}(a, b)",
        r"\operatorname{gcd}(a,b)",
        r"\operatorname{lcm}(a,b)",
        r"\operatorname{floor}(a)",
        r"\frac{d}{dx} x",
        r"||x||",
        r"\int^b_a x dx",
        r"\ln x",
        r"aX^2 + bX + c",
        r'(4a)X^2 + (4a + 2b)X + (a + b + c)'
    ]
    for tex in testList:
        math = latex2sympyStr(tex)
        print(tex, math)


        math = latex2sympyStr(tex)
    #math = math.subs(variances)
    print("latex:", tex)
    # print("var:", variances)
    print("raw_math:", math)


    tex = r"a * b + c * d + e * c * d"
    # print("latex2latex:", latex2latex(tex))
    math = latex2sympyStr(tex)
    #math = math.subs(variances)
    print("latex:", tex)
    # print("var:", variances)
    print("raw_math:", math)

    matrix = r'''
    \begin{pmatrix}
        1 & 2 & 3 \\ 
        4 & 5 & 6 \\
        7 & 8 & 9 \\ 
    \end{pmatrix}
'''
#     math = latex2sympyStr(matrix)
#     #math = math.subs(variances)
#     brac = r'''(n*(n + 1) + n + 2 + 3 + 4 + 5)'''
#     # print("var:", variances)
#     print("raw_math:", math)

#     math = latex2sympyStr(brac)
    
#     print(math)

#     complicatedLatex = r'''\lim_{n\to3} \exp(-(n+1)^n)'''

#     unarytex = r'''+c'''
#   #  
#     math = latex2sympyStr(complicatedLatex)
    
#     print(math)


#     unarytex = r'''+d*3'''
#   #  
#     math = latex2sympyStr(unarytex)
    
#     print(math)

#     summation= r"\sum_{n=1}^{\infty} 2^{-n} = 1"

#     math = latex2sympyStr(summation)
    
#     equals = r"n=1"

#     math = latex2sympyStr(equals)
#     print(math)

#     text = r"\mathbb{R}^N"


    
#     print(math)
#     math = latex2sympyStr(text)

main()
