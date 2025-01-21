from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)