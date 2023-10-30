class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            return -1
        ans = 10**5+1
        dic = {}
        for i, card in enumerate(cards):
            if card in dic:
                # ans = min(ans, i - dic[card] + 1)
                ans = min(ans, i - dic[card])

            dic[card] = i
        
        # return ans % (10**6+1) or -1
        return ans +1