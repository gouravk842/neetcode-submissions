class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=0
        curr_sum=0
        curr_avg=0

        res=0
        for r in range(len(arr)):
            curr_sum+=arr[r]

            if r-l+1 == k:
                if curr_sum//k >= threshold:
                    res+=1
                
                curr_sum-=arr[l]
                l+=1
        return res