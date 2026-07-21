class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        first=0
        for c in t:
            if first>=len(s):
                return False
            if s[first]==c:
                first+=1
                if first==len(s):
                    return True
        return False
        