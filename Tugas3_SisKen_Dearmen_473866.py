import numpy as np

def evaluate_polynomial(coefficients, s):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (s ** (len(coefficients) - i - 1))
    return result

def routh_stability(coefficients, K):0
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

# Example usage
coefficients = [1, 3, 3, 1]

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

# Prompt the user for a new value of K and compute the new Routh table
K = float(input("Enter a new value for K: "))
table = routh_stability(coefficients, K)
print(f"The Routh table with K = {K} is:")
print(table)
