def pretty_result(func):
    def inner(a, b):
        result = func(a, b)
        return f"Result is {result}"

    return inner



@pretty_result
def a_b(a, b):
    return a + b


@pretty_result
def a_mul_b(a, b):
    return a * b



print(a_b(2, 2))
print(a_mul_b(2, 2))