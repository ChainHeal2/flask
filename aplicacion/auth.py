"""Bienvenido a nuestro primer Blueprint"""
import functools
from flask import (Blueprint,flash,g,render_template,request,url_for,session,redirect)
from werkzeug.security import check_password_hash , generate_password_hash
from aplicacion.db import get_db
#creamos nuestro Blueprint que llamaremos bp
#lo llamaremos auth y cada vez que necesitemos acceder a alguna funcion como register
#en el navegador sera http://127.0.0.1:5000/auth/register (pero podemos personalizar claro)
bp = Blueprint('auth',__name__, url_prefix='/auth')
@bp.route('/register',methods=['GET','POST'])
def register():
    """Nuestra primera pagina que no sea index"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db,c = get_db()
        error = None
        c.execute(
            'select id from user where username = %s'
        )
        if not username:
            error ='Username es requerido'
        if not password:
            error = 'password es requerido'
        elif c.fetchone() is not None:
            error = f'Usuario {username} se encuentra registrado.'
        else:
            c.execute('insert into user (username,password) values (%s,%s)',)
            (username,generate_password_hash(password))
            db.commit()
            return redirect(url_for('index'))
    return 'register'