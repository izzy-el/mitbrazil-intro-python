# dict_test = {
#     'a': 10,
#     'b': 30,
#     'c': 80,
#     'd': 15
# }


def warehouse_process(_dict_, transaction):
    # print(transaction[0], transaction[1], transaction[2])
    if transaction[0] == 'receive' and transaction[1] not in _dict_:
        _dict_[transaction[1]] = transaction[2]
    elif transaction[0] == 'receive' and transaction[1] in _dict_:
        _dict_[transaction[1]] += transaction[2]
    elif transaction[0] == 'ship':
        if transaction[2] > _dict_[transaction[1]]:
            _dict_[transaction[1]] = 0
            print('not enough')
        else:
            _dict_[transaction[1]] -= transaction[2]

    return None


class Warehouse:
    def __init__(self):
        self._dict_ = {}

    def process(self, transaction):
        warehouse_process(self._dict_, transaction)

        return None
    
    def lookup(self, product):
        if product in self._dict_:
            return self._dict_[product]
        else:
            return 0

w = Warehouse()
w.process(('receive', 'a', 10))
w.process(('ship', 'a', 7))
print(w.lookup('a'))  # imprime 3
print(w.lookup('b'))  # imprime 0