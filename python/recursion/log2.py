# compute the integer part of the base-two logarithm of n using
# only addition and integer division

class Solution(object):
    def log2(self, num):
        return self._helper(num)

    def _helper(self, num):
        if num == 1:
            return 0
        return 1 + self._helper(num // 2)
