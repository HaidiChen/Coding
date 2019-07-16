# the knapsack problem.

# let's say if we choose item k, consider following situations:
# if the weight of item k is less than the capacity available,
# then we know that the value at this point is either:
# A. the current item value + total value of other items
# (i.e., v[i][w] = Vi + v[i-1][w - Wi])
# or
# B. total value of items without this item.
# (i.e., v[i][w] = v[i-1][w])
# so we need to choose the bigger one out of above two.
# if the weight of item k is greater than the capacity available,
# then there's only one choice we can make here:
# C. total value of items without this item.
# (i.e., v[i][w] = v[i-1][w])

class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value

class Solution:
    def optimum_subject_to_capacity(self, items, capacity):
        self.V = [[-1] * (capacity + 1) for _ in items]
        self.items = items

        return self._optimum_subject_to_item_and_capacity(
                len(items) - 1, capacity)

    def _optimum_subject_to_item_and_capacity(self, k, avail_capacity):
        if k < 0:
            return 0

        if self.V[k][avail_capacity] == -1:
            without_curr_item = self._optimum_subject_to_item_and_capacity(
                    k - 1, avail_capacity)
            with_curr_item = ( 0 if avail_capacity < self.items[k].weight
                    else self.items[k].value + 
                    self._optimum_subject_to_item_and_capacity(
                    k - 1, avail_capacity - self.items[k].weight))

            self.V[k][avail_capacity] = max(without_curr_item, with_curr_item)

        return self.V[k][avail_capacity]
