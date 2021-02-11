from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="Testing", user="Jaumae")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            # Mensaje para el usuario que hay un error con el email
            flash('Email must be greater than 4 caracteres', category='error')
        elif len(firstName) < 2:
            # Mensaje para el usuario que hay un error con el nombre
            flash('First Name must be greater than 2 caracteres', category='error')
        elif len(password1) < 7:
            # Mensaje para el usuario que hay un error con las contraseñas
            flash('Password must be greater than 7 caracteres', category='error')
        elif password1 != password2:
            # Mensaje para el usuario que hay un error con las contraseñas
            flash('Password no coinciden', category='error')
        else:
            # Como no hay ningún error, podmos añadir el usuario a la base de datos
            flash('Account created!', category='success')
            
    return render_template("signup.html")
