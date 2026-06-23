from fastapi import APIRouter, HTTPException

from services.telemetry_service import gerar_telemetria

from services.mongo_service import (
    salvar_telemetria,
    listar_telemetrias,
    buscar_por_id
)

router = APIRouter(
    prefix="/telemetria",
    tags=["Telemetria"]
)


@router.post("/")
def criar_telemetria():

    telemetria = gerar_telemetria()

    id_documento = salvar_telemetria(telemetria)

    return {
        "mensagem": "Telemetria salva",
        "id": id_documento
    }


@router.get("/")
def listar():

    return listar_telemetrias()


@router.get("/{id_documento}")
def buscar(id_documento: str):

    documento = buscar_por_id(id_documento)

    if not documento:

        raise HTTPException(
            status_code=404,
            detail="Documento não encontrado"
        )

    return documento