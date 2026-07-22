class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            add = numbers[l] + numbers[r]

            if add == target:
                return [l + 1, r + 1]
            elif add < target:
                l += 1
            else:
                r -= 1