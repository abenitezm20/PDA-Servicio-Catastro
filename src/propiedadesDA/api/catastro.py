from flask import Blueprint, Response, request
from propiedadesDA.modulos.catastro.aplicacion.queries.obtener_catastro import ObtenerCatastro
from propiedadesDA.modulos.catastro.aplicacion.mapeadores import MapeadorCatastroDTOJson
from propiedadesDA.seedwork.aplicacion.queries import ejecutar_query

from propiedadesDA.modulos.catastro.infraestructura.despachadores import Despachador

ca = Blueprint('catastro', __name__)

@ca.route('/catastro/health', methods = ['GET'])
def health():
    return Response({'result': 'OK'})

@ca.route('/catastro/propiedad/<id>', methods = ['GET'])
def obtener_catastro(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCatastro(id))
        map_catastro = MapeadorCatastroDTOJson()
        return map_catastro.dto_a_externo(query_resultado.resultado)
    else:
        return Response({'message': 'GET'})

@ca.route('/async-catastro', methods=['POST'])
def registrar_propiedad_contratro_async():
    map_propiedad = MapeadorCatastroDTOJson()
    catastro_dto = map_propiedad.externo_a_dto(request.json)

    # comando = ComandoRegistrarArrendamiento(
    #     propiedad_id=arriendo_dto.propiedad_id,
    #     numero_contrato=arriendo_dto.numero_contrato,
    #     fecha_creacion=arriendo_dto.fecha_creacion,
    #     fecha_actualizacion=arriendo_dto.fecha_actualizacion,)   

    Despachador().publicar_comando(catastro_dto, 'comandos-catastro')
    return Response('{}', status=202, mimetype='application/json')