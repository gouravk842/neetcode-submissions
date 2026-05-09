class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for paran in s:
            if paran == ']':
                print("paran ] ",paran[-1])
                if len(stack)>=1 and stack[-1]=='[':
                    stack.pop()
                    print(stack)
                else:
                    return False
            elif paran == '}':
                if len(stack)>=1 and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif paran == ')':
                if len(stack)>=1 and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paran)
            print(stack)
        if len(stack)==0:
            return True
        
        return False