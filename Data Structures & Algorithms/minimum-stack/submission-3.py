class MinStack:

    def __init__(self):
        self.stack = []
        self.minium = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minium[-1] if self.minium else val)
        self.minium.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minium.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minium[-1]
        
