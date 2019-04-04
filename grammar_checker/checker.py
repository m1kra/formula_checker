#!/usr/bin/python3
from lark import Lark, UnexpectedInput


class FormulaParser:
    grammars = {
        'maths':
        """
            start:
                | formula

            formula: summand
                | summand "+" formula
                | summand "-" formula

            summand: power
                | power "*" summand
                | power ":" summand
                | power "/" summand

            power: atom
                | atom "^" power

            atom: NUMBER
                | CNAME
                | "(" formula ")"
                | "{" formula "}"
                | "[" formula "]"

            %import common.CNAME
            %import common.NUMBER
            %import common.WS_INLINE
            %ignore WS_INLINE
        """,
        'braces': """
            start: formula

            formula: atom
                | atom "+" formula
                | atom "-" formula
                | atom "*" formula
                | atom "/" formula
                | atom ":" formula
                | atom "^" formula

            atom: (NUMBER|CNAME)*
                | "(" formula ")"
                | "[" formula "]"
                | "{" formula "}"

            %import common.CNAME
            %import common.NUMBER
            %import common.WS_INLINE
            %ignore WS_INLINE
        """
    }

    def __init__(self, parser_type: str = 'maths'):
        """
        :param parser_type: can be one of
                ['maths', 'braces']
            describes the type of the parser - weather it should
            parse input as mathematical formulas or text separated by braces.
            If parser_type == maths, full mathematical correctness is checked
                    e.g. '1+*[2]' isn't correct.
            If parser_type == braces, only the alignment of braces is checked
                    e.g. '1+*[2]' is correct.

        """
        grammar = self.grammars[parser_type]
        self.parser = Lark(grammar, parser='lalr')

    def check_formula_correctness(self, formula: str) -> bool:
        """
        :param formula: formula to check
        :returns: True or False depending on formula and parser type.
        """
        try:
            self.parser.parse(formula)
        except UnexpectedInput:
            return False
        return True


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='''Checks if formula is correct, according to'''
        ''' either mathematical rules or alignment of parentheses.'''
    )
    parser.add_argument(
        'formula', type=str, nargs=1,
        help='String, the formula to be checked.'
    )
    parser.add_argument(
        '--only-braces', dest='goal', action='store_false', default=True,
        help='Only alignment of braces should be taken into account.'
    )

    args = parser.parse_args()
    parser_type = 'maths' if args.goal else 'braces'
    formula = parser.parse_args().formula[0]

    formula_parser = FormulaParser(parser_type)
    print(formula_parser.check_formula_correctness(formula))
