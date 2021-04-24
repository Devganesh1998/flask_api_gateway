from flask import Flask, request,make_response
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return ({
        "service": "product"
    })

@app.route("/file", methods=['POST'])
def getFile():
    response = make_response(request.get_data())
    response.headers = request.headers
    return response

@app.route("/lists", methods=['GET'])
def show_list():
    return ({
        "lists": ['Amazon', 'Flipkart']
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
