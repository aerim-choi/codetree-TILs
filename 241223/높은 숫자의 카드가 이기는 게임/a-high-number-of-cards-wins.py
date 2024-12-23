n = int(input())

#1부터 2n까지의 번호가 쓰인 카드가 각한장씩 총 2n장

cards = [i for i in range(1, ((n*2)+1))]

b_cards = []

for _ in range(n):
    b_card = int(input())
    cards.remove(b_card)
    b_cards.append(b_card)

answer = 0 

for i in range(n):
    if cards[i] > b_cards[i]:
        answer+=1

print(answer)
