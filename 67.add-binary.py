class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = (len(b) - len(a)) * '0' + a
        else:
            b = (len(a) - len(b)) * '0' + b

        res = ''
        carry = 0
        for i in reversed(range(len(a))):
            res = str((int(a[i]) + int(b[i]) + carry) % 2) + res
            carry = (int(a[i]) + int(b[i]) + carry) // 2

        if carry > 0:
            res = '1' + res

        return res
