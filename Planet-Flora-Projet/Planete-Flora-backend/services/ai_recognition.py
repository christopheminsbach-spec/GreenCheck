import os
import requests

from dotenv import load_dotenv


load_dotenv()


PLANTNET_API_KEY = os.getenv(
    "PLANTNET_API_KEY"
)



def recognize(image_file):


    url = "https://my-api.plantnet.org/v2/identify/all"



    files = {

        "images": (

            image_file.filename,

            image_file.file,

            image_file.content_type

        )

    }



    data = {

        "organs":"leaf"

    }



    params = {

        "api-key": PLANTNET_API_KEY

    }



    response = requests.post(

        url,

        params=params,

        files=files,

        data=data

    )



    if response.status_code != 200:

        return {

            "error":"PlantNet erreur",

            "details":response.text

        }



    result=response.json()



    if not result.get("results"):

        return {

            "message":"Aucune plante trouvée"

        }



    best=result["results"][0]



    return {

        "plante":
        best["species"]["scientificName"],


        "noms_communs":
        best["species"].get(
            "commonNames",
            []
        ),


        "confiance":
        round(
            best["score"] * 100,
            2
        )

    }