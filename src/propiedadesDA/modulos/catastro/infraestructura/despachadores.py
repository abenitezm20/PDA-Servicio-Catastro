import pulsar
from pulsar.schema import *

from propiedadesDA.modulos.catastro.infraestructura.schema.v1.eventos import EventoRegistroCatastroCreado, RegistroCatastroPayload
from propiedadesDA.modulos.catastro.infraestructura.schema.v1.comandos import ComandoRegistrarCatastro, ComandoRegistrarCatastroPayload
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
            propiedad_id=str(evento.propiedad_id),
            numero_catastral=str(evento.numero_catastral),
            estrato=str(evento.estrato),
            pisos=str(evento.pisos),
        )
        evento_integracion = EventoRegistroCatastroCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoRegistroCatastroCreado))

    def publicar_comando(self, dto, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        # if isinstance(comando, ComandoRegistrarArrendamiento):
        #     print('AQUI :)')
        payload = ComandoRegistrarCatastroPayload(
            propiedad_id=dto.propiedad_id,
            numero_catastral=dto.numero_catastral,
            estrato=dto.estrato,
            pisos=dto.pisos,
        )

        comando_integracion = ComandoRegistrarCatastro(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoRegistrarCatastro))
