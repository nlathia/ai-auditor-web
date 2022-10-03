from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")
    

if __name__ == "__main__":
    main()
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
