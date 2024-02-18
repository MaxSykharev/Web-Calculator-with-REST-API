from fastapi import APIRouter, Depends
from app.backend.api.models import CalculationResponse, CalculationRequest

from app.backend.dependencies.calculator_dependencies import get_operator

router = APIRouter()

@router.post("/calculate/", response_model=CalculationResponse)
async def calculate(calculation: CalculationRequest, op=Depends(get_operator)):
    result = op.calculate(calculation.operand1, calculation.operand2)
    return {"result": result}
