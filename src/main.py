import time

from src.business.block_chain import BlockChain
from src.entity.block import Block
from src.entity.transaction import Transaction


#Created by kemalbayindir on 11.02.2018.

def main():

    chain = BlockChain()
    t1 = Transaction("kemal", "kerem", 10)
    chain.add_block(Block(index=1, timestamp=time.time(), data=t1))

    t2 = Transaction("kerem", "didem", 20)
    chain.add_block(Block(index=2, timestamp=time.time(), data=t2))

    t3 = Transaction("didem", "kemal", 10)
    chain.add_block(Block(index=3, timestamp=time.time(), data=t3))

    chain.dump_blocks()

if __name__ == '__main__':
    main()