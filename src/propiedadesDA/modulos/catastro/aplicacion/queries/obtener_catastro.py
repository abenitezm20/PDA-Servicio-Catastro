from propiedadesDA.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesDA.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadesDA.modulos.catastro.infraestructura.repositorios import RepositorioCatastroSQL
from dataclasses import dataclass
from .base import CatastroQueryBaseHandler
from propiedadesDA.modulos.catastro.aplicacion.mapeadores import MapeadorCatastro

@dataclass
class ObtenerCatastro(Query):
    id: str

class ObtenerCatastroHandler(CatastroQueryBaseHandler):

    def handle(self, query: ObtenerCatastro) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCatastroSQL.__class__)
        catastro =  self.fabrica_catastro.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCatastro())
        return QueryResultado(resultado=catastro)

@query.register(ObtenerCatastro)
def ejecutar_query_obtener_propiedad(query: ObtenerCatastro):
    handler = ObtenerCatastroHandler()
    return handler.handle(query)
