# Arithmetic Expression Evaluator

def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return 0


def apply_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by Zero"
        return a / b


def evaluate(expression):
    values = []
    operators = []

    i = 0
    while i < len(expression):

        if expression[i] == ' ':
            i += 1
            continue

        if expression[i].isdigit():
            value = 0

            while i < len(expression) and expression[i].isdigit():
                value = value * 10 + int(expression[i])
                i += 1

            values.append(value)
            continue

        elif expression[i] == '(':
            operators.append(expression[i])

        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                b = values.pop()
                a = values.pop()
                op = operators.pop()
                values.append(apply_operation(a, b, op))

            operators.pop()

        else:
            while (operators and
                   precedence(operators[-1]) >= precedence(expression[i])):

                b = values.pop()
                a = values.pop()
                op = operators.pop()

                values.append(apply_operation(a, b, op))

            operators.append(expression[i])

        i += 1

    while operators:
        b = values.pop()
        a = values.pop()
        op = operators.pop()
        values.append(apply_operation(a, b, op))

    return values[0]


expression = input("Enter Arithmetic Expression: ")
result = evaluate(expression)
print("Result =", result)
