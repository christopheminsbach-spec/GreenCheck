from database.db import db


connection = db.connect()


if connection:

    print("✅ Test base de données OK")

    cursor = connection.cursor()

    cursor.execute("SELECT DATABASE();")

    result = cursor.fetchone()

    print(result)


    db.close()


else:

    print("❌ Connexion impossible")

