class RegisterGroup:
    def __init__(self, reg_num = 16):
        self.reg_num = reg_num
        self.R = [0 for _ in range(self.reg_num)]
    
    def register_exchange(self, Mode):
        source = Mode&0xF0
        des = Mode&0x0F
        self.R[des] =self.R[source]

    def register_write_data(self, idx, data):
        self.R[idx] = data