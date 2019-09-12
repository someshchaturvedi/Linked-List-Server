from flask import Flask
# import json, jsonify
from flask import request, jsonify

from models import LinkedListManager, LinkedList
app = Flask(__name__)

linked_list_manager = LinkedListManager()

@app.route('/api/link', methods = ['POST'])
def create():
    data = request.form
    if 'name' not in data.keys() or 'birthyear' not in data.keys():
        return jsonify("Bad Parameters"), 400
    linked_list = linked_list_manager.create_list(data['name'], data['birthyear'])
    return jsonify(data = linked_list.to_json()), 200

@app.route('/api/link/<id>', methods = ['GET'])
def get_list(id):
    linked_list = linked_list_manager.retrieve_list(id)
    return jsonify(linked_list.to_json()), 200

@app.route('/api/link/<id>', methods = ['PUT'])
def push(id):
    data = request.form
    if 'name' not in data.keys() or 'birthyear' not in data.keys():
        return jsonify("Bad Parameters"), 400
    linked_list = linked_list_manager.retrieve_list(id)
    linked_list.add_node(data['name'], data['birthyear'])
    return jsonify(linked_list.to_json()), 200

@app.route('/api/link/pop/<id>', methods = ['GET'])
def pop(id):
    linked_list = linked_list_manager.retrieve_list(id)
    linked_list.pop_node()
    return jsonify(linked_list.to_json()), 200

@app.route('/api/link/remove/<id>', methods = ['POST'])
def remove(id):
    data = request.form
    if 'name' not in data.keys() or 'birthyear' not in data.keys():
        return jsonify("Bad Parameters"), 400
    linked_list = linked_list_manager.retrieve_list(id)
    linked_list.remove_node(data['name'], data['birthyear'])
    return jsonify(linked_list.to_json()), 200

@app.route('/api/link/pop/<id>', methods = ['GET'])
def reverse(id):
    linked_list = linked_list_manager.retrieve_list(id)
    linked_list.pop_node()
    return jsonify(linked_list.to_json()), 200


if __name__ == '__main__':
    app.run()