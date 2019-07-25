# given a magazine text and a letter text, determine if it's possible to build
# an anonymous letter using the letters from the magazine.

# the solution is to count the frequency of characters in the letter(we don't
# need to count the frequency of characters in the magazine, which is wasteful of
# space) using a hashtable, and then traverse through the magazine. if, at the
# end, the hashtable is empty, then we know we can construct the anonymous letter.
# otherwise, we can't.

# time complexity is O(n + m)
# space complexity is O(c) where c is the number of distinct characters in the
# letter.

import collections

class Solution(object):
    def is_letter_constructable_from_magazine(self, letter_text, magazine_text):
        char_frequency_for_letter = collections.Counter(letter_text)

        for c in magazine_text:
            if c in char_frequency_for_letter:
                char_frequency_for_letter[c] -= 1
                if char_frequency_for_letter[c] == 0:
                    del char_frequency_for_letter[c]
                    if not char_frequency_for_letter:
                        return True

        return not char_frequency_for_letter
