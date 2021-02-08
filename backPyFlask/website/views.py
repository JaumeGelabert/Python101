from flask import Blueprint, render_template


views = Blueprint('views', __name__)


# Cuando se ejecute esta dirección, '/', se ejecutará tambien la funcion de 'home()'
@views.route('/')
def home():
    return render_template("home.html")


@views.route('/servicios')
def servicios():
    return render_template("servicios.html")
