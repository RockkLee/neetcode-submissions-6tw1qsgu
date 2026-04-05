class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for val0, val1, val2 in triplets:
            # Unusable triplet: would exceed target after max-merge
            if val0 > target[0] or val1 > target[1] or val2 > target[2]:
                continue

            if val0 == target[0]:
                good.add(0)
            if val1 == target[1]:
                good.add(1)
            if val2 == target[2]:
                good.add(2)

        return len(good) == 3
