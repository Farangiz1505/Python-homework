 Exercise 1: Threaded Prime Number Checker

This program checks for prime numbers in a given range using multiple threads.

import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    local_primes = []
    for number in range(start, end):
        if is_prime(number):
            local_primes.append(number)
    result.extend(local_primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result = []
    chunk_size = (end - start) // num_threads
    result_lock = threading.Lock()

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size if i != num_threads - 1 else end

        thread = threading.Thread(
            target=lambda s=chunk_start, e=chunk_end: (
                result_lock.acquire(),
                result.extend([n for n in range(s, e) if is_prime(n)]),
                result_lock.release()
            )
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted(result)

# Example usage
if __name__ == "__main__":
    start = 1
    end = 100
    primes = threaded_prime_checker(start, end, num_threads=4)
    print("Primes:", primes)


Exercise 2: Threaded File Processing (Word Counter)
This program processes a large text file and counts word occurrences using threads.

import threading
from collections import Counter
import os

def process_lines(lines, counter, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    
    with lock:
        counter.update(local_counter)

def threaded_word_count(file_path, num_threads=4):
    if not os.path.exists(file_path):
        print("File not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = len(lines) if i == num_threads - 1 else (i + 1) * chunk_size
        thread = threading.Thread(target=process_lines, args=(lines[start:end], counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return counter

# Example usage
if __name__ == "__main__":
    file_path = "sample_text.txt"  # Replace with your file path
    word_counts = threaded_word_count(file_path, num_threads=4)
    
    if word_counts:
        for word, count in word_counts.most_common(10):  # Show top 10
            print(f"{word}: {count}")
