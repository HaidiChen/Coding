# compute the binomial coefficient(i.e., the number of ways to choose
# k elements out of n candidates)

# the solution is to break this down.
# to choose k out of n, the result is the same as choosing k out of n-1
# (i.e., without containing the nth element) plus choosing k-1 out of 
# n-1 (i.e., containing the nth element), so it looks like this:
# f(n, k) = f(n - 1, k) + f(n - 1, k - 1), and we need to use cache to 
# avoid repeated computations.

# the time complexity is O(nk)
# the space complexity is also O(nk) as it is dominated by the cache
# array we are using

class Solution:
    def compute_binomial_coefficient(self, n, k):
        self.x_choose_y = [[0] * (k + 1) for _ in range(n + 1)]
        
        return self._compute_x_choose_y(n,k)

    def _compute_x_choose_y(self, x, y):
        if y in (0, x):
            return 1

        if self.x_choose_y[x][y] == 0:
            without_y = self._compute_x_choose_y(x - 1, y)
            with_y = self._compute_x_choose_y(x - 1, y - 1)
            self.x_choose_y[x][y] = without_y + with_y

        return self.x_choose_y[x][y]
