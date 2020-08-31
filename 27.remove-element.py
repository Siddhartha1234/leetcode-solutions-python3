class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ci = 0
        for x in nums:
            if x != val:
                nums[ci] = x
                ci += 1
        
        return ci
