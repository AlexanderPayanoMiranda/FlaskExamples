from flask import render_template, request, redirect, url_for
from flask_wtf import CSRFProtect

from app import create_app
from app.db import db
from app.forms import BasicForm, RegisterForm, LoginForm
from app.models.models import User

from werkzeug.security import generate_password_hash

app = create_app()
csrf = CSRFProtect()

db.init_app(app)
csrf.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/acerca')
def acerca():
    return render_template("acerca.html")


@app.route('/contacto', methods=['GET','POST'])
def contacto():
    # args = request.args
    # nombre = args.get('nombre', 'Maria')
    # apellido = args.get('apellido', 'Magdalena')
    # nombre_completo = f"{nombre} {apellido}"

    form = BasicForm()
    nombre = "Maria"
    apellido = "Magdalena"
    if request.method == 'POST':
        nombre = form.nombre.data
        apellido = form.apellido.data
    return render_template("contacto.html", form=form, nombre=nombre+" "+apellido)
    
    # http://127.0.0.1:5000/contacto
    # http://127.0.0.1:5000/contacto?nombre=Pedro&apellido=Perez


@app.route('/users')
def users():
    # db.create_all()
    users = User.query.all() # SELECT * FROM users;
    return render_template("users.html", users=users)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        user = User(
            register_form.nombre.data,
            register_form.apellido.data,
            register_form.email.data,
            register_form.sobre_mi.data
        )
        user.set_password(register_form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("register.html", register_form=register_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()

        if user is not None:
            if user.check_password(login_form.password.data):
                print("Datos Correctos!")
            else:
                print("Datos Incorrectos!")
        else:
            print("El usuario no existe!")

    return render_template("login.html", login_form=login_form)


db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
