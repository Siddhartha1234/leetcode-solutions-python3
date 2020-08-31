class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        
        if len(haystack) < len(needle):
            return res
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                res = i
                break
        
        return res
