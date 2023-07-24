from .Component import Component


class RegisterGroup16(Component):
    def __init__(self):
        super().__init__()
        super()._slot_names = [
            "register_write_data_0",
            "register_write_data_1",
            "register_write_data_2",
            "register_write_data_3",
            "register_write_data_4",
            "register_write_data_5",
            "register_write_data_6",
            "register_write_data_7",
            "register_write_data_8",
            "register_write_data_9",
            "register_write_data_A",
            "register_write_data_B",
            "register_write_data_C",
            "register_write_data_D",
            "register_write_data_E",
            "register_write_data_F",
            "register_exchange",
        ]
        super()._slots = [
            self.register_write_data_0,
            self.register_write_data_1,
            self.register_write_data_2,
            self.register_write_data_3,
            self.register_write_data_4,
            self.register_write_data_5,
            self.register_write_data_6,
            self.register_write_data_7,
            self.register_write_data_8,
            self.register_write_data_9,
            self.register_write_data_A,
            self.register_write_data_B,
            self.register_write_data_C,
            self.register_write_data_D,
            self.register_write_data_E,
            self.register_write_data_F,
            self.register_exchange,
        ]
        super()._slots_register_config = 0
        self.reg_num = 16
        self.R = [0 for _ in range(self.reg_num)]

    def register_exchange(self, reg, Mode):
        source = (Mode & 0xF0) >> 4
        des = Mode & 0x0F
        self.R[des] = self.R[source]

    def register_write_data_0(self, _, data):
        self.R[0] = data

    def register_write_data_1(self, _, data):
        self.R[1] = data

    def register_write_data_2(self, _, data):
        self.R[2] = data

    def register_write_data_3(self, _, data):
        self.R[3] = data

    def register_write_data_4(self, _, data):
        self.R[4] = data

    def register_write_data_5(self, _, data):
        self.R[5] = data

    def register_write_data_6(self, _, data):
        self.R[6] = data

    def register_write_data_7(self, _, data):
        self.R[7] = data

    def register_write_data_8(self, _, data):
        self.R[8] = data

    def register_write_data_9(self, _, data):
        self.R[9] = data

    def register_write_data_A(self, _, data):
        self.R[10] = data

    def register_write_data_B(self, _, data):
        self.R[11] = data

    def register_write_data_C(self, _, data):
        self.R[12] = data

    def register_write_data_D(self, _, data):
        self.R[13] = data

    def register_write_data_E(self, _, data):
        self.R[14] = data

    def register_write_data_F(self, _, data):
        self.R[15] = data
