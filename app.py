from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return "Hello world"

    

if __name__ == "__main__":
    main()
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
