import xml.etree.ElementTree as ET
import xmltodict, json
import os

RUTA = 'FacturaExamen.xml'

def convert():
    with open(RUTA, 'r') as myfile:
        obj = xmltodict.parse(myfile.read())
        xml_to_json = json.dumps(obj)
        saveJSONFile(xml_to_json)

def queryToSQL(table, list_column, list_values):
    query = "INSERT INTO {0} ({1}) VALUES ({2})".format(table, list_column, list_values)
    return query

def saveIntoSQLFile(fullQuery, fileNumber):
    fileQuery = "Output/query_{0}.sql".format(fileNumber)
    if os.path.exists(fileQuery):
        os.remove(fileQuery)
    
    f = open(fileQuery, "a")
    f.write(fullQuery)

    f.close()

def saveJSONFile(json_):
    fileQuery = "Output/xml_to_json.json"
    if os.path.exists(fileQuery):
        os.remove(fileQuery)
    
    f = open(fileQuery, "a")
    f.write(json_)

    f.close()