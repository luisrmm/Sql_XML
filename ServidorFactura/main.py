import xml.etree.ElementTree as ET
from Tools.functions import *
from Tools.mysql_ import *
from Tools.serverThreads import server

filename = "FacturaExamen.xml"
xmlTree = ET.parse(filename)

rootElement = xmlTree.getroot()

COLUMNS_FACTURA = ['Clave', 'CodigoActividad', 'NumeroConsecutivo', 'FechaEmision', 'Emisor', 'Receptor', 'CondicionVenta', 'MedioPago', 'ResumenFactura', 'Otros']

def getDataQueryTwo():
    columns = []
    values = []
    indice = -1

    for tag in ['DetalleServicio']:
        for element in rootElement.findall(tag):

            if (element.tag and bool(element.text.strip())): 
                columns.append(element.tag)
                values.append(element.text)

            for level_1 in element: # DetalleServicio
                indice += 1
                columns.append([])
                values.append([])

                if (level_1.tag and bool(level_1.text.strip()) ):
                    columns[indice].append(element.tag + level_1.tag)
                    values[indice].append(level_1.text)

                for level_2 in level_1: # LineaDetalle
                    if (level_2.tag and bool(level_2.text.strip())):
                        columns[indice].append(element.tag + level_1.tag + level_2.tag)
                        values[indice].append(level_2.text)

                    for level_3 in level_2: # CodigoComercial
                        if (level_3.tag and bool(level_3.text.strip())):
                            columns[indice].append(element.tag + level_1.tag + level_2.tag + level_3.tag)
                            values[indice].append(level_3.text)
    return [columns, values]

def getDataQueryOne():
    columns = []
    values = []

    for tag in COLUMNS_FACTURA:
        for element in rootElement.findall(tag):
            if (element.tag and bool(element.text.strip())):
                columns.append(element.tag)
                values.append(element.text)


            for level_1 in element:
                if (level_1.tag and bool(level_1.text.strip()) ):
                    columns.append(element.tag + level_1.tag)
                    values.append(level_1.text)

                for level_2 in level_1:
                    if (level_2.tag and bool(level_2.text.strip())):
                        columns.append(element.tag + level_1.tag + level_2.tag)
                        values.append(level_2.text)

                    for level_3 in level_2:
                        if (level_3.tag and bool(level_3.text.strip())):
                            columns.append(element.tag + level_1.tag + level_2.tag + level_3.tag)
                            values.append(level_3.text)
    return [columns, values]

def part_1():
    str_columns_1 = ""
    str_values_2 = ""
    SEPARADOR = ", "
    objectQueryOne = getDataQueryOne()
    objectQueryTwo = getDataQueryTwo()
    
    for c in objectQueryOne[0]:
        str_columns_1 += c + SEPARADOR

    for v in objectQueryOne[1]:
        str_values_2 += "'" + v + "'" + SEPARADOR

    fullQueryOne = queryToSQL('factura', str_columns_1[0: -2], str_values_2[0: -2])

    # print(str_columns_1)
    str_columns_2 = ""
    objectQueryTwo[0][0].insert(0, "ClaveFacturaElectronica")

    for c in objectQueryTwo[0][0]:
        str_columns_2 += c + SEPARADOR

    clave = objectQueryOne[1][0]

    len_objectTwo = len(objectQueryTwo[1])

    i = 0
    for v in range(len_objectTwo):
        objectQueryTwo[1][i].insert(0, clave)
        i += 1

    fullQueryTwo = queryToSQL('detalleservicio', str_columns_2[0: -2], objectQueryTwo[1])

    formattedQuery = fullQueryTwo.replace("([[", "(").replace("]])", ")").replace("[", "(").replace("]", ")")

    connectDB()

    saveIntoSQLFile(fullQueryOne, 1)
    saveIntoSQLFile(formattedQuery, 2)

    insertFactura(fullQueryOne)
    insertFactura(formattedQuery)

def part_2():
    convert()

def part_3():
    server()

def main():
    part_1()
    # part_2()

    part_3()

if __name__ == "__main__":
    main()