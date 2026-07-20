from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes import plants
from routes import identify
from routes import diseases
from routes import history

app = FastAPI(

    title="Planet Flora API",

    description="IA de reconnaissance végétale 🌱"

)

app.include_router(

    history.router,

    prefix="/api/history"

)



app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)






app.include_router(

    plants.router,

    prefix="/api/plants"

)



app.include_router(
    identify.router,
    prefix="/api/identify"
)



app.include_router(

    diseases.router,

    prefix="/api/diseases"

)






@app.get("/")

def home():

    return {

        "message":

        "Planet Flora API 🌱"

    }