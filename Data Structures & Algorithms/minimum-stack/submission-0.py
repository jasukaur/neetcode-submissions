class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal:
            self.minVal.append(min(val,self.minVal[-1]))
        else:
            self.minVal.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minVal.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:

        return self.minVal[-1]
        
