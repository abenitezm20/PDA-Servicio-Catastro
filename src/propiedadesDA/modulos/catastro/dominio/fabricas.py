from .entidades import Catastro
from .excepciones import TipoObjetoNoExisteEnDominioAnalisisExcepcion
from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.seedwork.dominio.fabricas import Fabrica
from propiedadesDA.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaCatastro(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            catastro = mapeador.dto_a_entidad(obj)

            return catastro

@dataclass
class FabricaCatastro(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Catastro.__class__:
            fabrica_catastro = _FabricaCatastro()
            return fabrica_catastro.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAnalisisExcepcion()