class Memory:

    def __init__(self, address_width=8):
        self.address_width = address_width
        self.M = [0 for _ in range(0x01<<self.address_width)]

    def memory_operation(self, A, D, Mode):
        out = 0
        label = 0
        if Mode == 0x00:
            # read
            out = self.M[D]
        elif Mode == 0x01:
            # write
            self.M[D] = A
        return out, label
