from propiedadesDA.modulos.catastro.aplicacion.mapeadores import MapeadorCatastroDTOJson
from propiedadesDA.modulos.catastro.aplicacion.comandos.crear_catastro import RegistrarCatastros
from propiedadesDA.modulos.catastro.infraestructura.despachadores import Despachador
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando
from propiedadesDA.seedwork.aplicacion.handlers import Handler
from datetime import datetime


class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_catastro_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-creada')


class HandlePropiedadDominio():
    @staticmethod
    def handle_catastro_registrada(evento):
        obj = {
            "numero_catastro": evento.numero_catastro,
            "id_propiedad": evento.id_propiedad,
        }
        map_propiedad = MapeadorCatastroDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(obj)
        comando = RegistrarCatastros(
            propiedad_dto.numero_catastro,
            propiedad_dto.id_propiedad
        )

        ejecutar_comando(comando)
