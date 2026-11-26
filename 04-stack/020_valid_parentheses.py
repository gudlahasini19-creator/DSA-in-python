class Solution(object):
    def isValid(self, s):
        stack=[]
        match={')':'(','}':'{',']':'['}
        for i in s:
            if i in match:
                if stack and stack[-1]==match[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0      