class Solution:
    def countAndSay(self, n: int) -> str:
        curr = ['1']
        ind = 1
        nxt = []
        while ind < n:
            i, j, leng, nxt = 0, 1, len(curr), []

            while i < leng:
                while j < leng and curr[j] == curr[j - 1]:
                    j += 1

                nxt.append(str(j - i))
                nxt.append(curr[i])

                i = j
                j = i + 1
            curr = nxt
            ind += 1

        return ''.join(curr)
