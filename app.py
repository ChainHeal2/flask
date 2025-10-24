from flask import Flask,render_template,request
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
    return render_template('pagina_inicio/index.html',nombre_usuario = nombre) # la raiz de render_template sera una carpeta por defecto llamada templates

@app.route("/sql")
def ver_usuario():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    print(type(usuarios))
    for usuario in usuarios:
        print(usuario)
    return render_template("mostrar.html",usuarios = usuarios)

@app.route("/ingreso",methods = ['GET','POST'])
def ingreso_usuario():
    if request.method == 'POST':
        
