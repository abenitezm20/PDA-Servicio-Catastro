from propiedadesDA.modulos.catastro.dominio.entidades import Catastro
from propiedadesDA.modulos.catastro.dominio.eventos import CatastroRegistrado
from propiedadesDA.modulos.catastro.infraestructura.fabricas import FabricaRepositorio
from propiedadesDA.modulos.catastro.infraestructura.repositorios import RepositorioCatastroSQL
from propiedadesDA.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from propiedadesDA.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from propiedadesDA.modulos.catastro.infraestructura.despachadores import Despachador
from abc import ABC, abstractmethod
import traceback
import time


class ProyeccionCatastro(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...


class ProyeccionRegistrarCatastro(ProyeccionCatastro):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, operacion, id_propiedad, numero_catastro):
        self.operacion = operacion
        self.id_propiedad = id_propiedad
        self.numero_catastro = numero_catastro

    def ejecutar(self, db=None):
        if not db:
            print('ERROR: DB del app no puede ser nula')
            return

        print('Ejecutando proyección de catastro...')
        time.sleep(10)
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(
            RepositorioCatastroSQL.__class__)
        repositorio.agregar(
            Catastro(id_propiedad=self.id_propiedad,
                              numero_catastro=self.numero_catastro))
        db.commit()

        evento = CatastroRegistrado(id_propiedad=self.id_propiedad,
                                             numero_catastro=self.numero_catastro)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-creada')
        print('Proyección de catastro ejecutada!')




class ProyeccionReservaHandler(ProyeccionHandler):

    def handle(self, proyeccion: ProyeccionCatastro):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from propiedadesDA.conf.db import db_session as db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionRegistrarCatastro)
def ejecutar_proyeccion_catastro(proyeccion, app=None):
    if not app:
        print('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionReservaHandler()
            handler.handle(proyeccion)

    except:
        traceback.print_exc()
        print('ERROR: Persistiendo!')
