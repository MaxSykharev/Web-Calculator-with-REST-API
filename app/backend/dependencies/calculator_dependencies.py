from fastapi import HTTPException

from app.backend.api.models import CalculationRequest
from app.backend.mappers.operator_mapper import OPERATOR_MAPPING

def get_operator(calculation: CalculationRequest):
    operator_class = OPERATOR_MAPPING.get(calculation.operator)
    if operator_class:
        return operator_class()
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")
