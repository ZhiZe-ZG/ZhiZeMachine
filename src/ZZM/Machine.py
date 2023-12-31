from .ALU import ALU
from .Stack import Stack
from .Memory import Memory
from .RegisterGroup import RegisterGroup16
from .Controller import ControllerMemory, ProgramCounter


class ZZM:
    def __init__(self) -> None:
        self.CM = ControllerMemory()
        self.PC = ProgramCounter()
        self.RG = RegisterGroup16()
        self.components = [
            self.RG,
            self.PC,
            self.CM,
            ALU(),
            Memory(),
            Stack(max_deepth=0x0800),
        ]
        self._slot_names = sum([c.get_slot_names() for c in self.components], [])
        self.slots = sum([c.get_slots() for c in self.components], [])
        self.Loop = True
        self.M = [
            0x04,  # load E 0xAD
            0x05,  # load F 0x02
            0x10,  # mov E to A
            0x10,  # mov F to B
            0x13,  # point: cal A/B
            0x10,  # mov D(which is A%B) to E
            0x05, # mov 2 to F
            0x03,  # mov jump target into D
            0x11,  # if C is not zero jmp to point
            0xFF,  # end
        ]
        self.D = [
            0xAD,
            0x02,
            0x40,
            0x51,
            0x53,
            0x34,
            0x02,
            0x02,  # jump to the third command of this program
            0x01,
            0x00,
        ]
        self.CM.PM = self.M + [0 for _ in range(0x100 - len(self.M))]
        self.CM.DM = self.D + [0 for _ in range(0x100 - len(self.D))]

    def loop(self) -> None:
        while self.Loop:
            self.show()
            self.step()

    def show_commands(self) -> None:
        print("==Command==")
        for i in range(len(self._slot_names)):
            print(f"{hex(i)}  {self._slot_names[i]}")

    def show(self) -> None:
        print(f"PC:{self.PC.PC}")
        print(f"Registers:{self.RG.R}")
        print(f"M:{self.CM.PM}")
        print(f"D:{self.CM.DM}")

    def step(self) -> None:
        to_do_idx = self.PC.PC
        cmd = self.CM.PM[to_do_idx]
        opnum = self.CM.DM[to_do_idx]
        if cmd < 0:
            pass
        # write immediate number
        elif cmd >= 0x00 and cmd < 0xFF:
            self.slots[cmd](self.RG, opnum)
        elif cmd == 0xFF:
            # stop
            self.Loop = False
            return
        self.PC.step()
