from .ALU import ALU
from .Stack import Stack
from .Memory import Memory
from .RegisterGroup import RegisterGroup


class ZZM:
    def __init__(self) -> None:
        self.Slots = [
            None,  # for write immediate number to register
            RegisterGroup(),
            ALU(),
            Memory(),
            Stack(max_deepth=0x0800),
        ]
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
            0x00,  # load A 0xAD
            0x01,  # load B 0x02
            0x20,  # point: cal A/B
            0x10,  # mov D(which is A%B) to A
            0xE1,  # if C is not zero jmp to point
            0xFF,  # end
        ]
        self.D = [
            0xAD,
            0x02,
            0x53,
            0x30,
            0x02,  # jump to the third command of this program
            0x00,
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
        opnum = self.D[to_do_idx]
        if cmd < 0:
            pass
        # write immediate number
        elif cmd >= 0x00 and cmd <= 0x0F:
            self.Slots[1].register_write_data(cmd, opnum)
        # exchange registers
        elif cmd == 0x10:
            self.Slots[1].register_exchange(opnum)
        # Call ALU, input A and B, out C, label D
        elif cmd == 0x20:
            self.Slots[1].R[0x02], self.Slots[1].R[0x03] = self.Slots[2].calculate(
                self.Slots[1].R[0x00], self.Slots[1].R[0x01], opnum
            )
        # use memory
        elif cmd == 0x30:
            self.Slots[3].memory_operation(
                self, self.Slots[1].R[0x00], self.Slots[1].R[0x03], opnum
            )
        # use stack
        elif cmd == 0x40:
            self.Slots[4].stack_operation(self.Slots[1].R[0x00], opnum)
        # JMP
        elif cmd == 0xE0:
            # set PC if C is 0
            if self.Slots[1].R[0x02] == 0:
                self.PC = opnum
                return
        elif cmd == 0xE1:
            # set PC if C is not 0
            if self.Slots[1].R[0x02] != 0:
                self.PC = opnum
                return
        # elif cmd == 0x85:
        #     # Input copy to C
        #     self.C = self.In
        # elif cmd == 0x86:
        #     # C copy to Output
        #     self.Out = self.C
        elif cmd == 0xFF:
            # stop
            self.Loop = False
            return
        self.PC = self.PC + 1
        pass
