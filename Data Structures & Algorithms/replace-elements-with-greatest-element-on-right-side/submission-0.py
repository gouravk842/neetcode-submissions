class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)):
            sub_arr=arr[i+1:]
            if len(sub_arr)==0:
                continue
            max_number=max(sub_arr)
            arr[i]=max_number
        arr[-1]=-1
        return arr
        