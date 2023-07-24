class Component:
    def __init__(self):
        self._slots = []
        self._slots_register_config = 0 # minimal register requirement
        self._command_data_byte_num = 1

    def get_slots(self):
        return self._slots