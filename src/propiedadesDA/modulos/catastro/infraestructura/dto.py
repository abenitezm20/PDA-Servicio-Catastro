from propiedadesDA.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class Catastro(Base):
    __tablename__ = "catastro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_propiedad = Column(String)
    numero_catastro = Column(String)

    def __init__(self, id_propiedad, numero_catastro):
        self.id_propiedad = id_propiedad
        self.numero_catastro = numero_catastro