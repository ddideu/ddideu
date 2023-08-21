first_card = int(input())
first_card_number = sorted(map(int, input().split()))
second_card = int(input())
second_card_number = list(map(int, input().split()))
card_deck = [0] * second_card
for i in range(second_card):
    start = 0
    end = first_card - 1
    ans = 0
    while start <= end:
        middle = (start+end) // 2
        if first_card_number[middle] == second_card_number[i]:
            ans = 1
            break
        elif first_card_number[middle] > second_card_number[i]:
            end = middle - 1
        elif first_card_number[middle] < second_card_number[i]:
            start = middle + 1
    card_deck[i] += ans
print(*card_deck)