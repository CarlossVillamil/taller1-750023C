import time
import concurrent.futures

N = 40  # Número de Fibonacci a calcular

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calcular_fibonacci_paralelo(n_elementos, executor_type):
    inicio = time.time()
    resultados = [0] * n_elementos

    with executor_type() as executor:
        # relacionamos cada tarea con su posición original, porque as_completed
        # las devuelve a medida que terminan y no en el orden en que se enviaron
        futuros_a_indice = {
            executor.submit(fibonacci, i): i for i in range(n_elementos)
        }

        for futuro in concurrent.futures.as_completed(futuros_a_indice):
            indice = futuros_a_indice[futuro]
            resultados[indice] = futuro.result()

    fin = time.time()
    print(f"Fibonacci ({n_elementos}): {resultados}")
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    # se reemplaza ThreadPoolExecutor por ProcessPoolExecutor para eludir el GIL
    calcular_fibonacci_paralelo(N, concurrent.futures.ProcessPoolExecutor)