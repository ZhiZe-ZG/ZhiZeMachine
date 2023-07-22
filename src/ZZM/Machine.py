from .ALU import ALU

class ZZM:
    def __init__(self) -> None:
        self.ALU = ALU()
        self.A = 0 # number 1
        self.B = 0 # number 2
        self.C = 0 # calcute result
        self.D = 0 # address base
        self.PC =0
        self.In = 0
        self.Out = 0
        self.Loop = True
        self.M = [0 for _ in range(0xFF)]
        self.M[0] = 0x10
        self.M[1] = 0x42
        self.M[2] = 0x11
        self.M[3] = 0x9F
        self.M[4] = 0x80
        self.M[5] = 0x52
        self.M[6] = 0x32
        self.M[7] = 0x7F
        self.M[8] = 0xFF
        self.M[9] = 0x00

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

    def step(self)->None:
        to_do_idx = self.PC
        cmd = self.M[to_do_idx]
        opnum = self.M[to_do_idx+1]
        if cmd <=0:
            pass
        elif cmd == 0x10:
            # set A as value
            self.A = opnum
        elif cmd == 0x11:
            # set B as value
            self.B = opnum
        elif cmd == 0x12:
            # set C as value
            self.C = opnum
        elif cmd == 0x13:
            # set D as value
            self.D = opnum
        elif cmd == 0x20:
            # load A from address
            self.A = self.M[opnum]
        elif cmd == 0x21:
            # load B from address
            self.B = self.M[opnum]
        elif cmd == 0x22:
            # load C from address
            self.C = self.M[opnum]
        elif cmd == 0x23:
            # load D from address
            self.D = self.M[opnum]
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
        elif cmd == 0XFF:
            # stop
            self.Loop = False
            return
        self.PC = self.PC+2
        pass