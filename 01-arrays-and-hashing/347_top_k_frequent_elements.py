# LeetCode 347: Top K Frequent Elements
# Time Complexity: O(N log K) or O(N)
# Space Complexity: O(N)

import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        sorted_numbers = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return sorted_numbers[:k]
