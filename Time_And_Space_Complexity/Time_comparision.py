import time

# Nested loop approach
def nested_loop_approach():
    start = time.perf_counter()
    
    n = 1000
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    
    end = time.perf_counter()
    print(f"Nested loop approach execution time: {end - start} seconds")

# Single loop approach
def single_loop_approach():
    start = time.perf_counter()
    
    n = 1000
    count = 0
    for i in range(n):
        count += 1
    
    end = time.perf_counter()
    print(f"Single loop approach execution time: {end - start} seconds")

# Compare execution times
nested_loop_approach()
single_loop_approach()
