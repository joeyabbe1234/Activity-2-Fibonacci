import time
import matplotlib.pyplot as plt

arr2 = []
arr3 = []
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms =int(input("Enter a number: "))
arr3.append(nterms)
start_time = time.time()
print(arr3)

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

nterms =int(input("Enter a number: "))
arr3.append(nterms)
start_time = time.time()
print(arr3)

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       

print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

nterms =int(input("Enter a number: "))
arr3.append(nterms)
start_time = time.time()
print(arr3)

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       

print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)


x = arr3
y = arr2
plt.xlabel('Number of terms')
plt.ylabel('execution time')
plt.plot(x, y)
plt.title("Fibonacci Recursive")
plt.show()
