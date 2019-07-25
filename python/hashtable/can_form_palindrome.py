# Test for palindromic permutations

# solution is to count the number of each distinct characters, each character
# should have an even number of occurence except only one character could have
# an odd times of appearance (when the palindrom has an odd length).

# time complexity is O(n)
# space complexity is O(c) where c is the number of distinct characters.

import collections

class Solution(object):
    def can_form_palindrome(self, s):
        return sum(v % 2 for v in collections.Counter(s).values()) <= 1
