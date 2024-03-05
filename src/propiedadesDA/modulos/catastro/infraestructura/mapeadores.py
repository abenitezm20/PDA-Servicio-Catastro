from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.modulos.catastro.dominio.entidades import Catastro
from .dto import Catastro as CatastroDTO

class MapeadorCatastro(Mapeador):

    def obtener_tipo(self) -> type:
        return Catastro.__class__

    def entidad_a_dto(self, entidad: Catastro) -> CatastroDTO:
        catastro_dto = CatastroDTO(
            entidad.propiedad_id,
            entidad.numero_catastral,
            entidad.estrato,
            entidad.pisos
        )

        return catastro_dto

    def dto_a_entidad(self, dto: CatastroDTO) -> Catastro:
        catastro = Catastro(
            numero_catastral=dto.numero_catastral,
            estrato=dto.estrato,
            pisos=dto.pisos,
            propiedad_id=dto.propiedad_id,
        )
        
        return catastro