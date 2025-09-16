def plus(a, b):
    return a + b







def main():
    expression = input()
    elements = expression.split()
    a = Decimal(elements[0])
    b = Decimal(elements[2])
    if elements[1] == '-':
        result = minus(a, b)
    elif elements[1] == '+':
        result = plus(a, b)
    elif elements[1] == '*':
        result = product(a, b)
    elif (elements[1] == '/'):
        result = divide(a, b)
    return result

