# given an input array consisted of custom data type,
# and the array is not sorted, remove the duplicates
# from the array and result the result.

# e.g., array A stores (firstName, lastName), remove
# the firstName duplicates

# one solution is to use the hash table, using the
# hash function that returns the same hash value
# when the firstName is the same. time complexity of
# this solution is O(n) where n is the length of 
# array. and space complexity could be O(n) as well.

# another solution is to do this in place. first we
# sort the array and then do a linear scan and put
# distinct values into the result. the time complexity
# is dominated by the sorting algorithm which is
# O(nlogn), but the space complexity is O(1)

class Name:
    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        return (self.first_name < other.first_name if
                self.first_name != other.first_name
                else self.last_name < other.last_name)


def eliminate_duplicates(A):
    A.sort()
    prev = 0
    for name in A[1:]:
        if name != A[prev]:
            A[prev + 1] = name
            prev += 1

    del A[prev + 1:]
