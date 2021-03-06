class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        orig  = x
        y = 0
        while x != 0:
            y = y * 10 + x % 10
            x = x // 10
        
        return orig == y
