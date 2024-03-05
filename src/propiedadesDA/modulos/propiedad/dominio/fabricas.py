from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.seedwork.dominio.fabricas import Fabrica
from propiedadesDA.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad = mapeador.dto_a_entidad(obj)

            return propiedad

@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()