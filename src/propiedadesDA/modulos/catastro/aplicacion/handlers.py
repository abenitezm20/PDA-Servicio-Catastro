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
        despachador.publicar_evento(evento, 'eventos-catastro')


class HandlePropiedadDominio():
    @staticmethod
    def handle_catastro_registrada(evento):
        obj = {
            "numero_catastral": evento.numero_catastral,
            "estrato": evento.estrato,
            "propiedad_id": evento.propiedad_id,
            "pisos": evento.pisos
        }
        map_propiedad = MapeadorCatastroDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(obj)
        comando = RegistrarCatastros(
            propiedad_dto.numero_catastral,
            propiedad_dto.estrato,
            propiedad_dto.pisos,
            propiedad_dto.propiedad_id
        )

        ejecutar_comando(comando)
