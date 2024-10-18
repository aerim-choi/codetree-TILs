n = int(input())*2

num_list = list(map(int, input().split()))

#두개의 리스트를 각각 합을 구한 후 차를 구한다.
 
def calc(a_list,b_list):
    return abs(sum(a_list)-sum(b_list))


#두 그룹으로 나누기 (N개중에 중복 없이 N/2 뽑기)
combination_result = []
combination_idx = []
calc_answer = 10000 
def choose(curr_idx, cnt):
    global combination_idx
    global num_list
    global calc_answer
    combination1= []
    combination2 = []

    if cnt == n/2:
        
        for i in range(n):
            if i in combination_idx:
                combination1.append(num_list[i])
            else:
                combination2.append(num_list[i])
        
        calc_answer = min(calc_answer, calc(combination1,combination2))
        return
    if curr_idx==len(num_list):
        return 

    
    #선택
    combination_idx.append(curr_idx)
    choose(curr_idx+1, cnt+1)
    combination_idx.pop()
    
    #선택안함
    choose(curr_idx+1, cnt)

            
choose(0,0)
print(calc_answer)