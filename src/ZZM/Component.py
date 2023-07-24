class Component:
    def __init__(self):
        self._slots = []
        self._slots_register_need = [] 

    def get_slots(self):
        return self._slots