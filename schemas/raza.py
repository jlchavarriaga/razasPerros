
from fastapi import Query
from pydantic import BaseModel, Field,constr, PositiveInt
from typing import Optional, List
from datetime import date, datetime


class Raza(BaseModel):
    id : Optional[PositiveInt] = None
    nombre: constr( min_length=1, max_length=20, regex=r"^[A-Z ]{1,20}$")
    otros_nombres: str = Field(min_length=1, max_length=50, regex=r"^[A-Z ]{1,50}$")
    peso_kg: PositiveInt
    altura_cm: PositiveInt
    esperanza_vida: PositiveInt
    pais_origen: Optional[constr(min_length=2,max_length=30)]
    descripcion: constr(max_length=200)
    
    fecha_edicion: Optional[datetime]
    fecha_hora_creacion: Optional[datetime]
    estado: Optional[bool]


    class Config:
        schema_extra = {
            "example": {
                "nombre": "PITBULL",
                "otros_nombres": "",
                "peso_kg": "23",
                "altura_cm": "30",
                "esperanza_vida": "9",
                "pais_origen": "EEUU",
                "descripcion":"REQUIEREN ACTIVIDAD FISICA",
                "fecha_ingreso" : "2023-05-07"
            }
        }