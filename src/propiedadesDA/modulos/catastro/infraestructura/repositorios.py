from propiedadesDA.modulos.catastro.dominio.repositorios import RepositorioCatastro
from propiedadesDA.modulos.catastro.dominio.fabricas import FabricaCatastro
from propiedadesDA.modulos.catastro.dominio.entidades import Catastro
from uuid import UUID
from .dto import Catastro as CatastroDTO
from .mapeadores import MapeadorCatastro
from propiedadesDA.conf.db import db_session


class RepositorioCatastroSQL(RepositorioCatastro):

    def __init__(self):
        self._fabrica_catastro: FabricaCatastro = FabricaCatastro()

    @property
    def fabrica_catastro(self):
        return self._fabrica_catastro

    def obtener_por_id(self, id: UUID) -> Catastro:
        reserva_dto = db_session.query(CatastroDTO).filter_by(propiedad_id=str(id)).one()
        return self._fabrica_catastro.crear_objeto(reserva_dto, MapeadorCatastro())

    def obtener_todos(self) -> list[Catastro]:
        ...

    def agregar(self, propiedad: Catastro):
        propiedad_dto = self.fabrica_catastro.crear_objeto(propiedad, MapeadorCatastro())
        db_session.add(propiedad_dto)

    def actualizar(self, propiedad: Catastro):
        ...

    def eliminar(self, propiedad_id: UUID):
        ...