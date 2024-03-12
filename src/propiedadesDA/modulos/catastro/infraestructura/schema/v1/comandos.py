from pulsar.schema import *
from dataclasses import dataclass, field
from propiedadesDA.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoRegistrarCatastroPayload(Record):
    id_propiedad = String()
    numero_catastro = String()


class ComandoRegistrarCatastro(ComandoIntegracion):
    data = ComandoRegistrarCatastroPayload()
