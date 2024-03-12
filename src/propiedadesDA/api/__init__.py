from flask import Flask, jsonify
from propiedadesDA.conf.errors import ApiError
from propiedadesDA.conf.db import init_db
from .catastro import ca

app = Flask(__name__)
app.secret_key = '1D7FC7F9-3B7E-4C40-AF4D-141ED3F6013A'
init_db()
app.register_blueprint(ca)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "msg": err.description
    }
    return jsonify(response), err.code


def comenzar_consumidor():
    import threading
    import propiedadesDA.modulos.catastro.infraestructura.consumidores as catastro

    # Suscripción a eventos
    threading.Thread(target=catastro.suscribirse_a_eventos, args=[app]).start()

    # Suscripción a comandos
    threading.Thread(target=catastro.suscribirse_a_comandos, args=[app]).start()


comenzar_consumidor()