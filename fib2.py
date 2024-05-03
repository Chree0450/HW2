import time
import matplotlib.pyplot as plt


f4_counts = [0,0,0,0,1]
for i in range(5, 51):
    print(i)
    f4_counts.append(f4_counts[i-1]+f4_counts[i-2])
print(f4_counts)
plt.figure(figsize=(10, 5))
plt.plot(range(5, 51), f4_counts[5:51])
plt.xlabel('n')
plt.ylabel('Count of F(4) Calls')
plt.title('Overlapping Subproblems in Fibonacci Calculations')
plt.show()