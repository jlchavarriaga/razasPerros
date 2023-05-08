from configuracion.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean,Date, DateTime
from datetime import datetime


class Raza(Base):
    __tablename__ = "razas"
    id = Column(Integer, primary_key = True,index=True)
    nombre = Column(String,nullable=False,unique=True, index=True)
    otros_nombres = Column(String,nullable=True)
    peso_kg  = Column(Integer,nullable=False)
    altura_cm  = Column(Integer,nullable=False)
    esperanza_vida  = Column(String,nullable=False)
    pais_origen = Column(String)
    descripcion  =Column(String,nullable=False)    
    fecha_edicion= Column(DateTime,default=datetime.now,onupdate=datetime.now)
    fecha_hora_creacion= Column(DateTime, default=datetime.now) #Excluir de la edicion
    estado = Column(Boolean, default=True)#Excluir de la edicion