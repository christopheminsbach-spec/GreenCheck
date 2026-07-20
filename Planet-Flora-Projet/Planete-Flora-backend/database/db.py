import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self):
        self.connection = None


    def connect(self):

        try:

            self.connection = pymysql.connect(

                host=os.getenv("DB_HOST"),

                port=int(os.getenv("DB_PORT",3306)),

                user=os.getenv("DB_USER"),

                password=os.getenv("DB_PASSWORD"),

                database=os.getenv("DB_NAME"),

                cursorclass=pymysql.cursors.DictCursor,

                autocommit=True,

                charset="utf8mb4"

            )


            print("✅ Connexion MySQL réussie")


            return self.connection



        except Exception as e:

            print(
                f"❌ Erreur MySQL : {e}"
            )

            return None



    def close(self):

        if self.connection:

            self.connection.close()



db = Database()