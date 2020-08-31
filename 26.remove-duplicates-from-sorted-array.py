class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, leng = 1, 1, len(nums)
        if leng == 1:
            return 1
        
        while i < leng and j < leng:
            while j < leng and nums[j] == nums[j - 1]:
                j += 1
        
            if j < leng:
                nums[i] = nums[j]
                i += 1
                j += 1
        
        return i
                
                
