import time
import matplotlib.pyplot as plt
import os


folder_path = r'path\fibonacci_plots'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        try:
            return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
        except RecursionError:
            print("Recursion limit reached at n =", n)
            return None  


def measure_execution_time(method, n):
    start_time = time.time()
    result = method(n) 
    end_time = time.time()
    return end_time - start_time, result

n_values = list(range(1, 101))
execution_times_recursive = []

for n in n_values: 
    print(f"Calculating for n = {n}")
    execution_time_recursive, result = measure_execution_time(fibonacci_recursive, n)
    if n>=2:
        print(f"time = {execution_times_recursive[n-2]}")
    if result is not None:
        execution_times_recursive.append(execution_time_recursive)

        plt.figure(figsize=(10, 5))
        plt.plot(n_values[:len(execution_times_recursive)], execution_times_recursive, label='Recursive')
        plt.title(f'Execution Time of Fibonacci Calculation at n = {n}')
        plt.xlabel('n')
        plt.ylabel('Time (s)')
        plt.legend()
        plt.grid(True)

        plt.savefig(f'{folder_path}/fibonacci_{n}.png')
        plt.close()
    else:
        print("Stopped due to recursion limit.")
        break
