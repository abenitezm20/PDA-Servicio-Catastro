from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.seedwork.dominio.entidades import AgregacionRaiz
from propiedadesDA.modulos.catastro.dominio.eventos import CatastroRegistrado

@dataclass
class Catastro(AgregacionRaiz):
    numero_catastral: str = field(default=str)
    propiedad_id: str = field(default=str)
    estrato: str = field(default=str)
    pisos: str = field(default=str)
    
    def registrar_catastro(self, propiedad: Catastro):

        self.agregar_evento(CatastroRegistrado(
            propiedad_id=propiedad.propiedad_id,
            numero_catastral=propiedad.numero_catastral,
            estrato=propiedad.estrato,
            pisos=propiedad.pisos))
