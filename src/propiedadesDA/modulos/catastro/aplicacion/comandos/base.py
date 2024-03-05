from propiedadesDA.seedwork.aplicacion.comandos import ComandoHandler
from propiedadesDA.modulos.catastro.infraestructura.fabricas import FabricaRepositorio
from propiedadesDA.modulos.catastro.dominio.fabricas import FabricaCatastro


class RegistrarCatastrosBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_catastro: FabricaCatastro = FabricaCatastro()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_catastro(self):
        return self._fabrica_catastro
