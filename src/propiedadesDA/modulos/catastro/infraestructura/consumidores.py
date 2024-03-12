import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback
import uuid
from datetime import datetime
from propiedadesDA.modulos.catastro.infraestructura.proyecciones import ProyeccionRegistrarCatastro

from propiedadesDA.modulos.catastro.infraestructura.schema.v1.eventos import EventoRegistroCatastroCreado
from propiedadesDA.modulos.catastro.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearCatastroFallido
from propiedadesDA.seedwork.infraestructura import utils

#from propiedadesDA.modulos.catastro.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando
from flask import session

from propiedadesDA.seedwork.infraestructura.proyecciones import ejecutar_proyeccion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        #consumidor = cliente.subscribe('eventos-catastro', consumer_type=_pulsar.ConsumerType.Shared,
        #                               subscription_name='pda-sub-eventos', schema=AvroSchema(EventoRegistroCatastroCreado))
        consumidor = cliente.subscribe('eventos-propiedad-creada', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-eventos', schema=AvroSchema(EventoRegistroCatastroCreado))
        
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        #consumidor = cliente.subscribe('comandos-catastro', consumer_type=_pulsar.ConsumerType.Shared,
        #                               subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))
        consumidor = cliente.subscribe('comandos-crear-propiedad', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad)) #ComandoCrearPropiedad
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            ejecutar_proyeccion(ProyeccionRegistrarCatastro(
                ProyeccionRegistrarCatastro.ADD,
                mensaje.value().data.id_propiedad,
                uuid.uuid4()
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_compensacion(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-crear-propiedad-fallida', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearCatastroFallido))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando compensacion recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionRegistrarCatastro(
                ProyeccionRegistrarCatastro.DELETE,
                mensaje.value().data.id_propiedad,
                uuid.uuid4(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()