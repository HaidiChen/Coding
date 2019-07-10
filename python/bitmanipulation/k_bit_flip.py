import collections
# This is a relatively straight forward approach
# not an optimized one
def k_bit_flip(array, K):

    if array is None or len(array) < 1 or len(array) > 30000:
        return -1
    if K < 1 or K > len(array):
        return -1

    result = 0

    def true_flip(array):
        if len(array) < K:
            for e in array:
                if e == 0:
                    return False
            return True

        for i in range(K):
            if array[i] == 0:
                flip(K, array, i)
                return true_flip(array[i:])

        return true_flip(array[K:])

    def flip(length, array, offset):
        nonlocal result
        result += 1
        for i in range(offset, offset + K):
            array[i] = array[i] ^ 1

    if true_flip(array):
        return result
    return -1

# alternative approach
# the solution above flipped some bits several times
# which could be unnecessary. e.g., if we have 10101,
# then we first flip to 11011, and then flip to 11100,
# notice that we flipped the third and fourth bit two
# times which has the same effect of not flipping them.
# So we need to avoid repeatedly flpping the same bit
# to improve the time complexity.

# In this approach, we use a queue to store all the
# indices of elements that are needed to be flipped. 
# The length of this queue could be up to K as only K
# elements could be affected by one flipping operation.
# In this queue, the first value represents the index 
# of oldest element we flipped. Let assume that it is
# a, so the maximum elements in the array that could be
# affected by this value is array[a:a + K - 1]. So, if we
# are looking at index i right now, we need to make sure 
# that i <= a + K - 1. Only under this case can the first
# value in the queue affect the array[i]. Otherwise, 
# If the i > a + K - 1, then it means that the the first 
# value of the queue has no effect on the array[i] and 
# we need to pop it out of the queue to keep the condition
# 'a + K - 1 >= i' true.

# Next, we think about the what is the meaning of the length
# this queue. It turns out to be the number of flips we have
# done on array[i] when we are looking at index i. Checkout 
# the table below and we will find an euqation which is 
# going to be helpful for future analysis. Suppose that we
# are looking at index i right now.

# ----------------------------------------------------------
# array[i]|len(queue) | array[i] + len(queue) | need flip? |
# --------|-----------|-----------------------|------------|
#    1    |           |         even          |     yes    |
# --------|    odd    |-----------------------|------------|
#    0    |           |         odd           |     no     |
# --------|-----------|-----------------------|------------|
#    1    |           |         odd           |     no     |
# --------|    even   |-----------------------|------------|
#    0    |           |         even          |     yes    |
# ----------------------------------------------------------

# Here is the explanation of this table.
# First, we need to understandd that the length of the queue
# means the number of times we have flipped on array[i] when
# we are looking at index i.

# Why? Because we know that i <= a + K - 1 where
# a is the first value of the queue. So, the array[i] is 
# flipped by every value in the queue. 
# e.g., if the queue is
# [1,2] and we are looking at index i = 3, the K is 3. Then the
# a + K - 1 = 1 + 3 - 1 = 3 >= i. We can tell by this that 
# array[3] has been flipped twice which is the length of the 
# queue. The first flip happened at when we were flipping 
# array[1] array[2] array[3]; the second happened at when we 
# were flipping array[2] array[3] array[4]. And now we are at
# array[3], so the array[3] has already been flipped length of 
# queue times.
# Another example is the queue is [3,5] and the K
# is 5 and we are looking at index i = 6. the a + K - 1 = 3 + 5
# - 1 = 7 >= i. Therefore, so far the array[6] has been flipped
# twice. The first happened at when we were flipping array[3],
# array[4], array[5], array[6], array[7]; the second happened
# at when we were flipping array[5], array[6], array[7],
# array[8], array[9]. And we are at array[6], you see that 
# array[6] has indeed been flipped twice before.

# We continue the explanation of the table. We now know that 
# the length of queue represents the times of flips we have
# done on array[i]. Consider two big cases:
# 1) the length of queue is odd, then we know that the array[i]
# has been flipped odd times which changes the array[i] to its
# complement(i.e., 1 -> 0, 0 -> 1). After these odd times of
# flipping, if array[i] is 0, we need to flip it again; if 
# array[i] is 1, we leave it there.
# 2) the length of queue is even, then we know that the array[i]
# has beeen flipped even times which doesn't change the array[i]
# (i.e., 0 -> 0, 1 -> 1). After even times of flipping, if the
# array[i] is 0, we need to flip it again; if array[i] is 1,
# we leave it there.
# Also, based on the table, we can see that when following 
# condition satisfies, we need to flip array[i]:
# array[i] + len(queue) % 2 == 0, or we can rewrite it as
# array[i] + len(queue) & 1 == 0. If we need to flip the array[i]
# then we need to add index i to the queue. Afterwards, go 
# to the next index and repeat the same process again(i.e., 
# check the queue to satisfy the 'a + K - 1 >= i'; check the 
# array[i] + len(queue) to see if it needs to be flipped)
# also, when we are flipping the array[i], we need to check that
# if i + K > n where n is the length of array, if so, we can 
# not flip the last K elements which means the k bit flipping is 
# failed.

# the time complexity of this approach is O(n) along with space
# complexity which is O(k)
def k_bit_flip2(array, k):
    queue = collections.deque()
    result = 0

    for i in range(len(array)):
        if queue and queue[0] + k == i:
            queue.popleft()

        if array[i] + len(queue) & 1 == 0:
            if i + k > len(array):
                return -1
            result += 1
            queue.append(i)

    return result
