import time
import matplotlib.pyplot as plt

arr2 = []
arr3 = []
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

n = int(input("Enter a number: "))
arr3.append(n)
start_time = time.time()
print(arr3)
print(fibonacci(n))
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

n = int(input("Enter a number: "))
arr3.append(n)
start_time = time.time()
print(arr3)
print(fibonacci(n))
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

n = int(input("Enter a number: "))
arr3.append(n)
start_time = time.time()
print(arr3)
print(fibonacci(n))
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)


x = arr3
y = arr2
plt.xlabel('Number of terms')
plt.ylabel('execution time')
plt.plot(x, y)
plt.title("Fibonacci Iteration")
plt.show()
