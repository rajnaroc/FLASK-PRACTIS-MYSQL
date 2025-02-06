from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL
from config import config
from  werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


mysql = MySQL(app)

app.secret_key = '0806fb170ceff1b2c8524d9890dbbaf912'

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


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        cur = mysql.connection.cursor()
        cur.execute('SELECT email, password FROM users WHERE email=%s', (email,))
        users  = cur.fetchone()
        print(users)
        if users:    
            hashed_password = users[1]
            print(hashed_password)
            print(password)
            if check_password_hash(hashed_password, password):
                print('Iniciado sesion correctamente')
                return redirect(url_for('users'))
            else:
                print('Contraseña incorrecta. Intenta de nuevo.')
                flash('Contraseña incorrecta. Intenta de nuevo.', 'danger') 
        else:
            print('No se encuentra un usuario con ese email.')
            flash('No se encuentra un usuario con ese email.', 'danger')
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        password_has = generate_password_hash(password)

        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO users (nombre, email, password) VALUES (%s, %s, %s)', (nombre, email, password_has))
        mysql.connection.commit()

        print('Insertado correctamente {}'.format(nombre))

        return redirect(url_for('users'))
    
@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html')

@app.errorhandler(404)
def status_404(error):
    return '<h1>Pagina no encontrada</h1>'

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()