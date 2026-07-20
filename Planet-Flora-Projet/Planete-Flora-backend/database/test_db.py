from database.db import db


connection = db.connect()


if connection:
    print("Connexion OK")

else:
    print("Connexion échouée")