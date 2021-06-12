import mysql.connector as mysql

db = None

def connectDB():
    global db

    db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "admin",
        database = "factura",
    )

    print("Connected to DB")

def insertFactura(fullQuery):
    try:
        global db

        cursor = db.cursor()
        cursor.execute(fullQuery)
        db.commit()

        print(cursor.rowcount, " Row Updated")

    except ValueError:
        print(ValueError)
    except mysql.Error as err:
        print("Something went wrong: {}".format(err))
    