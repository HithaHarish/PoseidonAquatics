from math import comb
import sys

def find_kth_sequence(n, k):
    elements = list(range(1, n + 1))  # A = [1, 2, ..., n]
    result = []
    remaining = set(elements)  # Remaining elements in the set
    
    for i in range(1, n + 1):
        # Check if i can be part of the increasing sequence
        count = 0
        for j in sorted(remaining):
            temp_list = sorted(list(remaining - {j}), reverse=True)
            possible_sequences = comb(len(temp_list), len(remaining) - 1)
            count += possible_sequences

            if count >= k:
                result.append(j)
                remaining.remove(j)
                break
            k -= possible_sequences

        if count < k:  # Not enough sequences, means K is out of range
            return "-1"
    
    return " ".join(map(str, result))

# Input Handling
input = sys.stdin.read
data = input().split("\n")
t = int(data[0])

output = []
for i in range(1, t + 1):
    if data[i].strip():
        n, k = map(int, data[i].split())
        output.append(find_kth_sequence(n, k))

sys.stdout.write("\n".join(output) + "\n")
