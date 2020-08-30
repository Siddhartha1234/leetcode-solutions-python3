class Solution:
    def reverse(self, x: int) -> int:
        neg = ( x < 0 )
        x = abs(x)
        y = 0
        while x != 0:
            y = y * 10 +  x % 10
            x = x // 10
        
        lim = 1 << 31
    
        if neg:
            ans = -y
        else:
            ans = y
        
        if -lim <= ans <= lim  - 1:
            return ans
        else:
            return 0
        
