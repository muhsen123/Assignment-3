class EuclideanAlgorithm:
    """
    A class to represent the Euclidean Algorithm for finding the greatest common divisor (GCD).
    """

    def __init__(self, a, b):
        """
        Initialize the instance with two integers a and b.
        
        :param a: first integer
        :param b: second integer
        """
        self.a = a
        self.b = b

    def gcd(self):
        """
        Compute the GCD of the two integers using the Euclidean Algorithm.

        Returns:
            int: the greatest common divisor of a and b
        """
        a, b = self.a, self.b
        while b != 0:
            r = a % b
            a, b = b, r
        return a

def main():
    try:
        a = int(input("Enter the first non-negative integer: "))
        b = int(input("Enter the second non-negative integer: "))

        # Validate input: both numbers should be non-negative
        if a < 0 or b < 0:
            raise ValueError("Both numbers must be non-negative.")

        # Instantiate and use the EuclideanAlgorithm class
        if a == 0 and b == 0:
            print("At least one number must be non-zero.")
        else:
            gcd_calculator = EuclideanAlgorithm(a, b)
            result = gcd_calculator.gcd()
            print("The GCD is:", result)
    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("An error occurred:", e)


main()
