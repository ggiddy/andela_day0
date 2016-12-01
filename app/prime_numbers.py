# Function to generate prime numbers from 0 to n with assymptotic analysis

def generate_prime(n):
    """
    Genetates prime numbers from 0 to n
    """
    if not isinstance(n, int):
        return 'Pass numbers only'

    prime_numbers = []
    div = True

    if n < 0:
        return "Provide a positive number"
    else:
        for i in range(2, n+1):
            div = True

            for j in range(2, i):
                if i %j == 0:
                    div = False
            if div:
                prime_numbers.append(i)
        return prime_numbers