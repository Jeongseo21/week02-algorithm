N = int(input())
orders = []
answer = []
for _ in range(N):
    orders.append(int(input()))

for order in orders:
    if order:
        answer.append(order)
    else:
        answer.pop()
print(sum(answer))