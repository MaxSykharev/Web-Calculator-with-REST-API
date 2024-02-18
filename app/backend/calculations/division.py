from app.backend.calculations.operation import Operation


class Division(Operation):
    def calculate(self, x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y