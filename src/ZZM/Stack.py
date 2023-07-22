class Stack:
    def __init__(self, max_deepth=0x400):
        self.max_deepth = max_deepth
        self.L = []
        pass

    def is_full(self):
        return len(self.L) >= self.max_deepth

    def is_empty(self):
        return len(self.L) <= 0

    def push(self, X):
        if not self.is_full():
            self.L.append(X)
        else:
            self.L.pop(0)
            self.L.append(X)

    def pop(self):
        if not self.is_empty():
            return self.L.pop()
        else:
            return 0
        
    def stack_operation(self):
        pass
