import random
import time
import matplotlib.pyplot as plt

# Function to generate a random matrix of size n x n
def generate_random_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

# Function to multiply two matrices and measure execution time
def matrix_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    start_time = time.time()
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    end_time = time.time()
    
    return end_time - start_time

# Values of n to test
n_values = list(range(2, 151))

# Measure execution times for each n
execution_times = []

# Specify specific values of n to highlight in red
specific_values = [30, 50, 80, 100, 150]

for n in n_values:
    A = generate_random_matrix(n)
    B = generate_random_matrix(n)
    execution_time = matrix_multiply(A, B)
    execution_times.append(execution_time)

print(execution_times)

# Extract the execution times for specific values of n
specific_execution_values = [execution_times[n_values.index(n)] for n in specific_values]

# print(execution_times)

for i in range(len(n_values)):
    x = str(n_values[i])
    y = str(execution_times[i])
    print("The execution time for a " + x + "x" + x + " is: " + y)

print("\n\nSpecific execution times: \n\n")

for i in range(len(specific_execution_values)):
    x = str(specific_values[i])
    y = str(specific_execution_values[i])
    print("The execution time for a " + x + "x" + x + " is: " + y)

# Remove specific values of n from the list of all values
n_values = [n for n in n_values if n not in specific_values]

# Plot the execution time function of n
plt.plot(n_values, execution_times[:-len(specific_values)], marker='o', markersize=2, label='Execution Time')
plt.xlabel('Matrix Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Matrix Multiplication Execution Time vs. Matrix Size')

# Mark specific values on the graph in red
for n, execution_time in zip(specific_values, specific_execution_values):
    plt.scatter(n, execution_time, marker='o', c='red', s=20)

# Add a legend
plt.legend()

# Grid lines
plt.grid(True)

plt.show()


