#보석방 n
#도둑가방크기m

n, m = map(int, input().split())

crystals = []
for _ in range(n):
    w, v = map(int, input().split()) #w무게, v는보석의 가치 

    #최대 가치를 구해야함 무게가 작고 가격이 높은 보석이 가치가 있음
    crystals.append([v/w,w,v])

crystals.sort(key=lambda x:x[0], reverse=True)

worth = 0 

for crystal in crystals:
    if m==0: #가방이 꽉찼다면
        break

    if m-crystal[1]>=0: #가방에 통째로 넣을 수 있다면
        worth += crystal[2]
        m -=crystal[1]

    else: #가방에 통쨰로 넣을 수 없다면
        temp = m/crystal[1]
        worth += crystal[2] * temp
        m = m - (crystal[1]*(temp))
        
print(f'{worth:.3f}')

    
