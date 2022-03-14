import collections


class Stack:
    ElementWithCachedMax = collections.namedtuple(
        'ElementWithCachedMax', ['element', 'max'])

    def __init__(self):
        self._element_with_cached_max_stack = []

    def empty(self):
        return len(self._element_with_cached_max_stack) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max_stack[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max_stack.pop().element

    def push(self, x):
        self._element_with_cached_max_stack.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert(stack.pop() == 9)
    assert(stack.pop() == 8)
    stack.push(-1)
    stack.push(-2)
    assert(stack.max() == 7)
