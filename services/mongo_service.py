from bson import ObjectId

from database.connection import db

telemetry_collection = db["telemetry"]


def salvar_telemetria(dados):

    resultado = telemetry_collection.insert_one(dados)

    return str(resultado.inserted_id)


def listar_telemetrias():

    documentos = []

    for doc in telemetry_collection.find():

        doc["_id"] = str(doc["_id"])

        documentos.append(doc)

    return documentos


def buscar_por_id(id_documento):

    documento = telemetry_collection.find_one(
        {"_id": ObjectId(id_documento)}
    )

    if documento:

        documento["_id"] = str(documento["_id"])

    return documento