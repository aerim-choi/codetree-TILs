n = int(input())

result = 0
number_list = []
number_split=[]

#1~4조합의 n자리의 숫자 만들기
def choose_num(curr_idx):
    if curr_idx>n:
        #아름다운 수 인지 체크
        #아름다운 수라면 result+1 
        if check_beautiful_num(number_list):
            global result
            result+=1
        return 
    else:
        for i in range(1,5):
            number_list.append(str(i))
            choose_num(curr_idx+1)
            number_list.pop()
        return 

def check_beautiful_num(number_list):
    next_idx=1
    for i in range(0,n,next_idx):
        if number_list[i] == '1':
            next_idx=1
            
        elif i+1 < n and number_list[i]=='2' and number_list[i+1] == '2':
            next_idx=2
        
        elif i+2 < n and number_list[i] =='3' and number_list[i+1]=='3' and number_list[i+2]=='3':
            next_idx=3
        
        elif i+3 < n and number_list[i] =='4' and number_list[i+1]=='4' and number_list[i+2] =='4' and number_list[i+3]=='4':
            next_idx=4
        
        else:
            return False
    return True


choose_num(1)
print(result)