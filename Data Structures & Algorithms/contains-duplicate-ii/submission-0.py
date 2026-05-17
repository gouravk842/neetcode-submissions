class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp={}

        for i, a in enumerate(nums):
            if a in mp and i-mp[a] <=k:
                return True
            mp[a]=i
        return False

        