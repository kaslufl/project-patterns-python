from .add import Add
from .number import Number
from .subtract import Subtract


class Parser:

    @classmethod
    def parse(cls, sentence: str):

        tokens = sentence.split(" ")

        tree = []
        while len(tokens) > 1:
            left_expression = cls.decide_left_expression(tree, tokens)

            operator = tokens.pop(0)

            right = tokens[0]
            right_expression = Number(right)
            if not tree:

                if operator == '-':
                    tree.append(Subtract(left_expression, right_expression))

                if operator == '+':
                    tree.append(Add(left_expression, right_expression))

                else:
                    raise ValueError("not valid operator")

            else:
                if operator == '-':
                    tree.append(Subtract(tree[-1], right_expression))
                if operator == '+':
                    tree.append(Add(tree[-1], right_expression))

        return tree.pop()

    @staticmethod
    def decide_left_expression(tree, tokens):
        left = tokens.pop(0)
        if not tree:
            left_expression = Number(left)
        else:
            left_expression = tree[-1]
        return left_expression
