# find the longest substring without repeating characters

# we use a dictionary to track the latest index of encounterd
# elements. when we traverse the string, if we don't see a 
# duplicate, we add it and its index to the dictionary, and
# increase the count by one, if we see a duplicate, then find
# the previous index of this duplicate, say dup_idx, set the count to be
# the difference between current index and dup_idx, if the new count
# is greater than the final_count which is initialized as 0, the update
# the final_count. also we need to update the index of that duplicate
# in the dictionary

# time complexity is O(n)
# space complexity is O(n)

class Solution:
    def longest_substring(self, s):
        seen = {}
        final_count = 0
        count = 0
        for i in range(len(s)):
            if s[i] in seen:
                if count > final_count:
                    final_count = count
                count = i - seen[s[i]]
            else:
                count += 1

            seen[s[i]] = i

        return final_count


print(Solution().longest_substring('suchastupidhead'))

# this is the solution given by dailyinterviewpro

class Solution2:
    def length_of_longest_substring(self, s):
        letters = {}
        tail = -1
        head = 0
        result = 0

        while head < len(s):
            if s[head] in letters:
                tail = max(tail, letters[s[head]])
            letters[s[head]] = head
            result = max(result, head - tail)
            head += 1

        return result

print(Solution2().length_of_longest_substring('suchastupidhead'))
