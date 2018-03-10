from datetime import datetime
import hashlib
import json
import os
from config import *

class Block:
    def __init__(self, index, timestamp, data, pre_hash=None, nonce=None, block_hash=None):
        self.index = index
        self.timestamp = timestamp.strftime("%Y.%m.%d %H:%M:%S")
        self.data = data
        self.nonce = nonce
        self.pre_hash = pre_hash
        self.block_hash = block_hash or self.create_self_hash()

    def header_string(self):
        return json.dumps({
            'index': self.index,
            'pre_hash': self.pre_hash,
            'data': self.data,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }, sort_keys=True).encode()

    def create_self_hash(self):
        return hashlib.sha256(self.header_string()).hexdigest()

    def self_save(self):
        index_string = str(self.index).zfill(6)
        filename = f'chaindata/{index_string}.json'
        with open(filename, 'w', encoding='utf-8') as block_file:
            json.dump(self.__dict__(), block_file, sort_keys=True, indent=2, ensure_ascii=False)

    def __dict__(self):
        info = {
            'index': self.index,
            'timestamp': self.timestamp,
            'pre_hash': self.pre_hash,
            'block_hash': self.block_hash,
            'data': self.data,
        }
        return info

    def __str__(self):
        return f'Block<pre_hash: {self.pre_hash}, hash: {self.block_hash}>'


def create_first_block():
    # генезис блок
    block_data = {
        'index': 0,
        'timestamp': datetime.now(),
        'data': 'Привет я первый блок',
        'pre_hash': None
    }
    return Block(**block_data)


if __name__ == '__main__':
    chaindata_dir = 'chaindata/'
    if not os.path.exists(chaindata_dir):
        os.mkdir(chaindata_dir)
    if not os.listdir(chaindata_dir):
        first_block = create_first_block()
        first_block.self_save()
        print(first_block)
