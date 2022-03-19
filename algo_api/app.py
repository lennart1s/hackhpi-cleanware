from flask import Flask, request
import json

app = Flask(__name__)

# Accessing request data:
#   request.args.get('key': '')
#   request.data
#   request.form[<key>]

@app.route('/alive', methods=['GET'])
def alive():
  return {
    'alive': True,
  }

@app.route('/', methods=['GET'])
def index():
  return 'index handler'

@app.route('/task', methods=['PUT', 'DELETE'])
def putDelHandler():
  task = request.data.decode('utf8').replace("'", '"')
  if request.method == 'PUT':
    print('put: ')
    print(task)
  elif request.method == 'DELETE':
    print('del: ')
    print(task)
  return {}