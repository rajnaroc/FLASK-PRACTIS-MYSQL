from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from products')
    products  = cur.fetchall()
    print(products)
    return render_template('index.html', products=products)

@app.route('/agregar_fav/<string:id>')
def agregar_favoritos(id):
    if id == '':
        print(f"Producto con ID {id} agregado a favoritos")
    return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    pass

@app.route('/users', methods=['GET'])
def users():
    pass

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()