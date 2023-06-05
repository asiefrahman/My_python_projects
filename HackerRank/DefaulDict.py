# Source: Hackerrank.com
# Challenge: DefaultDict

import time

# Start the timer
start_time = time.time()

n, m = input().split()
# print(n, m)

A = [input() for _ in range(int(n))]
B = [input() for _ in range(int(m))]

# print(A, B)

for b in B:
    q = []
    for i in range(1, len(A)+1):
        if b in A and b == A[i-1]:
            q.append(int(i))
        else:
            # print('-1')
            continue
    # print(q)
    print(' '.join(str(item) for item in q))

elapsed_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {elapsed_time} seconds")
