from .Component import Component


class Memory(Component):
    def __init__(self, address_width=8):
        super().__init__()
        super()._slots_names = ['MEM']
        super()._slots = [self.memory_operation]
        super()._slots_register_config = 4
        self.address_width = address_width
        self.M = [0 for _ in range(0x01 << self.address_width)]

    def memory_operation(self, reg, Mode):
        A, D = reg.R[0], reg.R[3]
        out = 0
        label = 0
        if Mode == 0x00:
            # read
            out = self.M[D]
        elif Mode == 0x01:
            # write
            self.M[D] = A
        reg.R[0], reg.R[1] = out, label
        return
