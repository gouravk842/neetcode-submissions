class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for operation in logs:
            if operation == '../':
                if len(stack)>0:
                    stack.pop()
            elif operation == './':
                continue
            else:
                stack.append(operation)
        return len(stack)