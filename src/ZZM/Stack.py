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
        
    def stack_operation(self, A, Mode):
        out = 0
        label = 0
        if Mode == 0x00:
            self.push(A)
            label = self.is_full()
        elif Mode == 0x01:
            out = self.pop()
            label = self.is_empty()
        elif Mode == 0x02:
            label = self.is_full()
        elif Mode == 0x03:
            label = self.is_empty()
        return out, label

