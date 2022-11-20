def calculate(expression: str):
    return calculate_rpn(convert_to_rpn(expression))


def convert_to_rpn(expression: str):
    index = 0
    output = []
    operators = []
    while symbol := read_next_symbol(index, expression):
        if symbol.isdigit():
            output.append(symbol)
        elif is_operator(symbol):
            while operators and should_go_before(operators[-1], symbol):
                output.append(operators.pop())
            operators.append(symbol)
        elif is_bracket(symbol):
            raise Exception('Brackets are not implemented!')
        index += len(symbol)
    while operators:
        output.append(operators.pop())
    return output


def calculate_rpn(rpn: list[str]):
    result = []
    for element in rpn:
        if element.isdigit():
            result.append(int(element))
        elif is_operator(element):
            result.append(apply_operator(result.pop(), result.pop(), element))
    return int(result[0])


def apply_operator(a: int, b: int, op: str):
    if op == '+':
        return b + a
    elif op == '-':
        return b - a
    elif op == '*':
        return b * a
    elif op == '/':
        return b / a
    else:
        raise Exception(f'Unknown operator {op}')


def read_next_symbol(index: int, expression: str):
    if index >= len(expression):
        return None
    first = expression[index]
    if is_operator(first) or is_bracket(first):
        return first
    elif first.isdigit():
        return read_first_number(expression[index:])
    else:
        raise Exception(f'Unexpected symbol: {first}')


def should_go_before(candidate, compare_to):
    assert candidate in ('+', '-', '*', '/')
    assert compare_to in ('+', '-', '*', '/')
    return compare_to == '-' or (compare_to == '/' and candidate in ('*', '/'))


def is_operator(value: str):
    assert len(value) == 1
    return value in ('+', '-', '*', '/')


def is_bracket(value: str):
    assert len(value) == 1
    return value in ('(', ')')


def read_first_number(expression: str):
    number = ''
    for c in expression:
        if c.isdigit():
            number += c
        else:
            return number
    return number
