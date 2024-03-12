import pulsar
from pulsar.schema import *

from propiedadesDA.modulos.catastro.infraestructura.schema.v1.eventos import EventoRegistroCatastroCreado, RegistroCatastroPayload
from propiedadesDA.modulos.catastro.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from propiedadesDA.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schemas):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schemas)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = RegistroCatastroPayload(
            id_propiedad=str(evento.id_propiedad),
            numero_catastro=str(evento.numero_catastro),
        )
        evento_integracion = EventoRegistroCatastroCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoRegistroCatastroCreado))

    def publicar_comando(self, dto, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        # if isinstance(comando, ComandoRegistrarArrendamiento):
        #     print('AQUI :)')
        payload = ComandoCrearPropiedadPayload(
            id_propiedad=dto.id_propiedad,
            numero_catastro=dto.numero_catastro,
        )

        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoCrearPropiedad))
