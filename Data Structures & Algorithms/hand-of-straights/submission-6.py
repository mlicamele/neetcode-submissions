class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        h = {}
        for i in range(len(hand)):
            if hand[i] not in h:
                h[hand[i]] = 1
            else:
                h[hand[i]] += 1
        hand.sort()
        p = 0
        while p < len(hand):
            c = hand[p]
            if h[c] == 0:
                p += 1
                continue
            for e in range(c, c + groupSize):
                if e in h and h[e] > 0:
                    h[e] -= 1
                else:
                    return False
            p += 1
        return True
            
        