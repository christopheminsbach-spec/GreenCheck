from fastapi import APIRouter


router=APIRouter()



@router.get("/")
def diseases():


    return [

        {
        "name":
        "Mildiou",

        "symptoms":[
            "taches jaunes",
            "feuilles sèches"
        ],

        "treatment":
        "Traitement antifongique"
        },


        {
        "name":
        "Rouille",

        "symptoms":[
            "points oranges"
        ],

        "treatment":
        "Retirer les feuilles infectées"
        }

    ]