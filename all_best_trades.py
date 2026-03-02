arr = [4, 3, 5, 7, 2, 9, 3, 1, 8]


# Trial 1 - O(N^3)
dp = [[0 for i in range(len(arr) + 1)] for j in range(len(arr) + 1)]

for diff in range(1, len(arr)):
    for i in range(diff + 1, len(arr) + 1):
        result = 0
        j = i - diff
        for k in range(diff):
            result = max(result, dp[i][i - k] + dp[i - k - 1][j])
        result = max(result, arr[i - 1] - arr[j - 1])
        dp[i][i - diff] = result

for i in dp:
    print(i)

# Trial 2 - State machine 
hold, not_hold = [0 for i in range(len(arr))], [0 for i in range(len(arr))]
hold[0] = -4
for i in range(1, len(arr)):
    hold[i] = max(hold[i - 1], not_hold[i - 1] - arr[i])
    not_hold[i] = max(not_hold[i - 1], hold[i - 1] + arr[i])
print(hold)
print(not_hold)

# Trial 3 - Max k trades
k = 2
held, sold = [-float('inf') for i in range(k + 1)], [0 for i in range(k + 1)]
# held[0] = -arr[0]
for val in arr:
    for j in range(1, k + 1):
        sold[j] = max(sold[j], held[j] + val)
        held[j] = max(held[j], sold[j - 1] - val)
print(held)
print(sold)


# Trial 4 - 1 day rest after selling
H = [-float('inf') for _ in range(len(arr))]
S = [0 for i in range(len(arr))]
R = [0 for i in range(len(arr))]

H[0] = -arr[0]
for i, val in enumerate(arr):
    if i == 0: continue
    H[i] = max(H[i - 1], R[i - 1] - val)
    R[i] = max(R[i - 1], S[i - 1])
    S[i] = H[i - 1] + val

print("One day off")
print(H)
print(R)
print(S)


# Trial 5 - O(1) space
H = -float('inf')
S = 0
R = 0
arr = [1, 2, 3, 0, 2]
H = -arr[0]
for i, val in enumerate(arr):
    if i == 0: continue
    prev_h, prev_s, prev_r = H, S, R
    H = max(prev_h, prev_r - val)
    R = max(prev_r, prev_s)
    S = prev_h + val

print("One day off")
print(H)
print(R)
print(S)
