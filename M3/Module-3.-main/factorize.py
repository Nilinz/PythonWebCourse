import time
from multiprocessing import Pool, cpu_count

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    
    # Синхронно
    start_time = time.time()
    result_sync = [factorize(number) for number in numbers]
    end_time = time.time()
    
    print("Синхронна версія:")
    for i, number in enumerate(numbers):
        print(f"Число {number} розкладається на: {result_sync[i]}")
    print(f"Час виконання: {end_time - start_time:.4f} секунд")

    # Паралельно
    num_cores = cpu_count()
    start_time = time.time()
    with Pool(num_cores) as pool:
        result_parallel = pool.map(factorize_parallel, numbers)
    end_time = time.time()

    print("\nПаралельна версія:")
    for i, number in enumerate(numbers):
        print(f"Число {number} розкладається на: {result_parallel[i]}")
    print(f"Час виконання: {end_time - start_time:.4f} секунд")
