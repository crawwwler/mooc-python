
def balanced_brackets(my_string: str):
    helper = '([)]'
    my_string = ''.join(['' if c not in helper else c for c in my_string])
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False
    return balanced_brackets(my_string[1:-1])


