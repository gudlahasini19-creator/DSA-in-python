class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        t_count={}
        for i in range(len(t)):
            t_count[t[i]]=1+t_count.get(t[i],0)
        window={}
        need =len(t_count)
        have=0
        res=[-1,-1]
        res_len=float('inf')
        l=0
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            i=s[r]
            if i in t_count and window[i]==t_count[i]:
                have+=1
            while have==need:
                if (r-l+1)<res_len:
                    res=[l,r]
                    res_len=r-l+1
                window[s[l]]-=1
                if s[l] in t_count and window[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res_len!=float('inf') else ""