class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_dic={}
        for c in s1:
            count_dic[c] = count_dic.get(c,0)+1
        
        l=0
        window_dict={}
        for r in range(len(s2)):
            window_dict[s2[r]] = window_dict.get(s2[r],0)+1

            if r-l+1 == len(s1):
                is_sub=True
                for c in s2[l:r+1]:
                    print(c)
                    if window_dict.get(c) != count_dic.get(c):
                        is_sub=False
                if is_sub:
                    return is_sub
                else:
                    window_dict[s2[l]]=window_dict[s2[l]]-1
                    l+=1
        return False
                    

        