from pulsar.schema import *
from dataclasses import dataclass, field
from propiedadesDA.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearPropiedadPayload(Record):
    id_propiedad = String()


class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()


class ComandoCrearCatastroFallidoPayload(Record):
    id_propiedad = String()
    numero_catastro = String()

class ComandoCrearCatastroFallido(ComandoIntegracion):
    data = ComandoCrearCatastroFallidoPayload()