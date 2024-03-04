
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real_part, imag_part)


if __name__ == '__main__':
    # Create two complex numbers
    c1 = ComplexNumber(3, 2)  # Represents: 3 + 2i
    c2 = ComplexNumber(1, 7)  # Represents: 1 + 7i

    # Add the two complex numbers using the __add__ method
    sum_result = c1+c2
    # Expected Output: Sum: 4 + 9i
    print(f"Sum: {sum_result.real} + {sum_result.imag}i")

    # Multiply the two complex numbers using the mul__ method
    product_result = c1 * c2
    # Expected Output: Product: -11 + 231
    print(f"Product: {product_result.real} + {product_result.imag}i")
