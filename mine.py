from block import *
import sync


NUM_ZEROS = 4
node_blocks = sync.sync()


def generate_header(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False).encode()


def calculate_hash(data):
    return hashlib.sha256(generate_header(data)).hexdigest()


def mine(last_block):
    index = int(last_block.index) + 1
    data = f'Я блок под номером {index}'
    block_data = {
        'index': index,
        'timestamp': str(datetime.now()),
        'data': data,
        'pre_hash': last_block.block_hash,
        'nonce': 0
    }

    block_hash = calculate_hash(block_data)
    while str(block_hash[0:NUM_ZEROS]) != '0'*NUM_ZEROS:
        block_data['nonce'] += 1
        block_hash = calculate_hash(block_data)

    block_data['block_hash'] = block_hash
    return Block(**block_data)


if __name__ == '__main__':
    block = node_blocks[-1]
    new_block = mine(block)
    new_block.self_save()
