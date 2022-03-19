from flask import Flask, request

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