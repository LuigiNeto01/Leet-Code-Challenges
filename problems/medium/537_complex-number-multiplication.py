class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse first complex number: split at '+' to get real and imaginary parts
        # Example: "1+1i" -> parts = ["1", "1i"]
        real1, imag1 = num1.split('+')
        # Convert real part to int, and imaginary part to int (strip trailing 'i')
        real1 = int(real1)
        imag1 = int(imag1.rstrip('i'))
        
        # Parse second complex number similarly
        real2, imag2 = num2.split('+')
        real2 = int(real2)
        imag2 = int(imag2.rstrip('i'))
        
        # Multiply using complex number formula:
        # (a+bi)*(c+di) = (ac - bd) + (ad + bc)i
        real_result = real1 * real2 - imag1 * imag2
        imag_result = real1 * imag2 + imag1 * real2
        
        # Format result as "real+imaginaryi"
        return f"{real_result}+{imag_result}i"