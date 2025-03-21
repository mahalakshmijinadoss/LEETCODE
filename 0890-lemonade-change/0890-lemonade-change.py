class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        maps=defaultdict(int)
        for bill in bills:
            if bill==5:
                maps[bill]+=1
            if bill==10:
                maps[bill]+=1
                maps[5]-=1
                if maps[5]<0:
                    return False
            if bill== 20:
                if maps[5]>=1 and maps[10]>=1:
                    maps[5]-=1
                    maps[10]-=1
                elif maps[5]>=3:
                    maps[5]-=3
              
                else:
                    return False

        return True
                





        