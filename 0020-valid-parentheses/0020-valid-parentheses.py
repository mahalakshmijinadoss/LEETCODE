class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        maps={')':'(','}':'{',']':'['}
        for char in s:
            if char in maps.values():
                stack.append(char)
            else:
                if not stack or stack[-1]!=maps[char]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0    
 