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


gcd_calculator = EuclideanAlgorithm(1180, 482)
# Compute the GCD
result = gcd_calculator.gcd()
# Print the result
print("The GCD is:", result)
