from flask import Flask
import json
from models import LinkedListManager, LinkedList
app = Flask(__name__)

linked_list_manager = LinkedListManager()

@app.route('/api/link', methods = ['GET'])
def create():
    linked_list_manager.add()
    return json.dumps(linked_list_manager.count)

if __name__ == '__main__':
    app.run()