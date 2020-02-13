import time
import matplotlib.pyplot as plt

arr2 = []
arr3 = []
n = int(input("Enter a number: "))
arr3.append(n)
start_time = time.time()
print(arr3)

def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 
  

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
plt.title("Fibonacci")
plt.show()
