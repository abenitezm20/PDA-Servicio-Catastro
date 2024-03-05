from pulsar.schema import *
from dataclasses import dataclass, field
from propiedadesDA.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoRegistrarCatastroPayload(Record):
    propiedad_id = String()
    numero_catastral = String()
    estrato = String()
    pisos = String()


class ComandoRegistrarCatastro(ComandoIntegracion):
    data = ComandoRegistrarCatastroPayload()
