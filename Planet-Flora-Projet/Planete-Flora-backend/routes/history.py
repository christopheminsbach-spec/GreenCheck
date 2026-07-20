from fastapi import APIRouter

from database.db import db


router = APIRouter()



@router.get("/")
def get_history():

    try:

        connection = db.connect()


        if connection is None:

            return {
                "error": "Connexion MySQL impossible"
            }



        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                id,
                plant_name,
                common_names,
                confidence,
                image,
                created_at

            FROM diagnostics

            ORDER BY created_at DESC
            """
        )


        result = cursor.fetchall()


        db.close()


        return result



    except Exception as e:


        return {

            "error": str(e)

        }