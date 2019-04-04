#!/usr/bin/python3


def are_parentheses_correct(formula):
    return check_scopes(
        formula,
        {'(': ')', '[': ']', '{': '}'}
    )


def check_scopes(formula: str, tokens: dict) -> bool:
    """
    Checks if scopes in `formula` are aligned properly.
    :param formula: string to check
    :param tokens: a dictionary of the form:
        {'scope_opening_symbol': 'scope_closing_symbol',}
    """
    openings = tokens.keys()
    closings = tokens.values()
    stack = []
    for symbol in formula:
        if symbol in openings:
            stack.append(symbol)
        if symbol in closings:
            if not stack:
                return False
            last_opening = stack.pop()
            if tokens[last_opening] != symbol:
                return False
    return not stack


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='''Checks if the parentheses "(), [], {}"'''
        ''' are correctly placed in the input formula.'''
    )
    parser.add_argument(
        'formula', type=str, nargs=1,
        help='String, the formula to be checked.'
    )
    formula = parser.parse_args().formula[0]
    print(are_parentheses_correct(formula))
