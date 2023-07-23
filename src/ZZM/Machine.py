from .ALU import ALU
from .Stack import Stack
from .Memory import Memory
from .RegisterGroup import RegisterGroup


class ZZM:
    def __init__(self) -> None:
        self.Slots = [None, # for write immediatly number to register
                      RegisterGroup(), ALU(), Memory(), Stack(max_deepth=0x0800)]
        # self.A = 0  # number 1
        # self.B = 0  # number 2
        # self.C = 0  # calcute result
        # self.D = 0  # label or second result
        # and address base
        self.PC = 0
        # self.AD = 0
        # self.In = 0
        # self.Out = 0
        self.Loop = True
        self.M = [
            0x20,
            0xAF,
            0x21,
            0x02,
            0x80,
            0x53,
            0x52,
            0xFE,
            0x53,
            0xFF,
            0x18,
            0x00,
            0x1E,
            0x00,
            0x25,
            0x04,
            0xFF,
            0x00,
        ]
        self.D =[

        ]
        self.M = self.M + [0 for _ in range(0x100 - len(self.M))]
        self.D = self.D + [0 for _ in range(0x100 - len(self.D))]

    def loop(self) -> None:
        while self.Loop:
            self.show()
            self.step()

    def show(self) -> None:
        print(f"PC:{self.PC}")
        print(f"Registers:{self.Slots[1].R}")
        print(f"M:{self.M}")
        print(f"D:{self.D}")

    def register_exchange(self, X) -> None:
        pass

    def step(self) -> None:
        to_do_idx = self.PC
        cmd = self.M[to_do_idx]
        opnum = self.M[to_do_idx + 1]
        if cmd <= 0:
            pass
        # exchange registers
        elif cmd == 0x10:
            self.A = self.A
        elif cmd == 0x11:
            self.B = self.A
        elif cmd == 0x12:
            self.C = self.A
        elif cmd == 0x13:
            self.D = self.A
        elif cmd == 0x14:
            self.A = self.B
        elif cmd == 0x15:
            self.B = self.B
        elif cmd == 0x16:
            self.C = self.B
        elif cmd == 0x17:
            self.D = self.B
        elif cmd == 0x18:
            self.A = self.C
        elif cmd == 0x19:
            self.B = self.C
        elif cmd == 0x1A:
            self.C = self.C
        elif cmd == 0x1B:
            self.D = self.C
        elif cmd == 0x1C:
            self.A = self.D
        elif cmd == 0x1D:
            self.B = self.D
        elif cmd == 0x1E:
            self.C = self.D
        elif cmd == 0x1F:
            self.D = self.D
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
        elif cmd == 0x24:
            # set PC as value
            self.PC = opnum
            return
        elif cmd == 0x25:
            # set PC if C is not 0
            if self.C != 0:
                self.PC = opnum
                return
        elif cmd == 0x26:
            # set PC if C is 0
            if self.C == 0:
                self.PC = opnum
                return
        elif cmd == 0x27:
            # set AD as value
            self.AD = opnum
        elif cmd == 0x40:
            # load A from D + value as address
            self.A = self.M[self.AD + opnum]
        elif cmd == 0x41:
            # load B from D + value as address
            self.B = self.M[self.AD + opnum]
        elif cmd == 0x42:
            # load C from D + value as address
            self.C = self.M[self.AD + opnum]
        elif cmd == 0x43:
            # load D from D + value as address
            self.D = self.M[self.AD + opnum]
        elif cmd == 0x50:
            # save A to D + value as address
            self.M[self.AD + opnum] = self.A
        elif cmd == 0x51:
            # save B to D + value as address
            self.M[self.AD + opnum] = self.B
        elif cmd == 0x52:
            # save C to D + value as address
            self.M[self.AD + opnum] = self.C
        elif cmd == 0x53:
            # save D to D + value as address
            self.M[self.AD + opnum] = self.D
        elif cmd == 0x66:
            # set PC use D + address num
            self.PC = self.M[self.AD + opnum]
            return
        elif cmd == 0x67:
            # set PC if C is not 0 use D + address num
            if self.C != 0:
                self.PC = self.M[self.AD + opnum]
                return
        elif cmd == 0x68:
            # set PC if C is 0 use D + address num
            if self.C == 0:
                self.PC = self.M[self.AD + opnum]
                return
        elif cmd == 0x80:
            # Call ALU, input A and B, out C, label D
            self.C, self.D = self.ALU.calculate(self.A, self.B, opnum)
        elif cmd == 0x81:
            # push C to Stack, return full status to D
            self.Stack.push(self.C)
            self.D = self.Stack.is_full()
        elif cmd == 0x82:
            # pop Stack to C, return empty status to  D
            self.C = self.Stack.pop()
            self.D = self.Stack.is_empty()
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
        elif cmd == 0xFF:
            # stop
            self.Loop = False
            return
        self.PC = self.PC + 2
        pass
