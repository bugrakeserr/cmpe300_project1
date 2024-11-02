import time
import random

glob_execution_time = 0

def cmpe_algorithm(arr: list) -> int:
    global glob_execution_time
    n = len(arr)
    start_time = time.time()
    res = 1
    for i in range(n):
        if arr[i] == 'c':
            for j in range(n, 0, -1):
                k = i + n
                for y in range(0, n+1, j):
                    k = k - 1
                res = res + k
                
        elif arr[i] == 'm':
            z = 1
            while z < n:
                z = z * 2
                res = res + z

        elif arr[i] == 'p':
            w = n
            res = res - 1
            while w > 0:
                w = w // 5
                res = res + 1

        elif arr[i] == 'e':
            for m in range(1, i+1):
                p = m

                for l in range(m, n+1):
                    for t in range(n, 0, -1):
                        p = p + t
                    res = res + p
                    
    end_time = time.time()
    execution_time = end_time - start_time
    glob_execution_time += execution_time
    return res


def array_generator(scenario, size):
    arr = []
    if scenario == 'worst':
        arr.append('c')
        for i in range(size-1):
            arr.append('e')
    elif scenario == 'best':
        arr.append('e')
        for i in range(size-1):
            arr.append('p')
    else:
        letters = ["c","m","p","e"]
        probs = [1/8,1/4,1/8,1/2]
        arr = random.choices(letters,probs,k=size)
    return arr
 

# scenario = input()
# size = int(input())


# arr = array_generator(scenario, size)

# print(arr)
# cmpe_algorithm(arr)


# for j in [1, 5, 10, 20, 30, 40, 50, 60, 70, 90,
# 100, 120, 130, 140, 150, 160, 170]:
    
#     for i in range(10):
#          arr = array_generator('worst', j)
#          cmpe_algorithm(arr)
#     print(j,":: worst execution time is : " ,glob_execution_time/10)



#     glob_execution_time = 0
