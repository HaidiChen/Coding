# represent a value in a 1,0 strings in base (-2)

class Solution:
    def base_neg2(self, n):
        if n == 0:
            return '0'

        result = []
        while n:
            bit = n % 2
            n = n // 2
            n *= -1
            result.append(str(bit))

        return ''.join(reversed(result))
