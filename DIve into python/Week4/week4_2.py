class Value:
    def __init__(self):
        self.amount = None

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, amount):
        self.amount = amount - amount * instance.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


# new_account = Account(0.1)
# new_account.amount = 100
#
# print(new_account.amount)