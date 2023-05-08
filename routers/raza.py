from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from configuracion.database import Session
from models.raza  import Raza  as razaModel
from fastapi.encoders import jsonable_encoder
from services.raza  import RazaService
from schemas.raza  import Raza 

raza_router = APIRouter()    

@raza_router.get('/razas', tags=['razas'], response_model=List[Raza], status_code=200)
def get_raza() -> List[Raza]:
    db = Session()
    result = RazaService(db).get_razas()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@raza_router.get('/razas/{id}', tags=['razas'], response_model=Raza)
def get_raza(id: int = Path(ge=1, le=2000)) -> Raza:
    db = Session()
    result = RazaService(db).get_raza(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@raza_router.post('/razas', tags=['razas'], response_model=dict, status_code=201)
def create_raza(raza: Raza) -> dict:
    db = Session()
    RazaService(db).create_raza(raza)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la raza"})

@raza_router.put('/razas/{id}', tags=['razas'], response_model=dict, status_code=200)
def update_raza(id: int, raza: Raza) -> dict:
    db = Session()
    result = RazaService(db).get_raza(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})

    RazaService(db).update_raza(id, raza)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la raza"})


@raza_router.delete('/razas/{id}', tags=['razas'], response_model=dict, status_code=200)
def delete_raza(id: int) -> dict:
    db = Session()
    result: razaModel = db.query(razaModel).filter(razaModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró la raza"})
    RazaService(db).delete_raza(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la raza"})
