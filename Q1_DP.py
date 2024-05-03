import time
import matplotlib.pyplot as plt

def fibonacci_bottom_up(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def measure_execution_time(method, n):
    start_time = time.time()
    method(n)
    end_time = time.time()
    return end_time - start_time

n_values = list(range(1, 101))
execution_times_bottom_up = []

for n in n_values:
    execution_time_bottom_up = measure_execution_time(fibonacci_bottom_up, n)
    execution_times_bottom_up.append(execution_time_bottom_up)

plt.figure(figsize=(10, 5))
plt.plot(n_values, execution_times_bottom_up, label='DP')
plt.title('Execution Time of Fibonacci Calculation (DP)')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.show()
