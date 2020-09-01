from itertools import permutations as pr
from functools import reduce


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        x = ':'.join(
            reduce(
                lambda a, b: max([a, b]),
                filter(
                    lambda t: t[0] <= '23' and t[1] <= '59',
                    map(
                        lambda x:
                        (str(x[0]) + str(x[1]), str(x[2]) + str(x[3])),
                        list(pr(A)))), ('', '')))
        return x if x != ':' else ''
