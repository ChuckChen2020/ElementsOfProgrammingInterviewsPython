class Stack:
    class MaxWithCount:
        def __init__(self, maximum, count):
            self.max, self.count = maximum, count

    def __init__(self):
        self._element_stack = []
        self._max_with_count_stack = []

    def empty(self):
        return len(self._element_stack) == 0 and len(self._max_with_count_stack) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._max_with_count_stack[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        popped = self._element_stack.pop()
        if popped == self.max():
            if self._max_with_count_stack[-1].count == 1:
                self._max_with_count_stack.pop()
            else:
                self._max_with_count_stack[-1].count -= 1
        return popped

    def push(self, x):
        if self.empty():
            self._max_with_count_stack.append(self.MaxWithCount(x, 1))
        else:
            if x > self.max():
                self._max_with_count_stack.append(self.MaxWithCount(x, 1))
            elif x == self.max():
                self._max_with_count_stack[-1].count += 1
        self._element_stack.append(x)


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert(stack.pop() == 9)
    assert(stack.pop() == 8)
    stack.push(-1)
    stack.push(-2)
    assert(stack.max() == 7)
    stack.push(7)
    assert(stack.max() == 7)
    stack.push(8)
    assert(stack.max() == 8)
