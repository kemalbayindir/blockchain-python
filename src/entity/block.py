import hashlib

import time

from transaction import Transaction

#Created by kemalbayindir on 11.02.2018.

class Block:
    index = 0
    timestamp = time.time()
    data = Transaction('', '', 0)
    previous_hash = None
    hash = None
    nonce = 0

    def __init__(self, index, timestamp, data, previous_hash='', hash='', nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.nonce = nonce

    def calculate_hash(self):
        collection_str = self.index.__str__() + self.timestamp.__str__() + self.data.__str__() + self.previous_hash + self.nonce.__str__()
        return hashlib.sha256(collection_str).hexdigest()

    def mine_block(self, difficulty_level):
        search_key = ''.join('0' for _ in range(difficulty_level))
        while (self.hash[0:difficulty_level] != search_key):
            self.nonce = self.nonce + 1
            self.hash = self.calculate_hash()
        #print self.hash

    def __str__(self):
        return self.index.__str__() + ', time : ' + self.timestamp.__str__() + ', transaction : ' + self.data.__str__() + ', hash: ' + self.hash + ', prev hash: ' + self.previous_hash