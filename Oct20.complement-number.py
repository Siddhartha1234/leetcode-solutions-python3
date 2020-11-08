class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        res = 0 
        po = 1
        while N != 0:
            res += po * ( 1 - N % 2 )
            po *= 2
            N //= 2
        return res 
