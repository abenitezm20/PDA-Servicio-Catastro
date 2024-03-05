from __future__ import annotations
from dataclasses import dataclass
from propiedadesDA.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class CatastroRegistrado(EventoDominio):
    numero_catastral: str = None
    estrato: str = None
    pisos: str = None
    propiedad_id: str = None
