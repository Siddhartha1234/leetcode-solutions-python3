class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        ans = [-1, -1]
        for ind in range(len(nums)):
            if nums[ind] in ref:
                ref[nums[ind]].append(ind)
            else:
                ref[nums[ind]] = [ind]
        
        for k, v in ref.items():
            if target - k == k:
                if len(v) >= 2:
                    ans = [v[0] , v[1]]
                    break
            elif target - k in ref:
                ans = [ v[0], ref[target - k][0]]
                break       	 
        return ans
