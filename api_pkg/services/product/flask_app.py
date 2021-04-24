from flask import Flask, request,make_response
from flask_cors import CORS
import json
import traceback 

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def hello():
    return ({
        "service": "product"
    })

@app.route("/file", methods=['POST'])
def getFile():
    try:
        response = make_response(request.get_data())
        customHeader = {}
        for key, value in request.headers:
            customHeader[key] = request.headers.get(key)
        response.headers = customHeader
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except Exception as err:
        print(err)
        traceback.print_exc()
        return ({ 'err': str(err)})

@app.route("/lists", methods=['GET'])
def show_list():
    return ({
        "lists": ['Amazon', 'Flipkart']
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
