# find the longest palindromic substring in a given string.

# the solution is to choose one element or two as the centre of 
# the palindromic substring(if exists) on the go.

# time complexity is O(n^2)

class Solution:
    def longest_palindromic_substring(self, s):
        if len(s) == 0:
            return s

        self.max_length = 0
        self.start = 0

        for i in range(len(s)):
            self.expand_from_center(s, i, i)
            self.expand_from_center(s, i, i + 1)

        return s[self.start:self.start + self.max_length]

    def expand_from_center(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1

        if self.max_length < high - low - 1:
            self.max_length = high - low - 1
            self.start = low + 1

s = 'banana'
print(Solution().longest_palindromic_substring(s))
s = 'hello'
print(Solution().longest_palindromic_substring(s))
