from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.modulos.catastro.dominio.entidades import Catastro
from .dto import Catastro as CatastroDTO

class MapeadorCatastro(Mapeador):

    def obtener_tipo(self) -> type:
        return Catastro.__class__

    def entidad_a_dto(self, entidad: Catastro) -> CatastroDTO:
        catastro_dto = CatastroDTO(
            entidad.id_propiedad,
            entidad.numero_catastro,
        )

        return catastro_dto

    def dto_a_entidad(self, dto: CatastroDTO) -> Catastro:
        catastro = Catastro(
            numero_catastro=dto.numero_catastro,
            id_propiedad=dto.id_propiedad,
        )
        
        return catastro