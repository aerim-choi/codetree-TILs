n = int(input())

#1부터 2n까지의 번호가 쓰인 카드가 각한장씩 총 2n장

cards = [i for i in range(1, ((n*2)+1))]

b_cards = []

for _ in range(n):
    b_card = int(input())
    cards.remove(b_card)
    b_cards.append(b_card)

answer = 0 
b_cards = sorted(b_cards)

for i in range(n):
    if cards[i] > b_cards[i]:
        answer+=1

print(answer)

# 10
# 1 2 3  4  5  8 10 11 16 19
# 6 7 9 12 13 14 15 17 18 20