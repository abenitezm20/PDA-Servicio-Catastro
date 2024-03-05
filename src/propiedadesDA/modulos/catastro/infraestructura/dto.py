from propiedadesDA.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class Catastro(Base):
    __tablename__ = "catastro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    propiedad_id = Column(String)
    numero_catastral = Column(String)
    estrato = Column(String)
    pisos = Column(String)

    def __init__(self, propiedad_id, numero_catastral, estrato, pisos):
        self.propiedad_id = propiedad_id
        self.numero_catastral = numero_catastral
        self.estrato = estrato
        self.pisos = pisos