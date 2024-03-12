from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.seedwork.dominio.entidades import AgregacionRaiz
from propiedadesDA.modulos.catastro.dominio.eventos import CatastroRegistrado

@dataclass
class Catastro(AgregacionRaiz):
    numero_catastro: str = field(default=str)
    id_propiedad: str = field(default=str)

    
    def registrar_catastro(self, propiedad: Catastro):

        self.agregar_evento(CatastroRegistrado(
            id_propiedad=propiedad.id_propiedad,
            numero_catastro=propiedad.numero_catastro,
   ))
