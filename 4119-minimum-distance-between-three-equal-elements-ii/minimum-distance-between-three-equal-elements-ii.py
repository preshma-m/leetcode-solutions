class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        last = [-1] * min_len
        second = [-1] * min_len
        min_dist = math.inf
        for i, num in enumerate(nums):
            if second[num] != -1:
                dist = i - second[num]
                if min_dist > dist:
                    min_dist = dist
            second[num] = last[num]
            last[num] = i
        if min_dist == math.inf:
            return -1
        return 2 * min_dist