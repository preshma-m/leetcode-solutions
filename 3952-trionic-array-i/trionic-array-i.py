class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        i = 0

        # 1) strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # must have at least one increase
        if i == 0:
            return False

        # 2) strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        # must have at least one decrease
        if i == 0 or i == n - 1:
            return False

        # 3) strictly increasing again
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # must reach end
        return i == n - 1
