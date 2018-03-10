from flask import Flask, jsonify
import sync


node = Flask(__name__)


@node.route('/blockchain.json', methods=['GET'])  # текущий блок
def blockchain():
    node_blocks = sync.sync()
    response = []
    for block in node_blocks:
        response.append(block.__dict__())
    return jsonify(response), 200


if __name__ == '__main__':
    node.run()
