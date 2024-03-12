from __future__ import annotations
from dataclasses import dataclass
from propiedadesDA.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class CatastroRegistrado(EventoDominio):
    numero_catastro: str = None
    id_propiedad: str = None
