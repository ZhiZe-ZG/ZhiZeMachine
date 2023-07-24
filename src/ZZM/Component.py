class Component:
    def __init__(self):
        self._slots = []
        self._slots_register_config = 0 # minimal register requirement

    def get_slots(self):
        return self._slots