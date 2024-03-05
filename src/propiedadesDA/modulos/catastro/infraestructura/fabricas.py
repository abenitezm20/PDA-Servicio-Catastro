from dataclasses import dataclass
from propiedadesDA.seedwork.dominio.fabricas import Fabrica
from propiedadesDA.seedwork.dominio.repositorios import Repositorio
from propiedadesDA.modulos.catastro.dominio.repositorios import RepositorioCatastro
from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioCatastroSQL

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCatastro.__class__:
            return RepositorioCatastroSQL()
        else:
            raise ExcepcionFabrica()