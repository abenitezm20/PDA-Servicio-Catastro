from pulsar.schema import *
from propiedadesDA.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class RegistroCatastroPayload(Record):
    propiedad_id = String()
    numero_catastral = String()
    estrato = String()
    pisos = String()


class EventoRegistroCatastroCreado(EventoIntegracion):
    data = RegistroCatastroPayload()
