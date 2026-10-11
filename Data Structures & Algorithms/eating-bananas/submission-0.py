class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2
            
            if self.isValid(piles, h, mid):
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return k
    
    def isValid(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0

        if k == 0: return False

        for pile in piles:
            hours += math.ceil(pile / k)

        return hours <= h

    # Time: O(n log(m)) where m = max(piles)
    # Space: O(1)