class MinStack:

    def __init__(self):
        self.min_el_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_el_stack) == 0:
            self.min_el_stack.append(val)
        elif self.min_el_stack[-1] > val:
            self.min_el_stack.append(val)
        else:
            self.min_el_stack.append(self.min_el_stack[-1])

    def pop(self) -> None:

        self.min_el_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_el_stack[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
