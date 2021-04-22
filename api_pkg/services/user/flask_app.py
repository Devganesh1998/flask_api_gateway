from flask import Flask
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return ({
        "service": "user"
    })

@app.route("/lists", methods=['GET'])
def show_list():
    return ({
        "lists": ['test2@test.com', 'test1@test.com']
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
