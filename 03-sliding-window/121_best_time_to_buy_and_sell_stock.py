class Solution(object):
    def maxProfit(self, prices):
        i=0
        j=1
        maxp=0
        while j<=len(prices)-1:
            if prices[i]<prices[j]:
                profit=prices[j]-prices[i]
                maxp=max(profit,maxp)
            else:
                i=j
            j+=1
        return maxp
        