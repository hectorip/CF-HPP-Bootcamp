import numpy as np
import time

arr_list = list(range(100_000_000)) 

arr_np = np.array(arr_list, dtype=np.int32)

def calcular_suma_numpy():
    start = time.time()
    res_numpy = np.sum(arr_np) # Operación vectorizada
    end = time.time()
    tiempo = end - start
    return res_numpy, tiempo

resultado, tiempo = calcular_suma_numpy()
print(f"NumPy. Resultado = {resultado:,}. Tiempo = {tiempo:.4f} s")
