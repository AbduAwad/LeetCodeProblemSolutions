class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.min = None

    def push(self, val: int) -> None:
        if (self.size == 0):
            self.min = val
        else:
            if self.min > val:
                self.min = val
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return
        if self.size == 1:
            self.stack.pop()
            self.size -= 1
            self.min = None
            return
        if (self.min == self.stack[self.size-1]):
            self.stack.pop()
            self.size -= 1
            self.min = self.stack[0]
            for i in range(self.size):
                if (self.min > self.stack[i]):
                    self.min = self.stack[i]
            return
        self.stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()