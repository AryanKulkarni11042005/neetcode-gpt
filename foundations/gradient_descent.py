def power_derivative_value(x, n) -> float:
        if n == 0:
            return 0
        return n * (x ** (n - 1))
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        for _ in range(iterations):
            gradient = power_derivative_value(init, 2)
            init = float(init) - float(learning_rate) * float(gradient)
        return round(init, 5)
        pass

