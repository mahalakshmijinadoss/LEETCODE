class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        maps=defaultdict(int)
        sets=set()
        for num in arr:
            maps[num]+=1
        for i in maps.values():
            if i in sets:
                return False
            else:
                sets.add(i)
        return True

        