class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, value):
        self.stack.append(value)
        value=min(value,self.minstack[-1] if self.minstack else value)
        self.minstack.append(value)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minstack[-1]
        
        


