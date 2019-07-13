import collections

# partitioning and sorting an array with many repeated entries

# the solution is to count the size of each distinct element
# in this array and store the counts in a hash table, and use
# another hash table to track the starting index of each 
# distinct element.

# time complexity is O(n) 
# space complexity is O(m) where m is the number of distinct
# elements

Person = collections.namedtuple('Person', ('age', 'name'))

def group_by_age(people):
    age_to_count = collections.Counter([person.age for person in people])
    age_to_offset, offset = {}, 0

    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[people[from_idx].age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]

