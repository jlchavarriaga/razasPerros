from fastapi import FastAPI
from starlette.responses import RedirectResponse
from configuracion.database import engine, Base

from routers.raza import raza_router


app = FastAPI()

app.title = "Razas de Perros "
app.version = "0.0.1"

app.include_router(raza_router)
Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def raiz():
    return RedirectResponse(url='/docs/')
