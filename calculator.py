class Calculator:
    def _validate(self, a, b):
        if not isinstance(a, (int, float)) or isinstance(a, bool) or \
           not isinstance(b, (int, float)) or isinstance(b, bool):
            raise ValueError("Inputs must be numbers, not strings or other types.")

    def add(self, a: float, b: float) -> float:
        self._validate(a, b)
        return a + b

    def subtract(self, a: float, b: float) -> float:
        self._validate(a, b)
        return a - b

    def multiply(self, a: float, b: float) -> float:
        self._validate(a, b)
        return a * b

    def divide(self, a: float, b: float) -> float:
        self._validate(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
