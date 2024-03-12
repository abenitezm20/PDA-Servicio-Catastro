from propiedadesDA.seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from propiedadesDA.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesDA.modulos.catastro.aplicacion.dto import CatastroDTO
from propiedadesDA.modulos.catastro.dominio.entidades import Catastro

class MapeadorCatastroDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> CatastroDTO:
        catastro_dto = CatastroDTO
        catastro_dto.numero_catastro = externo.get('numero_catastro')
        catastro_dto.id_propiedad = externo.get('id_propiedad')
        return catastro_dto
    
    def dto_a_externo(self, dto: CatastroDTO) -> dict:
        return dto.__dict__
    
    def obtener_tipo(self) -> type:
        return Catastro.__class__


class MapeadorCatastro(RepMap):
    def dto_a_entidad(self, dto: CatastroDTO) -> Catastro:
        entidad = Catastro()
        entidad.numero_catastro = dto.numero_catastro
        entidad.id_propiedad = dto.id_propiedad
        return entidad
    
    def entidad_a_dto(self, entidad: Catastro) -> CatastroDTO:
        dto = CatastroDTO(
            entidad.numero_catastro,
            entidad.id_propiedad,
        )
        return dto
    
    def obtener_tipo(self) -> type:
        return Catastro.__class__