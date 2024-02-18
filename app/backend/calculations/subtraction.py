from app.backend.calculations.operation import Operation


class Subtraction(Operation):
    def calculate(self, x: float, y: float) -> float:
        return x - y