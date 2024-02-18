from app.backend.calculations.addition import Addition
from app.backend.calculations.division import Division
from app.backend.calculations.multiplication import Multiplication
from app.backend.calculations.subtraction import Subtraction

OPERATOR_MAPPING = {
    "+": Addition,
    "-": Subtraction,
    "*": Multiplication,
    "/": Division,
}
