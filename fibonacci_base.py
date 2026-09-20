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
		futures = [
			executor.submit(fibonacci, i) for i in range(n_elementos)
		]

		for i, future in enumerate(concurrent.futures.as_completed(futures)):
			resultados[i] = future.result()

	fin = time.time()
	tiempo_ejecucion = fin - inicio
	print(f"Fibonacci ({n_elementos}): {resultados}")
	print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")


if __name__ == "__main__":
	calcular_fibonacci_paralelo(
		N, concurrent.futures.ThreadPoolExecutor
	)  # o ProcessPoolExecutor