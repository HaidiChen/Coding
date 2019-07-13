import collections
# given a set of events, determine the maximum number of 
# events that take place concurrently. events are represented
# in intervals.

# the solution is to sort all the endpoints, if the endpoint
# equals, the one that represents the start time comes first.
# and then iterate throught the sorted endpoint array, if 
# the element is start time, count plus one, otherwise count
# minus one, the max count throughout the whole iteration is
# the result we want.

# time complexity is dominated by sorting which is O(nlogn)
# space complexity is O(n)

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1)
# so that if times are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):
    # Builds an array of all endpoints
    E = ([Endpoint(event.start, True)
        for event in A] + [Endpoint(event.finish, False) for
            event in A])

    E.sort(key=lambda e: (e.time, not e.is_start))

    max_num_events, num_events = 0, 0

    for e in E:
        if e.is_start:
            num_event += 1
            max_num_events = max(num_events, max_num_events)
        else:
            num_events -= 1

    return max_num_events
