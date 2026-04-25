class Solution:
    def validPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1

        while(start<end):
            if s[start] != s[end]:
                skipL, skipR = s[start+1:end+1],s[start:end]

                return (skipL==skipL[::-1]) or (skipR==skipR[::-1])
            
            start,end=start+1,end-1
        
        return True
        