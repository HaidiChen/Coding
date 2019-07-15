# validate a string of brackets.
# e.g., "{(())[]{}}" is valid while "[{]}()" is not

# the solution is to use stack to store the opening
# bracket, and when we encounter a closing one, try
# to match it with the top bracket in the stack, if
# matches, keep going, otherwise, not valid. at the
# end of traversing, if the stack is not empty, it's
# also not valid.

# time complexity is O(n)
# space complexity is O(k) where k is the number of
# opening brackets.

class Solution:
    def is_valid(self, s):
        openParens = ['(', '{', '[']
        closingParens = [')', '}', ']']
        stack = []
        for char in s:
            if char in openParens:
                stack.append(char)
            elif char in closingParens:
                if len(stack) <= 0:
                    return False
                if (openParens.index(stack.pop()) !=
                        closingParens.index(char)):
                    return False

        return len(stack) == 0

print(Solution().is_valid('{()()}[]'))

print(Solution().is_valid('{())}[]'))

print(Solution().is_valid(''))
