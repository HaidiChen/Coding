# using bit array to generate the power set
import math

def generate_power_set(S):
    power_set = []

    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1

        power_set.append(subset)

    return power_set

def main():
    example = [5,3,4]
    indices = generate_power_set(example)
    for x in indices:
        for i in range(len(x)):
            x[i] = example[x[i]]

    print(indices)


if __name__ == '__main__':
    main()
