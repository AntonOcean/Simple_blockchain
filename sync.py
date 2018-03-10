from block import *


def sync():
    node_blocks = []
    data_dir = 'chaindata'
    if os.path.exists(data_dir):
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                filepath = f'{data_dir}/{filename}'
                with open(filepath, 'r', encoding='utf-8') as block_file:
                    block_info = json.load(block_file)
                    block_object = Block(**block_info)
                    node_blocks.append(block_object)
    return node_blocks
