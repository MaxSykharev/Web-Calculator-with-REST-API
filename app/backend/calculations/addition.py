from app.backend.calculations.operation import Operation


class Addition(Operation):
    def calculate(self, x: float, y: float) -> float:
        return x + y