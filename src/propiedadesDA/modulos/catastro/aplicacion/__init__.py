from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion

from propiedadesDA.modulos.catastro.dominio.eventos import CatastroRegistrado

dispatcher.connect(HandlerReservaIntegracion.handle_catastro_creado,
                   signal=f'{CatastroRegistrado.__name__}Integracion')
