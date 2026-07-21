class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        length=0
        i=len(s)-1
        while i>=0:
            if s[i]==" ":
                return length
            length+=1
            i-=1
        return length


        