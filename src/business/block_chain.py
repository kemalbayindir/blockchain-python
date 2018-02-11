import time

from src.entity.block import Block
from src.entity.transaction import Transaction

#Created by kemalbayindir on 11.02.2018.

class BlockChain:

    chain = []
    difficulty_level = 4

    def __init__(self):
        self.chain.append(self.create_genesis_block())

    def get_last_block(self):
        return self.chain[-1]

    def create_genesis_block(self):
        transaction = Transaction('', '', 0)
        return Block(index=0, timestamp=time.time(), data=transaction, previous_hash='')

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty_level)
        self.chain.append(new_block)

    def dump_blocks(self):
        for b in self.chain:
            print b.__str__() + '\n'