import sys
sys.stdin = open("../test/num-card2.txt", 'r')
sys.setrecursionlimit(10**9)

input_1 = int(input())
num_cards = list(map(int, input().split()))
input_2 = int(input())
card_to_count = list(map(int, input().split()))


num_cards.sort()

print(num_cards)
print(card_to_count)

def binary_search2(arr, left, right, key, count):
    pl = left
    pr = right
    pc = (pl+pr) // 2
    if arr[pc] == key:
        count += 1
        count += binary_search2(arr, pl, pc-1, key, count)
        count += binary_search2(arr, pc+1, pr, key, count)
    if arr[pc] < key:
        pl = pc + 1
        count += binary_search2(arr, pl, pr, key, count)
    else:
        pr = pc - 1
        count += binary_search2(arr, pl, pr, key, count)
    if pl > pr: return count



ans_list = list()

for card in card_to_count:
    count = binary_search2(num_cards, 0, len(num_cards)-1, card, 0)
    ans_list.append(count)

str_ans = list(map(str, ans_list))
ans = " ".join(str_ans)
print(ans)