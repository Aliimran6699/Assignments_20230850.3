class Arithmetic:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        if self.second_number == 0:
            return "Error: Division by zero"
        return self.first_number / self.second_number


# Example usage:
arith = Arithmetic(5, 3)
print("Addition:", arith.addition())
print("Subtraction:", arith.subtraction())
print("Multiplication:", arith.multiplication())
print("Division:", arith.division())
