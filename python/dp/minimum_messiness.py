# calculate the minimum messiness of putting words
# in multiple lines.

# the solution is:
# if we want to calculate the messiness after putting
# the ith word. we could either put only the ith word 
# in the last line, or we could put several words that
# are prior to the ith word in the last line as well
# and compare the messiness among each other.
# so the solution looks like the following equation:
# M(i) = min(M(i), M(j, i)) where j <= i and i-j+1 is 
# the largest number of words we can put in the last
# line.

# the time complexity is O(ln) where l is the length
# of line and n is the number of words.
# the space complexity is O(n)

class Solution:
    def minimum_messiness(self, words, line_length):
        num_remaining_blanks = line_length - len(words[0])

        min_messiness = ([num_remaining_blanks ** 2] + 
                [float('inf')] * (len(words) - 1))

        for i in range(1, len(words)):
            num_remaining_blanks = line_length - len(words[i])
            min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks ** 2

            for j in reversed(range(i)):
                num_remaining_blanks -= len(words[j]) + 1
                if num_remaining_blanks < 0:
                    break
                first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
                current_line_messiness = num_remaining_blanks ** 2 
                min_messiness[i] = min(min_messiness[i], 
                        current_line_messiness + first_j_messiness)

        return min_messiness[-1]
