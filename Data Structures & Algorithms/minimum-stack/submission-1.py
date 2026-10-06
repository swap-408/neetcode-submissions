class MinStack:

    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        if not self.stack1: self.stack2.append(val)
        else: self.stack2.append(min(self.stack2[-1],val))
        self.stack1.append(val)

    def pop(self) -> None:
        if self.stack1:
            self.stack1.pop()
            self.stack2.pop()

    def top(self) -> int:
        if self.stack1: return self.stack1[-1]

    def getMin(self) -> int:
        if self.stack2: return self.stack2[-1]
        
