from flask import Flask  
app = Flask(__name__)

@app.route("/")
def Holaflask():
    return "<h1>¡Hola Flask!</h1><hr>"

@app.route("/ruta2")
def ruta2():
    return "<strong>Estamos en la segunda ruta</strong><hr>"

@app.route("/ruta3")
def ruta3():
    return "<em>Estamos en la tercera ruta</em><hr>"

if __name__ == '__main__':
    app.run(debug=True)
