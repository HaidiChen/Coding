class Solution(object):
    def sunset_buildings(self, sequence):
        BuildingWithHeight = collections.namedtuple(
                                  'BuildingWithHeight', ('id', 'height'))

        candidates = []

        for idx, height in enumerate(sequence):
            while candidates and height >= candidates[-1].height:
                candidates.pop()
            candidates.append(BuildingWithHeight(idx, height))

        return [candidate.id for candidate in reversed(candidates)]
