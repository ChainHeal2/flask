from flask import Flask,render_template,request,redirect,url_for,abort
from funciones.funciones import formato_nombre,formato_id
import mysql.connector
midb = mysql.connector.connect(
    host="localhost",
    user="jose",
    password = "uno23456",
    database ="prueba"
)
cursor =midb.cursor(dictionary=True)# sin nada dentro de los parentesis devuelve una lista
app = Flask(__name__)
@app.route("/")#Luego del slash podemos poner la ruta asociada en el navegador ejemplo http://127.0.0.1:5000/formularios
@app.route("/<nombre>")
def index(nombre = None):
    return render_template('base.html',nombre_usuario = nombre) # la raiz de render_template sera una carpeta por defecto llamada templates

@app.route("/sql")
def ver_usuario():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    return render_template("crud/usuario/lista_usuario.html",usuarios = usuarios)

@app.route("/ingreso",methods = ['POST','GET'])
def ingreso_usuario():
    if request.method == 'POST':
        for campo in request.form:
            if len(request.form[campo]) > 0 : #cambiar un largo mas real 4
                for numero in request.form[campo]:
                    print(numero)
                    if numero in '1234567890':
                        print("no se permiten numeros en los campos")
                    else:
                        print("todo correcto")
                        nombres = request.form['nombres']
                        apaterno = request.form['apaterno']
                        amaterno = request.form['amaterno']
                        sql = f"insert into usuario (nombres,apaterno,amaterno) values ('{nombres.lower().strip()}','{apaterno.lower().strip()}','{amaterno.lower().strip()}');"
                        print(sql)
                        cursor.execute(sql)
                        midb.commit()
                        return redirect(url_for('ver_usuario'))
            else:
                abort(400)
    return render_template('crud/usuario/ingresar_usuario.html')

@app.route("/modificar",methods = ['POST','GET','DELETE'])
def modificar_usuario():
    if request.method == 'GET':
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
    else:
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
        for dato in request.form:
            if request.form[dato] in '1234567890':
                abort(400)
        nombres = request.form['nombres']
        apaterno = request.form['apaterno']
        amaterno = request.form['amaterno']
        id_usuario = request.form.get('id')
        sql = f"UPDATE usuario SET nombres = '{nombres}', apaterno = '{apaterno}', amaterno = '{amaterno}' WHERE (id = '{id_usuario}');"
        cursor.execute(sql)
        midb.commit()
        return(redirect(url_for('modificar_usuario')))
    return render_template('crud/usuario/modificar_usuario.html',usuarios = usuarios)
@app.route("/eliminar",methods = ['POST','GET'])
def eliminar_usuario():
    if request.method == 'GET':
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
    else:
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
        id_usuario = request.form.get('id')
        cursor.execute(f"DELETE FROM usuario WHERE (id = '{id_usuario}');")
        midb.commit()
        return(redirect(url_for('eliminar_usuario')))
    return render_template('crud/usuario/eliminar_usuario.html',usuarios = usuarios)
@app.route("/ingreso_tarea", methods = ['GET','POST'])
def ingreso_tarea():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    #id_usuario = formato_id(usuarios)
    #nombre_completo = formato_nombre(usuarios)
    return render_template('crud/tarea/ingresar_tarea.html', usuarios = usuarios)
