class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1={}
        for s1 in s:
            if s1 not in dict1:
                dict1[s1]=1
            else:
                dict1[s1]+=1
        for s2 in t:
            if s2 in dict1:
                dict1[s2]-=1
            else:
                return False
        for v in dict1.values():
            if v != 0:
                return False
        return True



        