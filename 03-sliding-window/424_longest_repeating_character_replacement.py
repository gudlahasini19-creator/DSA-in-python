class Solution(object):
    def characterReplacement(self, s, k):
        count={}
        maxi=0
        l=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
        