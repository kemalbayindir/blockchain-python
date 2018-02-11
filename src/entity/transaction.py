#Created by kemalbayindir on 11.02.2018.

class Transaction:
    source = ''
    target = ''
    amount = 0

    def __init__(self, source, target, amount):
        self.source = source
        self.target = target
        self.amount = amount


    def __str__(self):
        return self.source + self.target + self.amount.__str__()