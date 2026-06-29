class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Count frequency
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        arr = list(freq.items())

        # Bubble sort (descending by frequency)
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j][1] < arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        ans = []

        for i in range(k):
            ans.append(arr[i][0])

        return ans