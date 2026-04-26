class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length1=len(word1)
        length2=len(word2)
        new_word=''
        min_len=min(length1,length2)
        for i in range(0,min_len):
            new_word+=word1[i]
            new_word+=word2[i]
        
        if min_len==length1:
            new_word+=word2[min_len:]
        else:
            new_word+=word1[min_len:]
        
        return new_word

        