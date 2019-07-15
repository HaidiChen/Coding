# compute the minimum distance between two words.

# compare the last character first, if they are equal, the
# distance of these two words equal to the distance of these
# two words without their last characters.
# if the last characters are not equal, the distance is going
# to be: 1 + min(dist1, dist2, dist3) where dist1 is the 
# distance between w1[:n-1] and w2[:n-1] and dist2 is the
# distance between w1[:n-1] and w2[:n] and dist3 is the distance
# between w1[:n] and w2[:n-1]

# to avoid repeatedly computing, we cache the intermediate
# distance value, in this case, we use a 2D array

# time complexity is O(ab) where a and b are the lengths of 
# word1 and word2 respectively.
# space complexity is also O(ab)

def levenshtein_distance(word1, word2):
    def compute_distance_between_prefixes(w1_idx, w2_idx):
        if w1_idx < 0:
            return w2_idx + 1
        elif w2_idx < 0:
            return w1_idx + 1
        if distance_between_prefixes[w1_idx][w2_idx] == -1:
            if word1[w1_idx] == word2[w2_idx]:
                distance_between_prefixes[w1_idx][w2_idx] = (
                        compute_distance_between_prefixes(
                            w1_idx - 1, w2_idx - 1))
            else:
                cand_dist1 = compute_distance_between_prefixes(
                        w1_idx - 1, w2_idx - 1)
                cand_dist2 = compute_distance_between_prefixes(
                        w1_idx, w2_idx - 1)
                cand_dist3 = compute_distance_between_prefixes(
                        w1_idx - 1, w2_idx)
                distance_between_prefixes[w1_idx][w2_idx] = (
                        1 + min(cand_dist1,cand_dist2,cand_dist3))

        return distance_between_prefixes[w1_idx][w2_idx]

    distance_between_prefixes = [[-1] * len(word2) for _ in word1]
    return compute_distance_between_prefixes(len(word1) - 1,
            len(word2) - 1)
