class Account:

    def __init__(self, _id, balance, pin):
        self.__id = _id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            return "Wrong pin"
        self.__pin = new_pin
        return "Pin changed"
