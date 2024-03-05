from dataclasses import dataclass
from propiedadesDA.seedwork.aplicacion.comandos import Comando
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando as comando
from propiedadesDA.modulos.catastro.aplicacion.dto import CatastroDTO
from propiedadesDA.modulos.catastro.dominio.entidades import Catastro
from propiedadesDA.modulos.catastro.aplicacion.mapeadores import MapeadorCatastro
from propiedadesDA.modulos.catastro.infraestructura.repositorios import RepositorioCatastroSQL
from propiedadesDA.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .base import RegistrarCatastrosBaseHandler


@dataclass
class RegistrarCatastros(Comando):
    propiedad_id: str
    numero_catastral: str
    estrato: str
    pisos: str


class RegistrarCatastrosHandler(RegistrarCatastrosBaseHandler):

    def handle(self, comando: RegistrarCatastros):
        propiedad_dto = CatastroDTO(
            numero_catastral=comando.numero_catastral,
            estrato=comando.estrato,
            pisos=comando.pisos,
            propiedad_id=comando.propiedad_id,
        )

        propiedad: Catastro = self.fabrica_catastro.crear_objeto(
            propiedad_dto, MapeadorCatastro())
        propiedad.registrar_catastro(propiedad)
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCatastroSQL.__class__)

        print('Registrando crear contrato en la unidad de trabajo')
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()


@comando.register(RegistrarCatastros)
def ejecutar_comando_crear_catastro(comando: RegistrarCatastros):
    print('Registrando comando crear catastro')
    handler = RegistrarCatastrosHandler()
    handler.handle(comando)
