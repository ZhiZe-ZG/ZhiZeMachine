from .ALU import ALU
from .Stack import Stack

class ZZM:
    def __init__(self) -> None:
        self.ALU = ALU()
        self.Stack = Stack(max_deepth=0x0800)
        self.A = 0 # number 1
        self.B = 0 # number 2
        self.C = 0 # calcute result
        self.D = 0 # label or second result
        # and address base
        self.PC = 0
        self.AD = 0
        self.In = 0
        self.Out = 0
        self.Loop = True
        self.PM0 = [0 for _ in range(0x0100)] # Program memory
        self.DM0 = [0 for _ in range(0x0100)] # Data memory
        self.PM1 = [0 for _ in range(0x0100)] # Program memory
        self.DM1 = [0 for _ in range(0x0100)] # Data memory
        self.RM0 = [0 for _ in range(0x0100)]
        self.RM1 = [0 for _ in range(0x0100)]
        self.RM2 = [0 for _ in range(0x0100)]
        self.RM3 = [0 for _ in range(0x0100)]
        self.M = [0 for _ in range(0x200)]
        self.M[0] = 0x20
        self.M[1] = 0x42
        self.M[2] = 0x21
        self.M[3] = 0x9F
        self.M[4] = 0x80
        self.M[5] = 0x52
        self.M[6] = 0x32
        self.M[7] = 0x7F
        self.M[8] = 0x33
        self.M[9] = 0x80
        self.M[0x0A] = 0xFF
        self.M[0x0B] = 0x00

    def loop(self)->None:
        while self.Loop:
            self.show()
            self.step()

    def show(self)->None:
        print(f"PC:{self.PC}")
        print(f"A:{self.A}")
        print(f"B:{self.B}")
        print(f"C:{self.C}")
        print(f"D:{self.D}")
        print(f"M:{self.M}")

    def register_exchange(self,X)->None:
        pass

    def step(self)->None:
        to_do_idx = self.PC
        cmd = self.M[to_do_idx]
        opnum = self.M[to_do_idx+1]
        if cmd <=0:
            pass
        elif cmd == 0x20:
            # set A as value
            self.A = opnum
        elif cmd == 0x21:
            # set B as value
            self.B = opnum
        elif cmd == 0x22:
            # set C as value
            self.C = opnum
        elif cmd == 0x23:
            # set D as value
            self.D = opnum
        elif cmd == 0x30:
            # register exchange
            self.register_exchange(opnum)
        elif cmd == 0x30:
            # save A to address
            self.M[opnum] = self.A
        elif cmd == 0x31:
            # save B to address
            self.M[opnum] = self.B
        elif cmd == 0x32:
            # save C to address
            self.M[opnum] = self.C
        elif cmd == 0x33:
            # save D to address
            self.M[opnum] = self.D
        elif cmd == 0x40:
            # load A from D + value as address
            self.A = self.M[self.D+opnum]
        elif cmd == 0x41:
            # load B from D + value as address
            self.B = self.M[self.D+opnum]
        elif cmd == 0x42:
            # load C from D + value as address
            self.C = self.M[self.D+opnum]
        elif cmd == 0x43:
            # load D from D + value as address
            self.D = self.M[self.D+opnum]
        elif cmd == 0x50:
            # save A to D + value as address
            self.M[self.D+opnum] = self.A
        elif cmd == 0x51:
            # save B to D + value as address
            self.M[self.D+opnum] = self.B
        elif cmd == 0x52:
            # save C to D + value as address
            self.M[self.D+opnum] = self.C
        elif cmd == 0x53:
            # save D to D + value as address
            self.M[self.D+opnum] = self.D
        elif cmd == 0x60:
            # set PC
            self.PC = opnum
            return
        elif cmd == 0x61:
            # set PC if C is not 0
            if self.C != 0:
                self.PC= opnum
                return
        elif cmd == 0x62:
            # set PC if C is 0
            if self.C == 0:
                self.PC= opnum
                return
        elif cmd == 0x63:
            # set PC use address num
            self.PC = self.M[opnum]
            return
        elif cmd == 0x64:
            # set PC if C is not 0 use address num
            if self.C != 0:
                self.PC= self.M[opnum]
                return
        elif cmd == 0x65:
            # set PC if C is 0 use address num
            if self.C == 0:
                self.PC= self.M[opnum]
                return
        elif cmd == 0x66:
            # set PC use D + address num
            self.PC = self.M[self.D+opnum]
            return
        elif cmd == 0x67:
            # set PC if C is not 0 use D + address num
            if self.C != 0:
                self.PC= self.M[self.D+opnum]
                return
        elif cmd == 0x68:
            # set PC if C is 0 use D + address num
            if self.C == 0:
                self.PC= self.M[self.D+opnum]
                return
        elif cmd == 0x80:
            # Call ALU, input A and B, out C, label D
            self.C, self.D = self.ALU.calculate(self.A,self.B,opnum)
        elif cmd == 0x81:
            # push C to Stack, return full status to D
            self.Stack.push(self.C)
            self.D = self.Stack.is_full()
        elif cmd == 0x82:
            # pop Stack to C, return empty status to  D
            self.C = self.Stack.pop()
            self.D =  self.Stack.is_empty()
        elif cmd == 0x83:
            # return full status to C
            self.C = self.Stack.is_full()
        elif cmd == 0x84:
            # return empty status to C
            self.C = self.Stack.is_empty()
        elif cmd == 0x85:
            # Input copy to C
            self.C = self.In
        elif cmd == 0x86:
            # C copy to Output
            self.Out = self.C
        elif cmd == 0XFF:
            # stop
            self.Loop = False
            return
        self.PC = self.PC+2
        pass