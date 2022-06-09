# Archivo init.py - archivo de inicio de Flask

# modulos
from flask import Flask # -> modulo principal
from flask import render_template # -> modulo para renderizado de archivos html
from flask import abort, redirect # -> redirecciones y errores

app = Flask(__name__)

# error 404
@app.errorhandler
def pagina_no_encontrada(error):
    return render_template("pag_no_encontrada.html"), 404

# pagina simple en la ruta raiz
@app.route("/")
def home():
    return "Hola mundo"

# ejemplo de renderizado de paginas html
@app.route("/1")
def firstpage():
    return render_template('1/index.html')

# ejemplo de renderizado de paginas html
@app.route("/2")
def secondpage():
    return render_template('2/index.html')


# para ejecutar el codigo
if __name__ == "__main__":
    app.run(debug=True)
