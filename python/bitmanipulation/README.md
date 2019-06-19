# bit tricks

1. extract the ith bit of x: (x >> i) & 1

2. extract the lowest bit that is 1 in x: x & ~(x - 1)

3. erase the lowest bit that is 1 in x: x & (x - 1)

4. flip ith bit in x: (1 << i) ^ x
