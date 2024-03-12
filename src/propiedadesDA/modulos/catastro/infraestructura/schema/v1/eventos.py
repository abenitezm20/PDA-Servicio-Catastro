from pulsar.schema import *
from propiedadesDA.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class RegistroCatastroPayload(Record):
    id_propiedad = String()
    numero_catastro = String()


class EventoRegistroCatastroCreado(EventoIntegracion):
    data = RegistroCatastroPayload()
