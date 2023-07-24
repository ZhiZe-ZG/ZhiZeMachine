from .Component import Component

class ControllerMemory(Component):
    def __init__(self):
        super().__init__()
        super()._slots_names = ['RW_PDM']
        super()._slots = [self.read_write_PDM]
        super()._slots_register_config = 4
        self.PM = [0 for _ in range(256)] # program memory
        self.DM = [0 for _ in range(256)] # data memory

    def read_write_PDM(self,reg, mode):
        A = reg.R[0]
        D = reg.R[3]
        out = 0
        label = 0
        if mode == 0x00:
            # read PM
            out = self.PM[D] 
        elif mode == 0x01:
            # read DM
            out = self.DM[D]
        elif mode == 0x02:
            # write PM
            self.PM[D] = A
        elif mode == 0x03:
            # write DM
            self.DM[D] = A
        reg.R[1] = label
        reg.R[2] = out
        return

class ProgramCounter(Component):
    def __init__(self):
        super().__init__()
        super()._slots = [self.jump]
        super()._slots_register_config = 4
        self.PC = 0

    def jump(self,reg, mode):
        C = reg.R[2]
        D = reg.R[3]
        if mode == 0x00:
            # jump when C is zero
            if C == 0:
                self.PC = D-1 # PC will always add 1
        elif mode == 0x01:
            # jump when C is not zero
            if C != 0:
                self.PC = D-1 # PC will always add 1
    
    def step(self):
        self.PC = self.PC+1