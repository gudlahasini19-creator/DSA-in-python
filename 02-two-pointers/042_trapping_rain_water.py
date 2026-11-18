class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        l=0
        r=len(height)-1
        left_max=height[l]
        right_max=height[r]
        water=0
        while (l<r):
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1
        return water
        