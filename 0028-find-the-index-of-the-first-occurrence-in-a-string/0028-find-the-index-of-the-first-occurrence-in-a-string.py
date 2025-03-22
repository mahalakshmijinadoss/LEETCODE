class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        check=""
        start_window=0
        for s in haystack:
            check+=s
            if len(check)==len(needle):
                if check==needle:
                    return start_window
                else:
                    start_window+=1
                    check=check[1:]
        return -1

    

      

        