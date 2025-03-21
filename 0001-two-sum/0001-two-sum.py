class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in complement_dict:
                return[complement_dict[complement],i]
            else:
                complement_dict[nums[i]]=i

        