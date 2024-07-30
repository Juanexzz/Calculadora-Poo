class Calculator:

    def add(self, a: float, b: float) -> float:
        return a + b

    def substract(self, a: float, b: float) -> float:
        return a - b

    def nultiply(self, a: float, b: float) -> float:
        return a * b

    def divition(self, a: float, b: float) -> float:
        if b == 0:
            return "Cannot divide by 0!"
        return a / b