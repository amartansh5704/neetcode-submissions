class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        d = Counter(hand)
        for k in hand:
            if d[k] != 0:
                d[k] -= 1
                for i in range(1, groupSize):
                    t = k + i
                    if t not in d and d[t] == 0:
                        return False
                    d[t] -= 1
        return True