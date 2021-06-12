import mysql.connector as mysql
from Tools.clases import *
import re

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

def getFactura():
    query = "SELECT * FROM factura"
        
    cursor = db.cursor()
    cursor.execute(query)

    COLUMNS_FACTURA = ['Clave', 'CodigoActividad', 'NumeroConsecutivo', 'FechaEmision', 'EmisorNombre', 'EmisorIdentificacionTipo', 'EmisorIdentificacionNumero', 'EmisorUbicacionProvincia', 'EmisorUbicacionCanton', 'EmisorUbicacionDistrito', 'EmisorUbicacionBarrio', 'EmisorUbicacionOtrasSenas', 'EmisorTelefonoCodigoPais', 'EmisorTelefonoNumTelefono', 'EmisorCorreoElectronico', 'ReceptorNombre', 'ReceptorIdentificacionTipo', 'ReceptorIdentificacionNumero', 'ReceptorCorreoElectronico', 'CondicionVenta', 'MedioPago', 'ResumenFacturaCodigoTipoMonedaCodigoMoneda', 'ResumenFacturaCodigoTipoMonedaTipoCambio', 'ResumenFacturaTotalServGravados', 'ResumenFacturaTotalServExentos', 'ResumenFacturaTotalMercanciasGravadas', 'ResumenFacturaTotalMercanciasExentas', 'ResumenFacturaTotalGravado', 'ResumenFacturaTotalExento', 'ResumenFacturaTotalVenta', 'ResumenFacturaTotalDescuentos', 'ResumenFacturaTotalVentaNeta', 'ResumenFacturaTotalImpuesto', 'ResumenFacturaTotalComprobante', 'OtrosOtroTexto']

    records = cursor.fetchall()

    temp_records = []
    ind = 0
    for r in records:
        for rr in r:
            newData = "{}: {}".format(re.sub(r"(\w)([A-Z])", r"\1 \2", COLUMNS_FACTURA[ind]), rr)
            temp_records.append(newData)
            # print(newData)
            ind += 1

    if len(temp_records) > 0:
        return Request(1, temp_records, "")
    return Request(0, [], "Factura no encontrada")

