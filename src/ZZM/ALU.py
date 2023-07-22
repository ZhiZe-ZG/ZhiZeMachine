class ALU:
    def __init__(self):
        pass

    def calculate(self,A,B,Mode):
        res = 0
        label = 0
        # binary logical operations
        # input (AB): 11 10 01 00
        if Mode == 0x00:
            # all zero 0 0 0 0
            res =  A^A
        elif Mode == 0x01:
            # not or 0 0 0 1
            res =  ~(A|B)
        elif Mode == 0x02:
            # 0 0 1 0
            res =  (~A)&B
        elif Mode == 0x03:
            # 0 0 1 1
            res =  ((~A)&B)|(~(A|B))
        elif Mode == 0x04:
            # not imply 0 1 0 0
            res =  A&(~B)
        elif Mode == 0x05:
            # 0 1 0 1
            res =  (A&(~B))|(~(A|B))
        elif Mode == 0x06:
            # xor 0 1 1 0
            res =  A^B
        elif Mode == 0x07:
            # not and 0 1 1 1
            res =  ~(A&B)
        elif Mode == 0x08:
            # and 1 0 0 0
            res =  A&B
        elif Mode == 0x09:
            # not xor 1 0 0 1
            res =  ~(A^B)
        elif Mode == 0x0A:
            # 1 0 1 0
            res =  (A&B)| ((~A)&B)
        elif Mode == 0x0B:
            # imply 1 0 1 1
            res =  ~(A&(~B))
        elif Mode == 0x0C:
            # 1 1 0 0
            res =  (A&B)|(A&(~B))
        elif Mode == 0x0D:
            # 1 1 0 1
            res =  ~((~A)&B)
        elif Mode == 0x0E:
            # or 1 1 1 0
            res =  A|B
        elif Mode == 0x0F:
            # all one 1 1 1 1
            res =  ~(A^A)
        # shift
        elif Mode >= 0x10 and Mode <= 0x17:
            # left shift add 0
            shift_num = Mode & 0x07
            res =  A<<shift_num
        elif Mode >= 0x18 and Mode <= 0x1F:
            # right shift add 0
            shift_num = Mode & 0x07
            res =  A>>shift_num
        elif Mode >= 0x20 and Mode <= 0x27:
            # left shift add 1
            shift_num = Mode & 0x07
            b = self.__get_bits(A)
            out = 0
            for i in range(8):
                if i < shift_num:
                    out = out | (0x01<<i)
                else:
                    out = out | ((b[i-shift_num])<<i)
            res =  out
        elif Mode >= 0x28 and Mode <= 0x2F:
            # right shift add 1
            shift_num = Mode & 0x07
            b = self.__get_bits(A)
            out = 0
            for i in range(8):
                if i < 8-shift_num:
                    out = out | ((b[i+shift_num])<<i)
                else:
                    out = out | (0x01<<i)
            res =  out
        elif Mode >= 0x30 and Mode <= 0x37:
            # left shift copy
            shift_num = Mode & 0x07
            b = self.__get_bits(A)
            c = b[0]
            out = 0
            for i in range(8):
                if i < shift_num:
                    out = out | (c<<i)
                else:
                    out = out | ((b[i-shift_num])<<i)
            res =  out
        elif Mode >= 0x38 and Mode <= 0x3F:
            # right shift copy
            shift_num = Mode & 0x07
            b = self.__get_bits(A)
            c = b[7]
            out = 0
            for i in range(8):
                if i < 8-shift_num:
                    out = out | ((b[i+shift_num])<<i)
                else:
                    out = out | (c<<i)
            res =  out
        elif Mode >= 0x40 and Mode <= 0x47:
            # left shift loop
            shift_num = Mode & 0x07
            b = self.__get_bits(A)
            c = b[0]
            out = 0
            for i in range(8):
                if i < shift_num:
                    out = out | ((b[i+8-shift_num])<<i)
                else:
                    out = out | ((b[i-shift_num])<<i)
            res =  out
        elif Mode >= 0x48 and Mode <= 0x4F:
            # right shift loop
            shift_num = Mode & 0x07
            b = self.__get_bits(A)
            c = b[7]
            out = 0
            for i in range(8):
                if i < 8-shift_num:
                    out = out | ((b[i+shift_num])<<i)
                else:
                    out = out | ((b[i-8+shift_num])<<i)
            res =  out
        # Add and Sub
        elif Mode == 0x50:
            # Add
            out = A+B
            if out > 255 or out<0:
                # overflow
                label = 1
            res = out % 256
        elif Mode == 0x51:
            # Add 1
            out = A + 1
            if out > 255 or out<0:
                # overflow
                label = 1
            res = out % 256
        elif Mode == 0x52:
            # Sub
            out = A-B
            if out > 255 or out<0:
                # overflow
                label = 1
            res = out%256
        elif Mode == 0x53:
            # Sub 1
            out = A-1
            if out > 255 or out<0:
                # overflow
                label = 1
            res = out%256
        elif Mode == 0x54:
            # Mul
            out = A*B
            if out > 255 or out<0:
                # overflow
                label = 1
            res = out%256
        elif Mode == 0x55:
            # SQR
            out = A*A
            if out>255 or out<0:
                # overflow
                label = 1
            res = out%256
        elif Mode == 0x56:
            # DIV
            out = A//B
            if out>255 or out<0:
                # overflow
                label = 1
            res = out%256
        elif Mode == 0x57:
            # MOD
            out = A%B
            if out>255 or out<0:
                # overflow
                label = 1
            res = out % 256
        else:
            pass
        return res, label
        
    def __get_bits(self,X):
        b = [0 for _ in range(8)]
        b[7] = (X & (0x01<<7))>>7
        b[6] = (X & (0x01<<6))>>6
        b[5] = (X & (0x01<<5))>>5
        b[4] = (X & (0x01<<4))>>4
        b[3] = (X & (0x01<<3))>>3
        b[2] = (X & (0x01<<2))>>2
        b[1] = (X & (0x01<<1))>>1
        b[0] = (X & (0x01<<0))>>0
        return b