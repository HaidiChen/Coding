# compute the Reverse Polish Notation Expression.

# time complexity is O(n) where n is the number of characters in the
# expression

class Solution(object):
    def evaluate(self, expression):
        results = []
        DELIMITER = ','
        OPERATORS = {
                '+': lambda y, x: x + y,
                '-': lambda y, x: x - y,
                '*': lambda y, x: x * y,
                '/': lambda y, x: x // y,
                }

        for token in expression.split(DELIMITER):
            if token in OPERATORS:
                results.append(OPERATORS[token](
                    results.pop(), results.pop()))
            else:
                results.append(int(token))

        return results[-1]
