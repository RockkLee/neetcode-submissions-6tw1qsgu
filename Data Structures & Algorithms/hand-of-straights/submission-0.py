class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq_dic: dict[int, int] = defaultdict(int)
        for num in hand:
            freq_dic[num] += 1

        card_vals = list(freq_dic.keys())
        heapq.heapify(card_vals)

        while card_vals:
            for val in range(card_vals[0], card_vals[0] + groupSize):
                if val not in freq_dic:
                    return False
                freq_dic[val] -= 1
                if freq_dic[val] == 0:
                    if val != card_vals[0]:
                        return False
                    heapq.heappop(card_vals)
        return True
