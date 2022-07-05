class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in set(nums):
            if nums.count(i)>n/3:
                ans.append(i)
        return ans