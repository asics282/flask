from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reg.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(150), unique=False, nullable=False)

    def __repr__(self):
        return f'User({self.name}, {self.surname})'

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/reg/', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']

        # Хеширование пароля перед сохранением в базе данных
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(name=name, surname=surname, email=email, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('final'))
        except:
            return 'Произошла ошибка'

    return render_template('reg.html')

@app.route('/final/')
def final():
    return render_template('final.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)