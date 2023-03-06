import numpy as np

def evaluate_polynomial(coefficients, s):
    """Evaluates a polynomial with the given coefficients at the point s."""
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (s ** (len(coefficients) - i - 1))
    return result

def routh_stability(coefficients, K):
    """Computes and displays the Routh table for the polynomial with the given coefficients and K value."""
    n = len(coefficients)
    table = np.zeros((n, (n+1)//2))
    table[0, :] = coefficients[::2]
    table[1, :] = coefficients[1::2]
    for i in range(2, n):
        for j in range((n+1)//2):
            if j == 0:
                table[i, j] = -1 / table[i-1, 1] * (table[i-2, 0] * (K if i == n-1 else 1) - table[i-1, 1] * table[i-2, j+1])
            else:
                table[i, j] = -1 / table[i-1, 1] * (table[i-2, j-1] * (K if i == n-1 else 1) - table[i-1, 1] * table[i-2, j])
    return table

def is_stable(table):
    """Determines if the polynomial represented by the Routh table is stable."""
    signs = np.sign(table[:, 0])
    changes = np.diff(signs)
    return np.all(changes >= 0) or np.all(changes <= 0)

# Example usage
coefficients = [1, 3, 3, 2]

# Evaluate the polynomial at s = 2
s = 2
value = evaluate_polynomial(coefficients, s)
print(f"The value of the polynomial at s = {s} is: {value}")

# Prompt the user for the value of K
K = float(input("Enter a value for K: "))

# Compute and display the Routh table
table = routh_stability(coefficients, K)
print("The Routh table is:")
print(table)

# Check stability
if is_stable(table):
    print("The polynomial is stable.")
else:
    print("The polynomial is unstable.")

# Prompt the user for a new value of K and compute the new Routh table
K = float(input("Enter a new value for K: "))
table = routh_stability(coefficients, K)
print(f"The Routh table with K = {K} is:")
print(table)

# Check stability again
if is_stable(table):
    print("The polynomial is stable.")
else:
    print("The polynomial is unstable.")
