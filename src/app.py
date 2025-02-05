from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    pass

@app.route('/register', methods=['GET','POST'])
def register():
    pass

@app.route('/users', methods=['GET'])
def users():
    pass

if __name__ == "__main__":
    app.run(debug=True)