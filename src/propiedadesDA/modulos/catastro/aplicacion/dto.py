from dataclasses import dataclass, field
from propiedadesDA.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CatastroDTO(DTO):
    numero_catastro: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)