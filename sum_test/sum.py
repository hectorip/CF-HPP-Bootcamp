import time

def sum_array_py(arr):
    total = 0
    for x in arr:
        total += x
    return total

arr = range(100_000_000)

start = time.time()
suma = sum_array_py(arr)
end = time.time()

print(f"Python sum = {suma}. Tiempo = {end - start:.4f} s")

