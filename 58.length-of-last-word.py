class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        last = len(s)
        
        while j >= 0 and s[j] == ' ':
            j -= 1
            last -= 1
            
        while j >= 0 and s[j] != ' ':
            j -= 1
        
        return last - j - 1
