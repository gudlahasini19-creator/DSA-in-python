import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output=[]
        q=collections.deque()
        l=0
        for r in range(len(nums)):
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
        return output
        
        