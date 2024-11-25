n = int(input())

words = dict()

answer = 0 
for _ in range(n):
    word_list= list(input())

    word_list = sorted(word_list)

    new_word = ''
    for s in word_list:
        new_word +=s
    
    if new_word in words:
        words[new_word]+=1
    else:
        words[new_word]=1

    answer = max(words[new_word],answer)
print(answer)