class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        j=len(nums)-1
        while j>0:
            if nums[j]>nums[i]:
                break
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=sorted(nums[i+1:])