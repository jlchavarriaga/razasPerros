import datetime
from http.client import HTTPException

from starlette import status

from models.raza import Raza as RazaModel
from fastapi.responses import HTMLResponse, JSONResponse
from schemas.raza import Raza
from datetime import datetime

class RazaService():
    def __init__(self, db) -> None:
        self.db = db

    def get_razas(self):
        result = self.db.query(RazaModel).all()
        return result
    
    def get_raza(self, nombre):
        result = self.db.query(RazaModel).filter(RazaModel.id == nombre).first()
        return result    
    
    def create_raza(self, raza: Raza):
        new_raza = RazaModel(**raza.dict())
        
        #validacion si ya existe
        si_existe = self.db.query(RazaModel).filter(
            RazaModel.nombre == new_raza.nombre,
        ).all()
        
        if (si_existe.__len__() > 0):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Esta raza ya esta creado",
                                headers={"X-Error": "Este Raza ya esta creado"})
        else:
            nombre=new_raza.nombre.lower() 

            self.db.add(new_raza)
            self.db.commit()
        return   
    
    def update_raza(self, id: int, data: Raza):
        raza = self.db.query(RazaModel).filter(RazaModel.id == id).first()
        raza.nombre = data.nombre
        raza.otros_nombres = data.otros_nombres
        raza.peso_kg = data.peso_kg
        raza.altura_cm = data.altura_cm
        raza.esperanza_vida = data.esperanza_vida
        raza.pais_origen = data.pais_origen
        raza.descripcion = data.descripcion  
        raza.fecha_edicion = datetime.now()
        self.db.commit()
        return    
    
    def delete_raza(self, id: int):
        self.db.query(RazaModel).filter(RazaModel.id == id).delete()
        self.db.commit()
        return    
