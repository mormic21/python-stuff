import multiprocessing
import math

def factorize(num):
    res = []
    i = 2
    while True:
        if num == 1:
            return res
        rest = num % i
        if rest == 0:
            res.append(i)
            num = num / i
        else:
            i = i + 1

def mp_worker(queue, numbers):
    result = {}
    for i in numbers:
        result[i] = factorize(i)
    queue.put(result)

def mp_factor(numbers, processes):
    queue = multiprocessing.Queue()
    chunks = int(math.ceil(len(numbers))/ processes)
    procs = []
    for i in range(processes):
        proc = multiprocessing.Process(target=mp_worker, args=(queue, numbers[chunks * i:chunks * (i + 1)]))
        procs.append(proc)
        proc.start()

    results = {}
    for i in range(processes):
        results.update(queue.get())

    for i in procs:
        i.join()
    return results

if __name__ == '__main__':
    res = mp_factor([42, 1337], 2)
    print(res)