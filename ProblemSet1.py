#Problem 2
s="abcbobobobdefgbobob"
count = 0
for i in range(len(s)+1):
    if s[i:i+3] == 'bob':
        count += 1
print("Number of times bob occurs is: "+ str(count))

#Problem 3
s = 'azcbbbbbbbbbbbbbbobobeggaaaaaaaaaaakl'
answer=""
temp=""
for i in range(len(s)+1):
    for j in range(len(s)+1):
        if list(s[j:i]) == sorted(s[j:i]):
            temp = s[j:i]
            if len(temp)>len(answer):
                answer=temp
print("Longest substring in alphabetical order is:",answer)
