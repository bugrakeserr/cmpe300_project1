import math

def analyze_operations(n):
    # Calculate the first term for 'c' with harmonic sum using integer division
    harmonic_sum = sum(1 // i for i in range(1, n + 1))
    term_c = (n / 8) * (n + n * harmonic_sum)

    # Contributions for 'm' and 'p' are 0
    term_m = 0
    term_p = 0

    # Calculate the fourth term for 'e'
    term_e = (n**2 - n) / 4

    # Final result
    total_operations = term_c + term_m + term_p + term_e

    return {
        'term_c': term_c,
        'term_m': term_m,
        'term_p': term_p,
        'term_e': term_e,
        'total_operations': total_operations
    }

# Example usage:
n = 10  # You can change this to any value you want to analyze
result = analyze_operations(n)
for key, value in result.items():
    print(f"{key}: {value}")