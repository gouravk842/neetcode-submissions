class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for n in nums:
            count[n]=count.get(n,0)+1
        
        bucket=[[] for _ in range(len(nums)+1)]
        for n in count:
            bucket[count[n]].append(n)

        res=[]
        
        for i in range(len(bucket)-1,-1,-1):
            
            for n in bucket[i]:
                res.append(n)
                k-=1
                if k<=0:
                    break
            
            if k<=0:
                break
        return res
